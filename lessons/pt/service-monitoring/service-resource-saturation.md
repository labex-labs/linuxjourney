---
lesson_id: "service-resource-saturation"
course_id: "service-monitoring"
lang: "pt"
order_index: 5
title: "Saturação de recursos"
description: "Aprenda a usar informações de utilização e de filas para descobrir onde um serviço pode estar chegando ao limite."
meta_title: "Saturação de recursos - Monitoramento de serviços"
meta_description: "Aprenda a usar informações de utilização e de filas para descobrir onde um serviço pode estar chegando ao limite."
meta_keywords: "saturação de recursos, filas, monitoramento de serviços, DevOps, Linux Journey"
---

Quando o serviço tem mais trabalho do que um recurso consegue atender imediatamente, as requisições podem ficar esperando. Se a espera persistir, você pode percebê-la em uma fila e em respostas mais lentas.

## Entendendo a capacidade e a demanda

A **utilização** indica quanto de um recurso está em uso. Um grupo com quatro workers, por exemplo, pode executar quatro tarefas ao mesmo tempo. Se os quatro estiverem ocupados, o grupo está no limite naquele momento. Quando outra tarefa chega, ela pode esperar na fila até um worker ficar livre.

:::single-choice{#service-resource-saturation-worker-capacity} Quatro workers estão ocupados e há três tarefas na fila. O que você pode concluir?

::option[Exatamente sete workers estão em execução.]{#service-resource-saturation-worker-capacity-b explanation="Três tarefas estão aguardando uma vaga para começar."}
::option[Todas as requisições já falharam.]{#service-resource-saturation-worker-capacity-c explanation="As tarefas em espera ainda podem terminar quando um worker ficar livre."}
::option[Todas as vagas estão ocupadas e há tarefas esperando.]{#service-resource-saturation-worker-capacity-a .correct explanation="A contagem de workers ocupados mostra a utilização atual. A fila mostra a demanda que ainda aguarda atendimento."}
:::

## Comparando ao longo do tempo

Um pico breve é diferente de uma fila que cresce de uma medição para outra. Compare a fila com a latência e o tráfego das requisições na mesma janela.

```text
Time   Busy workers   Queued jobs   Typical response
09:10       2 / 4           0             80 ms
09:11       4 / 4           5            300 ms
09:12       4 / 4          14            640 ms
```

Neste exemplo, os workers estão todos ocupados e a fila cresce. Isso sugere que as tarefas chegam mais rápido do que são concluídas. Verifique o que mantém os workers ocupados.

:::single-choice{#service-resource-saturation-sustained-pressure} Qual observação mais indica pressão contínua?

::option[Dois workers ocupados às 09:10.]{#service-resource-saturation-sustained-pressure-a explanation="Essa linha mostra que ainda havia capacidade e nenhuma tarefa esperava."}
::option[A fila cresce enquanto todos os workers permanecem ocupados.]{#service-resource-saturation-sustained-pressure-b .correct explanation="As tarefas se acumulam enquanto toda a capacidade continua em uso."}
::option[Uma resposta mais lenta enquanto a fila permanece vazia.]{#service-resource-saturation-sustained-pressure-c explanation="Uma resposta lenta pode merecer investigação. A fila crescente em várias medições com todos os workers ocupados é um indício mais forte de pressão contínua."}
:::

![Métricas simuladas de workers mostrando utilização total e uma fila crescente](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-resource-saturation/worker-queue.png)

## Investigando a causa

Os workers podem estar ocupados porque as requisições chegaram mais rápido, porque uma dependência ficou mais lenta ou porque uma mudança recente prolongou cada tarefa. Compare o volume de requisições, a duração do processamento e os dados das dependências. Outro sinal pode ajudar você a decidir como agir.

:::single-choice{#service-resource-saturation-next-observation} O volume de requisições permaneceu estável, mas as tarefas começaram a demorar mais. O que pode ajudar a explicar a fila?

::option[Verificar a duração das tarefas junto com o tempo de resposta das dependências.]{#service-resource-saturation-next-observation-c .correct explanation="Isso ajuda a identificar por que as tarefas ocupam as vagas por mais tempo."}
::option[Alterar a capacidade antes de coletar mais evidências.]{#service-resource-saturation-next-observation-a explanation="Aumentar a capacidade pode não resolver tarefas bloqueadas em uma dependência."}
::option[Contar os papéis no repositório.]{#service-resource-saturation-next-observation-b explanation="Esses papéis não mostram pelo que os workers estão esperando."}
:::

## Resumo

Agora você consegue distinguir um recurso ocupado de uma fila que continua acumulando tarefas.

1. Relacione a contagem de workers à capacidade do grupo.
2. Compare as filas com o comportamento das requisições ao longo do tempo.
3. Investigue o trabalho que ocupa o recurso com capacidade limitada.
