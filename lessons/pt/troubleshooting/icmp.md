---
lesson_id: "icmp"
course_id: "troubleshooting"
lang: "pt"
order_index: 1
title: "ICMP"
description: "Aprenda como o ICMP relata erros IP, apoia diagnósticos e permite comportamentos essenciais de IPv4 e IPv6."
meta_title: "ICMP - Solução de Problemas"
meta_description: "Este tutorial Linux ajuda você a aprender redes Linux explicando o protocolo ICMP. Entenda os tipos e códigos de mensagens ICMP para solução eficaz de problemas de rede."
meta_keywords: "ICMP, protocolo ICMP, solução de problemas de rede, tipos ICMP, redes Linux, aprender Linux, tutorial Linux, labex linux, iniciante, guia"
---

Internet Control Message Protocol transporta informações de controle, erro e diagnóstico junto ao IP. ICMP para IPv4 e ICMPv6 são protocolos relacionados, mas distintos, com números de tipos e responsabilidades diferentes.

## Tipos, códigos e checksums

Uma mensagem ICMP tem tipo, um código mais específico quando aplicável e checksum. Mensagens de erro normalmente incluem parte do pacote causador para que o remetente associe o erro a um fluxo.

:::single-choice{#icmp-code-purpose} O que um código ICMP fornece?

::option[Um nome DNS permanente do roteador.]{#icmp-code-dns explanation="A resolução de nomes não é a finalidade desse campo."}
::option[Um significado mais específico dentro do tipo.]{#icmp-code-specific .correct explanation="Por exemplo, códigos de destino inalcançável distinguem motivos da falha."}
::option[O payload completo de todos os pacotes anteriores.]{#icmp-code-all-payload explanation="Um erro cita apenas o necessário para identificação segundo o protocolo."}
:::

## Mensagens de eco e erro

No ICMPv4, Echo Request é tipo 8 e Echo Reply tipo 0. Destination Unreachable é tipo 3 e Time Exceeded tipo 11. ICMPv6 usa outros números; identifique a família antes de interpretar uma captura.

:::single-choice{#icmpv4-echo-request-type} Qual é o tipo do ICMPv4 Echo Request?

::option[0]{#icmp-type-zero explanation="Tipo zero é o Echo Reply do ICMPv4."}
::option[11]{#icmp-type-eleven explanation="Tipo onze é Time Exceeded no ICMPv4."}
::option[8]{#icmp-type-eight .correct explanation="Ping normalmente envia essa mensagem para solicitar resposta."}
:::

## Path MTU e ICMP essencial

ICMP não é apenas tráfego opcional de ping. Erros IPv4 de fragmentação necessária e mensagens ICMPv6 Packet Too Big sustentam Path MTU Discovery. ICMPv6 também transporta Neighbor Discovery e Router Advertisements. Bloquear tudo pode criar black holes e quebrar IPv6.

Filtre por tipo necessário, direção, taxa e escopo, não por regra total. Atacantes podem falsificar ICMP; valide o pacote citado e compare rotas e capturas locais.

:::single-choice{#icmp-block-all-risk} Por que bloquear todo ICMP pode quebrar tráfego válido?

::option[Toda resposta HTTP é transportada em Echo Reply.]{#icmp-http-echo explanation="HTTP normalmente usa TCP ou QUIC."}
::option[ICMP armazena todas as senhas de aplicativos.]{#icmp-passwords explanation="Ele não é banco de credenciais."}
::option[ICMP carrega informações necessárias de MTU e controle IPv6.]{#icmp-essential-control .correct explanation="Suprimi-las pode impedir dimensionamento, descoberta de vizinhos ou roteadores."}
:::

## Interpretação do silêncio

Ausência de resposta pode significar filtro, rate limit, rota assimétrica, falta de rota de retorno, host desligado ou dispositivo que ignora a mensagem. Um erro também pode vir de um dispositivo intermediário.

:::single-choice{#icmp-silence-meaning} O que a ausência de Echo Reply prova sozinha?

::option[Que o aplicativo-alvo certamente parou.]{#icmp-silence-app-down explanation="O serviço pode funcionar enquanto eco é filtrado."}
::option[Que o hostname foi removido do DNS.]{#icmp-silence-dns-deleted explanation="Uma sondagem por endereço pode ficar silenciosa independentemente do DNS."}
::option[Apenas que essa troca de echo não produziu uma resposta observada.]{#icmp-silence-limited .correct explanation="São necessárias evidências adicionais de rota, transporte, aplicação e captura para identificar a causa."}
:::

## Resumo

Agora você consegue interpretar ICMP como evidência de controle, não veredito binário.

1. Ler tipo e código na família IP correta.
2. Reconhecer eco, unreachable e time exceeded.
3. Preservar ICMP necessário a MTU e IPv6.
4. Correlacionar erros e silêncio com outras evidências.
