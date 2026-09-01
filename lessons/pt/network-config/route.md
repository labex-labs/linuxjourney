---
lesson_id: "route"
course_id: "network-config"
lang: "pt"
order_index: 2
title: "Rota"
description: "Aprenda a inspecionar, adicionar, substituir, excluir e verificar rotas Linux com segurança usando ip."
meta_title: "Rota - Configuração de Rede"
meta_description: "Aprenda a gerenciar sua tabela de roteamento Linux. Este guia aborda como adicionar e excluir rotas de rede usando o comando moderno 'ip route' e o comando legado 'route'."
meta_keywords: "comando ip route no linux, comando ip route linux, adicionar rota, excluir rota, tabela de roteamento, roteamento de rede, rede linux, ip route"
---

Rotas manuais alteram como o kernel escolhe a interface de saída e o próximo salto. Um erro pode desconectar o host ou redirecionar tráfego sensível; examine a rota efetiva, o proprietário da configuração e o caminho de recuperação antes de mudar o estado.

## Inspeção da decisão atual

Registre as rotas relevantes e pergunte ao kernel como ele alcança o destino:

```bash
$ ip -4 route show
$ ip route get 192.168.2.25
```

Examine também regras de política e tabelas alternativas quando existirem. A consulta é evidência local e não envia tráfego.

:::single-choice{#route-get-before-change} Por que executar `ip route get DESTINATION` antes de alterar uma rota?

::option[Ele registra a decisão local atual para comparação e rollback.]{#route-get-baseline .correct explanation="Interface, próximo salto e origem selecionados ajudam a definir a mudança pretendida."}
::option[Ele reserva permanentemente o destino em todos os roteadores.]{#route-get-reserves explanation="O comando faz uma consulta local e não muda estado remoto."}
::option[Ele desativa todas as regras de roteamento por política.]{#route-get-disables-policy explanation="A consulta avalia a política em vez de removê-la."}
:::

## Adição ou substituição de uma rota

Adicione uma rota para o prefixo canônico por um próximo salto alcançável:

```bash
$ sudo ip route add 192.168.2.0/23 via 10.11.12.3 dev enp1s0
```

O gateway deve ser alcançável pelo link relevante ou por um projeto on-link explícito. `add` falha quando já existe rota equivalente. `replace` cria ou altera, sendo útil para configuração idempotente, mas pode sobrescrever estado funcional; confira o alvo exato.

:::single-choice{#route-add-existing} O que normalmente acontece se `ip route add` aponta para uma rota existente?

::option[Ele apaga silenciosamente o prefixo antigo.]{#route-add-deletes explanation="Add normalmente informa objeto existente em vez de substituí-lo."}
::option[Ele falha em vez de substituir a rota.]{#route-add-fails .correct explanation="Use `replace` deliberadamente somente após revisar a entrada afetada."}
::option[Ele reinicia o gateway escolhido.]{#route-add-reboots explanation="Uma configuração local não solicita reinicialização remota dessa forma."}
:::

## Exclusão precisa

Exclua os atributos exatos quando houver mais de um candidato ou tabela:

```bash
$ sudo ip route del 192.168.2.0/23 via 10.11.12.3 dev enp1s0
```

Excluir somente pelo destino pode corresponder de forma ampla ou ambígua. Registre previamente o comando para restaurar a rota.

:::single-choice{#route-delete-precision} Por que incluir próximo salto e dispositivo ao excluir uma rota?

::option[Para identificar com maior precisão a entrada pretendida.]{#route-delete-exact .correct explanation="Atributos explícitos reduzem a chance de remover outra rota com o mesmo prefixo."}
::option[Para excluir também o adaptador físico.]{#route-delete-adapter explanation="Excluir a rota não remove o objeto de link do kernel."}
::option[Para apagar a zona DNS do destino.]{#route-delete-dns explanation="Roteamento e DNS autoritativo são sistemas separados."}
:::

## Persistência e segurança remota

`ip route` altera somente o estado atual. NetworkManager, systemd-networkd, netplan, ifupdown, DHCP, daemons ou orquestração podem substituí-lo. Armazene a rota no proprietário ativo somente após testar o comportamento.

Em host remoto, preserve console independente e use rollback que não dependa da rota alterada. Verifique depois a consulta, vizinhos, os dois sentidos do tráfego e o serviço real.

:::single-choice{#route-runtime-persistence} O que pode acontecer com uma rota manual após recarregar o gerenciador?

::option[Ela vira um recurso imutável do kernel.]{#route-manual-immutable explanation="Rotas de runtime podem ser removidas ou substituídas."}
::option[Ela aparece automaticamente em todo host da sub-rede.]{#route-manual-all-hosts explanation="O comando muda apenas o namespace atual."}
::option[Ela pode desaparecer se não estiver na política persistente.]{#route-manual-disappears .correct explanation="O gerenciador reconcilia o estado conforme seus perfis."}
:::

## Resumo

Agora você consegue fazer uma mudança limitada e recuperável de rota Linux.

1. Capturar rotas, regras e consulta efetiva atuais.
2. Usar prefixo canônico e próximo salto alcançável.
3. Distinguir adição de substituição deliberada.
4. Excluir a rota exata e preservar restauração.
5. Persistir pelo gerenciador ativo e verificar os dois sentidos.
