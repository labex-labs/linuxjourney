---
index: 4
lang: "pt"
title: "Gerenciador de Rede"
meta_title: "Gerenciador de Rede - Configuração de Rede"
meta_description: "Descubra o papel do daemon NetworkManager no gerenciamento moderno de redes Linux. Aprenda como esta ferramenta automatiza a configuração de rede e como interagir com ela usando nm-tool e o poderoso utilitário de linha de comando nmcli."
meta_keywords: "NetworkManager, nm-tool, nmcli, gerenciador de rede linux, networkmanager linux, gerenciador rede linux, gerenciamento de rede linux, configuração de rede, redes Linux"
---

## Lesson Content

Para que a rede de um sistema seja configurada automaticamente, um serviço geralmente já está implementado. A maioria das distribuições Linux modernas utiliza o daemon NetworkManager para este fim, tornando-o uma pedra angular da **gerenciamento de rede linux**.

### O que é Network Manager no Linux?

Se você estiver usando uma interface gráfica do usuário (GUI), provavelmente notará o serviço **Network Manager Linux** como um applet na barra de tarefas do seu desktop. Esta ferramenta gerencia seu hardware de rede e informações de conexão. Por exemplo, na inicialização, o NetworkManager coleta informações sobre o hardware de rede, procura por conexões disponíveis (como redes sem fio ou com fio) e, em seguida, as ativa para colocá-lo online.

### Interação com a Linha de Comando

Embora o applet da GUI seja conveniente, também existem ferramentas poderosas de linha de comando para interagir com o serviço **networkmanager linux**. Elas são essenciais para administração de servidores e scripting.

### Usando nm-tool

O comando `nm-tool` relata o estado atual do NetworkManager e uma lista de seus dispositivos gerenciados. Observe que o `nm-tool` é considerado obsoleto em muitos sistemas modernos em favor do `nmcli`.

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

### A Ferramenta Moderna nmcli

O comando `nmcli` é a principal utilidade de linha de comando para controlar e modificar o **Linux Network Manager**. Ele permite visualizar o status, gerenciar conexões e configurar dispositivos de rede diretamente do terminal. Para uma lista completa de suas capacidades, consulte sua página de manual (`man nmcli`).

## Exercise

Prática leva à perfeição! Embora o NetworkManager automatize grande parte da configuração de rede, entender os comandos e conceitos subjacentes que ele gerencia é crucial para solução de problemas e administração avançada. Aqui estão alguns laboratórios práticos para reforçar sua compreensão da identificação e gerenciamento de rede no Linux:

1. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Pratique o uso do comando `ip a` para identificar informações de endereçamento de rede, incluindo endereços MAC e IP, em um sistema Linux.
2. **[Gerenciar Endereçamento IP no Linux](https://labex.io/pt/labs/comptia-manage-ip-addressing-in-linux-592736)** - Aprenda a configurar endereços IP estáticos e dinâmicos, definir gateways padrão e verificar configurações de rede usando o comando `ip` e `dhclient`.
3. **[Explorar a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Use `ping` e `arp` para entender como as camadas de rede e de enlace de dados interagem, observando o ARP em ação e como os gateways padrão lidam com o tráfego.

Esses laboratórios ajudarão você a aplicar os conceitos de identificação e configuração de rede em cenários reais e a construir confiança com os fundamentos de rede do Linux.

## Quiz Question

Qual é o comando para visualizar um resumo do estado e dos dispositivos do NetworkManager conforme mostrado na lição? Por favor, responda usando apenas o nome do comando em inglês em minúsculas.

## Quiz Answer

nm-tool
