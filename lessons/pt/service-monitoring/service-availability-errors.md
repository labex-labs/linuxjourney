---
lesson_id: "service-availability-errors"
course_id: "service-monitoring"
lang: "pt"
order_index: 3
title: "Disponibilidade e erros"
description: "Aprenda a comparar erros nas requisições usando uma janela de tempo e a contagem total de requisições."
meta_title: "Disponibilidade e erros - Monitoramento de serviços"
meta_description: "Aprenda a comparar erros nas requisições usando uma janela de tempo e a contagem total de requisições."
meta_keywords: "disponibilidade, taxa de erros, monitoramento de serviços, DevOps, Linux Journey"
---

Um serviço pode responder à maioria dos visitantes enquanto algumas requisições falham. Use o total de requisições e o número de falhas na mesma janela de tempo para estimar a proporção de falhas observadas.

## Calculando a taxa de erros

Para obter a **taxa de erros**, divida a quantidade de requisições com falha pelo total observado. Multiplique por 100 para obter a porcentagem.

```text
Window          Requests   Failures
09:00–09:05          100          2
09:05–09:10           20          2
```

Na primeira janela, duas de cem requisições falharam, ou 2%. Na segunda, também houve duas falhas, mas em vinte requisições, ou 10%.

:::single-choice{#service-availability-errors-compare-windows} Em qual janela a proporção de falhas foi maior?

::option[Das 09:05 às 09:10.]{#service-availability-errors-compare-windows-b .correct explanation="Duas falhas em vinte requisições representam uma parcela maior que duas em cem."}
::option[As duas foram iguais porque cada uma teve duas falhas.]{#service-availability-errors-compare-windows-a explanation="O total de requisições de cada janela é diferente."}
::option[Das 09:00 às 09:05, porque houve mais tráfego.]{#service-availability-errors-compare-windows-c explanation="Com um total maior, a mesma quantidade de falhas representa uma fração menor."}
:::

## Comparando requisições equivalentes

Considere a janela de tempo, a rota e a definição de falha. Um endpoint de verificação de saúde pode responder normalmente enquanto uma página que precisa de uma dependência falha. Se você quer avaliar a experiência de quem usa a página, conte as requisições feitas a ela.

:::single-choice{#service-availability-errors-route-scope} O endpoint de verificação de saúde sempre responde com sucesso, mas os clientes relatam erros na finalização da compra. O que você deve examinar?

::option[Somente as respostas do endpoint de verificação de saúde.]{#service-availability-errors-route-scope-b explanation="Essas respostas descrevem outra operação."}
::option[O nome da conta de serviço.]{#service-availability-errors-route-scope-c explanation="O nome não dá a contagem das requisições afetadas."}
::option[As requisições à finalização da compra e as falhas nessa rota.]{#service-availability-errors-route-scope-a .correct explanation="A experiência relatada corresponde a essa rota."}
:::

## Interpretando tráfego baixo

Se duas requisições chegarem e uma falhar, a taxa observada será de 50%. Esse resultado descreve a amostra. Com poucas requisições, a porcentagem pode variar muito, então informe a contagem junto com ela. Quando o total de requisições é zero, a porcentagem de erros do tráfego real fica indefinida. Um teste agendado à parte ainda pode mostrar se uma requisição funcionou.

:::single-choice{#service-availability-errors-zero-traffic} Nenhum visitante fez requisições durante a janela. O que você deve informar sobre a porcentagem de erros dos visitantes?

::option[A janela comprova disponibilidade perfeita.]{#service-availability-errors-zero-traffic-a explanation="Nenhuma requisição de visitante foi observada para sustentar essa conclusão."}
::option[A janela não tem dados de requisições para calcular a porcentagem de erros.]{#service-availability-errors-zero-traffic-c .correct explanation="Se precisar verificar se o serviço responde, use um teste separado."}
::option[A porcentagem é certamente de 100%.]{#service-availability-errors-zero-traffic-b explanation="O denominador é zero porque não houve requisições observadas."}
:::

## Resumo

Agora você consegue explicar uma taxa de erros com o contexto necessário.

1. Compare as falhas com o total de requisições na mesma janela.
2. Use a rota e a definição de falha correspondentes à pergunta.
3. Informe as contagens quando houver pouco tráfego.
