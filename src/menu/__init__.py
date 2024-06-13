from src.urnaEletronica import UrnaEletronica


urna = UrnaEletronica()
lista = []
def menu():
    print('Menu: ')
    print('1. Votar')
    print('2. Apurar Votos')
    print('3. sair')

def voto():
    print('Nova votaçao adicionada')
    urna.votar
    lista.append(voto)

def apuro_votos():
    print('Votos em andamento')
    urna.apurar_votos()
    print(urna)

def voto_menu():
    print('Votar')
    print('Votar em branco')
    print('votar nulo')

def main():
    while True:
        menu()

        sessao = input('Digite 1 - votar ou 2 - apurar votos: ')

        if sessao == '1':
            voto()
        elif sessao == '2':
            apuro_votos()
        elif sessao == '3':
            print('saindo da sessao...')
            urna.finalizar_processo_eleitoral
        else:
            print('Opçao invalida! tente novamente.')

main()   