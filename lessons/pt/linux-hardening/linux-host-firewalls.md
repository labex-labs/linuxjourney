---
lesson_id: "linux-host-firewalls"
course_id: "linux-hardening"
lang: "pt"
order_index: 5
title: "Firewalls de host"
description: "Aprenda a interpretar uma política simples de firewall de host e a planejar verificações a partir dos locais relevantes."
meta_title: "Firewalls de host - Hardening do Linux"
meta_description: "Aprenda a interpretar uma política simples de firewall de host e a planejar verificações a partir dos locais relevantes."
meta_keywords: "firewall de host, hardening do Linux, cibersegurança, Linux Journey"
---

Um **firewall de host** pode permitir ou bloquear tráfego de entrada com base em propriedades como endereço de origem, protocolo e porta de destino. Comece identificando o tráfego de que o serviço precisa.

## Lendo uma política de exemplo

A política simplificada a seguir descreve um host. A notação com barra em `192.0.2.0/24` indica um intervalo de endereços IPv4. Neste exemplo, `192.0.2.44` está dentro do intervalo e `198.51.100.8` está fora.

```text
Allow TCP port 443 from any source.
Allow TCP port 22 from 192.0.2.0/24.
Deny other new inbound connections.
```

O site público usa a porta 443. A porta 22 fica reservada à rede de manutenção. A regra padrão se aplica às conexões que não correspondem a nenhuma das duas permissões.

:::single-choice{#linux-host-firewalls-match-trusted-network} Qual nova conexão corresponde à regra de manutenção?

::option[Porta TCP 22 a partir de 198.51.100.8.]{#linux-host-firewalls-match-trusted-network-b explanation="A porta corresponde à regra, mas a origem está fora da rede de manutenção."}
::option[Porta TCP 443 a partir de 192.0.2.44.]{#linux-host-firewalls-match-trusted-network-c explanation="Essa conexão corresponde à regra do site público."}
::option[Porta TCP 22 a partir de 192.0.2.44.]{#linux-host-firewalls-match-trusted-network-a .correct explanation="Tanto a porta de destino quanto o intervalo de origem correspondem à regra."}
:::

![Política simulada de firewall de host com HTTPS público e acesso restrito para manutenção](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-host-firewalls/sample-policy.png)

## Verificando a política e o serviço em escuta

Uma conexão permitida ainda pode falhar se nenhum programa estiver escutando na porta. Da mesma forma, um programa em escuta pode ficar inacessível por um caminho bloqueado pelo firewall. Confira a política e verifique também se o serviço está em escuta.

:::single-choice{#linux-host-firewalls-allowed-but-failed} A regra permite a porta 443, mas nenhum serviço está escutando nela. O que você deve verificar?

::option[Se o cliente deve usar o SSH de manutenção.]{#linux-host-firewalls-allowed-but-failed-a explanation="O SSH é outro serviço."}
::option[Se o serviço web público está escutando na porta esperada.]{#linux-host-firewalls-allowed-but-failed-b .correct explanation="Permitir uma porta no firewall não coloca um serviço em escuta."}
::option[Se a requisição veio da rede de manutenção.]{#linux-host-firewalls-allowed-but-failed-c explanation="Neste exemplo, a regra pública aceita qualquer origem."}
:::

## Planejando uma verificação segura

Ao revisar uma mudança controlada, mantenha um caminho legítimo de manutenção disponível. Teste o caminho permitido a partir da rede de manutenção. Depois, confirme que o acesso falha a partir de um local de teste autorizado fora dessa rede. Anote a origem, o destino e o resultado esperado de cada teste.

:::single-choice{#linux-host-firewalls-verification-pair} Qual par de testes verifica a restrição prevista para o SSH?

::option[Uma verificação autorizada da porta 22 de dentro e de fora da rede de manutenção.]{#linux-host-firewalls-verification-pair-c .correct explanation="Esses testes verificam os casos permitido e bloqueado pela política."}
::option[Duas conexões SSH pela mesma máquina autorizada.]{#linux-host-firewalls-verification-pair-a explanation="Isso verificaria duas vezes apenas o caso permitido."}
::option[Duas requisições do navegador à página inicial pública.]{#linux-host-firewalls-verification-pair-b explanation="Essas requisições testam a porta pública. O acesso de manutenção fica sem verificação."}
:::

## Resumo

Agora você consegue interpretar as regras do firewall de host junto com o estado do serviço.

1. Associe a regra ao protocolo, ao destino e à origem.
2. Confirme que o serviço permitido está em escuta.
3. Verifique o acesso previsto e a restrição esperada.
