---
lang: "pt"
title: "kill (Encerrar)"
meta_description: "Aprenda como usar o comando 'kill' do Linux para encerrar processos. Entenda SIGTERM, SIGKILL e outros sinais para gerenciamento de processos. Comece a aprender agora!"
meta_keywords: "comando kill, processos Linux, SIGTERM, SIGKILL, tutorial Linux, iniciante, gerenciamento de processos, guia Linux"
---

## Lesson Content

Você pode enviar sinais que encerram processos; tal comando é apropriadamente chamado de comando `kill`.

```bash
kill 12445
```

O `12445` é o PID do processo que você deseja encerrar. Por padrão, ele envia um sinal `TERM`. O sinal `SIGTERM` é enviado a um processo para solicitar sua terminação, permitindo que ele libere seus recursos e salve seu estado de forma limpa.

Você também pode especificar um sinal com o comando `kill`:

```bash
kill -9 12445
```

Isso executará o sinal `SIGKILL` e encerrará o processo.

### Diferenças entre SIGHUP, SIGINT, SIGTERM, SIGKILL, SIGSTOP?

Todos esses sinais soam razoavelmente semelhantes, mas eles têm suas diferenças.

- SIGHUP - Hangup (desconexão), enviado a um processo quando o terminal de controle é fechado. Por exemplo, se você fechasse uma janela de terminal que tinha um processo em execução, você receberia um sinal `SIGHUP`. Então, basicamente, você foi "desligado".
- SIGINT - É um sinal de interrupção, então você pode usar Ctrl-C, e o sistema tentará encerrar o processo de forma graciosa.
- SIGTERM - Encerra o processo, mas permite que ele faça alguma limpeza primeiro.
- SIGKILL - Encerra o processo, encerra-o com fogo, não faz nenhuma limpeza.
- SIGSTOP - Para/suspende um processo.

## Exercise

Encerre alguns processos usando diferentes sinais.

## Quiz Question

Qual é o nome do sinal para o comando `kill` padrão?

## Quiz Answer

SIGTERM
