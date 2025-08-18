---
lang: "pt"
title: "Camada de Transporte"
meta_description: "Aprenda sobre a Camada de Transporte em redes Linux, incluindo protocolos TCP/UDP, portas e segmentação de dados. Entenda como os dados são transferidos de forma confiável."
meta_keywords: "Camada de Transporte Linux, TCP/UDP, portas de rede, segmentação de dados, redes Linux, tutorial para iniciantes, protocolos de rede"
---

## Lesson Content

A camada de transporte nos ajuda a transferir nossos dados de uma forma que as redes possam lê-los. Ela divide nossos dados em blocos que serão transportados e remontados na ordem correta. Esses blocos são conhecidos como segmentos. Os segmentos facilitam o transporte de dados através das redes.

### Ports

Mesmo sabendo para onde estamos enviando nossos dados via endereços IP, eles não são específicos o suficiente para enviar nossos dados para determinados processos ou serviços. Serviços como HTTP usam um canal de comunicação via portas. Se quisermos enviar dados de página da web, precisamos enviá-los pela porta HTTP (porta 80). Além de formar segmentos, a camada de transporte também anexará as portas de origem e destino ao segmento, para que, quando o receptor receber o pacote final, saiba qual porta usar.

### UDP

Existem dois protocolos de transporte populares: UDP e TCP. Discutiremos brevemente o UDP e passaremos a maior parte do tempo no TCP, já que é o mais comumente usado.

UDP não é um método confiável de transporte de dados; na verdade, ele realmente não se importa se você recebe todos os seus dados originais. Isso pode parecer terrível, mas tem seus usos, como para streaming de mídia. Não há problema em perder alguns quadros; em troca, você obtém seus dados um pouco mais rápido.

### TCP

TCP fornece um fluxo de dados confiável e orientado à conexão. TCP usa portas para enviar dados de e para hosts. Um aplicativo abre uma conexão de uma porta em seu host para outra porta em um host remoto. Para estabelecer a conexão, usamos o handshake TCP.

- O cliente (processo de conexão) envia um segmento SYN para o servidor para solicitar uma conexão.
- O servidor envia ao cliente um segmento SYN-ACK para reconhecer a solicitação de conexão do cliente.
- O cliente envia um ACK para o servidor para reconhecer a solicitação de conexão do servidor.

Uma vez estabelecida esta conexão, os dados podem ser trocados por uma conexão TCP. Os dados são enviados em diferentes segmentos e são rastreados com números de sequência TCP para que possam ser organizados na ordem correta quando são entregues. Em nosso exemplo de e-mail, a camada de transporte anexa a porta de destino (25) à porta de origem do host de origem.

## Exercise

No exercises for this lesson.

## Quiz Question

Qual é um protocolo de transporte confiável?

## Quiz Answer

TCP
