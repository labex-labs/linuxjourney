---
lang: "pt"
title: "Rastreando processos: top"
meta_description: "Aprenda a usar o comando `top` do Linux para monitorar recursos do sistema e rastrear processos. Entenda os detalhes de CPU, memória e processos para análise de desempenho."
meta_keywords: "comando top Linux, monitorar processos, utilização do sistema, desempenho Linux, iniciante, tutorial, guia"
---

## Lesson Content

Neste curso, abordaremos como ler e analisar a utilização de recursos em seu sistema. Esta lição mostra algumas ótimas ferramentas para usar quando você precisa rastrear o que um processo está fazendo.

### top

Já discutimos o `top` antes, mas vamos nos aprofundar nos detalhes do que ele realmente exibe. Lembre-se, `top` é a ferramenta que usamos para obter uma visão em tempo real da utilização do sistema pelos nossos processos:

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

### 1st line: This is the same information you would see if you ran the `uptime` command (more to come)

Os campos são da esquerda para a direita:

1. Hora atual
2. Há quanto tempo o sistema está em execução
3. Quantos usuários estão logados atualmente
4. Média de carga do sistema (mais por vir)

### 2nd line: Tasks that are running, sleeping, stopped, and zombied

### 3rd line: CPU information

1. `us`: user CPU time - Porcentagem do tempo de CPU gasto executando processos de usuários que não são niced.
2. `sy`: system CPU time - Porcentagem do tempo de CPU gasto executando o kernel e processos do kernel.
3. `ni`: nice CPU time - Porcentagem do tempo de CPU gasto executando processos niced.
4. `id`: CPU idle time - Porcentagem do tempo de CPU que é gasto ocioso.
5. `wa`: I/O wait - Porcentagem do tempo de CPU que é gasto esperando por I/O. Se este valor for baixo, o problema provavelmente não é I/O de disco ou rede.
6. `hi`: hardware interrupts - Porcentagem do tempo de CPU gasto atendendo interrupções de hardware.
7. `si`: software interrupts - Porcentagem do tempo de CPU gasto atendendo interrupções de software.
8. `st`: steal time - Se você estiver executando máquinas virtuais, esta é a porcentagem do tempo de CPU que foi roubado de você para outras tarefas.

### 4th and 5th line: Memory Usage and Swap Usage

### Processes List that are Currently in Use

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

Brinque com o comando `top` e veja quais processos estão usando a maioria dos recursos.

## Quiz Question

Qual comando exibe a mesma saída que a primeira linha em `top`?

## Quiz Answer

uptime
