---
lesson_id: "memory-monitoring"
course_id: "process-utilization"
lang: "pt"
order_index: 6
title: "Monitoramento da Memória"
description: "Aprenda a interpretar amostras de memória, paginação, processos, E/S e CPU de vmstat."
meta_title: "Monitoramento da Memória - Utilização de Processos"
meta_description: "Domine o monitoramento da memória no Linux com o comando vmstat. Este guia explica como usar esse monitor para analisar métricas de desempenho do sistema."
meta_keywords: "monitoramento de memória, monitor de utilização da memória, vmstat, memória Linux, desempenho do sistema, uso da memória, tutorial Linux"
---

O Linux usa intencionalmente a memória que estaria ociosa para caches, portanto um valor pequeno em `free`, sozinho, não comprova pressão de memória. `vmstat` ajuda a relacionar a memória às tarefas executáveis, à paginação, à E/S e à atividade da CPU.

## Amostragem com vmstat

Colete uma amostra por segundo:

```bash
$ vmstat 1
```

A primeira linha de dados normalmente informa médias desde o boot; as linhas posteriores abrangem cada intervalo. Interrompa com `Ctrl-C` depois de capturar um período representativo. As unidades e os campos disponíveis variam, portanto consulte `vmstat --unit` e o manual local.

:::single-choice{#vmstat-interval-rows}
Quais linhas são mais adequadas para observar alterações a cada segundo com `vmstat 1`?

::option[As linhas posteriores ao relatório inicial.]{#vmstat-later-rows .correct explanation="As linhas posteriores descrevem cada intervalo solicitado, não o período acumulado."}
::option[Somente os cabeçalhos acima da primeira linha de dados.]{#vmstat-headings explanation="Os cabeçalhos definem os campos, mas não contêm amostras de atividade."}
::option[Somente uma linha copiada de outro host.]{#vmstat-other-host explanation="Um sistema diferente não representa a carga de trabalho atual."}
:::

## Processos e Memória

Os campos comuns de processos são `r`, tarefas executáveis, e `b`, tarefas bloqueadas em sono ininterruptível. Os campos de memória incluem swap usado (`swpd`), memória ociosa (`free`), buffers (`buff`) e cache (`cache`). Esses são valores de todo o sistema, não o consumo por processo.

Para obter uma visão mais simples da memória atualmente disponível, compare com:

```bash
$ free -h
```

A estimativa `available` normalmente é mais útil que apenas `free`, pois o cache recuperável pode atender a novas alocações.

:::single-choice{#vmstat-free-memory}
Por que um valor baixo de `free` pode ser normal no Linux?

::option[O valor sempre exclui toda a RAM física.]{#vmstat-excludes-ram explanation="Esse é um campo de memória, embora sua unidade exata deva ser verificada."}
::option[O kernel pode usar a memória ociosa para caches recuperáveis.]{#vmstat-reclaimable-cache .correct explanation="A memória em cache muitas vezes pode ser recuperada quando as aplicações precisam dela."}
::option[Um baixo valor de memória livre comprova que a CPU está desligada.]{#vmstat-cpu-off explanation="A alocação de memória e o estado de energia da CPU são conclusões não relacionadas."}
:::

## Paginação e E/S

`si` e `so` mostram as taxas de entrada e saída do swap. Uma paginação contínua combinada com latência e atividade de recuperação de memória pode indicar pressão, mas o uso de swap (`swpd`) diferente de zero não comprova por si só um problema atual. `bi` e `bo` informam as taxas de entrada e saída de blocos e não se limitam ao tráfego de swap.

:::single-choice{#vmstat-swap-pressure}
Qual evidência sustenta melhor o diagnóstico de pressão de memória atual?

::option[Um valor `swpd` diferente de zero sem nenhuma outra observação.]{#vmstat-swpd-alone explanation="As páginas podem permanecer no swap após uma pressão anterior, portanto a quantidade sozinha é insuficiente."}
::option[Paginação contínua relacionada à recuperação de memória e à latência da carga de trabalho.]{#vmstat-correlated-pressure .correct explanation="Evidências repetidas e relacionadas conectam o comportamento da memória ao impacto atual."}
::option[O nome do host mostrado durante o login.]{#vmstat-hostname explanation="O nome de um host não mede a recuperação nem a atividade de paginação."}
:::

## Atividade da CPU e do Sistema

As colunas da CPU normalmente incluem as porcentagens de usuário (`us`), sistema (`sy`), ocioso (`id`), espera por E/S (`wa`) e tempo tomado (`st`). As colunas do sistema incluem interrupções (`in`) e trocas de contexto (`cs`) por segundo. Interprete os picos em relação a uma linha de base; taxas altas de troca de contexto podem ser normais para algumas cargas.

:::single-choice{#vmstat-r-column}
O que o campo de processo `r` representa?

::option[Sistemas de arquivos montados somente para leitura.]{#vmstat-readonly explanation="As opções de montagem dos sistemas de arquivos não são representadas por esse campo de processo."}
::option[Usuários remotos com shells ativos.]{#vmstat-remote-users explanation="As sessões de login são informadas por outras ferramentas."}
::option[Tarefas executáveis ou que aguardam a CPU.]{#vmstat-runnable .correct explanation="Comparar essa contagem à capacidade da CPU pode ajudar a identificar sua demanda."}
:::

## Resumo

Agora você sabe interpretar `vmstat` como uma visão do sistema relacionada ao tempo.

1. Separe o relatório acumulado inicial das amostras dos intervalos.
2. Trate o cache como memória potencialmente recuperável.
3. Relacione a paginação à recuperação e ao impacto na aplicação.
4. Leia em conjunto os campos de processos, E/S, sistema e CPU.
