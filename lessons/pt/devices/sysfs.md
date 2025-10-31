---
index: 4
lang: "pt"
title: "sysfs"
meta_title: "sysfs - Dispositivos"
meta_description: "Explore o que é sysfs e seu papel no sistema sys do Linux. Este guia explica o diretório /sys do Linux, um sistema de arquivos virtual para informações de dispositivos, e o contrasta com /dev."
meta_keywords: "sysfs, o que é sysfs, /sys, linux /sys, sys linux, sistema sys, sistema de arquivos virtual, dispositivos linux, /dev"
---

## Lesson Content

O sistema de arquivos `sysfs` foi introduzido para fornecer uma maneira melhor de gerenciar dispositivos em um sistema Linux, uma tarefa para a qual o diretório `/dev` não estava totalmente equipado. Entender **o que é /sys no Linux** é fundamental para a administração moderna do sistema.

### O que é sysfs?

`sysfs` é um sistema de arquivos virtual, tipicamente montado em `/sys`, que exporta informações sobre objetos do kernel, dispositivos de hardware e drivers do modelo de dispositivo do kernel para o userspace. Ao contrário dos arquivos em um disco físico, os arquivos e diretórios dentro de `/sys` são gerados dinamicamente e representam o estado atual do **sistema sys**.

### O Papel do Diretório linux /sys

O principal objetivo do diretório **linux /sys** é fornecer uma visão estruturada de todos os dispositivos no seu sistema. Ele contém informações detalhadas como fabricante e modelo, onde o dispositivo está conectado, seu estado atual e sua posição na hierarquia de dispositivos.

Os arquivos que você vê aqui não são nós de dispositivo como os encontrados em `/dev`. Você não interage diretamente com o dispositivo através de `/sys`; em vez disso, você o usa para visualizar informações e gerenciar os atributos do dispositivo.

### sysfs vs. /dev

Embora `/sys` e `/dev` estejam relacionados a dispositivos, eles servem a funções diferentes.

- O diretório `/dev` fornece nós de dispositivo, que são arquivos especiais que permitem aos programas acessar os próprios dispositivos.
- O sistema de arquivos `/sys` é usado para visualizar informações sobre e gerenciar os dispositivos. Ele expõe o modelo de dispositivo subjacente.

Por exemplo, vamos inspecionar o conteúdo de um diretório de dispositivo de bloco dentro de `/sys`:

```bash
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
```

Esta saída mostra vários atributos e subdiretórios relacionados ao disco rígido `sda`, oferecendo uma visão muito mais detalhada do que apenas `/dev/sda`.

## Exercise

Prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da exploração de dispositivos de hardware no Linux:

1. **[Explorar Dispositivos de Hardware no Linux](https://labex.io/pt/labs/comptia-explore-hardware-devices-in-linux-590861)** - Pratique a identificação e inspeção de dispositivos de hardware em um ambiente Linux, de forma semelhante a como o sistema de arquivos `/sys` fornece informações sobre dispositivos.

Este laboratório ajudará você a aplicar os conceitos de compreensão do hardware do sistema e sua representação no Linux, aumentando a confiança na exploração de dispositivos.

## Quiz Question

Qual diretório é usado para visualizar informações detalhadas sobre dispositivos? Por favor, responda em inglês.

## Quiz Answer

/sys
