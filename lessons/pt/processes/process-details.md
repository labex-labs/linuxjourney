---
lesson_id: "process-details"
course_id: "processes"
lang: "pt"
order_index: 3
title: "Detalhes dos Processos"
description: "Aprenda quais estados e recursos diferenciam um processo em execução de um programa armazenado no disco."
meta_title: "Detalhes dos Processos - Processos"
meta_description: "Conheça os fundamentos dos processos Linux. Este guia explica o que é um processo, como o kernel gerencia processos e como aloca recursos do sistema, como CPU e memória."
meta_keywords: "processo Linux, detalhes de processos, kernel, gerenciamento de processos, recursos do sistema, ps aux, CPU, memória, tutorial Linux, guia para iniciantes"
---

Um programa é formado por código executável e dados armazenados em um arquivo. Um processo é um contexto ativo de execução: ele inclui código mapeado, memória, credenciais, descritores de arquivos abertos, estado dos sinais, informações de escalonamento e uma ou mais threads. O mesmo programa pode ter várias instâncias de processos independentes.

## Instâncias de Programas e PIDs

Por exemplo, inicie `cat` sem operandos em dois terminais. Cada instância aguarda uma entrada e possui seu próprio ID de processo:

```bash
$ pgrep -a cat
18420 cat
18457 cat
```

Os dois processos executam o mesmo programa, mas podem ter fluxos de entrada, conteúdos de memória, credenciais, diretórios de trabalho e durações diferentes. Um PID identifica um processo ativo por vez e pode ser reutilizado mais tarde, depois que esse processo termina.

:::single-choice{#process-details-program-versus-process} O que diferencia duas instâncias em execução do mesmo programa?

::option[O arquivo executável precisa ser copiado uma vez para cada instância.]{#process-details-copied-executable explanation="Vários processos podem mapear e compartilhar as páginas de código do mesmo arquivo executável sem duplicar o arquivo."}
::option[Somente uma instância pode possuir memória ou arquivos abertos.]{#process-details-one-instance-resources explanation="Cada processo pode ter seus próprios mapeamentos de memória e sua própria tabela de descritores de arquivos."}
::option[Cada instância possui seu próprio contexto de processo e PID.]{#process-details-independent-context .correct explanation="Execuções separadas recebem estados ativos distintos, mesmo quando seu código executável vem do mesmo arquivo."}
:::

## Estado Acompanhado pelo Kernel

O kernel mantém as informações necessárias para escalonar e controlar cada processo, incluindo:

- identificadores do processo e de seu pai
- credenciais de usuário e grupo
- mapeamentos de memória virtual
- descritores de arquivos abertos e diretório atual
- disposições de sinais e sinais pendentes
- política de escalonamento, prioridade e estado de execução
- dados de contabilização, como tempo de CPU

Alguns recursos subjacentes podem ser compartilhados. Processos relacionados podem compartilhar memória mapeada, e as threads de um mesmo processo compartilham um espaço de endereços e muitos recursos do processo. Portanto, um processo oferece limites de isolamento sem implicar que cada byte ou objeto do kernel seja fisicamente privado.

:::single-choice{#process-details-kernel-state} Qual componente mantém os estados de escalonamento e credenciais dos processos Linux?

::option[O kernel.]{#process-details-kernel .correct explanation="O kernel acompanha o estado dos processos e aplica regras de escalonamento, memória, sinais e controle de acesso."}
::option[O diretório do arquivo executável.]{#process-details-directory explanation="Um diretório armazena um mapeamento de nomes para inodes e não escalona processos em execução."}
::option[Somente o emulador de terminal do usuário.]{#process-details-terminal explanation="Um terminal pode interagir com processos, mas seu gerenciamento continua sendo responsabilidade do kernel."}
:::

## Escalonamento da CPU e Memória

As threads executáveis disputam tempo de CPU. O escalonador do kernel escolhe qual thread será executada em qual CPU de acordo com a classe de escalonamento, a prioridade, a afinidade de CPU, a carga e a política. Isso não é uma promessa de que todos os processos receberão uma parcela igual.

Cada processo normalmente enxerga um espaço de endereços virtual. O kernel e o hardware mapeiam endereços virtuais para a memória física ou outro armazenamento de apoio, aplicam proteções e podem compartilhar páginas quando apropriado. Portanto, um valor de memória em `ps` ou `top` não é automaticamente a quantidade de RAM física exclusiva atribuída àquele processo.

:::single-choice{#process-details-scheduler-role} O que o escalonador do Linux seleciona?

::option[Qual thread executável será executada em uma CPU disponível.]{#process-details-runnable-thread .correct explanation="A política de escalonamento escolhe entre contextos executáveis e atribui tempo de CPU."}
::option[Qual proprietário de arquivo é registrado quando um disco é formatado.]{#process-details-format-owner explanation="A propriedade do sistema de arquivos não tem relação com o escalonamento da CPU."}
::option[Qual linha de comando um usuário pode digitar.]{#process-details-command-entry explanation="O escalonador gerencia o tempo de execução, não a sintaxe dos comandos interativos."}
:::

## Encerramento do Processo e Liberação de Recursos

Quando um processo termina, o kernel libera a maioria de seus recursos privados, fecha os descritores restantes e registra informações de encerramento para o processo pai. Um pequeno registro na tabela de processos pode permanecer como zumbi até que o pai recupere o status de saída. Isso significa que “o processo terminou a execução” e “todos os vestígios desapareceram da tabela de processos” nem sempre ocorrem simultaneamente.

:::single-choice{#process-details-exit-status} Por que um processo encerrado pode permanecer brevemente como zumbi?

::option[Ele ainda está executando instruções com toda a memória alocada.]{#process-details-zombie-running explanation="Um zumbi terminou a execução e não mantém mais um espaço de endereços em funcionamento normal."}
::option[Seu pai ainda não coletou o status de encerramento registrado.]{#process-details-parent-wait .correct explanation="O kernel mantém informações mínimas de saída até que o pai realize uma operação wait."}
::option[Seu arquivo executável fica permanentemente bloqueado pelo kernel.]{#process-details-zombie-file-lock explanation="O estado zumbi diz respeito à contabilização do encerramento entre pai e filho, não ao bloqueio permanente do executável."}
:::

Use o laboratório [Gerenciamento e Monitoramento de Processos Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) para iniciar várias instâncias e comparar seus PIDs e estados. O laboratório [Comando `top` do Linux](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500) oferece uma visualização dinâmica das métricas de escalonamento e recursos.

## Resumo

Agora você sabe descrever um processo como algo além de um arquivo de programa.

1. Diferencie o código executável armazenado de uma instância ativa de processo.
2. Identifique os estados e recursos acompanhados pelo kernel.
3. Relacione o escalonamento às threads executáveis, não a parcelas iguais.
4. Reconheça que o status de saída pode permanecer até que o pai o colete.
