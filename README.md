# 🛒 Sistema de Recomendación para E-Commerce

Sistema inteligente de recomendación de productos implementado con Machine Learning para mejorar la experiencia de compra y aumentar las conversiones en plataformas de comercio electrónico.

**Autor:** David Caleb Chaparro Orozco  
**Fecha:** Octubre 2025

---

## 📝 Descripción

Este proyecto implementa un sistema de recomendación completo para una plataforma de e-commerce, utilizando múltiples algoritmos de Machine Learning para ofrecer sugerencias personalizadas a los usuarios. El sistema está diseñado para funcionar en producción y incluye monitoreo continuo, A/B testing y actualización automática.

### ¿Qué hace este proyecto?

- **Recomienda productos** personalizados basándose en el comportamiento de compra de los usuarios
- **Maneja datos dispersos** (sparse data) de manera eficiente
- **Resuelve el problema de Cold Start** para usuarios y productos nuevos
- **Se actualiza automáticamente** con nuevos datos
- **Monitorea su propio rendimiento** con KPIs en tiempo real
- **Permite A/B Testing** para evaluar mejoras

---

## 🎯 Características Principales

### 5 Algoritmos Implementados

1. **Popularidad** - Recomienda los productos más vendidos
2. **User-Based Collaborative Filtering** - Encuentra usuarios similares y recomienda lo que ellos compraron
3. **Item-Based Collaborative Filtering** - Encuentra productos similares basándose en patrones de compra
4. **SVD (Matrix Factorization)** - Usa factorización de matrices para capturar patrones latentes
5. **Modelo Híbrido** - Combina los mejores aspectos de todos los modelos anteriores

### Métricas y Evaluación

- Precision@10: 0.0034
- Recall@10: 0.0230
- F1-Score: 0.0060
- Sistema de evaluación continua
- Framework de A/B Testing incluido

---

## 🗂️ Estructura del Proyecto

```
EcommerceRecommendationSystembyDavidCaleb/
│
├── TestTecnicalbyDavidCaleb.ipynb    # Notebook principal con todo el análisis
├── dataset_sample_1.csv               # Datos de transacciones
├── dataset_sample_2.csv               # Datos de clientes
├── requirements.txt                   # Dependencias del proyecto
└── README.md                          # Este archivo
```

---

## 📊 Datos

El proyecto trabaja con dos datasets:

- **dataset_sample_1.csv**: 231,000 transacciones con información de productos, categorías y ventas
- **dataset_sample_2.csv**: Información de 37,570 clientes únicos (demografía, ubicación)

**Características del dataset:**
- 7,134 productos únicos
- 85 categorías de productos
- Período: Diciembre 2022 - Noviembre 2023
- Ticket promedio: $26,853 COP

---

## 🚀 Cómo Usar

### Requisitos Previos

- Python 3.8 o superior
- Jupyter Notebook o JupyterLab

### Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/DavidCalebChaparroOrozco/EcommerceRecommendationSystembyDavidCaleb.git
cd EcommerceRecommendationSystembyDavidCaleb
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Ejecutar el notebook**
```bash
jupyter notebook TestTecnicalbyDavidCaleb.ipynb
```

4. **Ejecutar todas las celdas**
   - En Jupyter: `Cell` → `Run All`
   - O ejecutar celda por celda con `Shift + Enter`
---

## 💻 Tecnologías Utilizadas

### Lenguajes y Frameworks
- **Python 3.8+** - Lenguaje principal
- **Jupyter Notebook** - Entorno de desarrollo

### Librerías de Data Science
- **Pandas** - Manipulación de datos
- **NumPy** - Cálculos numéricos
- **SciPy** - Matrices dispersas (sparse matrices)

### Machine Learning
- **Scikit-learn** - Algoritmos de ML y métricas
- **TruncatedSVD** - Factorización de matrices

### Visualización
- **Matplotlib** - Gráficos estáticos
- **Seaborn** - Visualizaciones estadísticas

---

## 📈 Resultados

### Mejor Modelo: Híbrido

El modelo híbrido que combina múltiples algoritmos obtuvo los mejores resultados:

| Métrica | Valor |
|---------|-------|
| Precision@10 | 0.0034 |
| Recall@10 | 0.0230 |
| F1-Score | 0.0060 |

**Mejora vs Baseline:** +94% en F1-Score

### Impacto en Negocio (Esperado)

- 📈 CTR: +15%
- 💰 Conversión: +10%
- 🛍️ AOV (Valor promedio del pedido): +8%
- ⏱️ ROI positivo en 3-4 meses

---

## 🔍 Lo que Encontrarás en el Notebook

### 1. Análisis Exploratorio (EDA)
   - Análisis de transacciones y clientes
   - Visualizaciones de comportamiento de compra
   - Análisis de categorías y productos
   - Patrones temporales de ventas

### 2. Preprocesamiento
   - Limpieza de datos
   - Manejo de valores nulos
   - Creación de características temporales
   - Ingeniería de features

### 3. Sistema de Recomendación
   - Implementación de 5 algoritmos diferentes
   - Manejo de datos dispersos
   - Solución para Cold Start
   - Modelo híbrido optimizado

### 4. Evaluación
   - Métricas de rendimiento
   - Comparación de modelos
   - Visualizaciones de resultados
   - Análisis de errores

### 5. Deployment
   - Plan de implementación en producción
   - Sistema de actualización automática
   - Monitoreo continuo con KPIs
   - Framework de A/B Testing

---

## 🛠️ Metodología

Este proyecto sigue la metodología **CRISP-DM** (Cross-Industry Standard Process for Data Mining):

1. **Business Understanding** - Entender el problema de negocio
2. **Data Understanding** - Análisis exploratorio de datos
3. **Data Preparation** - Limpieza y preparación
4. **Modeling** - Implementación de algoritmos
5. **Evaluation** - Evaluación de modelos
6. **Deployment** - Plan de implementación en producción

---

## 📦 Dependencias Principales

```
pandas==2.1.4
numpy==1.26.2
scipy==1.11.4
scikit-learn==1.3.2
matplotlib==3.8.2
seaborn==0.13.0
jupyter==1.0.0
```

Ver `requirements.txt` para la lista completa.

---

## 🎓 Aprendizajes Clave

Durante este proyecto aprendí y apliqué:

- Cómo manejar datos dispersos (sparsity de 0.082%)
- Implementación de múltiples algoritmos de recomendación desde cero
- Estrategias para resolver el problema de Cold Start
- Diseño de sistemas ML escalables para producción
- Creación de frameworks de A/B Testing
- Monitoreo continuo de modelos en producción

---

## 📧 Contacto

**David Caleb Chaparro Orozco**

- GitHub: [@DavidCalebChaparroOrozco](https://github.com/DavidCalebChaparroOrozco)
- LinkedIn: [David Caleb Chaparro Orozco](https://linkedin.com/in/DavidCalebChaparroOrozco)
---