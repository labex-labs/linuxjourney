---
lesson_id: "tracking-processes-top"
course_id: "process-utilization"
lang: "pt"
order_index: 1
title: "Acompanhamento de Processos: top"
description: "Aprenda a usar top para interpretar a carga do sistema, CPU, memória e atividade por processo."
meta_title: "Acompanhamento de Processos: top - Utilização de Processos"
meta_description: "Domine o comando `top` para monitorar recursos do sistema, acompanhar processos e entender métricas como VIRT e RES."
meta_keywords: "comando top Linux, monitorar processos, utilização do sistema, como Linux funciona, Linux top VIRT RES, desempenho Linux, gerenciamento de processos"
---

`top` fornece uma visualização atualizada repetidamente da atividade do sistema e dos processos em execução. Ele é útil para formular uma hipótese de desempenho, mas uma única amostra com muita atividade não comprova a causa de um problema. Compare várias atualizações e relacione-as aos logs e às métricas específicas da carga de trabalho.

## Leitura do Resumo do Sistema

Uma exibição comum começa com linhas de resumo seguidas por uma tabela de processos:

```text
top - 18:06:26 up 6 days, 4:07, 2 users, load average: 0.92, 0.62, 0.59
Tasks: 389 total, 1 running, 387 sleeping, 0 stopped, 1 zombie
%Cpu(s): 1.8 us, 0.4 sy, 0.0 ni, 97.6 id, 0.1 wa, 0.0 hi, 0.0 si, 0.0 st
MiB Mem : 32099.0 total, 5276.3 free, 7031.2 used, 19791.5 buff/cache
MiB Swap: 32700.0 total, 32661.0 free, 39.0 used
```

A primeira linha contém o horário atual, o tempo em atividade, a quantidade de usuários conectados e as médias de carga de 1, 5 e 15 minutos. A linha de tarefas conta os estados dos processos. A carga média não é uma porcentagem direta de CPU; no Linux, ela representa tarefas executáveis e tarefas em sono ininterruptível, portanto interprete-a junto com a quantidade de CPUs, a atividade de E/S e a latência.

:::single-choice{#top-load-average-periods} O que os três valores de carga média em `top` representam?

::option[A carga média durante 1, 5 e 15 minutos.]{#top-one-five-fifteen .correct explanation="Os valores resumem intervalos recentes de tempo progressivamente maiores."}
::option[O uso da CPU pelos três processos mais ocupados.]{#top-three-processes explanation="A CPU por processo aparece na tabela de processos, não nesses três valores de resumo."}
::option[A memória livre, o cache e o swap em megabytes.]{#top-three-memory-values explanation="A memória e o swap possuem linhas de resumo separadas."}
:::

## Interpretação do Tempo de CPU

Alguns campos comuns da CPU são:

- `us`: tempo de execução no espaço do usuário.
- `sy`: tempo de execução no kernel.
- `ni`: tempo no espaço do usuário para tarefas com nice ajustado.
- `id`: tempo ocioso.
- `wa`: tempo ocioso enquanto existe uma solicitação de E/S pendente.
- `hi` e `si`: tratamento de interrupções de hardware e software.
- `st`: tempo de CPU virtual usado pelo hipervisor para outros convidados.

Um valor alto de `wa` pode sustentar uma hipótese de espera por E/S, mas não identifica um dispositivo nem comprova que o armazenamento seja o único gargalo. Inspecione a latência do dispositivo e o comportamento da aplicação antes de concluir.

:::single-choice{#top-cpu-wa-meaning} O que o campo de CPU `wa` informa?

::option[O tempo gasto executando código comum do usuário.]{#top-wa-user explanation="A execução no espaço do usuário é informada em `us`."}
::option[As páginas de memória gravadas no swap desde o boot.]{#top-wa-swap explanation="A atividade de swap não é uma categoria de tempo de CPU."}
::option[O tempo ocioso da CPU enquanto existe uma solicitação de E/S pendente.]{#top-wa-io .correct explanation="O campo representa o tempo de espera por E/S e precisa de evidências do dispositivo para um diagnóstico."}
:::

## Leitura da Tabela de Processos

As colunas importantes normalmente incluem:

- `PID`, `USER` e `COMMAND`: identidade e propriedade.
- `S`: estado, como em execução (`R`), dormindo (`S`), sono ininterruptível (`D`), interrompido (`T`) ou zumbi (`Z`).
- `%CPU` e `%MEM`: atividade amostrada da CPU e parcela da memória física.
- `TIME+`: tempo de CPU acumulado.
- `VIRT`: espaço total de endereços virtuais associado à tarefa.
- `RES`: memória física residente e não transferida para o swap atualmente atribuída à tarefa.
- `SHR`: memória residente que pode ser compartilhada com outros processos.

`VIRT` não é a quantidade de RAM física consumida. Ele pode incluir arquivos mapeados, bibliotecas compartilhadas, espaço de endereços reservado e páginas no swap. Até mesmo `RES` deve ser interpretado com cuidado, pois as páginas compartilhadas complicam a atribuição.

:::single-choice{#top-res-versus-virt} Qual campo se aproxima mais da memória física atualmente residente de um processo?

::option[`TIME+`]{#top-time-field explanation="Esse campo acumula tempo de CPU, não memória."}
::option[`VIRT`]{#top-virt-field explanation="O tamanho virtual inclui espaço de endereços que não precisa estar residente na RAM."}
::option[`RES`]{#top-res-field .correct explanation="O tamanho residente representa páginas físicas atualmente residentes para o processo, considerando as ressalvas de compartilhamento."}
:::

## Foco e Ordenação

Monitore diretamente PIDs conhecidos:

```bash
$ top -p 1234,5678
```

Dentro de `top`, pressione `P` para ordenar por CPU, `M` para ordenar por memória, `1` para alternar as linhas por CPU e `q` para sair nas implementações comuns do procps-ng. Pressione `h` para consultar a ajuda interativa local, pois as teclas e os campos podem variar entre implementações.

Registre o PID, o comando, o timestamp e várias amostras antes de agir. Um processo chegar brevemente ao topo pode ser normal, e encerrá-lo pode causar perda de dados ou uma indisponibilidade.

:::single-choice{#top-monitor-known-pid} Qual invocação limita a exibição ao PID 1234?

::option[`top -u 1234`]{#top-user-filter explanation="A forma `-u` filtra por usuário, em vez de tratar o valor como um PID."}
::option[`top -d 1234`]{#top-delay-filter explanation="A opção `-d` controla o intervalo de atualização nas implementações comuns."}
::option[`top -p 1234`]{#top-pid-filter .correct explanation="A opção `-p` seleciona um ou mais IDs de processos para monitoramento."}
:::

## Resumo

Agora você sabe usar `top` para formular e testar uma hipótese de desempenho do sistema.

1. Leia as médias de carga como cargas em intervalos de tempo, não porcentagens de CPU.
2. Compare as categorias de CPU em várias amostras.
3. Diferencie o espaço de endereços virtual da memória residente.
4. Concentre-se em PIDs conhecidos e verifique as evidências antes de agir.
