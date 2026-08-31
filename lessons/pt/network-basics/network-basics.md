---
lesson_id: "network-basics"
course_id: "network-basics"
lang: "pt"
order_index: 1
title: "Fundamentos de rede"
description: "Aprenda como hosts, enlaces, switches, roteadores e pacotes formam redes locais e de longa distância."
meta_title: "Fundamentos de rede - Fundamentos de rede"
meta_description: "Descubra a melhor maneira de aprender Linux começando pelos fundamentos de rede. Este guia apresenta, para iniciantes, componentes básicos de rede como WAN, LAN, roteadores e hosts."
meta_keywords: "fundamentos de rede, fundamentos de linux, melhor maneira de aprender linux, noções básicas de linux, WAN, LAN, WLAN, tutorial de rede, guia de redes"
---

Uma rede conecta interfaces para que aplicações em hosts diferentes possam trocar dados. Entender qual dispositivo, endereço e enlace cuida de cada parte do caminho facilita a interpretação posterior dos comandos Linux.

## Hosts e interfaces

Um host é um ponto de extremidade ou sistema conectado à rede, como um laptop, servidor, telefone ou máquina virtual. Um host pode ter várias interfaces: Ethernet, Wi-Fi, loopback, túneis, pontes ou adaptadores virtuais. Cada interface pode ter configurações da camada de enlace e da camada de rede adequadas à sua tecnologia.

Inspecione as interfaces e os endereços de um host Linux com:

```bash
$ ip address show
```

A presença de uma interface ou seu estado administrativamente ativo não comprova a conectividade de ponta a ponta.

:::single-choice{#network-basics-host-interface}
O que é uma interface de rede?

::option[Uma cópia permanente de todos os pacotes da Internet.]{#network-basics-interface-copy explanation="Uma interface transmite e recebe tráfego; ela não é um arquivo global de pacotes."}
::option[O ponto de conexão de um host com uma rede ou enlace virtual.]{#network-basics-interface-attachment .correct explanation="Um host pode ter várias interfaces físicas ou virtuais com configurações distintas."}
::option[Um alias legível para a fatura de um provedor de Internet.]{#network-basics-interface-invoice explanation="Rótulos de cobrança não têm relação com as conexões de rede de um host."}
:::

## Redes locais

Uma rede local, ou LAN, abrange um ambiente limitado, como uma residência, um escritório ou um segmento de data center. Switches Ethernet encaminham quadros entre portas em um enlace local. Uma LAN sem fio, ou WLAN, usa tecnologia de enlace sem fio. Interfaces com e sem fio ainda podem pertencer à mesma sub-rede IP quando uma ponte ou um ponto de acesso as conecta.

:::single-choice{#network-basics-wlan-relationship}
Qual é a relação entre uma WLAN e uma LAN?

::option[Uma WLAN é sempre uma Internet global separada.]{#network-basics-wlan-global explanation="Ela é uma rede local que usa tecnologia de enlace sem fio."}
::option[Uma WLAN é uma partição de disco usada por roteadores.]{#network-basics-wlan-disk explanation="O termo descreve redes, não a organização do armazenamento."}
::option[Uma WLAN é uma forma sem fio de rede local.]{#network-basics-wlan-local .correct explanation="Enlaces com e sem fio podem inclusive ser conectados por uma ponte em um único domínio de broadcast local."}
:::

## Roteadores e redes mais amplas

Um roteador encaminha pacotes da camada de rede entre redes IP de acordo com sua tabela de roteamento. Um equipamento residencial costuma combinar roteamento, comutação, acesso Wi-Fi, firewall, NAT e DHCP, mas essas continuam sendo funções distintas.

Uma rede de longa distância, ou WAN, abrange limites geográficos ou administrativos maiores. Um provedor de serviços de Internet pode conectar a rede de um cliente a outras redes, mas “WAN” não significa simplesmente todo dispositivo fora de uma residência.

:::single-choice{#network-basics-router-role}
Qual é a função que define um roteador?

::option[Encaminhar pacotes entre redes da camada de rede.]{#network-basics-forward-networks .correct explanation="O roteamento seleciona os próximos saltos através dos limites das redes IP."}
::option[Armazenar os arquivos de todos os usuários como backup obrigatório.]{#network-basics-router-backup explanation="A retenção de arquivos não é a função que define o roteamento."}
::option[Traduzir todos os nomes de host sem consultar o DNS.]{#network-basics-router-hostnames explanation="A resolução de nomes e o encaminhamento de pacotes são funções separadas."}
:::

## Pacotes, quadros e fluxos

As aplicações produzem dados que as camadas de protocolo dividem e encapsulam para transmissão. O IP transporta pacotes entre redes; um enlace local transporta cada pacote dentro de um quadro específico da tecnologia. Normalmente, os roteadores substituem o enquadramento da camada de enlace a cada salto enquanto encaminham o pacote IP.

Uma conversa pode envolver muitos pacotes nas duas direções. Perda, reordenação, fragmentação, retransmissão e mudanças de caminho significam que um único pacote capturado raramente descreve toda a transação da aplicação.

:::single-choice{#network-basics-router-frame}
O que normalmente acontece com o enquadramento da camada de enlace em um salto de roteador?

::option[O roteador remove o enquadramento recebido e cria outro para o próximo enlace.]{#network-basics-reframe .correct explanation="O pacote IP encaminhado é transportado em um novo quadro da camada de enlace adequado à interface de saída."}
::option[O mesmo quadro Ethernet atravessa toda a Internet sem alterações.]{#network-basics-same-frame explanation="Os quadros ficam restritos aos seus enlaces e são substituídos nos saltos roteados."}
::option[A aplicação exclui permanentemente os endereços IP.]{#network-basics-delete-ip explanation="O roteamento depende dos endereços da camada de rede."}
:::

## Resumo

Agora você pode descrever os principais componentes de um caminho de rede básico.

1. Diferencie hosts de suas interfaces físicas e virtuais.
2. Reconheça as formas com e sem fio de redes locais.
3. Separe o roteamento das outras funções de um equipamento residencial combinado.
4. Diferencie quadros de enlace de pacotes IP roteados.
