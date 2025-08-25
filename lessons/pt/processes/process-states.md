---
index: 9
lang: "pt"
title: "Estados de Processo"
meta_title: "Estados de Processo - Processos"
meta_description: "Aprenda os estados de processo do Linux (R, S, D, Z, T) usando `ps aux`. Entenda os códigos STAT comuns e gerencie processos de forma eficaz. Comece sua jornada no Linux!"
meta_keywords: "estados de processo Linux, ps aux, gerenciamento de processo, tutorial Linux, Linux para iniciantes, códigos STAT, guia Linux"
---

## Lesson Content

Vamos dar uma olhada no comando `ps aux` novamente:

```bash
ps aux
```

Na coluna STAT, você verá muitos valores. Um processo Linux pode estar em vários estados diferentes. Os códigos de estado mais comuns que você verá são descritos abaixo:

- **R**: Running (Em execução) ou runnable (executável); está apenas esperando a CPU processá-lo.
- **S**: Interruptible sleep (Suspensão interrompível); esperando um evento ser concluído, como entrada do terminal.
- **D**: Uninterruptible sleep (Suspensão ininterrupta); processos que não podem ser encerrados ou interrompidos com um sinal. Geralmente, para fazê-los desaparecer, você precisa reiniciar ou corrigir o problema.
- **Z**: Zombie (Zumbi); discutimos em uma lição anterior que zumbis são processos terminados que estão esperando que seus status sejam coletados.
- **T**: Stopped (Parado); um processo que foi suspenso/parado.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento e estados de processos Linux:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Neste laboratório, você aprenderá habilidades essenciais para gerenciar e monitorar processos em um sistema Linux. Você explorará como interagir com processos em primeiro e segundo plano, inspecioná-los com `ps`, monitorar recursos com `top`, ajustar a prioridade com `renice` e encerrá-los com `kill`.

Este laboratório o ajudará a aplicar os conceitos de estados de processo em cenários reais e a construir confiança com o gerenciamento de processos Linux.

## Quiz Question

Qual código STAT é usado para representar uma suspensão ininterrupta?

## Quiz Answer

D
