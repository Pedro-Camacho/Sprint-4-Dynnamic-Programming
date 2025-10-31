# Sprint-4-Dynnamic-Programming# 🧠 Dynamic Programming — Controle de Consumo de Materiais em Unidades de Diagnóstico

## 👨‍💻 Integrante
*   Camila Pedroza da Cunha – RM 558768 

*   Isabelle Dallabeneta Carlesso – RM 554592 

*   Nicoli Amy Kassa – RM 559104 

*   Pedro Almeida e Camacho – RM 556831 

*   Renan Dias Utida – RM 558540  
## 🎯 Descrição do Problema
Nas unidades de diagnóstico, o consumo diário de insumos (reagentes e descartáveis) não é registrado com precisão, o que dificulta o controle de estoque e a previsão de reposição.  
Diante disso, este projeto propõe uma **solução baseada em Programação Dinâmica (PD)** para otimizar o registro e a reposição de materiais, **melhorando a visibilidade do consumo e reduzindo desperdícios**.

---

## 📋 Objetivos
- Modelar o problema como uma sequência de **decisões de reposição** de insumos ao longo do tempo.  
- Utilizar **Programação Dinâmica** para minimizar o **custo total**, composto por:
  - Custo fixo de pedido;  
  - Custo unitário dos materiais;  
  - Custo de manutenção em estoque;  
  - Custo de falta (ruptura).  

---

## 🧩 Estrutura do Problema

### 🔹 Estados
Cada estado representa a quantidade de material disponível em um determinado período:
```python
Estado(periodo, estoque, demanda)
```

### 🔹 Decisões
A decisão é a **quantidade de material a ser reposta** em cada período:
```python
DecisaoReposicao(quantidade_repor)
```

### 🔹 Função Objetivo
Minimizar o custo total:
\[
C(t, E) = \min_{q} [Custo(estoque, q, demanda_t) + C(t+1, novo\_estoque)]
\]

Onde:
- `q`: quantidade a repor;
- `Custo(estoque, q, demanda_t)`: custo no período t dado o estoque, a decisão e a demanda.

### 🔹 Função de Transição
```python
novo_estoque = max(0, min(estoque_atual + quantidade_repor - demanda, CAPACIDADE_MAXIMA))
```

---

## 🧮 Métodos Implementados

### 🔸 1. Recursiva com Memorização (Top-Down)
Explora todas as decisões possíveis e armazena resultados intermediários em um dicionário (`memo`) para evitar recomputações.

```python
custo_total, memo = pd_recursiva_memo(periodos, demandas)
```

### 🔸 2. Iterativa (Bottom-Up)
Constrói uma tabela `dp` iterativamente, partindo do último período até o primeiro.

```python
custo_total, tabela_dp, decisoes = pd_iterativa(periodos, demandas)
```

Ambas as abordagens produzem os **mesmos resultados**, validando a implementação.

---

## 📊 Visualização dos Resultados

O código gera gráficos para interpretar a solução ótima:

- Evolução do estoque e da demanda  
- Quantidades repostas por período  
- Custos por período  
- Resumo financeiro com custo total e médio

![visualizacao](assets/resultado.png)

---

## ⚙️ Execução do Projeto

### 📦 Dependências
Instale as bibliotecas necessárias:
```bash
pip install numpy matplotlib seaborn
```

### ▶️ Execução
Execute o arquivo principal:
```bash
python principal.ipynb
```

A saída inclui:
- Demandas simuladas;
- Custo mínimo total (recursivo e iterativo);
- Verificação de equivalência entre as versões;
- Tabela detalhada da solução ótima;
- Análises e gráficos de desempenho.

---

## 📈 Exemplo de Saída (resumida)
```
Demandas por período: [15, 22, 13, 28, 17, 19, 25, 14, 18, 21]
Custo mínimo total (recursiva): $1938.00
Custo mínimo total (iterativa): $1938.00
✓ Ambas as versões produzem os mesmos resultados!

Período  Est.Ini  Demanda  Repor  Est.Fim  Custo
1        0        15       30     15       $380.00
2        15       22       20     13       $290.00
...
TOTAL                                      $1938.00
```

---

## 🧠 Conclusões

A abordagem de **Programação Dinâmica** permite:
✅ Otimizar o controle de estoque  
✅ Reduzir custos de reposição e manutenção  
✅ Eliminar faltas de insumos  
✅ Melhorar previsibilidade e eficiência operacional  

> **Impacto estimado:** Redução de até 30–40% nos custos operacionais em comparação com métodos empíricos de reposição.

---

## 📁 Estrutura do Projeto
```
📦 Sprint-4-Dynnamic-Programming
 ┣ 📜 principal.ipynb
 ┣ 📜 README.md
 ┣ 📁 funcoes_auxiliares/
 ┃ ┗ calcular_custo.py
 ┃ ┗ transicao_estado.py
 ┣ 📁 funcoes_solucao/
 ┃ ┗ pd_iterativa.py
 ┃ ┗ pd_recursiva_memo.py
 ┃ ┗ reconstruir_solucao.py
 ┣ 📁 visualizacao/
 ┃ ┗ visualizar_solucao.py
 ┗ 📁 classes/
    ┗ EstadoMaterial.py
    ┗ DecisaoReposicao.py

```

---



