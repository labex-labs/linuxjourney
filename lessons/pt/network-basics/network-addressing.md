---
lesson_id: "network-addressing"
course_id: "network-basics"
lang: "pt"
order_index: 4
title: "Endereçamento de rede"
description: "Aprenda como endereços de enlace, endereços IP e nomes de host identificam diferentes partes da comunicação de rede."
meta_title: "Endereçamento de rede - Fundamentos de rede"
meta_description: "Descubra os fundamentos do endereçamento de rede. Este guia explica endereços MAC, endereços IP e nomes de host, conceitos essenciais para entender como os dispositivos se comunicam em redes Linux."
meta_keywords: "endereçamento de rede, endereço MAC, endereço IP, nome de host, identificadores de rede, redes Linux, fundamentos de rede, iniciante, tutorial, guia"
---

A comunicação de rede usa identificadores diferentes em escopos diferentes. Endereços da camada de enlace entregam quadros em um enlace local, endereços IP permitem a entrega roteada, e nomes ajudam aplicações e pessoas a selecionar serviços.

## Endereços da camada de enlace

Um endereço MAC Ethernet possui 48 bits e normalmente é escrito como seis octetos hexadecimais, por exemplo, `00:c4:b5:45:b2:43`. Um endereço de origem identifica uma interface no enlace atual, enquanto o destino pode ser unicast, multicast ou broadcast.

Não há garantia de que endereços MAC sejam permanentes ou globalmente exclusivos. O software pode atribuir um endereço administrado localmente, interfaces virtuais geram endereços, e recursos de privacidade do Wi-Fi podem torná-los aleatórios. Normalmente, os roteadores substituem o enquadramento Ethernet em cada salto; portanto, um servidor remoto não recebe o endereço Ethernet de origem do enlace local original.

:::single-choice{#network-addressing-mac-scope}
Qual é o escopo normal de um endereço MAC Ethernet na entrega de pacotes?

::option[O enlace local atual.]{#network-addressing-local-link .correct explanation="Os roteadores criam um novo enquadramento da camada de enlace para os saltos seguintes."}
::option[Todos os saltos roteados até o servidor final na Internet.]{#network-addressing-all-hops explanation="O quadro original não atravessa roteadores sem alterações."}
::option[Apenas a codificação de texto da aplicação.]{#network-addressing-text-encoding explanation="Um endereço MAC pertence ao enquadramento da camada de enlace."}
:::

## Endereços IP e prefixos

Endereços IPv4 possuem 32 bits, ou quatro octetos, enquanto endereços IPv6 possuem 128 bits. Um endereço IP normalmente é atribuído a uma interface e interpretado com um comprimento de prefixo, como `192.0.2.10/24` ou `2001:db8::10/64`. O prefixo identifica quais bits iniciais descrevem a rede.

Uma interface pode ter vários endereços IP, e um endereço pode mudar por DHCP, endereçamento de privacidade, failover ou administração. Endereços IPv4 privados podem ser reutilizados em redes separadas; as políticas de roteamento público e NAT determinam a acessibilidade externa.

:::single-choice{#network-addressing-ipv4-size}
Qual é o tamanho de um endereço IPv4?

::option[32 bits em quatro octetos.]{#network-addressing-thirty-two .correct explanation="Cada componente decimal exibido representa oito bits."}
::option[4 bits em um único dígito hexadecimal.]{#network-addressing-four-bits explanation="Quatro bits representam apenas um dígito hexadecimal."}
::option[128 bits em dezesseis octetos.]{#network-addressing-128-octets explanation="O IPv6 possui 128 bits, não 128 octetos."}
:::

## Nomes de host e resolução de nomes

Um nome de host é um nome, não um endereço. A resolução de nomes pode consultar `/etc/hosts`, DNS, sistemas multicast ou outras fontes, de acordo com a configuração de serviços de nomes do host. Um nome pode ser resolvido para vários endereços, e vários nomes podem se referir a um serviço.

Use o caminho do resolvedor do sistema ao testar o que uma aplicação provavelmente verá:

```bash
$ getent ahosts example.com
```

As respostas do DNS podem mudar ou estar em cache, e uma resolução bem-sucedida não comprova que o serviço está acessível.

:::single-choice{#network-addressing-getent-purpose}
Por que usar `getent ahosts` durante uma verificação de resolução de nomes?

::option[Ele atribui permanentemente o endereço retornado a todas as interfaces.]{#network-addressing-getent-assign explanation="O comando consulta bancos de dados e não configura interfaces."}
::option[Ele solicita endereços ao caminho de serviços de nomes configurado no sistema.]{#network-addressing-system-resolver .correct explanation="Isso pode incluir arquivos locais e DNS de acordo com a política do host."}
::option[Ele garante que uma aplicação esteja íntegra em todos os hosts retornados.]{#network-addressing-getent-health explanation="A consulta de nomes e a integridade da aplicação são testes separados."}
:::

## Inspecionando um host Linux

Consulte separadamente as configurações de enlace e IP:

```bash
$ ip -brief link
$ ip -brief address
```

Em seguida, inspecione as rotas e o estado dos vizinhos ao diagnosticar a acessibilidade. Nunca deduza a interface ou o endereço de origem correto apenas pelo nome; a seleção de rotas, as regras de política, os namespaces e os túneis podem alterar o caminho.

:::single-choice{#network-addressing-ip-link-versus-address}
Qual visualização de comando se concentra nos endereços IP atribuídos?

::option[`ip -brief address`]{#network-addressing-address-view .correct explanation="O objeto address exibe as atribuições de IPv4 e IPv6 nas interfaces."}
::option[Apenas `ip -brief link`.]{#network-addressing-link-only explanation="A visualização link se concentra no estado da interface e da camada de enlace."}
::option[`pwd`]{#network-addressing-pwd explanation="Pwd mostra o diretório de trabalho do shell."}
:::

## Resumo

Agora você pode diferenciar nomes e endereços de acordo com seus escopos de rede.

1. Trate endereços MAC como identificadores do enlace local que podem mudar.
2. Leia endereços IPv4 e IPv6 com seus comprimentos de prefixo.
3. Reconheça que as interfaces podem conter vários endereços lógicos.
4. Consulte nomes de host por meio do resolvedor configurado no sistema.
