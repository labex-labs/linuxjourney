---
lang: "pt"
title: "Estados de Processo"
description: "Aprenda os estados de processo do Linux (R, S, D, Z, T) usando `ps aux`. Entenda os códigos STAT comuns e gerencie processos de forma eficaz. Comece sua jornada no Linux!"
keywords: "estados de processo Linux, ps aux, gerenciamento de processos, tutorial Linux, Linux para iniciantes, códigos STAT, guia Linux"
---

## Lesson Content

Vamos dar uma olhada no comando `ps aux` novamente:

```bash
ps aux
```

Na coluna STAT, você verá muitos valores. Um processo Linux pode estar em vários estados diferentes. Os códigos de estado mais comuns que você verá são descritos abaixo:

- **R**: Em execução ou executável; está apenas esperando a CPU processá-lo.
- **S**: Suspensão interrompível; esperando que um evento seja concluído, como entrada do terminal.
- **D**: Suspensão ininterrupta; processos que não podem ser encerrados ou interrompidos com um sinal. Geralmente, para fazê-los desaparecer, você precisa reiniciar ou corrigir o problema.
- **Z**: Zumbi; discutimos em uma lição anterior que zumbis são processos terminados que estão esperando que seus status sejam coletados.
- **T**: Parado; um processo que foi suspenso/parado.

## Exercise

Observe os processos em execução no seu sistema e verifique seus estados de processo.

## Quiz Question

Qual código STAT é usado para representar uma suspensão ininterrupta?

## Quiz Answer

D
