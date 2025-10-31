---
index: 2
lang: "pt"
title: "Serviço System V"
meta_title: "Serviço System V - Init"
meta_description: "Aprenda a gerenciar serviços tradicionais System V (SysV) no Linux. Este guia aborda o uso do comando `service` para listar, iniciar, parar e reiniciar serviços em um sistema init System V."
meta_keywords: "system v, sysv init, serviços linux, comando service, gerenciar serviços linux, iniciar serviço, parar serviço, reiniciar serviço, linux system v"
---

## Lesson Content

**System V** (ou SysV) é um dos sistemas de inicialização clássicos em sistemas operacionais do tipo Unix. Embora muitas distribuições Linux modernas tenham migrado para sistemas mais novos como o `systemd`, entender como gerenciar serviços **System V** ainda é uma habilidade valiosa, pois muitos sistemas mantêm a compatibilidade com versões anteriores.

### O Comando service

A ferramenta principal para interagir com serviços em um sistema init **System V** é o comando `service`. Ele atua como um script wrapper, simplificando o processo de controle de serviços.

### Listando Todos os Serviços

Para obter uma visão geral de todos os serviços disponíveis e seu status atual, você pode usar a flag `--status-all`. Este comando lista cada serviço e indica se ele está em execução (`+`), parado (`-`) ou se seu estado é desconhecido (`?`).

```bash
service --status-all
```

### Controlando um Serviço Específico

Para gerenciar um serviço individual, você especifica o nome do serviço seguido por uma ação como `start`, `stop` ou `restart`. Essas ações exigem privilégios administrativos, então você normalmente usará `sudo`.

Para iniciar um serviço, como o serviço de rede:

```bash
sudo service networking start
```

Para parar um serviço em execução:

```bash
sudo service networking stop
```

Para parar e imediatamente iniciar um serviço, o que é útil para aplicar alterações de configuração:

```bash
sudo service networking restart
```

Estes comandos não são exclusivos de sistemas init **System V**; você frequentemente pode usá-los para gerenciar serviços Upstart também. À medida que as distribuições Linux continuam a evoluir, camadas de compatibilidade como o comando `service` são mantidas para ajudar a facilitar a transição de scripts init tradicionais.

## Exercise

Prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de gerenciamento de processos e tarefas, que são fundamentais para gerenciar serviços no Linux:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação, inspeção, monitoramento e terminação de processos em um ambiente Linux real.
2. **[Agendar Tarefas com at e cron no Linux](https://labex.io/pt/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Aprenda a automatizar tarefas usando `at` para trabalhos únicos e `cron` para tarefas recorrentes, uma habilidade chave para automação de serviços.

Estes laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança no gerenciamento de operações do sistema.

## Quiz Question

Qual é o comando completo para parar um serviço chamado `peanut` em um sistema System V? Por favor, forneça o comando exato em inglês, prestando atenção às maiúsculas e minúsculas.

## Quiz Answer

sudo service peanut stop
