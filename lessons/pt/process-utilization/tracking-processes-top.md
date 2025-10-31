---
index: 1
lang: "pt"
title: "Rastreamento de processos: top"
meta_title: "Rastreamento de processos: top - Utilização do Processo"
meta_description: "Descubra a melhor forma de aprender Linux dominando o comando `top`. Este guia explica como monitorar recursos do sistema, rastrear processos e entender métricas como VIRT e RES. Uma parte essencial para entender como o Linux funciona."
meta_keywords: "comando top linux, monitorar processos, utilização do sistema, como funciona o linux, linux top virt res, melhor forma de aprender linux, desempenho linux, gerenciamento de processos, treinamento linux online gratuito com certificado"
---

## Lesson Content

Compreender como ler e analisar a utilização de recursos é uma competência crítica para qualquer utilizador de Linux. Muitos consideram dominar as ferramentas de linha de comandos a **melhor forma de aprender Linux** desde o início, pois fornecem uma visão profunda sobre **como o Linux funciona**. Esta lição apresenta o `top`, uma ferramenta poderosa para rastrear o que os seus processos estão a fazer em tempo real.

### Compreender o Comando top

Já mencionámos brevemente o `top`, mas agora vamos aprofundar os detalhes do que ele exibe. O comando `top` fornece uma visão dinâmica e em tempo real dos processos e da utilização do sistema na sua máquina.

```plaintext
top - 18:06:26 up 6 days,  4:07,  2 users,  load average: 0.92, 0.62, 0.59
Tasks: 389 total,   1 running, 387 sleeping,   0 stopped,   1 zombie
%Cpu(s):  1.8 us,  0.4 sy,  0.0 ni, 97.6 id,  0.1 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:  32870888 total, 27467976 used,  5402912 free,   518808 buffers
KiB Swap: 33480700 total,    39892 used, 33440808 free. 19454152 cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 6675 patty    20   0 1731472 520960  30876 S   8.3  1.6 160:24.79 chrome
 6926 patty    20   0  935888 163456  25576 S   4.3  0.5   5:28.13 chrome
```

Vamos analisar o que este resultado significa. Não precisa de memorizar isto, mas pode usar esta lição como referência.

### Resumo do Sistema

A primeira secção fornece um resumo de alto nível do estado do sistema.

- **1ª linha**: Esta é a mesma informação que veria se executasse o comando `uptime`. Mostra a hora atual, o tempo de atividade do sistema, o número de utilizadores ligados e a média de carga do sistema nos últimos 1, 5 e 15 minutos.
- **2ª linha**: Um resumo de todas as tarefas (processos), categorizadas como em execução, em espera (sleeping), paradas (stopped) ou zumbis (zombie).

### Detalhe da Utilização da CPU

A terceira linha detalha a utilização da CPU.

- `us`: Percentagem do tempo da CPU gasta a executar processos de utilizador que não são "niced" (prioridade normal).
- `sy`: Percentagem do tempo da CPU gasta a executar o kernel e os seus processos.
- `ni`: Percentagem do tempo da CPU gasta a executar processos de utilizador "niced" (baixa prioridade).
- `id`: Percentagem do tempo da CPU que está ociosa.
- `wa`: Percentagem do tempo da CPU gasta à espera que as operações de I/O sejam concluídas. Um valor elevado pode indicar um gargalo no disco ou na rede.
- `hi`: Percentagem do tempo da CPU gasta a servir interrupções de hardware.
- `si`: Percentagem do tempo da CPU gasta a servir interrupções de software.
- `st`: Tempo de roubo (Steal time). Em ambientes virtualizados, esta é a percentagem de tempo da CPU que um processador virtual espera por um processador real, enquanto o hipervisor está a servir outro processador virtual.

### Informação de Memória e Swap

A quarta e quinta linhas mostram o uso do espaço de memória e swap, respetivamente. Isto inclui as quantidades total, usada e livre.

### A Lista de Processos

O corpo principal do `top` é uma lista dos processos que mais consomem recursos.

- `PID`: O Identificador de Processo único.
- `USER`: O utilizador que é proprietário do processo.
- `PR`: A prioridade de agendamento do processo.
- `NI`: O valor "nice", que afeta a sua prioridade.
- `VIRT`: Memória Virtual usada pelo processo. Esta é a quantidade total de memória que o processo pode aceder.
- `RES`: Memória Residente usada pelo processo. Esta é a memória física não trocada que uma tarefa está a usar. Compreender a diferença entre **linux top virt res** é fundamental para a análise de memória.
- `SHR`: Memória Partilhada usada pelo processo.
- `S`: O estado do processo: `S`=dormir (sleep), `R`=a correr (running), `Z`=zumbi (zombie), `D`=sono ininterruptível (uninterruptible sleep), `T`=parado (stopped).
- `%CPU`: A percentagem de tempo de CPU utilizada por este processo desde a última atualização.
- `%MEM`: A percentagem de RAM física usada por este processo.
- `TIME+`: O tempo total de CPU que o processo usou desde que iniciou.
- `COMMAND`: O nome do comando ou a linha de comandos que iniciou o processo.

Também pode monitorizar um processo específico pelo seu ID, o que é útil para resolução de problemas focada:

```bash
top -p 1
```

## Exercise

A prática é essencial para a mestria. Estes laboratórios práticos são alguns dos **melhores recursos para aprender Linux** sobre gestão de processos, fornecendo um ambiente prático para aplicar o que aprendeu.

1. **[Gerir e Monitorizar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação, inspeção, monitorização e terminação de processos num ambiente Linux real.
2. **[Comando Linux top: Monitorização do Sistema em Tempo Real](https://labex.io/pt/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprenda a usar o comando `top` para monitorizar a utilização da CPU, memória e processos em execução em tempo real.
3. **[Comando Linux free: Monitorização da Memória do Sistema](https://labex.io/pt/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Aprenda a usar o comando `free` para monitorizar e analisar a utilização da memória do sistema.

## Quiz Question

Que comando exibe o mesmo resultado que a primeira linha no `top`? Por favor, responda usando apenas o nome do comando em inglês minúsculo.

## Quiz Answer

uptime
