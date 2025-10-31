from constante import CAPACIDADE_MAXIMA_ESTOQUE
from funcoes_auxiliares.calcular_custo import calcular_custo
from funcoes_auxiliares.transicao_estado import transicao_estado
from typing import List, Tuple, Dict

def pd_recursiva_memo(periodos: int, demandas: List[int]) -> Tuple[float, Dict]:
    """
    Versão recursiva com memorização (top-down)

    Args:
        periodos: número de períodos
        demandas: lista com demandas de cada período

    Returns:
        custo_minimo: custo total mínimo
        memo: dicionário com resultados memorizados
    """
    memo = {}

    def resolver(t: int, estoque: int) -> float:
        """
        Resolve recursivamente o problema para período t com estoque dado
        """
        # Caso base: último período
        if t >= periodos:
            return 0.0

        # Verificar se já está memorizado
        if (t, estoque) in memo:
            return memo[(t, estoque)]

        demanda = demandas[t]
        custo_minimo = float('inf')

        # Testar diferentes quantidades de reposição
        for quantidade_repor in range(0, CAPACIDADE_MAXIMA_ESTOQUE - estoque + 1):
            # Custo imediato
            custo_atual = calcular_custo(estoque, quantidade_repor, demanda)

            # Próximo estado
            proximo_estoque = transicao_estado(estoque, quantidade_repor, demanda)

            # Custo futuro (recursivo)
            custo_futuro = resolver(t + 1, proximo_estoque)

            # Custo total
            custo_total = custo_atual + custo_futuro

            # Atualizar mínimo
            if custo_total < custo_minimo:
                custo_minimo = custo_total

        # Memorizar resultado
        memo[(t, estoque)] = custo_minimo
        return custo_minimo

    custo_final = resolver(0, 0)
    return custo_final, memo
