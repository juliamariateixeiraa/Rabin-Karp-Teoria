# 🔍 Projeto – Análise do Algoritmo Rabin–Karp  
## Teoria da Computação – Teoria da Complexidade e Análise de Tempo de Algoritmos

**Professor:** Daniel Bezerra  
**Data:** Outubro – Novembro de 2025  

---

## 📘 Descrição Geral

Este projeto tem como objetivo realizar uma **análise teórica e prática do algoritmo de busca de padrões em strings Rabin–Karp**, abordando desde a descrição lógica e classificação assintótica até a implementação em **duas linguagens (C e Python)** e a comparação dos resultados experimentais obtidos.

O trabalho faz parte da disciplina **Teoria da Computação** e tem como foco o estudo da **complexidade de tempo** e da **aplicabilidade prática** de algoritmos clássicos.

---

## 🎯 Objetivos

1. **Compreender a lógica do algoritmo Rabin–Karp**, incluindo sua função hash e o processo de pré-processamento.  
2. **Implementar o algoritmo em duas linguagens distintas (C e Python)**.  
3. **Executar experimentos controlados** para avaliar o desempenho prático.  
4. **Comparar os resultados experimentais** com as classificações teóricas (Big-O, Big-Ω, Big-Θ).  
5. **Discutir a aplicabilidade** e limitações do algoritmo em diferentes contextos.  
6. **Apresentar reflexões teóricas** sobre sua relação com classes de complexidade (P, NP, NP-completo).  

---

## 👥 Equipe e Responsabilidades

| Pessoa | Foco Principal | Tarefas Detalhadas |
|:--|:--|:--|
| **Pessoa 1** | 🧩 Análise Teórica e Documentação Base | - Descrição formal do problema (busca do padrão `P` em texto `T`)<br>- Explicação detalhada da lógica do **Rabin–Karp** e da função hash<br>- Classificação assintótica: Big-O, Big-Ω, Big-Θ<br>- Análise do **melhor caso** (ex: padrão não aparece)<br>- Redação das seções teóricas do relatório PDF |
| **Pessoa 2** | 🐍 Implementação (Python) e Análise Crítica | - Implementação completa do Rabin–Karp em **Pyhton** (incluindo pré-processamento e hash)<br>- Desenvolvimento do script de geração de entradas (textos e padrões pequenos, médios e grandes)<br>- Execução dos experimentos e **coleta de dados brutos** para a Linguagem 1<br>- Organização e publicação do **código-fonte no GitHub** |
| **Pessoa 3** | 💻 Implementação (C) e Experimentos | - Implementação completa do Rabin–Karp em **C**<br>- Execução dos experimentos e coleta de dados para a Linguagem 2<br>- Análise do **pior caso** e **caso médio** (ex: maior número de colisões ou shifts)<br>- Discussão sobre **aplicabilidade prática** (comparação KMP vs. Rabin–Karp vs. busca ingênua) |
| **Pessoa 4** | 📊 Análise de Dados e Apresentação Final | - Consolidação e limpeza dos dados coletados (P2 e P3)<br>- Criação de **gráficos e tabelas comparativas** (teoria vs. prática, linguagens, casos)<br>- Reflexão final: o algoritmo pertence à classe P? Há versões NP?<br>- Preparação da **apresentação oral** e organização final do relatório |

---

## 🧠 Aspectos Teóricos

- **Complexidade Assintótica:**
  - Melhor caso: `O(n + m)`
  - Caso médio: `O(n + m)`
  - Pior caso: `O(nm)` (devido a colisões de hash)
- **Classe de Problema:** Pertence à classe **P**.  
- **Aplicabilidade:** Eficiente em buscas múltiplas e contextos onde se pode usar **hash rolling**.  

---

## 🧪 Metodologia Experimental

1. **Gerar entradas sintéticas** com padrões e textos de diferentes tamanhos (pequeno, médio, grande).  
2. **Executar o algoritmo** 15–30 vezes por entrada para calcular média e desvio-padrão.  
3. **Comparar os tempos de execução** entre C e Python.  
4. **Plotar gráficos** de desempenho teórico × prático.  
5. **Discutir discrepâncias** entre a teoria e os resultados observados.  

---

## 📊 Resultados Esperados

- Gráficos de tempo × tamanho da entrada.  
- Comparações entre as linguagens.  
- Conclusões sobre a eficiência e aplicabilidade do Rabin–Karp.  

---

## 🗓️ Entregas e Avaliação

| Etapa | Descrição | Data |
|:--|:--|:--|
| **Entrega 1** | Definição da equipe | 24/10/2025 |
| **Entrega 2** | Relatório, slides e link do GitHub | 30/11/2025 |
| **Apresentações** | Exposição oral (7–8 min) | 01 a 10/12/2025 |

**Critérios de Avaliação:**
- Clareza e correção teórica — 2.0  
- Análise de complexidade — 2.0  
- Experimentos práticos e gráficos — 2.0  
- Código funcional e bem estruturado — 2.0  
- Apresentação oral — 2.0  

---

## 🧩 Referências

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.  
- Rabin, M. O., & Karp, R. M. (1987). *Efficient Randomized Pattern-Matching Algorithms*. IBM Journal of Research and Development.  
- Documentação da disciplina – Teoria da Computação (Prof. Daniel Bezerra, 2025).  

---

## 💡 Observações

> Todos os códigos e scripts utilizados nos experimentos estarão disponíveis neste repositório, com instruções de execução no arquivo `src/README.md`.

