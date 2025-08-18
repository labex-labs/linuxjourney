---
index: 3
lang: "pt"
title: "dhclient"
meta_title: "dhclient - Configuração de Rede"
meta_description: "Aprenda sobre o dhclient, como ele obtém endereços IP usando DHCP e gerencia concessões de rede. Entenda os arquivos dhclient.conf e dhclient.leases. Guia para iniciantes em Linux."
meta_keywords: "dhclient, DHCP, rede Linux, endereço IP, configuração de rede, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Já discutimos DHCP antes, e na maioria das vezes você nunca precisará definir estaticamente seus endereços IP, máscaras de sub-rede, etc. Em vez disso, você estará usando DHCP! O `dhclient` inicia na inicialização e obtém uma lista de interfaces de rede do arquivo `dhclient.conf`. Para cada interface listada, ele tenta configurar a interface usando o protocolo DHCP.

No arquivo `dhclient.leases`, o `dhclient` mantém um registro de uma lista de concessões entre as reinicializações do sistema. Depois de ler `dhclient.conf`, o arquivo `dhclient.leases` é lido para informá-lo sobre quais concessões ele já atribuiu.

### Para obter um IP novo

```bash
sudo dhclient
```

## Exercise

No exercises for this lesson.

## Quiz Question

O que tenta atribuir endereços IP com o protocolo DHCP?

## Quiz Answer

dhclient
