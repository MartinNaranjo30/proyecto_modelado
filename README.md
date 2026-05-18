# proyecto_modelado
Repositorio para la evaluación 2 de programación para la ciencia de datos
Proyecto de Machine Learning: Clasificación de Rendimiento NBA

Este proyecto aplica técnicas de Machine Learning (aprendizaje supervisado y no supervisado) para analizar estadísticas de jugadores de la NBA. El objetivo principal es clasificar si el rendimiento estadístico de un jugador corresponde a la **Temporada Regular** o a los **Playoffs**, y descubrir perfiles ocultos de jugadores mediante agrupamiento.

Este repositorio fue desarrollado como parte de la Evaluación Parcial 2 de la asignatura Programación para la Ciencia de Datos.

Estructura del Proyecto

El proyecto sigue una arquitectura modular y profesional, separando el código fuente, los modelos entrenados y los resultados analíticos:


├── README.md                 # Documentación principal del proyecto
├── data/                     # Carpeta para los datasets (original y limpio)
│   ├── nba_10000_processed.csv
│   └── nba_clean.csv         
├── src/                      # Código fuente principal
│   ├── 01_data_preprocessing.py
│   ├── 02_model_training.py
│   ├── 03_model_evaluation.py
│   ├── 04_hyperparameter_tuning.py
│   └── 05_final_analysis.py
├── models/                   # Objetos y modelos serializados
│   ├── scaler.pkl
│   ├── data_partitions.pkl
│   └── trained_models/
│       ├── model_log_reg_base.pkl
│       ├── model_dt_base.pkl
│       └── model_dt_optimized.pkl
└── results/                  # Evidencias y salidas del modelo
    ├── metrics/
    │   └── tabla_resultados_detallada.csv
    ├── plots/
    │   ├── matriz_confusion.png
    │   ├── matriz_correlacion.png
    │   └── clusters_jugadores.png
    └── reports/
        └── informe_final.pdf # Justificación técnica y conclusiones

Tecnologías Utilizadas: 
Lenguaje: Python 3.x
Manipulación de Datos: Pandas, NumPy
Machine Learning: Scikit-learn (Regresión Logística, Árboles de Decisión, KMeans, GridSearchCV)
Visualización: Matplotlib, Seaborn
Persistencia de Modelos: Joblib

Ejecutar el flujo de trabajo:
Ejecutar los scripts ubicados en la carpeta src/ en orden secuencial. El primer script limpiará los datos originales y generará nba_clean.csv, 
el cual será utilizado por los scripts posteriores para entrenar y evaluar los modelos.

Resultados Destacados:
Tras el entrenamiento y la evaluación comparativa, se priorizó la métrica de Recall debido a la naturaleza desbalanceada 
de los datos deportivos (mayor volumen de registros en temporada regular).

El modelo de Regresión Logística Base obtuvo una exactitud general del 79.26%, pero un recall moderado para la clase de Playoffs.

Mediante la optimización de hiperparámetros (GridSearchCV) en el modelo de Árbol de Decisión, 
logramos aumentar significativamente el Recall de Playoffs al 81.13%, minimizando los Falsos Negativos y mejorando la detección de rendimientos bajo presión.

El análisis no supervisado con KMeans (k=3) permitió segmentar exitosamente a los jugadores en tres perfiles estadísticos distintos basados en su volumen de puntos y eficiencia global.


Equipo de Desarrollo: 

Martin Corvalán

Martin Naranjo
