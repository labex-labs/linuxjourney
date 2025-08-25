---
index: 6
lang: "pt"
title: "Monitoramento de Memória"
meta_title: "Monitoramento de Memória - Utilização de Processos"
meta_description: "Aprenda a monitorar o uso da memória Linux com vmstat. Entenda as métricas de memória, swap e CPU para o desempenho do sistema. Comece sua jornada Linux!"
meta_keywords: "vmstat, monitoramento de memória Linux, desempenho do sistema, tutorial Linux, uso de memória, Linux para iniciantes, guia Linux"
---

## Lesson Content

Além do monitoramento de CPU e monitoramento de E/S, você pode monitorar o uso da sua memória com o **vmstat**.

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

Os campos são os seguintes:

### procs

- r - Número de processos para tempo de execução
- b - Número de processos em sono ininterrupto

### memória

- swpd - Quantidade de memória virtual usada
- free - Quantidade de memória livre
- buff - Quantidade de memória usada como buffers
- cache - Quantidade de memória usada como cache

### swap

- si - Quantidade de memória trocada do disco
- so - Quantidade de memória trocada para o disco

### io

- bi - Quantidade de blocos recebidos de um dispositivo de bloco
- bo - Quantidade de blocos enviados para um dispositivo de bloco

### sistema

- in - Número de interrupções por segundo
- cs - Número de trocas de contexto por segundo

### cpu

- us - Tempo gasto em tempo de usuário
- sy - Tempo gasto em tempo de kernel
- id - Tempo gasto ocioso
- wa - Tempo gasto esperando por IO

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do monitoramento de sistema e memória:

1. **[Comando Linux free: Monitorando a Memória do Sistema](https://labex.io/pt/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Aprenda a monitorar e analisar o uso da memória do sistema, compreendendo vários formatos de exibição e o consumo total de memória.
2. **[Comando Linux top: Monitoramento do Sistema em Tempo Real](https://labex.io/pt/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprenda a monitorar o desempenho do sistema em tempo real, incluindo processos, CPU e uso de memória, usando várias opções para classificação e filtragem.

Esses laboratórios o ajudarão a aplicar os conceitos de monitoramento de recursos do sistema em cenários reais e a construir confiança na análise do desempenho do sistema Linux.

## Quiz Question

Qual ferramenta é usada para visualizar a utilização da memória?

## Quiz Answer

vmstat
