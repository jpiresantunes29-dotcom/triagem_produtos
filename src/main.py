from validacoes import (
    ler_inteiro_positivo,
    ler_inteiro_nao_negativo,
    ler_float_nao_negativo,
    ler_sim_ou_nao,
)
from regras import classificar_pedido
from relatorios import (
    mostrar_todos_os_pedidos,
    mostrar_resumo,
    mostrar_maior_pedido,
    mostrar_bloqueados,
)


def cadastrar_pedidos(pedidos):
    quantidade = ler_inteiro_positivo("Quantos pedidos deseja analisar? ")

    for i in range(quantidade):
        print(f"\nPedido {i + 1}")

        codigo = input("Codigo do pedido: ").strip()
        valor = ler_float_nao_negativo("Valor da compra: ")
        idade = ler_inteiro_nao_negativo("Idade do cliente: ")
        quantidade_itens = ler_inteiro_positivo("Quantidade de itens: ")
        pagamento_aprovado = ler_sim_ou_nao("Pagamento aprovado (sim/nao): ")
        cliente_premium = ler_sim_ou_nao("Cliente premium (sim/nao): ")
        endereco_confirmado = ler_sim_ou_nao("Endereco confirmado (sim/nao): ")

        status, motivo = classificar_pedido(
            valor,
            idade,
            quantidade_itens,
            pagamento_aprovado,
            cliente_premium,
            endereco_confirmado,
        )

        pedido = {
            "codigo": codigo,
            "valor": valor,
            "idade": idade,
            "quantidade_itens": quantidade_itens,
            "pagamento_aprovado": pagamento_aprovado,
            "cliente_premium": cliente_premium,
            "endereco_confirmado": endereco_confirmado,
            "status": status,
            "motivo": motivo,
        }

        pedidos.append(pedido)

        print(f"Codigo: {codigo}")
        print(f"Resultado: {status}")
        print(f"Motivo: {motivo}")


def main():
    pedidos = []

    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar pedidos")
        print("2 - Mostrar todos os pedidos")
        print("3 - Mostrar resumo")
        print("4 - Mostrar pedido de maior valor")
        print("5 - Mostrar pedidos bloqueados")
        print("6 - Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_pedidos(pedidos)
        elif opcao == "2":
            mostrar_todos_os_pedidos(pedidos)
        elif opcao == "3":
            mostrar_resumo(pedidos)
        elif opcao == "4":
            mostrar_maior_pedido(pedidos)
        elif opcao == "5":
            mostrar_bloqueados(pedidos)
        elif opcao == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
