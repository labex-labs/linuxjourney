---
lang: "pt"
title: "Objetivos do Systemd"
description: "Aprenda os conceitos básicos das unidades systemd e os comandos essenciais do systemctl. Entenda como gerenciar serviços, visualizar status e habilitar unidades no Linux. Comece sua jornada!"
keywords: "systemd, systemctl, serviços Linux, arquivos de unidade, iniciante, tutorial, guia, comandos Linux"
---

## Lesson Content

Não entraremos nos detalhes de como escrever arquivos de unidade systemd. No entanto, faremos uma breve visão geral de um arquivo de unidade e como controlar unidades manualmente.

Aqui está um arquivo de unidade de serviço básico: foobar.service

```
[Unit]
Description=My Foobar
Before=bar.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

Este é um alvo de serviço simples. No início do arquivo, vemos uma seção para `[Unit]`. Isso nos permite dar uma descrição ao nosso arquivo de unidade, bem como controlar a ordem de ativação da unidade. A próxima parte é a seção `[Service]`; aqui, podemos iniciar, parar ou recarregar um serviço. E a seção `[Install]` é usada para dependências. Esta é apenas a ponta do iceberg para escrever arquivos systemd, então eu o imploro a ler sobre o assunto se quiser saber mais.

Agora, vamos ver alguns comandos que você pode usar com as unidades systemd:

### List units

```bash
systemctl list-units
```

### View status of unit

```bash
systemctl status networking.service
```

### Start a service

```bash
sudo systemctl start networking.service
```

### Stop a service

```bash
sudo systemctl stop networking.service
```

### Restart a service

```bash
sudo systemctl restart networking.service
```

### Enable a unit

```bash
sudo systemctl enable networking.service
```

### Disable a unit

```bash
sudo systemctl disable networking.service
```

Novamente, você ainda não viu a profundidade que o systemd atinge, então leia sobre ele se quiser aprender mais.

## Exercise

Visualize os status das unidades e inicie e pare alguns serviços. O que você observa?

## Quiz Question

Qual é o comando para iniciar um serviço chamado peanut.service?

## Quiz Answer

sudo systemctl start peanut.service
