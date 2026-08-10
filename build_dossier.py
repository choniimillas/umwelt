# -*- coding: utf-8 -*-
"""Genera el dossier PDF de umwelt desde umwelt_dossier.md + secciones nuevas."""
import re, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, PageBreak, Flowable, KeepTogether)

BASE = os.path.dirname(os.path.abspath(__file__)) if "__file__" in locals() else os.getcwd()
SRC  = os.path.join(BASE, "umwelt_dossier.md")
OUT  = os.path.join(BASE, "umwelt_dossier.pdf")

INK   = HexColor("#1a1a1a")
MUTE  = HexColor("#6b6b6b")
FAINT = HexColor("#9a9a9a")
BOXBG = HexColor("#f2f1ee")
BOXLN = HexColor("#b8b4ac")
RULE  = HexColor("#c9c5bd")

# ---------- sanitizado y markdown inline ----------
def sanitize(s):
    repl = {"—":"-", "–":"-", "…":"...", "“":'"', "”":'"',
            "‘":"'", "’":"'", "→":"->", "≡":"=", "≥":">=",
            " ":" "}
    for k,v in repl.items():
        s = s.replace(k,v)
    return s

def inline(s):
    s = sanitize(s)
    s = s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    return s

# ---------- parseo del markdown fuente ----------
raw = open(SRC, encoding="utf-8").read().splitlines()
sections, cur = {}, None
for line in raw:
    m = re.match(r"^##\s+(.*)", line)
    if m:
        cur = m.group(1).strip()
        sections[cur] = []
    elif cur is not None:
        sections[cur].append(line)

def paras(key):
    return [l.strip() for l in sections.get(key, []) if l.strip() and not l.strip().startswith("-")]
def items(key):
    return [l.strip()[2:].strip() for l in sections.get(key, []) if l.strip().startswith("- ")]

statement_key = next(k for k in sections if k.lower().startswith("statement"))
colonia_key   = next(k for k in sections if "colonia" in k.lower())
biblio_key    = next(k for k in sections if "bibliograf" in k.lower())

statement_paras = paras(statement_key)
colonia_items   = items(colonia_key)
colonia_tail    = paras(colonia_key)          # parrafo de cierre tras la lista
biblio_items    = items(biblio_key)

# ---------- estilos ----------
body = ParagraphStyle("body", fontName="Times-Roman", fontSize=10.5, leading=15.5,
                      textColor=INK, alignment=TA_JUSTIFY, spaceAfter=8)
lead = ParagraphStyle("lead", parent=body, fontSize=11, leading=16, spaceAfter=9)
h2   = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, leading=14,
                      textColor=INK, spaceBefore=6, spaceAfter=9,
                      tracking=1)
kicker = ParagraphStyle("kicker", fontName="Helvetica-Bold", fontSize=7.5, leading=10,
                        textColor=FAINT, spaceAfter=2)
li   = ParagraphStyle("li", parent=body, leftIndent=12, spaceAfter=4, alignment=TA_LEFT)
bib  = ParagraphStyle("bib", parent=body, fontSize=9, leading=13, leftIndent=12,
                      firstLineIndent=-12, spaceAfter=3, alignment=TA_LEFT)
# portada
t_title = ParagraphStyle("t_title", fontName="Helvetica-Bold", fontSize=52, leading=54,
                         textColor=INK, alignment=TA_LEFT)
t_pos = ParagraphStyle("t_pos", fontName="Times-Italic", fontSize=11, leading=15,
                       textColor=MUTE, alignment=TA_LEFT, spaceBefore=4)
t_def = ParagraphStyle("t_def", fontName="Times-Roman", fontSize=11.5, leading=17.5,
                       textColor=INK, alignment=TA_LEFT)
t_foot = ParagraphStyle("t_foot", fontName="Helvetica", fontSize=8.5, leading=12,
                        textColor=MUTE, alignment=TA_LEFT)

# ---------- flowables custom ----------
class HRule(Flowable):
    def __init__(self, w=None, color=RULE, thick=0.6, pad=0):
        super().__init__(); self.w=w; self.color=color; self.thick=thick; self.pad=pad
    def wrap(self, aw, ah):
        self.aw = self.w or aw; return (self.aw, self.thick+self.pad)
    def draw(self):
        self.canv.setStrokeColor(self.color); self.canv.setLineWidth(self.thick)
        self.canv.line(0, self.pad, self.aw, self.pad)

class WIPBox(Flowable):
    def __init__(self, title, sub, height=120):
        super().__init__(); self.title=title; self.sub=sub; self.height=height
    def wrap(self, aw, ah):
        self.width = aw; return (aw, self.height)
    def draw(self):
        c=self.canv; c.saveState()
        c.setFillColor(BOXBG); c.rect(0,0,self.width,self.height,fill=1,stroke=0)
        c.setStrokeColor(BOXLN); c.setLineWidth(1); c.setDash(4,3)
        c.rect(1,1,self.width-2,self.height-2,fill=0,stroke=1)
        c.setDash()
        c.setFillColor(FAINT)
        c.setFont("Helvetica-Bold",9)
        c.drawCentredString(self.width/2, self.height/2+6, self.title)
        c.setFont("Helvetica-Oblique",8)
        c.drawCentredString(self.width/2, self.height/2-9, self.sub)
        c.restoreState()

def wip(title, sub, h=120):
    return WIPBox("[ "+title+" ]", sub, h)

# --- captions con prompt / nota de captura debajo de cada recuadro ---
cap_note = ParagraphStyle("cap_note", fontName="Helvetica", fontSize=7.3, leading=10,
                          textColor=MUTE, leftIndent=2, spaceBefore=2, spaceAfter=2,
                          alignment=TA_LEFT)

def _esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

_LBL = {"ai":"Prompt IA sugerido", "real":"Material real a capturar", "have":"Ya disponible"}

def wipblock(title, sub, h, kind, note):
    label = _LBL[kind]
    txt = ("<font name='Helvetica-Bold'>"+label+":</font> "
           "<font name='Courier'>"+_esc(note)+"</font>")
    return [wip(title, sub, h), Spacer(1, 2*mm), Paragraph(txt, cap_note), Spacer(1, 3*mm)]

def imageblock(filename, max_h, caption_text):
    filepath = os.path.join(BASE, filename)
    if not os.path.exists(filepath):
        print("Warning: image not found, falling back to placeholder:", filepath)
        return wipblock(filename, "Placeholder (archivo no encontrado)", max_h, "real", filename)
    
    from PIL import Image as PILImage
    from reportlab.platypus import Image as RLImage
    
    img = PILImage.open(filepath)
    w, h = img.size
    aspect = w / h
    
    max_w = PAGE_W - LM - RM
    target_w = max_w
    target_h = target_w / aspect
    
    if target_h > max_h:
        target_h = max_h
        target_w = target_h * aspect
        
    rl_img = RLImage(filepath, width=target_w, height=target_h)
    rl_img.hAlign = 'CENTER'
    
    flows = [rl_img]
    if caption_text:
        cap_style = ParagraphStyle(
            "cap_style",
            fontName="Helvetica-Oblique",
            fontSize=7.5,
            leading=10,
            textColor=MUTE,
            spaceBefore=3,
            spaceAfter=4,
            alignment=TA_CENTER
        )
        flows.append(Paragraph(caption_text, cap_style))
    else:
        flows.append(Spacer(1, 3*mm))
    return flows

# --- prompts de imagen (ingles: mejor adherencia de los modelos) ---
PROMPT_HABITAT = ("Architectural technical line drawing, thin precise vector linework, blue outlines "
"on a plain white background with a few magenta accent lines. One-point / isometric perspective of a "
"gallery hall. A long low table holds a colony of small handmade electronic creatures (circuit "
"sculptures: perfboard, exposed components, small rectangular OLED screens) drawn as clean wireframe "
"contour outlines, not shaded, not colored. Thin single-line cables run from the creatures down to a "
"box under the table. A few human visitors as flat grey silhouettes, leaning in for scale. Subtle "
"dotted texture on the floor. CAD / blueprint / SketchUp line-export aesthetic, high detail, no fills, "
"no rendering, no text. --ar 16:9")

PROMPT_SENTIDOS = ("Architectural technical line drawing, thin precise vector linework, blue outlines "
"on plain white background with a few magenta accent lines, CAD / blueprint aesthetic (same style as "
"the habitat drawing). A neat row/grid of seven small handmade electronic creatures, one per sense, "
"each a clean wireframe contour outline (not shaded, not colored, not photographic): a COMPACT boxy "
"rectangular PCB, roughly as wide as it is tall like a small handheld module, NOT elongated or "
"stretched, with a small rectangular OLED screen at the top and exposed components. Each board shows "
"one sense organ prominently with a small magenta label: electret microphone (hearing); copper coil "
"antenna (phone radiation); small thermal camera module (heat); laser rangefinder VL53L0X "
"(proximity); capacitive antenna wires + IMU chip (touch and balance); CO2 sensor module (breath); "
"photoresistor (light). Consistent line weight, no fills, no rendering, no text beyond tiny labels.")

PROMPT_ACOPLE = ("Architectural technical line drawing, thin blue vector linework on white with magenta "
"accents, CAD / blueprint aesthetic. Two small handmade electronic creatures shown as FLAT compact "
"rectangular circuit-sculpture boards (perfboard bodies with exposed components and wiring, NOT round, "
"NOT spherical blobs, NOT brain-like balls), placed face to face in three-quarter view. Their mirrored "
"circular magnetic coupling faces meet at the center; simple concentric magenta arcs between them "
"indicate a radio link and merging signal. Clean wireframe contour outlines, consistent line weight, "
"no fills, no shading, no text.")

PROMPT_ATM_NATURAL = ("Architectural technical line drawing, thin precise vector linework, blue outlines "
"on plain white background with a few magenta accent lines, CAD / blueprint aesthetic (same style as "
"the habitat drawing). Isometric view of a long low table whose surface is a bed of moss, soil, small "
"ferns and plants drawn as fine line contours. A colony of small handmade electronic creatures "
"(compact rectangular circuit-sculpture boards with small OLED screens and exposed components) nestled "
"among the vegetation like animals in a garden. Thin single-line cables. A couple of human visitors as "
"flat grey silhouettes for scale. Discarded concept variant: nature habitat. No fills, no shading, no "
"text. --ar 16:9")

PROMPT_ATM_SCRAP = ("Architectural technical line drawing, thin precise vector linework, blue outlines on "
"plain white background with a few magenta accent lines, CAD / blueprint aesthetic (same style as the "
"habitat drawing). Isometric view of a long low table piled with electronic scrap and e-waste (old "
"keyboards, broken circuit boards, tangled cables, connectors) drawn as fine line contours. A colony of "
"small handmade electronic creatures (compact rectangular circuit-sculpture boards with small OLED "
"screens and exposed components) perched among the scrap like scavengers in their habitat. Thin "
"single-line cables. A couple of human visitors as flat grey silhouettes for scale. Discarded concept "
"variant: e-waste habitat. No fills, no shading, no text. --ar 16:9")

# ---------- documento ----------
PAGE_W, PAGE_H = A4
LM, RM, TM, BM = 26*mm, 26*mm, 24*mm, 22*mm

def on_content(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 7.5); canv.setFillColor(FAINT)
    canv.drawString(LM, 12*mm, "umwelt  ·  dossier conceptual")
    canv.drawRightString(PAGE_W-RM, 12*mm, str(doc.page-1))
    canv.restoreState()

def on_cover(canv, doc):
    pass

story = []
# ---- PORTADA ----
story.append(Spacer(1, 46*mm))
story.append(Paragraph("umwelt", t_title))
story.append(Paragraph("sustantivo &nbsp;·&nbsp; del alem&aacute;n, <i>mundo circundante</i>", t_pos))
story.append(Spacer(1, 9*mm))
story.append(HRule(w=52*mm, color=INK, thick=1.1))
story.append(Spacer(1, 7*mm))
definicion = ("<b>Biol.</b> T&eacute;rmino de Jakob von Uexk&uuml;ll (1934). El mundo propio de un "
    "organismo: no el entorno objetivo, sino la porci&oacute;n de realidad que sus &oacute;rganos "
    "sensoriales recortan y a la que puede responder. Cada especie habita un <i>umwelt</i> distinto. "
    "Lo que sus sentidos no alcanzan, para ella no existe.")
story.append(Paragraph(definicion, t_def))
story.append(Spacer(1, 60*mm))
story.append(HRule(w=None, color=RULE, thick=0.6))
story.append(Spacer(1, 3*mm))
story.append(Paragraph("Colonia de organismos electr&oacute;nicos sensoriales", t_foot))
story.append(Paragraph("Manuel Rodr&iacute;guez Rold&aacute;n &nbsp;·&nbsp; Juan Ignacio Miles &nbsp;·&nbsp; Rosario, 2026", t_foot))
story.append(Paragraph("Material complementario · Emergentes 2026 (CEC Rosario)", t_foot))
story.append(PageBreak())

def section(kicker_txt, title, flows):
    blk = [Paragraph(kicker_txt, kicker), Paragraph(title, h2)]
    blk += flows
    return blk

# ---- STATEMENT ----
story += [Paragraph("01", kicker), Paragraph("Statement", h2)]
for i,p in enumerate(statement_paras):
    story.append(Paragraph(inline(p), lead if i==0 else body))
story.append(Spacer(1, 4*mm))

# ---- LA COLONIA ----
story.append(HRule(color=RULE)); story.append(Spacer(1,4*mm))
story += [Paragraph("02", kicker), Paragraph("La colonia: los sentidos", h2)]
for it in colonia_items:
    story.append(Paragraph("&bull;&nbsp; "+inline(it), li))
for p in colonia_tail:
    story.append(Spacer(1,2*mm)); story.append(Paragraph(inline(p), body))
story.append(Spacer(1,4*mm))
story += imageblock("05_sentidos/sentidos.png", 150, "Retratos de los siete sentidos de la colonia")

# ---- HABITAT ----
story.append(PageBreak())
story += [Paragraph("03", kicker), Paragraph("El h&aacute;bitat", h2)]
hab = ("Los bichos viven en nidos fijos sobre una mesa (aprox. 3 &times; 1 m, adaptable al espacio). "
    "El p&uacute;blico puede levantarlos, manipularlos y acoplarlos, pero no retirarlos: cada uno se "
    "alimenta por un cable USB textil anclado a la estructura. El h&aacute;bitat es sobrio a "
    "prop&oacute;sito, para que el cuerpo t&eacute;cnico del bicho, el circuito a la vista, quede "
    "en primer plano.")
story.append(Paragraph(hab, body))
story.append(Spacer(1,3*mm))
story += imageblock("03_habitat/render_mesa_nidos.png", 240, "Render del hábitat (vista principal)")
story.append(Spacer(1,2*mm))
story += imageblock("03_habitat/atmosferas_descartadas/atmosferas_descartadas.png", 120, "Atmósferas exploradas y descartadas (jardín de musgo / chatarra electrónica)")

# ---- ACOPLE ----
story.append(PageBreak())
story += [Paragraph("04", kicker), Paragraph("El acople", h2)]
aco = ("Cada bicho emite por radio un murmullo con el resumen de su percepci&oacute;n; los dem&aacute;s "
    "lo incorporan d&eacute;bilmente, ponderado por la cercan&iacute;a. Al acoplar dos bichos por sus "
    "caras magn&eacute;ticas, unos sensores de efecto Hall detectan la uni&oacute;n y disparan la "
    "fusi&oacute;n total de sus percepciones: el que oye empieza a sentir el calor; el que siente el "
    "calor, a o&iacute;r. Al separarlos, la influencia se desvanece de a poco. Los cuerpos del "
    "p&uacute;blico, que absorben las ondas con que la colonia conversa, interfieren ese encuentro "
    "sin saberlo.")
story.append(Paragraph(aco, body))
story.append(Spacer(1,3*mm))
story += imageblock("04_acople/acople.png", 180, "Diagrama del acople magnético y de radio entre organismos")

# ---- PROTOTIPO ----
story.append(PageBreak())
story += [Paragraph("05", kicker), Paragraph("El prototipo", h2)]
pro = ("El motor gr&aacute;fico ya corre en un prototipo funcional: la se&ntilde;al del sensor alimenta "
    "un buffer circular que la pantalla repinta a cada cuadro, en un bit. Las im&aacute;genes muestran "
    "el dispositivo actual reaccionando a la voz y la m&uacute;sica de la sala.")
story.append(Paragraph(pro, body))
story.append(Spacer(1,3*mm))
story += wipblock("fotos y video del prototipo", "placa a la vista + pantalla 1-bit en movimiento", 140,
                  "real", "Foto/video del prototipo actual: primer plano de la placa desnuda con buena luz + la pantalla OLED reaccionando a voz/musica. Fondo neutro.")

# ---- PROCESO RE ----
story.append(Spacer(1,5*mm))
story.append(HRule(color=RULE)); story.append(Spacer(1,4*mm))
story += [Paragraph("06", kicker), Paragraph("Proceso: ingenier&iacute;a inversa del Quantum VJ", h2)]
rev = ("El motor de visualizaci&oacute;n no es un software adoptado sino comprendido. Naci&oacute; de "
    "meses de ingenier&iacute;a inversa del visualizador Quantum VJ, de Alexander Zolotov, le&iacute;do "
    "instrucci&oacute;n por instrucci&oacute;n hasta reconstruirlo como firmware propio para "
    "microcontrolador. Atender a una m&aacute;quina hasta entenderla tambi&eacute;n es una forma de "
    "cuidado.")
story.append(Paragraph(rev, body))
story.append(Spacer(1,3*mm))
story += wipblock("captura del desensamblado", "bytecode original del QVJ junto al firmware propio", 88,
                  "real", "Captura de pantalla del desensamblador (research/pixicode_dis.py) mostrando el bytecode, junto a un fragmento del firmware propio (umwelt_v0.2).")

# ---- EL DUO ----
story.append(PageBreak())
story += [Paragraph("07", kicker), Paragraph("El d&uacute;o", h2)]
bio_m = ("<b>Manuel Rodr&iacute;guez Rold&aacute;n</b> es dise&ntilde;ador de producto digital, formado en "
    "dise&ntilde;o gr&aacute;fico en la Escuela Superior de Dise&ntilde;o de Rosario. Rosarino nacido y "
    "criado, aporta al d&uacute;o el fondo conceptual del proyecto, junto al conocimiento de "
    "cibern&eacute;tica, tecnolog&iacute;a y la fabricaci&oacute;n f&iacute;sica de los organismos. Su "
    "inter&eacute;s por el posthumanismo tecnol&oacute;gico recorre trabajos previos como Gaze++ "
    "(instalaci&oacute;n de vigilancia y detecci&oacute;n sobre Raspberry Pi) y C.I.C.F.A. umwelt nace "
    "de esa exploraci&oacute;n.")
bio_j = ("<b>Juan Ignacio Miles</b> es un desarrollador, consultor tecnol&oacute;gico y artista "
    "audiovisual. Guiado por una curiosidad extrema hacia la electr&oacute;nica y el hardware, su "
    "formaci&oacute;n en ingenier&iacute;a ambiental conecta el estudio de los ecosistemas, los fluidos "
    "y el di&oacute;xido de carbono con el dise&ntilde;o de estos organismos electr&oacute;nicos. En el "
    "colectivo DJ Navarro, explora la m&uacute;sica como una herramienta de interacci&oacute;n "
    "comunitaria. Como VJ en Las Aventuras, hackea la 'caja negra' digital combinando software con "
    "perif&eacute;ricos anal&oacute;gicos, televisores de tubo y Liquid Light, investigando c&oacute;mo "
    "la tecnolog&iacute;a y el p&uacute;blico conviven a trav&eacute;s del est&iacute;mulo.")
story.append(Paragraph(bio_m, body)); story.append(Spacer(1,2*mm))
story.append(Paragraph(bio_j, body))

# ---- BIBLIOGRAFIA ----
story.append(Spacer(1,5*mm))
story.append(HRule(color=RULE)); story.append(Spacer(1,4*mm))
story += [Paragraph("08", kicker), Paragraph("Bibliograf&iacute;a", h2)]
for it in biblio_items:
    story.append(Paragraph(inline(it), bib))

# ---------- build ----------
doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=LM, rightMargin=RM,
                      topMargin=TM, bottomMargin=BM, title="umwelt - dossier conceptual",
                      author="Manuel Rodriguez Roldan, Juan Ignacio Miles")
frame = Frame(LM, BM, PAGE_W-LM-RM, PAGE_H-TM-BM, id="main")
doc.addPageTemplates([
    PageTemplate(id="cover", frames=[frame], onPage=on_cover),
    PageTemplate(id="content", frames=[frame], onPage=on_content),
])
# primera pagina usa cover; forzamos cambio tras el primer PageBreak
from reportlab.platypus import NextPageTemplate
story2 = [NextPageTemplate("content")] + story
doc.build(story2)
print("OK ->", OUT)

# Copy to 01_dossier/umwelt_dossier.pdf
dossier_dir = os.path.join(BASE, "01_dossier")
os.makedirs(dossier_dir, exist_ok=True)
import shutil
shutil.copy2(OUT, os.path.join(dossier_dir, "umwelt_dossier.pdf"))
print("Copied PDF to:", os.path.join(dossier_dir, "umwelt_dossier.pdf"))

print("statement paras:", len(statement_paras), "| colonia items:", len(colonia_items),
      "| biblio items:", len(biblio_items))
