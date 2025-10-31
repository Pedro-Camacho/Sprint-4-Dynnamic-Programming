from funcoes_auxiliares.calcular_custo import calcular_custo
from funcoes_auxiliares.transicao_estado import transicao_estado
from typing import List, Dict   
import numpy as np
def reconstruir_solucao(decisoes: np.ndarray, demandas: List[int], estoque_inicial: int = 0) -> List[Dict]:
    """
    Reconstrói a sequência ótima de decisões
    """
    solucao = []
    estoque_atual = estoque_inicial

    for t, demanda in enumerate(demandas):
        quantidade_repor = decisoes[t, estoque_atual]
        custo_periodo = calcular_custo(estoque_atual, quantidade_repor, demanda)
        proximo_estoque = transicao_estado(estoque_atual, quantidade_repor, demanda)

        solucao.append({
            'periodo': t + 1,
            'estoque_inicial': estoque_atual,
            'demanda': demanda,
            'quantidade_repor': quantidade_repor,
            'estoque_final': proximo_estoque,
            'custo': custo_periodo
        })

        estoque_atual = proximo_estoque

    return solucao