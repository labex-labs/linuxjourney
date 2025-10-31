---
index: 5
lang: "pt"
title: "Monitoramento de E/S"
meta_title: "Monitoramento de E/S - Utilização de Processos"
meta_description: "Domine o monitoramento de E/S do Linux com o comando iostat. Este guia explica como analisar métricas de uso de CPU e disco para otimizar o desempenho do seu sistema."
meta_keywords: "monitoramento de e/s, iostat, monitoramento de e/s linux, uso de cpu, uso de disco, desempenho do sistema, iowait, comandos linux"
---

## Lesson Content

O **monitoramento de I/O** eficaz é crucial para manter um sistema Linux saudável e responsivo. Uma ferramenta poderosa de linha de comando para esta tarefa é o **iostat**, que fornece relatórios detalhados sobre a atividade da CPU e do disco.

Executar o comando `iostat` gera um instantâneo das métricas de desempenho do seu sistema.

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

A saída é dividida em duas seções principais. Vamos analisá-las.

### Entendendo as Métricas da CPU

A primeira seção detalha a utilização da CPU, fornecendo informações sobre como o processador está gastando seu tempo.

- **%user**: Porcentagem do tempo da CPU gasto executando processos em nível de usuário (aplicativos).
- **%nice**: Porcentagem do tempo da CPU gasto em processos de nível de usuário com prioridade modificada (nice).
- **%system**: Porcentagem do tempo da CPU gasto executando processos em nível de sistema (kernel).
- **%iowait**: Porcentagem do tempo em que a CPU ficou ociosa enquanto esperava a conclusão de uma solicitação de E/S de disco pendente. Valores altos aqui podem indicar um gargalo de armazenamento.
- **%steal**: Em um ambiente virtualizado, esta é a porcentagem de tempo que uma CPU virtual espera por uma CPU real enquanto o hipervisor está atendendo a outro processador virtual.
- **%idle**: Porcentagem do tempo em que a CPU ficou ociosa e não estava esperando por nenhuma solicitação de E/S de disco.

### Analisando a Utilização do Disco

A segunda seção foca no **monitoramento de E/S** em nível de dispositivo, mostrando como os dados estão sendo transferidos de e para seus dispositivos de armazenamento.

- **tps**: Transferências por segundo emitidas para o dispositivo. Uma transferência é uma solicitação de E/S, e várias solicitações lógicas podem ser combinadas em uma única.
- **kB_read/s**: A quantidade de dados lidos do dispositivo, expressa em kilobytes por segundo.
- **kB_wrtn/s**: A quantidade de dados gravados no dispositivo, expressa em kilobytes por segundo.
- **kB_read**: O número total de kilobytes lidos do dispositivo desde a última reinicialização.
- **kB_wrtn**: O número total de kilobytes gravados no dispositivo desde a última reinicialização.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre monitoramento de sistema e uso de disco:

1. **[Comando Linux df: Relatório de Espaço em Disco](https://labex.io/pt/labs/linux-linux-df-command-disk-space-reporting-219188)** - Pratique a geração de relatórios sobre o uso de espaço em disco em sistemas de arquivos montados, um aspecto chave do monitoramento.
2. **[Comando Linux du: Estimativa de Espaço em Arquivos](https://labex.io/pt/labs/linux-linux-du-command-file-space-estimating-219190)** - Aprenda a estimar o uso de espaço em disco para diretórios e subdiretórios, complementando as informações de E/S de disco do `iostat`.
3. **[Comando Linux top: Monitoramento de Sistema em Tempo Real](https://labex.io/pt/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Explore o monitoramento de sistema em tempo real, incluindo uso de CPU e memória, o que fornece um contexto mais amplo para as métricas de CPU vistas no `iostat`.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança no monitoramento dos recursos do sistema Linux.

## Quiz Question

Qual comando pode ser usado para visualizar o uso de E/S e CPU? (Por favor, responda apenas com caracteres em inglês minúsculos)

## Quiz Answer

iostat
