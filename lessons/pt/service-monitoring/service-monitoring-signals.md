---
lesson_id: "service-monitoring-signals"
course_id: "service-monitoring"
lang: "pt"
order_index: 1
title: "Sinais de monitoramento"
description: "Aprenda a escolher um sinal de monitoramento que responda a uma pergunta sobre um serviço web."
meta_title: "Sinais de monitoramento - Monitoramento de serviços"
meta_description: "Aprenda a escolher um sinal de monitoramento que responda a uma pergunta sobre um serviço web."
meta_keywords: "sinais de monitoramento, monitoramento de serviços, DevOps, Linux Journey"
---

Um visitante diz que a página parece lenta. Comece pelo que ele percebeu e escolha uma medição que possa descrever essa experiência. Um **sinal** é uma observação, como uma contagem, uma medição ou um evento registrado.

## Verificando a experiência do usuário

A **disponibilidade** indica se o serviço consegue executar o trabalho esperado. Uma verificação pode solicitar a página inicial e confirmar se a resposta foi bem-sucedida. A **latência** indica quanto tempo a requisição leva. Uma página pode abrir normalmente e ainda assim demorar vários segundos.

:::single-choice{#service-monitoring-signals-slow-page} Os visitantes recebem a página, mas ela leva vários segundos para abrir. Qual sinal descreve o sintoma mais diretamente?

::option[O número de contêineres no servidor.]{#service-monitoring-signals-slow-page-b explanation="Isso não mede quanto tempo os visitantes esperam."}
::option[O tempo que leva para receber a página.]{#service-monitoring-signals-slow-page-a .correct explanation="A latência mede quanto tempo a requisição levou."}
::option[O número de bytes no repositório do código-fonte.]{#service-monitoring-signals-slow-page-c explanation="O tamanho do repositório não descreve a duração das requisições."}
:::

## Contando requisições e erros

O **tráfego** representa a demanda pelo serviço, como o número de requisições por minuto. Acompanhe o total junto com a quantidade de requisições que falharam. Cinco erros em 1.000 requisições têm um significado diferente de cinco erros em dez requisições.

:::single-choice{#service-monitoring-signals-count-context} Você observa cinco falhas em cada uma de duas janelas. O que ajuda a comparar o impacto para os usuários?

::option[O total de requisições em cada janela.]{#service-monitoring-signals-count-context-b .correct explanation="Para comparar as taxas de erros, você precisa do denominador de cada contagem."}
::option[O nome do painel.]{#service-monitoring-signals-count-context-a explanation="O nome indica onde está o gráfico. O volume de tráfego é outra informação."}
::option[A ordem dos serviços na lista.]{#service-monitoring-signals-count-context-c explanation="A ordem da lista não mede quantas requisições foram afetadas."}
:::

## Verificando a pressão sobre os recursos

A **saturação** indica o quanto um recurso está perto do seu limite. Um serviço pode ter tarefas esperando pelo banco de dados mesmo com o processo web em execução. Compare o comportamento percebido pelos usuários com o sinal do recurso antes de tirar uma conclusão.

:::single-choice{#service-monitoring-signals-saturation-check} As requisições ficam mais lentas enquanto a fila de tarefas cresce. Qual é um próximo passo razoável?

::option[Afirmar que a fila é definitivamente a causa do problema.]{#service-monitoring-signals-saturation-check-a explanation="As duas mudanças oferecem uma pista. São necessárias mais evidências para estabelecer a causa."}
::option[Contar novamente as imagens armazenadas no host.]{#service-monitoring-signals-saturation-check-b explanation="A disponibilidade das imagens não explica por que as requisições estão na fila."}
::option[Verificar o recurso que executa as tarefas em espera.]{#service-monitoring-signals-saturation-check-c .correct explanation="Examinar esse recurso pode mostrar se ele está deixando de acompanhar a demanda."}
:::

## Resumo

Agora você consegue escolher um sinal com base no que o usuário percebeu.

1. Distinga disponibilidade de latência.
2. Interprete as falhas junto com o volume de requisições.
3. Use a saturação como pista sobre a capacidade.
