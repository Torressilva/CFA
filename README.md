# Corrección de Fechas Automatizada (CFA)

25 de enero de 2014

El objetivo de este proyecto es corregir las fechas en las bases de datos utilizadas por el gobierno de México de forma inteligente y automatizada.

Para lograr el objetivo primero se realizan sustituciones simples, utilizando como criterio una lista-base, después sustituciones más complejas mediaten el uso de regex, y, en caso de ser necesario, se utilizará clustering (una técnica de inteligencia artificial) para inferir más correcciones posibles.

Una vez terminado el análisis, se realizarán las correcciones pertinentes y se actualizará la lista-base en la nube con los nuevos patrones de errores encontrados para facilitar el proceso de corrección la próxima vez que corra el algoritmo, aprovechando lo aprendido de ejecuciones anteriores.

Este proyecto fue desarrollado como parte del proyecto de **Datos Abiertos** de la **Estrategia Digital Nacional de México**. Los integrantes del equipo son:

- **Carlos Castro** (Director de Datos Abiertos)
- **Ernesto Ramírez** (estudiante de Matemáticas Aplicadas - ITAM)
- **Enrique Bonilla** (estudiante de Matemáticas Aplicadas - ITAM)
- **Omar Trejo** (estudiante de Matemáticas Aplicadas y Economía - ITAM)

# Archivos

1. Main
2. Traducción Python-Excel
3. Análisis estadístico
4. Comunicación con _Dropbox_
5. Sustituciones simples
6. Sustituciones _regex_
7. _Clustering / NLP_


# Explicación

1. **Main** (main.py)

 Controla la ejecución general del algoritmo. Hace los preparativos que necesitan las diferentes etapas y comunica los resultados de unas partes del algoritmo con otras.

2. **Traducción Python-Excel** (python-excel.py)

 Recibe una BD en formato .XLS o .XLSX (Excel), trata de inferir qué datos utilizar pero si no encuentra la columna relevante pide al humano que la indique, y la importa al ambiente de Python para poder utilizarla en el resto del algoritmo.

 También, al concluir el algoritmo, escribe los resultados a un archivo nuevo con el mismo nombre que el anterior pero anexando **"_CFA"** entre el nombre del archivo y la extensión, que significa "Corrección de Fechas Automática".

3. **Análisis estadístico** (anali_estad.py)

 Recibe un vector de fechas y realiza estadística descriptiva sobre el mismo. La función principal de este algoritmo es encontrar el porcentaje de los siguientes tipos de errores:

 - **Tipo**: el dato no está en formato fecha.
 - **Rango**: el dato no está dentro del rango de fechas posibles.
 - **Formato**: el dato presenta números inadmisibles o letras.

 Esto permite medir la eficacia del algoritmo y dar una medición de qué tanto ha limpiado la BD.

 Hay un cuarto tipo de error con es detectable ni corregible con este algoritmo. Este error se da cuando el capturista o sistema ingresa un dato incorrecto pero dentro del conjunto de datos posibles. Este dato es indiferente a un dato correcto y no puede ser detectado con este algoritmo.

 Para corregir este error es necesario utilizar el contexto del dato y verificarlo por un humano una vez que se ha percatado que hay un dato incorrecto. La única forma de detectarlo es cuando se necesite usar la información y la misma no haga sentido.

4. **Comunicación con _Dropbox_** (dropbox.py)

 En este archivo se realiza la conexión con _Dropbox_ para leer y escribir las listas necesarias para ejecutar el archivo. Es necesario mantenerlas en la nube para poder utilizar el conocimiento acumulado cada vez que se corre el algoritmo y no estar restringidos por la BD que se trabaja en cada ejecución, sino poder apalancar el conocimiento generado por todas las correcciones anteriores.

5. **Sustituciones simples** (sust_simp.py)

 Recibe un vector de fechas (extraído de la BD), un vector con los índices de las entradas en el vector que contienen errores detectados, y una lista-base bajada de _Dropbox_. Utiliza esta lista-base para buscar sustituciones simples que realizar en el vector, las realiza y regresa un vector actualizado.

6. **Sustituciones _regex_** (sust_regex.py)

 Recibe un vector de fechas (proveniente de la etapa anterior: "Sustituciones simples"), un vector con los índices de las entradas en el vector que contienen errores detectados (menos los corregidos en la etapa anterior), y una lista-base bajada de _Dropbox_ (la misma que en la etapa anterior). Utiliza esta lista-base para buscar sustituciones con expresiones regulares (regex) que realizar en el vector, las realiza y regresa un vector actualizado.

7. **_Clustering / NLP_** (clusterin.py)

 Recibe un vector de fechas (proveniente de la etapa anterior: "Sustituciones regex"), un vector con los índices de las entradas en el vector que contienen errores detectados (menos los corregidos en la etapa anterior), y una lista-base bajada de _Dropbox_ (diferente de la utilizada en las etapas anteriores). Utiliza esta lista-base para buscar patrones en los errores del vector que no hayan sido corregidos en las etapas anteriores.

 Realiza clusters con estos errores y si logra identificar algún patrón proprone cambios para este conjunto de entradas en el vector. Si no logra encontrar cambios relevantes, pide ayuda de un humano, dándole la opción de que corrija adecuadamente las entradas restantes.

 Después utiliza la informaciónn introducida por el humano como conjunto de entrenamiento y lo sube a una lista en _Dropbox_ (esta lista contiene toda la información de entrenamiento del algoritmo).

# Licencia

Este proyecto se publica bajo la licensia **_Apache, versión 2_**, y se anexa una copia en la carpeta raíz del mismo.
