from typing import List, Dict
import matplotlib.pyplot as plt

def visualizar_solucao(solucao: List[Dict]):
    """
    Cria visualizações da solução ótima
    """
    periodos = [s['periodo'] for s in solucao]
    estoque_inicial = [s['estoque_inicial'] for s in solucao]
    estoque_final = [s['estoque_final'] for s in solucao]
    demanda = [s['demanda'] for s in solucao]
    reposicao = [s['quantidade_repor'] for s in solucao]
    custos = [s['custo'] for s in solucao]

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Análise da Solução Ótima - Controle de Consumo', fontsize=16, fontweight='bold')

    # Gráfico 1: Evolução do Estoque
    axes[0, 0].plot(periodos, estoque_inicial, marker='o', label='Estoque Inicial', linewidth=2)
    axes[0, 0].plot(periodos, estoque_final, marker='s', label='Estoque Final', linewidth=2)
    axes[0, 0].plot(periodos, demanda, marker='^', label='Demanda', linewidth=2, linestyle='--')
    axes[0, 0].set_xlabel('Período')
    axes[0, 0].set_ylabel('Quantidade')
    axes[0, 0].set_title('Evolução do Estoque e Demanda')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # Gráfico 2: Reposições
    axes[0, 1].bar(periodos, reposicao, color='steelblue', alpha=0.7)
    axes[0, 1].set_xlabel('Período')
    axes[0, 1].set_ylabel('Quantidade Reposta')
    axes[0, 1].set_title('Decisões de Reposição')
    axes[0, 1].grid(True, alpha=0.3, axis='y')

    # Gráfico 3: Custos por Período
    axes[1, 0].bar(periodos, custos, color='coral', alpha=0.7)
    axes[1, 0].set_xlabel('Período')
    axes[1, 0].set_ylabel('Custo ($)')
    axes[1, 0].set_title('Custos por Período')
    axes[1, 0].grid(True, alpha=0.3, axis='y')

    # Gráfico 4: Resumo de Custos
    custo_total = sum(custos)
    custo_medio = custo_total / len(custos)
    axes[1, 1].text(0.5, 0.6, f'Custo Total: ${custo_total:.2f}',
                    ha='center', va='center', fontsize=16, fontweight='bold')
    axes[1, 1].text(0.5, 0.4, f'Custo Médio/Período: ${custo_medio:.2f}',
                    ha='center', va='center', fontsize=14)
    axes[1, 1].axis('off')
    axes[1, 1].set_title('Resumo Financeiro')

    plt.tight_layout()
    plt.show()
