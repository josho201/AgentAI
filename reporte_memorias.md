**Reporte Técnico: Tipos de Memorias en Sistemas Computacionales**  
*Fecha de elaboración: 23 de agosto de 2025*  

---

### **Introducción**  
Las memorias son componentes críticos en sistemas computacionales, clasificadas según su volatilidad, capacidad de escritura y aplicaciones. Este reporte analiza cinco tipos clave: **RAM**, **ROM**, **EPROM**, **EEPROM** y **FLASH**, basado en fuentes técnicas verificadas.  

---

### **Explicaciones Técnicas**  

#### **1. RAM (Random Access Memory)**  
- **Definición**: Memoria volátil de acceso aleatorio utilizada para almacenar datos temporalmente durante la ejecución de programas. Pierde su contenido al desconectar la energía.  
- **Características clave**:  
  - Alta velocidad de lectura/escritura.  
  - Subtipos: **DRAM** (más lenta, económica, usada en memoria principal) y **SRAM** (más rápida, costosa, usada en caché).  
  - *Ejemplo de aplicación*: Almacenamiento temporal de procesos activos en sistemas operativos.  
- **Fuente**:  
  > *"RAM is volatile, meaning it loses its data when power is turned off. It allows the CPU to quickly access data that is actively being used."*  
  **(Vemeko, "Ultimate Guide to Memory Types", 2024)**  

#### **2. ROM (Read-Only Memory)**  
- **Definición**: Memoria no volátil programada en fábrica, diseñada para solo lectura. Almacena instrucciones críticas (ej.: firmware de arranque).  
- **Características clave**:  
  - Datos permanentes, incluso sin energía.  
  - No reprogramable (en su forma estándar, conocida como *Mask ROM*).  
  - *Ejemplo de aplicación*: BIOS de computadoras antiguas.  
- **Fuente**:  
  > *"ROM is a kind of computer memory that you can only read from, not write to. This means once you put information in ROM, you can't change it. ROM keeps the information even when you turn off the computer."*  
  **(GeeksforGeeks, "Difference between EPROM and EEPROM", 2025)**  

#### **3. EPROM (Erasable Programmable Read-Only Memory)**  
- **Definición**: Variante reprogramable de ROM, borrada mediante luz ultravioleta (UV).  
- **Características clave**:  
  - Reutilizable (hasta ~1,000 ciclos).  
  - Tiempo de borrado lento (~20 minutos bajo luz UV).  
  - *Ejemplo de aplicación*: Firmware en dispositivos embebidos antiguos.  
- **Fuente**:  
  > *"EPROM is erased using a special UV light. You need to leave your notebook in the sun to erase it instead of just using an eraser."*  
  **(GeeksforGeeks, "Difference between EPROM and EEPROM", 2025)**  

#### **4. EEPROM (Electrically Erasable Programmable Read-Only Memory)**  
- **Definición**: Memoria no volátil reprogramable eléctricamente, con borrado a nivel de byte.  
- **Características clave**:  
  - Borrado/escritura sin remover el chip.  
  - Mayor durabilidad (~100,000 ciclos) pero velocidad de escritura lenta.  
  - *Ejemplo de aplicación*: Almacenamiento de configuraciones en BIOS modernas.  
- **Fuente**:  
  > *"In EEPROM, electric signal is used to erase the contents. You can change small parts without erasing everything, like rewriting one sentence in a book."*  
  **(GeeksforGeeks, "Difference between EPROM and EEPROM", 2025)**  

#### **5. FLASH**  
- **Definición**: Subtipo de EEPROM que borra datos en bloques (no a nivel de byte), optimizado para alta densidad y velocidad.  
- **Características clave**:  
  - Dos variantes: **NOR** (acceso aleatorio rápido, para ejecución de código) y **NAND** (alta capacidad, para almacenamiento masivo).  
  - *Ejemplo de aplicación*: Unidades SSD, memorias USB y tarjetas SD.  
- **Fuente**:  
  > *"Flash memory is an electronic non-volatile storage medium that can be electrically erased and reprogrammed. NAND flash is used in SSDs and USB drives due to its cost-effective, high-capacity storage."*  
  **(Wikipedia, "Flash memory", 2025)**  

---

### **Tabla Comparativa**  

| **Característica**       | **RAM**               | **ROM**               | **EPROM**             | **EEPROM**            | **FLASH**             |
|--------------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| **Volatilidad**          | Volátil               | No volátil            | No volátil            | No volátil            | No volátil            |
| **Método de borrado**    | N/A                   | No reprogramable      | Luz UV (~20 min)      | Eléctrico (byte)      | Eléctrico (bloque)    |
| **Velocidad escritura**  | Alta                  | N/A                   | Lenta                 | Moderada              | Alta (en bloques)     |
| **Ciclos de vida**       | Ilimitados            | 1 (fábrica)           | ~1,000                | ~100,000              | ~10,000–100,000       |
| **Uso típico**           | Memoria principal     | Firmware estático     | Firmware embebido     | Configuraciones BIOS  | Almacenamiento masivo |

---

### **Conclusiones**  
- **RAM** es esencial para el rendimiento temporal, mientras que **ROM** y sus variantes (**EPROM**, **EEPROM**, **FLASH**) ofrecen almacenamiento no volátil con distintos grados de flexibilidad.  
- **FLASH** domina el mercado de almacenamiento moderno por su equilibrio entre costo, velocidad y capacidad, reemplazando gradualmente a **EEPROM** en aplicaciones de alta densidad.  
- **EPROM** persiste en sistemas legacy, pero su dependencia de luz UV limita su uso actual.  

---

### **Referencias**  
1. Vemeko. (2024). *Ultimate Guide to Memory Types: RAM, Flash, and Emerging Technologies Explained*. Recuperado de https://www.vemeko.com/blog/memory-types-guide.html  
2. GeeksforGeeks. (2025). *Difference between EPROM and EEPROM*. Recuperado de https://www.geeksforgeeks.org/digital-logic/difference-between-eprom-and-eeprom/  
3. Wikipedia. (2025). *Flash memory*. Recuperado de https://en.wikipedia.org/wiki/Flash_memory  

*Este reporte se basa exclusivamente en fuentes técnicas verificadas, sin introducir información externa no respaldada.*