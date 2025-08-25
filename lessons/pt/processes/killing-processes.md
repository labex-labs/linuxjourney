---
index: 7
lang: "pt"
title: "kill (Terminar)"
meta_title: "kill (Terminar) - Processos"
meta_description: "Aprenda como usar o comando 'kill' do Linux para encerrar processos. Entenda SIGTERM, SIGKILL e outros sinais para gerenciamento de processos. Comece a aprender agora!"
meta_keywords: "comando kill, processos Linux, SIGTERM, SIGKILL, tutorial Linux, iniciante, gerenciamento de processos, guia Linux"
---

## Lesson Content

Você pode enviar sinais que encerram processos; tal comando é apropriadamente chamado de comando `kill`.

```bash
kill 12445
```

O `12445` é o PID do processo que você deseja encerrar. Por padrão, ele envia um sinal `TERM`. O sinal `SIGTERM` é enviado a um processo para solicitar sua terminação, permitindo que ele libere seus recursos de forma limpa e salve seu estado.

Você também pode especificar um sinal com o comando `kill`:

```bash
kill -9 12445
```

Isso executará o sinal `SIGKILL` e encerrará o processo.

### Diferenças entre SIGHUP, SIGINT, SIGTERM, SIGKILL, SIGSTOP?

Esses sinais soam razoavelmente semelhantes, mas eles têm suas diferenças.

- SIGHUP - Hangup (desligar), enviado a um processo quando o terminal de controle é fechado. Por exemplo, se você fechasse uma janela de terminal que tinha um processo em execução, você receberia um sinal `SIGHUP`. Então, basicamente, você foi "desligado".
- SIGINT - É um sinal de interrupção, então você pode usar Ctrl-C, e o sistema tentará encerrar o processo de forma graciosa.
- SIGTERM - Encerra o processo, mas permite que ele faça alguma limpeza primeiro.
- SIGKILL - Encerra o processo, encerra-o com fogo, não faz nenhuma limpeza.
- SIGSTOP - Para/suspende um processo.

## Exercise

Prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento e terminação de processos:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Neste laboratório, você aprenderá habilidades essenciais para gerenciar e monitorar processos em um sistema Linux. Você explorará como interagir com processos em primeiro e segundo plano, inspecioná-los com `ps`, monitorar recursos com `top`, ajustar a prioridade com `renice` e encerrá-los com `kill`.

Este laboratório o ajudará a aplicar os conceitos de controle e terminação de processos em cenários reais e a construir confiança no gerenciamento de processos Linux.

## Quiz Question

Qual é o nome do sinal para o comando `kill` padrão?

## Quiz Answer

SIGTERM
