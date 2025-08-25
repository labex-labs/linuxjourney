---
index: 2
lang: "pt"
title: "tipos de dispositivo"
meta_title: "tipos de dispositivo - Dispositivos"
meta_description: "Aprenda sobre os tipos de dispositivos Linux (caractere, bloco, pipe, socket) e como identificá-los usando `ls -l /dev`. Entenda os números de dispositivo principal/secundário. Tutorial de Linux para iniciantes."
meta_keywords: "tipos de dispositivo Linux, ls -l /dev, dispositivo de caractere, dispositivo de bloco, número de dispositivo principal secundário, tutorial Linux, guia Linux, iniciante"
---

## Lesson Content

Antes de falarmos sobre como os dispositivos são gerenciados, vamos dar uma olhada em alguns dispositivos.

```bash
$ ls -l /dev
brw-rw----   1 root disk      8,   0 Dec 20 20:13 sda
crw-rw-rw-   1 root root      1,   3 Dec 20 20:13 null
srw-rw-rw-   1 root root           0 Dec 20 20:13 log
prw-r--r--   1 root root           0 Dec 20 20:13 fdata
```

As colunas são as seguintes, da esquerda para a direita:

- Permissões
- Proprietário
- Grupo
- Número Principal do Dispositivo
- Número Secundário do Dispositivo
- Carimbo de Data/Hora
- Nome do Dispositivo

Lembre-se, no comando `ls`, você pode ver o tipo de arquivo com o primeiro bit em cada linha. Os arquivos de dispositivo são denotados da seguinte forma:

- c - character
- b - block
- p - pipe
- s - socket

### Dispositivo de Caractere

Esses dispositivos transferem dados, mas um caractere por vez. Você verá muitos pseudo-dispositivos (`/dev/null`) como dispositivos de caractere. Esses dispositivos não estão realmente conectados fisicamente à máquina, mas permitem maior funcionalidade ao sistema operacional.

### Dispositivo de Bloco

Esses dispositivos transferem dados, mas em grandes blocos de tamanho fixo. Você verá mais comumente dispositivos que utilizam blocos de dados como dispositivos de bloco, como discos rígidos, sistemas de arquivos, etc.

### Dispositivo Pipe

Pipes nomeados permitem que dois ou mais processos se comuniquem entre si. Eles são semelhantes aos dispositivos de caractere, mas em vez de ter a saída enviada para um dispositivo, ela é enviada para outro processo.

### Dispositivo Socket

Dispositivos socket facilitam a comunicação entre processos, semelhante aos dispositivos pipe, mas podem se comunicar com muitos processos ao mesmo tempo.

### Caracterização do Dispositivo

Os dispositivos são caracterizados usando dois números: **número principal do dispositivo** e **número secundário do dispositivo**. Você pode ver esses números no exemplo `ls` acima; eles são separados por uma vírgula. Por exemplo, digamos que um dispositivo tivesse os números de dispositivo: **8, 0**:

O número principal do dispositivo representa o driver do dispositivo que é usado, neste caso 8, que é frequentemente o número principal para dispositivos de bloco sd. O número secundário informa ao kernel qual dispositivo único ele é nesta classe de driver; neste caso, 0 é usado para representar o primeiro dispositivo (a).

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão dos arquivos de dispositivo Linux e seu gerenciamento:

1. **[Gerenciar Partições e Sistemas de Arquivos Linux](https://labex.io/pt/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Pratique a criação e o gerenciamento de partições de disco e sistemas de arquivos, que são dispositivos de bloco fundamentais no Linux.
2. **[Explorar Dispositivos de Hardware no Linux](https://labex.io/pt/labs/comptia-explore-hardware-devices-in-linux-590861)** - Aprenda a identificar e inspecionar vários dispositivos de hardware, entendendo como eles são representados no diretório `/dev`.
3. **[Criar e Ativar um Arquivo Swap no Linux](https://labex.io/pt/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Ganhe experiência prática na criação e ativação de um arquivo swap, que funciona como um dispositivo de memória virtual.

Esses laboratórios o ajudarão a aplicar os conceitos de interação e gerenciamento de dispositivos em cenários reais e a construir confiança com a administração de sistemas Linux.

## Quiz Question

Qual é o símbolo para dispositivos de caractere no comando `ls -l`?

## Quiz Answer

c
