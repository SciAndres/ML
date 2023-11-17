# ML
# ML y streaming

Este conjunto de códigos aborda un flujo de trabajo que incluye manipulación de datos, análisis exploratorio, ml con regresión lineal, guardar el modelo e integración con Kafka.
## Estructura de Código

### 1. Importación de Librerías:
Se importan bibliotecas esenciales como pandas, sqlalchemy, seaborn, matplotlib, joblib, scikit-learn y otras para análisis de datos, ml y guardar el modelo.

### 2. Lectura y Limpieza de Datos:
Los datos se leen desde archivos CSV correspondientes a diferentes años y se realiza la limpieza.

### 3. Exploración y Consolidación de Datos:
Se exploran estadísticas descriptivas y visualizaciones, y se concatenan los datos en un DataFrame consolidado.

### 4. Guardar el modelo:
El modelo de regresión lineal se entrena y se guardar en extencion .pkl usando joblib para su uso futuro sin necesidad de volver a entrenarlos.

### 5. Integración con Kafka:
Funciones `kafka_producer` y `kafka_consumer` se implementan para enviar y recibir mensajes con Kafka.


## Instrucciones de Uso

1. **Configuración del Entorno:**
   - Asegúrate de tener instaladas todas las bibliotecas requeridas. Puedes instalarlas utilizando `pip install (Libreria requerida)`.

2. **Lectura de Datos:**
   - Ajusta las rutas de los archivos CSV en las funciones `pd.read_csv` según la ubicación de tus datos.

3. **Manipulación y Exploración de Datos:**
   - Utiliza las funciones para manipular y explorar los datos según las necesidades.

4. **Modelado y guardado:**
   - Se entrena un modelo de regresión lineal y se guarda los modelos con extencio .pkl con joblib.dump.

5. **Integración con Kafka:**
   - Configura las funciones `kafka_producer` y `kafka_consumer` según la configuración de tu servidor Kafka.

6. **Ejecución del Código:**
   - Ejecuta el código en un entorno compatible con las bibliotecas mencionadas.

## Consideraciones

- Asegúrate de tener un servidor Kafka en ejecución para probar la funcionalidad de productor y consumidor.
- Ajusta parámetros y rutas según tus necesidades y ubicación de archivos.

Este código proporciona una base para el análisis de datos, modelo de regresion y streaming con Kafka. 
