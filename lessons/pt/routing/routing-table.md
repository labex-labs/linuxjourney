---
lesson_id: "routing-table"
course_id: "routing"
lang: "pt"
order_index: 2
title: "Tabela de roteamento"
description: "Aprenda a ler rotas no Linux e inspecionar a rota selecionada para um destino."
meta_title: "Tabela de roteamento - Roteamento"
meta_description: "Um guia para entender a tabela de roteamento do Linux. Aprenda a interpretar a saída do comando route, incluindo destino, gateway, genmask e a interface eth0. Domine os fundamentos da tabela de rotas do Linux."
meta_keywords: "tabela de roteamento linux, tabela de rotas linux, genmask, eth0, comando route, roteamento de rede, roteamento IP, destino, gateway, máscara de sub-rede, redes linux"
---

O estado de roteamento do Linux determina quais próximos saltos, interfaces e origens são elegíveis para um destino IP. A visualização legada `route -n` ainda é encontrada, mas `ip route` expõe os conceitos modernos de roteamento do kernel de forma mais direta.

## Lendo rotas IPv4

Um exemplo de saída pode ser:

```text
$ ip -4 route show
default via 192.168.224.2 dev eth0 proto dhcp src 192.168.224.10 metric 100
192.168.224.0/24 dev eth0 proto kernel scope link src 192.168.224.10 metric 100
```

A rota `/24` conectada envia os destinos correspondentes diretamente por `eth0`. A rota padrão usa o gateway de próximo salto `192.168.224.2`. `proto` descreve como a rota foi instalada, `src` é uma origem preferida para o tráfego correspondente, e uma métrica ajuda a classificar rotas que, de outra forma, seriam comparáveis.

:::single-choice{#routing-table-via-meaning}
O que `via 192.168.224.2` indica?

::option[A única aplicação autorizada a usar a rota.]{#routing-table-application explanation="A autorização da aplicação não é codificada pela palavra-chave `via`."}
::option[O gateway de próximo salto da rota.]{#routing-table-next-hop .correct explanation="O pacote é enquadrado para esse roteador no enlace enquanto mantém seu destino IP."}
::option[O ponto de montagem da rota no sistema de arquivos.]{#routing-table-mount explanation="As entradas de roteamento tratam do encaminhamento de rede, não de sistemas de arquivos."}
:::

## Rotas conectadas e padrão

Uma rota com `scope link` e sem próximo salto `via` trata o prefixo como diretamente acessível pela interface. Uma rota padrão corresponde a todos os endereços, mas perde para qualquer rota elegível mais específica.

:::single-choice{#routing-table-connected-route}
Como um destino conectado com `scope link` é normalmente alcançado?

::option[Pelo gateway padrão, mesmo quando uma rota conectada corresponde.]{#routing-table-connected-default explanation="O prefixo conectado é mais específico e não possui operando de gateway."}
::option[Convertendo o destino em um servidor DNS.]{#routing-table-connected-dns explanation="O serviço de nomes não faz parte de uma rota IP já selecionada."}
::option[Diretamente pela interface indicada após a resolução do vizinho.]{#routing-table-direct .correct explanation="O host resolve o endereço do destino no enlace e enquadra o tráfego localmente."}
:::

## Comprimento do prefixo e métrica

A seleção de rotas considera as regras de política e escolhe o prefixo elegível mais longo. As métricas classificam rotas dentro de conjuntos comparáveis apropriados; uma rota padrão de métrica baixa não substitui uma `/24` correspondente apenas porque seu número é menor.

:::single-choice{#routing-table-prefix-before-default}
Qual rota normalmente corresponde de forma mais específica a `192.168.224.50`?

::option[`192.168.224.0/24 dev eth0`]{#routing-table-twenty-four .correct explanation="O prefixo correspondente de 24 bits é o mais longo entre as rotas listadas."}
::option[`default via 192.168.224.2`]{#routing-table-default-less-specific explanation="A rota padrão possui comprimento de prefixo zero."}
::option[`192.168.0.0/16 via 192.168.224.3`]{#routing-table-sixteen explanation="Ela abrange o endereço, mas fixa menos bits do que `/24`."}
:::

## Regras de política e várias tabelas

O Linux pode consultar várias tabelas de roteamento de acordo com políticas de `ip rule` baseadas em origem, marca, interface ou outros seletores. Por isso, visualizar apenas a tabela principal pode omitir o caminho real:

```bash
$ ip rule show
$ ip route show table all
```

Namespaces de rede e VRFs também podem conter estados separados. Execute a inspeção no mesmo contexto do processo afetado.

:::single-choice{#routing-table-policy-limit}
Por que `ip route show` por si só pode não explicar o caminho de uma aplicação?

::option[Regras de política ou outro namespace de rede podem selecionar um estado de roteamento diferente.]{#routing-table-policy-context .correct explanation="A consulta efetiva depende dos atributos do pacote e do contexto de rede do processo."}
::option[As tabelas de roteamento do Linux não contêm prefixos de destino.]{#routing-table-no-prefixes explanation="Os prefixos de destino são chaves fundamentais das rotas."}
::option[As aplicações nunca enviam pacotes IP.]{#routing-table-apps-never explanation="O tráfego das aplicações é transportado por protocolos de rede e transporte."}
:::

## Consultando uma rota efetiva

Peça ao kernel para avaliar um destino e, opcionalmente, uma origem:

```bash
$ ip route get 203.0.113.10
$ ip route get 203.0.113.10 from 192.168.224.10
```

O resultado prevê a consulta local naquele momento. Ele não envia uma sondagem nem comprova a acessibilidade do vizinho, dos saltos seguintes, do firewall ou da aplicação.

:::single-choice{#routing-table-route-get-limit}
O que `ip route get` não faz?

::option[Exibir a interface local e o próximo salto escolhidos.]{#routing-table-get-does-interface explanation="Esses são campos principais do resultado da consulta."}
::option[Avaliar a política atual de rotas locais para um destino.]{#routing-table-get-does-policy explanation="O comando realiza uma consulta de rota no kernel."}
::option[Comprovar a entrega bem-sucedida através de todos os saltos seguintes.]{#routing-table-get-not-probe .correct explanation="Ele é uma consulta de decisão local, não uma sondagem de rede de ponta a ponta."}
:::

## Resumo

Agora você pode ler entradas de roteamento do Linux e consultar a decisão local efetiva.

1. Diferencie rotas conectadas de rotas que passam por um gateway.
2. Leia os campos de prefixo, interface, protocolo, origem e métrica.
3. Aplique a correspondência de prefixo mais longo antes de comparar métricas relevantes.
4. Considere tabelas de política, namespaces e VRFs.
5. Trate `ip route get` como uma consulta, não como um teste de acessibilidade.
