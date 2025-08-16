---
title: "Modelo TCP/IP"
description: "Aprenda sobre as camadas do modelo TCP/IP: Aplicação, Transporte, Rede e Enlace. Entenda como os dados viajam pelas redes. Comece sua jornada de rede Linux!"
keywords: "modelo TCP/IP, conceitos básicos de rede, rede Linux, TCP, IP, tutorial para iniciantes, camadas de rede, guia"
---

## Lesson Content

O modelo OSI deu origem ao que eventualmente se tornou o modelo TCP/IP, e este modelo é, na verdade, a base da Internet. É a implementação real de redes. O modelo TCP/IP usa o conjunto de protocolos TCP/IP, que comumente chamamos de TCP/IP. Esses protocolos trabalham juntos para especificar como os dados devem ser coletados, endereçados, transmitidos e roteados através de uma rede. Usando o modelo TCP/IP, podemos ver como esses protocolos são usados para mostrar a quebra de como um pacote viaja pela rede.

### Application Layer

A Camada de Aplicação é a camada superior do modelo TCP/IP. Ela determina como os programas do seu computador (como o seu navegador da web) interagem com os serviços da camada de transporte para visualizar os dados que são enviados ou recebidos.

Esta camada usa:

- HTTP (Hypertext Transfer Protocol) - usado para páginas da web na Internet.
- SMTP (Simple Mail Transfer Protocol) - transmissão de correio eletrônico (email)

### Transport Layer

Como os dados serão transmitidos, inclui a verificação das portas corretas, a integridade dos dados e, basicamente, a entrega dos nossos pacotes.

Esta camada usa:

- TCP (Transmission Control Protocol) - entrega de dados confiável
- UDP (User Datagram Protocol) - entrega de dados não confiável

### Network Layer

Esta camada especifica como mover pacotes entre hosts e através de redes.

Esta camada usa:

- IP (Internet Protocol) - Ajuda a rotear pacotes de uma máquina para outra.
- ICMP (Internet Control Message Protocol) - Ajuda a nos dizer o que está acontecendo, como mensagens de erro e informações de depuração.

### Link Layer

Esta camada especifica como enviar dados através de uma peça física de hardware, como dados viajando por Ethernet, fibra, etc.

As listas acima de protocolos que cada camada usa não são exaustivas, e você encontrará muitos outros protocolos que entram em jogo.

Nas lições seguintes, vamos aprofundar cada uma dessas camadas e discutir como nosso pacote atravessa a rede sob a ótica do modelo TCP/IP (existem muitas perspectivas sobre como um pacote viaja através de redes; não veremos todas, mas esteja ciente de que elas existem).

## Exercise

No exercises for this lesson.

## Quiz Question

Qual é a camada superior do modelo TCP/IP?

## Quiz Answer

Application
