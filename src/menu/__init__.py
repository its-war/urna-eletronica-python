from src.urnaEletronica import UrnaEletronica

urna = UrnaEletronica()


def menu():
    print('1. Votar')
    print('2. Apurar Votos')


def apuro_votos():
    print('Votos em andamento')
    urna.apurar_votos('senha')
    print(urna)


def voto_menu():
    while True:
        print('Votar em um candidato')
        print('Votar em branco')
        voto_menu_opcao = input('Digite a opção: ')

        # continuar processo de escolha aqui
        # imprimir os candidatos para escolha


def main():
    while True:
        menu()

        opcao = input('Digite a opção: ')

        if opcao == '1':
            voto_menu()
        elif opcao == '2':
            # pedir senha depois para usar no metodo `urna.apurar_votos()`
            apuro_votos()
        else:
            print('Opçao invalida! tente novamente.')
