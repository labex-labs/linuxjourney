---
index: 3
lang: "pt"
title: "Modelo TCP/IP"
meta_title: "Modelo TCP/IP - Fundamentos de Rede"
meta_description: "Aprenda sobre as camadas do modelo TCP/IP: Aplicação, Transporte, Rede e Enlace. Entenda como os dados viajam pelas redes. Comece sua jornada de rede Linux!"
meta_keywords: "modelo TCP/IP, fundamentos de rede, rede Linux, TCP, IP, tutorial para iniciantes, camadas de rede, guia"
---

## Lesson Content

O modelo OSI deu origem ao que eventualmente se tornou o modelo TCP/IP, e este modelo é, na verdade, a base da Internet. É a implementação real da rede. O modelo TCP/IP usa o conjunto de protocolos TCP/IP, que comumente chamamos de TCP/IP. Esses protocolos trabalham juntos para especificar como os dados devem ser coletados, endereçados, transmitidos e roteados através de uma rede. Usando o modelo TCP/IP, podemos ver como esses protocolos são usados para mostrar a quebra de como um pacote viaja pela rede.

### Camada de Aplicação

A camada superior do modelo TCP/IP. Ela determina como os programas do seu computador (como o seu navegador web) interagem com os serviços da camada de transporte para visualizar os dados que são enviados ou recebidos.

Esta camada usa:

- HTTP (Hypertext Transfer Protocol) - usado para páginas web na Internet.
- SMTP (Simple Mail Transfer Protocol) - transmissão de correio eletrónico (email)

### Camada de Transporte

Como os dados serão transmitidos, inclui a verificação das portas corretas, a integridade dos dados e, basicamente, a entrega dos nossos pacotes.

Esta camada usa:

- TCP (Transmission Control Protocol) - entrega de dados confiável
- UDP (User Datagram Protocol) - entrega de dados não confiável

### Camada de Rede

Esta camada especifica como mover pacotes entre hosts e através de redes.

Esta camada usa:

- IP (Internet Protocol) - Ajuda a rotear pacotes de uma máquina para outra.
- ICMP (Internet Control Message Protocol) - Ajuda a nos dizer o que está acontecendo, como mensagens de erro e informações de depuração.

### Camada de Enlace

Esta camada especifica como enviar dados através de uma peça física de hardware, como dados viajando via Ethernet, fibra, etc.

As listas acima de protocolos que cada camada usa não são exaustivas, e você encontrará muitos outros protocolos que entram em jogo.

Nas lições seguintes, vamos aprofundar cada uma dessas camadas e discutir como nosso pacote atravessa a rede sob a ótica do modelo TCP/IP (existem muitas perspectivas sobre como um pacote viaja através de redes; não vamos olhar para todas elas, mas esteja ciente de que elas existem).

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do modelo TCP/IP e dos fundamentos de rede:

1. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Pratique a identificação de informações chave de endereçamento de rede, como endereços MAC e IP, usando o comando `ip a`, que é fundamental para entender as camadas de rede e de enlace de dados do modelo TCP/IP.
2. **[Explorar a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda como os comandos `ping` e `arp` demonstram a interação entre as camadas de rede e de enlace de dados, fornecendo uma visão prática de como os dispositivos se comunicam dentro da pilha TCP/IP.
3. **[Simular Conectividade da Camada de Rede no Linux](https://labex.io/pt/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Ganhe experiência prática simulando a conectividade de rede entre nós Linux, atribuindo endereços IP e testando a comunicação, aplicando diretamente conceitos relacionados à camada de rede do modelo TCP/IP.

Esses laboratórios o ajudarão a aplicar os conceitos do modelo TCP/IP em cenários reais e a construir confiança com a configuração e solução de problemas de rede.

## Quiz Question

Qual é a camada superior do modelo TCP/IP?

## Quiz Answer

Application
