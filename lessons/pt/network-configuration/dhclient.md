---
index: 3
lang: "pt"
title: "dhclient"
meta_title: "dhclient - Configuração de Rede"
meta_description: "Aprenda sobre dhclient, como ele obtém endereços IP usando DHCP e gerencia concessões de rede. Entenda os arquivos dhclient.conf e dhclient.leases. Guia para iniciantes em Linux."
meta_keywords: "dhclient, DHCP, rede Linux, endereço IP, configuração de rede, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Já discutimos DHCP antes, e na maioria das vezes você nunca precisará definir estaticamente seus endereços IP, máscaras de sub-rede, etc. Em vez disso, você usará DHCP! O `dhclient` inicia na inicialização e obtém uma lista de interfaces de rede do arquivo `dhclient.conf`. Para cada interface listada, ele tenta configurar a interface usando o protocolo DHCP.

No arquivo `dhclient.leases`, o `dhclient` mantém um registro de uma lista de concessões entre as reinicializações do sistema. Depois de ler `dhclient.conf`, o arquivo `dhclient.leases` é lido para informá-lo sobre quais concessões ele já atribuiu.

### Para obter um IP novo

```bash
sudo dhclient
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre endereçamento IP dinâmico e configuração de rede:

1. **[Gerenciar Endereçamento IP no Linux](https://labex.io/pt/labs/linux-manage-ip-addressing-in-linux-592736)** - Pratique o uso de `dhclient` para obter um endereço IP dinâmico e verificar a configuração de rede em um ambiente Linux real.
2. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Aprenda a inspecionar interfaces de rede e identificar endereços MAC e IP, que são fundamentais para entender como o DHCP atribui endereços.
3. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Teste a acessibilidade da rede e explore diferentes tipos de endereço IP, aprofundando sua compreensão de como os endereços IP funcionam em uma rede.

Esses laboratórios o ajudarão a aplicar os conceitos de DHCP e endereçamento IP em cenários reais e a construir confiança com a configuração de rede no Linux.

## Quiz Question

O que tenta atribuir endereços IP com o protocolo DHCP?

## Quiz Answer

dhclient
