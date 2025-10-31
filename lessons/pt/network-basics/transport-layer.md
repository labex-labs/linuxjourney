---
index: 6
lang: "pt"
title: "Camada de Transporte"
meta_title: "Camada de Transporte - Fundamentos de Rede"
meta_description: "Explore a Camada de Transporte em redes Linux. Esta lição aborda protocolos chave como TCP e UDP, a função das portas de rede, segmentação de dados e o handshake TCP para transferência de dados confiável."
meta_keywords: "Camada de Transporte Linux, TCP, UDP, handshake TCP, portas de rede, segmentação de dados, redes Linux, protocolos de rede, transferência de dados confiável"
---

## Lesson Content

A camada de transporte é uma parte fundamental da rede Linux responsável pela comunicação de ponta a ponta e pela transferência de dados confiável entre aplicações em hosts diferentes. Ela prepara os dados para o transporte através da rede de forma estruturada e gerenciável.

### Segmentação de Dados

Uma das principais funções da camada de transporte é a segmentação de dados. Ela divide grandes quantidades de dados em pedaços menores e mais gerenciáveis, chamados segmentos. Esse processo torna a transferência de dados mais eficiente e resiliente. Se um segmento for perdido ou corrompido durante a transmissão, apenas essa pequena parte precisa ser reenviada, e não o conjunto de dados inteiro. Assim que os segmentos chegam ao destino, a camada de transporte os remonta na ordem correta.

### Entendendo Portas de Rede

Enquanto os endereços IP identificam o host correto em uma rede, eles não especificam qual aplicação ou serviço deve receber os dados. É aí que entram as portas de rede. Serviços como HTTP (tráfego web) ou SMTP (e-mail) escutam em portas específicas e bem conhecidas. Por exemplo, o HTTP geralmente usa a porta 80. A camada de transporte anexa números de porta de origem e destino a cada segmento, garantindo que os dados sejam entregues ao processo correto no host receptor.

### Protocolos de Transporte Principais: TCP e UDP

Existem dois protocolos de transporte principais usados em redes modernas: TCP (Transmission Control Protocol) e UDP (User Datagram Protocol). Abordaremos brevemente o UDP e depois focaremos no TCP, pois ele é o mais utilizado para comunicação confiável.

### UDP (User Datagram Protocol)

UDP é um protocolo sem conexão que oferece um método rápido, mas não confiável, de transporte de dados. Ele não garante que todos os segmentos chegarão ou que chegarão na ordem correta. Embora isso possa parecer uma desvantagem, o UDP é altamente eficaz para aplicações onde a velocidade é mais crítica do que a precisão perfeita, como streaming de vídeo ao vivo ou jogos online. Perder alguns quadros de vídeo é frequentemente uma troca aceitável para um fluxo mais suave e rápido.

### TCP (Transmission Control Protocol)

O TCP fornece um fluxo de dados confiável e orientado à conexão. Antes que qualquer dado seja trocado, o TCP estabelece uma conexão formal entre os dois hosts para garantir que ambos estejam prontos para se comunicar.

### O Handshake TCP

Para estabelecer uma conexão, o TCP usa um processo chamado handshake de três vias:

1.  **SYN**: O cliente envia um segmento SYN (sincronizar) para o servidor para iniciar uma conexão.
2.  **SYN-ACK**: O servidor responde com um segmento SYN-ACK (sincronizar-reconhecer) para acusar o recebimento da solicitação do cliente.
3.  **ACK**: O cliente envia um segmento ACK (reconhecer) de volta ao servidor, confirmando que a conexão foi estabelecida.

Após a conclusão do handshake, os dados podem ser trocados de forma confiável. O TCP usa números de sequência para rastrear cada segmento, permitindo que o host receptor os remonte na ordem correta e solicite a retransmissão de quaisquer segmentos ausentes. Em nosso exemplo de e-mail, a camada de transporte anexaria a porta de destino para SMTP (porta 25) e uma porta de origem do host cliente a cada segmento.

## Exercise

Embora não haja laboratórios específicos para este tópico, recomendamos explorar o abrangente [Trilha de Aprendizagem Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual é um protocolo de transporte confiável? (Sua resposta deve estar em inglês e diferencia maiúsculas de minúsculas).

## Quiz Answer

TCP
