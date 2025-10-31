class EstadoMaterial:
    """
    Estado: representa a quantidade de material em estoque em um determinado período
    """
    def __init__(self, periodo: int, estoque: int, demanda: int):
        self.periodo = periodo
        self.estoque = estoque
        self.demanda = demanda

    def __repr__(self):
        return f"Estado(t={self.periodo}, estoque={self.estoque}, demanda={self.demanda})"
