from constante import CAPACIDADE_MAXIMA_ESTOQUE
def transicao_estado(estoque_atual: int, quantidade_repor: int, demanda: int) -> int:
    """
    Calcula o novo estado (estoque) após a decisão e demanda
    """
    novo_estoque = estoque_atual + quantidade_repor - demanda
    # Garantir que não ultrapasse capacidade máxima e não seja negativo
    return max(0, min(novo_estoque, CAPACIDADE_MAXIMA_ESTOQUE))