# main.py
import requests
import pandas as pd
import numpy as np

# Extraer datos de la APIpp
url = "https://randomuser.me/api/?results=20"
response = requests.get(url)
data = response.json()["results"]

# Transformar los datos en un DataFrame
df = pd.json_normalize(data)

# Crear columnas simuladas de signos vitales
np.random.seed(42)
df["Temperatura"] = np.random.normal(36.7, 0.5, len(df))
df["Presion_Sistolica"] = np.random.normal(120, 10, len(df))
df["Presion_Diastolica"] = np.random.normal(80, 5, len(df))
df["Frecuencia_Cardiaca"] = np.random.normal(75, 8, len(df))

# Reglas de detección
TEMP_MAX = 37.5
PRESION_SIS_MAX = 140
PRESION_DIA_MAX = 90
FC_MAX = 100

df["Estado"] = np.where(
    (df["Temperatura"] > TEMP_MAX)
    | (df["Presion_Sistolica"] > PRESION_SIS_MAX)
    | (df["Presion_Diastolica"] > PRESION_DIA_MAX)
    | (df["Frecuencia_Cardiaca"] > FC_MAX),
    "CRÍTICO",
    "NORMAL"
)

# Guardar reporte
df.to_csv("datos/reporte_pacientes.csv", index=False)

# Generar resumen
resumen = df["Estado"].value_counts().to_dict()
with open("datos/resumen.txt", "w") as f:
    f.write(f"Pacientes críticos: {resumen.get('CRÍTICO', 0)}\n")
    f.write(f"Pacientes normales: {resumen.get('NORMAL', 0)}\n")

print("Análisis completado.")