# Dashboard de anuncios de autos en EE. UU.

Este proyecto consiste en una aplicación web desarrollada con Streamlit para visualizar datos de anuncios de venta de vehículos usados en Estados Unidos.

La aplicación permite al usuario generar un histograma y un gráfico de dispersión interactivo para explorar el kilometraje y los precios de los autos publicados.

## Archivos del repositorio

- `vehicles_us.csv`: dataset utilizado.
- `app.py`: script principal de la app en Streamlit.
- `requirements.txt`: librerías necesarias.
- `notebooks/EDA.ipynb`: notebook de análisis exploratorio.

## Cómo ejecutarla localmente

1. Clona el repositorio.
2. Crea un entorno virtual (por ejemplo, `autos_env`).
3. Instala las dependencias con:

    pip install -r requirements.txt

4. Ejecuta la app con:

    streamlit run app.py

# analisis-coches-streamlit