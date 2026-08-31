---
lesson_id: "network-manager"
course_id: "network-config"
lang: "pt"
order_index: 4
title: "Gerenciador de Rede"
description: "Aprenda como o NetworkManager separa dispositivos, perfis persistentes e estado ativo em tempo de execução."
meta_title: "Gerenciador de Rede - Configuração de Rede"
meta_description: "Descubra o papel do daemon NetworkManager no gerenciamento moderno de redes Linux. Aprenda como esta ferramenta automatiza a configuração de rede e como interagir com ela usando nm-tool e o poderoso utilitário de linha de comando nmcli."
meta_keywords: "NetworkManager, nm-tool, nmcli, gerenciador de rede linux, networkmanager linux, gerenciador rede linux, gerenciamento de rede linux, configuração de rede, redes Linux"
---

O NetworkManager gerencia dispositivos e ativa perfis de conexão em muitos desktops e servidores Linux. Ele não é universal; confirme que controla a interface desejada antes de usar `nmcli` para mudar a configuração.

## Dispositivos e conexões

Um dispositivo é uma interface do kernel como `enp1s0` ou `wlan0`. Uma conexão é um perfil armazenado com IPv4, IPv6, DNS, Wi-Fi, roteamento e outras definições. Um dispositivo pode ter vários perfis, mas normalmente apenas um aplicável fica ativo por vez.

```bash
$ nmcli device status
$ nmcli connection show
$ nmcli connection show --active
```

:::single-choice{#networkmanager-device-profile}
O que é um perfil de conexão do NetworkManager?

::option[Um conector físico soldado à placa de rede.]{#networkmanager-physical-connector explanation="Isso é hardware, não um perfil."}
::option[Um conjunto armazenado de definições que pode ser ativado num dispositivo.]{#networkmanager-stored-settings .correct explanation="Perfis persistem a configuração separadamente do objeto de interface do kernel."}
::option[Um pacote capturado de cada fluxo ativo.]{#networkmanager-packet-capture explanation="Perfis descrevem configuração e não contêm todo o tráfego."}
:::

## Inspeção do estado efetivo

Mostre o perfil ativo e os detalhes do dispositivo:

```bash
$ nmcli -f GENERAL,IP4,IP6 device show enp1s0
$ nmcli connection show 'Wired connection 1'
```

Definições do perfil, resultados DHCP e estado do kernel podem diferir. Compare com `ip address`, `ip route` e o resolver. O obsoleto `nm-tool` não deve fundamentar um fluxo atual.

:::single-choice{#networkmanager-active-command}
Qual comando lista os perfis ativos?

::option[`nmcli device delete --all`]{#networkmanager-delete-all explanation="Isso não é inspeção e sugere uma ação destrutiva."}
::option[`nmcli connection show --active`]{#networkmanager-show-active .correct explanation="Ele filtra as conexões armazenadas para as que estão ativadas."}
::option[`ip route flush table all`]{#networkmanager-flush-routes explanation="Isso remove rotas em vez de listar perfis."}
:::

## Modificação e ativação de um perfil

Modifique explicitamente um perfil e ative-o numa janela de manutenção:

```bash
$ sudo nmcli connection modify 'Wired connection 1' ipv4.method auto
$ sudo nmcli connection up 'Wired connection 1'
```

Modificar muda dados persistentes; ativar pode substituir endereços, rotas e DNS ativos. Uma mudança remota exige console, definições originais salvas e rollback temporizado independente. Não dependa da conexão alterada para transportar sua própria recuperação.

:::single-choice{#networkmanager-modify-versus-up}
Qual é a diferença entre `connection modify` e `connection up`?

::option[Modify reinicia o host; up edita o código-fonte do DNS.]{#networkmanager-reboot-source explanation="Nenhuma descrição corresponde aos comandos."}
::option[Modify muda as definições; up ativa um perfil.]{#networkmanager-change-activate .correct explanation="Persistência e ativação em runtime são operações relacionadas, mas separadas."}
::option[Ambos são aliases somente leitura.]{#networkmanager-readonly explanation="Os dois podem alterar estado nesse fluxo."}
:::

## Verificação e proteção de segredos

Depois da ativação, verifique perfil, endereços e rotas do kernel, DNS, ambas as famílias e o aplicativo. Perfis Wi-Fi, VPN, 802.1X e móveis podem conter segredos. Limite permissões e não imprima campos secretos em logs ou transcrições compartilhadas.

:::single-choice{#networkmanager-verification}
O que prova mais que o NetworkManager informar “conectado”?

::option[O nome do perfil contém Wired.]{#networkmanager-name-proof explanation="Um rótulo não demonstra a saúde do caminho."}
::option[A janela do terminal continua aberta.]{#networkmanager-terminal-open explanation="Um terminal pode sobreviver a falhas parciais."}
::option[Os testes pretendidos de DNS e aplicativo têm êxito.]{#networkmanager-end-to-end .correct explanation="O estado do gerenciador deve ser correlacionado ao kernel e ao serviço."}
:::

## Resumo

Agora você consegue gerenciar perfis sem confundi-los com objetos de interface.

1. Confirmar que o NetworkManager controla o dispositivo.
2. Distinguir perfis armazenados de estado ativo.
3. Inspecionar dispositivos, todos os perfis e os ativos.
4. Modificar, ativar, recuperar e verificar como etapas distintas.
