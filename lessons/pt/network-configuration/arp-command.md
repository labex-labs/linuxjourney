---
lang: "pt"
title: "arp"
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
4. O host de origem adiciona o mapeamento de IP para endereço MAC ao cache ARP e, em seguida, prossegue com o envio do pacote.

Você também pode visualizar seu cache ARP através do comando `ip`:

```bash
ip neighbour show
```

## Exercise

Observe o que acontece com o seu cache ARP quando você reinicia sua máquina e depois faz algo na rede.

## Quiz Question

Qual comando você pode usar para visualizar seu cache ARP?

## Quiz Answer

arp
