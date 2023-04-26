---
title: 'Relacionamento entre bases no relatório operacional'
---

# Introdução 

As bases  que compõem o relatório operacional são provenientes do [armazém B.O](http://www.armazem.mg.gov.br/), que é alimentado por diferentes fluxos dos sistemas transacionais SIAFI e SIAD, e também pelas bases de Restimativa da Despesa e Receita, de atualização pela DCMEFO e DCAF, que se encontra compartilhada atualmente no OneDrive. 

Essas bases contêm diferentes granularidades (dimensões) nos dados entre elas, em razão de especificidades inerentes a natureza dos dados e ao fluxo a que pertencem, o que exige do usuário desenvolvedor do qlikview conhecimento intermediário da ferramenta para o relacionamento correto das bases na ferramenta. 

O objetivo desta nota é apresentar as principais particularidades da granulariade de cada uma das bases, bem como o método encontrado para contornar essa situação no qlikview.

# As diferentes granularidades das bases do relatório operacional:

As diferentes granularidades dos dados pode ser verificada por meio do ementário completo das bases do projeto disponível em [data package relatorio operacional](https://gist.github.com/hslinhares/68a3d06eae13b8facb1df42e1095c49e).

Como exemplo, temos as diferenças nas bases de Execução da Despesa, Restos a Pagar e Crédito Inicial e Autorizado.
A primeira e a segunda, além de toda a classificação orçamentária até o menor nível, elemento item de despesa, retornam dados por credor, contrato, obra, entre outras dimensões, enquanto a base de Crédito Inicial e Autorizado retorna o dado somente até a  classificação orçamentária por FONTE e IPU, um nível acima ao de elemento item da despesa. 

Além deste exemplo, existem outras combinações de dimensões em comum entre as bases. A seguir é listado um resumo:

(em elaboração)

As bases Execução da Despesa e Restos a Pagar contêm o maior nível de dimensões. Contendo todas as dimensões das demais bases.

A base Crédito Inicial e Autorizado contém toda a classificação orçamentária, porém não contém a classificação por elemento item da despesa existentes nas demais bases.
A base de Arrecadação da receita contém em comum com as demais somente Unidade Orçamentária e Fonte.
A base Cota contém não contém Modalidade, Contrato e Credor, entre outras dimensões das bases Execução e Restos a pagar.

Diante do exposto, para uma correta visualização dos dados, o trabalho de relacionar as bases no aplicativo qlikview exige a utilização de uma técnica específica (linktable), conforme será mostrado mais aditante, requisitando do usuário desenvolvedor conhecimentos intermediários da ferramenta.

## Métodos de relacionamento entre as bases

### Método da concatenação (concatenate)

(em elaboração: inserir referência, ilustrações, exemplo real)

A forma mais intuitiva, geralmente utilizada por usuários desenvolvedores iniciantes do qlikview,  seria relacionar todas bases por meio do comando concatenate no script do aplicativo. Isso resultaria em uma tabela única, contendo todas as informações de todas as bases. Contudo, isso traz alguns inconvenientes na criação de visualização dos dados na ferramenta.

Exemplo:

Ao se filtrar, por exemplo, pela classificação orçamentária grupo de despesa, os painéis que trazerem dados das bases onde esse dado existe,retornarão corretamente. Entretanto, o painel com dados da Arrecadação da receita retornarão nulo, uma vez que inexiste esse no fluxo da arrecadação da receita. Essa situação ocorre em qualquer filtro que se faça em um parâmetro que inexiste em alguma das bases.

inserir visualizações


### Método linktable

(em elaboração: ver texto, inserir referência, ilustrações, exemplo real)

Explicar o que se espera...

A forma encontrada para se relacionar as bases foi a adaptação do método linktable(inserir link do tutorial). Por meio de criação da coluna de chaves em todas elas contendo todas  os parâmetros comuns a ao menos uma das bases. 
Resumidamente, o linktable resulta na concatenação em uma tabela de todas as dimensões de todas as bases. Resultando em uma única tabela com todas as dimensões e chaves para se ligar às tabelas fato. Ou seja, todas classificações orçamentárias e demais dimensões vão estar nesta grande tabela chamada “link”, e também as chaves, que correspondem a uma coluna resultado da concatenação de todas as colunas dimensão.
Nas tabelas fato (bases Execução, Crédito, Restos a Pagar, Cota Orçamentária) vão restar somente a chave para se ligar a tabela link e os dados da tabela fato (Crédito Inicial e Autorizado, Empenhado, Liquidado, Pago, Cota Aprovada Líquida, Receita Arrecadada, e etc.)

(Inserir visualizações)
(Inserir parte do script)










