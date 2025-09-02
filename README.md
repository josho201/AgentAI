####


###Simple Deep Research

A ver, tengo que definir la meta final del proyecto, debe ser algo claro, mas o menos peciso, mas o menos alcanzable, etc, etc. debe ser una cosa. Una sola cosa y nada más. por ahora el uso que tiene es deep research entonces eso será.
¿que hay implementado ya? 
- un web scaper
- busqueda en google
- Guardar archivos ???

que podria ser util implementar? 

- en el tool para extraer contenido de paginas web, añadir un campo de "infomacion para extraer/preferencial", indexar el texto de la pagina y luego devolver al modelo las secciones de la pagina más utiles. Además, también ayudaria a usar menos tokens (y asi prevenir context rot) al darle al modelo, en teoria, solo información util. quiza como campo opcional del web scrapper, o como tool indibvidual? 
- guardar los reportes diectamente como rich text y no markdown tambipen seria algo bastabte util 
- La directiva completa del prompt también me parece algo que hay que cambiar porque me parece demamsiado rigida, google-> scrap sin interar en ese ciclo, probablemente deberia haber un par de rondas de abstracción despues de tener el resultado dado por google
# Simple Deep Research

**Simple Deep Research** es una herramienta ligera de investigación automatizada construida con [qwen-agent](https://github.com/QwenLM/qwen-agent).  
Su objetivo es asistir en procesos de **deep research** mediante un ciclo de búsqueda, extracción, organización e integración de información.

---

## ✨ Capacidades principales

- **Búsqueda en Google**
  - Generación automática de queries a partir de la necesidad de investigación.
  - Iteración de consultas para obtener resultados más específicos.

- **Extracción de contenido web**
  - Web scraper integrado.
  - Posibilidad de definir *información preferencial* (ej: "extraer estadísticas", "extraer definiciones").
  - Indexación del contenido en fragmentos relevantes para reducir consumo de tokens.
  - Selección de secciones más útiles para el modelo.

- **Gestión de memoria del proyecto**
  - Almacenamiento de hallazgos en archivos persistentes.
  - Base de conocimiento incremental para evitar duplicar búsquedas.
  - Posibilidad de consultar qué información ya fue recolectada en runs previos.

- **Procesamiento iterativo**
  - Ciclo de reflexión + acción: el agente decide si debe realizar más búsquedas o si ya puede producir un reporte.
  - Máximo configurable de rondas de iteración.

- **Generación de reportes enriquecidos**
  - Exportación a **Rich Text (RTF)** o **HTML**, con soporte básico para Markdown.
  - Inclusión de secciones jerárquicas:
    - Hechos crudos
    - Resúmenes analíticos
    - Conclusiones / hipótesis
  - Referencias con URLs a las fuentes utilizadas.

- **Control del nivel de abstracción**
  - El usuario puede especificar el nivel de profundidad del reporte:
    - Nivel 1 → Datos crudos.
    - Nivel 2 → Síntesis y análisis.
    - Nivel 3 → Conclusiones, hipótesis y conexiones.


---

## 🚀 Uso básico

1. Define un **tema de investigación**.
2. Lanza el agente con una query inicial.
3. El sistema:
   - Busca en Google.
   - Extrae y procesa páginas relevantes.
   - Itera según necesidad.
   - Genera un reporte enriquecido.
4. Consulta el resultado en la carpeta `research_outputs`.

---

## 🔮 Roadmap

- [ ] Integración con PDFs y documentos locales.  
- [ ] Soporte para exportar a DOCX y LaTeX.  
- [ ] Panel web interactivo para gestión de investigaciones.  
