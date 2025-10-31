---
index: 4
lang: "pt"
title: "Empregos Upstart"
meta_title: "Empregos Upstart - Init"
meta_description: "Um guia para gerenciar serviços com empregos Upstart em um ambiente Linux. Aprenda a usar o utilitário initctl para listar, iniciar, parar e reiniciar trabalhos em um sistema Linux upstart."
meta_keywords: "Empregos Upstart, initctl, upstart linux, serviços Linux, administração de sistema, sistema init, tutorial Linux"
---

## Lesson Content

O Upstart é um sistema init baseado em eventos usado em algumas distribuições **upstart linux** para gerenciar serviços e tarefas durante a inicialização e enquanto o sistema está em execução. Ele opera através de um sistema de jobs (tarefas) e eventos. Embora rastrear a origem de cada evento possa ser complexo, muitas vezes exigindo que você explore as configurações de jobs em `/etc/init`, você mais comumente precisará gerenciar esses jobs diretamente da linha de comando. O utilitário `initctl` fornece um conjunto de comandos para esse fim.

### Visualizando o Status do Job

Para ver uma lista de todos os jobs Upstart conhecidos e seus estados atuais, use o comando `list`.

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

A saída exibe o nome do job, seu objetivo (goal) e seu status atual. No exemplo `shutdown stop/waiting`, o nome do job é `shutdown`, seu objetivo é `stop` e seu status atual é `waiting`. O status e os objetivos do job mudarão conforme você interage com eles.

Para verificar o status de um job específico, use o comando `status`.

```plaintext
initctl status networking
networking start/running
```

### Controlando Jobs Manualmente

Embora os arquivos de configuração de jobs em `/etc/init` definam como os jobs iniciam, param e interagem com eventos, você pode anular manualmente essas ações usando `initctl`. Isso é útil para solução de problemas ou para realizar tarefas administrativas.

Para iniciar um job manualmente:

```bash
sudo initctl start networking
```

Para parar um job manualmente:

```bash
sudo initctl stop networking
```

Para reiniciar um job manualmente, que é um atalho conveniente para pará-lo e depois iniciá-lo:

```bash
sudo initctl restart networking
```

### Emitindo Eventos Personalizados

Jobs Upstart são acionados por eventos. Você também pode "emitir" um evento manualmente, o que pode ser útil para acionar jobs personalizados ou para fins de teste. Qualquer job configurado para iniciar em `some_event` seria acionado pelo seguinte comando.

```bash
sudo initctl emit some_event
```

## Exercise

A prática leva à perfeição! Embora não existam laboratórios específicos para Upstart, entender como agendar e gerenciar tarefas é crucial para controlar processos do sistema. Aqui está um laboratório prático para reforçar sua compreensão do gerenciamento de tarefas:

1. **[Agendar Tarefas com at e cron no Linux](https://labex.io/pt/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Pratique a criação, gerenciamento e remoção de jobs únicos e recorrentes, que são conceitos fundamentais relacionados à forma como serviços e tarefas são gerenciados em ambientes Linux como os tratados pelo Upstart.

Este laboratório ajudará você a aplicar os conceitos de automação de tarefas em cenários reais e a ganhar confiança no gerenciamento de operações do sistema.

## Quiz Question

Como você reiniciaria manualmente um job Upstart chamado `peanuts`? Por favor, forneça o comando completo. (Nota: A resposta diferencia maiúsculas de minúsculas e deve estar em inglês.)

## Quiz Answer

sudo initctl restart peanuts
