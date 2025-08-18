---
lang: "pt"
title: "Subnets"
meta_title: "Subnets - Subnetting"
meta_description: "Aprenda sobre subnets e subnet masks em redes Linux. Entenda os prefixos de rede e como as subnets segmentam o tráfego. Comece com este guia amigável para iniciantes!"
meta_keywords: "subnets, subnet mask, network prefix, Linux networking, IP address, iniciante, tutorial, ifconfig"
---

## Lesson Content

Como posso saber se estou na mesma rede que a Patty? Bem, podemos simplesmente olhar para a subnet, abreviação de sub-rede. Uma subnet é um grupo de hosts com endereços IP que são semelhantes de uma certa forma. Esses hosts geralmente estão em uma localização próxima uns dos outros, e você pode facilmente enviar dados para e de hosts na mesma subnet. Pense nisso como enviar correspondência no mesmo CEP; é muito mais fácil do que enviar correspondência para um estado diferente.

Por exemplo, todos os hosts com um endereço IP que começa com 123.45.67 estariam na mesma subnet. Meu host tem um IP de 123.45.67.8, e o da Patty tem um IP de 123.45.67.9. Os números comuns são meu network prefix, e o 8 e o 9 são nossos hosts; portanto, minha rede é a mesma que a da Patty. Uma subnet é dividida em um network prefix, como 123.45.67.0, e uma subnet mask.

### Subnet Masks

Subnet masks determinam qual parte do seu endereço IP é a porção de rede e qual parte é a porção de host.

Uma subnet mask típica pode ser algo assim:

```plaintext
255.255.255.0
```

A porção 255 é na verdade nossa mask. Para tornar isso um pouco mais fácil de entender, lembre-se de como nos referimos a cada octeto como 8 bits? Em ciência da computação, um bit é denotado por um 0 ou um 1 na forma binária. Quando números binários são usados, 1 significa ligado e 0 significa desligado. Então, o que 8 0s ou 1s equivalem?

Digite no Google "calculadora binário para decimal" e converta 11111111 para a forma decimal. O que você obtém? 255! Então, um octeto varia de 0 a 255. Então, se tivéssemos uma subnet mask de 255.255.255.0, e um endereço IP de 192.168.1.0, quantos hosts estão nessa subnet? Descobriremos a resposta para isso em nossa lição de matemática de subnet.

Além disso, quando falamos sobre nossa subnet, geralmente a denotamos pelo network prefix seguido pela subnet mask:

```plaintext
123.234.0.0/255.255.0.0
```

### Por quê?

Por que diabos fazemos subnets? O subnetting é usado para segmentar redes e controlar o fluxo de tráfego dentro dessa rede. Assim, um host em uma subnet não pode interagir com outro host em uma subnet diferente.

Mas espere um minuto, e se eu quiser me conectar a outros hosts como yahoo.com? Então você precisa conectar subnets. Para conectar subnets, você só precisa encontrar os hosts que estão conectados a mais de uma subnet. Por exemplo, se meu host em 192.168.1.129 estiver conectado a uma rede local de 192.168.1.129/24, ele pode alcançar quaisquer hosts nessa rede. Para alcançar hosts no resto da Internet, ele precisa se comunicar através do router. Tradicionalmente, na maioria das redes com uma subnet mask de 255.255.255.0, o router geralmente está no endereço 1 da subnet, então 192.168.1.1. Agora, esse router terá uma porta que o conecta a outra subnet (mais no curso de Roteamento). Certos endereços IP (redes privadas) não são visíveis para a internet, e temos coisas como NAT em vigor (mais sobre isso depois).

## Exercise

Use `ifconfig` para visualizar sua subnet mask.

## Quiz Question

Verdadeiro ou falso, uma subnet consiste em uma subnet mask e um network prefix.

## Quiz Answer

True
