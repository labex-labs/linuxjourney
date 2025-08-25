---
index: 4
lang: "pt"
title: "Endereçamento de Rede"
meta_title: "Endereçamento de Rede - Fundamentos de Rede"
meta_description: "Aprenda os conceitos básicos de endereçamento de rede: endereços MAC vs. IP e nomes de host. Entenda como os dispositivos se comunicam em uma rede. Comece sua jornada de rede Linux!"
meta_keywords: "endereçamento de rede, endereço MAC, endereço IP, nome de host, rede Linux, iniciante, tutorial, guia"
---

## Lesson Content

Antes de mergulharmos em como um pacote se move através de uma rede, precisamos nos familiarizar com algumas terminologias. Quando você envia uma carta, você deve saber para quem ela está sendo enviada e de onde ela está vindo. Os pacotes precisam da mesma informação. Nossos hosts e outros hosts são identificados usando endereços MAC (Media Access Control) e endereços IP. Para facilitar para nós, humanos, usamos nomes de host para identificar um host.

### Endereços MAC

Um endereço MAC é um identificador único usado como um endereço de hardware. Este endereço nunca mudará. Quando você quer ter acesso à Internet, sua máquina precisa ter um dispositivo chamado placa de interface de rede. Este adaptador de rede tem seu próprio endereço de hardware que é usado para identificar sua máquina. Um endereço MAC para um dispositivo Ethernet se parece com isto: `00:C4:B5:45:B2:43`. Os endereços MAC são atribuídos aos adaptadores de rede quando são fabricados. Cada fabricante tem um Identificador Único de Organização (OUI) para identificá-los como o fabricante. Este OUI é denotado pelos primeiros 3 bytes do endereço MAC. Por exemplo, a Dell tem `00-14-22`, então um adaptador de rede da Dell poderia ter um endereço MAC como: `00-14-22-34-B2-C2`.

### Endereços IP

Um endereço IP é usado para identificar um dispositivo em uma rede. Eles são independentes de hardware e podem variar na sintaxe dependendo se você está usando IPv4 ou IPv6 (mais sobre isso depois). Por enquanto, vamos assumir que você está usando IPv4, então um endereço IP típico seria parecido com: `10.24.12.4`. Os endereços IP são usados com o lado do software da rede. Sempre que um sistema está conectado à Internet, ele deve ter um endereço IP. Eles também podem mudar se sua rede mudar e são únicos para toda a Internet (isso nem sempre é o caso quando aprendemos sobre NAT).

Lembre-se, são necessários tanto software quanto hardware para mover pacotes através de redes, então temos dois identificadores para cada um: MAC (hardware) e IP (software).

### Nomes de Host

Uma última maneira de identificar suas máquinas é através de nomes de host. Os nomes de host pegam seu endereço IP e permitem que você vincule esse endereço a um nome legível por humanos. Em vez de lembrar `192.12.41.4`, você pode simplesmente lembrar `myhost.com`.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão dos identificadores de rede, como endereços MAC, endereços IP e nomes de host:

1. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Pratique o uso do comando `ip a` para identificar informações de endereçamento de rede, incluindo endereços MAC e IP, em um sistema Linux.
2. **[Explorar Tipos de Endereços IP e Acessibilidade no Linux](https://labex.io/pt/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore diferentes tipos de endereços IP e teste a acessibilidade da rede usando `ping` e `ip a`.
3. **[Gerenciar Resolução de Nome de Host Local no Linux](https://labex.io/pt/labs/linux-manage-local-hostname-resolution-in-linux-592792)** - Aprenda a gerenciar a resolução de nome de host local editando o arquivo `/etc/hosts` e testando suas alterações.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com os fundamentos de rede do Linux.

## Quiz Question

Quantos bytes existem em um endereço IPv4?

## Quiz Answer

4
