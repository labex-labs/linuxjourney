---
title: "Estados de Energia"
description: "Aprenda os estados de energia do sistema Linux: comandos shutdown, reboot e halt. Entenda como desligar ou reiniciar seu sistema Linux com segurança. Comece com comandos essenciais!"
keywords: "desligar Linux, comando reboot, sistema halt, desligar Linux, comandos Linux, Linux para iniciantes, tutorial Linux, estados do sistema"
---

## Lesson Content

É difícil acreditar que ainda não discutimos maneiras de controlar o estado do seu sistema através da linha de comando. Ao falar sobre `init`, não discutimos apenas os modos que iniciam nosso sistema, mas também os que o param.

Para desligar seu sistema:

```bash
sudo shutdown -h now
```

Este comando irá parar o sistema (desligá-lo). Você também deve especificar um horário em que deseja que isso ocorra. Você pode adicionar um tempo em minutos que desligará o sistema nesse período.

```bash
sudo shutdown -h +2
```

Isso desligará seu sistema em dois minutos. Você também pode reiniciar com o comando `shutdown`:

```bash
sudo shutdown -r now
```

Ou apenas use o comando `reboot`:

```bash
sudo reboot
```

## Exercise

O que você acha que está acontecendo com `init` quando você desliga sua máquina?

## Quiz Question

Qual é o comando para desligar seu sistema em 4 minutos?

## Quiz Answer

sudo shutdown -h +4
