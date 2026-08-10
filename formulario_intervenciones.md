# umwelt: Formulario Emergentes 2026 — Intervenciones en el espacio

Borrador para el segundo formulario en línea (rosario.gob.ar/cultura). Mismo proyecto que `formulario_nerd.md`, re-encuadrado para la categoría **Intervenciones en el espacio**: el eje pasa de "lo digital / tiempo real" a "lo espacial / la colonia habitando el galpón". Cierra el **domingo 5 de julio inclusive**.
Un formulario por formato (las bases lo exigen); el link de Drive y la bio son los mismos que en Ne:RD.

---

## Formato de presentación

Intervenciones en el espacio

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

Microcontroladores ESP32, pantallas OLED monocromas de 128×64 píxeles, sensores (micrófonos I2S, cámara térmica, telémetro láser, acelerómetros, bobinas electromagnéticas, sensor de CO2, fotorresistencias), placas perforadas, alambre de cobre estañado, imanes de neodimio, sensores de efecto Hall, cables USB textiles con alma de acero, estructura o mesa como hábitat.

### Técnicas

Electrónica artesanal a la vista (escultura de circuito), firmware propio en C++ desarrollado a partir de ingeniería inversa, visualización 1-bit en tiempo real sobre buffer de audio circular, red de radio ESP-NOW entre organismos, acople magnético con detección por efecto Hall, instalación de dispositivos manipulables sobre hábitat fijo.

### Dimensiones/duración

Colonia de 8 a 12 organismos de aprox. 10 × 8 × 6 cm cada uno, sobre un hábitat de aprox. 3 × 1 m dispuesto como isla en el galpón, adaptable a su escala y en diálogo con el equipo del CEC. Funcionamiento continuo durante todo el horario de exhibición.

### Necesidades técnicas

Una superficie o estructura (aprox. 3 × 1 m, adaptable) ubicable en el galpón y dos tomas de 220V. Todo el resto del equipamiento lo aporta el proyecto. No requiere computadoras, proyectores ni internet. Iluminación tenue: favorece la lectura de las pantallas y recorta la colonia en la penumbra de la nave.

### Descripción del proyecto (máx. 1.500 caracteres)

Toda percepción es una burbuja. El biólogo Jakob von Uexküll llamó umwelt al mundo propio de cada organismo: la garrapata vive en un mundo de tres señales, y lo demás no existe para ella. Las máquinas también viven en burbujas: su mundo es exactamente aquello que sus sensores alcanzan.

umwelt es una colonia de ocho a doce organismos electrónicos mínimos, hechos a mano y con el circuito a la vista, que habitan una porción del galpón como un pequeño territorio vivo. Cada bicho posee un único sentido: uno oye; otro siente el calor de los cuerpos; otro, la radiación de los teléfonos; otro, el aliento de la sala; otro percibe que lo alzan. No nos reconocen ni nos registran: nos sienten, como clima. Su memoria se repinta a cada instante, en un bit, y se olvida cada segundo.

La obra es una relación espacial de convivencia, no de uso. El visitante entra en el territorio de la colonia, se agacha, levanta un bicho, lo acerca a otro y sus mundos se contaminan: el que oye empieza a sentir el calor. Su propio cuerpo, que absorbe las ondas con que la colonia conversa, interfiere ese encuentro sin saberlo. La escala es deliberada: criaturas diminutas y de percepción pobre dentro de una nave enorme, que hay que buscar, rodear y atender.

Los circuitos van desnudos: cuerpos vulnerables, nada que esconder.

### Memoria descriptiva (máx. 2.500 caracteres)

La colonia se compone de 8 a 12 organismos autónomos dispuestos sobre un hábitat de mesa o estructura baja (aprox. 3 × 1 m, adaptable), pensado como una isla en el espacio del galpón: el público circula alrededor y se inclina sobre ella. La escala es parte de la obra: criaturas de 10 × 8 × 6 cm y percepción mínima dentro de una nave de gran volumen, que obligan a acercarse, buscar y bajar la mirada.

Cada organismo es una escultura de circuito a la vista (placa perforada, alambre de cobre estañado, componentes desnudos, sin carcasa), con un microcontrolador ESP32-S3, una pantalla OLED monocroma de 128×64 píxeles y un único sensor que define su sentido:

- oído: micrófono I2S
- electrosentido: bobina captora + amplificador (radiación de celulares)
- calor: cámara térmica de 8×8 píxeles
- proximidad: telémetro láser
- tacto y equilibrio: acelerómetro y antenas capacitivas
- respiración: sensor de CO2
- luz: fotorresistencias

El motor de visualización corre íntegramente en el microcontrolador, sin computadoras: la señal del sensor alimenta un buffer circular que la pantalla repinta a cada cuadro, en 1 bit. Es una reescritura propia, reconstruida por ingeniería inversa, del motor del visualizador Quantum VJ, ya operativa en un prototipo funcional.

Los organismos se sienten entre sí por radio (ESP-NOW): cada uno emite un resumen de su percepción varias veces por segundo y mezcla débilmente lo que recibe de sus vecinos, ponderado por la intensidad de señal. El acople es magnético: imanes de neodimio y sensores de efecto Hall en disposición espejada detectan la unión de dos organismos y disparan la fusión de sus percepciones; al separarlos, la influencia se desvanece. La arquitectura es en capas independientes (organismo autónomo, rumor ambiente, fusión por acople) y cada capa funciona sin las siguientes.

Montaje y ocupación del espacio: los organismos viven en nidos fijos sobre la estructura; cada uno se alimenta por un cable USB textil soldado internamente, con alma de acero anclada, así el público puede levantarlos, manipularlos y acoplarlos, pero no retirarlos. La fuente de 5V queda en una caja cerrada bajo la estructura. Sin partes móviles, sin tensiones peligrosas, sin calor: apto para manipulación directa. La obra pide poco al espacio y funciona mejor con iluminación tenue. Producción: componentes del mercado local, fabricación por tandas en 6 a 8 semanas, presupuesto dentro del estímulo con margen para repuestos. Montaje: dos personas, medio día.

### Materiales audiovisuales de referencia (link)

**COMPLETAR**: mismo link de Drive que en el formulario Ne:RD (carpeta pública única). Contenido: video del prototipo, fotos de placa, esquema del hábitat sobre la mesa, diagrama del acople, dossier conceptual en PDF y, si llega, video de dos organismos acoplándose.

*Verificar acceso público en ventana de incógnito antes de enviar.*

### Nota biográfica (máx. 1.200 caracteres) — 1.107/1.200

Manuel Rodríguez Roldán es diseñador de producto digital, formado en diseño gráfico en la Escuela Superior de Diseño de Rosario. Rosarino nacido y criado, aporta al dúo el fondo conceptual del proyecto, junto al conocimiento de cibernética, tecnología y la fabricación física de los organismos. Su interés por el posthumanismo tecnológico recorre trabajos previos como Gaze++ (instalación de vigilancia y detección sobre Raspberry Pi) y C.I.C.F.A. Umwelt nace de esa exploración.

Juan Ignacio Miles es un desarrollador, consultor tecnológico y artista audiovisual. Guiado por una curiosidad extrema hacia la electrónica y el hardware, su formación en ingeniería ambiental conecta el estudio de los ecosistemas, los fluidos y el dióxido de carbono con el diseño de estos organismos electrónicos. En el colectivo DJ Navarro, explora la música como una herramienta de interacción comunitaria. Como VJ en Las Aventuras, hackea la 'caja negra' digital combinando software con periféricos analógicos, televisores de tubo y Liquid Light, investigando cómo la tecnología y el público conviven a través del estímulo.

---

## Diferencias con el formulario Ne:RD (para no confundirlos al cargar)

- **Formato**: Intervenciones en el espacio (no Expresiones digitales).
- **Descripción y memoria**: eje espacial (habitar el galpón, escala, circulación del público) en vez de eje digital (tiempo real, generativo).
- **Materiales / técnicas / necesidades**: agregan la dimensión de instalación y ocupación del espacio.
- **Bio, link de Drive, título y datos del representante**: idénticos a Ne:RD.

## Antes de enviar (checklist)

- [x] Bios escritas y dentro de 1.200 caracteres (1.107/1.200)
- [x] Descripción y memoria dentro de límite (1.311/1.500 y 2.494/2.500)
- [ ] Link de Drive con acceso público (mismo que Ne:RD)
- [ ] Datos personales del representante
- [ ] Releer los desplegables del formulario real (formato y modalidad)
- [ ] Enviar antes del domingo 5/7 (no dejar para las 23:00)
