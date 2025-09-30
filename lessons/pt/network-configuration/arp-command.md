---
index: 5
lang: "pt"
title: "arp"
meta_title: "arp - Configuração de Rede"
meta_description: "Aprenda sobre o comando ARP do Linux e como visualizar seu cache ARP. Entenda o papel do ARP na comunicação de rede. Um guia para iniciantes em ARP."
meta_keywords: "Linux ARP, cache ARP, ip neighbour show, comandos de rede, rede Linux, Linux para iniciantes, tutorial Linux"
---

## Lesson Content

Lembre-se que quando procuramos um endereço MAC com ARP, ele primeiro verifica o cache ARP armazenado localmente em nosso sistema. Você pode realmente visualizar este cache:

```
pete@icebox:~$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.22.1            ether   00:12:24:fc:12:cc   C                     eth0
192.168.22.254          ether   00:12:45:f2:84:64   C                     eth0
```

O cache ARP está realmente vazio quando uma máquina inicializa; ele é preenchido à medida que os pacotes são enviados para outros hosts. Se enviarmos um pacote para um destino que não está no cache ARP, o seguinte acontece:

1. O host de origem cria o quadro Ethernet com um pacote de solicitação ARP.
2. O host de origem transmite este quadro para toda a rede.
3. Se um dos hosts na rede souber o endereço MAC correto, ele enviará um pacote de resposta e um quadro contendo o endereço MAC.
4. O host de origem adiciona o mapeamento de IP para endereço MAC ao cache ARP e então prossegue com o envio do pacote.

Você também pode visualizar seu cache ARP através do comando `ip`:

```bash
ip neighbour show
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de ARP e interação da camada de rede:

1. **[Explore a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Use os comandos `ping` e `arp` para observar como os endereços IP são resolvidos para endereços MAC e como o gateway padrão lida com o tráfego.
2. **[Identifique Endereços MAC e IP no Linux](https://labex.io/pt/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Aprenda a usar o comando `ip a` para identificar informações de endereçamento de rede, incluindo endereços MAC e IP, que são fundamentais para entender o ARP.
3. **[Gerencie o Endereçamento IP no Linux](https://labex.io/pt/labs/comptia-manage-ip-addressing-in-linux-592736)** - Pratique o gerenciamento de endereçamento IP usando o comando `ip` e verifique a configuração de rede com `arp` e `traceroute`.

Esses laboratórios o ajudarão a aplicar os conceitos de ARP e endereçamento de rede em cenários reais e a construir confiança com a rede Linux.

## Quiz Question

Qual comando você pode usar para visualizar seu cache ARP?

## Quiz Answer

arp
