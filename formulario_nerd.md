# umwelt: Formulario Emergentes 2026

Borrador para el formulario en línea (rosario.gob.ar/cultura). Cierra el **domingo 5 de julio inclusive**.
Cada campo respeta el límite de caracteres de las bases. Lo marcado **COMPLETAR** va por cuenta nuestra antes de enviar.

---

## Formato de presentación

Expresiones digitales (Festival Ne:RD)

## Modalidad del proyecto

Colectiva (dúo). *Elegir la opción equivalente del desplegable.*

## Datos personales del representante

- Nombre/s: **COMPLETAR**
- Apellido/s: **COMPLETAR**
- Tipo y n° de documento: **COMPLETAR**
- Fecha de nacimiento: **COMPLETAR**
- ¿Reside en Rosario?: **COMPLETAR**
- Teléfono de contacto: **COMPLETAR**
- Correo electrónico: **COMPLETAR**

---

## Proyecto

### Título del proyecto/obra

umwelt

### Año de realización

2026 (en desarrollo: prototipo funcional; producción de la colonia completa tras la selección)

### Materiales

Microcontroladores ESP32, pantallas OLED monocromas de 128×64 píxeles, sensores (micrófonos I2S, cámara térmica, telémetro láser, acelerómetros, bobinas electromagnéticas, sensor de CO2, fotorresistencias), placas perforadas, alambre de cobre estañado, imanes de neodimio, sensores de efecto Hall, cables USB textiles con alma de acero.

### Técnicas

Electrónica artesanal a la vista (escultura de circuito), firmware propio en C++ desarrollado a partir de ingeniería inversa, visualización 1-bit en tiempo real sobre buffer de audio circular, red de radio ESP-NOW entre organismos, acople magnético con detección por efecto Hall.

### Dimensiones/duración

Colonia de 8 a 12 organismos de aprox. 10 × 8 × 6 cm cada uno, dispuestos sobre un hábitat de aprox. 3 × 1 m (adaptable al espacio disponible). Funcionamiento continuo durante todo el horario del festival.

### Necesidades técnicas

Una mesa o superficie equivalente (aprox. 3 × 1 m, adaptable) y dos tomas de 220V. Todo el resto del equipamiento lo aporta el proyecto. No requiere computadoras, proyectores ni red de internet. Iluminación tenue favorece la lectura de las pantallas.

### Descripción del proyecto (máx. 1.500 caracteres)

Toda percepción es una burbuja. El biólogo Jakob von Uexküll llamó *umwelt* al mundo propio de cada organismo: la garrapata vive en un mundo de tres señales: el ácido butírico, la tibieza, la piel. Lo demás no existe para ella. Las máquinas también viven en burbujas: su mundo es exactamente aquello que sus sensores alcanzan.

Vivimos dentro de una percepción maquínica planetaria, hecha de cámaras, micrófonos y antenas, que nos siente sin cesar y que no podemos sentir, y que percibe para clasificar y extraer. umwelt le responde en escala doméstica: una colonia de bichos electrónicos (*critters*, diría Donna Haraway: especies compañeras), cada uno con un único sentido. Uno oye. Otro siente el calor de los cuerpos. Otro, la radiación de los teléfonos; otro, el aliento de la sala; otro percibe que lo alzan. No nos reconocen ni nos registran: nos sienten, como clima. Su memoria se repinta a cada instante, en un bit: perciben sin identificar, recuerdan un segundo, olvidan.

Los bichos también se sienten entre sí. Al acercarlos, sus mundos se contaminan: el que oye empieza a sentir el calor; el que siente el calor, a oír. Los cuerpos del público, que absorben las ondas con que la colonia conversa, interfieren ese encuentro sin saberlo.

Los circuitos van desnudos: cuerpos vulnerables, nada que esconder. El motor nació de leer por dentro, durante meses, un visualizador ajeno (Quantum VJ, de Alexander Zolotov) hasta entenderlo. Atender a una máquina también es una forma de cuidado.

### Memoria descriptiva (máx. 2.500 caracteres)

La colonia se compone de 8 a 12 organismos autónomos. Cada uno es una escultura de circuito a la vista: placa perforada, alambre de cobre estañado, componentes desnudos, sin carcasa. Por organismo: un microcontrolador ESP32-S3 en formato mini, una pantalla OLED monocroma de 128×64 píxeles y un único sensor que define su sentido:

- oído: micrófono I2S
- electrosentido: bobina captora + amplificador (radiación de celulares)
- calor: cámara térmica de 8×8 píxeles
- proximidad: telémetro láser
- tacto y equilibrio: acelerómetro y antenas capacitivas
- respiración: sensor de CO2
- luz: fotorresistencias

El motor de visualización corre íntegramente en el microcontrolador, sin computadoras: la señal del sensor alimenta un buffer circular de 1024 muestras que se repinta en pantalla a cada cuadro, en 1 bit. Es una reescritura propia, reconstruida por ingeniería inversa, del motor del visualizador Quantum VJ, ya operativa en un prototipo funcional.

Red y acople: los organismos emiten por radio (ESP-NOW) un resumen de su percepción varias veces por segundo; cada uno mezcla débilmente lo que recibe de sus vecinos, ponderado por la intensidad de señal. El acople es magnético: imanes de neodimio y sensores de efecto Hall en disposición espejada detectan la unión de dos organismos y disparan la fusión total de sus percepciones; al separarlos, la influencia se desvanece gradualmente. La arquitectura es en capas independientes (organismo autónomo, rumor ambiente por radio, fusión por acople) y cada capa funciona sin las siguientes: la interacción puede ajustarse durante la producción sin comprometer el núcleo de la obra.

Hábitat y montaje: los organismos viven en nidos fijos sobre una mesa o estructura (aprox. 3 × 1 m, adaptable al espacio y en diálogo con el equipo del festival). Cada uno se alimenta por un cable USB textil soldado internamente, con alma de acero anclada a la estructura: el público puede levantarlos, manipularlos y acoplarlos, pero no retirarlos. La fuente de 5V queda en una caja cerrada bajo la estructura. Sin partes móviles, sin tensiones peligrosas, sin calor: apto para manipulación directa del público.

Producción: componentes estándar disponibles en el mercado local, fabricación por tandas en 6 a 8 semanas, presupuesto dentro del estímulo previsto con margen para repuestos. Montaje: dos personas, medio día. Requerimientos al espacio: una mesa o superficie equivalente y dos tomas de 220V.

### Materiales audiovisuales de referencia (link)

**COMPLETAR**: carpeta pública de Drive con:

1. Video del prototipo actual reaccionando a voz/música (1-2 min, primer plano de pantalla + plano del dispositivo entero)
2. Fotos del prototipo (placa a la vista)
3. Esquema del hábitat: la colonia sobre la mesa, nidos y cables, público alrededor (puede ser dibujo escaneado)
4. Diagrama del gesto de acople: dos organismos uniéndose por imanes y fusionando percepciones
5. Si llega: video de dos organismos acoplándose (prototipo del acople)
6. Dossier conceptual en PDF (statement extendido + bibliografía): borrador listo en `umwelt_dossier.md`, convertir a PDF tras revisión

*Verificar que la carpeta tenga acceso público antes de enviar: material que no abre no se evalúa.*

### Nota biográfica (máx. 1.200 caracteres) — 1.107/1.200

Manuel Rodríguez Roldán es diseñador de producto digital, formado en diseño gráfico en la Escuela Superior de Diseño de Rosario. Rosarino nacido y criado, aporta al dúo el fondo conceptual del proyecto, junto al conocimiento de cibernética, tecnología y la fabricación física de los organismos. Su interés por el posthumanismo tecnológico recorre trabajos previos como Gaze++ (instalación de vigilancia y detección sobre Raspberry Pi) y C.I.C.F.A. Umwelt nace de esa exploración.

Juan Ignacio Miles es un desarrollador, consultor tecnológico y artista audiovisual. Guiado por una curiosidad extrema hacia la electrónica y el hardware, su formación en ingeniería ambiental conecta el estudio de los ecosistemas, los fluidos y el dióxido de carbono con el diseño de estos organismos electrónicos. En el colectivo DJ Navarro, explora la música como una herramienta de interacción comunitaria. Como VJ en Las Aventuras, hackea la 'caja negra' digital combinando software con periféricos analógicos, televisores de tubo y Liquid Light, investigando cómo la tecnología y el público conviven a través del estímulo.

---

## Antes de enviar (checklist)

- [x] Bios escritas y dentro de 1.200 caracteres (1.107/1.200)
- [ ] Link de Drive con acceso público probado en ventana de incógnito
- [ ] Datos personales del representante
- [ ] Releer los desplegables del formulario real (modalidad) y ajustar
- [ ] Enviar antes del domingo 5/7 (no dejar para las 23:00)
