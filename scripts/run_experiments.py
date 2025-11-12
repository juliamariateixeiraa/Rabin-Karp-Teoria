import time
import random
import string
import csv
import sys
import subprocess
from pathlib import Path

# para adicionar o diretório 'src' ao caminho de módulos em python.
sys.path.append(str(Path(__file__).parent.parent))

try:
    from src.python.rabin_karp import RabinKarp
except ImportError:
    #verifica se cpnseguiu importar para a analise
    print("ERRO CRÍTICO: Não foi possível importar o módulo RabinKarp.")
    print("Verifique se 'rabin_karp.py' está em 'src/python/'.")
    sys.exit(1)

NUM_REPETICOES = 25  # repetições de 15 a 30
SAIDA_CSV = Path(__file__).parent.parent / 'data' / 'raw_times_all.csv'
C_EXECUTABLE = Path(__file__).parent.parent / 'bin' / 'rabin_karp_c_exp' #em c

TAMANHOS_TEXTO = [10**4, 10**5, 5*10**5]
TAMANHOS_PADRAO = [10, 50, 200]
CASES = ['best', 'average', 'worst']

#geração de dados
def generate_random_string(length, char_set=string.ascii_letters + string.digits):
    """Gera uma string aleatória."""
    return ''.join(random.choice(char_set) for _ in range(length))

def generate_test_case(text_size, pattern_size, case_type):
    """
    Gera o texto (T) e o padrão (P) para os cenários de complexidade.
    """

    if case_type == 'worst':
        # pior Caso (Rabin-Karp): força colisões
        char = 'a'
        text = char * text_size
        pattern = char * pattern_size

    elif case_type == 'best':
        # melhor Caso (O(N+M)): padrão no início
        pattern = generate_random_string(pattern_size)
        text = pattern + generate_random_string(text_size - pattern_size)

    elif case_type == 'average':
        # caso Médio: padrão no meio
        pattern = generate_random_string(pattern_size)
        text = generate_random_string(text_size)
        mid_index = text_size // 2 - pattern_size // 2

        if mid_index < 0:
             mid_index = 0

        end_index = mid_index + pattern_size

        text = generate_random_string(mid_index) + pattern + generate_random_string(text_size - end_index)

    else:
        raise ValueError("Tipo de caso inválido.")
    return text, pattern, case_type

#para executar em c
def run_c_experiment(text, pattern, t_size, p_size, case_type, results):
    """
    Executa o código C, passando o texto via stdin para evitar Argument list too long,
    e coleta o tempo.
    """

    #tratando o erro de execução
    if not C_EXECUTABLE.exists():
        print(f"ERRO: Executável C não encontrado em {C_EXECUTABLE}. Rode 'make all' primeiro.")
        return

    # o texto é enviado via stdin. Adiciona o \n para o fgets no C funcionar.
    text_bytes = (text + '\n').encode('utf-8')

    for run in range(1, NUM_REPETICOES + 1):
        process = None
        try:
            process = subprocess.run(
                [str(C_EXECUTABLE), pattern],
                input=text_bytes,
                capture_output=True,
                check=True
            )

            # decodifica o stdout do processo C e remove espaços
            output_str = process.stdout.decode('utf-8').strip()
            execution_time = float(output_str)

        except subprocess.CalledProcessError as e:
            # se retorna um erro
            sys.stderr.write(f"Erro C (T={t_size}, P={p_size}, Run={run}): {e.stderr.decode('utf-8').strip()}\n")
            execution_time = float('nan')
        except ValueError:
            # se a saída não for um número float
            output = process.stdout.decode('utf-8').strip() if process else "N/A"
            sys.stderr.write(f"Erro conversão C (T={t_size}, P={p_size}, Run={run}). Saída: {output}\n")
            execution_time = float('nan')

        # salvando o resultado
        results.append([
            'C', t_size, p_size, case_type, run, execution_time
        ])


def run_all_experiments():
    """Executa todos os testes (Python e C) e salva os dados brutos em CSV."""

    rk = RabinKarp()
    results = []

    results.append(['language', 'text_size', 'pattern_size', 'case_type', 'run_number', 'execution_time_seconds'])

    for t_size in TAMANHOS_TEXTO:
        for p_size in TAMANHOS_PADRAO:
            if p_size > t_size: continue

            for case in CASES:

                text, pattern, case_type = generate_test_case(t_size, p_size, case)

                # executando o python
                print(f"Executando Python: T={t_size}, P={p_size}, Caso={case} ({NUM_REPETICOES}x)...")
                for run in range(1, NUM_REPETICOES + 1):
                    start_time = time.perf_counter()
                    rk.search(text, pattern)
                    end_time = time.perf_counter()
                    execution_time = end_time - start_time

                    results.append([
                        'Python', t_size, p_size, case_type, run, execution_time
                    ])

                # executando o c
                print(f"Executando C: T={t_size}, P={p_size}, Caso={case} ({NUM_REPETICOES}x)...")
                run_c_experiment(text, pattern, t_size, p_size, case_type, results)


    with open(SAIDA_CSV, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)
    print(f"\n✅ Experimentos em Python e C concluídos.")
    print(f"Arquivo de dados brutos salvo em: {SAIDA_CSV}")

if __name__ == "__main__":
    SAIDA_CSV.parent.mkdir(parents=True, exist_ok=True)
    run_all_experiments()