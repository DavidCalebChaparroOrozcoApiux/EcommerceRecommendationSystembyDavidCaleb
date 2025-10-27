"""
Script para consolidar el notebook eliminando versiones duplicadas y corregidas
Mantiene solo las versiones finales y mejoradas desde el inicio
"""

import json
import re

def consolidate_notebook(input_file, output_file):
    """Consolidar notebook eliminando duplicados y versiones corregidas"""
    
    # Leer notebook
    with open(input_file, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    cells = notebook['cells']
    consolidated_cells = []
    
    # Celdas a eliminar (índices)
    cells_to_skip = set()
    
    # Patrón para detectar celdas de corrección/mejora
    patterns_to_skip = [
        r'===.*CORREGID',
        r'===.*COMPLETAMENTE CORREGID',
        r'APLICANDO MEJORAS ADICIONALES',
        r'Esta sección implementa un modelo.*mejorado',
        r'def evaluate_models_fixed',
        r'También necesitamos corregir',
        r'Reemplazar la función original con la corregida',
        r'Ahora ejecutar la evaluación corregida',
        r'Y también corregir get_popular_recommendations'
    ]
    
    print(f"[*] Procesando {len(cells)} celdas...")
    
    # Primer paso: identificar celdas a eliminar
    for i, cell in enumerate(cells):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Verificar si es una celda de corrección
            for pattern in patterns_to_skip:
                if re.search(pattern, source, re.IGNORECASE):
                    cells_to_skip.add(i)
                    print(f"  [X] Celda {i}: Marcada para eliminar (correccion/mejora redundante)")
                    break
    
    # Segundo paso: consolidar celdas
    for i, cell in enumerate(cells):
        if i in cells_to_skip:
            continue
        
        # Limpiar outputs con mensajes de CORREGIDO/MEJORADO
        if cell['cell_type'] == 'code' and 'outputs' in cell and cell['outputs']:
            cleaned_outputs = []
            for output in cell['outputs']:
                should_keep = True
                
                if 'text' in output:
                    text = ''.join(output['text']) if isinstance(output['text'], list) else output['text']
                    
                    # Eliminar outputs que digan CORREGIDO/MEJORADO
                    if any(palabra in text.upper() for palabra in ['CORREGID', 'COMPLETAMENTE CORREGID']):
                        should_keep = False
                        print(f"  [-] Celda {i}: Limpiando output con mensajes de correccion")
                
                if should_keep:
                    cleaned_outputs.append(output)
            
            cell['outputs'] = cleaned_outputs
        
        # Limpiar código fuente
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Reemplazar nombres de funciones mejoradas a nombres estándar
            replacements = {
                'generate_recommendations_fixed': 'generate_recommendations',
                'generate_recommendations_final': 'generate_recommendations',
                'evaluate_models_fixed': 'evaluate_models',
                'evaluate_final_system': 'evaluate_models',
                'get_popular_recommendations_fixed': 'get_popular_recommendations',
                '_get_item_based_recommendations_enhanced': '_get_item_based_recommendations',
                '_get_hybrid_recommendations_enhanced': '_get_hybrid_recommendations',
                'enhanced_item_based_cf': 'item_based_cf',
                '_get_item_based_scores_enhanced': '_get_item_based_scores',
                'item_based_enhanced': 'item_based',
                'hybrid_enhanced': 'hybrid',
                'test_enhanced_system': 'test_system'
            }
            
            for old_name, new_name in replacements.items():
                if old_name in source:
                    source = source.replace(old_name, new_name)
                    print(f"  [~] Celda {i}: Renombrando {old_name} -> {new_name}")
            
            # Actualizar source
            cell['source'] = source.split('\n')
            if cell['source'] and cell['source'][-1] == '':
                cell['source'] = cell['source'][:-1]  # Eliminar línea vacía final
        
        # Limpiar textos de Markdown
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            
            # Eliminar frases sobre correcciones
            phrases_to_remove = [
                r'completamente corregida',
                r'versión corregida',
                r'mejorado con múltiples estrategias',
                r'con todos los modelos mejorados',
                r'Item-Based CF mejorado'
            ]
            
            for phrase in phrases_to_remove:
                if re.search(phrase, source, re.IGNORECASE):
                    source = re.sub(phrase, '', source, flags=re.IGNORECASE)
                    print(f"  [-] Celda {i}: Limpiando texto de Markdown")
            
            cell['source'] = source.split('\n')
            if cell['source'] and cell['source'][-1] == '':
                cell['source'] = cell['source'][:-1]
        
        consolidated_cells.append(cell)
    
    # Actualizar notebook
    notebook['cells'] = consolidated_cells
    
    # Guardar notebook consolidado
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=1)
    
    print(f"\n[OK] Notebook consolidado guardado en: {output_file}")
    print(f"[*] Celdas originales: {len(cells)}")
    print(f"[*] Celdas finales: {len(consolidated_cells)}")
    print(f"[*] Celdas eliminadas: {len(cells_to_skip)}")

if __name__ == '__main__':
    input_notebook = 'TestTecnicalbyDavidCaleb.ipynb'
    output_notebook = 'TestTecnicalbyDavidCaleb_consolidated.ipynb'
    
    print("="*80)
    print("CONSOLIDANDO NOTEBOOK")
    print("="*80)
    print(f"Entrada: {input_notebook}")
    print(f"Salida: {output_notebook}\n")
    
    consolidate_notebook(input_notebook, output_notebook)
    
    print("\n" + "="*80)
    print("CONSOLIDACION COMPLETADA")
    print("="*80)

