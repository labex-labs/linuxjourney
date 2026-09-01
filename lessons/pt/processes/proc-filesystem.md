---
lesson_id: "proc-filesystem"
course_id: "processes"
lang: "pt"
order_index: 10
title: "Sistema de Arquivos /proc"
description: "Aprenda como o Linux expõe informações ativas de processos e do kernel por meio do sistema de arquivos virtual `/proc`."
meta_title: "Sistema de Arquivos /proc - Processos"
meta_description: "Conheça o sistema de arquivos /proc do Linux, um diretório virtual que oferece uma visão do kernel e dos processos em execução. Aprenda a acessar detalhes adicionais dos processos."
meta_keywords: "sistema de arquivos /proc, proc Linux, informações de processos, detalhes proc Linux, painel do sistema, processos Linux, informações do kernel"
---

O Linux normalmente monta `procfs` em `/proc`. Esse sistema de arquivos virtual apresenta interfaces geradas pelo kernel como arquivos e diretórios; seu conteúdo não é formado por arquivos persistentes comuns armazenados no disco. Ele expõe o estado dos processos e determinadas informações do kernel para todo o sistema.

## Localização dos Diretórios de Processos

Liste a montagem e as entradas do nível superior com:

```bash
$ findmnt /proc
$ ls /proc
```

Os nomes numéricos dos diretórios correspondem aos IDs de processos visíveis no namespace de PIDs do solicitante. Por exemplo, `/proc/12345` representa o PID 12345 no instante em que ele existe. `/proc/self` é um link simbólico que aponta para o diretório do próprio processo observador, e `/proc/thread-self` identifica a thread atual.

A visibilidade e o acesso dependem das credenciais, dos namespaces, da política de segurança e das opções de montagem do procfs, como `hidepid`. Um processo pode terminar entre a listagem de um diretório e a abertura de um de seus arquivos, portanto o desaparecimento é uma condição de corrida normal que as ferramentas de inspeção precisam tratar.

:::single-choice{#proc-filesystem-numeric-directory} O que o diretório numérico `/proc/12345` normalmente representa?

::option[O bloco de disco de número 12345.]{#proc-filesystem-disk-block explanation="`/proc` é uma interface virtual do kernel, não um diretório de blocos brutos do disco."}
::option[O processo atualmente visível com o PID 12345.]{#proc-filesystem-pid-directory .correct explanation="Os dados por processo do procfs são agrupados em um diretório nomeado pelo PID visível."}
::option[A conta de usuário cujo UID é 12345.]{#proc-filesystem-user-directory explanation="Os diretórios numéricos de processos no nível superior são identificados pelo PID, não pelo UID."}
:::

## Leitura das Informações de Processos

Inspecione o arquivo de estado de um processo quando as permissões permitirem:

```bash
$ less /proc/12345/status
```

Ele inclui campos como nome do processo, estado, IDs, credenciais, contadores de memória, capacidades e máscaras de sinais. Outras entradas úteis são:

- `/proc/12345/cmdline`: argumentos da linha de comando separados por bytes nulos
- `/proc/12345/environ`: entradas do ambiente, com controle de acesso e potencialmente confidenciais
- `/proc/12345/fd/`: links simbólicos que representam descritores de arquivos abertos
- `/proc/12345/maps`: mapeamentos atuais de memória
- `/proc/12345/cwd`: link simbólico para o diretório de trabalho atual

Trate essas informações como observações mutáveis. Os campos podem variar conforme a versão do kernel, um processo pode mudar de estado durante a leitura de vários arquivos, e alguns contadores possuem detalhes que seus nomes, sozinhos, não revelam.

:::single-choice{#proc-filesystem-status-file} Qual caminho contém um resumo legível organizado em campos para o PID 12345?

::option[`/proc/status/12345`]{#proc-filesystem-status-reversed explanation="Os arquivos de cada processo ficam dentro do diretório nomeado pelo PID, não em um diretório `status` do nível superior."}
::option[`/proc/12345/status`]{#proc-filesystem-process-status .correct explanation="A interface `status` do processo apresenta identificadores, estado, memória, sinais e campos de credenciais."}
::option[`/proc/cpuinfo/12345`]{#proc-filesystem-cpuinfo-pid explanation="`/proc/cpuinfo` é uma interface de todo o sistema, não um diretório de arquivos de estado por PID."}
:::

## Leitura de Interfaces de Todo o Sistema

Nem toda entrada de `/proc` pertence a um processo. Alguns exemplos são:

- `/proc/cpuinfo` para informações de CPU fornecidas pelo kernel
- `/proc/meminfo` para contadores de memória do sistema
- `/proc/mounts` para a visão das montagens do processo atual
- `/proc/loadavg` para informações de carga média e tarefas executáveis
- `/proc/sys/` para parâmetros do kernel em tempo de execução

Alguns arquivos, especialmente em `/proc/sys`, são interfaces de configuração graváveis. Não grave neles apenas porque parecem arquivos comuns. Compreenda o parâmetro, o escopo, o mecanismo de persistência e a reversão antes de realizar uma alteração autorizada no sistema.

:::single-choice{#proc-filesystem-system-interface} Qual entrada fornece contadores de memória de todo o sistema, não o estado de um único processo?

::option[`/proc/self/status`]{#proc-filesystem-self-status explanation="Esse caminho aponta para o estado do próprio processo observador."}
::option[`/proc/meminfo`]{#proc-filesystem-memory-info .correct explanation="`meminfo` contém estatísticas da memória do sistema fornecidas pelo kernel."}
::option[`/proc/1/fd`]{#proc-filesystem-one-fd explanation="Esse diretório representa os descritores de arquivos pertencentes ao PID 1, sujeito aos controles de acesso."}
:::

## Uso de `/proc` por Meio de Ferramentas

As implementações Linux de ferramentas como `ps`, `top` e `free` obtêm grande parte de seus dados do procfs e de outras interfaces do kernel e então os rotulam, calculam e formatam. Prefira essas ferramentas no trabalho comum quando elas fornecerem o campo necessário; leia `/proc` diretamente para detalhes específicos ou scripts somente depois de estudar a documentação da interface.

Leitores diretos precisam interpretar os formatos corretamente, tolerar processos ausentes, proteger saídas confidenciais e evitar presumir que uma leitura seja um snapshot atômico do sistema.

:::single-choice{#proc-filesystem-live-data} Por que `/proc/PID` pode desaparecer entre dois comandos de inspeção?

::option[Todo arquivo do procfs é renomeado automaticamente uma vez por segundo.]{#proc-filesystem-renamed explanation="Não existe uma regra de renomeação periódica para todas as entradas do procfs."}
::option[A leitura de `status` exclui o diretório do processo.]{#proc-filesystem-read-delete explanation="A inspeção do status é somente para leitura e não encerra nem remove o processo."}
::option[O processo pode terminar enquanto está sendo observado.]{#proc-filesystem-process-exit .correct explanation="O procfs reflete o estado ativo, portanto o kernel remove o diretório de um processo depois que ele deixa de existir."}
:::

## Resumo

Agora você sabe usar o procfs como uma interface ativa e controlada por acesso do kernel.

1. Associe os diretórios numéricos de `/proc` aos PIDs visíveis.
2. Leia arquivos selecionados de processos considerando condições de corrida e confidencialidade.
3. Diferencie diretórios de processos de interfaces de todo o sistema.
4. Prefira ferramentas e formatos documentados para uma inspeção rotineira confiável.
