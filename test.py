# ============================================================================
# 7.4 ESTRATEGIA DE PRODUCCIÓN Y DEPLOYMENT
# 
# ARCHIVO: test.py
# PROPÓSITO: Definir estrategia de producción de forma modular
# AUTOR: David Caleb
# FECHA: Octubre 2025
#
# Este script puede ejecutarse:
#   - De forma independiente: python test.py
#   - Desde el notebook: %run test.py
#   - Como módulo: from test import ProductionStrategy
# ============================================================================

# Imports necesarios
import matplotlib.pyplot as plt
import numpy as np

# ============================================================================
# MOCK RECOMMENDER PARA TESTING INDEPENDIENTE
# Si ejecutas desde el notebook, comentar esto y usar el recommender real
# ============================================================================

class MockRecommender:
    """
    Objeto mock para testing sin necesidad del notebook.
    
    Si ejecutas desde el notebook, este mock será reemplazado por el 
    objeto 'recommender' real que ya existe en el scope del notebook.
    """
    def __init__(self):
        self.models = {
            'popularity': {'type': 'popularity'},
            'item_based': {'type': 'item_based'},
            'svd': {'type': 'svd'},
            'hybrid': {'type': 'hybrid'}
        }
        print("[INFO] Usando MockRecommender para testing")

# ============================================================================
# CLASE PRINCIPAL: ProductionStrategy
# ============================================================================

print("\n" + "="*80)
print("ESTRATEGIA DE PRODUCCIÓN Y DEPLOYMENT")
print("="*80)

class ProductionStrategy:
    """Estrategia para llevar el modelo a producción"""
    
    def __init__(self, recommender):
        self.recommender = recommender
        self.deployment_plan = {}
        print("[OK] Estrategia de produccion inicializada")
    
    def define_architecture(self):
        """Definir arquitectura de producción"""
        
        architecture = {
            'components': {
                '1_data_storage': {
                    'name': 'Almacenamiento de Datos',
                    'technology': 'PostgreSQL / Data Warehouse',
                    'purpose': 'Almacenar transacciones, usuarios, productos'
                },
                '2_batch_processing': {
                    'name': 'Procesamiento Batch',
                    'technology': 'Python + pandas + scikit-learn',
                    'purpose': 'Generar recomendaciones para todos los usuarios',
                    'schedule': 'Diario a las 2 AM'
                },
                '3_recommendations_cache': {
                    'name': 'Cache de Recomendaciones',
                    'technology': 'Redis / Memcached',
                    'purpose': 'Almacenar recomendaciones pre-calculadas para acceso rapido',
                    'ttl': '24 horas'
                },
                '4_monitoring': {
                    'name': 'Monitorización',
                    'technology': 'Logs + Dashboard',
                    'purpose': 'Monitorear métricas y performance del sistema'
                }
            },
            'workflow': [
                '1. Transacciones diarias --> Data Warehouse',
                '2. Proceso batch nocturno --> Genera recomendaciones',
                '3. Recomendaciones --> Cache (Redis)',
                '4. Frontend consulta --> Cache (respuesta <10ms)',
                '5. Metricas --> Sistema de monitoreo'
            ]
        }
        
        print("\n[ARQUITECTURA DE PRODUCCION]")
        print("="*80)
        
        print("\nComponentes del Sistema:")
        for comp_id, comp in architecture['components'].items():
            print(f"\n{comp['name']}:")
            print(f"  • Tecnología: {comp['technology']}")
            print(f"  • Propósito: {comp['purpose']}")
            if 'schedule' in comp:
                print(f"  • Schedule: {comp['schedule']}")
        
        print("\n\nFlujo de Trabajo:")
        for i, step in enumerate(architecture['workflow'], 1):
            print(f"  {i}. {step}")
        
        return architecture
    
    def estimate_resources(self):
        """Estimar recursos necesarios"""
        
        n_users = 37570
        n_products = 7134
        n_recommendations_per_user = 10
        
        total_recommendations = n_users * n_recommendations_per_user
        storage_per_rec = 100
        total_storage_mb = (total_recommendations * storage_per_rec) / (1024 ** 2)
        
        users_per_second = 50
        total_processing_time_hours = (n_users / users_per_second) / 3600
        
        resources = {
            'storage': {
                'recommendations_cache': f'{total_storage_mb:.1f} MB',
                'model_files': '~500 MB',
                'total_estimated': f'{total_storage_mb/1024 + 2.5:.1f} GB'
            },
            'compute': {
                'batch_processing': '4-8 CPU cores',
                'memory': '16-32 GB RAM',
                'processing_time': f'{total_processing_time_hours:.1f} horas'
            },
            'costs_monthly': {
                'infrastructure': '$200-400 USD',
                'storage': '$50-100 USD',
                'total': '$300-550 USD/mes'
            }
        }
        
        print("\n[ESTIMACION DE RECURSOS]")
        print("="*80)
        
        print(f"\nAlmacenamiento:")
        for key, value in resources['storage'].items():
            print(f"  • {key.replace('_', ' ').title()}: {value}")
        
        print(f"\nCómputo:")
        for key, value in resources['compute'].items():
            print(f"  • {key.replace('_', ' ').title()}: {value}")
        
        print(f"\nCostos Mensuales Estimados:")
        for key, value in resources['costs_monthly'].items():
            print(f"  • {key.replace('_', ' ').title()}: {value}")
        
        return resources
    
    def define_rollout_plan(self):
        """Definir plan de rollout gradual"""
        
        rollout = {
            'phase_1': {
                'name': 'Piloto Interno (Semana 1)',
                'users': '5%',
                'goals': 'Validar funcionalidad básica'
            },
            'phase_2': {
                'name': 'Rollout Limitado (Semanas 2-3)',
                'users': '20%',
                'goals': 'Validar escalabilidad'
            },
            'phase_3': {
                'name': 'Rollout Parcial (Semana 4)',
                'users': '50%',
                'goals': 'Recopilar métricas de negocio'
            },
            'phase_4': {
                'name': 'Rollout Completo (Semana 5+)',
                'users': '100%',
                'goals': 'Operación normal'
            }
        }
        
        print("\n[PLAN DE ROLLOUT GRADUAL]")
        print("="*80)
        
        for phase_id, phase in rollout.items():
            print(f"\n{phase['name']}:")
            print(f"  • Cobertura: {phase['users']}")
            print(f"  • Objetivos: {phase['goals']}")
        
        return rollout
    
    def visualize_deployment_timeline(self):
        """Visualizar timeline de deployment"""
        
        fig, ax = plt.subplots(figsize=(16, 8))
        
        phases = [
            {'name': 'Preparación', 'start': 0, 'duration': 7, 'color': '#3498db'},
            {'name': 'Staging Test', 'start': 7, 'duration': 3, 'color': '#9b59b6'},
            {'name': 'Piloto 5%', 'start': 10, 'duration': 7, 'color': '#f39c12'},
            {'name': 'Rollout 20%', 'start': 17, 'duration': 7, 'color': '#e67e22'},
            {'name': 'Rollout 50%', 'start': 24, 'duration': 7, 'color': '#e74c3c'},
            {'name': 'Rollout 100%', 'start': 31, 'duration': 7, 'color': '#27ae60'},
            {'name': 'Monitoring', 'start': 38, 'duration': 14, 'color': '#95a5a6'},
        ]
        
        for i, phase in enumerate(phases):
            ax.barh(i, phase['duration'], left=phase['start'], 
                   height=0.6, color=phase['color'], alpha=0.8,
                   edgecolor='black', linewidth=1.5)
            
            ax.text(phase['start'] + phase['duration']/2, i, 
                   phase['name'], 
                   ha='center', va='center', fontweight='bold', 
                   fontsize=10, color='white')
            
            ax.text(phase['start'] + phase['duration'] + 1, i, 
                   f"{phase['duration']}d", 
                   va='center', fontsize=9)
        
        ax.set_yticks(range(len(phases)))
        ax.set_yticklabels([])
        ax.set_xlabel('Días desde inicio', fontsize=12, fontweight='bold')
        ax.set_title('Timeline de Deployment - Sistema de Recomendacion', 
                    fontsize=14, fontweight='bold', pad=20)
        ax.grid(True, axis='x', alpha=0.3)
        ax.set_xlim(0, 55)
        
        milestones = [(10, 'Go Live Piloto'), (31, 'Go Live Producción'), 
                     (52, 'Fin Monitoreo')]
        
        for day, label in milestones:
            ax.axvline(x=day, color='red', linestyle='--', linewidth=2, alpha=0.5)
            ax.text(day, len(phases) - 0.5, label, 
                   rotation=90, va='bottom', fontsize=9, fontweight='bold')
        
        plt.tight_layout()
        plt.show()

# ============================================================================
# BLOQUE DE EJECUCIÓN
# Se ejecuta solo si el script se corre directamente (no si se importa)
# ============================================================================

if __name__ == '__main__':
    # Configuración
    SHOW_PLOTS = True  # Cambiar a False si ejecutas en modo consola sin GUI
    
    # Verificar si recommender ya existe (cuando se ejecuta desde notebook)
    if 'recommender' not in dir():
        # Si no existe, usar el mock
        recommender = MockRecommender()
    else:
        print("[OK] Usando objeto 'recommender' del notebook")
    
    # Inicializar estrategia
    prod_strategy = ProductionStrategy(recommender)
    
    # Definir arquitectura
    architecture = prod_strategy.define_architecture()
    
    # Estimar recursos
    resources = prod_strategy.estimate_resources()
    
    # Plan de rollout
    rollout = prod_strategy.define_rollout_plan()
    
    # Visualizar timeline (solo si SHOW_PLOTS es True)
    if SHOW_PLOTS:
        print("\n[INFO] Generando visualizacion de timeline...")
        try:
            prod_strategy.visualize_deployment_timeline()
        except Exception as e:
            print(f"[WARNING] No se pudo mostrar grafico: {e}")
            print("[INFO] Ejecuta desde Jupyter o activa GUI para ver graficos")
    else:
        print("\n[INFO] Visualizacion de graficos desactivada (SHOW_PLOTS=False)")
    
    print("\n" + "="*80)
    print("[OK] Estrategia de produccion documentada completamente")
    print("="*80)

# ============================================================================
# INSTRUCCIONES DE USO:
# ============================================================================
# 
# OPCIÓN 1: Ejecutar de forma independiente
#   python test.py
#
# OPCIÓN 2: Usar desde el notebook
#   # En una celda del notebook, después de entrenar el recommender:
#   %run test.py
#
# OPCIÓN 3: Importar como módulo
#   from test import ProductionStrategy
#   prod_strategy = ProductionStrategy(recommender)
#   architecture = prod_strategy.define_architecture()
#
# ============================================================================
