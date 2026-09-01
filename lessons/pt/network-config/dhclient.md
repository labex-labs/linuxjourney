---
lesson_id: "dhclient"
course_id: "network-config"
lang: "pt"
order_index: 3
title: "dhclient"
description: "Aprenda quando e como usar dhclient sem entrar em conflito com o gerenciador de rede do sistema."
meta_title: "dhclient - Configuração de Rede"
meta_description: "Aprenda sobre dhclient, como ele obtém endereços IP usando DHCP e gerencia concessões de rede. Entenda os arquivos dhclient.conf e dhclient.leases. Guia para iniciantes em Linux."
meta_keywords: "dhclient, DHCP, rede Linux, endereço IP, configuração de rede, tutorial Linux, guia para iniciantes"
---

`dhclient` é um cliente ISC DHCP presente em alguns sistemas Linux. Muitas instalações atuais deixam NetworkManager, systemd-networkd ou outro serviço executar seu próprio cliente. Iniciar um segundo cliente numa interface gerenciada pode criar endereços, rotas, DNS e concessões concorrentes.

## Identificação do cliente ativo

Antes de invocar `dhclient`, examine o proprietário e os processos:

```bash
$ nmcli device status
$ networkctl status
$ ps -ef | grep '[d]hclient'
```

Use as ferramentas disponíveis no host. Se um gerenciador controla a interface, solicite DHCP por ele, em vez de iniciar outro cliente.

:::single-choice{#dhclient-second-client-risk} Por que evitar `dhclient` numa interface já gerenciada?

::option[DHCP só pode atribuir endereços loopback.]{#dhclient-loopback-only explanation="DHCP normalmente fornece configurações de rede não loopback."}
::option[Dois clientes podem disputar endereços, rotas, DNS e concessões.]{#dhclient-competing-state .correct explanation="Somente o proprietário identificado deve normalmente reconciliar a interface."}
::option[Toda solicitação DHCP reformata o disco local.]{#dhclient-reformats explanation="O protocolo altera o estado de rede, não o formato do disco."}
:::

## Solicitação explícita de uma concessão

Em uma interface de teste não gerenciada, quando `dhclient` é o proprietário pretendido, especifique a interface e use saída detalhada:

```bash
$ sudo dhclient -v enp1s0
```

Sem uma interface, o comando pode agir em várias interfaces elegíveis. Caminhos de configuração e concessão variam; nomes comuns incluem `dhclient.conf` e `dhclient.leases`, mas não presuma uma localização fixa.

:::single-choice{#dhclient-interface-operand} Por que especificar `enp1s0` numa solicitação manual?

::option[Para limitar a ação à interface pretendida.]{#dhclient-scope-interface .correct explanation="Uma invocação sem qualificação pode considerar mais interfaces que o desejado."}
::option[Para escolher a porta TCP 1 para DHCP.]{#dhclient-tcp-port explanation="DHCP usa UDP, e o nome da interface não é uma porta."}
::option[Para tornar a concessão permanente.]{#dhclient-permanent explanation="A configuração DHCP continua sendo uma concessão limitada no tempo."}
:::

## Liberação de uma concessão

`dhclient -r INTERFACE` solicita liberação e pode remover a configuração utilizável. É disruptivo e não garante que o servidor esteja acessível para receber o pedido. Não libere apenas para inspecionar, sobretudo no caminho de gerenciamento remoto.

:::single-choice{#dhclient-release-effect} Qual é o risco operacional de `dhclient -r enp1s0`?

::option[Ele apenas mostra a concessão atual sem mudanças.]{#dhclient-release-readonly explanation="A liberação altera o estado."}
::option[Ele renova toda concessão por tempo ilimitado.]{#dhclient-release-renews explanation="Liberar e renovar são operações opostas."}
::option[Ele pode remover a conectividade DHCP atual.]{#dhclient-release-connectivity .correct explanation="O fluxo abre mão da concessão e pode encerrar o acesso remoto."}
:::

## Verificação da concessão aplicada

Depois de uma solicitação controlada, verifique mais que o endereço:

```bash
$ ip address show dev enp1s0
$ ip route show
$ resolvectl status
```

Examine os logs do gerenciador ou do cliente e a duração da concessão e, em seguida, teste a resolução de nomes e a aplicação pretendidas. Um DHCPACK pode trazer opções incorretas, e a atribuição bem-sucedida de um endereço não comprova a acessibilidade do gateway nem do DNS.

:::single-choice{#dhclient-verify-state} O que deve ser verificado após obter uma concessão?

::option[Endereço, rotas, DNS, concessão e comportamento do aplicativo.]{#dhclient-complete-verify .correct explanation="A concessão configura componentes relacionados que precisam funcionar juntos."}
::option[Apenas que uma string de endereço apareceu.]{#dhclient-address-only explanation="Rotas, DNS, validade e funcionamento ainda podem estar errados."}
::option[Apenas o papel de parede do desktop.]{#dhclient-wallpaper explanation="A aparência não tem relação com DHCP."}
:::

## Resumo

Agora você consegue usar `dhclient` somente quando ele é o proprietário pretendido da interface.

1. Descobrir o gerenciador e o cliente DHCP ativos.
2. Evitar clientes concorrentes na mesma interface.
3. Limitar pedidos manuais a uma interface de teste nomeada.
4. Tratar liberação como disruptiva e verificar toda a concessão.
