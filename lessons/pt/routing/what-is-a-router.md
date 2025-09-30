---
index: 1
lang: "pt"
title: "O que é um roteador?"
meta_title: "O que é um roteador? - Roteamento"
meta_description: "Aprenda o que é um roteador, como funciona e seu papel na rede. Entenda roteamento, saltos e entrega de pacotes para iniciantes."
meta_keywords: "roteador, rede, roteamento, saltos, comutação de pacotes, rede Linux, tutorial para iniciantes, guia de rede"
---

## Lesson Content

Já usamos o termo roteador antes; espero que você saiba o que é um, já que provavelmente tem um em sua casa. Um roteador permite que máquinas em uma rede se comuniquem entre si, bem como com outras redes. Em um roteador típico, você terá portas LAN que permitem que suas máquinas se conectem à mesma rede local, e também terá uma porta de uplink de internet que o conecta à internet. Às vezes, você verá esta porta rotulada como WAN porque ela essencialmente o conecta a uma rede mais ampla. Quando fazemos qualquer tipo de atividade de rede, ela precisa passar pelo roteador. O roteador decide para onde nossos pacotes de rede vão e quais entram. Ele roteia nossos pacotes entre várias redes para ir do host de origem ao host de destino.

### Como funciona um roteador?

Pense no roteamento da mesma forma que a entrega de correspondência. Temos um endereço para o qual queremos enviar uma carta. Quando a enviamos para os correios, eles pegam a carta e veem: "Ah, isso vai para a Califórnia." Vou colocá-la no caminhão que vai para a Califórnia (honestamente, não faço ideia de como o sistema postal funciona). A carta é então enviada para São Francisco. Dentro de São Francisco, existem diferentes códigos postais, e então nesses códigos postais, existem códigos de endereço menores até que, finalmente, alguém consiga entregar sua carta no endereço desejado. Por outro lado, se você já morasse em São Francisco e no mesmo código postal, o entregador de correspondência provavelmente saberia exatamente para onde a carta deve ir sem entregá-la a mais ninguém.

Quando roteamos pacotes, eles usam "rotas" de endereço semelhantes, como "para chegar à rede A, envie esses pacotes para a rede B". Quando não temos uma rota definida para isso, temos uma rota padrão que nossos pacotes usarão. Essas rotas são definidas em uma tabela de roteamento que nosso sistema usa para nos navegar pelas redes.

### Saltos

À medida que os pacotes se movem pelas redes, eles viajam em saltos. Um salto é como medimos aproximadamente a distância que o pacote deve percorrer para ir da origem ao destino. Digamos que eu tenha dois roteadores conectando o host A ao host B; portanto, dizemos que há dois saltos entre o host A e o host B. Cada salto é um dispositivo intermediário, como os roteadores, pelo qual devemos passar.

### Entendendo a diferença básica entre Switching, Routing e Flooding?

- **Packet SWITCHING** é basicamente receber, processar e encaminhar dados para o dispositivo de destino.
- **ROUTING** é um processo de criação da tabela de roteamento para que possamos fazer SWITCHING melhor.
- Antes do roteamento, **FLOODING** era usado. Se um roteador não sabe para onde enviar um pacote, então cada pacote de entrada é enviado por cada link de saída, exceto aquele em que chegou.

## Exercise

Prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da conectividade de rede e roteamento:

1. **[Explore os Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Pratique o teste da pilha TCP/IP local, identificando IPs privados e públicos e verificando a acessibilidade da rede, que são fundamentais para entender como um roteador facilita a comunicação.
2. **[Explore a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda como os comandos `ping` e `arp` ajudam você a observar como as camadas de rede e de enlace de dados interagem, e como o gateway padrão (roteador) lida com o tráfego remoto.
3. **[Simule a Conectividade da Camada de Rede no Linux](https://labex.io/pt/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Use o Docker para simular nós de rede e atribuir endereços IP, então teste a conectividade para entender como as sub-redes IP e o roteamento governam a comunicação de rede.

Esses laboratórios o ajudarão a aplicar os conceitos de comunicação de rede, endereçamento IP e o papel do roteamento em cenários reais, construindo confiança com os fundamentos da rede.

## Quiz Question

Como os pacotes medem a distância?

## Quiz Answer

Hops
