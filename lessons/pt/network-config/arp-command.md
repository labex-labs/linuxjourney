---
lesson_id: "arp-command"
course_id: "network-config"
lang: "pt"
order_index: 5
title: "arp"
description: "Aprenda a inspecionar e interpretar o estado do cache de vizinhos ARP IPv4 e IPv6 no Linux."
meta_title: "arp - Configuração de Rede"
meta_description: "Aprenda sobre o comando ARP do Linux e como visualizar seu cache ARP. Entenda o papel do ARP na comunicação de rede. Um guia para iniciantes em ARP."
meta_keywords: "Linux ARP, cache ARP, ip neighbour show, comandos de rede, rede Linux, Linux para iniciantes, tutorial Linux"
---

O Linux guarda endereços de enlace de próximos saltos resolvidos recentemente na tabela de vizinhos. Para IPv4 sobre Ethernet, as entradas são aprendidas por ARP; IPv6 usa Neighbor Discovery. O comando legado `arp` mostra apenas parte do estado, enquanto `ip neighbor` cobre ambas as famílias.

## Visualização das entradas

Examine todas as entradas ou uma interface:

```bash
$ ip neighbor show
$ ip neighbor show dev enp1s0
```

Uma entrada inclui IP, endereço da camada de enlace, dispositivo e estado de alcance. A tabela pode estar vazia após o boot e ser preenchida conforme o tráfego exige próximos saltos locais.

:::single-choice{#arp-command-modern-view} Qual comando mostra o estado moderno da tabela de vizinhos?

::option[`pwd neighbor`]{#arp-command-pwd explanation="Pwd informa o diretório de trabalho do shell."}
::option[`ip neighbor show`]{#arp-command-ip-neighbor .correct explanation="Ele informa entradas derivadas de ARP IPv4 e Neighbor Discovery IPv6."}
::option[`route --passwords`]{#arp-command-route-passwords explanation="Uma inspeção de rotas não deve expor credenciais."}
:::

## Resolução de um vizinho IPv4

Quando falta o mapeamento de um IPv4 no mesmo link, o host transmite uma solicitação ARP perguntando quem possui o endereço. O alvo, ou um roteador com proxy ARP explícito, responde. O remetente armazena o mapeamento e envia o quadro aguardando.

Para um destino IP remoto, o host resolve o endereço do gateway escolhido, não o MAC do host remoto.

:::single-choice{#arp-command-remote-target} Qual vizinho IPv4 o host resolve para um destino fora do link?

::option[O servidor remoto final, atravessando todos os roteadores.]{#arp-command-final-server explanation="O MAC do servidor remoto não tem significado no link de origem."}
::option[Todo servidor DNS configurado no resolver.]{#arp-command-all-dns explanation="A resolução de vizinhos segue a rota escolhida, não a lista DNS."}
::option[O gateway selecionado no mesmo link.]{#arp-command-gateway .correct explanation="O quadro Ethernet local é endereçado ao roteador que encaminha o pacote IP."}
:::

## Interpretação dos estados

Estados comuns incluem `REACHABLE`, `STALE`, `DELAY`, `PROBE`, `INCOMPLETE` e `FAILED`. `STALE` significa que a confirmação recente expirou; o endereço armazenado ainda pode ser usado enquanto a pilha testa conforme necessário. `FAILED` indica que a resolução ou detecção não teve êxito, com causas possíveis em link, VLAN, endereço, rota, filtro ou peer desligado.

:::single-choice{#arp-command-stale-state} `STALE` significa que o vizinho é sabidamente inalcançável?

::option[Não; falta confirmação recente e ele pode ser testado ao ser usado.]{#arp-command-stale-probe .correct explanation="Esse estado não equivale a `FAILED`."}
::option[Sim, e a entrada nunca mais pode ser usada.]{#arp-command-stale-dead explanation="Entradas stale continuam candidatas e podem mudar após testes."}
::option[Sim, porque seu registro DNS expirou.]{#arp-command-stale-dns explanation="Estado do vizinho e cache DNS são separados."}
:::

## Alteração cuidadosa do estado

Entradas estáticas e limpezas mudam o estado, podem interromper tráfego e apagar evidências. Capture primeiro rotas, contadores e vizinhos. Prefira uma sondagem direcionada e captura de pacotes em rede de teste autorizada antes de limpar toda uma interface.

ARP não tem autenticação embutida; endereços duplicados ou respostas falsas podem envenenar mapeamentos. Proteções do switch, segmentação, monitoramento e autenticação em camadas superiores reduzem o impacto.

:::single-choice{#arp-command-flush-first} Por que não limpar toda a tabela como primeiro diagnóstico?

::option[As entradas ficam apenas nos servidores DNS raiz.]{#arp-command-neighbors-dns explanation="Elas são mantidas pela pilha local."}
::option[A limpeza remove permanentemente o hardware.]{#arp-command-flush-hardware explanation="Ela remove cache, não dispositivos físicos."}
::option[Ela altera evidências e pode interromper próximos saltos funcionais.]{#arp-command-flush-disrupts .correct explanation="Inspeção somente leitura e testes direcionados preservam o estado necessário ao diagnóstico."}
:::

## Resumo

Agora você consegue inspecionar a resolução de vizinhos sem tratar todo estado de cache como falha.

1. Usar `ip neighbor` para estados IPv4 e IPv6.
2. Resolver o destino somente quando ele está no link.
3. Resolver o gateway para tráfego IP fora do link.
4. Preservar evidências antes de mudanças direcionadas.
