def mostrar_todos_os_pedidos(pedidos):
    if len(pedidos) == 0:
        print("Nenhum pedido cadastrado.")
        return

    print("\nTodos os pedidos:")
    for pedido in pedidos:
        print(f"Codigo: {pedido['codigo']}")
        print(f"Valor: {pedido['valor']}")
        print(f"Idade: {pedido['idade']}")
        print(f"Quantidade de itens: {pedido['quantidade_itens']}")
        print(f"Pagamento aprovado: {pedido['pagamento_aprovado']}")
        print(f"Cliente premium: {pedido['cliente_premium']}")
        print(f"Endereco confirmado: {pedido['endereco_confirmado']}")
        print(f"Status: {pedido['status']}")
        print(f"Motivo: {pedido['motivo']}")
        print("-" * 30)


def mostrar_resumo(pedidos):
    if len(pedidos) == 0:
        print("Nenhum pedido cadastrado.")
        return

    aprovados = 0
    em_revisao = 0
    bloqueados = 0

    for pedido in pedidos:
        if pedido["status"] == "BLOQUEADO":
            bloqueados += 1
        elif pedido["status"] == "EM REVISAO":
            em_revisao += 1
        else:
            aprovados += 1

    print("\nResumo final:")
    print(f"Total de pedidos processados: {len(pedidos)}")
    print(f"Aprovados: {aprovados}")
    print(f"Em revisao: {em_revisao}")
    print(f"Bloqueados: {bloqueados}")


def mostrar_maior_pedido(pedidos):
    if len(pedidos) == 0:
        print("Nenhum pedido cadastrado.")
        return

    maior_pedido = pedidos[0]

    for pedido in pedidos:
        if pedido["valor"] > maior_pedido["valor"]:
            maior_pedido = pedido

    print("\nPedido de maior valor:")
    print(f"Codigo: {maior_pedido['codigo']}")
    print(f"Valor: {maior_pedido['valor']}")
    print(f"Status: {maior_pedido['status']}")
    print(f"Motivo: {maior_pedido['motivo']}")


def mostrar_bloqueados(pedidos):
    if len(pedidos) == 0:
        print("Nenhum pedido cadastrado.")
        return

    print("\nPedidos bloqueados:")
    tem_bloqueado = False

    for pedido in pedidos:
        if pedido["status"] == "BLOQUEADO":
            print(f"{pedido['codigo']} - {pedido['motivo']}")
            tem_bloqueado = True

    if not tem_bloqueado:
        print("Nenhum pedido bloqueado.")
