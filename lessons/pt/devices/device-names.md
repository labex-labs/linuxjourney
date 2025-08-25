---
index: 3
lang: "pt"
title: "Nomes de Dispositivos"
meta_title: "Nomes de Dispositivos - Dispositivos"
meta_description: "Aprenda os nomes de dispositivos Linux como SCSI (sd), pseudo e PATA (hd). Entenda /dev/sda, /dev/null e muito mais neste guia para iniciantes."
meta_keywords: "nomes de dispositivos Linux, /dev, dispositivos SCSI, pseudodispositivos, dispositivos PATA, tutorial Linux, Linux para iniciantes, arquivos de dispositivo"
---

## Lesson Content

Aqui estão os nomes de dispositivos mais comuns que você encontrará:

### Dispositivos SCSI

Se você tem algum tipo de armazenamento em massa em sua máquina, é provável que ele esteja usando o protocolo SCSI (pronuncia-se "scuzzy"). SCSI significa Small Computer System Interface; é um protocolo usado para permitir a comunicação entre discos, impressoras, scanners e outros periféricos e seu sistema. Você pode ter ouvido falar de dispositivos SCSI, que na verdade não estão em uso em sistemas modernos; no entanto, nossos sistemas Linux correspondem a discos SCSI com unidades de disco rígido em `/dev`. Eles são representados por um prefixo de `sd` (disco SCSI):

Arquivos de dispositivo SCSI comuns:

- `/dev/sda` - Primeiro disco rígido
- `/dev/sdb` - Segundo disco rígido
- `/dev/sda3` - Terceira partição no primeiro disco rígido

### Pseudodispositivos

Como discutimos anteriormente, os pseudodispositivos não estão realmente conectados fisicamente ao seu sistema. A maioria dos pseudodispositivos comuns são dispositivos de caractere:

- `/dev/zero` - aceita e descarta toda a entrada, produz um fluxo contínuo de bytes NULL (valor zero)
- `/dev/null` - aceita e descarta toda a entrada, não produz saída
- `/dev/random` - produz números aleatórios

### Dispositivos PATA

Às vezes, em sistemas mais antigos, você pode ver discos rígidos sendo referidos com um prefixo `hd`:

- `/dev/hda` - Primeiro disco rígido
- `/dev/hdd2` - Segunda partição no 4º disco rígido

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão dos nomes de dispositivos Linux e gerenciamento de armazenamento:

1. **[Gerenciar Partições e Sistemas de Arquivos Linux](https://labex.io/pt/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Pratique a criação, formatação e montagem de partições, o que envolve diretamente o trabalho com nomes de dispositivos.
2. **[Explorar Dispositivos de Hardware no Linux](https://labex.io/pt/labs/comptia-explore-hardware-devices-in-linux-590861)** - Aprenda a identificar e inspecionar vários dispositivos de hardware e seus nomes associados em um ambiente Linux.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança no gerenciamento de armazenamento e na compreensão de hardware no Linux.

## Quiz Question

Qual seria comumente o nome do dispositivo para a primeira partição no segundo disco SCSI?

## Quiz Answer

sdb1
