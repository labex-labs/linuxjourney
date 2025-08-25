---
index: 2
lang: "pt"
title: "Controlando o Terminal"
meta_title: "Controle de Terminal - Processos"
meta_description: "Aprenda sobre o controle de terminais no Linux, incluindo TTY vs. PTS, e como os processos estão vinculados a eles. Entenda os processos daemon. Comece sua jornada no Linux!"
meta_keywords: "terminal de controle, TTY, PTS, terminal Linux, processos daemon, iniciante em Linux, tutorial Linux, guia Linux"
---

## Lesson Content

Discutimos como existe um campo TTY na saída do `ps`. O TTY é o terminal que executou o comando.

Existem dois tipos de terminais: **dispositivos de terminal** regulares e **dispositivos de pseudoterminal**. Um dispositivo de terminal regular é um dispositivo de terminal nativo no qual você pode digitar e enviar saída para o seu sistema. Isso soa como o aplicativo de terminal que você tem lançado para acessar seu shell, mas não é.

Vamos fazer uma digressão para que você possa ver isso em ação. Vá em frente e digite Ctrl-Alt-F1 para entrar no TTY1 (o primeiro console virtual). Você notará que não tem nada além do terminal — sem gráficos, etc. Isso é considerado um dispositivo de terminal regular. Você pode sair disso com Ctrl-Alt-F7.

Um pseudoterminal é o que você está acostumado a trabalhar. Eles emulam terminais com a janela do terminal shell e são denotados por PTS. Se você olhar o `ps` novamente, verá seu processo de shell em `pts/*`.

Ok, agora voltando ao terminal de controle: os processos geralmente estão vinculados a um terminal de controle. Por exemplo, se você estivesse executando um programa em sua janela de shell, como `find`, e fechasse a janela, seu processo também terminaria com ela.

Existem processos como processos daemon, que são processos especiais que essencialmente mantêm o sistema funcionando. Eles geralmente iniciam na inicialização do sistema e geralmente são encerrados quando o sistema é desligado. Eles são executados em segundo plano e, como não queremos que esses processos especiais sejam encerrados, eles não estão vinculados a um terminal de controle. Na saída do `ps`, o TTY é listado como um **?**, o que significa que ele não possui um terminal de controle.

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão dos processos Linux e sua interação com os terminais:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Neste laboratório, você aprenderá habilidades essenciais para gerenciar e monitorar processos em um sistema Linux. Você explorará como interagir com processos em primeiro e segundo plano, inspecioná-los com `ps`, monitorar recursos com `top`, ajustar a prioridade com `renice` e encerrá-los com `kill`.

Este laboratório o ajudará a aplicar os conceitos de gerenciamento de processos em cenários reais e a construir confiança na compreensão de como os processos são executados e interagem com o sistema.

## Quiz Question

Qual valor é dado para um processo que não possui um terminal de controle?

## Quiz Answer

?
