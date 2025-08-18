---
lang: "pt"
title: "Gerenciador de Rede"
meta_description: "Aprenda sobre o NetworkManager no Linux, como ele automatiza a configuração de rede e use os comandos nm-tool e nmcli. Comece com este guia para iniciantes!"
meta_keywords: "NetworkManager, nm-tool, nmcli, rede Linux, configuração de rede, tutorial Linux, guia para iniciantes"
---

## Lesson Content

É claro que, se você deseja que a rede do seu sistema esteja funcionando automaticamente, já existe algo para isso. A maioria das distribuições utiliza o daemon NetworkManager para configurar suas redes automaticamente.

Você notará o NetworkManager na forma de um applet em algum lugar na barra de tarefas da sua área de trabalho, se estiver usando uma GUI. Como você pode ver, ele gerencia o hardware e as informações de conexão da sua rede. Por exemplo, na inicialização, o NetworkManager coletará informações de hardware de rede, procurará conexões (sem fio, com fio, etc.) e, em seguida, as ativará.

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

O comando `nmcli` permite controlar e modificar o NetworkManager. Consulte a página man para mais detalhes.

## Exercise

No exercises for this lesson.

## Quiz Question

Qual é o comando para visualizar as informações do NetworkManager?

## Quiz Answer

nm-tool
