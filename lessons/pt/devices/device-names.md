---
index: 3
lang: "pt"
title: "Nomes de Dispositivos"
meta_title: "Nomes de Dispositivos - Dispositivos"
meta_description: "Explore nomes comuns de dispositivos Linux para armazenamento e periféricos. Este guia explica a convenção de nomenclatura para discos SCSI (como sda), o que sda significa e dispositivos pseudo como /dev/null."
meta_keywords: "nomes de dispositivos linux, nome de dispositivo linux, o que significa sda, nome do elemento sd, qual seria comumente o nome do dispositivo para a primeira partição no segundo disco scsi, /dev, dispositivos SCSI, dispositivos pseudo, dispositivos PATA"
---

## Lesson Content

No Linux, cada dispositivo é representado por um arquivo no diretório `/dev`. Entender as convenções de nomenclatura para esses arquivos é crucial para a administração do sistema. Aqui estão os tipos mais comuns de nomes de dispositivos Linux que você encontrará.

### Dispositivos SCSI e de Armazenamento Modernos

Mesmo que sua máquina use armazenamento moderno como SATA, NVMe ou unidades USB, o kernel Linux geralmente os gerencia por meio de seu subsistema SCSI (Small Computer System Interface). É por isso que o prefixo mais comum para dispositivos de armazenamento é `sd`, que originalmente significava "SCSI disk" (Disco SCSI).

A `sd element name` segue um padrão claro:

- O prefixo `sd` indica um dispositivo de armazenamento em massa.
- A próxima letra representa a unidade em si, atribuída na ordem de detecção (`a` para a primeira, `b` para a segunda, e assim por diante).
- Um número no final indica a partição nessa unidade.

Os arquivos de dispositivo SCSI comuns incluem:

- `/dev/sda`: A primeira unidade de armazenamento.
- `/dev/sdb`: A segunda unidade de armazenamento.
- `/dev/sda3`: A terceira partição na primeira unidade de armazenamento.

Então, qual seria comumente o nome do dispositivo para a primeira partição no segundo disco SCSI? Seguindo o padrão, o segundo disco é `sdb`, e sua primeira partição é `1`. Portanto, o nome do dispositivo é `/dev/sdb1`.

### Pseudo-Dispositivos

Pseudo-dispositivos são arquivos especiais que não correspondem a nenhum hardware físico, mas fornecem funções úteis ao sistema. Eles são tipicamente dispositivos de caractere.

- `/dev/zero`: Aceita e descarta toda a entrada. Quando lido, produz um fluxo contínuo de bytes NULL (valor zero).
- `/dev/null`: Aceita e descarta tudo o que é escrito nele, e não produz saída quando lido.
- `/dev/random`: Produz um fluxo de números aleatórios gerados a partir do ruído ambiental.

### Dispositivos PATA Legados

Em sistemas mais antigos, você pode encontrar discos rígidos que usam a interface PATA (Parallel ATA). O nome do dispositivo Linux para essas unidades usa o prefixo `hd`.

- `/dev/hda`: O primeiro disco rígido PATA.
- `/dev/hdd2`: A segunda partição no quarto disco rígido PATA.

## Exercise

Prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão dos nomes de dispositivos Linux e gerenciamento de armazenamento:

1. **[Gerenciar Partições e Sistemas de Arquivos Linux](https://labex.io/pt/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Pratique a criação, formatação e montagem de partições, o que envolve diretamente trabalhar com nomes de dispositivos.
2. **[Explorar Dispositivos de Hardware no Linux](https://labex.io/pt/labs/comptia-explore-hardware-devices-in-linux-590861)** - Aprenda a identificar e inspecionar vários dispositivos de hardware e seus nomes associados em um ambiente Linux.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança no gerenciamento de armazenamento e na compreensão de hardware no Linux.

## Quiz Question

Qual seria comumente o nome do dispositivo para a primeira partição no segundo disco SCSI? Por favor, forneça a resposta em inglês, prestando atenção ao uso correto de maiúsculas e minúsculas.

## Quiz Answer

/dev/sdb1
