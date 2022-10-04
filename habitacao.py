import menuFinanceiraPy

def menu():
    print("""\
    Opções do menu :\n 
    (1) Simular financiamento
    (2) Forma de aprovação
    (3) Encerrar programa\n""")
def nova_consulta():
    continuar = int(input("""\
        Deseja realizar uma nova consulta?
        (1) Sim
        (2) Não
        Selecione: """))
    if (continuar == 1):
        return habitacao_ini()
    else:
        print("Programa encerrado")
def confere_financiamento():
    casa = float(input("Digite o valor da casa: "))
    salario = float(input("Digite seu salário: "))
    anos = int(input("Digite em quantos anos deseja pagar: "))

    parcela = casa / (12 * anos)
    pSalario = 30 / 100 * salario

    if pSalario > parcela:
        print('\nFinanciamento aprovado\n')
        return nova_consulta()
    else:
        print('\nSeu financiamento foi recusado pois a prestação esta acima de 30% do seu salário\n')
        return nova_consulta()
def habitacao_ini():
    simulacoes = 0

    while (simulacoes <= 0):

        menu()

        opcao = int(input("Selecione uma opção: "))

        if (opcao == 1):
            confere_financiamento()

        elif (opcao == 2):
            print("Para o financiamento ser aprovado é preciso que o valor da prestação nao ultrapasse 30% do salario do mesmo!\n")
            retornar = input('Precione Enter para retornar ao Menu inicial')
            return habitacao_ini()

        elif (opcao == 3):
            print("Obrigado por utilizar o nosso programa.\n")
            menuFinanceiraPy.menuFinanceiraPy()

    simulacoes += 1

if(__name__) == '__main__':
    habitacao_ini()
