---
index: 4
lang: "pt"
title: "Tarefas Upstart"
meta_title: "Tarefas Upstart - Init"
meta_description: "Aprenda a gerenciar tarefas Upstart no Linux usando comandos initctl. Entenda o status da tarefa, inicie, pare e reinicie serviços. Melhore suas habilidades de administração de sistema Linux."
meta_keywords: "tarefas Upstart, initctl, serviços Linux, administração de sistema, tutorial Linux, guia para iniciantes"
---

## Lesson Content

O Upstart pode acionar muitos eventos e tarefas para serem executados. Infelizmente, não há uma maneira fácil de ver de onde um evento ou tarefa se originou, então você terá que investigar as configurações de tarefas em `/etc/init`. Na maioria das vezes, você nunca precisará olhar para os arquivos de configuração de tarefas do Upstart, mas você vai querer controlar algumas tarefas específicas mais facilmente. Existem muitos comandos úteis que você pode usar em um sistema Upstart.

### Visualizar tarefas

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

Você verá uma lista de tarefas do Upstart com diferentes status aplicados a elas. Em cada linha, o nome da tarefa é o primeiro valor, e o segundo campo (antes do `/`) é na verdade o objetivo da tarefa. O terceiro valor (depois do `/`) é o status atual. Assim, vemos que nossa tarefa `shutdown` eventualmente quer parar, mas está atualmente em estado de espera. O status e os objetivos da tarefa mudarão à medida que você iniciar ou parar tarefas.

### Visualizar tarefa específica

```plaintext
initctl status networking
networking start/running
```

Não entraremos em detalhes sobre como escrever uma configuração de tarefa do Upstart; no entanto, já sabemos que as tarefas são paradas, iniciadas e reiniciadas nessas configurações. Essas tarefas também emitem eventos, então elas podem iniciar outras tarefas. Abordaremos os comandos manuais da operação do Upstart, mas se você estiver curioso, deve aprofundar-se nos arquivos `.conf`.

### Iniciar uma tarefa manualmente

```bash
sudo initctl start networking
```

### Parar uma tarefa manualmente

```bash
sudo initctl stop networking
```

### Reiniciar uma tarefa manualmente

```bash
sudo initctl restart networking
```

### Emitir um evento manualmente

```bash
sudo initctl emit some_event
```

## Exercise

Practice makes perfect! While there are no specific labs for Upstart, understanding how to schedule and manage tasks is crucial for controlling system processes. Here's a hands-on lab to reinforce your understanding of task management:

1. **[Agendar Tarefas com at e cron no Linux](https://labex.io/pt/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Pratique a criação, gerenciamento e remoção de tarefas únicas e recorrentes, que são conceitos fundamentais relacionados a como os serviços e tarefas são gerenciados em ambientes Linux como os tratados pelo Upstart.

This lab will help you apply the concepts of task automation in real scenarios and build confidence with managing system operations.

## Quiz Question

Como eu reiniciaria manualmente uma tarefa Upstart chamada `peanuts`?

## Quiz Answer

sudo initctl restart peanuts
