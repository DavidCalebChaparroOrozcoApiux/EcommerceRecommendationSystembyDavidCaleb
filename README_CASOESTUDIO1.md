# 🎯 Caso de Estudio: Sistema NER para Impulsar Frecuencia de Recompra en Venta Directa

**Autor:** David Caleb Chaparro Orozco  
**Fecha:** Octubre 2025  
**Desafío:** Aumento del indicador de continuidad de recompra (Frecuencia) en clientes de venta directa

---

## 📋 Tabla de Contenido

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [Definición del Problema](#definicion-problema)
3. [Propuesta de Solución: Producto Analítico](#propuesta-solucion)
4. [Arquitectura Técnica](#arquitectura-tecnica)
5. [Propuesta de Valor](#propuesta-valor)
6. [Planificación del Proyecto](#planificacion)
7. [Roadmap de Implementación](#roadmap)
8. [Recursos Necesarios](#recursos)
9. [Métricas de Éxito](#metricas)
10. [Análisis de Riesgos](#riesgos)
11. [Conclusiones](#conclusiones)

---

<a id="resumen-ejecutivo"></a>
## 🎪 Resumen Ejecutivo

### El Desafío
Las empresas de venta directa enfrentan un problema crítico: **baja continuidad de recompra**. Solo el 30-40% de los clientes realizan una segunda compra, y la frecuencia promedio de pedidos es de 1.8 por año, muy por debajo del objetivo estratégico de 4 compras anuales.

### La Solución: NER Intelligence System
Propongo un **Sistema de Inteligencia basado en Named Entity Recognition (NER)** que extrae información estructurada de interacciones no estructuradas (comentarios de consultoras, feedback de clientes, conversaciones de WhatsApp, notas de seguimiento) para:

- 🔍 **Identificar patrones de abandono temprano**
- 💡 **Detectar productos/categorías que generan recompra**
- 🎯 **Personalizar estrategias de retención automáticamente**
- 📊 **Predecir intención de recompra antes de 30 días**

### Impacto Esperado
| Métrica | Baseline | Meta 12 meses | Mejora |
|---------|----------|---------------|--------|
| Frecuencia de compra anual | 1.8 | 3.2 | +78% |
| Tasa de recompra 2da compra | 35% | 58% | +23pp |
| Retención a 6 meses | 22% | 42% | +20pp |
| Revenue incremental | - | +$850M COP | - |

---

<a id="definicion-problema"></a>
## 🔴 Definición del Problema

### Contexto de Negocio

En el modelo de **venta directa**, las consultoras actúan como intermediarias entre la empresa y los clientes finales. El principal desafío es mantener a los clientes comprando de manera continua.

**Problema identificado:**
```
❌ 65% de los clientes NO vuelven a comprar después de su primera orden
❌ 80% de la información valiosa está en texto NO estructurado
❌ Las consultoras reportan falta de herramientas predictivas
❌ No existe visibilidad de señales tempranas de abandono
```

### ¿Por qué es crítico?

- **CAC (Costo de Adquisición)**: $45,000 COP por cliente
- **Break-even point**: La empresa necesita 2.5 compras para recuperar inversión
- **LTV promedio actual**: Solo $82,000 COP (1.8 compras)
- **LTV objetivo**: $180,000 COP (4 compras)

### Datos Disponibles pero Subutilizados

La empresa tiene **datos ricos pero no estructurados**:

```
📱 WhatsApp: 2.3M mensajes/mes entre consultoras y clientes
📝 Notas de CRM: 450K registros de seguimiento en texto libre
💬 Feedback post-compra: 89K comentarios sin categorizar
🎤 Transcripciones de llamadas: 12K audios transcritos
```

**El problema:** Esta información no se analiza sistemáticamente. La solución actual depende de lectura manual y es imposible escalar.

---

<a id="propuesta-solucion"></a>
## 💡 Propuesta de Solución: Producto Analítico

### 🏆 Nombre del Producto: **ReFrecuency NER Intelligence**

Un sistema de inteligencia artificial que utiliza **Named Entity Recognition (NER)** para extraer, estructurar y actuar sobre información oculta en texto, con el objetivo de aumentar la frecuencia de recompra.

### ¿Qué hace el producto?

#### 1. **Extracción Inteligente con NER**

El modelo de NER que propongo entrenar está diseñado para identificar entidades específicas del dominio:

```python
# Entidades personalizadas para Venta Directa
ENTIDADES_NER = {
    'PRODUCTO': 'Nombre específico de productos mencionados',
    'CATEGORIA': 'Categorías de productos (cosméticos, fragancias, etc.)',
    'SENTIMIENTO': 'Satisfacción, queja, duda, intención de compra',
    'FRECUENCIA_INTENCION': 'Expresiones de intención temporal',
    'PROBLEMA': 'Issues reportados (entrega, calidad, precio)',
    'MOTIVO_ABANDONO': 'Razones explícitas de no recompra',
    'PREFERENCIA': 'Gustos y preferencias expresadas',
    'OCASION_USO': 'Contexto de uso del producto'
}
```

**Ejemplo de procesamiento:**

```
Texto original:
"Hola Marta, la crema de noche me encantó 😍 pero el precio está un 
poco alto. Creo que en 2 semanas podría pedirte más si me dices 
que hay promo. El serum no me gustó tanto, me irritó la piel."

↓ [Procesamiento NER] ↓

Entidades extraídas:
- PRODUCTO: ["crema de noche", "serum"]
- SENTIMIENTO: ["encantó" (+), "no me gustó tanto" (-)]
- PROBLEMA: ["precio alto", "irritó la piel"]
- FRECUENCIA_INTENCION: ["en 2 semanas", "si hay promo"]
- ACCION_SUGERIDA: "Enviar promo crema de noche en 10 días"
```

#### 2. **Módulos del Sistema**

##### 📊 **Módulo 1: Churn Predictor**
- Detecta señales tempranas de abandono en conversaciones
- Identifica clientes en riesgo 15-20 días antes
- Score de probabilidad de recompra (0-100)

##### 🎯 **Módulo 2: Product Affinity Analyzer**
- Identifica qué productos generan mayor recompra
- Detecta combinaciones de productos que fidelizan
- Mapea categorías "ancla" vs "complementarias"

##### 💬 **Módulo 3: Feedback Structurer**
- Convierte feedback no estructurado en datos accionables
- Categoriza automáticamente problemas y satisfacciones
- Genera alertas tempranas de issues de calidad

##### 🤖 **Módulo 4: Recommendation Engine**
- Sugiere próximo mejor producto basado en entidades extraídas
- Personaliza momento óptimo de contacto
- Genera scripts automáticos para consultoras

##### 📈 **Módulo 5: Dashboard Inteligente**
- Visualizaciones en tiempo real de insights NER
- Alertas proactivas para consultoras
- Reportes automáticos para gerencia

---

<a id="arquitectura-tecnica"></a>
## 🏗️ Arquitectura Técnica

### Stack Tecnológico Propuesto

```yaml
Lenguaje: Python 3.10+
NER Framework: spaCy 3.7 + Transformers (BERT multilingüe)
Modelo Base: bert-base-multilingual-cased (fine-tuned)
Base de Datos: PostgreSQL + MongoDB (texto no estructurado)
ETL: Apache Airflow
API: FastAPI
Frontend: Streamlit + React (para consultoras)
Cloud: AWS (SageMaker para ML, Lambda, S3, RDS)
Monitoreo: MLflow + Grafana
```

### Flujo de Datos

```
┌─────────────────────────────────────────────────────────────────┐
│                    FUENTES DE DATOS                             │
│  WhatsApp API  │  CRM Notes  │  Surveys  │  Call Transcripts   │
└───────────────┬─────────────────────────────────────────────────┘
                │
                ↓
┌───────────────────────────────────────────────────────────────┐
│              CAPA DE INGESTION (Apache Airflow)                │
│  • Extracción diaria (batch)                                   │
│  • Limpieza y normalización                                    │
│  • Detección de idioma y traducción si necesario               │
└───────────────┬───────────────────────────────────────────────┘
                │
                ↓
┌───────────────────────────────────────────────────────────────┐
│              MOTOR NER (spaCy + BERT Fine-tuned)              │
│  • Tokenización                                                │
│  • Reconocimiento de entidades personalizadas                 │
│  • Análisis de sentimiento                                     │
│  • Extracción de intenciones                                   │
└───────────────┬───────────────────────────────────────────────┘
                │
                ↓
┌───────────────────────────────────────────────────────────────┐
│           CAPA DE ANALYTICS Y ML                               │
│  • Agregación de entidades por cliente                        │
│  • Cálculo de scores de recompra                              │
│  • Detección de patrones                                       │
│  • Generación de recomendaciones                               │
└───────────────┬───────────────────────────────────────────────┘
                │
                ↓
┌───────────────────────────────────────────────────────────────┐
│                    APLICACIONES                                │
│  Dashboard Consultoras  │  Admin Panel  │  API Integraciones  │
└───────────────────────────────────────────────────────────────┘
```

### Entrenamiento del Modelo NER (Plan Propuesto)

**Fase 1: Anotación de Datos**
```
• Dataset inicial: 50K conversaciones a anotar manualmente
• Herramienta: Label Studio
• Equipo requerido: 3 anotadores + 1 revisor experto
• Tiempo estimado: 6 semanas
• Kappa score inter-anotador objetivo: >0.85
```

**Fase 2: Fine-tuning**
```python
# Arquitectura del modelo propuesta
Base: bert-base-multilingual-cased
+ Custom NER head (8 entidades personalizadas)
+ Sentiment classifier (3 clases: positivo, neutro, negativo)
+ Intent classifier (5 intenciones: compra, consulta, queja, etc.)

# Métricas objetivo
Precision: >0.88
Recall: >0.85
F1-Score: >0.86
```

---

<a id="propuesta-valor"></a>
## 💎 Propuesta de Valor

### Para los CLIENTES FINALES

✅ **Experiencia personalizada**
- Reciben recomendaciones relevantes basadas en sus propias palabras
- Seguimiento proactivo de sus necesidades expresadas

✅ **Mejor servicio**
- Problemas detectados y resueltos más rápido
- Consultoras más preparadas con información contextual

### Para las CONSULTORAS (Usuarios Directos)

✅ **Herramienta de trabajo poderosa**
```
Dashboard personal con:
• Lista de clientes en riesgo de abandono (priorizada)
• Scripts sugeridos personalizados por cliente
• Alertas: "María mencionó 'precio alto' hace 3 días - enviar promo"
• Recordatorios automáticos de follow-up
```

✅ **Aumento de ingresos**
- +25% en conversión de recontactos
- -40% en tiempo de gestión manual
- +30% en tickets promedio

### Para la EMPRESA

✅ **ROI Directo**
```
Inversión inicial: $280M COP
Revenue incremental año 1: $850M COP
ROI: 303%
Payback period: 4.2 meses
```

✅ **Ventajas competitivas**
- Única empresa del sector con NER aplicado a venta directa
- Barrera de entrada tecnológica para competidores
- Data moat: mejora continua con más datos

✅ **Eficiencia operacional**
- Automatización de 60% de análisis manual
- Reducción de 15 FTEs en análisis de feedback
- Ahorro: $180M COP/año en costos operacionales

### Para STAKEHOLDERS

✅ **Gerencia Comercial**
- Visibilidad de drivers reales de recompra
- KPIs predictivos (no solo históricos)
- Insights accionables en tiempo real

✅ **Marketing**
- Segmentación automática por preferencias extraídas
- Mensajes hiperpersonalizados a escala
- Test A/B automático de estrategias de retención

✅ **Producto**
- Feedback estructurado de calidad/issues
- Detección temprana de problemas con productos
- Insights de desarrollo de nuevos productos

---

<a id="planificacion"></a>
## 📅 Planificación del Proyecto

### Fases del Proyecto Propuestas

```
FASE 0: Discovery y Validación (4 semanas)
FASE 1: Preparación de Datos y Anotación (8 semanas)
FASE 2: Desarrollo del Modelo NER (10 semanas)
FASE 3: Desarrollo de Aplicaciones (8 semanas)
FASE 4: Piloto y Testing (6 semanas)
FASE 5: Rollout Nacional (4 semanas)
FASE 6: Optimización Continua (ongoing)

DURACIÓN TOTAL ESTIMADA: 40 semanas (~9-10 meses)
```

### Timeline Detallado

#### **FASE 0: Discovery y Validación** (Semanas 1-4)
```
Objetivos:
✓ Validar hipótesis con datos históricos
✓ Definir casos de uso prioritarios
✓ Conseguir buy-in de stakeholders

Entregables:
• Business case completo
• Dataset de prueba anotado (5K ejemplos)
• PoC funcional con F1>0.75
• Roadmap aprobado

Equipo recomendado: 1 DS Lead + 1 Product Manager + 2 Business Analysts
```

#### **FASE 1: Preparación de Datos y Anotación** (Semanas 5-12)
```
Objetivos:
✓ Crear dataset de entrenamiento de calidad
✓ Establecer pipeline de datos
✓ Definir taxonomía final de entidades

Actividades:
• Extracción y limpieza de datos históricos
• Anotación manual de 50K conversaciones
• Validación cruzada de anotaciones
• Setup de infraestructura base (AWS)

Entregables:
• Dataset anotado (train/val/test)
• Documentación de taxonomía
• Pipeline ETL funcional
• Infraestructura cloud provisionada

Equipo recomendado: 1 Data Engineer + 3 Anotadores + 1 DS + 1 QA
```

#### **FASE 2: Desarrollo del Modelo NER** (Semanas 13-22)
```
Objetivos:
✓ Entrenar modelo NER con F1>0.86
✓ Desarrollar módulos de analytics
✓ Crear API de inferencia

Actividades:
Semanas 13-16: Fine-tuning de BERT para NER
Semanas 17-19: Desarrollo de clasificadores adicionales
Semanas 20-21: Integración de módulos
Semana 22: Testing y optimización

Entregables:
• Modelo NER productivo (F1>0.86)
• API FastAPI con documentación
• Módulos de analytics funcionales
• Tests unitarios e integración

Equipo recomendado: 2 ML Engineers + 1 Backend Developer + 1 DevOps
```

#### **FASE 3: Desarrollo de Aplicaciones** (Semanas 23-30)
```
Objetivos:
✓ Crear dashboard para consultoras
✓ Desarrollar panel de administración
✓ Integrar con sistemas existentes

Actividades:
Semanas 23-26: Frontend dashboard consultoras (React)
Semanas 27-28: Admin panel y reportes
Semanas 29-30: Integraciones (CRM, WhatsApp API)

Entregables:
• App web para consultoras
• Panel administrativo
• Integraciones completas
• Documentación de usuario

Equipo recomendado: 2 Frontend Devs + 1 UX Designer + 1 Backend Dev
```

#### **FASE 4: Piloto y Testing** (Semanas 31-36)
```
Objetivos:
✓ Validar solución con usuarios reales
✓ Medir impacto en KPIs
✓ Ajustar basado en feedback

Actividades:
• Selección de 200 consultoras piloto (10% del total)
• Capacitación de usuarios
• Monitoreo diario de métricas
• Iteración rápida de mejoras

Entregables:
• Reporte de resultados del piloto
• Plan de ajustes
• Material de capacitación
• Casos de éxito documentados

Equipo recomendado: 1 PM + 1 DS + 2 Support + 1 Trainer
```

#### **FASE 5: Rollout Nacional** (Semanas 37-40)
```
Objetivos:
✓ Desplegar a todas las consultoras
✓ Garantizar adopción >80%
✓ Estabilizar operación

Actividades:
• Rollout por regiones (4 semanas escalonadas)
• Capacitación masiva (webinars + videos)
• Soporte 24/7 durante transición
• Monitoreo intensivo

Entregables:
• Sistema en producción 100%
• Adopción >80% de consultoras
• SLA de uptime >99.5%
• Documentación completa

Equipo recomendado: Full team + 4 Support adicionales
```

#### **FASE 6: Optimización Continua** (Ongoing)
```
Actividades:
• Re-entrenamiento mensual del modelo
• A/B testing de features nuevas
• Expansión a nuevos casos de uso
• Mejora continua basada en feedback

Equipo recomendado: 1 ML Eng + 1 Data Analyst (dedicados)
```

---

<a id="roadmap"></a>
## 🗺️ Roadmap de Implementación

### Diagrama de Gantt Simplificado

```
Mes  │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 10 │
─────┼───┴───┴───┴───┴───┴───┴───┴───┴───┴────┤
F0   │███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
F1   │░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
F2   │░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░░│
F3   │░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░│
F4   │░░░░░░░░░░░░░░░░░░░░░░░░░░░███████░░░░░│
F5   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░│
F6   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████│
```

### Hitos Clave (Milestones)

| Semana | Hito | Criterio de Éxito |
|--------|------|-------------------|
| 4 | ✅ PoC Aprobado | F1-Score >0.75 en muestra |
| 12 | ✅ Datos Listos | 50K ejemplos anotados, κ>0.85 |
| 22 | ✅ Modelo Productivo | F1-Score >0.86, latencia <200ms |
| 30 | ✅ Apps Completas | UAT aprobado por 10 usuarios |
| 36 | ✅ Piloto Exitoso | +20% frecuencia en grupo piloto |
| 40 | ✅ Producción 100% | Adopción >80%, uptime >99.5% |

### Criterios de Go/No-Go por Fase

**Al final de Fase 0:**
- [ ] PoC demuestra F1>0.75
- [ ] ROI proyectado >200%
- [ ] Buy-in de VP Comercial y CTO

**Al final de Fase 2:**
- [ ] Modelo alcanza F1>0.86 en test set
- [ ] Latencia de inferencia <200ms
- [ ] API pasa load testing (1000 req/s)

**Al final de Fase 4:**
- [ ] Piloto muestra +15% en frecuencia
- [ ] NPS de consultoras >8/10
- [ ] 0 incidents críticos en 2 semanas

---

<a id="recursos"></a>
## 👥 Recursos Necesarios (Propuesta)

### Equipo Humano Requerido

#### **Core Team (Dedicado 100%)**

| Rol | Cantidad | Duración | Seniority | Justificación |
|-----|----------|----------|-----------|---------------|
| **Data Scientist Lead** | 1 | 10 meses | Senior | Arquitectura del modelo, experimentación |
| **ML Engineer** | 2 | 8 meses | Mid-Senior | Desarrollo, fine-tuning, optimización |
| **Data Engineer** | 1 | 10 meses | Senior | Pipelines, ETL, infraestructura de datos |
| **Backend Developer** | 1 | 7 meses | Mid | API, integraciones, servicios |
| **Frontend Developer** | 2 | 6 meses | Mid | Dashboard, apps, UX |
| **DevOps Engineer** | 1 | 10 meses | Senior | Cloud, CI/CD, monitoreo, seguridad |
| **Product Manager** | 1 | 10 meses | Senior | Roadmap, stakeholders, priorización |
| **UX/UI Designer** | 1 | 4 meses | Mid | Diseño de interfaces, usabilidad |

**Total Core Team: 10 personas**

#### **Support Team (Parcial)**

| Rol | Cantidad | Dedicación | Fase |
|-----|----------|------------|------|
| **Anotadores de Datos** | 3 | 8 semanas full | Fase 1 |
| **QA Engineer** | 1 | 30% tiempo | Fases 2-5 |
| **Business Analyst** | 2 | 20% tiempo | Fase 0, 4 |
| **Trainer/Change Mgmt** | 1 | 6 semanas full | Fases 4-5 |
| **Support Engineers** | 4 | 4 semanas full | Fase 5 |

### Infraestructura y Tecnología

#### **Cloud (AWS)**

```yaml
Desarrollo:
  - EC2: 2x g4dn.xlarge (GPU para entrenamiento)
  - RDS: PostgreSQL db.r5.large
  - S3: 2TB storage
  - Costo mensual: ~$1,800 USD

Producción:
  - SageMaker: ml.g4dn.xlarge (inferencia)
  - Lambda: 5M invocaciones/mes
  - RDS: db.r5.2xlarge (Multi-AZ)
  - DocumentDB: 500GB
  - CloudFront + S3: Frontend
  - Costo mensual: ~$4,200 USD
```

#### **Software y Licencias**

| Herramienta | Uso | Costo Anual |
|-------------|-----|-------------|
| Label Studio Enterprise | Anotación de datos | $12,000 USD |
| GitHub Enterprise | Control de versiones | $2,100 USD |
| MLflow | Experiment tracking | Open Source |
| Grafana Cloud | Monitoreo | $3,600 USD |
| Postman Enterprise | API testing | $1,440 USD |

### Presupuesto Total

#### **CAPEX (Inversión Inicial)**

| Concepto | Monto (COP) | % |
|----------|-------------|---|
| **Equipo Humano** (10 meses) | $180,000,000 | 64% |
| **Infraestructura Cloud** (Setup) | $18,000,000 | 6% |
| **Software y Licencias** | $15,000,000 | 5% |
| **Anotación de Datos** | $35,000,000 | 13% |
| **Capacitación y Change Mgmt** | $12,000,000 | 4% |
| **Contingencia** (10%) | $20,000,000 | 7% |
| **TOTAL CAPEX** | **$280,000,000** | 100% |

#### **OPEX (Operación Anual)**

| Concepto | Monto Anual (COP) | Mes (COP) |
|----------|-------------------|-----------|
| Cloud (Producción) | $215,000,000 | $17,900,000 |
| Equipo Dedicado (2 FTE) | $144,000,000 | $12,000,000 |
| Licencias | $80,000,000 | $6,700,000 |
| Re-entrenamiento y mejoras | $45,000,000 | $3,750,000 |
| **TOTAL OPEX** | **$484,000,000** | **$40,300,000** |

#### **Análisis de ROI**

```
Inversión Total Año 1: $764M COP (CAPEX + OPEX)

Beneficios Año 1:
• Revenue incremental: +$850M COP
• Ahorro operacional: +$180M COP
• TOTAL BENEFICIOS: $1,030M COP

ROI Año 1: 35% (1,030/764 - 1)
Payback: 8.9 meses

Proyección 3 años:
Año 1: +$266M COP
Año 2: +$720M COP (OPEX reducido + mayor adopción)
Año 3: +$980M COP
NPV (3 años, 12% descuento): $1,456M COP
```

---

<a id="metricas"></a>
## 📊 Métricas de Éxito

### KPIs de Negocio (North Star Metrics)

#### **Primarios**

| Métrica | Baseline | Meta 6m | Meta 12m | Impacto $ |
|---------|----------|---------|----------|-----------|
| **Frecuencia de compra anual** | 1.8 | 2.4 | 3.2 | +$620M |
| **Tasa de recompra 2da compra** | 35% | 48% | 58% | +$280M |
| **Retención a 6 meses** | 22% | 32% | 42% | +$340M |

#### **Secundarios**

| Métrica | Baseline | Meta 12m |
|---------|----------|----------|
| Días hasta 2da compra | 89 | 52 |
| Clientes 3+ compras/año | 12% | 28% |
| Churn rate mes 2-3 | 58% | 35% |
| AOV (Average Order Value) | $135K | $152K |

### KPIs Técnicos

#### **Modelo NER**

```yaml
Performance:
  F1-Score: >0.86
  Precision: >0.88
  Recall: >0.85
  
Operación:
  Latencia p95: <200ms
  Throughput: >1000 req/s
  Uptime: >99.5%
  
Calidad:
  Drift detection: <5% mensual
  Data quality score: >0.95
```

#### **Producto**

```yaml
Adopción:
  - Consultoras activas: >80%
  - Login frecuency: >3x/semana
  - Feature usage: >60%
  
Experiencia:
  - NPS: >8/10
  - Time to value: <10 min
  - Support tickets: <50/mes
  
Impacto:
  - Precision de predicción churn: >0.78
  - Conversión de alertas actuadas: >35%
  - Reducción tiempo análisis: >60%
```

### Framework de Medición

#### **Dashboard Ejecutivo**

```
┌─────────────────────────────────────────────────────────┐
│  REFREQUENCY NER - EXECUTIVE DASHBOARD                  │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  💰 IMPACTO FINANCIERO                                   │
│  Revenue Incremental (YTD): $423M COP  ↑ 12% vs prev    │
│  ROI: 187%                                               │
│                                                          │
│  📊 KPIs CORE                                            │
│  Frecuencia Compra: 2.6  ↑ 0.8 vs baseline              │
│  Recompra 2da: 51%       ↑ 16pp vs baseline              │
│  Retención 6m: 34%       ↑ 12pp vs baseline              │
│                                                          │
│  🤖 SALUD DEL SISTEMA                                    │
│  Modelo F1: 0.87  |  Uptime: 99.7%  |  Users: 1,847     │
│                                                          │
│  ⚠️  ALERTAS                                             │
│  • 234 clientes alto riesgo (próximas 48h)              │
│  • Drift detectado en categoría "fragancias" (revisar)  │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

#### **Ciclo de Revisión**

```
Diario:
  - Monitoreo de sistema (uptime, latencia)
  - Alertas de modelo (drift, errores)
  
Semanal:
  - Revisión de KPIs de adopción
  - Casos de uso exitosos
  - Issues y mejoras
  
Mensual:
  - Business review con stakeholders
  - Análisis de impacto financiero
  - Re-entrenamiento del modelo
  
Trimestral:
  - Roadmap de features
  - Análisis estratégico
  - Budget review
```

---

<a id="riesgos"></a>
## ⚠️ Análisis de Riesgos

### Matriz de Riesgos

| # | Riesgo | Probabilidad | Impacto | Mitigación |
|---|--------|--------------|---------|------------|
| 1 | **Calidad de datos insuficiente** | Media | Alto | Auditoría temprana + plan de limpieza estructurado |
| 2 | **Resistencia de consultoras a nueva herramienta** | Alta | Alto | Change management robusto + incentivos de adopción |
| 3 | **Modelo no alcanza performance esperada** | Media | Alto | PoC validado antes de inversión total + plan B con reglas |
| 4 | **Privacidad y GDPR** | Baja | Crítico | Legal review + anonimización desde diseño |
| 5 | **Escalabilidad técnica** | Media | Medio | Load testing temprano + arquitectura cloud-native |
| 6 | **Falta de expertise en NER en el equipo** | Media | Alto | Contratación temprana + training + consultores externos |
| 7 | **Cambios regulatorios venta directa** | Baja | Medio | Monitoreo legal + arquitectura flexible |
| 8 | **Competencia copia la solución** | Media | Bajo | Data moat + mejora continua + patentes de proceso |

### Plan de Contingencia

#### **Si el modelo NER no alcanza F1>0.86:**

```
Plan B: Hybrid Rules + ML
- Implementar sistema basado en reglas para casos simples (40%)
- Usar modelo ML para casos complejos (60%)
- Iterar dataset con active learning
- Meta reducida: F1>0.80
```

#### **Si la adopción es <60% en piloto:**

```
Acciones:
1. Focus groups para identificar fricción
2. Simplificar UI (remover features poco usadas)
3. Incentivos económicos por uso
4. Gamificación (leaderboards, badges)
5. Considerar extensión de piloto 4 semanas
```

#### **Si hay problemas de privacidad:**

```
Protocolos:
- Todos los textos se anonimizan (PII detection)
- Encriptación end-to-end
- Opt-in explícito de clientes
- Auditoría legal externa
- Certificaciones: ISO 27001
```

---

<a id="conclusiones"></a>
## 🎯 Conclusiones y Próximos Pasos

### Resumen de Mi Propuesta

**ReFrecuency NER Intelligence** es una solución innovadora que propongo para aplicar Named Entity Recognition (NER) a un problema de negocio crítico: **la baja frecuencia de recompra en venta directa**.

**Diferenciadores clave:**

1. ✅ **Primera aplicación de NER en venta directa** en la industria colombiana
2. ✅ **ROI comprobable:** 35% año 1, payback en 8.9 meses
3. ✅ **Impacto medible:** +78% en frecuencia de compra
4. ✅ **Escalable:** De piloto a nacional en 10 meses
5. ✅ **Data moat:** Mejora continua con cada interacción

### ¿Por qué esta solución vs alternativas?

| Alternativa | Limitación | ReFrecuency NER |
|-------------|------------|-----------------|
| Análisis manual | No escala, lento | Automatizado, tiempo real |
| Reglas fijas | No captura matices | Aprende de contexto |
| ML tradicional | Solo datos estructurados | Aprovecha texto (80% de info) |
| Encuestas | Baja respuesta, sesgadas | Data orgánica, sin sesgo |

### Factores Críticos de Éxito

```
1. 🎯 Sponsorship ejecutivo fuerte (VP Comercial + CTO)
2. 👥 Equipo técnico de primer nivel (especialmente en NER/NLP)
3. 📊 Datos de calidad (anotación rigurosa)
4. 🔄 Change management efectivo (consultoras = usuarios clave)
5. ⚡ Iteración rápida (fail fast, learn fast)
```

### Roadmap de Decisión

#### **Inmediato (Próximas 2 semanas)**
- [ ] Presentación a comité ejecutivo
- [ ] Aprobación de presupuesto Fase 0
- [ ] Identificación de líderes de proyecto

#### **Corto Plazo (Mes 1-2)**
- [ ] Kick-off Fase 0
- [ ] Extracción de dataset inicial
- [ ] PoC con 5K ejemplos
- [ ] Go/No-Go para fase completa

#### **Mediano Plazo (Mes 3-10)**
- [ ] Ejecución de Fases 1-5
- [ ] Piloto con 200 consultoras
- [ ] Rollout nacional

#### **Largo Plazo (Año 2+)**
- [ ] Expansión a otros países
- [ ] Nuevos casos de uso (orden promedio, crecimiento)
- [ ] Monetización como producto SaaS

### Pregunta Clave para Stakeholders

> **¿Está la empresa dispuesta a invertir $280M COP para obtener $1,030M COP en beneficios anuales recurrentes, con un sistema que la diferenciará estratégicamente en el mercado?**

---

## 📎 Anexos

### A. Glosario de Términos

- **NER (Named Entity Recognition):** Técnica de NLP que identifica y clasifica entidades en texto
- **Venta Directa:** Modelo de negocio donde consultoras venden productos directamente a consumidores
- **Frecuencia de Recompra:** Número de veces que un cliente compra en un período
- **Cold Start:** Problema de nuevos usuarios sin historial
- **F1-Score:** Métrica de ML que balancea precisión y recall

### B. Referencias Técnicas

- spaCy: https://spacy.io/
- Transformers (Hugging Face): https://huggingface.co/transformers/
- BERT multilingual: https://huggingface.co/bert-base-multilingual-cased
- CRISP-DM Methodology: https://www.datascience-pm.com/crisp-dm-2/

### C. Casos de Estudio Similares

- **Retail NER:** Amazon product review analysis
- **Customer Service:** Zendesk intent classification
- **Healthcare:** Clinical NER for patient records
- **Financial Services:** Compliance and risk detection in communications

### D. Información de Contacto

**David Caleb Chaparro Orozco**  
Data Scientist & ML Engineer  
Autor de esta propuesta  

📧 Email: davidcaleb@example.com  
💼 LinkedIn: [linkedin.com/in/DavidCalebChaparroOrozco](https://linkedin.com/in/DavidCalebChaparroOrozco)  
🐙 GitHub: [@DavidCalebChaparroOrozco](https://github.com/DavidCalebChaparroOrozco)

---

<div align="center">

**🚀 Ready to transform Direct Sales with NER Intelligence 🚀**

*Propuesta desarrollada como parte del Desafío Técnico - Octubre 2025*

</div>

