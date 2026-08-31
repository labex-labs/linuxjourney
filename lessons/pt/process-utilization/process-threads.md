---
lesson_id: "process-threads"
course_id: "process-utilization"
lang: "pt"
order_index: 3
title: "Threads de Processos"
description: "Aprenda como as threads Linux compartilham recursos de processos e como inspecioná-las com ps."
meta_title: "Threads de Processos - Utilização de Processos"
meta_description: "Um guia sobre threads de processos Linux. Aprenda a diferença entre processos de uma ou várias threads e como usar o comando ps para mostrá-las."
meta_keywords: "threads Linux, threads de processos, ps mostrar threads, ps m, multithread, single-thread, processo leve, gerenciamento de processos Linux"
---

Uma thread é um fluxo de execução escalonado dentro de um processo. Todo processo em execução possui pelo menos uma thread, e um processo multithread possui vários fluxos capazes de progredir simultaneamente.

## Processos e Threads

As threads de um mesmo processo compartilham recursos como o espaço de endereços virtual e os descritores de arquivos abertos. Cada thread ainda possui seu próprio estado de execução, incluindo registradores e uma pilha. O compartilhamento torna a comunicação eficiente, mas também significa que uma alteração não sincronizada por uma thread pode afetar as outras.

Processos separados normalmente possuem espaços de endereços distintos e se comunicam por mecanismos explícitos entre processos. Nenhum dos projetos é automaticamente mais rápido ou seguro; a carga de trabalho e a implementação determinam as compensações.

:::single-choice{#threads-shared-resource}
Qual recurso normalmente é compartilhado pelas threads de um mesmo processo?

::option[O espaço de endereços virtual do processo.]{#threads-shared-address-space .correct explanation="As threads podem acessar a mesma memória do processo, sujeitas à sincronização do programa."}
::option[Uma instalação separada do kernel para cada thread.]{#threads-separate-kernel explanation="Todas as threads usam o kernel do sistema em execução."}
::option[Uma raiz diferente do sistema de arquivos para cada thread.]{#threads-different-root explanation="As threads normalmente compartilham o contexto do sistema de arquivos do processo, em vez de receber raízes separadas."}
:::

## Identificadores de Threads

O Linux representa cada thread como uma tarefa escalonável com seu próprio ID de thread. O ID do líder do grupo de threads normalmente é apresentado como o ID do processo, enquanto todos os membros compartilham um ID de grupo de threads. As ferramentas usam rótulos como `PID`, `TID`, `LWP` e `SPID`; verifique as definições dos campos da ferramenta, em vez de presumir que todos os rótulos signifiquem a mesma coisa.

:::single-choice{#threads-own-scheduling-state}
O que cada thread mantém independentemente?

::option[A tabela completa de arquivos abertos do processo.]{#threads-open-files-shared explanation="As threads de um processo normalmente compartilham os descritores de arquivos abertos."}
::option[O banco de dados de usuários de todo o sistema.]{#threads-user-database explanation="Os bancos de dados de contas não são estados privados das threads."}
::option[Seu estado de execução e sua pilha.]{#threads-stack-state .correct explanation="Uma thread precisa de seu próprio contexto de execução, embora os recursos do processo sejam compartilhados."}
:::

## Listagem de Threads com ps

Use campos explícitos de saída para evitar layouts padrão ambíguos:

```bash
$ ps -eLo pid,tid,psr,stat,comm
```

No `ps` do procps, `-L` mostra as threads, e `-e` seleciona todos os processos. `pid` identifica o grupo de threads, `tid` identifica uma thread individual, `psr` mostra a CPU em que ela foi executada pela última vez e `stat` informa o estado. Para inspecionar um processo:

```bash
$ ps -L -p 1234 -o pid,tid,stat,pcpu,comm
```

As listagens de threads são snapshots. Uma thread pode terminar ou mudar de estado imediatamente depois.

:::single-choice{#threads-ps-one-process}
Qual comando lista as threads pertencentes ao PID 1234 com campos explícitos?

::option[`ps -p 1234 -o pid,ppid,stat,pcpu,comm`]{#threads-process-only explanation="Essa saída não solicita linhas por thread."}
::option[`ps -L -p 1234 -o pid,tid,stat,pcpu,comm`]{#threads-ps-l .correct explanation="A opção `-L` solicita linhas de threads para o processo selecionado."}
::option[`ps -e -o pid,user,stat,pcpu,comm`]{#threads-all-processes explanation="Esse comando seleciona processos de todo o sistema sem IDs de threads."}
:::

## Interpretação da Atividade das Threads

O uso elevado de CPU em uma thread pode ficar oculto por uma média de todo o processo. Combine amostras de CPU no nível das threads com logs da aplicação, rastreamentos de pilha e ferramentas de profiling. Não anexe depuradores nem envie sinais a tarefas de produção sem compreender os impactos sobre pausas, permissões e serviços.

:::single-choice{#threads-snapshot-limit}
Por que uma listagem de threads de `ps` não deve ser tratada como estado permanente?

::option[`ps` cria uma thread substituta para cada linha.]{#threads-ps-creates explanation="O comando observa as tarefas; ele não clona cada uma que lista."}
::option[Os IDs de threads são idênticos em todos os hosts Linux.]{#threads-identical-ids explanation="Os identificadores são atribuídos dentro de um sistema em execução e não são universais."}
::option[As threads podem mudar de estado ou terminar depois do snapshot.]{#threads-change-after-snapshot .correct explanation="A inspeção dos processos observa um momento de um sistema em constante mudança."}
:::

## Resumo

Agora você sabe diferenciar os recursos do processo do estado de execução de cada thread.

1. Reconheça que todo processo possui pelo menos uma thread.
2. Identifique os recursos compartilhados pelas threads de um processo.
3. Liste IDs explícitos de processos e threads com `ps -L`.
4. Trate a saída das threads como um snapshot e relacione-a a outras evidências.
