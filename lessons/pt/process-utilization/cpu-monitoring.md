---
lesson_id: "cpu-monitoring"
course_id: "process-utilization"
lang: "pt"
order_index: 4
title: "Monitoramento da CPU"
description: "Aprenda a interpretar as médias de carga do Linux junto com a quantidade de CPUs, a utilização e o estado das tarefas."
meta_title: "Monitoramento da CPU - Utilização de Processos"
meta_description: "Aprenda os fundamentos do monitoramento da CPU no Linux usando o comando uptime. Este guia explica como interpretar a carga média, entender a utilização dos processos e avaliar o desempenho do sistema."
meta_keywords: "comando uptime, monitoramento CPU Linux, carga média, desempenho do sistema, utilização de processos, tutorial Linux, guia para iniciantes"
---

A solução de problemas da CPU começa pela separação entre carga, utilização e capacidade de resposta. Nenhum número isolado comprova um gargalo, portanto compare vários intervalos de tempo e relacione as métricas do host à carga de trabalho realmente percebida pelos usuários.

## Leitura de uptime

`uptime` fornece um ponto de partida compacto:

```text
$ uptime
 17:23:35 up 1 day, 5:59, 2 users, load average: 0.00, 0.02, 0.05
```

Os três valores finais são as médias de carga durante aproximadamente 1, 5 e 15 minutos. Compará-los mostra a direção: um valor de 1 minuto muito maior pode indicar carga crescente, enquanto um valor de 15 minutos maior pode indicar uma carga em queda.

:::single-choice{#cpu-uptime-windows}
Em que ordem `uptime` exibe os intervalos de carga média?

::option[15, 5 e 1 segundos.]{#cpu-windows-seconds explanation="Os valores são médias em escala de minutos e não aparecem do mais longo para o mais curto."}
::option[1, 5 e 15 minutos.]{#cpu-windows-one-five-fifteen .correct explanation="O intervalo recente mais curto aparece primeiro, e o mais longo aparece por último."}
::option[Porcentagens atual, mínima e máxima da CPU.]{#cpu-windows-percentages explanation="A carga média não é uma porcentagem mínima ou máxima da CPU."}
:::

## Compreensão da Carga no Linux

A carga média do Linux conta as tarefas executáveis, incluindo as que usam ou aguardam CPU, e as tarefas em sono ininterruptível, normalmente associadas à E/S. Portanto, ela não é o mesmo que a utilização da CPU.

Uma carga de `4.0` possui implicações diferentes em sistemas com uma e dezesseis CPUs lógicas. Descubra a quantidade de unidades de processamento disponíveis para o sistema com:

```bash
$ nproc
```

Cotas de CPU, afinidade, virtualização e limites de contêineres podem reduzir a capacidade visível para determinada carga de trabalho, portanto a quantidade de CPUs do host é apenas um ponto de partida.

:::single-choice{#cpu-load-not-percentage}
Por que a carga média não é uma porcentagem de utilização da CPU?

::option[Ela informa somente a frequência do clock da CPU.]{#cpu-load-clock explanation="A velocidade do clock é uma métrica separada de hardware ou escalonamento."}
::option[Ela mede somente a memória física livre.]{#cpu-load-memory explanation="A disponibilidade de memória é informada por outras métricas."}
::option[Ela inclui tarefas executáveis e tarefas em sono ininterruptível.]{#cpu-load-task-count .correct explanation="A carga se baseia na demanda e no estado de espera das tarefas, não em uma porcentagem do tempo de CPU decorrido."}
:::

## Comparação da Carga com a Atividade da CPU

Colete várias amostras, em vez de depender de uma única saída. Algumas ferramentas complementares úteis são:

```bash
$ top
$ vmstat 1
$ mpstat -P ALL 1
```

`top` combina visualizações do host e dos processos. `vmstat` mostra as contagens de tarefas executáveis e bloqueadas junto com categorias da CPU. `mpstat`, fornecido pelo `sysstat` em muitas distribuições, mostra a atividade por CPU. A disponibilidade e os campos exatos variam, portanto consulte os manuais locais.

Uma carga alta com CPUs ocupadas pode indicar demanda de CPU. Uma carga alta com muitas tarefas bloqueadas, latência de E/S ou observações de espera por E/S aponta para outro recurso limitado. Uma utilização média baixa também pode ocultar uma única CPU saturada ou um pico breve de latência.

:::single-choice{#cpu-high-load-next-step}
Qual é a melhor próxima etapa após observar uma carga média alta?

::option[Comparar medições repetidas de CPU, estados das tarefas, E/S e carga de trabalho.]{#cpu-load-correlate .correct explanation="Amostras relacionadas diferenciam as possíveis explicações para a carga."}
::option[Reiniciar imediatamente sem coletar outros dados.]{#cpu-load-reboot explanation="A reinicialização remove evidências e pode interromper serviços sem identificar a causa."}
::option[Presumir que todas as CPUs estejam totalmente utilizadas.]{#cpu-load-assume explanation="A carga pode incluir tarefas ininterruptíveis e estar distribuída de forma desigual entre as CPUs."}
:::

## Avaliação da Capacidade e do Impacto

Não existe uma regra universal de que a carga sempre deva permanecer abaixo da quantidade de CPUs. Sistemas em lote podem aceitar filas, enquanto serviços interativos podem violar metas de latência antes desse ponto. Estabeleça uma linha de base para o mesmo host e a mesma carga de trabalho e depois compare tempo de resposta, throughput, taxa de erros, saturação e uso de recursos.

:::single-choice{#cpu-capacity-threshold}
O que deve determinar se a carga observada é aceitável?

::option[Uma exigência de que o valor sempre permaneça abaixo de um.]{#cpu-below-one explanation="A capacidade de vários núcleos e os objetivos da carga de trabalho tornam esse limite fixo pouco confiável."}
::option[Somente a quantidade de usuários listados por `uptime`.]{#cpu-user-count explanation="Os usuários conectados por shells não representam toda a demanda da carga de trabalho."}
::option[A linha de base e os objetivos de serviço da carga de trabalho.]{#cpu-baseline-objectives .correct explanation="A aceitabilidade depende do comportamento esperado e do desempenho percebido pelos usuários, não de um limite universal."}
:::

## Resumo

Agora você sabe interpretar a carga média como uma parte da investigação da CPU.

1. Leia os intervalos de carga de 1, 5 e 15 minutos.
2. Diferencie a carga das tarefas das porcentagens de tempo da CPU.
3. Compare a carga com a capacidade de processamento disponível.
4. Relacione medições repetidas do host aos resultados dos serviços.
