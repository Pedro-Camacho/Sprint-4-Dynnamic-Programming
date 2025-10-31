from constante import CUSTO_PEDIDO, CUSTO_UNITARIO, CUSTO_ESTOQUE, CUSTO_FALTA

def calcular_custo(estoque_inicial: int, quantidade_repor: int, demanda: int) -> float:
    """
    Calcula o custo total para um período dado:
    - Estoque inicial
    - Decisão de reposição
    - Demanda do período
    """
    custo_total = 0.0

    # Custo de pedido (fixo + variável)
    if quantidade_repor > 0:
        custo_total += CUSTO_PEDIDO + (quantidade_repor * CUSTO_UNITARIO)

    # Estoque após reposição
    estoque_apos_reposicao = estoque_inicial + quantidade_repor

    # Estoque final após atender demanda
    estoque_final = estoque_apos_reposicao - demanda

    if estoque_final >= 0:
        # Custo de manutenção de estoque
        custo_total += estoque_final * CUSTO_ESTOQUE
    else:
        # Custo de falta
        falta = abs(estoque_final)
        custo_total += falta * CUSTO_FALTA

    return custo_total