---
lesson_id: "job-control"
course_id: "processes"
lang: "pt"
order_index: 11
title: "Controle de Tarefas"
description: "Aprenda como um shell interativo gerencia tarefas em primeiro plano, segundo plano e interrompidas."
meta_title: "Controle de Tarefas - Processos"
meta_description: "Conheça o controle de tarefas no Linux para gerenciar processos em segundo plano. Aprenda a usar os comandos jobs, bg, fg e kill para trabalhar com várias tarefas no shell."
meta_keywords: "controle de tarefas Linux, processos em segundo plano, comando jobs, comando bg, comando fg, comando kill, tutorial Linux, Linux para iniciantes"
---

Os shells interativos usam o controle de tarefas para coordenar pipelines dentro de uma sessão de terminal. Uma tarefa pode conter um processo ou um pipeline inteiro, normalmente agrupado em um grupo de processos para que o terminal e o shell possam agir sobre ele como uma unidade.

## Início de uma Tarefa em Segundo Plano

Acrescente `&` para iniciar um pipeline de forma assíncrona:

```bash
$ sleep 1000 &
[1] 18420
```

O shell retorna um prompt sem aguardar o fim da tarefa. O estado em segundo plano não redireciona automaticamente a saída, não desanexa o terminal de controle nem faz a tarefa sobreviver ao logout. Redirecione a entrada e a saída explicitamente quando necessário e use um gerenciador de serviços, agendador ou multiplexador de terminais para trabalhos que precisam sobreviver ao shell interativo.

Uma tarefa em segundo plano que tenta ler do terminal de controle normalmente é interrompida com `SIGTTIN`, pois não pertence ao grupo de processos em primeiro plano do terminal.

:::single-choice{#job-control-ampersand-effect} O que um `&` final solicita a um shell interativo?

::option[Garantir que a tarefa sobreviva ao logout e à reinicialização do sistema.]{#job-control-survive-restart explanation="A execução em segundo plano, sozinha, não oferece supervisão duradoura nem persistência após a reinicialização."}
::option[Executar o pipeline como uma tarefa em segundo plano sem aguardar antes do próximo prompt.]{#job-control-background-job .correct explanation="O shell inicia a tarefa de forma assíncrona e permanece disponível para outros comandos."}
::option[Descartar a saída e os erros padrão da tarefa.]{#job-control-discard-output explanation="A menos que sejam redirecionados, uma tarefa em segundo plano ainda pode gravar no terminal."}
:::

## Listagem das Tarefas do Shell

O comando interno `jobs` lista as tarefas conhecidas pelo shell atual:

```text
$ jobs
[1]    Running    sleep 1000 &
[2]-   Running    sleep 1001 &
[3]+   Stopped    sleep 1002
```

O número entre colchetes é um ID de tarefa do shell, não um PID. Um prefixo `%` forma uma especificação de tarefa, como `%1`. O marcador `+` identifica a tarefa atual selecionada por muitos comandos quando nenhum operando é fornecido; `-` identifica a tarefa anterior.

Como a tabela de tarefas pertence a um único shell, o shell de outro terminal normalmente não consegue listar nem endereçar essas tarefas por seus próprios comandos internos `jobs`, `fg` ou `bg`.

:::single-choice{#job-control-jobs-scope} O que o comando interno `jobs` lista?

::option[As tarefas acompanhadas pela sessão atual do shell.]{#job-control-jobs-current-shell .correct explanation="Os IDs e estados das tarefas são mantidos pelo shell interativo que iniciou ou adotou essas tarefas."}
::option[Todos os processos atualmente visíveis no sistema.]{#job-control-jobs-all-processes explanation="A inspeção de processos de todo o sistema pertence a ferramentas como `ps`; a tabela de tarefas do shell é mais restrita."}
::option[Somente serviços iniciados durante o boot do sistema.]{#job-control-jobs-boot-services explanation="Os serviços de boot normalmente são supervisionados por um gerenciador de serviços, não pela tabela de tarefas do shell interativo."}
:::

## Interrupção e Continuação de uma Tarefa

Enquanto uma tarefa está em primeiro plano, pressionar `Ctrl-Z` normalmente faz o terminal enviar `SIGTSTP` ao grupo de processos em primeiro plano. O shell recupera o controle depois que a tarefa é interrompida:

```text
$ sleep 1002
^Z
[3]+  Stopped    sleep 1002
```

Continue a tarefa atual interrompida em segundo plano com:

```bash
$ bg
```

`bg` envia um sinal de continuação e mantém a tarefa fora do primeiro plano do terminal. Ele só é útil para uma tarefa interrompida; um comando que já está em execução em segundo plano não precisa ser retomado.

:::single-choice{#job-control-bg-purpose} O que `bg %3` faz com a tarefa 3 interrompida?

::option[Move seus arquivos para um diretório chamado `bg`.]{#job-control-bg-files explanation="`bg` é um comando interno de controle de tarefas do shell e não move objetos do sistema de arquivos."}
::option[Continua sua execução como tarefa em segundo plano.]{#job-control-bg-continue .correct explanation="O shell retoma a tarefa interrompida selecionada sem atribuir a ela o primeiro plano do terminal."}
::option[Encerra-a com `SIGKILL`.]{#job-control-bg-kill explanation="O comando interno continua a tarefa, não a encerra."}
:::

## Movimentação de uma Tarefa para o Primeiro Plano

Use `fg` com uma especificação de tarefa para torná-la o grupo de processos em primeiro plano do terminal e aguardá-la:

```bash
$ fg %1
```

Sem um operando, `fg` normalmente seleciona a tarefa atual marcada com `+`. Uma tarefa interrompida é retomada ao entrar no primeiro plano.

:::single-choice{#job-control-fg-effect} O que `fg %1` faz?

::option[Atribui a tarefa 1 ao primeiro plano do terminal e aguarda por ela.]{#job-control-fg-foreground .correct explanation="O shell coloca a tarefa selecionada em primeiro plano para que ela possa interagir com o terminal."}
::option[Transforma a tarefa 1 no PID 1.]{#job-control-fg-pid-one explanation="Um ID de tarefa do shell não substitui nem reescreve IDs de processos."}
::option[Inicia uma segunda cópia da tarefa 1 em segundo plano.]{#job-control-fg-copy explanation="`fg` atua sobre a tarefa existente, em vez de criar uma duplicata."}
:::

## Envio de Sinais a uma Tarefa

Os shells permitem que `kill` aceite uma especificação de tarefa:

```bash
$ kill -TERM %1
```

Normalmente, isso sinaliza o grupo de processos da tarefa, não apenas um membro do pipeline. Inspecione primeiro a tarefa selecionada e use `SIGTERM` antes de considerar um escalonamento forçado. As especificações de tarefas são sintaxe do shell; scripts e ferramentas externas normalmente trabalham com PIDs ou IDs de grupos de processos verificados.

:::single-choice{#job-control-job-specification} Qual operando se refere à tarefa 1 do shell, em vez de ao processo com PID 1?

::option[`1`]{#job-control-plain-one explanation="Um operando numérico simples para `kill` normalmente é interpretado como um PID."}
::option[`#1`]{#job-control-hash-one explanation="Um prefixo de cerquilha não é a sintaxe apresentada para um ID de tarefa do shell."}
::option[`%1`]{#job-control-percent-one .correct explanation="O prefixo de porcentagem identifica uma especificação de tarefa do shell."}
:::

Pratique essas operações com comandos inofensivos, como `sleep`, no laboratório [Gerenciamento e Monitoramento de Processos Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864).

## Resumo

Agora você sabe mover tarefas deliberadamente entre estados controlados pelo shell.

1. Use `&` para iniciar uma tarefa em segundo plano sem desanexá-la automaticamente.
2. Use `jobs` para inspecionar a tabela de tarefas do shell atual.
3. Interrompa com `Ctrl-Z` e continue em segundo plano com `bg`.
4. Retorne uma tarefa selecionada ao terminal com `fg`.
5. Enderece tarefas do shell com `%JOB_ID` ao enviar sinais.
