# 📸 GUÍA: Imágenes para la Presentación
## Inventario y Recomendaciones

**Autor:** David Caleb Chaparro Orozco  
**Para:** Sustentación Prueba Técnica

---

## ✅ IMÁGENES QUE YA TIENES

### **CasoEstudio1/** (2 imágenes)

#### 1. `DiagramadeGrantt.png`
- **Usar en:** Slide 7 (Planificación del Proyecto)
- **Muestra:** Gantt con las 6 fases del proyecto NER
- **Resolución:** 61KB - OK para presentación
- **Estado:** ✅ LISTA PARA USAR

#### 2. `FlujoDeDatos.png`
- **Usar en:** Slide 5 (Arquitectura Técnica)
- **Muestra:** Flujo desde fuentes de datos hasta aplicaciones
- **Resolución:** 168KB - Excelente calidad
- **Estado:** ✅ LISTA PARA USAR

---

### **CasoEstudio2/** (4 imágenes)

#### 1. `AnalisisExploratorioDatos.png`
- **Usar en:** Slide 10 (EDA)
- **Muestra:** Múltiples gráficos del análisis exploratorio
- **Resolución:** 191KB - Excelente calidad
- **Estado:** ✅ LISTA PARA USAR

#### 2. `DistribuccionValorxUnidad.png`
- **Usar en:** Slide 10 (EDA - complemento)
- **Muestra:** Distribución de valor por unidad
- **Resolución:** 44KB - OK
- **Estado:** ✅ LISTA PARA USAR

#### 3. `SistemaRecomendacion.png`
- **Usar en:** Slide 11 (Solución Multi-Algoritmo)
- **Muestra:** Arquitectura del sistema de recomendación
- **Resolución:** 74KB - OK
- **Estado:** ✅ LISTA PARA USAR

#### 4. `EvolucionPerformanceyEstrategiaReentrenamiento+DegradaciónAcumuladaDelModelo.png`
- **Usar en:** Slide 15 (Estrategia de Deployment)
- **Muestra:** Evolución de performance y estrategia de re-entrenamiento
- **Resolución:** 82KB - OK
- **Estado:** ✅ LISTA PARA USAR

---

## 🎨 RESUMEN DE COBERTURA

### ✅ Slides con Imagen (6 slides)
- Slide 5: FlujoDeDatos.png ✅
- Slide 7: DiagramadeGrantt.png ✅
- Slide 10: AnalisisExploratorioDatos.png + DistribuccionValorxUnidad.png ✅
- Slide 11: SistemaRecomendacion.png ✅
- Slide 15: EvolucionPerformance...png ✅

### 📝 Slides sin Imagen (14 slides)
Estos slides usan texto, tablas, diagramas simples que se pueden hacer en PowerPoint:
- Slide 1: Portada (texto + diseño)
- Slide 2: Contexto (texto + iconos)
- Slide 3: Problema (texto + números)
- Slide 4: Solución NER (diagrama simple)
- Slide 6: Propuesta de Valor (tabla + números)
- Slide 8: Justificación (tabla comparativa)
- Slide 9: Contexto Caso 2 (texto + números)
- Slide 12: CRISP-DM (diagrama de flujo)
- Slide 13: Resultados (tabla de métricas)
- Slide 14: Impacto Negocio (tabla + números)
- Slide 16: A/B Testing (diagrama simple)
- Slide 17: Comparativa (tabla)
- Slide 18: Aprendizajes (texto + bullets)
- Slide 19: Valor (grid de checkmarks)
- Slide 20: Contacto (texto + info)

**CONCLUSIÓN: Tienes todas las imágenes técnicas necesarias! ✅**

---

## 💡 IMÁGENES OPCIONALES (Si Quieres Mejorar)

### **Prioridad ALTA (Recomendadas)**

#### CasoEstudio2/comparacion_modelos.png
**Para:** Slide 13 (Resultados Técnicos)
**Código para generar desde tu notebook:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Datos
models = ['Popularidad', 'User-Based', 'Item-Based', 'SVD', 'Híbrido']
precision = [0.0017, 0.0017, 0.0017, 0.0017, 0.0034]
recall = [0.0172, 0.0115, 0.0172, 0.0057, 0.0230]
f1 = [0.0031, 0.0029, 0.0031, 0.0027, 0.0060]

x = np.arange(len(models))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 6))
bars1 = ax.bar(x - width, precision, width, label='Precision@10', color='#1f77b4')
bars2 = ax.bar(x, recall, width, label='Recall@10', color='#ff7f0e')
bars3 = ax.bar(x + width, f1, width, label='F1-Score', color='#2ca02c')

# Destacar el modelo híbrido
bars3[-1].set_color('#FFD700')  # Dorado
bars3[-1].set_edgecolor('black')
bars3[-1].set_linewidth(2)

ax.set_xlabel('Modelos', fontsize=12)
ax.set_ylabel('Score', fontsize=12)
ax.set_title('Comparación de Performance - 5 Modelos', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(models, rotation=15, ha='right')
ax.legend()
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('CasoEstudio2/comparacion_modelos.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

#### CasoEstudio2/impacto_negocio.png
**Para:** Slide 14 (Impacto en Negocio)
**Código:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Datos
metrics = ['CTR', 'Conversión', 'AOV', 'Engagement']
sin_sistema = [5.0, 2.0, 26853, 100]
con_sistema = [5.75, 2.2, 29000, 110]
lift = [15, 10, 8, 10]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico 1: Comparación Antes/Después
x = np.arange(len(metrics))
width = 0.35

bars1 = ax1.bar(x - width/2, sin_sistema, width, label='Sin Sistema', color='#d62728')
bars2 = ax1.bar(x + width/2, con_sistema, width, label='Con Sistema', color='#2ca02c')

ax1.set_ylabel('Valor', fontsize=11)
ax1.set_title('Impacto del Sistema de Recomendación', fontsize=13, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(metrics)
ax1.legend()
ax1.grid(axis='y', alpha=0.3)

# Añadir valores sobre las barras
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

# Gráfico 2: % de Mejora
colors = ['#00875A'] * len(metrics)
bars = ax2.barh(metrics, lift, color=colors, edgecolor='black', linewidth=1.5)
ax2.set_xlabel('Mejora (%)', fontsize=11)
ax2.set_title('Porcentaje de Mejora por Métrica', fontsize=13, fontweight='bold')
ax2.grid(axis='x', alpha=0.3)

# Añadir valores
for i, (metric, value) in enumerate(zip(metrics, lift)):
    ax2.text(value + 0.5, i, f'+{value}%', va='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('CasoEstudio2/impacto_negocio.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

#### CasoEstudio2/ab_test_visual.png
**Para:** Slide 16 (A/B Testing)
**Código:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Datos del A/B test
groups = ['Control\n(Popularidad)', 'Treatment\n(Híbrido)']
ctr = [5.37, 6.12]
colors = ['#d62728', '#2ca02c']

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(groups, ctr, color=colors, edgecolor='black', linewidth=2, width=0.5)

# Añadir valores sobre las barras
for i, (bar, value) in enumerate(zip(bars, ctr)):
    ax.text(bar.get_x() + bar.get_width()/2, value + 0.1, 
            f'{value}%', ha='center', va='bottom', 
            fontsize=16, fontweight='bold')

# Añadir línea de mejora
ax.plot([0, 1], [ctr[0], ctr[0]], 'k--', alpha=0.5, linewidth=1)
ax.annotate('', xy=(1, ctr[1]), xytext=(1, ctr[0]),
            arrowprops=dict(arrowstyle='<->', color='green', lw=2))
ax.text(1.15, (ctr[0] + ctr[1])/2, '+14.0%\nLift', 
        fontsize=12, fontweight='bold', color='green')

ax.set_ylabel('CTR (%)', fontsize=13)
ax.set_title('Resultados A/B Test - Click-Through Rate', 
             fontsize=15, fontweight='bold')
ax.set_ylim(0, 7)
ax.grid(axis='y', alpha=0.3)

# Añadir significancia
ax.text(0.5, 6.5, 'p-value < 0.05 ✓', ha='center', 
        fontsize=11, bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

plt.tight_layout()
plt.savefig('CasoEstudio2/ab_test_visual.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

### **Prioridad MEDIA (Opcionales)**

#### CasoEstudio1/roi_waterfall.png
**Para:** Slide 6 (Propuesta de Valor - Caso 1)
**Descripción:** Gráfico de cascada mostrando inversión → beneficios → ROI

**Herramienta:** Puedes usar Excel/PowerPoint para crear un waterfall chart simple

---

#### CasoEstudio1/dashboard_mockup.png
**Para:** Slide 6 (Valor para Consultoras)
**Descripción:** Mockup del dashboard que verían las consultoras

**Opciones para crear:**
1. **Figma** (gratis): https://figma.com
2. **PowerPoint:** Usar SmartArt y formas
3. **Canva** (gratis): https://canva.com

**Elementos del mockup:**
```
┌──────────────────────────────────────────────┐
│  Dashboard Consultora - María López          │
├──────────────────────────────────────────────┤
│                                              │
│  ⚠️ ALERTAS (3)                              │
│  • Cliente Ana: Score 35/100 - Contactar    │
│    hoy con promo crema                       │
│  • Cliente Juan: Riesgo alto - Llamar       │
│                                              │
│  📊 MIS CLIENTES HOY (12)                    │
│  • 3 en riesgo alto                          │
│  • 5 oportunidad de recompra                 │
│  • 4 satisfechos                             │
│                                              │
│  💬 SCRIPT SUGERIDO                          │
│  Para Ana: "Hola Ana! Vi que te gustó..."   │
│                                              │
│  📈 MIS MÉTRICAS                             │
│  • Conversión: 68% (↑12%)                    │
│  • Revenue: $2.3M este mes                   │
└──────────────────────────────────────────────┘
```

---

### **Prioridad BAJA (Solo si Sobra Tiempo)**

#### CasoEstudio1/ejemplo_ner_highlighted.png
**Para:** Slide 4 (Ejemplo de NER)
**Descripción:** Screenshot de WhatsApp con entidades resaltadas en colores

**Cómo crear:**
1. Toma un screenshot de WhatsApp (o crea uno falso en PowerPoint)
2. Usa highlighter para marcar entidades:
   - Amarillo: PRODUCTO
   - Verde: SENTIMIENTO positivo
   - Rojo: PROBLEMA
   - Azul: INTENCIÓN

---

## 🎯 RECOMENDACIÓN FINAL

### **Estrategia de Tiempo:**

#### Si tienes < 1 hora:
✅ **USA SOLO LAS IMÁGENES QUE YA TIENES**
- Tienes las 6 más importantes
- El resto se puede hacer con texto y tablas en PowerPoint
- Es más que suficiente para una sustentación profesional

#### Si tienes 1-2 horas:
✅ **AÑADE LAS 3 DE PRIORIDAD ALTA**
- `comparacion_modelos.png` - Mejora mucho el Slide 13
- `impacto_negocio.png` - Visualiza el valor claramente
- `ab_test_visual.png` - Hace el A/B test más tangible

#### Si tienes 3+ horas:
✅ **AÑADE MOCKUPS Y EXTRAS**
- Dashboard mockup en Figma (30 min)
- ROI waterfall en Excel (20 min)
- Ejemplo NER highlighted (15 min)

---

## 📋 CHECKLIST DE IMÁGENES

### Imágenes Existentes ✅
- [x] CasoEstudio1/DiagramadeGrantt.png
- [x] CasoEstudio1/FlujoDeDatos.png
- [x] CasoEstudio2/AnalisisExploratorioDatos.png
- [x] CasoEstudio2/DistribuccionValorxUnidad.png
- [x] CasoEstudio2/SistemaRecomendacion.png
- [x] CasoEstudio2/EvolucionPerformanceyEstrategiaReentrenamiento.png

### Imágenes Opcionales (Prioridad Alta) ⭐
- [ ] CasoEstudio2/comparacion_modelos.png
- [ ] CasoEstudio2/impacto_negocio.png
- [ ] CasoEstudio2/ab_test_visual.png

### Imágenes Opcionales (Prioridad Media)
- [ ] CasoEstudio1/roi_waterfall.png
- [ ] CasoEstudio1/dashboard_mockup.png

### Imágenes Opcionales (Prioridad Baja)
- [ ] CasoEstudio1/ejemplo_ner_highlighted.png

---

## 💻 INSERTAR IMÁGENES EN POWERPOINT

### **Método 1: Insertar Directamente**
```
1. Slide → Insertar → Imágenes → Este dispositivo
2. Navegar a CasoEstudio1/ o CasoEstudio2/
3. Seleccionar imagen
4. Ajustar tamaño (mantener proporciones)
5. Centrar en la slide
```

### **Método 2: Desde Código**
Si generas gráficos nuevos, el código ya incluye:
```python
plt.savefig('ruta/nombre.png', dpi=300, bbox_inches='tight')
```
Esto crea imágenes de alta calidad listas para usar.

### **Tamaño Recomendado en PowerPoint:**
- Ancho: 20-24 cm para gráficos principales
- Ancho: 15-18 cm para gráficos secundarios
- Resolución: 300 DPI (ya están así)
- Formato: PNG (mejor que JPG para gráficos)

---

## ✅ CONCLUSIÓN

**TIENES TODO LO NECESARIO!**

Las 6 imágenes que ya tienes cubren los aspectos técnicos más importantes:
- Arquitectura (2 imágenes)
- Planificación (1 imagen)
- Análisis de datos (2 imágenes)
- Performance (1 imagen)

El resto de la presentación se puede hacer perfectamente con:
- Tablas (PowerPoint tiene excelentes templates)
- Diagramas simples (SmartArt de PowerPoint)
- Texto estructurado con bullets
- Números grandes y destacados

**Mi recomendación:** Si vas en el Slide 15 y el tiempo apremia, **usa solo las imágenes existentes** y enfócate en practicar la presentación y preparar respuestas a preguntas. La sustentación exitosa depende más de tu claridad al explicar que de tener 20 gráficos perfectos.

**¡Éxito en tu presentación!** 🚀

---

*Guía creada: Octubre 2025*  
*Autor: David Caleb Chaparro Orozco*

