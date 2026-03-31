# Triagem de Pedidos

Sistema em Python para cadastrar, classificar e consultar pedidos de uma loja virtual, aplicando regras de aprovacao, revisao e bloqueio com validacao de dados e relatorios simples.

## Sobre o projeto

Este projeto foi desenvolvido com foco em pratica de logica de programacao e organizacao de codigo em Python. A proposta e simular um sistema simples de triagem de pedidos, como os usados em lojas virtuais para analisar compras antes da aprovacao final.

Durante a execucao, o usuario pode cadastrar pedidos, visualizar os registros salvos e consultar relatorios diretamente pelo terminal.

## Funcionalidades

- cadastro de pedidos pelo terminal
- validacao de entradas numericas e respostas `sim/nao`
- classificacao automatica dos pedidos
- listagem de todos os pedidos cadastrados
- resumo geral com totais por categoria
- identificacao do pedido de maior valor
- exibicao apenas dos pedidos bloqueados
- menu interativo para navegar pelas opcoes do sistema

## Regras de classificacao

Cada pedido pode receber um dos seguintes status:

### `BLOQUEADO`
O pedido sera bloqueado quando ocorrer pelo menos uma destas situacoes:

- pagamento nao aprovado
- cliente menor de idade
- endereco nao confirmado

### `EM REVISAO`
O pedido sera enviado para revisao quando nao estiver bloqueado, mas apresentar alguma condicao de risco, como:

- valor da compra maior que `1000`
- quantidade de itens maior ou igual a `10`
- cliente nao premium com compra acima de `500`

### `APROVADO`
O pedido sera aprovado quando nao se encaixar nas regras de bloqueio nem nas regras de revisao.

## Conceitos praticados

Este projeto trabalha varios fundamentos importantes de programacao:

- operadores relacionais
- operadores logicos
- estruturas condicionais com `if`, `elif` e `else`
- repeticao
- validacao de dados
- modularizacao do codigo
- organizacao em multiplos arquivos

## Estrutura do projeto

triagem_produtos/
├── docs/
│   └── enunciado.md
├── src/
│   ├── main.py
│   ├── validacoes.py
│   ├── regras.py
│   └── relatorios.py
└── README.md
