---
lesson_id: "service-latency"
course_id: "service-monitoring"
lang: "pt"
order_index: 4
title: "Latência"
description: "Aprenda a comparar tempos de resposta típicos com os mais lentos observados."
meta_title: "Latência - Monitoramento de serviços"
meta_description: "Aprenda a comparar tempos de resposta típicos com os mais lentos observados."
meta_keywords: "latência, percentis, monitoramento de serviços, DevOps, Linux Journey"
---

A **latência** é o tempo que uma requisição leva. Um só número pode esconder experiências diferentes. Compare o tempo de uma requisição típica com os das mais lentas, usando a mesma rota e janela de tempo.

## Lendo uma amostra pequena

Os cinco tempos a seguir estão em milissegundos. Quatro requisições terminaram em menos de 100 milissegundos e uma demorou dois segundos.

```text
40  50  60  70  2000
```

A **mediana**, também chamada de percentil 50, é o valor do meio quando você ordena a amostra. Aqui, são 60 milissegundos. A requisição mais lenta levou 2.000 milissegundos. A média, calculada ao dividir a soma por cinco, é de 444 milissegundos.

:::single-choice{#service-latency-sample-median} Qual valor descreve a requisição que está no meio da amostra ordenada?

::option[444 milissegundos.]{#service-latency-sample-median-a explanation="Essa é a média, que inclui o peso da resposta lenta."}
::option[60 milissegundos.]{#service-latency-sample-median-b .correct explanation="O terceiro dos cinco valores ordenados é a mediana."}
::option[2.000 milissegundos.]{#service-latency-sample-median-c explanation="Esse é o maior valor observado."}
:::

## Examinando as requisições mais lentas

Um **percentil** indica o limite abaixo do qual fica uma parcela das observações. O percentil 95 da latência, geralmente exibido como p95, indica um limite próximo dos valores mais lentos de uma amostra maior. Use a mesma definição do painel em suas comparações. Amostras muito pequenas tornam instáveis as estimativas dos tempos mais altos.

:::single-choice{#service-latency-slow-end} A mediana quase não muda, mas os visitantes relatam demoras ocasionais. O que ajudaria a entender o problema?

::option[As latências mais altas, junto com o número de requisições.]{#service-latency-slow-end-a .correct explanation="Os tempos das respostas mais lentas podem mudar mesmo se os do meio permanecerem parecidos."}
::option[Conferir apenas a mediana novamente.]{#service-latency-slow-end-b explanation="Isso pode deixar passar mudanças que afetam uma parcela pequena das visitas."}
::option[O tamanho total do arquivo de log.]{#service-latency-slow-end-c explanation="O tamanho do arquivo não mostra quanto tempo as requisições levaram."}
:::

## Comparando requisições semelhantes

Compare a mesma rota sob tráfego semelhante. É normal que um download leve mais tempo do que uma pequena consulta de status. Se uma rota estiver especialmente lenta, examine os logs das requisições e as dependências na mesma janela de tempo. Use a métrica para delimitar o problema e as outras evidências para investigá-lo.

:::single-choice{#service-latency-compare-route} Qual comparação ajuda a verificar se a mesma página inicial ficou mais lenta após uma release?

::option[As respostas da página inicial de hoje com os downloads do mês passado.]{#service-latency-compare-route-a explanation="O tipo de trabalho e os períodos são diferentes, o que dificulta interpretar a comparação."}
::option[Uma única requisição por release, sem indicação de horário.]{#service-latency-compare-route-b explanation="Uma medição isolada deixa de mostrar a variação."}
::option[A latência da página inicial em janelas comparáveis antes e depois da release.]{#service-latency-compare-route-c .correct explanation="Comparar a mesma rota sob cargas semelhantes facilita interpretar a mudança."}
:::

## Resumo

Agora você consegue analisar os tempos típicos e os mais lentos em conjunto.

1. Encontre a mediana em uma amostra pequena e ordenada.
2. Observe os tempos mais altos junto com as contagens.
3. Compare requisições semelhantes antes de investigar diferenças.
