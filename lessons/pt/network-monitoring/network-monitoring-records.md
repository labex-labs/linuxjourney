---
lesson_id: "network-monitoring-records"
course_id: "network-monitoring"
lang: "pt"
order_index: 1
title: "Registros de rede"
description: "Aprenda a escolher um registro de rede adequado à pergunta que você quer responder."
meta_title: "Registros de rede - Monitoramento de redes"
meta_description: "Aprenda a escolher um registro de rede adequado à pergunta que você quer responder."
meta_keywords: "registros de rede, logs de DNS, captura de pacotes, monitoramento de redes, cibersegurança, Linux Journey"
---

Uma observação de rede descreve o que uma ferramenta conseguiu ver a partir de um ponto. Comece perguntando o que precisa descobrir. Fontes diferentes revelam partes diferentes da mesma atividade.

## Escolhendo o tipo de registro

Um **registro de fluxo** resume a comunicação entre endpoints da rede. Um **log de DNS** relata as consultas de nomes observadas por um resolvedor. Uma **captura de pacotes** armazena cópias de pacotes individuais vistos no ponto de captura. Um endpoint é um dos lados da comunicação, geralmente identificado por um endereço e uma porta.

:::single-choice{#network-monitoring-records-choose-dns} Você quer saber qual resposta um resolvedor retornou para site.example. Qual fonte atende melhor a essa pergunta?

::option[Uma contagem de processos web em execução.]{#network-monitoring-records-choose-dns-b explanation="A contagem de processos não tem relação com a consulta."}
::option[Um log de DNS daquele resolvedor.]{#network-monitoring-records-choose-dns-a .correct explanation="O resolvedor pode registrar a consulta e a resposta que processou."}
::option[Um resumo de fluxo que traz apenas o volume de tráfego.]{#network-monitoring-records-choose-dns-c explanation="O resumo de fluxo pode omitir a consulta e a resposta DNS."}
:::

## Identificando o ponto de observação

Uma captura em um notebook inclui os pacotes visíveis na interface selecionada. Um log de servidor depende do que chegou ao servidor e do que ele registrou. Por exemplo, uma requisição de usuário pode falhar antes de chegar ao servidor. Use a fonte cujo ponto de observação ajude a responder à sua pergunta.

:::single-choice{#network-monitoring-records-capture-scope} Você não encontra uma requisição na captura feita em outro computador. O que verificar antes de tirar uma conclusão?

::option[Se a interface de captura conseguia observar o caminho relevante no horário em questão.]{#network-monitoring-records-capture-scope-b .correct explanation="A ausência do pacote pode refletir os limites de visibilidade daquele ponto."}
::option[Se a captura contém alguns pacotes sem relação com a requisição.]{#network-monitoring-records-capture-scope-a explanation="Encontrar tráfego sem relação mostra que houve coleta. Ainda falta saber se o caminho relevante era visível naquele horário."}
::option[Se outro host fez uma captura ao mesmo tempo.]{#network-monitoring-records-capture-scope-c explanation="Capturar em outro host no mesmo momento não esclarece o que essa interface conseguia observar."}
:::

## Usando uma amostra pequena

Capturas de pacotes podem conter dados que as pessoas não pretendiam compartilhar. Ao aprender a ler pacotes, use uma captura preparada com tráfego de prática inofensivo. Ao compartilhar um trecho, informe o horário observado e o filtro para que outra pessoa entenda os limites da amostra.

:::single-choice{#network-monitoring-records-choosing-evidence} Qual amostra é melhor para ensinar a identificar uma resposta DNS?

::option[Uma captura longa de tráfego sem relação com o exercício, gerado por funcionários.]{#network-monitoring-records-choosing-evidence-a explanation="Isso acrescenta dados desnecessários e pode expor informações privadas."}
::option[Um resumo sem campos que descrevam a consulta.]{#network-monitoring-records-choosing-evidence-b explanation="Quem está aprendendo ficaria sem as evidências necessárias para interpretar a consulta."}
::option[Uma pequena captura preparada com a consulta e a resposta do exercício.]{#network-monitoring-records-choosing-evidence-c .correct explanation="Ela reúne apenas a troca de mensagens necessária para responder à pergunta."}
:::

## Resumo

Agora você consegue escolher um registro de rede e explicar o que ele podia observar.

1. Distinga resumos de fluxo, logs de DNS e capturas de pacotes.
2. Associe o ponto de observação ao caminho da rede.
3. Use uma amostra adequada e focada na análise.
