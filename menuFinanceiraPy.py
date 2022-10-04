# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal. sabendo que ela não pode exceder 30% do salário ou então o empréstimo sera negado
from time import sleep
import os
import sys
import habitacao

def loading():
    # Barra de loading (fake)
    # print("\nCarregando modulos financeiros")

    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
                 "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]",
                 "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

def limpar():
    os.system('cls')
    return

def menuFinanceiraPy():
    
    limpar()
    print('Carregando modulos financeiros...')
    loading()
    limpar()
    print('Atualizando tabelas de valores...')
    loading()
    limpar()
    print('Atualizando juros...')
    loading()
    limpar()



    print("""\
    ███████╗██╗███╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗██╗██████╗  █████╗     ██████╗ ██╗   ██╗
    ██╔════╝██║████╗  ██║██╔══██╗████╗  ██║██╔════╝██╔════╝██║██╔══██╗██╔══██╗    ██╔══██╗╚██╗ ██╔╝
    █████╗  ██║██╔██╗ ██║███████║██╔██╗ ██║██║     █████╗  ██║██████╔╝███████║    ██████╔╝ ╚████╔╝ 
    ██╔══╝  ██║██║╚██╗██║██╔══██║██║╚██╗██║██║     ██╔══╝  ██║██╔══██╗██╔══██║    ██╔═══╝   ╚██╔╝  
    ██║     ██║██║ ╚████║██║  ██║██║ ╚████║╚██████╗███████╗██║██║  ██║██║  ██║    ██║        ██║   
    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝        ╚═╝   
                                                                                                """)

    print('Bem vindo ao sistema Financeira PY©')
    print("""\
Abaixo estão as opçoes do programa:

(1) Financiamento Habitacional
(2) Emprestimo PF
(3) Emprestimo PJ
(4) Negociação de dividas
(5) Sair""")

    opcao = int(input('\nSelecione: '))
    while(opcao != 5):
        if opcao == 1:
            os.system('cls')
            print('Carregando modulo Habitacional')
            loading()
            os.system('cls')
            telaHabitacao()
            habitacao.habitacao_ini()
            break
        else:
            print('Opçao em Desenvolvimento')
            opcao = int(input('Selecione outra opçao: '))
    print('\nObrigado por participar do Alpha de nosso programa!!!!')
    botaoEncerrar = str(input('\nPrecione ENTER para encerrar o programa'))


def telaHabitacao():
    print("""██╗  ██╗ █████╗ ██████╗ ██╗████████╗ █████╗  ██████╗ █████╗  ██████╗ 
██║  ██║██╔══██╗██╔══██╗██║╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔═══██╗
███████║███████║██████╔╝██║   ██║   ███████║██║     ███████║██║   ██║
██╔══██║██╔══██║██╔══██╗██║   ██║   ██╔══██║██║     ██╔══██║██║   ██║
██║  ██║██║  ██║██████╔╝██║   ██║   ██║  ██║╚██████╗██║  ██║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ """)


if(__name__ == '__main__'):
    menuFinanceiraPy()

