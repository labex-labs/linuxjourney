---
lang: "ru"
title: "Network Manager"
meta_title: "Network Manager - Конфигурация сети"
meta_description: "Узнайте о NetworkManager в Linux, как он автоматизирует настройку сети, и используйте команды nm-tool и nmcli. Начните с этого руководства для начинающих!"
meta_keywords: "NetworkManager, nm-tool, nmcli, Linux networking, network configuration, Linux tutorial, beginner guide"
---

## Lesson Content

Конечно, если вы хотите, чтобы сеть вашей системы работала автоматически, для этого уже есть готовое решение. Большинство дистрибутивов используют демон NetworkManager для автоматической настройки своих сетей.

Вы заметите NetworkManager в виде апплета где-нибудь на панели задач вашего рабочего стола, если вы используете GUI. Как вы можете видеть, он управляет аппаратным обеспечением вашей сети и информацией о подключении. Например, при запуске NetworkManager собирает информацию об аппаратном обеспечении сети, ищет подключения (беспроводные, проводные и т.д.), а затем активирует их.

Существуют также инструменты командной строки для взаимодействия с NetworkManager:

### nm-tool

`nm-tool` сообщает состояние NetworkManager и его устройств.

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

Команда `nmcli` позволяет управлять и изменять NetworkManager. Подробнее см. на странице man.

## Exercise

No exercises for this lesson.

## Quiz Question

Какая команда используется для просмотра информации NetworkManager?

## Quiz Answer

nm-tool
