def ler_inteiro_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Digite um numero inteiro maior que zero.")
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.")


def ler_inteiro_nao_negativo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= 0:
                return valor
            else:
                print("Digite um numero inteiro maior ou igual a zero.")
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.")


def ler_float_nao_negativo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
            else:
                print("Digite um valor maior ou igual a zero.")
        except ValueError:
            print("Entrada invalida. Digite um numero valido.")


def ler_sim_ou_nao(mensagem):
    while True:
        valor = input(mensagem).strip().lower()
        if valor == "sim" or valor == "nao":
            return valor
        else:
            print("Entrada invalida. Digite apenas sim ou nao.")
