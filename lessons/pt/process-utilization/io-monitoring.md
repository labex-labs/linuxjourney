---
lesson_id: "io-monitoring"
course_id: "process-utilization"
lang: "pt"
order_index: 5
title: "Monitoramento de E/S"
description: "Aprenda a usar amostras de iostat para investigar a atividade da CPU e dos dispositivos de bloco."
meta_title: "Monitoramento de E/S - Utilização de Processos"
meta_description: "Domine o monitoramento de E/S no Linux com o comando iostat. Este guia explica como analisar métricas de uso da CPU e dos discos para investigar o desempenho do sistema."
meta_keywords: "monitoramento E/S, iostat, monitoramento E/S Linux, uso da CPU, uso do disco, desempenho do sistema, iowait, comandos Linux"
---

`iostat`, normalmente fornecido pelo pacote `sysstat`, informa a atividade da CPU e dos dispositivos de bloco. Use amostras repetidas junto com a latência da aplicação: o throughput ou a utilização, sozinhos, não comprovam que o armazenamento esteja causando um problema perceptível ao usuário.

## Coleta de Amostras Úteis

Execute estatísticas detalhadas dos dispositivos em intervalos de um segundo:

```bash
$ iostat -xz 1
```

Nas implementações comuns, o primeiro relatório contém médias desde o boot, e os relatórios posteriores abrangem cada intervalo. A opção `-x` acrescenta campos detalhados, enquanto `-z` omite dispositivos inativos. Aguarde vários intervalos para capturar períodos normais e problemáticos.

:::single-choice{#iostat-first-report} O que o primeiro relatório de `iostat` normalmente representa?

::option[Somente as operações do último segundo do comando.]{#iostat-final-second explanation="Isso não descreve o relatório acumulado inicial."}
::option[As médias de atividade desde a inicialização do sistema.]{#iostat-since-boot .correct explanation="Os relatórios posteriores normalmente são específicos do intervalo, portanto o primeiro precisa ser interpretado separadamente."}
::option[Uma previsão da utilização dos dispositivos no dia seguinte.]{#iostat-forecast explanation="A ferramenta informa estatísticas observadas, não a demanda futura."}
:::

## Leitura dos Campos da CPU

A seção da CPU normalmente inclui os tempos de usuário (`%user`), sistema (`%system`), ocioso (`%idle`), espera por E/S (`%iowait`) e tomado pela máquina virtual (`%steal`). A espera por E/S é o tempo ocioso da CPU durante o qual o sistema possui uma solicitação de E/S pendente; não é a porcentagem de ocupação de um disco.

:::single-choice{#iostat-iowait-meaning} O que `%iowait` descreve?

::option[A porcentagem da capacidade do disco que já está ocupada.]{#iostat-capacity explanation="A capacidade do sistema de arquivos e o tempo de CPU são medições diferentes."}
::option[O tempo ocioso da CPU enquanto existe uma solicitação de E/S pendente.]{#iostat-iowait-cpu .correct explanation="Essa é uma categoria de tempo de CPU e, sozinha, não consegue identificar um dispositivo."}
::option[A quantidade de arquivos que aguardam exclusão.]{#iostat-delete-queue explanation="As contagens de exclusões de arquivos não são representadas por esse campo."}
:::

## Leitura dos Campos dos Dispositivos

Os nomes dos campos variam conforme a versão do sysstat, mas alguns conceitos úteis são:

- As operações ou os dados de leitura e escrita por segundo mostram a taxa da carga de trabalho.
- `await` informa a latência média das solicitações, incluindo o tempo na fila e de atendimento.
- Os campos de tamanho médio da fila mostram as solicitações aguardando ou sendo atendidas.
- `%util` informa a porcentagem do tempo decorrido durante o qual o dispositivo possuía E/S em andamento.

Um `%util` alto pode indicar saturação em um dispositivo serial simples, mas não se traduz diretamente na capacidade de desempenho de um armazenamento paralelo, arranjo ou dispositivo virtual. Compare a latência com o projeto do dispositivo, o padrão da carga de trabalho e o objetivo de serviço.

:::single-choice{#iostat-await-purpose} Qual campo está mais diretamente associado à latência média das solicitações de E/S?

::option[Nome do dispositivo.]{#iostat-device-name explanation="O nome identifica o dispositivo, mas não mede a duração das solicitações."}
::option[`await`]{#iostat-await .correct explanation="Await representa o tempo médio das solicitações, incluindo o período na fila e de atendimento."}
::option[`%idle`]{#iostat-idle explanation="Esse é um campo de CPU, não a latência das solicitações do dispositivo."}
:::

## Relação entre as Evidências

Mapeie os nomes dos dispositivos para as montagens e os dispositivos subjacentes antes de tirar conclusões:

```bash
$ lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
$ findmnt
```

Depois, relacione os intervalos de `iostat` ao tempo de resposta da aplicação, às métricas do banco de dados ou sistema de arquivos e à E/S no nível dos processos. Device mapper, RAID, contêineres e armazenamento apoiado por rede podem acrescentar camadas que exigem suas próprias ferramentas.

:::single-choice{#iostat-high-util-conclusion} O que você deve fazer depois de observar um `%util` alto em um dispositivo?

::option[Presumir que todos os sistemas de arquivos estejam sem espaço livre.]{#iostat-assume-full explanation="O tempo de ocupação não informa a capacidade do sistema de arquivos."}
::option[Excluir arquivos antes de identificar a carga de trabalho montada.]{#iostat-delete-first explanation="A exclusão altera o estado e não comprova um gargalo de E/S."}
::option[Relacionar a latência e o comportamento da carga ao projeto do armazenamento.]{#iostat-correlate .correct explanation="O paralelismo do dispositivo e os objetivos da carga determinam se a observação é prejudicial."}
:::

## Resumo

Agora você sabe usar `iostat` como evidência em uma investigação de E/S.

1. Colete vários intervalos de estatísticas detalhadas.
2. Diferencie a espera da CPU por E/S do tempo de ocupação do dispositivo.
3. Interprete juntos a latência, o enfileiramento, o throughput e a utilização.
4. Mapeie os dispositivos para as cargas de trabalho e verifique o impacto na aplicação.
