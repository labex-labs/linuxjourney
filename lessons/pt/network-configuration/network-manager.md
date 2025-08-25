---
index: 4
lang: "pt"
title: "Network Manager"
meta_title: "Network Manager - Configuração de Rede"
meta_description: "Aprenda sobre o NetworkManager no Linux, como ele automatiza a configuração de rede e use os comandos nm-tool e nmcli. Comece com este guia para iniciantes!"
meta_keywords: "NetworkManager, nm-tool, nmcli, rede Linux, configuração de rede, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Claro, se você quer que a rede do seu sistema esteja funcionando automaticamente, já existe algo para isso. A maioria das distribuições utiliza o daemon NetworkManager para configurar suas redes automaticamente.

Você notará o NetworkManager na forma de um applet em algum lugar na barra de tarefas da sua área de trabalho se estiver usando uma GUI. Como você pode ver, ele gerencia o hardware da sua rede e as informações de conexão. Por exemplo, na inicialização, o NetworkManager coletará informações de hardware de rede, procurará por conexões (sem fio, com fio, etc.) e as ativará.

Existem também ferramentas de linha de comando para interagir com o NetworkManager:

### nm-tool

`nm-tool` relata o estado do NetworkManager e seus dispositivos.

```plaintext
pete@icebox:/$ nm-tool
NetworkManager Tool

State: connected (global)

- Device: eth0  [Wired connection 1] -------------------------------------------
  Type:              Wired
  Driver:            pcnet32
  State:             connected
  Default:           yes
  HW Address:        12:3D:45:56:7D:CC

  Capabilities:
    Carrier Detect:  yes

  Wired Properties
    Carrier:         on

  IPv4 Settings:
    Address:         192.168.22.1
    Prefix:          24 (255.255.255.0)
    Gateway:         192.168.22.2

    DNS:             192.168.22.2
```

### nmcli

O comando `nmcli` permite controlar e modificar o NetworkManager. Veja a página do manual para mais detalhes.

## Exercise

A prática leva à perfeição! Embora o NetworkManager automatize grande parte da configuração de rede, entender os comandos e conceitos subjacentes que ele gerencia é crucial para a solução de problemas e administração avançada. Aqui estão alguns laboratórios práticos para reforçar sua compreensão da identificação e gerenciamento de rede no Linux:

1. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Pratique o uso do comando `ip a` para identificar informações de endereçamento de rede, incluindo endereços MAC e IP, em um sistema Linux.
2. **[Gerenciar Endereçamento IP no Linux](https://labex.io/pt/labs/linux-manage-ip-addressing-in-linux-592736)** - Aprenda a configurar endereços IP estáticos e dinâmicos, definir gateways padrão e verificar configurações de rede usando o comando `ip` e `dhclient`.
3. **[Explorar a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Use `ping` e `arp` para entender como as camadas de rede e de enlace de dados interagem, observando o ARP em ação e como os gateways padrão lidam com o tráfego.

Esses laboratórios o ajudarão a aplicar os conceitos de identificação e configuração de rede em cenários reais e a construir confiança com os fundamentos de rede do Linux.

## Quiz Question

Qual é o comando para visualizar as informações do NetworkManager?

## Quiz Answer

nm-tool
