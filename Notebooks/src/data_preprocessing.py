# Celda 1: Importación de librerías básicas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Celda 2: Carga del dataset original y revisión inicial
df = pd.read_csv('nba_10000_processed.csv')
print("Dimensiones originales:", df.shape)
display(df.head())
print(df.info())

# Celda 3: Preprocesamiento y Limpieza
# Seleccionamos las columnas numéricas clave de rendimiento y la variable objetivo
cols_features = ['MIN', 'PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'EFF', 'Season_type']
df_clean = df.dropna(subset=cols_features).copy()

# Guardar el dataset limpio para los siguientes cuadernos
df_clean.to_csv('nba_clean.csv', index=False)
print("Dataset limpio exportado correctamente como 'nba_clean.csv'. Dimensiones finales:", df_clean.shape)

# Celda 4: Visualización de Distribuciones (Histogramas con curvas KDE)
plt.figure(figsize=(12, 8))
metrics_to_plot = ['PTS', 'AST', 'REB', 'EFF']
for i, col in enumerate(metrics_to_plot):
    plt.subplot(2, 2, i+1)
    sns.histplot(df_clean[col], kde=True, bins=30, color='royalblue')
    plt.title(f'Distribución de la variable: {col}')
    plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()

# Celda 5: Análisis de Correlación (Mapa de calor)
plt.figure(figsize=(9, 7))
numeric_cols = ['MIN', 'PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'EFF']
correlation_matrix = df_clean[numeric_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matriz de Correlación de Características de Rendimiento')
plt.show()