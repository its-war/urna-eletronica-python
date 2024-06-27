from src.model import Candidato
import sys


class UrnaEletronica:
    def __init__(self):
        """
        Inicializa o objeto UrnaEletronica.
        Configura a lista de candidatos, a contagem de votos nulos, a contagem de votos em branco e a senha.
        """
        self.__candidatos = [
            Candidato(45, 'Carlos Paiva', 'PTC'),
            Candidato(13, 'Monteiro Lobato', 'PT'),
            Candidato(12, 'Elis Regina', 'PDT')
        ]
        self.votos_nulos = 0
        self.votos_brancos = 0
        self.__senha = '123'

    def votar(self, numero_candidato):
        """
        Incrementa os votos de um candidato se o número do candidato fornecido corresponder ao número do candidato.
        Se o número do candidato não corresponder, incrementa o número de votos nulos.

        :param numero_candidato: Um inteiro representando o número do candidato.
        :type numero_candidato: int
        :return: Nada
        """
        for i, candidato in enumerate(self.__candidatos):
            if candidato.get_numero() == numero_candidato:
                self.__candidatos[i].votar()
            else:
                self.votos_nulos = self.votos_nulos + 1

    def votar_em_branco(self):
        """
        Incrementa o número de votos em branco em 1.

        Essa função incrementa o atributo `votos_brancos` do objeto `UrnaEletronica` em 1. Ela é usada para registrar
        um voto em branco em uma eleição.

        Retorna:
            Nada
        """
        self.votos_brancos = self.votos_brancos + 1

    def apurar_votos(self, senha):
        """
            Calcula os resultados da eleição com base nos votos recebidos.

            Args:
                senha (str): A senha para acessar os resultados da eleição.

            Returns:
                list: Uma lista de strings contendo os resultados da eleição. Se a senha estiver correta,
                  a lista conterá os nomes dos candidatos, a quantidade de votos que receberam,
                  e o vencedor da eleição. Se a senha estiver incorreta, False será retornado.
            """
        if senha == self.__senha:
            self.__organizar_lista()
            dados = ['DADOS DA VOTAÇÃO']
            for candidato in self.__candidatos:
                dados.append(f'{candidato.get_partido()} - {candidato.get_nome()} - {candidato.get_votos()} votos')
            if self.__tem_vencedor() is not False:
                dados.append(f'VENCEDOR: {self.__candidatos[self.__tem_vencedor()].get_nome()}')
            else:
                dados.append('SEGUNDO TURNO NECESSÁRIO')
            return dados
        else:
            return False

    def __tem_vencedor(self):
        """
        Verifica se há um vencedor na eleição com base no número de votos recebidos.

        Esta função calcula o total de votos recebidos, iterando sobre a lista de candidatos.
        Em seguida, verifica se algum candidato recebeu mais da metade dos votos totais mais um.
        Se um candidato atingir esta condição, o índice desse candidato é retornado como o vencedor.
        Se nenhum candidato atingir esta condição, False é retornado.

        Retorna:
            int ou False: O índice do candidato vencedor, caso haja um vencedor, ou False caso contrário.
        """
        total_votos = sum(candidato.get_votos() for candidato in self.__candidatos)
        for i, candidato in enumerate(self.__candidatos):
            if candidato.get_votos() >= ((total_votos / 2) + 1):
                return i
            else:
                return False

    def __organizar_lista(self):
        """
        Ordena a lista de candidatos em ordem decrescente com base no número de votos recebidos.

        Esta função não recebe nenhum parâmetro.

        Ela não retorna nada.

        Essa função é privada.
        """
        self.__candidatos = sorted(self.__candidatos, key=lambda candidato: candidato.get_votos(), reverse=True)

    def finalizar_processo_eleitoral(self):
        """
        Encerra o processo eleitoral.
        """
        sys.exit(0)

    def get_candidatos(self):
        """
        Essa função retorna a lista de candidatos.
        """
        return self.__candidatos

    def get_candidato(self, numero):
        """
        Essa função retorna o candidato que tiver o número igual ao número fornecido
        ou retorna None caso não tenha candidato com o número fornecido.
        :param numero: número do candidato
        :type numero: int
        :return: Candidato | None
        """
        for candidato in self.__candidatos:
            if candidato.get_numero() == numero:
                return candidato
        return None
