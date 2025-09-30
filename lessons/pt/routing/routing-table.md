---
index: 2
lang: "pt"
title: "Tabela de Roteamento"
meta_title: "Tabela de Roteamento - Roteamento"
meta_description: "Aprenda a entender a tabela de roteamento do Linux e como os pacotes são roteados usando o comando route. Explore destinos, gateways e interfaces para os fundamentos de rede."
meta_keywords: "tabela de roteamento Linux, comando route, roteamento de rede, rede Linux, Linux para iniciantes, tutorial Linux, guia de rede"
---

## Lesson Content

Observe a tabela de roteamento da sua máquina:

```plaintext
pete@icebox:~$ sudo route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
```

### Destino

No primeiro campo, temos um endereço IP de destino de 192.168.224.0. Isso significa que qualquer pacote que tente ir para esta rede sai pelo meu cabo Ethernet (eth0). Se eu fosse 192.168.224.5 e quisesse chegar a 192.168.224.7, eu usaria a interface de rede eth0 diretamente.

Observe que temos endereços de **0.0.0.0**. Isso significa que nenhum endereço é especificado ou é desconhecido. Então, se, por exemplo, eu quisesse enviar um pacote para o endereço IP 151.123.43.6, nossa tabela de roteamento não sabe para onde ele vai, então ela o denota como 0.0.0.0 e, portanto, roteia nosso pacote para o Gateway.

### Gateway

Se estivermos enviando um pacote que não está na mesma rede, ele será enviado para este endereço de Gateway, que é apropriadamente nomeado como um Gateway para outra rede.

### Genmask

Esta é a máscara de sub-rede, usada para descobrir quais endereços IP correspondem a qual destino.

### Flags

- UG - A rede está ativa (Up) e é um Gateway
- U - A rede está ativa (Up)

### Iface

Esta é a interface pela qual nosso pacote sairá. eth0 geralmente significa o primeiro dispositivo Ethernet em seu sistema.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre roteamento de rede e endereçamento IP:

1. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Pratique o uso do comando `ip a` para identificar informações de endereçamento de rede, incluindo endereços IP e interfaces de rede, que são componentes chave de uma tabela de roteamento.
2. **[Gerenciar Endereçamento IP no Linux](https://labex.io/pt/labs/comptia-manage-ip-addressing-in-linux-592736)** - Aprenda a gerenciar o endereçamento IP, configurar IPs estáticos, definir gateways padrão e verificar configurações de rede, diretamente relacionados às entradas encontradas em uma tabela de roteamento.
3. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore o endereçamento IP e a acessibilidade da rede usando `ping` e `ip a`, ajudando você a entender como diferentes tipos de IP interagem e como a acessibilidade da rede é determinada, o que se reflete nas decisões de roteamento.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com a configuração e solução de problemas de rede.

## Quiz Question

Para onde os pacotes são roteados se nossa tabela de roteamento não souber?

## Quiz Answer

Gateway
