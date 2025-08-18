---
index: 2
lang: "pt"
title: "Serviço System V"
meta_title: "Serviço System V - Init"
meta_description: "Aprenda a gerenciar serviços System V usando ferramentas de linha de comando. Descubra como listar, iniciar, parar e reiniciar serviços com este tutorial de Linux para iniciantes."
meta_keywords: "serviços System V, serviços Linux, comando service, SysV init, tutorial Linux, Linux para iniciantes, gerenciamento de serviços, guia Linux"
---

## Lesson Content

Existem muitas ferramentas de linha de comando que você pode usar para gerenciar serviços Sys V.

### List services

```bash
service --status-all
```

### Start a service

```bash
sudo service networking start
```

### Stop a service

```bash
sudo service networking stop
```

### Restart a service

```bash
sudo service networking restart
```

Esses comandos não são específicos para sistemas init Sys V; você pode usá-los para gerenciar serviços Upstart também. Como o Linux está tentando se afastar dos scripts init Sys V mais tradicionais, ainda existem coisas em vigor para ajudar nessa transição.

## Exercise

Gerencie alguns serviços e altere seus estados. O que você observa?

## Quiz Question

Qual é o comando para parar um serviço chamado `peanut` com Sys V?

## Quiz Answer

sudo service peanut stop
