class Participante:
    def __init__(self, id, nome, transacoes_qtd, valorenviado, valorrecebido):
        self.id = id
        self.nome = nome
        self.transacoes_qtd = transacoes_qtd
        self.valorenviado = valorenviado
        self.valorrecebido = valorrecebido

class Transacao:
    def __init__(self, remetente, recebedor, valor):
        self.id = id
        self.remetente = remetente
        self.recebedor = recebedor
        self.valor = valor
