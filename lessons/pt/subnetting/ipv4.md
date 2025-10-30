---
index: 1
lang: "pt"
title: "IPv4"
meta_title: "IPv4 - Sub-redes"
meta_description: "Descubra a melhor forma de aprender redes Linux entendendo endereços IPv4. Este guia para iniciantes cobre a estrutura de IP e como encontrar seu IP usando a linha de comando."
meta_keywords: "IPv4, endereço IP, linux iniciante, melhor forma de aprender linux, linha de comando linux para iniciantes, ifconfig, ip addr, noções básicas de rede"
---

## Lesson Content

Todo dispositivo conectado a uma rede possui um endereço exclusivo, conhecido como endereço IP (Protocolo de Internet). Para este curso, focaremos nos endereços IPv4, que são o tipo mais comum que você encontrará. Entendê-los é uma parte central do aprendizado de redes no Linux.

Um endereço IPv4 é um número de 32 bits normalmente representado em um formato legível por humanos, como este:

```
204.23.124.23
```

Este endereço contém duas partes distintas: a porção de **rede**, que identifica a rede específica em que o dispositivo está, e a porção de **host**, que identifica o dispositivo específico nessa rede.

### A Estrutura de um Endereço IP

Um endereço IPv4 é dividido em quatro seções separadas por pontos. Cada seção é chamada de **octeto**. Em ciência da computação, um octeto é um grupo de 8 bits, e como 8 bits equivalem a 1 byte, um endereço IPv4 tem 4 bytes de comprimento. Essa estrutura é fundamental, e dominá-la é um dos `melhores recursos para aprender a linha de comando linux para iniciantes` em redes.

### Encontrando Seu Endereço IP no Linux

Para qualquer usuário `linux iniciante`, uma das primeiras tarefas é encontrar o endereço IP do sistema. Você pode fazer isso usando ferramentas de linha de comando.

O comando tradicional para isso é `ifconfig`. Embora ainda seja encontrado em muitos sistemas, é considerado uma ferramenta legada.

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

Na saída acima, o endereço IPv4 é `192.168.1.129`.

### A Abordagem Moderna com ip addr

A `melhor maneira de aprender` redes no Linux hoje envolve o uso do comando moderno `ip`. O comando `ip addr` substituiu o `ifconfig` e é o padrão na maioria das distribuições Linux atuais.

```bash
pete@icebox:~$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 1d:3a:32:24:4d:ce brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.129/24 brd 192.168.1.255 scope global dynamic eth0
       valid_lft 85646sec preferred_lft 85646sec
```

Aqui, você pode encontrar o mesmo endereço IPv4, `192.168.1.129`, listado ao lado de `inet` para a interface `eth0`.

## Exercise

Pratique suas habilidades com estes laboratórios práticos para reforçar sua compreensão de endereçamento IP e identificação de rede no Linux:

1. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Pratique o uso do comando `ip a` para identificar informações de endereçamento de rede, incluindo endereços IPv4 e IPv6, em um sistema Linux.
2. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore diferentes tipos de endereços IP e teste a acessibilidade da rede usando comandos como `ping` e `ip a`.
3. **[Realizar Sub-redes IP e Conversão Binária no Terminal Linux](https://labex.io/pt/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine a sub-rede IP e a conversão binária, essenciais para uma compreensão mais profunda de como os endereços IP e as redes são estruturados no nível de bit.

Estes laboratórios ajudarão você a aplicar os conceitos de endereçamento IP em cenários reais e a construir confiança na configuração e solução de problemas de rede no Linux.

## Quiz Question

Quantos bytes há em um endereço IPv4?

## Quiz Answer

4
