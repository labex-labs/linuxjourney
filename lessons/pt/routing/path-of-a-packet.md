---
lang: "pt"
title: "Caminho de um Pacote"
description: "Aprenda como um pacote viaja dentro e fora de uma rede. Entenda IP, MAC, ARP e tabelas de roteamento para comunicação em rede. Comece sua jornada de rede Linux!"
keywords: "viagem de pacote, comunicação de rede, ARP, endereço IP, endereço MAC, tabela de roteamento, rede Linux, guia para iniciantes"
---

## Lesson Content

### Vamos ver como um pacote viaja dentro de sua rede local

1. Primeiro, a máquina local comparará o endereço IP de destino para ver se está na mesma sub-rede, verificando sua máscara de sub-rede.
2. Quando os pacotes são enviados, eles precisam ter um endereço MAC de origem, endereço MAC de destino, endereço IP de origem e endereço IP de destino. Neste ponto, não sabemos o endereço MAC de destino.
3. Para chegar ao host de destino, usamos ARP para transmitir uma solicitação na rede local para encontrar o endereço MAC do host de destino.
4. Agora o pacote pode ser enviado com sucesso!

### Vamos ver como um pacote viaja para fora de sua rede

1. Primeiro, a máquina local comparará o endereço IP de destino. Como está fora da nossa rede, ela não vê o endereço MAC do host de destino. E não podemos usar ARP porque a solicitação ARP é uma transmissão para hosts conectados localmente.
2. Então nosso pacote agora olha para a routing table. Ele não sabe o endereço do IP de destino, então o envia para o default gateway (outro roteador). Então agora nosso pacote contém nosso IP de origem, IP de destino e MAC de origem; no entanto, não temos um MAC de destino. Lembre-se, os endereços MAC só são alcançados através da mesma rede. Então o que ele faz? Ele envia uma solicitação ARP para obter o endereço MAC do default gateway.
3. O roteador olha para o pacote e confirma o endereço MAC de destino, mas não é o endereço IP de destino final, então ele continua olhando para a routing table para encaminhar o pacote para outro endereço IP que possa ajudar o pacote a seguir para seu destino. Cada vez que o pacote se move, ele remove os antigos endereços MAC de origem e destino e atualiza o pacote com os novos endereços MAC de origem e destino.
4. Uma vez que o pacote é encaminhado para a mesma rede, usamos ARP para encontrar o endereço MAC de destino final.
5. Durante este processo, nosso pacote não altera o endereço IP de origem ou destino.

## Exercise

No exercises for this lesson.

## Quiz Question

Como encontramos o endereço MAC de um endereço IP?

## Quiz Answer

ARP
