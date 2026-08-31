---
lesson_id: "network-interfaces"
course_id: "network-config"
lang: "pt"
order_index: 1
title: "Interfaces de Rede"
description: "Aprenda a inspecionar estado, endereços, estatísticas e propriedade da configuração persistente de interfaces Linux."
meta_title: "Interfaces de Rede - Configuração de Rede"
meta_description: "Um guia completo sobre a interface de rede Linux. Aprenda a usar ifconfig e o moderno comando ip, e entenda arquivos de configuração como /etc/network/interfaces, especialmente em sistemas Debian."
meta_keywords: "interface linux, interface de rede linux, etc interfaces de rede, interfaces de rede debian, ifconfig, comando ip, configuração de rede, rede linux"
---

Uma interface de rede Linux conecta um namespace de rede a um dispositivo físico, loopback, bridge, túnel, dispositivo virtual ou outro link. Estado, endereços, rotas, DNS e configuração persistente são relacionados, mas distintos.

## Descoberta das interfaces

Use as ferramentas modernas do iproute2:

```bash
$ ip -brief link show
$ ip -brief address show
```

Os nomes podem ser derivados do hardware, como `enp1s0`, tradicionais, como `eth0`, ou definidos pelo administrador. Nunca presuma que `eth0` exista ou identifique um adaptador específico.

:::single-choice{#interfaces-name-assumption}
Por que um script deve descobrir a interface em vez de presumir `eth0`?

::option[Toda interface precisa se chamar `lo`.]{#interfaces-all-loopback explanation="Loopback é uma interface especial, não o nome de todos os links."}
::option[Sistemas Linux podem usar vários esquemas de nomes.]{#interfaces-naming-varies .correct explanation="Nomes derivados do hardware, virtuais e personalizados tornam `eth0` pouco confiável."}
::option[Nomes de interface são sempre senhas remotas.]{#interfaces-name-password explanation="Eles identificam dispositivos do kernel, não credenciais."}
:::

## Estado administrativo e operacional

`UP` significa que a interface está administrativamente habilitada. `LOWER_UP` costuma indicar que a camada inferior relata prontidão, como portadora Ethernet. Nenhuma flag isolada prova que endereço IP, rota, DNS, firewall ou aplicativo funcionam.

```bash
$ ip -details link show dev enp1s0
$ ip -s link show dev enp1s0
```

As estatísticas revelam erros, descartes e contadores, mas precisam de intervalo e linha de base para ter significado.

:::single-choice{#interfaces-up-limit}
O que o estado administrativo `UP` não prova?

::option[Que a conectividade de ponta a ponta funciona.]{#interfaces-up-not-connectivity .correct explanation="Ainda podem existir falhas de camada inferior, endereço, rota, filtro, nome ou serviço."}
::option[Que o administrador habilitou a interface.]{#interfaces-up-does-prove explanation="Esse é o significado direto do estado."}
::option[Que existe um objeto de interface no kernel.]{#interfaces-up-kernel-object explanation="O estado exibido pertence a uma interface existente."}
:::

## Alteração do estado em execução

Comandos de runtime incluem:

```bash
$ sudo ip link set dev enp1s0 up
$ sudo ip address add 192.0.2.10/24 dev enp1s0
```

Eles afetam o estado atual e podem conflitar com um gerenciador que reaplique seu perfil. Derrubar a interface de acesso remoto pode encerrar a conexão. Antes de mudar, confirme o dispositivo, preserve console, registre o estado e prepare rollback testado ou temporizado.

:::single-choice{#interfaces-ip-address-add-persistence}
`ip address add` garante sozinho persistência após reiniciar?

::option[Não; o sistema de configuração ativo também precisa guardar a definição.]{#interfaces-manager-persistence .correct explanation="NetworkManager, systemd-networkd, ifupdown ou outro proprietário aplica a política persistente."}
::option[Sim; toda mudança do kernel edita todos os perfis.]{#interfaces-runtime-always-persistent explanation="Mudanças de runtime não atualizam universalmente a configuração persistente."}
::option[Apenas quando o endereço é IPv4 privado.]{#interfaces-private-persistent explanation="O escopo do endereço não torna o comando persistente."}
:::

## Identificação do proprietário da configuração

Os caminhos persistentes variam entre distribuições e instalações. Entre as possibilidades estão perfis do NetworkManager, unidades do systemd-networkd, entradas do netplan, `/etc/network/interfaces`, cloud-init ou orquestração. Determine qual serviço gerencia o dispositivo antes de editar arquivos:

```bash
$ systemctl --type=service --state=running | grep -E 'NetworkManager|networkd|networking'
$ networkctl status
$ nmcli device status
```

Use somente comandos do gerenciador identificado. Dois gerenciadores no mesmo link podem competir e sobrescrever estados.

:::single-choice{#interfaces-config-owner}
O que deve preceder uma mudança persistente na interface?

::option[Editar todos os arquivos de rede possíveis.]{#interfaces-edit-all explanation="Definições concorrentes criam conflitos e reaplicações imprevisíveis."}
::option[Identificar qual gerenciador controla a interface.]{#interfaces-identify-owner .correct explanation="A fonte e o método corretos dependem desse proprietário."}
::option[Apagar todas as rotas antes da inspeção.]{#interfaces-delete-routes explanation="Isso é destrutivo e pode remover o acesso de recuperação."}
:::

## Verificação da mudança

Verifique link, endereços e validade, rotas escolhidas, resolver, vizinhos e o aplicativo real. Para mudança persistente, teste reinício controlado do serviço ou do sistema somente com recuperação disponível.

:::single-choice{#interfaces-change-verification}
O que é evidência melhor que apenas ver o novo endereço em `ip address`?

::option[O nome da interface contém um dígito.]{#interfaces-digit explanation="O nome não valida o caminho."}
::option[O prompt continua com a mesma cor.]{#interfaces-prompt-color explanation="A aparência do terminal não tem relação com a rede."}
::option[Rotas, resolver e o aplicativo pretendido também funcionam.]{#interfaces-end-to-end .correct explanation="Uma configuração utilizável depende do caminho completo e do serviço."}
:::

## Resumo

Agora você consegue inspecionar e alterar uma interface sem confundir estado ativo com política persistente.

1. Descobrir nomes e endereços reais.
2. Separar estado administrativo de conectividade operacional.
3. Tratar mudanças diretas com `ip` como estado atual.
4. Identificar o proprietário antes de persistir configurações.
5. Verificar roteamento, resolução e aplicativo depois.
