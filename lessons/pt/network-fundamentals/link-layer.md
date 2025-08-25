---
index: 8
lang: "pt"
title: "Camada de Enlace"
meta_title: "Camada de Enlace - Fundamentos de Rede"
meta_description: "Aprenda sobre a Camada de Enlace no TCP/IP, como o ARP resolve endereços MAC e a travessia de pacotes. Entenda os fundamentos de rede com este tutorial de rede Linux."
meta_keywords: "Camada de Enlace, ARP, TCP/IP, endereço MAC, fundamentos de rede, rede Linux, iniciante, tutorial"
---

## Lesson Content

Na parte inferior do modelo TCP/IP, encontra-se a Camada de Enlace. Esta camada é específica do hardware.

Na camada de enlace, nosso pacote é encapsulado mais uma vez em algo chamado quadro. O cabeçalho do quadro anexa os endereços MAC de origem e destino de nossos hosts, somas de verificação e separadores de pacote para que o receptor possa saber quando um pacote termina.

Felizmente, estamos na mesma rede, então nosso pacote não terá que viajar muito longe. Primeiro, a camada de enlace anexa meu endereço MAC de origem ao cabeçalho do quadro, mas também precisa saber o endereço MAC de Patty. Como ela sabe disso, e como eu o encontro, já que não está na Internet? Usamos ARP!

### ARP (Protocolo de Resolução de Endereços)

O ARP encontra o endereço MAC associado a um endereço IP. O ARP é usado dentro da mesma rede. Se Patty não estivesse na mesma rede, usaríamos um sistema de roteamento para determinar o próximo roteador que receberia o pacote, e uma vez que estivéssemos na mesma rede, poderíamos usar o ARP.

Uma vez que estamos na mesma rede, os sistemas primeiro usam a tabela de pesquisa ARP que armazena informações sobre quais endereços IP estão associados a qual endereço MAC. Se o valor não estiver lá, então o ARP é usado. Então o sistema enviará uma mensagem de broadcast para a rede usando o protocolo ARP para descobrir qual host tem o IP 10.10.1.4. Uma mensagem de broadcast é uma mensagem especial que é enviada para todos os hosts em uma rede (apropriadamente nomeada para enviar um broadcast). Qualquer máquina com o endereço IP solicitado responderá com um pacote ARP contendo o endereço IP e o endereço MAC.

Agora que temos todos os dados necessários — endereço IP e endereços MAC — nossa camada de enlace encaminha este quadro através de nossa placa de interface de rede, para o próximo dispositivo, e encontra a rede de Patty. Este passo é um pouco mais complexo do que eu acabei de explicar, mas discutiremos mais detalhes no curso de Roteamento.

E aí está: uma travessia de pacote simples (ou nem tão simples) pela camada TCP/IP. Tenha em mente que os pacotes não viajam de forma unidirecional como esta. Ainda nem chegamos à rede de Patty! Ao viajar por redes, é necessário passar pelo modelo TCP/IP pelo menos duas vezes antes que qualquer dado seja enviado ou recebido. Na realidade, a aparência deste pacote seria algo assim:

### Travessia de Pacotes

1. Pete envia um e-mail para Patty: esses dados são enviados para a camada de transporte.
2. A camada de transporte encapsula os dados em um cabeçalho TCP ou UDP para formar um segmento. O segmento anexa a porta TCP ou UDP de destino e origem, então o segmento é enviado para a camada de rede.
3. A camada de rede encapsula o segmento TCP dentro de um pacote IP; ela anexa o endereço IP de origem e destino. Em seguida, roteia o pacote para a camada de enlace.
4. O pacote então atinge o hardware físico de Pete e é encapsulado em um quadro. Os endereços MAC de origem e destino são adicionados ao quadro.
5. Patty recebe este quadro de dados através de sua camada física e verifica cada quadro quanto à integridade dos dados, então desencapsula o conteúdo do quadro e envia o pacote IP para a camada de rede.
6. A camada de rede lê o pacote para encontrar o IP de origem e destino que foi anexado anteriormente. Ela verifica se seu IP é o mesmo que o IP de destino, o que é! Ela desencapsula o pacote e envia o segmento para a camada de transporte.
7. A camada de transporte desencapsula os segmentos, verifica os números de porta TCP ou UDP e faz uma conexão com a camada de aplicação com base nesses números de porta.
8. A camada de aplicação recebe os dados da camada de transporte na porta que foi especificada e os apresenta a Patty na forma da mensagem de e-mail final.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da Camada de Enlace, endereços MAC e ARP:

1. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Pratique o uso do comando `ip a` para identificar informações de endereçamento de rede, incluindo endereços MAC, em um sistema Linux.
2. **[Explorar a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda como os comandos `ping` e `arp` funcionam juntos para resolver endereços IP para endereços MAC e entender as interações da camada de rede.
3. **[Analisar Quadros Ethernet com tcpdump no Linux](https://labex.io/pt/labs/linux-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - Obtenha experiência prática na captura e inspeção de quadros Ethernet, incluindo endereços MAC, para entender as comunicações de rede de baixo nível.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com os fundamentos de rede na Camada de Enlace.

## Quiz Question

O que é usado para encontrar o endereço MAC na mesma rede?

## Quiz Answer

ARP
