---
lesson_id: "service-alerts"
course_id: "service-monitoring"
lang: "pt"
order_index: 6
title: "Alertas de serviço"
description: "Aprenda a interpretar a condição de um alerta, sua janela de tempo e o que fazer a seguir."
meta_title: "Alertas de serviço - Monitoramento de serviços"
meta_description: "Aprenda a interpretar a condição de um alerta, sua janela de tempo e o que fazer a seguir."
meta_keywords: "alertas de serviço, monitoramento de serviços, DevOps, Linux Journey"
---

Um painel exibe medições. Um **alerta** chama a atenção de alguém para uma condição que pode exigir uma resposta. Um alerta útil ajuda você a entender o que aconteceu e o que verificar.

## Lendo a condição

Imagine uma regra que verifica se mais de 5% das requisições à página inicial falharam em cinco minutos. Ela também exige pelo menos 100 requisições para que o alerta represente uma amostra útil para esse serviço.

```text
Window   09:10–09:15 UTC
Route    /
Requests 120
Failures 12
```

Doze falhas em 120 requisições correspondem a 10%. As duas condições da regra foram atendidas. O aviso aponta as falhas observadas na página inicial.

:::single-choice{#service-alerts-condition-match} A mesma regra dispararia um alerta para uma falha em dez requisições?

::option[Não, porque o total ficou abaixo do mínimo de requisições.]{#service-alerts-condition-match-b .correct explanation="No exemplo, tanto a taxa quanto o total precisam atender à regra."}
::option[Sim, porque a taxa de erros passa de 5%.]{#service-alerts-condition-match-a explanation="A regra também exige pelo menos 100 requisições."}
::option[Não, porque uma falha em dez equivale a 1%.]{#service-alerts-condition-match-c explanation="Uma em dez equivale a 10%, mas o total de requisições ainda está abaixo do mínimo."}
:::

## Verificando a janela de tempo

Use o intervalo indicado no alerta, mesmo se o painel agora mostrar que tudo está bem. O aviso pode descrever uma condição anterior. Verifique se o sinal voltou à faixa habitual e se as funções importantes para os usuários voltaram a funcionar.

:::single-choice{#service-alerts-alert-window} O alerta chegou às 09:16 e descrevia o intervalo das 09:10 às 09:15. Onde você deve procurar primeiro pelos erros correspondentes?

::option[Somente em um relatório da semana anterior.]{#service-alerts-alert-window-b explanation="Ele pode dar uma referência, mas não cobre o período afetado."}
::option[Somente depois das 09:16.]{#service-alerts-alert-window-c explanation="O envio da notificação pode demorar. O aviso pode chegar depois do período em que os erros foram observados."}
::option[Na janela de tempo registrada no alerta.]{#service-alerts-alert-window-a .correct explanation="Foi nesse intervalo que a regra contou os erros."}
:::

## Escolhendo o próximo passo

Um alerta sobre falhas na página inicial pode trazer links para as métricas dessa rota e para os logs recentes. Confirme primeiro como os usuários foram afetados e investigue a causa em seguida. Se o serviço se recuperou, guarde informações suficientes para investigar alertas recorrentes.

:::single-choice{#service-alerts-next-check} Qual é a primeira ação que verifica diretamente se a página inicial ainda falha?

::option[Contar todas as imagens de contêiner no cache.]{#service-alerts-next-check-a explanation="O alerta descreve o resultado das requisições recebidas pelo serviço."}
::option[Fazer uma requisição de teste autorizada à rota afetada.]{#service-alerts-next-check-c .correct explanation="Uma nova requisição verifica se o problema relatado ainda afeta esse caminho."}
::option[Desativar a regra para silenciar o aviso.]{#service-alerts-next-check-b explanation="Isso altera as notificações sem verificar o comportamento do serviço."}
:::

## Resumo

Agora você consegue ler um alerta e decidir o que verificar.

1. Confira a métrica, o limite e o tamanho mínimo da amostra.
2. Use a janela de tempo do alerta para procurar evidências correspondentes.
3. Verifique o sintoma percebido pelo usuário com um teste adequado.
