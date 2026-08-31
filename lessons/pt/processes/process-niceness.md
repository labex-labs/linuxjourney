---
lesson_id: "process-niceness"
course_id: "processes"
lang: "pt"
order_index: 8
title: "Niceness"
description: "Aprenda como os valores nice influenciam o peso do escalonamento da CPU para processos Linux comuns."
meta_title: "Niceness - Processos"
meta_description: "Descubra o que é niceness no Linux e como ele afeta a prioridade dos processos. Esta lição explica o uso dos comandos nice e renice para gerenciar o escalonamento da CPU."
meta_keywords: "niceness Linux, o que é niceness no Linux, niceness de processos Linux, prioridade de processos, comando nice, comando renice, escalonamento da CPU"
---

O Linux pode executar threads simultaneamente em diferentes núcleos da CPU e dividir o tempo de um núcleo entre mais threads executáveis do que consegue executar de uma vez. O escalonador faz essas escolhas de acordo com a política de escalonamento, a prioridade, a afinidade e a carga de trabalho. Um valor nice é uma das entradas usadas nas políticas comuns de compartilhamento de tempo.

## Interpretação dos Valores Nice

O intervalo convencional de nice vai de `-20` a `19`:

- Um valor menor atribui a uma tarefa um peso de escalonamento maior em relação a tarefas comparáveis.
- Um valor maior a torna mais “gentil” ao conceder-lhe um peso relativo menor.
- O padrão normalmente é `0`.

Niceness não reserva uma porcentagem da CPU nem garante a execução imediata. Seu efeito é mais visível quando tarefas executáveis comparáveis disputam tempo de CPU. Políticas de tempo real, cgroups, afinidade de CPU, esperas por E/S e outros controles podem predominar no comportamento observado.

:::single-choice{#process-niceness-lower-value}
Sob a mesma política comum de escalonamento, qual valor nice oferece maior peso relativo da CPU?

::option[`10`]{#process-niceness-value-ten explanation="Um valor positivo é mais gentil e normalmente possui menos peso que zero ou um valor negativo."}
::option[`19`]{#process-niceness-value-nineteen explanation="Esse é o extremo mais gentil do intervalo convencional e possui um peso relativamente baixo."}
::option[`-5`]{#process-niceness-value-minus-five .correct explanation="Valores nice menores correspondem a um peso relativo maior entre tarefas comuns comparáveis."}
:::

## Visualização do Niceness

Em `top`, a coluna `NI` exibe o valor nice. Você também pode solicitá-lo a `ps`:

```bash
$ ps -o pid,ni,pri,stat,cmd -p 3245
```

`NI` é o valor nice visível ao usuário. Uma coluna `PRI` ou semelhante pode representar uma prioridade derivada do escalonador, e sua escala varia conforme a ferramenta e a classe de escalonamento; portanto, não presuma que as duas colunas sejam intercambiáveis.

:::single-choice{#process-niceness-top-column}
Qual coluna de `top` normalmente exibe o valor nice?

::option[`PID`]{#process-niceness-column-pid explanation="`PID` identifica um processo, não mostra seu ajuste de escalonamento."}
::option[`TTY`]{#process-niceness-column-tty explanation="`TTY` identifica a associação com um terminal de controle."}
::option[`NI`]{#process-niceness-column-ni .correct explanation="`NI` é a abreviação convencional do valor nice do processo ou da thread."}
:::

## Início de um Comando com `nice`

Use `nice` para iniciar um novo comando com um valor ajustado:

```bash
$ nice -n 5 long-computation
```

O ajuste solicitado e a sintaxe aceita podem ser verificados no manual local. Um usuário sem privilégios normalmente pode tornar um comando mais gentil aumentando seu valor. Atribuir um valor nice menor e, portanto, um peso de escalonamento mais favorável exige privilégios adequados ou limites de recursos configurados.

:::single-choice{#process-niceness-nice-command}
O que `nice -n 5 long-computation` faz?

::option[Inicia o comando com o valor nice 5, se permitido.]{#process-niceness-start-five .correct explanation="`nice` inicia um novo comando usando o ajuste de escalonamento solicitado."}
::option[Altera o PID 5 para o menor valor nice possível.]{#process-niceness-pid-five explanation="O operando após `-n` é um valor nice, não um PID de destino."}
::option[Garante ao comando exatamente cinco por cento de uma CPU.]{#process-niceness-five-percent explanation="Os valores nice expressam peso relativo e não reservam porcentagens fixas da CPU."}
:::

## Alteração de um Processo Existente com `renice`

Use `renice` para um processo que já está em execução:

```bash
$ renice -n 10 -p 3245
```

Esse comando solicita o valor nice `10` para o PID `3245`. Verifique primeiro o destino, pois os PIDs podem ser reutilizados, e então confirme o valor resultante. As permissões dependem da propriedade, dos privilégios, dos limites de recursos e da política do sistema. Aumentar o valor nice normalmente é permitido para um processo que você possui; desfazer essa alteração pode não ser permitido sem privilégios.

:::single-choice{#process-niceness-renice-purpose}
Qual ferramenta altera o valor nice de um processo existente?

::option[`nice`]{#process-niceness-tool-nice explanation="`nice` inicia principalmente um novo comando com um valor ajustado."}
::option[`kill`]{#process-niceness-tool-kill explanation="`kill` envia sinais e não é o editor comum de niceness."}
::option[`renice`]{#process-niceness-tool-renice .correct explanation="`renice` atua sobre um PID, grupo de processos ou usuário existente, conforme suas opções."}
:::

O laboratório [Gerenciamento e Monitoramento de Processos Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) oferece um ambiente controlado para visualizar e alterar valores nice. Compare tarefas limitadas pela CPU em disputa, em vez de esperar uma diferença visível em um sistema ocioso.

## Resumo

Agora você sabe interpretar e ajustar niceness sem tratá-lo como uma garantia de CPU.

1. Leia valores nice menores como um peso relativo maior de escalonamento.
2. Inspecione `NI` separadamente dos campos de prioridade derivados.
3. Use `nice` ao iniciar um comando.
4. Use `renice` para um processo existente e verificado.
