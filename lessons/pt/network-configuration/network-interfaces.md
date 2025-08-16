---
title: "Interfaces de Rede"
description: "Aprenda sobre interfaces de rede Linux, ifconfig e comandos ip. Entenda como configurar e gerenciar configurações de rede. Comece sua jornada de rede Linux!"
keywords: "interfaces de rede Linux, ifconfig, comando ip, configuração de rede, rede Linux, iniciante, tutorial, guia"
---

## Lesson Content

Uma interface de rede é como o kernel conecta o lado do software da rede ao lado do hardware. Já vimos um exemplo disso:

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### The ifconfig command

A ferramenta **ifconfig** nos permite configurar nossas interfaces de rede. Se não tivermos nenhuma interface de rede configurada, os drivers de dispositivo do kernel e a rede não saberão como se comunicar. O ifconfig é executado na inicialização e configura nossas interfaces através de arquivos de configuração, mas também podemos modificá-los manualmente. A saída do ifconfig mostra o nome da interface no lado esquerdo, e o lado direito mostra informações detalhadas. Você verá mais comumente interfaces nomeadas eth0 (primeira placa Ethernet na máquina), wlan0 (interface sem fio) e lo (interface de loopback). A interface de loopback é usada para representar seu computador; ela apenas o "loopa" de volta para você mesmo. Isso é bom para depuração ou para conectar-se a servidores em execução localmente.

O status das interfaces pode ser up ou down. Como você pode imaginar, se você quisesse "desligar" uma interface, você pode configurá-la para down. Os campos que você provavelmente mais verá na saída do ifconfig são o HWaddr (endereço MAC da interface), inet address (endereço IPv4) e inet6 (endereço IPv6). Claro, você pode ver que a máscara de sub-rede e o endereço de broadcast também estão lá. Você também pode visualizar informações da interface em /etc/network/interfaces.

### To create an interface and bring it up

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

Isso atribui um endereço IP e netmask à interface eth0 e também a ativa.

### To bring up or down an interface

```bash
ifup eth0
ifdown eth0
```

### The ip command

O comando **ip** também nos permite manipular a pilha de rede de um sistema. Dependendo da distribuição que você está usando, pode ser o método preferido para manipular suas configurações de rede.

Aqui estão alguns exemplos de seu uso:

### To show interface information for all interfaces

```bash
ip link show
```

### To show the statistics of an interface

```bash
ip -s link show eth0
```

### To show IP addresses allocated to interfaces

```bash
ip address show
```

### To bring interfaces up and down

```bash
ip link set eth0 up
ip link set eth0 down
```

### To add an IP address to an interface

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

Experimente mudar o estado de suas interfaces de rede para up ou down e observe o que acontece.

Você consegue mudar suas interfaces de rede com os comandos ifconfig e ip?

## Quiz Question

Qual é o comando para configurar nossas interfaces de rede?

## Quiz Answer

ifconfig
