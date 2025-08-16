---
title: "Tarefas Upstart"
description: "Aprenda a gerenciar tarefas do Upstart no Linux usando comandos initctl. Entenda o status da tarefa, inicie, pare e reinicie serviços. Melhore suas habilidades de administração de sistema Linux."
keywords: "tarefas Upstart, initctl, serviços Linux, administração de sistema, tutorial Linux, guia para iniciantes"
---

## Lesson Content

O Upstart pode acionar muitos eventos e tarefas para serem executados. Infelizmente, não há uma maneira fácil de ver a origem de um evento ou tarefa, então você terá que investigar as configurações das tarefas em `/etc/init`. Na maioria das vezes, você nunca precisará olhar os arquivos de configuração de tarefas do Upstart, mas desejará controlar algumas tarefas específicas mais facilmente. Existem muitos comandos úteis que você pode usar em um sistema Upstart.

### View jobs

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

Você verá uma lista de tarefas do Upstart com diferentes status aplicados a elas. Em cada linha, o nome da tarefa é o primeiro valor, e o segundo campo (antes da `/`) é, na verdade, o objetivo da tarefa. O terceiro valor (depois da `/`) é o status atual. Assim, vemos que nossa tarefa `shutdown` eventualmente deseja parar, mas está atualmente em estado de espera. O status e os objetivos da tarefa mudarão à medida que você iniciar ou parar tarefas.

### View specific job

```plaintext
initctl status networking
networking start/running
```

Não entraremos nos detalhes de como escrever uma configuração de tarefa do Upstart; no entanto, já sabemos que as tarefas são paradas, iniciadas e reiniciadas nessas configurações. Essas tarefas também emitem eventos, para que possam iniciar outras tarefas. Abordaremos os comandos manuais da operação do Upstart, mas se você estiver curioso, deve aprofundar-se nos arquivos `.conf`.

### Manually start a job

```bash
sudo initctl start networking
```

### Manually stop a job

```bash
sudo initctl stop networking
```

### Manually restart a job

```bash
sudo initctl restart networking
```

### Manually emit an event

```bash
sudo initctl emit some_event
```

## Exercise

Observe sua lista de tarefas do Upstart. Agora, altere o estado da tarefa com um dos comandos que aprendemos hoje. O que você percebe depois?

## Quiz Question

Como eu reiniciaria manualmente uma tarefa do Upstart chamada `peanuts`?

## Quiz Answer

sudo initctl restart peanuts
