---
index: 2
lang: "pt"
title: "Terminal de Controle"
meta_title: "Terminal de Controle - Processos"
meta_description: "Explore o conceito de um terminal de controle no Linux. Saiba o que é um TTY, a diferença entre TTY e PTS, e como usar a saída de `ps tty` para identificar processos sem um terminal de controle, como daemons."
meta_keywords: "terminal de controle, ps tty, o que é tty, como usar ps, TTY, PTS, terminal Linux, processo daemon, processos Linux"
---

## Lesson Content

Ao inspecionar processos em execução, você notará um campo `TTY` na saída do comando `ps`. Este campo é importante, pois indica o **terminal de controle** que executou o comando. Entender este conceito é fundamental para gerenciar processos de forma eficaz.

### O que é um TTY

TTY é uma abreviação para "Teletype", que historicamente era um dispositivo físico para interagir com um computador. Nos sistemas Linux modernos, um TTY refere-se ao terminal que fornece a entrada e saída padrão para um processo.

Existem dois tipos principais de terminais que você encontrará: dispositivos de terminal e dispositivos de pseudo-terminal.

### Dispositivos de Terminal vs. Pseudo-Terminais

Aparelho de terminal verdadeiro é um console nativo que permite digitar comandos e ver a saída diretamente. Você pode experimentar isso mudando para um console virtual. Em muitos sistemas, você pode pressionar `Ctrl-Alt-F1` para acessar o TTY1. Você verá um prompt de login em um ambiente puramente baseado em texto, sem interface gráfica. Este é um dispositivo de terminal clássico. Para retornar à sua sessão gráfica, você pode tipicamente usar `Ctrl-Alt-F7` (a combinação exata de teclas pode variar).

Um pseudo-terminal (PTS), por outro lado, é o que você mais comumente usa. Quando você abre um aplicativo de terminal dentro do seu ambiente de desktop gráfico, você está usando um PTS. Estes emulam um terminal dentro de uma janela. Se você verificar a saída de `ps tty` para seu shell, verá seu TTY listado como `pts/*`.

### O Papel do Terminal de Controle

A maioria dos processos está vinculada a um **terminal de controle**. Isso significa que o ciclo de vida do processo está ligado à sessão de terminal que o iniciou. Por exemplo, se você executar um programa como `find` na sua janela do terminal e depois fechar essa janela, o processo `find` também será encerrado.

### Processos Sem um Terminal de Controle

Alguns processos, conhecidos como daemons, são projetados para serem executados em segundo plano e gerenciar serviços do sistema. Esses processos geralmente são iniciados quando o sistema é inicializado e só são interrompidos quando é desligado.

Para evitar que sejam encerrados acidentalmente, os daemons não estão anexados a um **terminal de controle**. Quando você aprende **como usar ps** para examinar esses processos, verá um ponto de interrogação (`?`) na coluna TTY. Este `?` significa que o processo não tem um terminal de controle e está sendo executado independentemente de qualquer sessão de usuário.

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão de processos Linux e sua interação com terminais:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Neste laboratório, você aprenderá habilidades essenciais para gerenciar e monitorar processos em um sistema Linux. Você explorará como interagir com processos em primeiro plano e em segundo plano, inspecioná-los com `ps`, monitorar recursos com `top`, ajustar a prioridade com `renice` e terminá-los com `kill`.

Este laboratório o ajudará a aplicar os conceitos de gerenciamento de processos em cenários reais e a construir confiança na compreensão de como os processos são executados e interagem com o sistema.

## Quiz Question

Qual valor é dado a um processo que não possui um terminal de controle?

## Quiz Answer

?
