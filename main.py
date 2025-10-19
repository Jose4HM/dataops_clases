import pandas as pd
import numpy as np

df = pd.read_csv('datos/pacientes.csv')

# Signos anormales o críticos
TEMP_MAX = 37.5
PRESION_SIS_MAX = 140
PRESION_DIA_MAX = 90
FC_MAX = 100

# Detectamos paciente criticps
df['Estado'] = np.where(
    (df['Temperatura'] > TEMP_MAX) |
    (df['Presion_Sistolica'] > PRESION_SIS_MAX) |
    (df['Presion_Diastolica'] > PRESION_DIA_MAX) |
    (df['Frecuencia_Cardiaca'] > FC_MAX),
    'CRÍTICO',
    'NORMAL'
)

prom_temp = df['Temperatura'].mean()
prom_fc = df['Frecuencia_Cardiaca'].mean()
num_criticos = (df['Estado'] == 'CRÍTICO').sum()

df.to_csv('datos/reporte_pacientes.csv', index=False)

print("✅ Análisis completado correctamente.")
print(f"Promedio de temperatura: {prom_temp:.2f} °C")
print(f"Promedio de frecuencia cardíaca: {prom_fc:.1f} bpm")
print(f"Pacientes críticos detectados: {num_criticos}")
