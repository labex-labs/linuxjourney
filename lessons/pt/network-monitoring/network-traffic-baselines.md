---
lesson_id: "network-traffic-baselines"
course_id: "network-monitoring"
lang: "pt"
order_index: 5
title: "Referências de tráfego"
description: "Aprenda a comparar janelas de tráfego semelhantes antes de tratar uma mudança como anomalia."
meta_title: "Referências de tráfego - Monitoramento de redes"
meta_description: "Aprenda a comparar janelas de tráfego semelhantes antes de tratar uma mudança como anomalia."
meta_keywords: "referências de tráfego, anomalias, monitoramento de redes, cibersegurança, Linux Journey"
---

Uma **referência** descreve o comportamento que você costuma observar sob condições definidas. No monitoramento de tráfego, isso pode ser uma contagem típica ou um intervalo de valores para o mesmo serviço e horário do dia.

## Escolhendo janelas comparáveis

Uma página pública pode receber mais tráfego no horário comercial. Para detectar uma mudança, compare janelas com rotinas parecidas. Este exemplo conta as requisições de um serviço em janelas de cinco minutos.

```text
Window                 Requests
Typical weekdays 09:00  90–120
Today 09:00                230
Typical nights 02:00       2–8
```

As 230 requisições se destacam da faixa típica das manhãs de dias úteis. A faixa da madrugada seria uma comparação menos útil.

:::single-choice{#network-traffic-baselines-baseline-fit} Qual linha dá a referência mais útil para a janela das 09:00 de hoje?

::option[As madrugadas típicas às 02:00.]{#network-traffic-baselines-baseline-fit-b explanation="Essa linha descreve outro padrão de tráfego."}
::option[A contagem de 230 requisições observadas hoje, sozinha.]{#network-traffic-baselines-baseline-fit-c explanation="Uma medição atual precisa de uma referência para mostrar o que mudou."}
::option[Os dias úteis típicos às 09:00.]{#network-traffic-baselines-baseline-fit-a .correct explanation="A linha corresponde ao horário e ao serviço em análise."}
:::

## Procurando contexto

Um aviso em um banner ou uma tarefa agendada pode explicar uma mudança. Confira as rotas, os horários e as mudanças autorizadas antes de decidir se precisa investigar mais. A referência destaca uma diferença e ajuda a formular a primeira pergunta.

:::single-choice{#network-traffic-baselines-baseline-explain} O tráfego dobrou após um lançamento anunciado. O que você deve verificar?

::option[Tratar a diferença como prova de que uma conta foi comprometida.]{#network-traffic-baselines-baseline-explain-a explanation="A contagem, por si só, não mostra a causa nem descreve um evento de conta."}
::option[Comparar os horários e caminhos com o tráfego esperado para o lançamento.]{#network-traffic-baselines-baseline-explain-b .correct explanation="Isso testa uma explicação plausível com observações relacionadas."}
::option[Ignorar a mudança porque um lançamento sempre explica todo pico.]{#network-traffic-baselines-baseline-explain-c explanation="Uma mudança esperada pode acontecer junto com outra atividade sem relação com ela."}
:::

## Revisando a medição

Uma mudança no coletor pode alterar a contagem sem que o tráfego de fato mude. Se o monitoramento começou a cobrir outra rede ontem, verifique qual tráfego cada janela inclui. Registre o serviço, o ponto de observação, o horário e a unidade junto à comparação.

:::single-choice{#network-traffic-baselines-changed-coverage} O coletor passou a registrar um segundo site. O que torna a próxima comparação mais útil?

::option[Comparar contagens do mesmo site, com a mesma cobertura das fontes.]{#network-traffic-baselines-changed-coverage-c .correct explanation="Um escopo consistente ajuda a distinguir alterações no tráfego de alterações na cobertura."}
::option[Comparar as duas contagens totais sem verificar seu escopo.]{#network-traffic-baselines-changed-coverage-a explanation="A mudança na coleta torna esses totais menos comparáveis."}
::option[Comparar o novo total com o de ontem depois de aumentar a janela de tempo.]{#network-traffic-baselines-changed-coverage-b explanation="Uma janela maior ainda mistura escopos se os totais incluírem sites e fontes diferentes."}
:::

## Resumo

Agora você consegue verificar se uma comparação de rede tem uma referência adequada.

1. Use o mesmo serviço, horário e unidade.
2. Procure mudanças esperadas antes de interpretar uma diferença.
3. Confira se a cobertura da coleta mudou.
