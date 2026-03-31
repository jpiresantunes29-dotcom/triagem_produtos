def classificar_pedido(
    valor,
    idade,
    quantidade_itens,
    pagamento_aprovado,
    cliente_premium,
    endereco_confirmado,
):
    if pagamento_aprovado != "sim":
        return "BLOQUEADO", "pagamento nao aprovado"
    elif idade < 18:
        return "BLOQUEADO", "cliente menor de idade"
    elif endereco_confirmado != "sim":
        return "BLOQUEADO", "endereco nao confirmado"
    elif valor > 1000:
        return "EM REVISAO", "valor da compra acima de 1000"
    elif quantidade_itens >= 10:
        return "EM REVISAO", "quantidade de itens alta"
    elif cliente_premium != "sim" and valor > 500:
        return "EM REVISAO", "cliente nao premium com compra acima de 500"
    else:
        return "APROVADO", "pedido dentro das regras normais"
