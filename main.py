import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')

tlou_df = pd.read_csv("data/the_last_of_us_survival_dataset.csv") # Leemos el csv

# Obtenemos las columnas importantes en el eje x para determinar si una persona sobrevive o no
x = tlou_df[['Edad', 'Genero', 'Faccion', 'ExperienciaCombate', 'HabilidadSigilo', 'Salud', 'NivelInfeccionZona', 'CondicionesClimaticas', 'NivelEstrés', 'TieneCompañero']]
y = tlou_df['Superviviente'] # En el eje y determinamos si sobrevive o no

# El algoritmo entiende de 0 y 1, por lo que tenemos que pasar las variables categóricas a variables numéricas.
# Para ello establecemos, mediante la función ".map" que el género femenino sea 0 y el masculino sea 1
x['Genero'] = x['Genero'].map({'Femenino': 0, 'Masculino': 1})
# En este caso hacemos lo mismo para la facción y para la condición climática
x['Faccion'] = x['Faccion'].map({'Civil': 0, 'Militar':1, 'Cazador':2, 'Firefly': 3})
x['CondicionesClimaticas'] = x['CondicionesClimaticas'].map({'Seco': 0, 'Húmedo': 1, 'Lluvioso': 2})

# Dividimos los datos en entrenamientos para el algoritmo y en test para ver el porcentaje de acierto
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(x_train, y_train) # Entrenamos al algoritmo

y_pred = rf_classifier.predict(x_test) # Hacemos una predicción con los test
accuracy = accuracy_score(y_test, y_pred) # Obtenemos el porcentaje de acierto
print(f"Accuraccy: {accuracy:.2f}")

# Ahora vamos a crear un dataframe con datos nuevos (con los datos ya numéricos) y hacemos predicciones
columnas = [
    "Edad","Genero","Faccion","ExperienciaCombate","HabilidadSigilo",
    "Salud", "NivelInfeccionZona","CondicionesClimaticas","NivelEstrés",
    "TieneCompañero"
]

datos_prediccion_codificados = [
    [22,0,0,2,8,90,1,0,3,1],
    [48,1,1,7,3,60,8,2,7,0],
    [34,1,3,6,6,72,4,1,5,1],
    [17,0,0,1,7,95,2,0,4,1],
    [56,1,2,8,2,55,9,0,9,0],
    [29,0,3,5,9,68,3,1,6,1],
    [63,1,1,9,1,50,10,2,10,0],
    [40,0,0,4,5,78,5,0,5,1]
]

df_pred = pd.DataFrame(datos_prediccion_codificados, columns=columnas)

prediccion = rf_classifier.predict(df_pred) # Hacemos predicciones con los datos nuevos
i = 1
# Pintamos por pantalla el resultado
for resultado, superviviente in zip(prediccion, datos_prediccion_codificados):
    print(f"El superviviente número {i} era: ")
    if superviviente[2] == 1:
        print("- Militar")
    elif superviviente[2] == 0:
        print("- Civil")
    elif superviviente[2] == 2:
        print("- Cazador")
    else:
        print("- Luciernaga")
    print(f"- Tenía una experiencia de combate de {superviviente[3]}")
    print(f"- Además tenía una habilidad de sigilo de {superviviente[4]}")
    print(f"- Tenia una salud de {superviviente[5]}")
    print(f"- Vivía en una zona infectada de nivel {superviviente[6]}")
    if superviviente[9] == 1:
        print("- Además tenía compañero")
    else:
        print("- El superviviente no tenía compañero")
    print(f"- Y su nivel de estres era de {superviviente[8]}")
    print(f"Este superviviente ha {'sobrevivido' if resultado==1 else 'muerto'}")
    print()
    i=i+1
