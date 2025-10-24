# main.py
import requests
import pandas as pd
import numpy as np

# Api para obtenre data random de personas
url = "https://randomuser.me/api/?results=20"
response = requests.get(url)
data = response.json()["results"]

# Necesitamos un df_data_user
df_data_user_full = pd.json_normalize(data)

# Solo nos improta las columnas importantes
df_data_user = df_data_user_full[['gender', 'name.first', 'name.last']].copy()

# GEneramos data random para los signos
np.random.seed(42)
df_data_user["Temperatura"] = np.random.normal(36.7, 0.5, len(df_data_user))
df_data_user["Presion_Sistolica"] = np.random.normal(120, 10, len(df_data_user))
df_data_user["Presion_Diastolica"] = np.random.normal(80, 5, len(df_data_user))
df_data_user["Frecuencia_Cardiaca"] = np.random.normal(75, 8, len(df_data_user))

# Reglas para derectar
TEMP_MAX = 37.5
PRESION_SIS_MAX = 140
PRESION_DIA_MAX = 90
FC_MAX = 100

df_data_user["Estado"] = np.where(
    (df_data_user["Temperatura"] > TEMP_MAX)
    | (df_data_user["Presion_Sistolica"] > PRESION_SIS_MAX)
    | (df_data_user["Presion_Diastolica"] > PRESION_DIA_MAX)
    | (df_data_user["Frecuencia_Cardiaca"] > FC_MAX),
    "CRÍTICO",
    "NORMAL"
)

# Guardar reporte
df_data_user.to_csv("datos/reporte_pacientes.csv", index=False)

# Generamos resumen
resumen = df_data_user["Estado"].value_counts().to_dict()
with open("datos/resumen.txt", "w") as f:
    f.write(f"Pacientes criticos: {resumen.get('CRÍTICO', 0)}\n")
    f.write(f"Pacientes normales: {resumen.get('NORMAL', 0)}\n")

print("Análisis completado.")