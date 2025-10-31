---
index: 6
lang: "pt"
title: "Sinais"
meta_title: "Sinais - Processos"
meta_description: "Explore os fundamentos dos sinais do Linux, um mecanismo chave para o gerenciamento de processos. Aprenda como funcionam os sinais de processo do Linux como SIGTERM (sinal 15 linux) e SIGKILL, e entenda seus códigos de sinal do SO."
meta_keywords: "sinais linux, sinais de processo linux, sinal 15 linux, código de sinal so, SIGKILL, SIGTERM, SIGINT, gerenciamento de processos, tutorial linux"
---

## Lesson Content

No Linux, um sinal é uma interrupção de software enviada a um processo para notificá-lo de que ocorreu um evento importante. Entender os **sinais linux** é fundamental para gerenciar processos e o comportamento do sistema de forma eficaz.

### O Propósito dos Sinais

Os sinais servem como um método primário de comunicação entre processos (IPC). Eles têm muitos usos:

- **Interação do Usuário**: Um usuário pode digitar caracteres especiais do terminal, como `Ctrl-C` (SIGINT) ou `Ctrl-Z` (SIGTSTP), para interromper ou suspender processos em primeiro plano.
- **Notificações do Kernel**: O kernel pode enviar sinais a um processo para notificá-lo sobre problemas de hardware ou software, como um acesso ilegal à memória (SIGSEGV).
- **Gerenciamento de Processos**: Administradores de sistema e outros processos usam sinais para gerenciar o ciclo de vida de outros processos, como solicitar terminação ou recarregamento de configuração.

### O Ciclo de Vida do Sinal

Quando um evento gera um sinal, ele é primeiro entregue a um processo de destino. O sinal permanece em estado "pendente" até que o kernel execute o processo. Quando o processo é agendado, o sinal é entregue. No entanto, os processos têm máscaras de sinal, que podem ser configuradas para bloquear a entrega de sinais específicos.

Quando um sinal é entregue, o processo pode tomar uma das várias ações:

- **Ignorar o sinal**: O processo simplesmente descarta o sinal e continua a execução.
- **Capturar o sinal**: O processo executa uma função personalizada chamada manipulador de sinal (signal handler) para responder ao evento.
- **Executar a ação padrão**: Se não for capturado ou ignorado, a ação padrão é executada. Para muitos sinais, isso significa terminar o processo.
- **Bloquear o sinal**: Se o sinal estiver na máscara de sinal do processo, ele permanece pendente até ser desbloqueado.

### Sinais Comuns de Processos Linux

Cada sinal é definido por um número inteiro, mas são quase sempre referidos por seus nomes simbólicos (o **código sig do os**), que começam com `SIG`. Embora os números possam variar ligeiramente entre arquiteturas, os nomes são consistentes. Aqui estão alguns dos **sinais de processo linux** mais comuns:

- **SIGHUP (1)**: Hangup (Desconexão). Frequentemente usado para instruir um daemon a recarregar sua configuração.
- **SIGINT (2)**: Interrupção. Enviado por `Ctrl-C`. É um pedido para terminar o processo.
- **SIGKILL (9)**: Matar. Esta é uma terminação imediata e forçada. O processo não pode capturar, ignorar ou bloquear este sinal.
- **SIGSEGV (11)**: Falha de Segmentação. Indica que o processo fez uma referência de memória inválida.
- **SIGTERM (15)**: Terminação. Esta é a maneira padrão e educada de solicitar a terminação de um processo. É o sinal padrão enviado pelo comando `kill`. Um processo pode capturar este sinal para realizar a limpeza antes de sair. Este é frequentemente referido como **sinal 15 linux**.
- **SIGSTOP**: Parar. Pausa o processo. Assim como o SIGKILL, não pode ser capturado ou ignorado.

A principal diferença entre `SIGTERM` (**sinal linux 15**) e `SIGKILL` é que `SIGTERM` é um pedido que pode ser tratado, enquanto `SIGKILL` é um comando que destrói o processo imediatamente.

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão de processos e como os sinais são usados para interagir com eles:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Neste laboratório, você aprenderá habilidades essenciais para gerenciar e monitorar processos em um sistema Linux. Você explorará como interagir com processos em primeiro plano e em segundo plano, inspecioná-los com `ps`, monitorar recursos com `top`, ajustar a prioridade com `renice` e terminá-los com `kill`. Terminar processos com `kill` é uma aplicação direta do envio de sinais.

Este laboratório o ajudará a aplicar os conceitos de gerenciamento de processos e o uso subjacente de sinais em cenários reais e a construir confiança com a administração de sistemas Linux.

## Quiz Question

Qual sinal não pode ser bloqueado? Por favor, responda em inglês, usando o nome exato do sinal e prestando atenção às maiúsculas e minúsculas.

## Quiz Answer

SIGKILL
