---
index: 5
lang: "pt"
title: "udev"
meta_title: "udev - Dispositivos"
meta_description: "Aprenda sobre udev, como ele gerencia dinamicamente arquivos de dispositivo Linux e use udevadm. Entenda a criação de nós de dispositivo para iniciantes."
meta_keywords: "udev, udevadm, gerenciamento de dispositivos Linux, arquivos de dispositivo, tutorial Linux, Linux para iniciantes, regras udev, guia Linux"
---

## Lesson Content

Antigamente, e na verdade hoje, se você realmente quisesse, criaria nós de dispositivo usando um comando como:

```bash
mknod /dev/sdb1 b 8 3
```

Este comando criará um nó de dispositivo `/dev/sdb1` e o tornará um dispositivo de bloco (b) com um número principal de 8 e um número secundário de 3.

Para remover um dispositivo, você simplesmente usaria o comando **rm** no arquivo do dispositivo no diretório `/dev`.

Felizmente, não precisamos mais fazer isso por causa do udev. O sistema udev cria e remove dinamicamente arquivos de dispositivo para nós, dependendo se eles estão conectados ou não. Existe um daemon `udevd` que está sendo executado no sistema e ele escuta as mensagens do kernel sobre os dispositivos conectados ao sistema. O `Udevd` analisará essas informações e corresponderá os dados às regras especificadas em `/etc/udev/rules.d`. Dependendo dessas regras, ele provavelmente criará nós de dispositivo e links simbólicos para os dispositivos. Você pode escrever suas próprias regras udev, mas isso está um pouco fora do escopo desta lição. Felizmente, seu sistema já vem com muitas regras udev, então você pode nunca precisar escrever as suas próprias.

Você também pode visualizar o banco de dados udev e o sysfs usando o comando **udevadm**. Esta ferramenta é muito útil, mas às vezes pode ficar muito complicada. Um comando simples para visualizar informações de um dispositivo seria:

```bash
udevadm info --query=all --name=/dev/sda
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da interação de hardware e gerenciamento de dispositivos no Linux:

1. **[Explorar Dispositivos de Hardware no Linux](https://labex.io/pt/labs/comptia-explore-hardware-devices-in-linux-590861)** - Neste laboratório, você aprenderá as habilidades essenciais para explorar, identificar e inspecionar dispositivos de hardware em um ambiente Linux. Você ganhará experiência prática com poderosas utilidades de linha de comando para entender como o sistema operacional interage com os componentes físicos, o que é crucial para entender os nós de dispositivo e o papel do udev.

Este laboratório o ajudará a aplicar os conceitos em cenários reais e a construir confiança com o gerenciamento de hardware Linux.

## Quiz Question

O que adiciona e remove dispositivos dinamicamente?

## Quiz Answer

udev
