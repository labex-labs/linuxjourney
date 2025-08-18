---
lang: "pt"
title: "Monitoramento de Memória"
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
- b - Número de processos em suspensão ininterrupta

### memory

- swpd - Quantidade de memória virtual usada
- free - Quantidade de memória livre
- buff - Quantidade de memória usada como buffers
- cache - Quantidade de memória usada como cache

### swap

- si - Quantidade de memória trocada do disco (swapped in)
- so - Quantidade de memória trocada para o disco (swapped out)

### io

- bi - Quantidade de blocos recebidos de um dispositivo de bloco
- bo - Quantidade de blocos enviados para um dispositivo de bloco

### system

- in - Número de interrupções por segundo
- cs - Número de trocas de contexto por segundo

### cpu

- us - Tempo gasto em user time
- sy - Tempo gasto em kernel time
- id - Tempo gasto ocioso
- wa - Tempo gasto esperando por IO

## Exercise

Observe o uso da sua memória com o vmstat.

## Quiz Question

Qual ferramenta é usada para visualizar a utilização da memória?

## Quiz Answer

vmstat
