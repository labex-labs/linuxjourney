---
index: 6
lang: "pt"
title: "Monitoramento de Memória"
meta_title: "Monitoramento de Memória - Utilização de Processos"
meta_description: "Domine o monitoramento de memória do Linux com o comando vmstat. Este guia explica como usar este poderoso monitor de utilização de memória para analisar métricas de desempenho do sistema."
meta_keywords: "monitoramento de memória, monitor de utilização de memória, vmstat, memória linux, desempenho do sistema, uso de memória, tutorial linux"
---

## Lesson Content

A administração eficaz do sistema exige que se monitore de perto o uso de recursos, e o **monitoramento de memória** é uma parte crítica desse processo. Quando um sistema fica com pouca memória, seu desempenho pode se degradar significativamente. O Linux fornece várias ferramentas para ajudar a rastrear o consumo de memória, e uma das mais versáteis é o `vmstat`.

### Introdução ao vmstat

O comando `vmstat` (estatísticas de memória virtual) é um poderoso **monitor de utilização de memória** que relata informações sobre processos, memória, paginação, E/S de bloco, interrupções (traps) e atividade da CPU. Executá-lo sem argumentos fornece um instantâneo do estado atual do sistema desde a última inicialização.

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

A saída é organizada em várias colunas. Vamos detalhar o que cada campo significa.

### Procs

- `r`: O número de processos executáveis esperando por tempo de execução.
- `b`: O número de processos em suspensão ininterrupta, tipicamente esperando por E/S.

### Memory

- `swpd`: A quantidade de memória virtual usada (em kilobytes).
- `free`: A quantidade de memória ociosa (em kilobytes).
- `buff`: A quantidade de memória usada como buffers.
- `cache`: A quantidade de memória usada como cache de página.

### Swap

- `si`: A quantidade de memória trocada (swapped in) do disco por segundo (em kilobytes). Valores altos indicam que o sistema está com pouca memória física.
- `so`: A quantidade de memória trocada (swapped out) para o disco por segundo (em kilobytes). Isso deve ser idealmente zero.

### IO

- `bi`: Blocos recebidos de um dispositivo de bloco (blocos/s).
- `bo`: Blocos enviados para um dispositivo de bloco (blocos/s).

### System

- `in`: O número de interrupções por segundo, incluindo o relógio.
- `cs`: O número de trocas de contexto (context switches) por segundo.

### CPU

Estas são porcentagens do tempo total da CPU.

- `us`: Tempo gasto executando código não-kernel (tempo de usuário).
- `sy`: Tempo gasto executando código kernel (tempo de sistema).
- `id`: Tempo gasto ocioso.
- `wa`: Tempo gasto esperando por E/S.
- `st`: Tempo roubado de uma máquina virtual (para ambientes virtualizados).

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre monitoramento de sistema e memória:

1. **[Comando free do Linux: Monitorando a Memória do Sistema](https://labex.io/pt/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Aprenda a monitorar e analisar o uso de memória do sistema, entendendo vários formatos de exibição e o consumo total de memória.
2. **[Comando top do Linux: Monitoramento de Sistema em Tempo Real](https://labex.io/pt/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprenda a monitorar o desempenho do sistema em tempo real, incluindo processos, CPU e uso de memória, usando várias opções para ordenação e filtragem.

Estes laboratórios ajudarão você a aplicar os conceitos de monitoramento de recursos do sistema em cenários reais e a ganhar confiança na análise do desempenho do sistema Linux.

## Quiz Question

Qual ferramenta é usada para visualizar a utilização da memória? (Por favor, responda em inglês, prestando atenção à sensibilidade de maiúsculas e minúsculas)

## Quiz Answer

vmstat
