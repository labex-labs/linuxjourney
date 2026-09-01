---
lesson_id: "controlling-terminal"
course_id: "processes"
lang: "pt"
order_index: 2
title: "Terminal de Controle"
description: "Aprenda como terminais de controle conectam sessões à entrada interativa, aos sinais e ao controle de tarefas do shell."
meta_title: "Terminal de Controle - Processos"
meta_description: "Conheça o conceito de terminal de controle no Linux. Aprenda o que é uma TTY, a diferença entre TTY e PTS e como usar a saída TTY de `ps` para identificar processos sem terminal de controle."
meta_keywords: "terminal de controle, ps tty, o que é tty, como usar ps, TTY, PTS, terminal Linux, processo daemon, processos Linux"
---

Uma sessão de login interativa pode possuir um terminal de controle: um dispositivo de terminal associado à sessão e usado pelo kernel para sinais gerados pelo terminal e para o controle de tarefas. O campo `TTY` nas listagens de processos ajuda a identificar essa associação.

## Dispositivos de Terminal e Pseudoterminal

O nome TTY vem dos teletipos históricos. No Linux moderno, as interfaces de terminal são abstrações de dispositivos e não necessariamente equipamentos físicos.

Um console virtual do sistema pode aparecer com um nome como `tty1`. Os atalhos da área de trabalho para alternar entre consoles variam conforme a distribuição e não devem ser presumidos. Um emulador de terminal, login remoto ou multiplexador normalmente usa um par de pseudoterminais, com o lado interativo mostrado por um nome como `pts/3`.

Exiba o terminal conectado à entrada padrão do comando atual com:

```bash
$ tty
/dev/pts/3
```

Esse resultado está relacionado ao conceito mais amplo de terminal de controle, mas não é idêntico a ele. Um processo pode redirecionar a entrada ou saída padrão e ainda permanecer em uma sessão que possui um terminal de controle.

:::single-choice{#controlling-terminal-pts-meaning} O que um nome como `pts/3` normalmente identifica?

::option[Um ID de processo atribuído ao terceiro shell.]{#controlling-terminal-pts-pid explanation="Um PID é um metadado numérico do processo e não é expresso como um nome de dispositivo `pts/N`."}
::option[Um dispositivo de pseudoterminal usado por uma sessão interativa.]{#controlling-terminal-pts-device .correct explanation="As entradas em `/dev/pts` são dispositivos escravos de pseudoterminais, normalmente usados por emuladores de terminal e sessões remotas."}
::option[Uma partição do sistema de arquivos que contém programas de terminal.]{#controlling-terminal-pts-partition explanation="O nome identifica uma interface de dispositivo de terminal, não uma partição de armazenamento."}
:::

## Sessões, Grupos de Processos e Controle de Tarefas

Um terminal de controle pertence a uma sessão, não apenas ao comando que abriu uma janela. Dentro dessa sessão, o terminal acompanha um grupo de processos em primeiro plano. O shell coloca um pipeline em primeiro plano nesse grupo para que ele possa ler entradas e receber sinais gerados pelo terminal.

Por exemplo, pressionar `Ctrl-C` normalmente faz o driver do terminal enviar `SIGINT` ao grupo de processos em primeiro plano. Um grupo em segundo plano que tenta ler do terminal pode receber `SIGTTIN`. Essas regras permitem que o shell coordene tarefas em primeiro e segundo plano.

:::single-choice{#controlling-terminal-ctrl-c-target} Para quais processos um terminal normalmente direciona o sinal gerado por `Ctrl-C`?

::option[Todos os processos pertencentes ao usuário atual.]{#controlling-terminal-ctrl-c-user explanation="Os sinais gerados pelo terminal se restringem ao grupo de processos em primeiro plano, não a todos os processos de um usuário."}
::option[Somente o shell de login, independentemente da tarefa em primeiro plano.]{#controlling-terminal-ctrl-c-shell explanation="Enquanto outra tarefa estiver em primeiro plano, o grupo dessa tarefa será o destino normal do sinal."}
::option[O grupo de processos em primeiro plano do terminal.]{#controlling-terminal-ctrl-c-foreground .correct explanation="O driver do terminal envia `SIGINT` ao grupo de processos atualmente em primeiro plano."}
:::

## Leitura da Coluna `TTY`

Solicite explicitamente os campos de processos quando quiser uma visualização estável:

```bash
$ ps -o pid,tty,stat,cmd
```

Um nome de terminal como `pts/3` identifica o terminal de controle registrado para aquele processo. Um ponto de interrogação (`?`) normalmente significa que o processo não possui um terminal de controle.

Muitos processos de serviços não possuem um terminal de controle porque um gerenciador de serviços os inicia independentemente de uma sessão de login interativa. Contudo, a ausência de uma TTY não comprova por si só que um processo seja um daemon, e uma tarefa do shell em segundo plano ainda pode possuir um terminal de controle.

:::single-choice{#controlling-terminal-question-mark} O que `?` na coluna `TTY` de `ps` normalmente significa?

::option[O processo não possui um terminal de controle.]{#controlling-terminal-no-tty .correct explanation="Um ponto de interrogação é a representação convencional quando nenhum terminal de controle está associado ao processo."}
::option[O terminal do processo não pôde ser lido porque está ocupado.]{#controlling-terminal-busy-tty explanation="O marcador representa a ausência de um terminal de controle, não uma disputa temporária pelo dispositivo."}
::option[O processo sempre é uma thread do kernel.]{#controlling-terminal-kernel-only explanation="Threads do kernel muitas vezes não possuem terminais, mas muitos serviços do espaço do usuário também não."}
:::

## Fechamento do Terminal e Hangups

Quando a conexão de um terminal desaparece, o kernel ou o software do terminal/sessão pode enviar `SIGHUP` aos processos associados. Um processo pode terminar, capturar o sinal, ignorá-lo ou já ter sido configurado para sobreviver a ele. Recursos do shell como `disown`, utilitários como `nohup`, multiplexadores e gerenciadores de serviços afetam o comportamento do ciclo de vida.

Portanto, fechar um terminal não garante que todos os comandos iniciados nele terminarão. Inspecione a sessão do processo, o tratamento dos sinais, os redirecionamentos e o supervisor quando a persistência for importante.

:::single-choice{#controlling-terminal-close-effect} Por que é incorreto afirmar que fechar um terminal sempre encerra todos os processos iniciados nele?

::option[Os terminais Linux nunca geram sinais quando são fechados.]{#controlling-terminal-never-signals explanation="A sinalização de hangup é um comportamento real dos terminais e sessões, embora seu resultado não seja necessariamente o encerramento."}
::option[Somente processos com PIDs numéricos podem receber hangups.]{#controlling-terminal-pid-hangup explanation="Todos os processos comuns possuem PIDs numéricos; esse fato não determina a sobrevivência ao fechamento do terminal."}
::option[Os processos podem tratar ou evitar o hangup e ser gerenciados independentemente.]{#controlling-terminal-hangup-handling .correct explanation="A disposição dos sinais, o comportamento do shell, os multiplexadores e os supervisores podem permitir que um processo continue após o fechamento do terminal."}
:::

O laboratório [Gerenciamento e Monitoramento de Processos Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) oferece um ambiente seguro para comparar tarefas em primeiro e segundo plano e seus campos `TTY`.

## Resumo

Agora você sabe relacionar um terminal de controle ao gerenciamento interativo de processos.

1. Diferencie terminais virtuais de pseudoterminais.
2. Relacione os sinais do terminal ao grupo de processos em primeiro plano.
3. Interprete nomes de terminais e `?` na saída de `ps`.
4. Trate o fechamento do terminal como uma sinalização, não como encerramento garantido dos processos.
