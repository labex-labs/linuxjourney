---
lesson_id: "link-layer"
course_id: "network-basics"
lang: "pt"
order_index: 8
title: "Camada de enlace"
description: "Aprenda como quadros Ethernet, descoberta de vizinhos, switches e roteadores entregam pacotes em um enlace local."
meta_title: "Camada de enlace - Fundamentos de rede"
meta_description: "Explore os fundamentos da camada de enlace do TCP/IP. Aprenda como o cabeçalho da camada de enlace é construído, como o ARP resolve endereços IP para endereços MAC e como os pacotes atravessam uma rede local."
meta_keywords: "camada de enlace, cabeçalho da camada de enlace, ARP, TCP/IP, endereço MAC, fundamentos de rede, redes Linux, percurso de pacotes, protocolo de resolução de endereços"
---

A camada de enlace transporta pacotes da camada de rede através de um meio local ou enlace virtual. Ethernet e Wi-Fi usam detalhes de enquadramento diferentes, mas ambos fornecem entrega local abaixo do IP.

## Quadros Ethernet

Um quadro Ethernet contém endereços MAC de destino e origem, um campo EtherType ou de comprimento, uma carga útil e um trailer de sequência de verificação do quadro. A transmissão física também usa um preâmbulo e um delimitador de início. A sequência de verificação detecta corrupção no enlace; ela não repara um quadro danificado nem o protege criptograficamente.

:::single-choice{#link-layer-fcs-purpose}
Para que a sequência de verificação do quadro Ethernet é usada?

::option[Detectar corrupção do quadro no enlace.]{#link-layer-detect-corruption .correct explanation="Um receptor pode descartar um quadro que falhe na verificação de integridade."}
::option[Criptografar a carga útil em todos os saltos roteados.]{#link-layer-fcs-encryption explanation="A FCS é um código de detecção de erros, não criptografia ou autenticação."}
::option[Selecionar uma aplicação pela porta TCP.]{#link-layer-fcs-port explanation="As portas de transporte são carregadas dentro da carga útil IP."}
:::

## Switches e entrega local

Um switch Ethernet aprende quais endereços MAC de origem aparecem em suas portas e encaminha quadros unicast conhecidos em direção à porta aprendida para o destino. Tráfego de broadcast e algum tráfego de destino desconhecido é inundado dentro do domínio de broadcast. VLANs podem dividir um sistema de comutação em domínios lógicos de enlace separados.

:::single-choice{#link-layer-switch-learning}
Quais informações um switch Ethernet normalmente aprende com os quadros?

::option[Senhas de aplicações e cookies HTTP.]{#link-layer-switch-passwords explanation="Uma tabela básica de encaminhamento usa endereços de enlace, não credenciais de aplicações."}
::option[A tabela completa de roteamento da Internet de cada roteador.]{#link-layer-switch-routing-table explanation="A comutação de Camada 2 e a troca de rotas globais são funções diferentes."}
::option[Endereços MAC de origem associados às portas do switch.]{#link-layer-switch-source .correct explanation="Esse aprendizado constrói a tabela de encaminhamento usada posteriormente para tráfego unicast conhecido."}
:::

## Resolvendo o endereço do próximo salto

Para IPv4 sobre Ethernet, o Protocolo de Resolução de Endereços mapeia um endereço IPv4 de próximo salto no enlace para um endereço MAC. Primeiro, o host verifica seu cache de vizinhos. Se necessário, ele transmite uma solicitação ARP em broadcast, e o proprietário ou um proxy autorizado responde.

Para um destino IP fora do enlace, o host resolve o endereço MAC do gateway padrão ou selecionado — não o endereço MAC do destino remoto. O IPv6 usa a Descoberta de Vizinhos sobre ICMPv6 em vez de ARP.

:::single-choice{#link-layer-remote-destination-mac}
Qual endereço MAC um host usa para um destino IPv4 fora do enlace?

::option[O endereço MAC do roteador de próximo salto selecionado.]{#link-layer-gateway-mac .correct explanation="O pacote IP continua endereçado ao host remoto, enquanto o quadro local segue para o roteador."}
::option[O endereço MAC do servidor remoto através de todos os roteadores.]{#link-layer-remote-mac explanation="Endereços MAC são identificadores do enlace local e não são transportados de ponta a ponta."}
::option[Um endereço MAC derivado da porta TCP de destino.]{#link-layer-port-mac explanation="As portas de transporte não determinam os endereços de enlace."}
:::

## Inspecionando o estado dos vizinhos

Consulte as entradas ARP do IPv4 e de Descoberta de Vizinhos do IPv6 com:

```bash
$ ip neighbor show
```

Estados como `REACHABLE`, `STALE`, `DELAY`, `PROBE` e `FAILED` descrevem o processo de detecção de inacessibilidade dos vizinhos. `STALE` não significa falha; significa que a confirmação de acessibilidade em cache já não é recente e pode ser testada durante o uso.

:::single-choice{#link-layer-stale-neighbor}
O que uma entrada de vizinho `STALE` indica?

::option[O vizinho está permanentemente bloqueado pelo firewall.]{#link-layer-stale-blocked explanation="O estado não descreve a política do firewall."}
::option[O endereço MAC foi gravado em disco como backup.]{#link-layer-stale-backup explanation="O estado do vizinho é uma informação operacional do cache."}
::option[O mapeamento em cache não possui confirmação recente de acessibilidade.]{#link-layer-stale-confirmation .correct explanation="A pilha ainda pode usá-lo e realizar a detecção de acessibilidade conforme necessário."}
:::

## Encapsulamento através de um roteador

O remetente coloca um pacote IP dentro de um quadro endereçado ao próximo salto. O roteador valida e remove o quadro recebido, processa o cabeçalho IP, seleciona uma rota de saída e constrói um novo quadro para esse enlace. O receptor desfaz o encapsulamento e entrega a carga útil de transporte ao socket apropriado.

:::single-choice{#link-layer-router-reframing}
O que permanece igual no encaminhamento comum enquanto o enquadramento Ethernet muda em um roteador?

::option[O destino IP, a menos que um dispositivo intermediário, como um NAT, o altere.]{#link-layer-ip-destination .correct explanation="Roteadores comuns encaminham em direção ao destino IP final enquanto substituem os quadros locais de cada salto."}
::option[A sequência de verificação do quadro recebido.]{#link-layer-same-fcs explanation="Um novo quadro de saída recebe seu próprio valor de integridade do enlace."}
::option[O endereço MAC de destino em todos os enlaces.]{#link-layer-same-mac explanation="Cada enlace usa o endereço de enlace apropriado do próximo salto."}
:::

## Resumo

Agora você pode acompanhar um pacote IP em uma etapa de entrega pelo enlace local.

1. Identifique os principais campos do quadro Ethernet e o trailer de integridade.
2. Explique como um switch aprende os locais de encaminhamento na rede local.
3. Resolva um próximo salto IPv4 com ARP e vizinhos IPv6 com NDP.
4. Interprete o estado do cache de vizinhos sem presumir uma falha.
5. Reconheça que os roteadores reconstroem os quadros para cada enlace de saída.
