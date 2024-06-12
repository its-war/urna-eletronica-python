from src.model import Candidato


class UrnaEletronica:
    def __init__(self):
        self.candidatos = [
            Candidato(45, 'Carlos Paiva', 'PTC'),
            Candidato(13, 'Monteiro Lobato', 'PT'),
            Candidato(12, 'Elis Regina', 'PDT')
        ]
        self.votos_nulos = 0
        self.votos_brancos = 0
        self.__senha = 'karlos.warney.7410'

    def votar(self, numero_candidato):
        for i, candidato in self.candidatos:
            if candidato.get_numero() == numero_candidato:
                self.candidatos[i].votar()
            else:
                self.votos_nulos = self.votos_nulos + 1

    def votar_em_branco(self):
        self.votos_brancos = self.votos_brancos + 1

    def apurar_votos(self, senha):
        if senha == self.__senha:
            self.__organizar_lista()
        else:
            return False

    def __verifica_votos(self):
        pass
        # TODO: desenvolver esse metodo

    def __organizar_lista(self):
        self.candidatos = sorted(self.candidatos, key=lambda candidato: candidato.get_votos(), reverse=True)

    def finalizar_processo_eleitoral(self):
        exit(0)
