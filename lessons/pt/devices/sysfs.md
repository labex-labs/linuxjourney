---
title: "sysfs"
description: "Aprenda sobre sysfs, um sistema de arquivos virtual para informações e gerenciamento detalhados de dispositivos Linux. Entenda /sys vs /dev. Comece sua jornada no Linux!"
keywords: "sysfs, diretório /sys, dispositivos Linux, sistema de arquivos virtual, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Sysfs foi criado há muito tempo para gerenciar melhor os dispositivos em nosso sistema, uma tarefa que o diretório `/dev` não conseguiu realizar adequadamente. Sysfs é um sistema de arquivos virtual, na maioria das vezes montado no diretório `/sys`. Ele nos fornece informações mais detalhadas do que seríamos capazes de ver no diretório `/dev`. Ambos os diretórios, `/sys` e `/dev`, parecem muito semelhantes e são em alguns aspectos, mas eles têm grandes diferenças. Basicamente, o diretório `/dev` é simples; ele permite que outros programas acessem os próprios dispositivos, enquanto o sistema de arquivos `/sys` é usado para visualizar informações e gerenciar o dispositivo.

O sistema de arquivos `/sys` basicamente contém todas as informações para todos os dispositivos em seu sistema, como o fabricante e o modelo, onde o dispositivo está conectado, o estado do dispositivo, a hierarquia dos dispositivos e muito mais. Os arquivos que você vê aqui não são nós de dispositivo, então você realmente não interage com dispositivos a partir do diretório `/sys`; em vez disso, você está gerenciando dispositivos.

Veja o conteúdo do diretório `/sys`:

```bash
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
```

## Exercise

Verifique o conteúdo do diretório `/sys` e veja quais arquivos estão localizados lá.

## Quiz Question

Qual diretório é usado para visualizar informações detalhadas sobre dispositivos?

## Quiz Answer

/sys
