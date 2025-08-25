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

### Listar serviços

```bash
service --status-all
```

### Iniciar um serviço

```bash
sudo service networking start
```

### Parar um serviço

```bash
sudo service networking stop
```

### Reiniciar um serviço

```bash
sudo service networking restart
```

Esses comandos não são específicos para sistemas de inicialização Sys V; você pode usá-los para gerenciar serviços Upstart também. Como o Linux está tentando se afastar dos scripts de inicialização Sys V mais tradicionais, ainda há coisas em vigor para ajudar nessa transição.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento de processos e tarefas, que são fundamentais para gerenciar serviços no Linux:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação, inspeção, monitoramento e encerramento de processos em um ambiente Linux real.
2. **[Agendar Tarefas com at e cron no Linux](https://labex.io/pt/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Aprenda a automatizar tarefas usando `at` para trabalhos únicos e `cron` para tarefas recorrentes, uma habilidade chave para a automação de serviços.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança no gerenciamento de operações do sistema.

## Quiz Question

Qual é o comando para parar um serviço chamado `peanut` com Sys V?

## Quiz Answer

sudo service peanut stop
