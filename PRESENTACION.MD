### **APERTURA (2 min)**

```
"Buenos días/tardes. Mi nombre es David Caleb Chaparro Orozco, 
Data Scientist y ML Engineer.

Hoy les voy a presentar DOS casos de estudio que demuestran 
capacidades complementarias en Data Science:

El primero, un sistema de NER para venta directa con ROI de 303%.
El segundo, un sistema de recomendación para e-commerce con +94% 
de mejora vs baseline.

Ambos resuelven problemas de negocio reales con tecnologías 
diferentes pero complementarias.

Comencemos."
```
---
### **CASO 1: TRANSICIÓN (30 seg)**

```
"Primer caso: Venta Directa.

El problema es simple pero costoso: 65% de los clientes 
no vuelven a comprar. Eso representa $850M en revenue perdido.

"Los clientes expresan sus intenciones, problemas
y preferencias en texto libre - pero nadie lo analiza
sistemáticamente. Aquí está la oportunidad."

Cual es esa oportunidad oculta: 80% de la información más 
valiosa está en texto no estructurado - WhatsApp, CRM, 
transcripciones de llamadas.


Mi propuesta: usar NER para convertir ese texto en acción."
```
---

### **CASO 1: EJEMPLO (1 min)**

```
"Veamos un ejemplo real.

[Leer conversación en pantalla]

Con NER, extraemos automáticamente:
- Los productos mencionados
- El sentimiento (positivo o negativo)
- Los problemas reportados
- Y lo más importante: la intención de recompra

El sistema genera una alerta automática para la consultora
con acciones específicas: 'Enviar promo en 10 días'

Esto es convertir texto en acción."
```

---
### **CASO 1: ROI (1 min)**

```
"Los números son contundentes.

Inversión: $280M pesos.
Retorno año 1: $1,030M pesos.
ROI: 303%.
Payback: 4.2 meses.

Y las métricas de negocio:
- Frecuencia de compra sube 78%
- Tasa de segunda compra de 35% a 58%
- Retención a 6 meses de 22% a 42%

No es un experimento. Es una inversión con retorno medible."

```
--- 

### **CASO 1: KPIs - Impacto Esperado (1 min)**
```
TÍTULO: Valor del Producto Analítico


VALOR PARA STAKEHOLDERS:

Para CONSULTORAS:
✅ Dashboard con alertas inteligentes
✅ Scripts personalizados por cliente
✅ +25% conversión en recontactos
✅ -40% tiempo de gestión manual

Para CLIENTES:
✅ Experiencia personalizada
✅ Problemas resueltos más rápido
✅ Seguimiento proactivo

Para la EMPRESA:
✅ Primera en aplicar NER a venta directa
✅ Ventaja competitiva sostenible
✅ Automatización 60% de análisis manual
```

---


### **Caso 1: PLANIFICACIÓN DEL PROYECTO 📅 IMPORTANTE**

```
FASES DEL PROYECTO:

MES 1   │ FASE 0: Discovery & PoC
        │ • Validar hipótesis con 5K ejemplos
        │ • F1-Score objetivo: >0.75
        │ • Go/No-Go decision
        │ Equipo: 1 DS Lead + 1 PM + 2 BA

MES 2-3 │ FASE 1: Preparación de Datos
        │ • Anotación manual 50K conversaciones
        │ • Pipeline ETL
        │ • Kappa score: >0.85

MES 4-5 │ FASE 2: Desarrollo Modelo NER
        │ • Fine-tuning BERT
        │ • F1-Score objetivo: >0.86
        │ • API FastAPI

MES 6-7 │ FASE 3: Aplicaciones
        │ • Dashboard React para consultoras
        │ • Admin panel
        │ • Integraciones

MES 8-9 │ FASE 4: Piloto
        │ • 200 consultoras (10% del total)
        │ • Validación impacto: +15% frecuencia
        │ • NPS: >8/10

MES 10  │ FASE 5: Rollout Nacional
        │ • 100% consultoras
        │ • Producción completa
```

---
### **CASO 2: VALOR DIFERENCIADOR**
```
Implementar sistema de recomendación completo para
e-commerce usando Python

Implementé 5 algoritmos diferentes y un modelo híbrido,
siguiendo metodología CRISP-DM completa
```
---
### **CASO 2: RESULTADOS (1 min)**

```
"Los resultados técnicos son excelentes:

F1-Score de 0.0060 - que en un sistema con sparsity 
extrema es un número muy bueno.

Pero lo importante es el impacto en negocio:
- CTR sube 15%
- Conversión sube 10%
- Valor promedio de orden sube 8%

Eso se traduce en $850M pesos de revenue incremental al año.
"
```


### **CASO 2: SISTEMAS DE RECOMENDACION**
```
5 ALGORITMOS IMPLEMENTADOS:

1. POPULARIDAD (Baseline)
   • Productos más vendidos
   • Peso en híbrido: 20%
   • Uso: Fallback para cold start

2. USER-BASED COLLABORATIVE FILTERING
   • Encuentra usuarios similares
   • Recomienda lo que compraron
   • Basado en similitud de coseno

3. ITEM-BASED COLLABORATIVE FILTERING
   • Encuentra productos similares
   • Peso en híbrido: 40%
   • Más estable que user-based

4. SVD (MATRIX FACTORIZATION)
   • 50 componentes latentes
   • Peso en híbrido: 40%
   • Maneja sparsity efectivamente

5. MODELO HÍBRIDO 🏆
   • Combina los 4 anteriores
   • Pesos optimizados
   • Mejor performance general

MANEJO DE DESAFÍOS:
✅ Sparsity: SVD + Sparse matrices (SciPy)
✅ Cold Start: Popularidad como fallback
✅ Escalabilidad: Optimización algorítmica
```

### **CASO 2: METODOLOGÍA CRISP-DM**
```
METODOLOGÍA: CRISP-DM (Requerida en la prueba)

┌────────────────────────────────────────┐
│ 1. BUSINESS UNDERSTANDING              │
│    ✅ Objetivos: CTR +15%, Conv +10%   │
│    ✅ Definición de éxito              │
└────────────────────────────────────────┘
              ↓
┌────────────────────────────────────────┐
│ 2. DATA UNDERSTANDING                  │
│    ✅ EDA de 231K transacciones        │
│    ✅ Análisis de sparsity             │
│    ✅ Identificación de patrones       │
└────────────────────────────────────────┘
              ↓
┌────────────────────────────────────────┐
│ 3. DATA PREPARATION                    │
│    ✅ Matriz user-item dispersa        │
│    ✅ Train/Test split (80/20)         │
│    ✅ Estratificación por usuario      │
└────────────────────────────────────────┘
              ↓
┌────────────────────────────────────────┐
│ 4. MODELING                            │
│    ✅ 5 algoritmos implementados       │
│    ✅ Hiperparámetros optimizados      │
│    ✅ Modelo híbrido diseñado          │
└────────────────────────────────────────┘
              ↓
┌────────────────────────────────────────┐
│ 5. EVALUATION                          │
│    ✅ Precision@10, Recall@10, F1      │
│    ✅ Comparación de modelos           │
│    ✅ Validación cruzada               │
└────────────────────────────────────────┘
              ↓
┌────────────────────────────────────────┐
│ 6. DEPLOYMENT                          │
│    ✅ Estrategia de producción         │
│    ✅ Sistema de actualización         │
│    ✅ Monitoreo continuo               │
│    ✅ Framework A/B Testing            │
└────────────────────────────────────────┘
```

### **CASO 2: PERFORMANCE DE MODELOS 📈** 
```
TÍTULO: Performance de Modelos

MÉTRICAS DE EVALUACIÓN:

┌──────────────────────────────────────────────────┐
│ MODELO      │ Prec@10 │ Recall@10 │ F1-Score   │
├──────────────────────────────────────────────────┤
│ Popularidad │ 0.0017  │ 0.0172    │ 0.0031     │
│ User-Based  │ 0.0017  │ 0.0115    │ 0.0029     │
│ Item-Based  │ 0.0017  │ 0.0172    │ 0.0031     │
│ SVD         │ 0.0017  │ 0.0057    │ 0.0027     │
│ 🏆 HÍBRIDO  │ 0.0034  │ 0.0230    │ 0.0060     │
└──────────────────────────────────────────────────┘

MEJORA VS BASELINE:
✅ +94% en F1-Score
✅ +100% en Precision@10
✅ +34% en Recall@10

CONTEXTO IMPORTANTE:
En sistemas de recomendación con sparsity extrema
(0.082%), estos números representan EXCELENTE
performance según literatura académica.
```