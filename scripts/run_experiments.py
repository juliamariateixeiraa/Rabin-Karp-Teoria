# scripts/run_experiments.py

import time
import random
import string
import csv
import sys
from pathlib import Path

# Adiciona o diretório 'src' ao caminho de módulos do Python.
sys.path.append(str(Path(__file__).parent.parent)) 
# ^^^ Aponta para a pasta raiz do projeto, que contém 'src'

try:
    # A importação deve ser feita do pacote 'src.python'
    from src.python.rabin_karp import RabinKarp
except ImportError:
    print("ERRO CRÍTICO: Não foi possível importar o módulo RabinKarp.")
    print("Verifique se 'rabin_karp.py' está em 'src/python/'.")
    sys.exit(1)


# --- CONFIGURAÇÕES DE EXPERIMENTO ---
NUM_REPETICOES = 25  # Repetições (de 15 a 30)
SAIDA_CSV_PYTHON = Path(__file__).parent.parent / 'data' / 'raw_times_python.csv'

# Definições de tamanhos para textos e padrões
TAMANHOS_TEXTO = [10**4, 10**5, 5*10**5] # Pequeno, Médio, Grande
TAMANHOS_PADRAO = [10, 50, 200]        

# --- FUNÇÕES DE GERAÇÃO DE DADOS ---

def generate_random_string(length, char_set=string.ascii_letters + string.digits):
    """Gera uma string aleatória."""
    return ''.join(random.choice(char_set) for _ in range(length))

def generate_test_case(text_size, pattern_size, case_type):
    """
    Gera o texto (T) e o padrão (P) para os cenários de complexidade.
    """
    
    if case_type == 'worst':
        # Pior Caso (O(N*M)): Força colisões com repetição do mesmo caractere.
        char = 'a'
        text = char * text_size
        pattern = char * pattern_size
        
    elif case_type == 'best':
        # Melhor Caso (O(N+M)): Padrão no início (mínimo de shifts)
        pattern = generate_random_string(pattern_size)
        text = pattern + generate_random_string(text_size - pattern_size)
        
    elif case_type == 'average':
        # Caso Médio: Padrão no meio
        pattern = generate_random_string(pattern_size)
        text = generate_random_string(text_size)
        mid_index = text_size // 2 - pattern_size // 2
        text = text[:mid_index] + pattern + text[mid_index + pattern_size:]
        
    else:
        raise ValueError("Tipo de caso inválido.")
    
    return text, pattern, case_type

# --- FUNÇÃO PRINCIPAL DE EXECUÇÃO ---

def run_all_experiments():
    """Executa todos os testes e salva os dados brutos em CSV."""
    
    rk = RabinKarp()
    results = []
    
    # Cabeçalho do CSV
    results.append(['language', 'text_size', 'pattern_size', 'case_type', 'run_number', 'execution_time_seconds'])

    # Iterar sobre todos os cenários
    for t_size in TAMANHOS_TEXTO:
        for p_size in TAMANHOS_PADRAO:
            if p_size > t_size: continue

            for case in ['best', 'average', 'worst']:
                
                print(f"Executando Python: T={t_size}, P={p_size}, Caso={case} ({NUM_REPETICOES}x)...")

                text, pattern, case_type = generate_test_case(t_size, p_size, case)
                
                # Repetir a execução (15-30 vezes)
                for run in range(1, NUM_REPETICOES + 1):
                    start_time = time.perf_counter()
                    
                    # Chama o algoritmo de busca
                    rk.search(text, pattern)
                    
                    end_time = time.perf_counter()
                    execution_time = end_time - start_time
                    
                    # Salva o resultado bruto
                    results.append([
                        'Python', 
                        t_size, 
                        p_size, 
                        case_type, 
                        run, 
                        execution_time
                    ])

    # 4. Salvar resultados
    with open(SAIDA_CSV_PYTHON, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)
        
    print(f"\n✅ Experimentos em Python concluídos.")
    print(f"Arquivo de dados brutos salvo em: {SAIDA_CSV_PYTHON}")

if __name__ == "__main__":
    # Garante que a pasta 'data' exista antes de salvar
    SAIDA_CSV_PYTHON.parent.mkdir(parents=True, exist_ok=True)
    run_all_experiments()