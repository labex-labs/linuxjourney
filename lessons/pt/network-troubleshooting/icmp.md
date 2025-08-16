---
title: "ICMP"
description: "Aprenda sobre os conceitos básicos do protocolo ICMP, tipos de mensagens e códigos para solução de problemas de rede. Entenda como o ICMP funciona para depurar problemas de rede."
keywords: "ICMP, protocolo ICMP, solução de problemas de rede, tipos de ICMP, rede Linux, iniciante, tutorial, guia"
---

## Lesson Content

O Internet Control Message Protocol (ICMP) faz parte do pacote de protocolos TCP/IP. Ele é usado para enviar atualizações e mensagens de erro e é um protocolo extremamente útil para depurar problemas de rede, como falha na entrega de pacotes.

Cada mensagem ICMP contém um campo de tipo, código e checksum. O campo de tipo indica o tipo de mensagem ICMP, o código é um subtipo que fornece mais informações sobre a mensagem, e o checksum é usado para detectar quaisquer problemas com a integridade da mensagem.

Vamos ver alguns tipos comuns de ICMP:

- Type 0 - Echo Reply
- Type 3 - Destination Unreachable
- Type 8 - Echo Request
- Type 11 - Time Exceeded

Quando um pacote não consegue alcançar um destino, uma mensagem ICMP do Tipo 3 é gerada. Dentro do Tipo 3, existem 16 valores de código que descrevem ainda mais por que ele não consegue alcançar o destino:

- Code 0 - Network Unreachable
- Code 1 - Host Unreachable
  etc...etc...

Essas mensagens farão mais sentido à medida que usarmos algumas ferramentas de solução de problemas de rede.

## Exercise

No exercises for this lesson.

## Quiz Question

Qual é o tipo ICMP para uma solicitação de eco?

## Quiz Answer

8
