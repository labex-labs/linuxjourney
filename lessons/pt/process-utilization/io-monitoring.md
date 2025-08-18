---
lang: "pt"
title: "Monitoramento de I/O"
meta_title: "Monitoramento de I/O - Utilização de Processos"
meta_description: "Aprenda a usar o iostat para monitoramento de I/O no Linux. Entenda as métricas de uso de CPU e disco com este comando essencial. Melhore o desempenho do sistema!"
meta_keywords: "iostat, monitoramento de I/O Linux, uso de CPU, uso de disco, comandos Linux, iniciante, tutorial, guia"
---

## Lesson Content

Podemos monitorar o uso da CPU, bem como o uso do disco, com uma ferramenta útil conhecida como **iostat**.

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

A primeira parte é a informação da CPU:

- **%user** - Mostra a porcentagem de utilização da CPU que ocorreu durante a execução no nível do usuário (aplicativo).
- **%nice** - Mostra a porcentagem de utilização da CPU que ocorreu durante a execução no nível do usuário com prioridade nice.
- **%system** - Mostra a porcentagem de utilização da CPU que ocorreu durante a execução no nível do sistema (kernel).
- **%iowait** - Mostra a porcentagem de tempo em que a CPU ou CPUs ficaram ociosas, durante o qual o sistema tinha uma solicitação de I/O de disco pendente.
- **%steal** - Mostra a porcentagem de tempo gasto em espera involuntária pela CPU virtual ou CPUs enquanto o hypervisor estava atendendo outro processador virtual.
- **%idle** - Mostra a porcentagem de tempo em que a CPU ou CPUs ficaram ociosas e o sistema não tinha uma solicitação de I/O de disco pendente.

A segunda parte é a utilização do disco:

- **tps** - Indica o número de transferências por segundo que foram emitidas para o dispositivo. Uma transferência é uma solicitação de I/O para o dispositivo. Múltiplas solicitações lógicas podem ser combinadas em uma única solicitação de I/O para o dispositivo. Uma transferência tem tamanho indeterminado.
- **kB_read/s** - Indica a quantidade de dados lidos do dispositivo, expressa em kilobytes por segundo.
- **kB_wrtn/s** - Indica a quantidade de dados escritos no dispositivo, expressa em kilobytes por segundo.
- **kB_read** - O número total de kilobytes lidos.
- **kB_wrtn** - O número total de kilobytes escritos.

## Exercise

Use iostat para visualizar o uso do seu disco.

## Quiz Question

Qual comando pode ser usado para visualizar o uso de I/O e CPU?

## Quiz Answer

iostat
