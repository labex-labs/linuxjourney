---
lesson_id: "upstart-overview"
course_id: "init"
lang: "pt"
order_index: 3
title: "Visão Geral do Upstart"
description: "Aprenda como o sistema init legado Upstart conecta expressões de eventos aos objetivos do ciclo de vida das tarefas."
meta_title: "Visão Geral do Upstart - Init"
meta_description: "Conheça o Upstart, seu modelo orientado a eventos e como ele gerencia serviços no Linux. Entenda as configurações de tarefas Upstart e sua função como sistema init."
meta_keywords: "Upstart, sistema init, serviços Linux, Ubuntu, SysV, tutorial para iniciantes, guia Linux"
---

O Upstart é um sistema legado de init e gerenciamento de serviços baseado em eventos, desenvolvido pela Canonical. Versões antigas do Ubuntu e várias outras distribuições o utilizaram, mas as versões atuais do Ubuntu usam systemd. Estude o Upstart ao manter um host legado confirmado, não como uma suposição padrão para uma instalação moderna.

## Confirmação de um Host Upstart Legado

Inspecione o PID 1 e a interface de controle ativa:

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
$ initctl version
```

O último comando só retorna informações significativas quando o serviço de controle e o cliente do Upstart estão presentes. Um diretório como `/usr/share/upstart` ou arquivos restantes em `/etc/init` são evidências fracas, pois pacotes e vestígios de migrações podem permanecer depois que outro sistema init assume o controle.

:::single-choice{#upstart-overview-active-evidence} Qual é a evidência mais forte de que um host realmente usa o Upstart?

::option[O nome de um diretório contém a palavra `upstart`.]{#upstart-overview-directory-only explanation="Documentação instalada ou vestígios podem permanecer em um sistema que usa outro init."}
::option[O sistema possui pelo menos um script de shell.]{#upstart-overview-shell-script explanation="Scripts de shell são comuns a todos os ambientes init."}
::option[O PID 1 e a interface `initctl` ativa identificam o Upstart.]{#upstart-overview-live-interface .correct explanation="As evidências do processo e do controle em tempo de execução são mais fortes que a existência de arquivos legados."}
:::

## Tarefas e Eventos

Uma **tarefa** do Upstart descreve um serviço ou trabalho, incluindo os comandos de seu processo e as condições do ciclo de vida. Um **evento** é uma notificação nomeada com variáveis de ambiente opcionais. A configuração da tarefa pode expressar quando seu objetivo deve se tornar iniciar ou interromper.

Os arquivos de tarefas do sistema normalmente ficam em `/etc/init/` com o sufixo `.conf`. Por exemplo:

```text
description "Example worker"
start on runlevel [2345]
stop on runlevel [016]
exec /usr/local/sbin/example-worker
```

Isso usa eventos de runlevels como entradas de compatibilidade. O Upstart também pode reagir a eventos do sistema de arquivos, dispositivos, rede ou definidos por aplicações, dependendo do que o sistema emite.

:::single-choice{#upstart-overview-start-on} O que uma seção `start on` do Upstart define?

::option[A versão do kernel que deve ser compilada em seguida.]{#upstart-overview-kernel-version explanation="As condições de eventos das tarefas não selecionam uma compilação do kernel."}
::option[A expressão de eventos que muda o objetivo da tarefa para a inicialização.]{#upstart-overview-start-condition .correct explanation="Quando a expressão é satisfeita, o Upstart tenta realizar a transição de início configurada para a tarefa."}
::option[A partição de disco onde todas as tarefas armazenam dados.]{#upstart-overview-partition explanation="O local do armazenamento não tem relação com a sintaxe de eventos do Upstart."}
:::

## Inicialização Orientada a Eventos

Durante a inicialização, o Upstart carrega as definições das tarefas e recebe eventos. As expressões `start on` ou `stop on` correspondentes atualizam os objetivos das tarefas; as transições podem emitir eventos adicionais que liberam outros trabalhos. Tarefas independentes podem progredir simultaneamente.

Esse modelo evita uma única sequência global de scripts codificada, mas pode ser difícil de diagnosticar quando os nomes dos eventos, a ordem e as condições são implícitos. Os eventos não são, por padrão, uma fila persistente de mensagens, portanto uma tarefa adicionada ou uma condição alterada posteriormente não deve presumir que todos os eventos anteriores serão repetidos.

:::single-choice{#upstart-overview-event-chain} Como uma tarefa do Upstart pode levar outra tarefa a iniciar?

::option[Ela reescreve na memória o binário executável da outra tarefa.]{#upstart-overview-rewrite-binary explanation="A coordenação ocorre por eventos, não por alteração do código."}
::option[Todas as tarefas sempre iniciam estritamente na ordem dos nomes dos arquivos.]{#upstart-overview-filename-order explanation="O Upstart usa expressões de eventos, não uma única lista de inicialização ordenada por nomes de arquivos."}
::option[Sua transição pode emitir um evento que corresponde à outra tarefa.]{#upstart-overview-emitted-event .correct explanation="As expressões de eventos conectam as transições dos ciclos de vida de tarefas que seriam independentes."}
:::

## Migração e Compatibilidade

O systemd pode oferecer compatibilidade limitada com alguns scripts de serviços legados, mas não executa a sintaxe das tarefas do Upstart como unidades nativas do systemd. Ao migrar, traduza as condições do ciclo de vida, o ambiente, a política de respawn, o registro, as dependências e as semânticas de prontidão, em vez de renomear arquivos mecanicamente.

:::single-choice{#upstart-overview-current-ubuntu} Qual sistema init é usado pelas versões padrão atuais do Ubuntu?

::option[Upstart exclusivamente em todas as instalações.]{#upstart-overview-current-upstart explanation="Isso só foi verdade em períodos e configurações de versões históricas."}
::option[systemd.]{#upstart-overview-current-systemd .correct explanation="O Upstart pertence a gerações antigas do Ubuntu; as versões atuais usam systemd como PID 1."}
::option[Nenhum processo init.]{#upstart-overview-no-init explanation="Um sistema Ubuntu completo ainda precisa de um gerenciador de serviços como PID 1."}
:::

## Resumo

Agora você sabe interpretar o Upstart como um modelo legado de eventos e tarefas.

1. Confirme o PID 1 ativo e a interface de controle.
2. Diferencie definições de tarefas de notificações de eventos.
3. Interprete `start on` e `stop on` como expressões do ciclo de vida.
4. Migre as semânticas explicitamente, em vez de renomear arquivos de configuração.
