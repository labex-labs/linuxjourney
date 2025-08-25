---
index: 6
lang: "pt"
title: "Metas do Systemd"
meta_title: "Metas do Systemd - Init"
meta_description: "Aprenda os fundamentos das unidades systemd e os comandos essenciais do systemctl. Entenda como gerenciar serviços, visualizar status e habilitar unidades no Linux. Comece sua jornada!"
meta_keywords: "systemd, systemctl, serviços Linux, arquivos de unidade, iniciante, tutorial, guia, comandos Linux"
---

## Lesson Content

Não entraremos em detalhes sobre como escrever arquivos de unidade systemd. No entanto, faremos uma breve visão geral de um arquivo de unidade e como controlar unidades manualmente.

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

Agora, vamos ver alguns comandos que você pode usar com unidades systemd:

### Listar unidades

```bash
systemctl list-units
```

### Ver status da unidade

```bash
systemctl status networking.service
```

### Iniciar um serviço

```bash
sudo systemctl start networking.service
```

### Parar um serviço

```bash
sudo systemctl stop networking.service
```

### Reiniciar um serviço

```bash
sudo systemctl restart networking.service
```

### Habilitar uma unidade

```bash
sudo systemctl enable networking.service
```

### Desabilitar uma unidade

```bash
sudo systemctl disable networking.service
```

Novamente, você ainda não viu a profundidade que o systemd atinge, então leia sobre ele se quiser aprender mais.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre o gerenciamento de processos, que são frequentemente controlados por serviços systemd:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação com processos em primeiro e segundo plano, inspecionando-os com `ps`, monitorando recursos com `top`, ajustando a prioridade com `renice` e encerrando-os com `kill`. Este laboratório lhe dará experiência prática com os efeitos em tempo de execução do gerenciamento de unidades systemd.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com o gerenciamento de processos no Linux.

## Quiz Question

Qual é o comando para iniciar um serviço chamado peanut.service?

## Quiz Answer

sudo systemctl start peanut.service
