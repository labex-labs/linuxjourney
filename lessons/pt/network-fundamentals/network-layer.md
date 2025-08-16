---
title: "Camada de Rede"
description: "Aprenda sobre a camada de Rede no Linux, como os endereços IP roteiam pacotes entre sub-redes e seu papel na transmissão de dados. Comece sua jornada de rede Linux!"
keywords: "Camada de rede, endereços IP, sub-redes, rede Linux, roteamento de pacotes, iniciante, tutorial, guia"
---

## Lesson Content

A camada de Rede determina o roteamento dos nossos pacotes do nosso host de origem para um host de destino. Felizmente, no nosso exemplo, o nosso pacote está a viajar apenas dentro da mesma rede, mas a Internet é composta por muitas redes. Estas redes mais pequenas que compõem a Internet são conhecidas como subnets. Todas as subnets ligam-se umas às outras de alguma forma, razão pela qual conseguimos aceder a <https://www.google.com> mesmo estando na sua própria rede. Não entrarei em detalhes, pois temos um curso inteiro dedicado a subnets, mas por agora, no que diz respeito à nossa camada de Rede, saiba que os IP addresses definem as regras para viajar para diferentes subnets.

Na camada de Rede, ela recebe o segmento vindo da camada de Transporte e encapsula este segmento num IP packet, depois anexa o IP address do host de origem e o IP address do host de destino ao packet header. Assim, neste ponto, o nosso pacote tem informações sobre para onde vai e de onde veio. Agora ele envia o nosso pacote para a camada de hardware físico.

## Exercise

No exercises for this lesson.

## Quiz Question

Como são chamadas as redes menores que compõem a Internet?

## Quiz Answer

subnets
