---
index: 1
lang: "pt"
title: "O que é um roteador?"
meta_title: "O que é um roteador? - Roteamento"
meta_description: "Aprenda o que é um roteador, como ele funciona e seu papel na rede. Entenda roteamento, hops e entrega de pacotes para iniciantes."
meta_keywords: "roteador, rede, roteamento, hops, comutação de pacotes, rede Linux, tutorial para iniciantes, guia de rede"
---

## Lesson Content

Já usamos o termo roteador antes; esperamos que você saiba o que é um, já que provavelmente tem um em sua casa. Um roteador permite que máquinas em uma rede se comuniquem entre si, bem como com outras redes. Em um roteador típico, você terá portas LAN que permitem que suas máquinas se conectem à mesma rede local, e também terá uma porta de uplink de internet que o conecta à internet. Às vezes, você verá esta porta rotulada como WAN porque ela essencialmente o conecta a uma rede mais ampla. Quando fazemos qualquer tipo de atividade de rede, ela precisa passar pelo roteador. O roteador decide para onde nossos pacotes de rede vão e quais entram. Ele roteia nossos pacotes entre várias redes para ir do host de origem ao host de destino.

### Como funciona um roteador?

Pense no roteamento da mesma forma que na entrega de correspondência. Temos um endereço para o qual queremos enviar uma carta. Quando a enviamos para os correios, eles pegam a carta e veem: "Ah, isso vai para a Califórnia." Vou colocá-la no caminhão que vai para a Califórnia (honestamente, não tenho ideia de como o sistema postal funciona). A carta então é enviada para São Francisco. Dentro de São Francisco, existem diferentes códigos postais, e então nesses códigos postais, existem códigos de endereço menores até que, finalmente, alguém consiga entregar sua carta no endereço desejado. Por outro lado, se você já morasse em São Francisco e no mesmo código postal, o entregador de correspondência provavelmente saberá exatamente para onde a carta deve ir sem entregá-la a mais ninguém.

Quando roteamos pacotes, eles usam "rotas" de endereço semelhantes, como "para chegar à rede A, envie esses pacotes para a rede B". Quando não temos uma rota definida para isso, temos uma rota padrão que nossos pacotes usarão. Essas rotas são definidas em uma tabela de roteamento que nosso sistema usa para nos navegar pelas redes.

### Hops

À medida que os pacotes se movem pelas redes, eles viajam em "hops". Um hop é como medimos aproximadamente a distância que o pacote deve percorrer para ir da origem ao destino. Digamos que eu tenha dois roteadores conectando o host A ao host B; portanto, dizemos que há dois hops entre o host A e o host B. Cada hop é um dispositivo intermediário, como os roteadores, pelo qual devemos passar.

### Entendendo a diferença básica entre Switching, Routing e Flooding?

- **Packet SWITCHING** é basicamente receber, processar e encaminhar dados para o dispositivo de destino.
- **ROUTING** é um processo de criação da tabela de roteamento para que possamos fazer SWITCHING melhor.
- Antes do roteamento, **FLOODING** era usado. Se um roteador não sabe para onde enviar um pacote, então cada pacote de entrada é enviado por cada link de saída, exceto aquele em que chegou.

## Exercise

No exercises for this lesson.

## Quiz Question

Como os pacotes medem a distância?

## Quiz Answer

Hops
