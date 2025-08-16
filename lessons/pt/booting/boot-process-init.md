---
title: "Processo de Inicialização: Init"
description: "Aprenda sobre os sistemas init do Linux: System V, Upstart e systemd. Entenda seus papéis no processo de inicialização e como eles gerenciam serviços. Comece sua jornada no Linux!"
keywords: "Linux init, systemd, System V init, Upstart, processo de inicialização do Linux, tutorial de Linux, Linux para iniciantes, guia de Linux"
---

## Lesson Content

Discutimos o init em lições anteriores e sabemos que é o primeiro processo a ser iniciado, e ele inicia todos os outros serviços essenciais em nosso sistema. Mas como?

Existem, na verdade, três implementações principais de init no Linux:

### System V init (sysv)

Este é o sistema init tradicional. Ele inicia e para processos sequencialmente com base em scripts de inicialização. O estado da máquina é denotado por runlevels; cada runlevel inicia ou para uma máquina de uma maneira diferente.

### Upstart

Este é o init que você encontrará em instalações mais antigas do Ubuntu. O Upstart usa a ideia de jobs e events e funciona iniciando jobs que executam certas ações em resposta a events.

### Systemd

Este é o novo padrão para init; é orientado a objetivos. Basicamente, você tem um objetivo que deseja alcançar, e o systemd tenta satisfazer as dependências do objetivo para completá-lo.

Temos um curso inteiro sobre sistemas Init onde nos aprofundaremos em cada um desses sistemas em mais detalhes.

## Exercise

No exercises for this lesson.

## Quiz Question

Qual é o padrão mais recente para init?

## Quiz Answer

systemd
