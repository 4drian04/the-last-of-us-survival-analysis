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

```
📦 the-last-of-us-survival-analysis
│
├── data/
│   └── dataset_supervivientes.csv
│
├── analisis_datos.ipynb
│
├── main.py
│
├── pyproject.toml
├── uv.lock
├── .python-version
│
└── README.md
```



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

## 📊 Resultados clave del análisis

- Personas por facción
  <img width="849" height="558" alt="personasPorFaccion" src="https://github.com/user-attachments/assets/8e93503f-cbe3-45a1-b934-9ee002cafcd5" />

  Vemos en primer lugar, una distribución de personas por las distintas facciones, es una información que nos puede resultar útil para tener una visión general

- Supervivencia media por facción
  <img width="784" height="484" alt="supervivenciaMediaPorFaccion" src="https://github.com/user-attachments/assets/5d886a76-8bf1-4667-815d-34d9aba87f7a" />

  Vemos que los que más sobreviven son los que son inmunes (ya que no se pueden infectar), y luego le siguen los luciernaga. Sin embargo, podemos ver que los inmunes no tienen un 100% de supervivencia, esto se     puede deber a que hayan muerto por otros seres humanos y no infectados

- Supervivencia media por nivel de infección de zona
  <img width="784" height="484" alt="SupervivenciaMediaPorInfeccion" src="https://github.com/user-attachments/assets/05f45ad3-ae98-4406-8d72-d127cee74c35" />

  Vemos que, como es normal, en los niveles de infección menores sobreviven más gente, aunque podemos ver que en las zonas de nivel 5 y 8 han sobrevido algunas personas

- Supervivencia según el nivel de combate
  <img width="699" height="480" alt="SupervivenicaSegunNivelCombate" src="https://github.com/user-attachments/assets/b4df0d3b-3501-42f7-aed9-58cf2f7d0faa" />

  Por otro lado, en este gráfica observamos una tendencia ascendente, en el que, cuanto mayor sea el nivel de combate, (salvo excepciones como el nivel 2 con 3, y 5 con el 6 y 7) mayor es la tasa promedio de       supervivencia

- Supervivencia según sigilo y combate
  <img width="673" height="556" alt="SupervivenciaSigiloCombate" src="https://github.com/user-attachments/assets/cd40a3ec-1c3d-4e57-87f6-9abc4f8fd989" />

  Por último, podemos ver una comparación con el nivel de combate, el nivel de sigilo y la tasa de supervivencia. Podemos ver que hay una correlación positiva entre ellas, cuanto mayor nivel de sigilo    y mayor   nivel de combate, la tasa de promedio de supervivencia tiende a subir, por lo que podemos cocluir que el equilibrio entre agresividad y discreción es clave en entornos hostiles.

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
