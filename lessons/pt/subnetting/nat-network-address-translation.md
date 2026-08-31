---
lesson_id: "nat-network-address-translation"
course_id: "subnetting"
lang: "pt"
order_index: 6
title: "NAT"
description: "Aprenda como a tradução de origem, destino e portas modifica fluxos IPv4 e o estado das conexões."
meta_title: "NAT - Sub-redes"
meta_description: "Aprenda sobre NAT (Tradução de Endereços de Rede) no Linux, como ele funciona e sua relação com a segurança de rede. Entenda IPs privados e públicos neste guia de redes Linux."
meta_keywords: "NAT, Tradução de Endereços de Rede, redes Linux, IP privado, IP público, tutorial Linux, guia para iniciantes"
---

A Tradução de Endereços de Rede reescreve campos de endereço e, frequentemente, portas de transporte à medida que os pacotes atravessam um dispositivo de tradução. Ela é amplamente usada para conectar redes IPv4 com endereços privados por meio de um conjunto menor de endereços roteáveis externamente.

## Tradução de origem

O NAT de origem substitui o endereço de origem de um pacote quando ele sai de uma rede. Implantações de muitos para um também traduzem portas de origem para que vários fluxos internos possam compartilhar um endereço externo. Essa forma que considera portas costuma ser chamada de NAPT, PAT ou mascaramento quando o endereço externo pode mudar.

O tradutor acompanha os mapeamentos para que os pacotes de resposta possam ser reescritos de volta ao ponto de extremidade interno original. Normalmente, ele encaminha o mesmo fluxo de transporte; não precisa abrir uma conexão de proxy separada como faria um proxy de aplicação.

:::single-choice{#nat-source-translation}
O que o NAT de origem altera em um pacote de saída?

::option[Apenas as permissões de arquivo da aplicação de destino.]{#nat-file-permissions explanation="O NAT opera nos cabeçalhos de rede e transporte, não em sistemas de arquivos remotos."}
::option[O endereço de origem e, no uso de muitos para um, frequentemente a porta de origem.]{#nat-source-fields .correct explanation="O mapeamento permite associar o tráfego de retorno ao fluxo interno original."}
::option[O nome DNS armazenado permanentemente pelo cliente.]{#nat-dns-name explanation="A tradução não reescreve o banco de dados de serviços de nomes do cliente."}
:::

## Tradução de destino

O NAT de destino reescreve o endereço ou a porta de destino, normalmente para publicar um serviço interno por meio de um ponto de extremidade externo. Uma regra de encaminhamento de portas pode mapear uma porta TCP externa para um endereço e uma porta internos diferentes. O tráfego de retorno precisa de uma tradução reversa consistente.

:::single-choice{#nat-port-forward}
Qual forma de NAT normalmente implementa um encaminhamento de porta de entrada?

::option[Apenas NAT de origem, antes da consulta de rota.]{#nat-snat-port-forward explanation="Publicar um destino interno exige a tradução dos campos de destino."}
::option[Nenhuma tradução de endereço ou porta.]{#nat-no-translation explanation="Uma regra de encaminhamento de porta é, por definição, uma política de tradução."}
::option[NAT de destino.]{#nat-dnat .correct explanation="O DNAT mapeia o destino externo para o ponto de extremidade do serviço interno selecionado."}
:::

## NAT e política de firewall

NAT não é um firewall. Um tradutor com estado pode não ter um mapeamento para tráfego de entrada não solicitado, mas o encaminhamento explícito, a tradução de destino, a filtragem e a exposição da aplicação determinam o que está acessível. A política de segurança deve ser expressa e auditada com regras de firewall, serviços de privilégio mínimo e controles de ponta a ponta, em vez de ser deduzida da reescrita de endereços.

:::single-choice{#nat-not-firewall}
Por que o NAT não deve ser tratado como uma política de segurança por si só?

::option[O NAT criptografa automaticamente toda carga útil.]{#nat-encrypts explanation="A tradução de endereços não fornece confidencialidade à carga útil."}
::option[Regras de tradução e regras de filtragem de tráfego têm finalidades diferentes.]{#nat-filter-separate .correct explanation="A acessibilidade e a autorização exigem políticas explícitas de filtragem e serviço, mesmo quando há tradução."}
::option[O NAT impede que administradores definam regras de firewall.]{#nat-prevents-firewall explanation="A tradução e a política de firewall normalmente coexistem."}
:::

## Consequências operacionais

O NAT pode esgotar os mapeamentos de endereços e portas, complicar protocolos ponto a ponto, ocultar das aplicações as origens reais e exigir tratamento especial para protocolos que incorporam endereços. Se for necessário rastrear fluxos, os logs devem preservar os horários das traduções e os detalhes dos mapeamentos.

No Linux, as políticas modernas costumam ser configuradas com nftables e rastreamento de conexões. Inspecione o conjunto de regras real antes de alterá-lo:

```bash
$ sudo nft list ruleset
$ sudo conntrack -L
```

O segundo comando exige as ferramentas conntrack e privilégios. Alterações no conjunto de regras podem desconectar o acesso remoto; portanto, use recuperação por console, configuração atômica, validação e reversão.

:::single-choice{#nat-trace-flow}
Quais evidências são necessárias para rastrear um fluxo de endereço compartilhado até um cliente interno?

::option[Apenas o endereço externo, sem horário nem porta.]{#nat-address-only explanation="Muitos clientes e fluxos podem compartilhar esse endereço."}
::option[Apenas o nome de host exibido pelo cliente.]{#nat-hostname-only explanation="O tradutor mapeia tuplas de pacotes, não necessariamente nomes de host."}
::option[Um mapeamento de tradução correlacionado no tempo, incluindo protocolo e portas.]{#nat-correlated-mapping .correct explanation="A tupla completa e o registro de horário diferenciam fluxos traduzidos simultâneos."}
:::

## Resumo

Agora você pode diferenciar tradução de endereços, roteamento, proxy e política de firewall.

1. Identifique a tradução de origem nos fluxos de saída.
2. Identifique a tradução de destino nos serviços publicados.
3. Entenda como os mapeamentos de portas permitem o compartilhamento de endereços.
4. Aplique filtragem explícita em vez de tratar o NAT como segurança.
5. Preserve evidências de mapeamento e acesso de recuperação durante alterações.
