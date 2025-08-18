---
lang: "pt"
title: "tipos de dispositivos"
meta_description: "Aprenda sobre os tipos de dispositivos Linux (character, block, pipe, socket) e como identificá-los usando `ls -l /dev`. Entenda os major/minor device numbers. Tutorial de Linux para iniciantes."
meta_keywords: "tipos de dispositivos Linux, ls -l /dev, character device, block device, major minor device number, tutorial Linux, guia Linux, iniciante"
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
- Major Device Number
- Minor Device Number
- Carimbo de data/hora
- Nome do Dispositivo

Lembre-se, no comando `ls`, você pode ver o tipo de arquivo com o primeiro bit em cada linha. Os arquivos de dispositivo são denotados da seguinte forma:

- c - character
- b - block
- p - pipe
- s - socket

### Character Device

Esses dispositivos transferem dados, mas um caractere por vez. Você verá muitos pseudo dispositivos (`/dev/null`) como character devices. Esses dispositivos não estão realmente conectados fisicamente à máquina, mas permitem maior funcionalidade ao sistema operacional.

### Block Device

Esses dispositivos transferem dados, mas em grandes blocos de tamanho fixo. Você verá mais comumente dispositivos que utilizam blocos de dados como block devices, como discos rígidos, sistemas de arquivos, etc.

### Pipe Device

Named pipes permitem que dois ou mais processos se comuniquem entre si. Eles são semelhantes aos character devices, mas em vez de ter a saída enviada para um dispositivo, ela é enviada para outro processo.

### Socket Device

Socket devices facilitam a comunicação entre processos, semelhante aos pipe devices, mas podem se comunicar com muitos processos ao mesmo tempo.

### Device Characterization

Os dispositivos são caracterizados usando dois números: **major device number** e **minor device number**. Você pode ver esses números no exemplo `ls` acima; eles são separados por uma vírgula. Por exemplo, digamos que um dispositivo tivesse os números de dispositivo: **8, 0**:

O major device number representa o driver de dispositivo que é usado, neste caso 8, que é frequentemente o número principal para dispositivos de bloco sd. O minor number informa ao kernel qual dispositivo único ele é nesta classe de driver; neste caso, 0 é usado para representar o primeiro dispositivo (a).

## Exercise

Olhe para o seu diretório `/dev` e descubra quais tipos de dispositivos você pode ver.

## Quiz Question

Qual é o símbolo para character devices no comando `ls -l`?

## Quiz Answer

c
