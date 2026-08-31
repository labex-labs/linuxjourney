---
lesson_id: "killing-processes"
course_id: "processes"
lang: "pt"
order_index: 7
title: "kill (Encerrar)"
description: "Aprenda a identificar um processo e enviar um sinal adequado com `kill` usando uma sequência segura de escalonamento."
meta_title: "kill (Encerrar) - Processos"
meta_description: "Domine o comando kill do Linux para gerenciar e encerrar processos. Este guia aborda as diferenças entre kill e terminate e explica sinais como SIGTERM, SIGKILL e SIGHUP."
meta_keywords: "comando kill, kill sigterm, kill sighup, Linux kill -0, kill versus terminate, kill -15 Linux, SIGTERM, SIGKILL, gerenciamento de processos, encerrar processo"
---

O comando `kill` envia um sinal a um processo ou grupo de processos. Seu nome é histórico: o sinal solicitado pode encerrar, interromper, continuar ou pedir alguma ação definida pela aplicação. Sempre confirme o destino exato e compreenda o comportamento documentado dos sinais do programa antes de enviar um.

## Solicitação de um Encerramento Ordenado

Com apenas um PID, `kill` envia `SIGTERM` por padrão:

```bash
$ kill 12445
```

Prefira o nome simbólico ao especificar um sinal explicitamente:

```bash
$ kill -TERM 12445
```

`SIGTERM` possui como ação padrão o encerramento, mas um programa pode capturá-lo ou ignorá-lo. Um serviço bem projetado pode usar um manipulador para parar de aceitar trabalhos, salvar o estado apropriado e liberar recursos da aplicação. Essa é uma possibilidade, não uma garantia de limpeza imediata ou bem-sucedida.

:::single-choice{#killing-processes-default-signal}
Qual sinal `kill PID` solicita por padrão?

::option[`SIGKILL`]{#killing-processes-default-kill explanation="O sinal forçado que não pode ser capturado precisa ser selecionado explicitamente."}
::option[`SIGTERM`]{#killing-processes-default-term .correct explanation="Sem outro operando de sinal, `kill` envia a solicitação padrão de encerramento."}
::option[`SIGSTOP`]{#killing-processes-default-stop explanation="Interromper um processo não é a ação padrão solicitada por `kill`."}
:::

## Verificação do Destino

Os PIDs podem ser reutilizados, portanto um PID antigo pode identificar outro processo mais tarde. Inspecione o destino ativo imediatamente antes de agir:

```bash
$ ps -p 12445 -o pid,ppid,user,lstart,stat,cmd
```

Verifique seu usuário, horário de início, comando, pai, serviço proprietário e função operacional. Se um gerenciador de serviços controlar o processo, use o comando de parada ou recarga desse gerenciador quando possível, para que ele mantenha o estado correto e não reinicie imediatamente o filho.

Você pode sinalizar os processos que possui, sujeito às regras de credenciais. Sinalizar o processo de outro usuário normalmente exige privilégios adequados. Não use um comando amplo baseado em nomes antes de revisar todas as correspondências.

:::single-choice{#killing-processes-pid-reuse}
Por que você deve inspecionar um PID imediatamente antes de sinalizá-lo?

::option[Um PID muda toda vez que o processo lê um arquivo.]{#killing-processes-pid-read explanation="Um processo ativo normalmente mantém o mesmo PID durante toda a sua existência."}
::option[O kernel pode reutilizar um PID depois que o processo anterior termina.]{#killing-processes-pid-reused .correct explanation="Um PID numérico lembrado pode mais tarde se referir a outro processo ativo."}
::option[`kill` aceita nomes de comandos, mas não identificadores numéricos.]{#killing-processes-no-numeric explanation="Um PID numérico é o operando de destino comum de `kill`."}
:::

## Verificação da Permissão de Sinal com o Sinal Zero

O sinal de número zero realiza verificações de erros sem entregar um sinal real:

```bash
$ kill -0 12445
```

Um resultado bem-sucedido significa que um processo com esse PID existe e que o solicitante tem permissão para sinalizá-lo naquele instante. Uma falha é ambígua: o processo pode não existir ou o solicitante pode não ter permissão. Examine o erro e o status de saída, em vez de traduzir toda falha como “não está em execução”. Essa também é apenas uma verificação momentânea e não elimina uma condição de corrida posterior por reutilização do PID.

:::single-choice{#killing-processes-signal-zero}
O que um `kill -0 PID` bem-sucedido estabelece naquele momento?

::option[O processo concluiu toda a limpeza e terminou.]{#killing-processes-zero-exited explanation="O sucesso indica um destino ativo que pode ser sinalizado, não o encerramento concluído."}
::option[O processo manterá esse PID permanentemente.]{#killing-processes-zero-permanent explanation="A verificação é instantânea, e os PIDs podem ser reutilizados após o encerramento."}
::option[O processo existe, e o solicitante pode sinalizá-lo.]{#killing-processes-zero-permitted .correct explanation="O sinal zero verifica a existência e a autorização do destino sem entregar um sinal comum."}
:::

## Escalonamento Somente Quando Necessário

Se um destino autorizado não terminar após `SIGTERM`, aguarde um tempo adequado à carga de trabalho e investigue o motivo. Então, quando o encerramento forçado for justificável, envie:

```bash
$ kill -KILL 12445
```

`SIGKILL` não pode ser capturado, ignorado nem bloqueado, portanto o programa não consegue realizar uma limpeza no nível da aplicação. Ele pode deixar transações incompletas, estados temporários ou trabalho de recuperação para outros componentes. Use-o como escalonamento, não como primeira medida rotineira.

Outros sinais só possuem significado conforme o contrato do programa receptor. `SIGHUP` costuma solicitar a recarga da configuração, mas alguns programas mantêm seu comportamento padrão de encerramento. `SIGSTOP` pausa sem limpeza, e `SIGCONT` retoma um processo interrompido.

:::single-choice{#killing-processes-kill-tradeoff}
Qual é a principal desvantagem operacional de `SIGKILL`?

::option[Ele só pode ser tratado pelo proprietário do processo.]{#killing-processes-kill-owner-handler explanation="Nenhum processo de destino pode instalar um manipulador para `SIGKILL`."}
::option[Ele pausa o processo, mas nunca o encerra.]{#killing-processes-kill-pauses explanation="`SIGSTOP` pausa; `SIGKILL` encerra."}
::option[Ele não oferece ao programa oportunidade para a limpeza no nível da aplicação.]{#killing-processes-kill-no-cleanup .correct explanation="O kernel impõe o encerramento sem invocar um manipulador de sinais no espaço do usuário."}
:::

Pratique a seleção de sinais somente em processos que você iniciou em um ambiente isolado. O laboratório [Gerenciamento e Monitoramento de Processos Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) oferece um fluxo controlado de inspeção e encerramento.

## Resumo

Agora você sabe enviar sinais a processos com um fluxo deliberado e verificável.

1. Confirme o destino ativo e seu supervisor antes de agir.
2. Use `SIGTERM` como solicitação normal de encerramento.
3. Interprete o sinal zero como uma verificação momentânea de existência e permissão.
4. Reserve `SIGKILL` para um escalonamento justificado após a investigação.
