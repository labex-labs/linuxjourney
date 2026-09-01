---
lesson_id: "ipv6"
course_id: "subnetting"
lang: "pt"
order_index: 7
title: "IPv6"
description: "Aprenda a ler endereços IPv6, prefixos, escopos, configuração automática e estado de roteamento no Linux."
meta_title: "IPv6 - Sub-redes"
meta_description: "Um guia de introdução ao protocolo IPv6. Aprenda por que o IPv6 foi criado, como ele difere do IPv4 e entenda os fundamentos de seu esquema de endereçamento para redes Linux modernas."
meta_keywords: "IPv6, IPv4, endereço IP, redes Linux, protocolos de rede, protocolo de internet, esgotamento de endereços, iniciante, tutorial, guia"
---

O IPv6 usa endereços de 128 bits e foi projetado para oferecer um espaço de endereços muito maior, junto com comportamentos atualizados de pacotes e descoberta de vizinhos. IPv4 e IPv6 são protocolos separados; hosts de pilha dupla podem executar ambos durante a transição das redes.

## Lendo a notação IPv6

Um endereço IPv6 é escrito como oito grupos hexadecimais de 16 bits:

```text
2001:0db8:0000:0000:0000:0000:0000:0025
```

Os zeros iniciais de cada grupo podem ser omitidos, e uma sequência consecutiva de grupos formados por zeros pode ser comprimida com `::`:

```text
2001:db8::25
```

Apenas um `::` pode aparecer, pois, caso contrário, a quantidade de grupos omitidos seria ambígua. `2001:db8::/32` é reservado para exemplos de documentação.

:::single-choice{#ipv6-double-colon-rule} Por que `::` pode aparecer no máximo uma vez em um endereço IPv6?

::option[Vários marcadores `::` tornariam a expansão ambígua.]{#ipv6-compression-ambiguity .correct explanation="Um marcador de compressão pode ser expandido para a quantidade exata de grupos necessária para chegar a oito."}
::option[Endereços IPv6 contêm apenas um bit zero.]{#ipv6-one-zero explanation="Um endereço pode conter muitos bits zero e grupos formados por zeros."}
::option[O marcador seleciona a porta TCP zero.]{#ipv6-port-zero explanation="A compressão do endereço não tem relação com as portas de transporte."}
:::

## Tipos de endereço e escopo

Entre os endereços e intervalos importantes estão:

- `::1/128`: loopback no host local.
- `fe80::/10`: unicast link-local; normalmente presente nas interfaces IPv6.
- `2000::/3`: espaço unicast global atualmente alocado.
- `ff00::/8`: multicast.

O IPv6 não possui endereço de broadcast; multicast e Descoberta de Vizinhos atendem a casos de uso que o IPv4 costuma tratar com broadcast. Um destino link-local pode exigir uma zona de interface, como `fe80::1%eth0`, pois o mesmo prefixo existe em todos os enlaces.

:::single-choice{#ipv6-link-local-scope} Qual é o escopo normal de um endereço `fe80::/10`?

::option[Todos os hosts da Internet global.]{#ipv6-global-link-local explanation="Endereços unicast globais atendem ao escopo global roteado."}
::option[Apenas um arquivo de zona DNS.]{#ipv6-dns-only explanation="Endereços link-local são atribuídos a interfaces e usados em redes."}
::option[Um enlace local.]{#ipv6-one-link .correct explanation="Roteadores não encaminham tráfego link-local comum entre enlaces."}
:::

## Prefixos e endereços de interface

A notação CIDR do IPv6 usa um comprimento de prefixo de `/0` a `/128`. Um `/64` é o tamanho padrão para a maioria das sub-redes LAN e permite a Configuração Automática de Endereço sem Estado. Uma interface pode conter simultaneamente endereços link-local, globais estáveis, temporários de privacidade e outros, cada um com durações preferencial e válida.

:::single-choice{#ipv6-address-multiplicity} Por que uma interface pode mostrar vários endereços IPv6?

::option[O IPv6 exige um endereço para cada dígito hexadecimal.]{#ipv6-one-per-digit explanation="Os dígitos são uma representação, não atribuições separadas à interface."}
::option[Diferentes escopos e papéis de privacidade ou duração podem coexistir.]{#ipv6-several-roles .correct explanation="É normal ter um endereço link-local e um ou mais endereços globais ou temporários."}
::option[Cada endereço identifica uma placa de rede física separada.]{#ipv6-separate-card explanation="Uma interface pode possuir vários endereços."}
:::

## Descoberta de vizinhos e roteadores

A Descoberta de Vizinhos do IPv6 usa ICMPv6 para resolução de endereços, detecção de endereços duplicados, descoberta de roteadores e informações de acessibilidade. Anúncios de Roteador podem fornecer prefixos e informações do roteador padrão. Os hosts podem combinar SLAAC com DHCPv6 para outras configurações; normalmente, o DHCPv6 não fornece o roteador padrão.

Bloquear todo o ICMPv6 interrompe comportamentos essenciais do protocolo. A política de firewall deve permitir os tipos de mensagem necessários com o escopo apropriado, em vez de tratar o ICMPv6 como opcional.

:::single-choice{#ipv6-default-router-source} Como um host IPv6 normalmente aprende um roteador padrão de forma dinâmica?

::option[Por meio de Anúncios de Roteador.]{#ipv6-router-advertisements .correct explanation="A Descoberta de Roteadores faz parte da Descoberta de Vizinhos do ICMPv6."}
::option[Por um endereço de broadcast Ethernet.]{#ipv6-ethernet-broadcast explanation="O IPv6 não usa um endereço IP de broadcast."}
::option[Pelo handshake TCP de três vias.]{#ipv6-tcp-handshake explanation="O TCP estabelece o estado de transporte depois que o roteamento já está disponível."}
:::

## Inspecionando e testando o IPv6

Inspecione endereços, rotas e vizinhos de forma independente:

```bash
$ ip -6 address show
$ ip -6 route show
$ ip -6 neighbor show
$ ping -6 -c 3 2001:db8::25
```

Use um endereço de teste realmente atribuído, não o endereço de documentação mostrado. Uma aplicação de pilha dupla pode funcionar por IPv4 enquanto o IPv6 está com falha, ou vice-versa; portanto, teste explicitamente cada família e seus registros DNS `A` ou `AAAA`.

:::single-choice{#ipv6-dual-stack-test} Por que testar IPv4 e IPv6 separadamente em um serviço de pilha dupla?

::option[Todo pacote IPv6 precisa primeiro se tornar um broadcast IPv4.]{#ipv6-becomes-ipv4 explanation="IPv6 e IPv4 nativos são caminhos de protocolo distintos."}
::option[As duas famílias podem ter DNS, rotas, filtros e falhas diferentes.]{#ipv6-independent-paths .correct explanation="Um fallback bem-sucedido pode ocultar uma família de endereços preferida com falha."}
::option[Ferramentas IPv6 não conseguem exibir o estado das interfaces.]{#ipv6-tools-cannot explanation="Os comandos `ip -6` expõem o estado de endereços, rotas e vizinhos."}
:::

## Resumo

Agora você pode ler e testar estados comuns de interfaces e roteamento IPv6.

1. Expanda ou comprima corretamente oito grupos hexadecimais de endereço.
2. Diferencie os escopos de loopback, link-local, global e multicast.
3. Espere vários endereços IPv6 e durações em uma interface.
4. Preserve o tráfego necessário de Descoberta de Vizinhos e Anúncios de Roteador.
5. Teste os caminhos IPv4 e IPv6 de forma independente em serviços de pilha dupla.
