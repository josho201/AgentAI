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
