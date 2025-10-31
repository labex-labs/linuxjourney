---
index: 1
lang: "pt"
title: "IPv4"
meta_title: "IPv4 - Sub-redes"
meta_description: "Comece sua jornada com nosso tutorial completo de Linux sobre endereços IPv4. Este guia para usuários iniciantes de Linux é a melhor forma de aprender redes Linux, cobrindo estrutura de IP e ferramentas essenciais de linha de comando como ip addr."
meta_keywords: "IPv4, endereço IP, linux para iniciantes, melhor forma de aprender linux, tutorial completo de linux, melhor curso de linux online grátis, cursos de certificação linux grátis, redes linux, ifconfig, ip addr"
---

## Lesson Content

Todo dispositivo em uma rede possui um identificador exclusivo chamado endereço IP (Internet Protocol). Esta lição, uma parte fundamental do nosso `tutorial completo de linux`, foca nos endereços IPv4 — o tipo mais comum que você encontrará. Para qualquer usuário `linux iniciante`, entender o IPv4 é um primeiro passo crítico no mundo das redes.

### Por que o IPv4 é Essencial

Aprender sobre IPv4 é fundamental para quem leva a sério a administração de sistemas ou gerenciamento de redes. Ele forma a espinha dorsal da maior parte da comunicação em rede. Este guia oferece a `melhor maneira de aprender linux` networking do zero. Embora este não seja um daqueles `cursos de certificação linux gratuitos`, dominar esses conceitos básicos é um passo chave em direção à certificação profissional.

### Estrutura do Endereço IPv4

Um endereço IPv4 é um número de 32 bits, mas geralmente é exibido em um formato legível por humanos como este:

```
204.23.124.23
```

Este endereço tem duas partes principais: a **porção de rede**, que identifica a rede, e a **porção de host**, que identifica o dispositivo específico nessa rede. O endereço é dividido em quatro seções separadas por pontos, sendo cada seção chamada de **octeto**. Um octeto é um grupo de 8 bits, o que significa que um endereço IPv4 tem 4 bytes (32 bits) de comprimento. Entender essa estrutura é crucial para a configuração e solução de problemas de rede.

### Encontrando Seu Endereço IP

Uma das primeiras tarefas para qualquer usuário Linux é encontrar o endereço IP do seu sistema. Você pode fazer isso usando ferramentas simples de linha de comando. O comando tradicional para isso é o `ifconfig`. Embora ainda seja encontrado em muitos sistemas, ele é considerado uma ferramenta legada.

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

Na saída acima, o endereço IPv4 é `192.168.1.129`.

### Usando o Comando ip addr

O método moderno e recomendado usa o comando `ip`. O comando `ip addr` substituiu o `ifconfig` e é o padrão na maioria das distribuições Linux atuais. Ele fornece informações mais detalhadas e é a ferramenta na qual você deve focar em aprender.

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
3. **[Realizar Sub-redes IP e Conversão Binária no Terminal Linux](https://labex.io/pt/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine a sub-rede IP e a conversão binária, essenciais para uma compreensão mais profunda de como os endereços e redes IP são estruturados no nível de bit.

Estes laboratórios ajudarão você a aplicar os conceitos de endereçamento IP em cenários reais e a construir confiança com a configuração e solução de problemas de rede no Linux.

## Quiz Question

Quantos bytes há em um endereço IPv4?

## Quiz Answer

4
