---
index: 1
lang: "pt"
title: "Interfaces de Rede"
meta_title: "Interfaces de Rede - Configuração de Rede"
meta_description: "Aprenda sobre interfaces de rede Linux, ifconfig e comandos ip. Entenda como configurar e gerenciar configurações de rede. Comece sua jornada de rede Linux!"
meta_keywords: "interfaces de rede Linux, ifconfig, comando ip, configuração de rede, rede Linux, iniciante, tutorial, guia"
---

## Lesson Content

Uma interface de rede é como o kernel conecta o lado do software da rede ao lado do hardware. Já vimos um exemplo disso:

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### O comando ifconfig

A ferramenta **ifconfig** nos permite configurar nossas interfaces de rede. Se não tivermos nenhuma interface de rede configurada, os drivers de dispositivo do kernel e a rede não saberão como se comunicar. O ifconfig é executado na inicialização e configura nossas interfaces através de arquivos de configuração, mas também podemos modificá-las manualmente. A saída do ifconfig mostra o nome da interface no lado esquerdo, e o lado direito mostra informações detalhadas. Você verá mais comumente interfaces nomeadas eth0 (primeira placa Ethernet na máquina), wlan0 (interface sem fio) e lo (interface de loopback). A interface de loopback é usada para representar seu computador; ela apenas o redireciona para si mesmo. Isso é bom para depuração ou para conectar-se a servidores em execução localmente.

O status das interfaces pode ser up ou down. Como você pode imaginar, se você quisesse "desligar" uma interface, você pode configurá-la para ficar down. Os campos que você provavelmente mais verá na saída do ifconfig são o HWaddr (endereço MAC da interface), inet address (endereço IPv4) e inet6 (endereço IPv6). Claro, você pode ver que a máscara de sub-rede e o endereço de broadcast também estão lá. Você também pode visualizar informações da interface em /etc/network/interfaces.

### Para criar uma interface e ativá-la

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

Isso atribui um endereço IP e netmask à interface eth0 e também a ativa.

### Para ativar ou desativar uma interface

```bash
ifup eth0
ifdown eth0
```

### O comando ip

O comando **ip** também nos permite manipular a pilha de rede de um sistema. Dependendo da distribuição que você está usando, pode ser o método preferido para manipular suas configurações de rede.

Aqui estão alguns exemplos de seu uso:

### Para mostrar informações de interface para todas as interfaces

```bash
ip link show
```

### Para mostrar as estatísticas de uma interface

```bash
ip -s link show eth0
```

### Para mostrar endereços IP alocados às interfaces

```bash
ip address show
```

### Para ativar e desativar interfaces

```bash
ip link set eth0 up
ip link set eth0 down
```

### Para adicionar um endereço IP a uma interface

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão das interfaces de rede e endereçamento IP:

1. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Pratique o uso do comando `ip a` para identificar informações de endereçamento de rede, incluindo endereços MAC, IPv4 e IPv6 em um sistema Linux.
2. **[Gerenciar Endereçamento IP no Linux](https://labex.io/pt/labs/linux-manage-ip-addressing-in-linux-592736)** - Aprenda a configurar endereços IP estáticos e dinâmicos, definir um gateway padrão e verificar configurações de rede usando o comando `ip`.
3. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore diferentes tipos de endereço IP (privado, público, multicast) e teste a acessibilidade da rede usando `ping` e `ip a`.

Esses laboratórios o ajudarão a aplicar os conceitos de identificação de interface de rede e endereçamento IP em cenários reais e a construir confiança com redes Linux.

## Quiz Question

Qual é o comando para configurar nossas interfaces de rede?

## Quiz Answer

ifconfig
