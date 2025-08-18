---
lang: "pt"
title: "Camada de Enlace"
meta_description: "Aprenda sobre a Camada de Enlace no TCP/IP, como o ARP resolve endereços MAC e a travessia de pacotes. Entenda os fundamentos de rede com este tutorial de rede Linux."
meta_keywords: "Camada de Enlace, ARP, TCP/IP, endereço MAC, fundamentos de rede, rede Linux, iniciante, tutorial"
---

## Lesson Content

Na base do modelo TCP/IP está a Camada de Enlace (Link Layer). Esta camada é específica do hardware.

Na camada de enlace, nosso pacote é encapsulado mais uma vez em algo chamado quadro (frame). O cabeçalho do quadro anexa os endereços MAC de origem e destino de nossos hosts, checksums e separadores de pacote para que o receptor possa saber quando um pacote termina.

Felizmente, estamos na mesma rede, então nosso pacote não terá que viajar muito longe. Primeiro, a camada de enlace anexa meu endereço MAC de origem ao cabeçalho do quadro, mas também precisa saber o endereço MAC de Patty. Como ela sabe disso, e como eu o encontro, já que não está na Internet? Usamos o ARP!

### ARP (Address Resolution Protocol)

O ARP encontra o endereço MAC associado a um endereço IP. O ARP é usado dentro da mesma rede. Se Patty não estivesse na mesma rede, usaríamos um sistema de roteamento para determinar o próximo roteador que receberia o pacote, e uma vez que estivéssemos na mesma rede, poderíamos usar o ARP.

Uma vez que estamos na mesma rede, os sistemas primeiro usam a tabela de pesquisa ARP que armazena informações sobre quais endereços IP estão associados a qual endereço MAC. Se o valor não estiver lá, então o ARP é usado. Então o sistema enviará uma mensagem de broadcast para a rede usando o protocolo ARP para descobrir qual host tem o IP 10.10.1.4. Uma mensagem de broadcast é uma mensagem especial que é enviada para todos os hosts em uma rede (apropriadamente nomeada para enviar um broadcast). Qualquer máquina com o endereço IP solicitado responderá com um pacote ARP contendo o endereço IP e o endereço MAC.

Agora que temos todos os dados necessários — endereço IP e endereços MAC — nossa camada de enlace encaminha este quadro através de nossa placa de interface de rede, para o próximo dispositivo, e encontra a rede de Patty. Esta etapa é um pouco mais complexa do que eu acabei de explicar, mas discutiremos mais detalhes no curso de Roteamento.

E aí está: uma travessia de pacote simples (ou não tão simples) pela camada TCP/IP. Tenha em mente que os pacotes não viajam de forma unidirecional como esta. Ainda nem chegamos à rede de Patty! Ao viajar por redes, é necessário passar pelo modelo TCP/IP pelo menos duas vezes antes que qualquer dado seja enviado ou recebido. Na realidade, a aparência deste pacote seria algo assim:

### Packet Traversal

1. Pete sends Patty an email: this data gets sent to the transport layer.
2. The transport layer encapsulates the data into a TCP or UDP header to form a segment. The segment attaches the destination and source TCP or UDP port, then the segment is sent to the network layer.
3. The network layer encapsulates the TCP segment inside an IP packet; it attaches the source and destination IP address. Then it routes the packet to the link layer.
4. The packet then reaches Pete's physical hardware and gets encapsulated in a frame. The source and destination MAC addresses get added to the frame.
5. Patty receives this data frame through her physical layer and checks each frame for data integrity, then de-encapsulates the frame contents and sends the IP packet to the network layer.
6. The network layer reads the packet to find the source and destination IP that was previously attached. It checks if its IP is the same as the destination IP, which it is! It de-encapsulates the packet and sends the segment to the transport layer.
7. The transport layer de-encapsulates the segments, checks the TCP or UDP port numbers, and makes a connection to the application layer based on those port numbers.
8. The application layer receives the data from the transport layer on the port that was specified and presents it to Patty in the form of the final email message.

## Exercise

No exercises for this lesson.

## Quiz Question

O que é usado para encontrar o endereço MAC na mesma rede?

## Quiz Answer

ARP
