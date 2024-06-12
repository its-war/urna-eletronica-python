class Candidato:
    def __init__(self, numero, nome, partido):
        self.numero = numero
        self.nome = nome
        self.partido = partido
        self.votos = 0

    def votar(self):
        self.votos = self.votos + 1

    def get_votos(self):
        return self.votos

    def get_nome(self):
        return self.nome

    def get_numero(self):
        return self.numero

    def get_partido(self):
        return self.partido
