---
index: 8
lang: "pt"
title: "Camada de Enlace"
meta_title: "Camada de Enlace - Fundamentos de Rede"
meta_description: "Explore os fundamentos da camada de enlace do TCP/IP. Aprenda como o cabeçalho da camada de enlace é construído, como o ARP resolve endereços IP para endereços MAC e o processo de travessia de pacotes em uma rede local."
meta_keywords: "camada de enlace, cabeçalho camada de enlace, ARP, TCP/IP, endereço MAC, fundamentos de rede, rede Linux, travessia de pacotes, protocolo de resolução de endereços"
---

## Lesson Content

A **Camada de Enlace** (Link Layer) é a camada fundamental do modelo TCP/IP, responsável pelas comunicações no segmento de rede local. Esta camada é específica de hardware, lidando diretamente com as placas de interface de rede e o endereçamento físico.

### Quadros (Frames) e o Cabeçalho da Camada de Enlace

Na **camada de enlace**, o pacote da camada de rede é encapsulado em uma estrutura chamada quadro (frame). Uma parte crucial deste processo é a adição do **cabeçalho da camada de enlace**. Este cabeçalho contém os endereços MAC de origem e destino dos hosts, somas de verificação (checksums) para detecção de erros e separadores de pacotes, que permitem ao dispositivo receptor identificar onde um quadro termina e o próximo começa.

Para construir o **cabeçalho da camada de enlace**, o sistema precisa dos endereços MAC de origem e destino. Embora o endereço MAC de origem seja conhecido, o endereço MAC de destino para um IP na mesma rede local precisa ser descoberto. É aqui que entra o Protocolo de Resolução de Endereços (ARP).

### ARP (Address Resolution Protocol)

ARP é um protocolo da **camada de enlace** usado para encontrar o endereço MAC associado a um endereço IP específico dentro da mesma rede. Se o host de destino estivesse em uma rede diferente, o pacote seria enviado para um gateway padrão (roteador), e o ARP seria usado para encontrar o endereço MAC do roteador.

Os sistemas primeiro consultam sua tabela de pesquisa ARP, que armazena em cache os mapeamentos conhecidos de IP para endereço MAC. Se o endereço necessário não estiver no cache, o sistema transmite uma solicitação ARP para toda a rede. Esta mensagem especial pergunta qual host possui um endereço IP específico, por exemplo, 10.10.1.4. O host com esse endereço IP enviará uma resposta ARP contendo seu endereço IP e MAC.

Com todos os endereços IP e MAC necessários, a **camada de enlace** pode agora encaminhar o quadro através da placa de interface de rede. A jornada de um pacote é um processo de múltiplas etapas de encapsulamento e desencapsulamento à medida que ele sobe e desce na pilha TCP/IP nas extremidades de envio e recebimento.

### Travessia do Pacote

Aqui está um detalhamento passo a passo de como um pacote viaja de um remetente (Pete) para um destinatário (Patty):

1. Pete envia um e-mail para Patty. Esses dados são enviados para a camada de transporte.
2. A camada de transporte encapsula os dados em um cabeçalho TCP ou UDP para formar um segmento. Ela anexa as portas de destino e origem e envia o segmento para a camada de rede.
3. A camada de rede encapsula o segmento dentro de um pacote IP e anexa os endereços IP de origem e destino. Em seguida, roteia o pacote para a **camada de enlace**.
4. O pacote chega à **camada de enlace**, onde é encapsulado em um quadro. O **cabeçalho da camada de enlace**, contendo os endereços MAC de origem e destino, é adicionado.
5. Patty recebe este quadro de dados através de sua camada física, verifica a integridade dos dados do quadro, desencapsula-o e envia o pacote IP para sua camada de rede.
6. A camada de rede lê o pacote para encontrar os endereços IP de origem e destino. Confirma que o IP de destino corresponde ao seu, desencapsula o pacote e envia o segmento para a camada de transporte.
7. A camada de transporte desencapsula o segmento, verifica os números de porta TCP ou UDP e estabelece uma conexão com a camada de aplicação com base nessas portas.
8. A camada de aplicação recebe os dados da camada de transporte na porta especificada e os apresenta a Patty como a mensagem de e-mail final.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da Camada de Enlace, endereços MAC e ARP:

1. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Pratique o uso do comando `ip a` para identificar informações de endereçamento de rede, incluindo endereços MAC, em um sistema Linux.
2. **[Explorar a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda como os comandos `ping` e `arp` trabalham juntos para resolver endereços IP para endereços MAC e entender as interações da camada de rede.
3. **[Analisar Quadros Ethernet com tcpdump no Linux](https://labex.io/pt/labs/comptia-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - Ganhe experiência prática capturando e inspecionando quadros Ethernet, incluindo endereços MAC, para entender as comunicações de rede de baixo nível.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e a construir confiança com os fundamentos de rede na Camada de Enlace.

## Quiz Question

Qual protocolo é usado para encontrar o endereço MAC de um host na mesma rede local? (Por favor, responda com a sigla em inglês em letras maiúsculas).

## Quiz Answer

ARP
