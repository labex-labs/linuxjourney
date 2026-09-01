---
lesson_id: "upstart-jobs"
course_id: "init"
lang: "pt"
order_index: 4
title: "Tarefas do Upstart"
description: "Aprenda a inspecionar e controlar tarefas em um sistema legado Upstart confirmado com `initctl`."
meta_title: "Tarefas do Upstart - Init"
meta_description: "Um guia para gerenciar serviços por tarefas do Upstart em um ambiente Linux. Aprenda a usar initctl para listar, iniciar, interromper e reiniciar tarefas."
meta_keywords: "tarefas Upstart, initctl, Upstart Linux, serviços Linux, administração de sistemas, sistema init, tutorial Linux"
---

`initctl` se comunica com um daemon init Upstart em execução. Use-o somente depois de confirmar que o namespace de PIDs relevante realmente executa o Upstart; em um host atual com systemd, use as ferramentas nativas do systemd.

## Listagem e Leitura do Estado das Tarefas

Liste as tarefas e instâncias conhecidas:

```bash
$ initctl list
```

Inspecione uma tarefa:

```bash
$ initctl status networking
networking start/running
```

O Upstart informa tanto um **objetivo**, como `start` ou `stop`, quanto um **estado** atual, como `running` ou `waiting`. `stop/waiting` significa que a tarefa não está em execução e aguarda uma condição de início ou uma solicitação manual; isso não indica necessariamente um erro.

:::single-choice{#upstart-jobs-stop-waiting} O que `stop/waiting` normalmente significa na saída de estado do Upstart?

::option[A tarefa está em execução, mas não consome CPU.]{#upstart-jobs-running-idle explanation="Uma tarefa em execução normalmente mostraria um objetivo start e o estado running."}
::option[O objetivo da tarefa é permanecer parada, e nenhuma instância de processo está em execução.]{#upstart-jobs-stopped-waiting .correct explanation="A definição continua conhecida enquanto o Upstart aguarda uma condição ou comando futuro."}
::option[Todo o sistema operacional está aguardando o desligamento.]{#upstart-jobs-system-poweroff explanation="O par descreve essa instância da tarefa, não necessariamente o estado global do sistema."}
:::

## Início e Interrupção de uma Tarefa

Depois de revisar as dependências e o impacto:

```bash
$ sudo initctl start JOB_NAME
$ sudo initctl stop JOB_NAME
```

As tarefas podem definir várias instâncias identificadas por variáveis de ambiente. Nesse caso, forneça as variáveis exatas exigidas pela configuração e inclua-as de forma consistente ao consultar ou interromper uma instância. Iniciar tarefas de rede, armazenamento, autenticação ou acesso remoto pode prejudicar a sessão, portanto preserve o acesso de recuperação pelo console.

:::single-choice{#upstart-jobs-start-command} Qual comando solicita manualmente que a tarefa `peanuts` seja iniciada?

::option[`sudo initctl start peanuts`]{#upstart-jobs-start-peanuts .correct explanation="O subcomando start é seguido pelo nome configurado da tarefa e por eventuais variáveis de instância necessárias."}
::option[`sudo initctl peanuts start`]{#upstart-jobs-name-first explanation="A sintaxe de initctl coloca o subcomando antes do nome da tarefa."}
::option[`sudo systemctl initctl peanuts`]{#upstart-jobs-systemctl-mixed explanation="Esse comando mistura incorretamente duas interfaces distintas de gerenciadores de serviços."}
:::

## Reinicialização e Alterações de Configuração

Solicite a reinicialização de uma tarefa já em execução com:

```bash
$ sudo initctl restart peanuts
```

No Upstart, `restart` nem sempre equivale a uma nova sequência de `stop` e `start` após a edição de um arquivo de tarefa: a configuração existente da tarefa em execução pode continuar sendo a autoridade. Valide o `.conf` alterado, peça ao Upstart que recarregue a configuração conforme a versão instalada e siga o procedimento documentado de parada/início quando a nova configuração precisar entrar em vigor.

Uma reinicialização causa interrupção e pode não devolver o serviço à operação. Verifique depois o endpoint real e os logs.

:::single-choice{#upstart-jobs-restart-peanuts} Qual comando solicita a reinicialização da tarefa Upstart `peanuts` em execução?

::option[`sudo initctl restart peanuts`]{#upstart-jobs-restart-command .correct explanation="O subcomando restart atua sobre a tarefa nomeada pela interface de controle do Upstart."}
::option[`sudo initctl emit peanuts`]{#upstart-jobs-emit-not-restart explanation="A emissão de um evento afeta todas as condições de tarefas correspondentes e não é uma solicitação direta de reinicialização."}
::option[`sudo service --status-all peanuts`]{#upstart-jobs-status-all explanation="Uma listagem de estados não solicita uma reinicialização."}
:::

## Validação da Configuração da Tarefa

Antes de instalar um arquivo de tarefa modificado, use a ferramenta de validação fornecida pela distribuição legada, normalmente `init-checkconf`, e revise os scripts incluídos, o ambiente, as configurações de usuário/grupo, a política de respawn e as expressões de eventos. Depois, recarregue as definições com o fluxo de `initctl reload-configuration` apropriado à versão.

A validação da sintaxe não comprova que os caminhos existam, as credenciais permitam a execução, os eventos ocorram ou o processo fique pronto. Teste em um ambiente com capacidade de recuperação.

:::single-choice{#upstart-jobs-syntax-validation-limit} O que a validação da sintaxe da tarefa não comprova?

::option[Que o serviço será iniciado com sucesso e ficará pronto.]{#upstart-jobs-runtime-not-proven .correct explanation="Os caminhos, as permissões, as dependências e o fluxo de eventos em tempo de execução exigem um teste controlado real."}
::option[Que o texto da configuração pode ser interpretado.]{#upstart-jobs-parse-purpose explanation="A interpretação é justamente a principal finalidade da validação da sintaxe."}
::option[Que um arquivo foi fornecido ao validador.]{#upstart-jobs-file-supplied explanation="A ferramenta pode informar imediatamente a ausência da entrada."}
:::

## Emissão Cuidadosa de Eventos

O Upstart pode emitir um evento nomeado:

```bash
$ sudo initctl emit EVENT_NAME
```

Todas as tarefas cujas expressões de início ou parada correspondam podem reagir. Um evento não é endereçado a uma única tarefa, e seus efeitos podem se propagar por outros eventos. Inspecione todas as configurações correspondentes antes de emitir um evento personalizado ou do sistema; não repita casualmente eventos essenciais de boot em um host de produção.

:::single-choice{#upstart-jobs-emit-scope} O que pode acontecer quando `initctl emit EVENT_NAME` é executado?

::option[Todas as expressões de tarefas correspondentes ao evento podem realizar transições.]{#upstart-jobs-event-matches .correct explanation="Os eventos são transmitidos ao modelo de dependências do Upstart, não enviados somente a um serviço nomeado."}
::option[Somente uma tarefa cujo nome seja exatamente igual ao evento pode responder.]{#upstart-jobs-event-name-only explanation="A correspondência é definida pelas expressões `start on` e `stop on`, não pela igualdade do nome da tarefa."}
::option[O evento fica armazenado para sempre como uma mensagem em uma fila persistente.]{#upstart-jobs-event-durable explanation="Os eventos do Upstart são notificações do ciclo de vida, não uma fila geral e persistente de mensagens."}
:::

## Resumo

Agora você sabe operar tarefas do Upstart com escopo explícito de estados e eventos.

1. Leia separadamente o objetivo e o estado na saída de `initctl`.
2. Inicie e interrompa a instância exata da tarefa após revisar o impacto.
3. Trate a reinicialização e a alteração da configuração da tarefa como questões distintas.
4. Valide a sintaxe e depois teste a prontidão em tempo de execução.
5. Inspecione todas as correspondências antes de emitir um evento.
