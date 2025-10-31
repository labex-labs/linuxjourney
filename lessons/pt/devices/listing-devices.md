---
index: 6
lang: "pt"
title: "lsusb, lspci, lssci"
meta_title: "lsusb, lspci, lssci - Dispositivos"
meta_description: "Descubra como listar e inspecionar hardware USB, PCI e SCSI no seu sistema Linux. Este guia abrange os comandos lsusb, lspci e lssci, incluindo opções como lsusb -t para ver árvores de dispositivos."
meta_keywords: "lsusb, lspci, lssci, lsusb -t, listar dispositivos usb, listar dispositivos pci, listar dispositivos scsi, hardware linux, informação de dispositivo"
---

## Lesson Content

Assim como você usa o comando `ls` para listar arquivos, o Linux fornece ferramentas semelhantes para listar dispositivos de hardware. Esses comandos são essenciais para identificar o hardware conectado ao seu sistema.

### Listando Dispositivos USB com lsusb

Para ver todos os dispositivos USB conectados ao seu sistema, você pode usar o comando `lsusb`. Este comando escaneia os hubs USB e relata informações sobre os dispositivos que encontra, como webcams, teclados e unidades externas.

```bash
lsusb
```

Para uma visualização mais estruturada, você pode usar o comando `lsusb -t`. Esta opção exibe os dispositivos USB em uma estrutura semelhante a uma árvore, o que é útil para entender como os dispositivos estão fisicamente conectados aos controladores e hubs USB.

### Listando Dispositivos PCI com lspci

O comando `lspci` é usado para listar todos os dispositivos PCI (Peripheral Component Interconnect). Estes são tipicamente componentes internos conectados à placa-mãe, como placas gráficas, adaptadores de rede e placas de som. Este comando fornece uma visão geral rápida do hardware principal do seu sistema.

```bash
lspci
```

### Listando Dispositivos SCSI e SATA com lssci

Para dispositivos de armazenamento, o comando `lssci` é particularmente útil. Ele lista todos os dispositivos SCSI e SATA conectados, que comumente incluem discos rígidos, SSDs e unidades ópticas (CD/DVD/Blu-ray). Embora outros comandos possam mostrar o controlador de armazenamento, o `lssci` fornece informações diretas sobre os próprios dispositivos de armazenamento, tornando-o uma ferramenta valiosa para administradores de sistema e usuários que gerenciam armazenamento.

```bash
lssci
```

## Exercise

Para reforçar sua compreensão sobre a exploração de dispositivos de hardware no Linux, experimente o seguinte laboratório prático:

1.  **[Explorar Dispositivos de Hardware no Linux](https://labex.io/pt/labs/comptia-explore-hardware-devices-in-linux-590861)** - Neste laboratório, você aprenderá as habilidades essenciais para explorar, identificar e inspecionar dispositivos de hardware dentro de um ambiente Linux. Você ganhará experiência prática com utilitários poderosos de linha de comando para entender como o sistema operacional interage com componentes físicos.

Este laboratório ajudará você a aplicar esses conceitos em um cenário do mundo real e a ganhar confiança no gerenciamento de informações de dispositivos.

## Quiz Question

Qual comando é usado para visualizar uma lista de dispositivos USB conectados? (Por favor, responda apenas com caracteres em inglês minúsculos.)

## Quiz Answer

lsusb
