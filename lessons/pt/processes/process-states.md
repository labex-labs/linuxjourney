---
lesson_id: "process-states"
course_id: "processes"
lang: "pt"
order_index: 9
title: "Estados dos Processos"
description: "Aprenda a interpretar os códigos comuns de estados de processos Linux em snapshots de `ps`."
meta_title: "Estados dos Processos - Processos"
meta_description: "Um guia completo dos estados de processos Linux. Aprenda sobre os diferentes estados R, S, D, Z e T e como interpretá-los usando o comando ps."
meta_keywords: "estados de processos Linux, estado de processo no Linux, estados de processos explicados, comando ps, códigos STAT, gerenciamento de processos"
---

Uma tarefa Linux transita entre estados de execução enquanto trabalha, aguarda, é interrompida e termina. O campo `STAT` de `ps` captura um único momento, portanto observações repetidas são mais úteis que uma única letra ao diagnosticar um comportamento.

```bash
$ ps -o pid,ppid,stat,wchan:24,cmd
```

O primeiro caractere de `STAT` é o estado principal. Os caracteres adicionais são modificadores que descrevem propriedades como a liderança da sessão ou a participação no grupo de processos em primeiro plano. Consulte o manual local de `ps` para conhecer o conjunto completo.

## Execução e Sono Interrompível

- `R` significa em execução ou executável. A tarefa está sendo executada em uma CPU ou aguardando tempo de CPU em uma fila de execução.
- `S` significa sono interrompível. A tarefa aguarda um evento e pode ser despertada por um sinal ou evento apropriado.

Dormir é normal. Programas interativos e serviços passam grande parte do tempo aguardando entradas, temporizadores, tráfego de rede, bloqueios ou outros eventos, em vez de consumir CPU continuamente.

:::single-choice{#process-states-runnable-code}
O que significa o estado principal `R`?

::option[Em execução em uma CPU ou pronto para executar.]{#process-states-r-running .correct explanation="`R` reúne tarefas atualmente em execução e tarefas executáveis que aguardam atendimento da CPU."}
::option[Coletado depois que seu pai recuperou o status.]{#process-states-r-reaped explanation="Um processo totalmente coletado deixa de aparecer como uma entrada comum da tabela de processos."}
::option[Aguardando em sono ininterruptível.]{#process-states-r-uninterruptible explanation="O sono ininterruptível é representado por `D`."}
:::

:::single-choice{#process-states-interruptible-code}
Qual estado principal representa um sono interrompível?

::option[`D`]{#process-states-sleep-d explanation="`D` indica sono ininterruptível."}
::option[`Z`]{#process-states-sleep-z explanation="`Z` indica um filho encerrado cujo status ainda não foi coletado."}
::option[`S`]{#process-states-sleep-s .correct explanation="`S` é o código convencional de `ps` para uma espera interrompível."}
:::

## Sono Ininterruptível

`D` significa sono ininterruptível, normalmente enquanto a tarefa aguarda em uma operação do kernel, como determinados tipos de E/S de armazenamento ou de sistemas de arquivos de rede. A tarefa não reage a sinais comuns até sair dessa espera; enquanto isso, um sinal pode permanecer pendente.

Um estado `D` breve pode ser normal. Tarefas persistentes ou numerosas em `D` podem indicar E/S lenta, indisponível ou com falhas, mas o estado sozinho não identifica a causa. Inspecione o canal de espera, os logs do kernel, a integridade do armazenamento e da rede e o subsistema relevante antes de tirar conclusões.

:::single-choice{#process-states-uninterruptible-code}
Qual estado principal indica sono ininterruptível?

::option[`T`]{#process-states-d-stopped explanation="`T` identifica uma tarefa interrompida."}
::option[`D`]{#process-states-d-uninterruptible .correct explanation="`D` é usado para uma tarefa que aguarda em um sono ininterruptível do kernel."}
::option[`R`]{#process-states-d-runnable explanation="`R` identifica uma tarefa em execução ou executável."}
:::

## Estados Interrompido e Zumbi

- `T` normalmente significa interrompido por uma ação de controle de tarefas, como `SIGTSTP`, ou por `SIGSTOP`. Algumas ferramentas usam `t` minúsculo para uma parada de rastreamento.
- `Z` significa zumbi: o processo terminou, mas seu pai ainda não coletou o registro de encerramento.

Retome uma parada por controle de tarefas com `SIGCONT` quando for apropriado. Um zumbi não pode ser retomado nem encerrado, pois já não está executando; seu pai ou um coletor adotante precisa coletá-lo.

:::single-choice{#process-states-zombie-code}
O que o estado principal `Z` identifica?

::option[Um processo encerrado cujo registro de encerramento aguarda coleta.]{#process-states-z-zombie .correct explanation="Um zumbi mantém um estado mínimo visível ao pai depois que a execução termina."}
::option[Um processo pausado por um sinal de suspensão do terminal.]{#process-states-z-terminal-stop explanation="Uma parada por controle de tarefas normalmente é mostrada como `T`."}
::option[Um processo que atualmente usa um núcleo inteiro da CPU.]{#process-states-z-cpu explanation="Uma tarefa em execução é representada por `R`, enquanto um zumbi não executa instruções."}
:::

## Leitura dos Estados em Contexto

Os códigos de estado são observações, não diagnósticos. Combine-os com tempo decorrido, uso da CPU, canais de espera, relações entre pais e filhos, logs e amostras repetidas. Uma tarefa pode mudar de estado entre o instante em que o kernel o informa e o momento em que você lê a tela.

O laboratório [Gerenciamento e Monitoramento de Processos Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) oferece um ambiente seguro para observar tarefas em primeiro plano, dormindo, interrompidas e encerradas.

## Resumo

Agora você sabe interpretar os estados principais mais comuns dos processos.

1. Leia `R` como em execução ou executável e `S` como sono interrompível.
2. Investigue um `D` persistente como sintoma de espera, não como diagnóstico.
3. Diferencie o `T` interrompido do `Z` encerrado e ainda não coletado.
4. Use observações repetidas e evidências do contexto.
