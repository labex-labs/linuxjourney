---
index: 2
lang: "pt"
title: "Sub-redes"
meta_title: "Sub-redes - Subnetting"
meta_description: "Aprenda sobre sub-redes e máscaras de sub-rede em redes Linux. Entenda os prefixos de rede e como as sub-redes segmentam o tráfego. Comece com este guia amigável para iniciantes!"
meta_keywords: "sub-redes, máscara de sub-rede, prefixo de rede, redes Linux, endereço IP, iniciante, tutorial, ifconfig"
---

## Lesson Content

Como posso saber se estou na mesma rede que a Patty? Bem, podemos simplesmente olhar para a sub-rede, abreviação de subnetwork. Uma sub-rede é um grupo de hosts com endereços IP que são semelhantes de uma certa forma. Esses hosts geralmente estão em um local próximo um do outro, e você pode facilmente enviar dados para e de hosts na mesma sub-rede. Pense nisso como enviar correspondência no mesmo CEP; é muito mais fácil do que enviar correspondência para um estado diferente.

Por exemplo, todos os hosts com um endereço IP que começa com 123.45.67 estariam na mesma sub-rede. Meu host tem um IP de 123.45.67.8, e o da Patty tem um IP de 123.45.67.9. Os números comuns são meu prefixo de rede, e o 8 e o 9 são nossos hosts; portanto, minha rede é a mesma que a da Patty. Uma sub-rede é dividida em um prefixo de rede, como 123.45.67.0, e uma máscara de sub-rede.

### Máscaras de Sub-rede

Máscaras de sub-rede determinam qual parte do seu endereço IP é a porção de rede e qual parte é a porção de host.

Uma máscara de sub-rede típica pode ser algo assim:

```plaintext
255.255.255.0
```

A porção 255 é na verdade nossa máscara. Para tornar isso um pouco mais fácil de entender, lembre-se de como nos referimos a cada octeto como 8 bits? Em ciência da computação, um bit é denotado por um 0 ou um 1 na forma binária. Quando números binários são usados, 1 significa ligado e 0 significa desligado. Então, o que 8 0's ou 1's equivalem?

Digite no Google "calculadora binário para decimal" e converta 11111111 para a forma decimal. O que você obtém? 255! Então um octeto varia de 0 a 255. Então, se tivéssemos uma máscara de sub-rede de 255.255.255.0, e um endereço IP de 192.168.1.0, quantos hosts estão nessa sub-rede? Descobriremos a resposta para isso em nossa lição de matemática de sub-rede.

Além disso, quando falamos sobre nossa sub-rede, geralmente a denotamos pelo prefixo de rede seguido pela máscara de sub-rede:

```plaintext
123.234.0.0/255.255.0.0
```

### Por que?

Por que diabos fazemos sub-redes? O subnetting é usado para segmentar redes e controlar o fluxo de tráfego dentro dessa rede. Assim, um host em uma sub-rede não pode interagir com outro host em uma sub-rede diferente.

Mas espere um minuto, e se eu quiser me conectar a outros hosts como yahoo.com? Então você precisa conectar sub-redes. Para conectar sub-redes, você só precisa encontrar os hosts que estão conectados a mais de uma sub-rede. Por exemplo, se meu host em 192.168.1.129 estiver conectado a uma rede local de 192.168.1.129/24, ele pode alcançar qualquer host nessa rede. Para alcançar hosts no resto da Internet, ele precisa se comunicar através do roteador. Tradicionalmente, na maioria das redes com uma máscara de sub-rede de 255.255.255.0, o roteador geralmente está no endereço 1 da sub-rede, então 192.168.1.1. Agora, esse roteador terá uma porta que o conecta a outra sub-rede (mais no curso de Roteamento). Certos endereços IP (redes privadas) não são visíveis para a internet, e temos coisas como NAT em vigor (mais sobre isso depois).

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de endereçamento IP e subnetting:

1. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Pratique o uso do comando `ip a` para identificar informações de endereçamento de rede, incluindo endereços IPv4, o que é fundamental para entender sub-redes.
2. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Aprenda a explorar diferentes tipos de endereço IP e testar a acessibilidade da rede, ajudando você a verificar se os hosts estão na mesma rede.
3. **[Realizar Subnetting IP e Conversão Binária no Terminal Linux](https://labex.io/pt/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine o subnetting IP e a conversão binária, aplicando diretamente os conceitos de prefixos de rede e identificação de host discutidos na lição.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com endereçamento de rede e subnetting.

## Quiz Question

Verdadeiro ou falso, uma sub-rede consiste em uma máscara de sub-rede e um prefixo de rede.

## Quiz Answer

True
