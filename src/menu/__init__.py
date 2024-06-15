from src.urnaEletronica import UrnaEletronica
import os
import platform
from time import sleep

urna = UrnaEletronica()


def limpar_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    print('          URNA PY')


def printar_candidatos():
    for candidato in urna.get_candidatos():
        print(f'{candidato.get_numero()} — {candidato.get_nome()} ({candidato.get_partido()})')


def apuro_votos_menu():
    limpar_terminal()
    senha = input('Digite a senha do presidente da sessão: ')
    apuracao = urna.apurar_votos(senha)
    limpar_terminal()
    if apuracao is not False:
        for linha in apuracao:
            print(linha)
        while True:
            escolha = input('Deseja finalizar o processo eleitoral? (s/n) ')
            if escolha.lower() == 's':
                urna.finalizar_processo_eleitoral()
            else:
                break
    else:
        limpar_terminal()
        print('Senha incorreta!')
        sleep(3)


def menu_voto_digitar_numero():
    limpar_terminal()
    printar_candidatos()
    tentativas_corrigir = 3
    while True:
        numero_candidato = int(input('Digite o número do candidato: '))
        candidato_temp = urna.get_candidato(numero_candidato)
        if candidato_temp is not None:
            print(f'Voce escolheu {candidato_temp.get_nome()} — {candidato_temp.get_partido()}')
        else:
            print('Candidato inexistente! Se confirmar, seu voto será considerado nulo.')

        opcao = None
        if tentativas_corrigir <= 0:
            print('Voce ultrapassou o limite de tentativas de corrigir. Seu voto será computado. Aguarde...')
            sleep(10)
        else:
            print('1 — Confirmar         2 — Corrigir')
            opcao = input('Digite a opção: ')

        if opcao == '1' or tentativas_corrigir <= 0:
            urna.votar(numero_candidato)
            break
        elif opcao == '2' and tentativas_corrigir > 0:
            tentativas_corrigir -= 1
            limpar_terminal()
            printar_candidatos()
        else:
            print('Opção invalida! tente novamente.')


def voto_menu():
    limpar_terminal()
    printar_candidatos()
    while True:
        print('1 — Votar em um candidato')
        print('2 — Votar em branco')
        voto_menu_opcao = input('Digite a opção: ')

        if voto_menu_opcao == '1':
            menu_voto_digitar_numero()
            break
        elif voto_menu_opcao == '2':
            urna.votar_em_branco()
            break
        else:
            print('Opção invalida! tente novamente.')


def main():
    while True:
        limpar_terminal()
        printar_candidatos()
        print('1 — Votar         2 — Apurar votos')
        opcao = input('Digite a opção: ')
        if opcao == '1':
            voto_menu()
        elif opcao == '2':
            apuro_votos_menu()
        else:
            print('Opçao invalida! tente novamente.')
