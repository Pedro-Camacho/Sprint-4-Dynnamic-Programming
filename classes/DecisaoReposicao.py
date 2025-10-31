class DecisaoReposicao:
    """
    Decisão: quantidade de material a ser reposto
    """
    def __init__(self, quantidade_repor: int):
        self.quantidade = quantidade_repor

    def __repr__(self):
        return f"Repor {self.quantidade} unidades"