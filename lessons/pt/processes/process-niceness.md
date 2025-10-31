---
index: 8
lang: "pt"
title: "Simpatia"
meta_title: "Simpatia - Processos"
meta_description: "Descubra o que é a simpatia (niceness) no Linux e como ela afeta a prioridade dos processos. Esta lição explica a simpatia de processos no Linux, usando os comandos nice e renice para gerenciar o agendamento da CPU e melhorar o desempenho do sistema."
meta_keywords: "simpatia linux, linux simpatia, o que é simpatia no linux, simpatia de processo linux, simpatia do processo, prioridade do processo, comando nice, comando renice, agendamento da CPU"
---

## Lesson Content

Quando você executa vários aplicativos no seu computador, parece que todos estão rodando simultaneamente. Na realidade, a CPU está alternando rapidamente entre eles, dando a cada processo uma pequena quantidade de tempo de processamento.

### Como a CPU Gerencia Processos

Cada processo recebe uma pequena quantidade de tempo de CPU chamada "fatia de tempo" (time slice). Após sua fatia de tempo, um processo é pausado e a CPU passa para o próximo. Por padrão, o kernel Linux agenda os processos de forma circular (round-robin), garantindo que cada processo receba uma parte justa do tempo da CPU até ser concluído. O escalonador (scheduler) do kernel é altamente eficiente no gerenciamento dessas trocas rápidas.

### O Que é Niceness no Linux

Embora os processos não possam controlar diretamente seu tempo de CPU, você pode influenciar as decisões de agendamento do kernel. Isso é feito ajustando o valor de **niceness do linux** de um processo. O termo "niceness" refere-se ao quão "gentil" um processo é com outros processos no sistema.

A **niceness de um processo** é representada por um número que varia de -20 (maior prioridade) a 19 (menor prioridade).

- Um valor de niceness alto (ex: 19) significa que o processo é muito "gentil" e tem baixa prioridade, cedendo tempo de CPU para outros.
- Um valor de niceness baixo ou negativo (ex: -20) significa que o processo não é "gentil" e exige mais tempo de CPU, recebendo assim uma prioridade maior.

Compreender a **niceness de processo no linux** é fundamental para gerenciar os recursos do sistema de forma eficaz.

### Ajustando a Prioridade do Processo

Você pode visualizar o nível de niceness atual dos processos em execução usando o comando `top`. Procure pela coluna `NI`, que exibe o valor de niceness.

```bash
top
```

Para controlar o valor de **niceness linux**, você pode usar os comandos `nice` e `renice`.

Use o comando `nice` para iniciar um novo processo com um nível de niceness específico. Por exemplo, o comando a seguir inicia `apt upgrade` com um niceness de 5.

```bash
nice -n 5 apt upgrade
```

Para alterar a prioridade de um processo já em execução, use o comando `renice`. O comando a seguir altera o niceness de um processo com PID 3245 para 10.

```bash
renice 10 -p 3245
```

## Exercise

Aplique seu conhecimento com este laboratório prático para reforçar sua compreensão sobre gerenciamento e agendamento de processos no Linux:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação com processos em primeiro plano e em segundo plano, inspecionando-os com `ps`, monitorando recursos com `top`, ajustando a prioridade com `renice` e encerrando-os com `kill`.

Este laboratório ajudará você a aplicar os conceitos de agendamento de processos e niceness em cenários reais e a ganhar confiança no gerenciamento de processos no Linux.

## Quiz Question

If you want a process to get more CPU priority, should you use a lower or higher nice number? Please answer in a single English word, all lowercase.

## Quiz Answer

lower
