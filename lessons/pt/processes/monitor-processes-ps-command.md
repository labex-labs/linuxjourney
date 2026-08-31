---
lesson_id: "monitor-processes-ps-command"
course_id: "processes"
lang: "pt"
order_index: 1
title: "ps (Processos)"
description: "Aprenda a obter snapshots de processos com `ps` e monitorar atividades em mudança com `top`."
meta_title: "ps (Processos) - Processos"
meta_description: "Conheça o comando ps do Linux. Aprenda a usar ps -ef e outras opções para visualizar processos em execução, entender PIDs e gerenciar tarefas do sistema."
meta_keywords: "comando ps, ps -ef Linux, comando ps -ef, Linux ps -ef, ps -e Linux, processos Linux, ID de processo, PID, comando top, Linux Journey"
---

Um processo é uma instância em execução de um programa, junto com sua memória, suas credenciais, seus recursos abertos e seu estado de execução. O Linux identifica cada processo ativo com um ID numérico de processo, ou PID. Um PID é exclusivo entre os processos existentes ao mesmo tempo, mas o kernel pode reutilizá-lo depois que um processo termina.

## Obtenção de um Snapshot Básico

Execute `ps` sem opções para ver um snapshot selecionado pelos padrões da implementação, normalmente os processos associados ao seu terminal e usuário atuais:

```text
$ ps
    PID TTY          TIME CMD
  41230 pts/4    00:00:00 bash
  51224 pts/4    00:00:00 ps
```

Os campos comuns incluem:

- `PID`: ID do processo
- `TTY`: terminal de controle, ou `?` quando nenhum está associado
- `TIME`: tempo de CPU acumulado, não a duração decorrida no relógio
- `CMD`: nome ou linha de comando, conforme o formato selecionado

As colunas exatas e os padrões de seleção variam entre implementações de `ps` e ambientes.

:::single-choice{#ps-command-pid-meaning}
O que a coluna `PID` identifica?

::option[O número do diretório atual do processo.]{#ps-command-pid-directory explanation="Um diretório atual é uma referência do sistema de arquivos e não é representado pelo PID."}
::option[O tempo de CPU acumulado em segundos.]{#ps-command-pid-cpu explanation="O uso da CPU é mostrado em um campo separado, como `TIME`."}
::option[O ID de processo atribuído pelo kernel.]{#ps-command-pid-kernel .correct explanation="PID é o identificador numérico usado para se referir a um processo ativo."}
:::

## Listagem de Processos com Opções no Estilo BSD

O `ps` do Linux aceita vários estilos de opções. As opções no estilo BSD normalmente são escritas sem um hífen inicial:

```bash
$ ps aux
```

Nessa combinação:

- `a` amplia a seleção para processos de outros usuários que possuem terminais.
- `x` também inclui processos sem terminais de controle e amplia a seleção quando combinado com `a`.
- `u` seleciona um formato de saída voltado ao usuário, com campos como `USER`, `%CPU`, `%MEM`, `VSZ` e `RSS`.

Como os significados das opções podem interagir, interprete a combinação completa em vez de tratar cada letra como um comando independente.

:::single-choice{#ps-command-aux-user-format}
Em `ps aux`, qual opção solicita o formato de saída voltado ao usuário?

::option[`u`]{#ps-command-aux-u .correct explanation="A opção `u` no estilo BSD seleciona um conjunto de colunas voltado ao usuário."}
::option[`x`]{#ps-command-aux-x explanation="A opção `x` afeta a seleção dos processos, especialmente os que não possuem terminais de controle."}
::option[`a`]{#ps-command-aux-a explanation="A opção `a` amplia a seleção para além dos processos do usuário atual associados a terminais."}
:::

## Uso de Opções no Estilo Padrão

O comando amplamente usado `ps -ef`, no estilo padrão, escreve as opções com um hífen inicial:

```bash
$ ps -ef
```

- `-e` seleciona todos os processos visíveis ao solicitante.
- `-f` solicita uma listagem em formato completo.

A saída normalmente inclui `UID`, `PID`, `PPID`, horário de início e informações do comando. `PPID` é o ID do processo pai. Essa listagem não é inerentemente hierárquica; use uma opção como `--forest` quando disponível ou um visualizador de árvores dedicado, como `pstree`, quando a disposição entre pais e filhos for importante.

:::single-choice{#ps-command-ef-selection}
O que `-e` solicita em `ps -ef`?

::option[Uma atualização a cada segundo até ser interrompida.]{#ps-command-e-refresh explanation="`ps` produz um snapshot; a atualização contínua é um recurso de ferramentas como `top`."}
::option[Uma seleção que contém todos os processos visíveis ao solicitante.]{#ps-command-e-every .correct explanation="A opção `-e` no estilo padrão amplia o snapshot para todos os processos selecionáveis."}
::option[Somente processos cujo comando terminou com erro.]{#ps-command-e-errors explanation="A seleção dos processos não se baseia no futuro status de saída de um comando."}
:::

## Monitoramento da Atividade ao Longo do Tempo

`ps` termina depois de produzir um snapshot. Use `top` para obter uma visualização interativa atualizada periodicamente:

```bash
$ top
```

`top` ajuda a identificar consumidores variáveis de CPU e memória, mas seus valores são amostras e podem oscilar. Confirme um possível problema em várias observações e relacione as porcentagens à quantidade de CPUs da máquina, à contabilidade de memória e à carga de trabalho.

:::single-choice{#ps-command-snapshot-versus-top}
Qual ferramenta apresentada aqui atualiza sua exibição de processos periodicamente por padrão?

::option[`top`]{#ps-command-top-refresh .correct explanation="`top` é um monitor interativo que atualiza sua exibição em intervalos."}
::option[`ps -ef`]{#ps-command-ps-ef-snapshot explanation="Esse comando imprime um snapshot de processos em formato completo e termina."}
::option[`ls -l`]{#ps-command-ls-files explanation="`ls -l` exibe entradas do sistema de arquivos, não um monitor ativo de processos."}
:::

Para praticar, use o laboratório [Gerenciamento e Monitoramento de Processos Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) para comparar snapshots com um monitor interativo ou explore a ordenação e filtragem no laboratório [Comando `top` do Linux](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500).

## Resumo

Agora você sabe escolher uma visualização de processos e interpretar seus identificadores básicos.

1. Trate um PID como um identificador reutilizável de um processo atualmente ativo.
2. Use `ps` sem opções para um pequeno snapshot padrão.
3. Use `ps aux` ou `ps -ef` para seleções mais amplas e colunas mais detalhadas.
4. Use `top` quando as alterações ao longo do tempo forem importantes.
