---
index: 5
lang: "pt"
title: "Monitoramento de E/S"
meta_title: "Monitoramento de E/S - Utilização de Processos"
meta_description: "Aprenda a usar o iostat para monitoramento de E/S no Linux. Entenda as métricas de uso de CPU e disco com este comando essencial. Melhore o desempenho do sistema!"
meta_keywords: "iostat, monitoramento de E/S Linux, uso de CPU, uso de disco, comandos Linux, iniciante, tutorial, guia"
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
- **%iowait** - Mostra a porcentagem de tempo em que a CPU ou CPUs ficaram ociosas, durante o qual o sistema tinha uma solicitação de E/S de disco pendente.
- **%steal** - Mostra a porcentagem de tempo gasto em espera involuntária pela CPU ou CPUs virtuais enquanto o hypervisor estava atendendo outro processador virtual.
- **%idle** - Mostra a porcentagem de tempo em que a CPU ou CPUs ficaram ociosas e o sistema não tinha uma solicitação de E/S de disco pendente.

A segunda parte é a utilização do disco:

- **tps** - Indica o número de transferências por segundo que foram emitidas para o dispositivo. Uma transferência é uma solicitação de E/S para o dispositivo. Múltiplas solicitações lógicas podem ser combinadas em uma única solicitação de E/S para o dispositivo. Uma transferência tem tamanho indeterminado.
- **kB_read/s** - Indica a quantidade de dados lidos do dispositivo, expressa em kilobytes por segundo.
- **kB_wrtn/s** - Indica a quantidade de dados gravados no dispositivo, expressa em kilobytes por segundo.
- **kB_read** - O número total de kilobytes lidos.
- **kB_wrtn** - O número total de kilobytes gravados.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre monitoramento de sistema e uso de disco:

1. **[Comando Linux df: Relatório de Espaço em Disco](https://labex.io/pt/labs/linux-linux-df-command-disk-space-reporting-219188)** - Pratique o relatório de uso do espaço em disco em sistemas de arquivos montados, um aspecto chave do monitoramento.
2. **[Comando Linux du: Estimativa de Espaço em Arquivo](https://labex.io/pt/labs/linux-linux-du-command-file-space-estimating-219190)** - Aprenda a estimar o uso do espaço em disco para diretórios e subdiretórios, complementando as informações de E/S de disco do `iostat`.
3. **[Comando Linux top: Monitoramento de Sistema em Tempo Real](https://labex.io/pt/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Explore o monitoramento de sistema em tempo real, incluindo uso de CPU e memória, o que fornece um contexto mais amplo para as métricas de CPU vistas no `iostat`.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança no monitoramento de recursos do sistema Linux.

## Quiz Question

Qual comando pode ser usado para visualizar o uso de E/S e CPU?

## Quiz Answer

iostat
