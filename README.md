# 🧟‍♂️ Análisis de Supervivencia en *The Last of Us*

Este proyecto consiste en el **análisis de un dataset inspirado en el universo de *The Last of Us***, con información sobre distintos supervivientes en un mundo postapocalíptico.  
El objetivo principal es **analizar los datos** y **predecir si una persona sobrevivirá o no** utilizando un modelo de **Random Forest**.

---

## 📊 Objetivos del proyecto

- Analizar y explorar un dataset de supervivientes.
- Realizar limpieza y visualización de datos.
- Entrenar un modelo de Machine Learning.
- Evaluar el rendimiento del modelo.
- Predecir la supervivencia de nuevos individuos a partir de sus características.

---

## 📁 Estructura del proyecto

📦 the-last-of-us-survival-analysis
│
├── data/
│ └── dataset_supervivientes.csv
│
├── analisis_datos.ipynb
│
│
├── main.py
│
├── pyproject.toml
├── uv.lock
├── .python-version
│
└── README.md


---

## 🧪 Dataset

El dataset contiene información sobre personas que intentan sobrevivir en un entorno hostil.  
Cada fila representa a un superviviente y cada columna describe una de sus características.

### 📌 Significado de las columnas

| Columna | Descripción |
|-------|-------------|
| Edad | Edad de la persona |
| Genero | Género de la persona |
| Facción | Facción a la que pertenece la persona (Militar, Civil, Bombero, etc.) |
| ExperienciaCombate | Experiencia en combate (1 = muy poca, 10 = mucha) |
| HabilidadSigilo | Habilidad para realizar acciones en sigilo (1 = muy poca, 10 = mucha) |
| Salud | Estado de salud de la persona |
| ArmaFuego | Arma de fuego que posee |
| ArmaCuerpoCuerpo | Arma cuerpo a cuerpo que posee |
| ItemCreable | Objeto que es capaz de crear |
| NivelInfeccionZona | Intensidad del peligro ambiental |
| CondicionesClimaticas | Condiciones climáticas del entorno |
| NivelEstrés | Nivel de estrés (0 = nada, 10 = máximo) |
| TieneCompañero | Indica si la persona tiene un compañero |
| Superviviente | Variable objetivo: indica si la persona sobrevive o no |

---

## 📓 Análisis de datos (`analisis_datos.ipynb`)

En el notebook se realiza:

- Exploración inicial del dataset.
- Análisis estadístico de las variables.
- Visualización de datos.
- Estudio de relaciones entre variables.

---

## 🤖 Modelo de Machine Learning (`main.py`)

En el archivo `main.py` se lleva a cabo:

- Carga del dataset ya procesado.
- División de los datos en entrenamiento y test.
- Entrenamiento de un **RandomForestClassifier**.
- Evaluación del modelo.
- Predicción de la supervivencia con nuevos datos de personas.

---

## ⚙️ Gestión de dependencias

Este proyecto utiliza **uv** para la gestión de dependencias y versiones de Python.

- `pyproject.toml`: definición del proyecto y dependencias.
- `uv.lock`: bloqueo de versiones exactas de las librerías.
- `.python-version`: versión de Python utilizada en el proyecto.

 ## 🚀 Ejecución del proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/4drian04/the-last-of-us-survival-analysis.git
  
2. Sincronizar el entorno y las dependencias con **uv**:
   ```bash
   uv sync
  
3. Entrenar el modelo y realizar predicciones:
   ```bash
   uv run python main.py

   
## 📈 Resultados

El modelo permite predecir si un superviviente tiene probabilidades de sobrevivir, identificando qué características influyen más en la supervivencia dentro de un entorno extremo.
