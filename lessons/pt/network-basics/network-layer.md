---
lesson_id: "network-layer"
course_id: "network-basics"
lang: "pt"
order_index: 7
title: "Camada de rede"
description: "Aprenda como endereçamento IP, prefixos, tabelas de roteamento e limites de saltos transportam pacotes entre redes."
meta_title: "Camada de rede - Fundamentos de rede"
meta_description: "Explore a camada de Rede nas redes Linux. Este guia explica como endereços IP e sub-redes permitem o roteamento de pacotes para a transmissão de dados entre redes."
meta_keywords: "camada de Rede, endereços IP, sub-redes, redes Linux, roteamento de pacotes, transmissão de dados, modelo OSI, pacote IP"
---

A camada de rede fornece endereçamento lógico e entrega de pacotes por melhor esforço através de redes interconectadas. Na suíte de protocolos da Internet, IPv4 e IPv6 transportam pacotes enquanto os roteadores escolhem o próximo salto em direção a cada destino.

## Pacotes IP

Um cabeçalho IP inclui endereços de origem e destino, além dos campos necessários ao encaminhamento e ao processamento do protocolo. A carga útil geralmente contém um segmento TCP, um datagrama UDP ou uma mensagem ICMP. O IP não garante chegada, ordem nem ausência de duplicatas.

:::single-choice{#network-layer-ip-service}
Qual serviço de entrega o IP fornece por si só?

::option[Confirmações garantidas de transações da aplicação.]{#network-layer-guaranteed-commit explanation="O resultado de uma entrega IP não pode comprovar a persistência da aplicação."}
::option[Entrega de pacotes por melhor esforço.]{#network-layer-best-effort .correct explanation="As camadas superiores ou as aplicações acrescentam qualquer recuperação ou ordenação necessária."}
::option[Reserva permanente de um cabo físico.]{#network-layer-cable-reservation explanation="O encaminhamento de pacotes não reserva um caminho físico dedicado."}
:::

## Prefixos e sub-redes

Um endereço e um comprimento de prefixo definem quais bits iniciais formam um prefixo de rede. Os hosts usam essas informações e suas rotas para decidir se um destino está no enlace ou exige um roteador de próximo salto. Uma sub-rede é um intervalo de endereços sob um prefixo e uma política; sub-redes não estão automaticamente conectadas a todas as outras sub-redes.

:::single-choice{#network-layer-prefix-decision}
O que ajuda um host a decidir se um destino IPv4 está no enlace?

::option[A senha da aplicação no destino.]{#network-layer-password explanation="Os dados de autenticação não definem prefixos de rede."}
::option[A cor do cabo Ethernet.]{#network-layer-cable-color explanation="A aparência do cabo não possui semântica de endereçamento."}
::option[Seus prefixos configurados e sua tabela de roteamento.]{#network-layer-prefix-routes .correct explanation="O host compara os destinos com as rotas, inclusive os prefixos conectados."}
:::

## Decisões de roteamento

O Linux consulta as políticas e as tabelas de roteamento para selecionar uma interface de saída, um próximo salto e as informações de origem preferidas. Entre rotas igualmente elegíveis, normalmente é preferido o prefixo correspondente mais específico. Inspecione a decisão real para um destino com:

```bash
$ ip route get 203.0.113.10
```

Essa é uma consulta de rota local, não uma prova de que todos os roteadores seguintes possuem uma rota funcional nem de que o destino aceita tráfego.

:::single-choice{#network-layer-longest-prefix}
Qual rota normalmente vence entre as rotas elegíveis para o mesmo destino?

::option[A rota cujo nome de interface vem primeiro em ordem alfabética.]{#network-layer-alphabetical explanation="A grafia da interface não é a regra de seleção."}
::option[A rota mais antiga, independentemente de seu prefixo.]{#network-layer-oldest explanation="A idade por si só não prevalece sobre a correspondência de prefixos."}
::option[A rota com o prefixo correspondente mais específico.]{#network-layer-most-specific .correct explanation="A correspondência de prefixo mais longo escolhe a rota que abrange o intervalo de endereços correspondente mais estreito."}
:::

## Limites de saltos e alterações no encaminhamento

Cada pacote IPv4 possui um TTL e cada pacote IPv6, um Limite de Saltos. Um roteador reduz esse valor; quando ele chega a zero, o roteador descarta o pacote e pode enviar um erro ICMP. Isso impede que loops de encaminhamento circulem indefinidamente.

Normalmente, os roteadores preservam os endereços IP de ponta a ponta, mas NAT, túneis, proxies e outros dispositivos intermediários podem transformar ou encapsular os pacotes. Os cabeçalhos da camada de enlace mudam em cada salto roteado de qualquer forma.

:::single-choice{#network-layer-hop-limit}
Por que o TTL ou o Limite de Saltos é reduzido pelos roteadores?

::option[Para aumentar as permissões de arquivo da aplicação.]{#network-layer-hop-permissions explanation="A contagem de saltos não tem relação com a autorização do sistema de arquivos."}
::option[Para converter todos os pacotes de IPv4 para IPv6.]{#network-layer-hop-convert explanation="A tradução de protocolos não é a finalidade do campo."}
::option[Para impedir que os pacotes fiquem em loop para sempre.]{#network-layer-prevent-loop .correct explanation="Uma contagem finita de saltos garante que um loop de roteamento persistente acabe descartando o pacote."}
:::

## Resumo

Agora você pode explicar como um host IP seleciona a próxima etapa em direção a um destino.

1. Trate a entrega IP como melhor esforço.
2. Use prefixos e rotas para diferenciar destinos no enlace e destinos roteados.
3. Aplique a correspondência de prefixo mais longo à seleção de rotas.
4. Reconheça como os limites de saltos restringem loops de encaminhamento.
