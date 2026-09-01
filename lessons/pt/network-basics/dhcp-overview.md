---
lesson_id: "dhcp-overview"
course_id: "network-basics"
lang: "pt"
order_index: 9
title: "Visão geral do DHCP"
description: "Aprenda como o DHCPv4 concede endereços e opções de rede por meio de descoberta, seleção e renovação."
meta_title: "Visão geral do DHCP - Fundamentos de rede"
meta_description: "Aprenda os fundamentos do DHCP (Protocolo de Configuração Dinâmica de Hosts). Este guia aborda como o DHCP atribui endereços IP, seu processo de quatro etapas (DORA) e sua função na configuração de rede. Ideal para iniciantes em redes Linux."
meta_keywords: "DHCP, Protocolo de Configuração Dinâmica de Hosts, camada dhcp, endereço IP, redes Linux, processo DHCP, DORA, configuração de rede"
---

O Protocolo de Configuração Dinâmica de Hosts fornece aos clientes uma configuração de rede concedida por tempo limitado. No DHCPv4, ela pode incluir um endereço IPv4, máscara de sub-rede, roteadores padrão, servidores DNS, duração da concessão e outras opções selecionadas pela política local.

## Clientes, servidores e retransmissores

Um servidor DHCP gerencia escopos ou conjuntos de endereços e o estado das concessões. O servidor não precisa estar em todos os segmentos físicos: um retransmissor DHCP pode encaminhar as trocas do cliente entre uma sub-rede e um servidor centralizado. Redes que usam apenas configuração estática podem não oferecer DHCP.

O DHCP é um protocolo da camada de aplicação transportado sobre UDP. Servidores DHCPv4 normalmente usam a porta UDP 67, e clientes, a porta 68.

:::single-choice{#dhcp-relay-purpose} O que um retransmissor DHCP possibilita?

::option[Que cada cliente escolha um endereço sem qualquer política.]{#dhcp-client-any-address explanation="O servidor ainda aplica a política de escopo e concessão."}
::option[Que clientes em outra sub-rede alcancem um servidor DHCP centralizado.]{#dhcp-central-server .correct explanation="O retransmissor encaminha as trocas DHCP através de um limite de roteamento e identifica a rede do cliente."}
::option[Que switches Ethernet substituam todos os roteadores IP.]{#dhcp-switch-router explanation="A retransmissão de DHCP não elimina os limites entre redes roteadas."}
:::

## Troca inicial do DHCPv4

O processo inicial comum é lembrado como DORA:

1. `DHCPDISCOVER`: um cliente procura servidores disponíveis.
2. `DHCPOFFER`: um servidor propõe um endereço e opções.
3. `DHCPREQUEST`: o cliente seleciona e solicita uma concessão oferecida.
4. `DHCPACK`: o servidor selecionado confirma a concessão e as opções.

Os detalhes de broadcast e unicast variam conforme o estado do cliente, o uso de retransmissores e os recursos do servidor. Uma oferta ainda não é a concessão final utilizável; a confirmação conclui a troca normal de seleção.

:::single-choice{#dhcp-dora-order} Qual é a ordem inicial normal do DHCPv4?

::option[OFFER, DISCOVER, ACK, REQUEST.]{#dhcp-wrong-order-one explanation="Um cliente descobre antes de um servidor oferecer, e solicita antes da confirmação."}
::option[DISCOVER, OFFER, REQUEST, ACK.]{#dhcp-correct-order .correct explanation="A sequência procura, propõe, seleciona e confirma."}
::option[REQUEST, ACK, DISCOVER, OFFER.]{#dhcp-wrong-order-two explanation="Um novo cliente normalmente precisa da descoberta e de uma oferta antes de selecionar uma concessão."}
:::

## Renovação da concessão

Uma concessão expira se não for renovada. Normalmente, o cliente começa a renovação antes do vencimento, muitas vezes contatando primeiro o servidor original diretamente. Se a renovação não tiver sucesso, mais tarde ele amplia a tentativa de revinculação. Os temporizadores exatos são fornecidos ou derivados de acordo com o protocolo.

Um endereço exibido como atribuído dinamicamente não comprova que sua concessão permanecerá para sempre. Ao solucionar alterações, registre a concessão ativa, sua duração, o servidor e as opções.

:::single-choice{#dhcp-lease-expiration} O que acontece com a concessão de um endereço DHCP sem uma renovação bem-sucedida?

::option[Ela se torna um endereço MAC de hardware permanente.]{#dhcp-lease-mac explanation="Uma concessão IP não altera a identidade da camada de enlace."}
::option[Ela acaba expirando, e o cliente deve deixar de tratá-la como válida.]{#dhcp-lease-expires .correct explanation="As concessões permitem que endereços e opções sejam recuperados ou alterados conforme a política do servidor."}
::option[Ela transforma o cliente na raiz autoritativa do DNS.]{#dhcp-lease-dns-root explanation="Uma concessão DHCP não concede autoridade de DNS."}
:::

## Inspecionando o resultado

Depois que um cliente configura o DHCP, verifique todo o estado necessário, não apenas o endereço:

```bash
$ ip address show
$ ip route show
$ resolvectl status
```

O comando do resolvedor varia conforme o sistema. Inspecione também os dados da concessão e os logs do gerenciador de rede ativo. Endereços duplicados ainda podem ocorrer por servidores não autorizados, atribuições estáticas dentro de um conjunto, estado obsoleto ou configuração manual; o DHCP reduz erros, mas não pode impedir todo conflito por si só.

:::single-choice{#dhcp-result-verification} O que deve ser verificado depois que uma concessão DHCP é aceita?

::option[Apenas o nome exibido da interface.]{#dhcp-interface-name-only explanation="O nome de uma interface não comprova o endereçamento, o roteamento nem a resolução."}
::option[Apenas se o teclado responde.]{#dhcp-keyboard explanation="A entrada do teclado não tem relação com a configuração da concessão de rede."}
::option[Endereço, rotas, DNS e detalhes da concessão.]{#dhcp-check-complete-state .correct explanation="Uma configuração utilizável depende de várias opções e do estado delas aplicado ao sistema."}
:::

## DHCPv6 e configuração IPv6

Hosts IPv6 podem usar Configuração Automática de Endereço sem Estado, DHCPv6, configuração estática ou combinações. O DHCPv6 não usa a troca DORA do IPv4, e as informações do roteador padrão normalmente vêm dos Anúncios de Roteador IPv6, não do DHCPv6.

:::single-choice{#dhcp-ipv6-default-router} Onde um host IPv6 normalmente aprende as informações de seu roteador padrão?

::option[Nos Anúncios de Roteador IPv6.]{#dhcp-router-advertisement .correct explanation="O DHCPv6 pode fornecer outras configurações, mas os roteadores se anunciam por meio da Descoberta de Vizinhos."}
::option[Em um trailer FCS do Ethernet.]{#dhcp-ipv6-fcs explanation="A FCS detecta corrupção no enlace e não transporta configuração de roteadores."}
::option[Apenas em um DHCPACK do IPv4.]{#dhcp-ipv4-ack explanation="Mensagens DHCP do IPv4 não configuram o roteamento IPv6."}
:::

## Resumo

Agora você pode explicar como o DHCPv4 concede e renova a configuração de rede de um host.

1. Diferencie servidores DHCP de retransmissores e sub-redes de clientes.
2. Acompanhe a troca DISCOVER, OFFER, REQUEST e ACK.
3. Trate endereços e opções como estado de concessão por tempo limitado.
4. Verifique em conjunto endereço, rotas, DNS e metadados da concessão.
5. Mantenha o comportamento do DHCPv4 distinto da configuração automática do IPv6.
