---
index: 1
lang: "pt"
title: "Rastreando processos: top"
meta_title: "Rastreando processos: top - Utilização de Processos"
meta_description: "Aprenda a usar o comando `top` do Linux para monitorar recursos do sistema e rastrear processos. Entenda os detalhes de CPU, memória e processos para análise de desempenho."
meta_keywords: "comando top Linux, monitorar processos, utilização do sistema, desempenho Linux, iniciante, tutorial, guia"
---

## Lesson Content

Neste curso, abordaremos como ler e analisar a utilização de recursos em seu sistema. Esta lição mostra algumas ótimas ferramentas para usar quando você precisa rastrear o que um processo está fazendo.

### top

Já discutimos o `top` antes, mas vamos aprofundar nos detalhes do que ele realmente está exibindo. Lembre-se, `top` é a ferramenta que usamos para obter uma visão em tempo real da utilização do sistema pelos nossos processos:

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

Vamos analisar o que essa saída significa. Você não precisa memorizar isso, mas volte aqui quando precisar de uma referência.

### 1ª linha: Esta é a mesma informação que você veria se executasse o comando `uptime` (mais por vir)

Os campos são da esquerda para a direita:

1. Hora atual
2. Há quanto tempo o sistema está em execução
3. Quantos usuários estão atualmente logados
4. Média de carga do sistema (mais por vir)

### 2ª linha: Tarefas que estão em execução, dormindo, paradas e zumbis

### 3ª linha: Informações da CPU

1. `us`: tempo de CPU do usuário - Porcentagem do tempo de CPU gasto executando processos de usuários que não são niced.
2. `sy`: tempo de CPU do sistema - Porcentagem do tempo de CPU gasto executando o kernel e processos do kernel.
3. `ni`: tempo de CPU nice - Porcentagem do tempo de CPU gasto executando processos niced.
4. `id`: tempo ocioso da CPU - Porcentagem do tempo de CPU que é gasto ocioso.
5. `wa`: espera de E/S - Porcentagem do tempo de CPU que é gasto esperando por E/S. Se este valor for baixo, o problema provavelmente não é E/S de disco ou rede.
6. `hi`: interrupções de hardware - Porcentagem do tempo de CPU gasto atendendo interrupções de hardware.
7. `si`: interrupções de software - Porcentagem do tempo de CPU gasto atendendo interrupções de software.
8. `st`: tempo de roubo - Se você estiver executando máquinas virtuais, esta é a porcentagem do tempo de CPU que foi roubado de você para outras tarefas.

### 4ª e 5ª linha: Uso de Memória e Uso de Swap

### Lista de Processos Atualmente em Uso

1. `PID`: ID do processo
2. `USER`: usuário que é o proprietário do processo
3. `PR`: Prioridade do processo
4. `NI`: O valor nice
5. `VIRT`: Memória virtual usada pelo processo
6. `RES`: Memória física usada pelo processo
7. `SHR`: Memória compartilhada do processo
8. `S`: Indica o status do processo: `S`=sleep, `R`=running, `Z`=zombie, `D`=uninterruptible, `T`=stopped
9. `%CPU`: esta é a porcentagem de CPU usada por este processo
10. `%MEM`: porcentagem de RAM usada por este processo
11. `TIME+`: tempo total de atividade deste processo
12. `COMMAND`: nome do processo

Você também pode especificar um ID de processo se quiser apenas rastrear certos processos:

```bash
top -p 1
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da utilização de recursos do Linux e do gerenciamento de processos:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique interagir, inspecionar, monitorar e encerrar processos em um ambiente Linux real.
2. **[Comando Linux top: Monitoramento de Sistema em Tempo Real](https://labex.io/pt/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprenda a usar o comando `top` para monitorar o uso da CPU, memória e processos em execução em tempo real.
3. **[Comando Linux free: Monitorando a Memória do Sistema](https://labex.io/pt/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Aprenda a usar o comando `free` para monitorar e analisar o uso da memória do sistema.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com o monitoramento do sistema e o gerenciamento de processos.

## Quiz Question

Qual comando exibe a mesma saída que a primeira linha em `top`?

## Quiz Answer

uptime
