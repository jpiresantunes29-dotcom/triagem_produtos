# Enunciado do Projeto

## Contexto

Uma pequena loja virtual precisa de um sistema simples para realizar a triagem inicial de pedidos antes do envio. Atualmente, essa verificacao e feita manualmente, o que torna o processo mais lento e aumenta a chance de erros.

Seu desafio e desenvolver um programa em Python capaz de analisar pedidos com base em regras de negocio e informar se cada compra deve ser aprovada, enviada para revisao ou bloqueada.

## Objetivo

Criar um sistema de triagem de pedidos que permita:

- cadastrar pedidos pelo terminal
- validar as informacoes digitadas
- classificar pedidos de acordo com regras definidas
- armazenar os pedidos durante a execucao
- consultar relatorios e listagens usando um menu interativo

## Conceitos obrigatorios

O projeto deve exigir o uso integrado dos seguintes conceitos fundamentais de programacao:

- operadores relacionais: `==`, `!=`, `>`, `<`, `>=`, `<=`
- operadores logicos: `and`, `or`, `not`
- estruturas condicionais: `if`, `elif`, `else`
- estruturas de repeticao

## Dados de entrada

Para cada pedido, o programa deve receber:

- codigo do pedido
- valor da compra
- idade do cliente
- quantidade de itens
- pagamento aprovado (`sim` ou `nao`)
- cliente premium (`sim` ou `nao`)
- endereco confirmado (`sim` ou `nao`)

As entradas devem ser validadas para evitar:
- numeros negativos
- quantidade invalida
- respostas fora do padrao esperado

## Regras de classificacao

### Pedido bloqueado

O pedido deve ser classificado como `BLOQUEADO` quando ocorrer qualquer uma das seguintes situacoes:

- pagamento nao aprovado
- cliente menor de idade
- endereco nao confirmado

### Pedido em revisao

Se o pedido nao for bloqueado, ele deve ser classificado como `EM REVISAO` quando ocorrer pelo menos uma destas situacoes:

- valor da compra maior que `1000`
- quantidade de itens maior ou igual a `10`
- cliente nao premium com compra acima de `500`

### Pedido aprovado

O pedido sera classificado como `APROVADO` quando:

- nao se enquadrar nas regras de bloqueio
- nao se enquadrar nas regras de revisao

## Saidas esperadas

Para cada pedido cadastrado, o programa deve exibir:

- codigo do pedido
- status final da analise
- motivo principal da classificacao

O sistema tambem deve permitir a consulta de:

- todos os pedidos cadastrados
- resumo geral com contagem por categoria
- pedido de maior valor
- lista de pedidos bloqueados

## Requisitos funcionais

O programa deve:

- usar `for` no cadastro de varios pedidos
- utilizar `if`, `elif` e `else` para as decisoes
- aplicar operadores logicos e relacionais nas regras
- validar as entradas do usuario
- organizar o codigo em funcoes
- permitir navegacao por menu

## Possiveis expansoes

Depois da versao inicial, o projeto pode evoluir com:

- salvamento em arquivo
- filtros por status
- calculo de media de compras
- percentual de pedidos aprovados, revisados e bloqueados
- edicao de pedidos
- interface grafica
- integracao com banco de dados

## Resultado esperado

Ao final, o projeto deve representar um pequeno sistema em Python capaz de unir logica de programacao, validacao de dados, modularizacao e interacao com o usuario de forma clara e funcional.
