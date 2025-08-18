---
lang: "pt"
title: "Sinais"
meta_description: "Aprenda sobre os sinais Linux, seu propósito, tipos comuns como SIGINT e SIGKILL, e como os processos os manipulam. Entenda os conceitos básicos de sinais para um melhor controle do Linux."
meta_keywords: "sinais Linux, SIGKILL, SIGINT, comunicação de processos, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Um sinal é uma notificação para um processo de que algo aconteceu.

### Por que Temos Sinais

São interrupções de software e têm muitos usos:

- Um usuário pode digitar um dos caracteres especiais do terminal (Ctrl-C) ou (Ctrl-Z) para matar, interromper ou suspender processos.
- Podem ocorrer problemas de hardware, e o kernel quer notificar o processo.
- Podem ocorrer problemas de software, e o kernel quer notificar o processo.
- São basicamente formas de os processos se comunicarem.

### Processo de Sinal

Quando um sinal é gerado por algum evento, ele é então entregue a um processo; é considerado em um estado pendente até ser entregue. Quando o processo é executado, o sinal será entregue. No entanto, os processos têm máscaras de sinal, e podem configurar a entrega de sinal para ser bloqueada, se especificado. Quando um sinal é entregue, um processo pode fazer uma infinidade de coisas:

- Ignorar o sinal.
- "Capturar" o sinal e executar uma rotina de tratamento específica.
- O processo pode ser terminado, em oposição à chamada de sistema de saída normal.
- Bloquear o sinal, dependendo da máscara de sinal.

### Sinais Comuns

Cada sinal é definido por inteiros com nomes simbólicos que estão na forma de SIGxxx. Alguns dos sinais mais comuns são:

- SIGHUP ou HUP ou 1: Hangup
- SIGINT ou INT ou 2: Interrupt
- SIGKILL ou KILL ou 9: Kill
- SIGSEGV ou SEGV ou 11: Segmentation fault
- SIGTERM ou TERM ou 15: Software termination
- SIGSTOP ou STOP: Stop

Os números podem variar com os sinais, então eles são geralmente referidos pelos seus nomes.

Alguns sinais são inbloqueáveis; um exemplo é o sinal SIGKILL. O sinal KILL destrói o processo.

## Exercise

No exercises for this lesson.

## Quiz Question

Qual sinal é inbloqueável?

## Quiz Answer

SIGKILL
