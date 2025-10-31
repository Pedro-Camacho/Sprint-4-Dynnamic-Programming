from constante import CAPACIDADE_MAXIMA_ESTOQUE
from funcoes_auxiliares.calcular_custo import calcular_custo
from funcoes_auxiliares.transicao_estado import transicao_estado
from typing import List, Tuple
import numpy as np

def pd_iterativa(periodos: int, demandas: List[int]) -> Tuple[float, np.ndarray, np.ndarray]:
    """
    Versão iterativa (bottom-up)

    Args:
        periodos: número de períodos
        demandas: lista com demandas de cada período

    Returns:
        custo_minimo: custo total mínimo
        tabela_dp: tabela com custos ótimos
        decisoes: tabela com decisões ótimas
    """
    # Tabelas DP
    # dp[t][estoque] = custo mínimo do período t até o fim, começando com estoque
    dp = np.full((periodos + 1, CAPACIDADE_MAXIMA_ESTOQUE + 1), float('inf'))
    decisoes = np.zeros((periodos, CAPACIDADE_MAXIMA_ESTOQUE + 1), dtype=int)

    # Caso base: último período (custo 0)
    dp[periodos, :] = 0.0

    # Preencher tabela de trás para frente
    for t in range(periodos - 1, -1, -1):
        demanda = demandas[t]

        for estoque in range(CAPACIDADE_MAXIMA_ESTOQUE + 1):
            custo_minimo = float('inf')
            melhor_decisao = 0

            # Testar diferentes quantidades de reposição
            for quantidade_repor in range(0, CAPACIDADE_MAXIMA_ESTOQUE - estoque + 1):
                # Custo imediato
                custo_atual = calcular_custo(estoque, quantidade_repor, demanda)

                # Próximo estado
                proximo_estoque = transicao_estado(estoque, quantidade_repor, demanda)

                # Custo futuro
                custo_futuro = dp[t + 1, proximo_estoque]

                # Custo total
                custo_total = custo_atual + custo_futuro

                # Atualizar mínimo
                if custo_total < custo_minimo:
                    custo_minimo = custo_total
                    melhor_decisao = quantidade_repor

            dp[t, estoque] = custo_minimo
            decisoes[t, estoque] = melhor_decisao

    return dp[0, 0], dp, decisoes