---
index: 7
lang: "pt"
title: "kill (Terminar)"
meta_title: "kill (Terminar) - Processos"
meta_description: "Domine o comando Linux kill para gerenciar e encerrar processos. Este guia aborda as diferenças entre kill vs. terminar e explica sinais como kill sigterm (SIGTERM), SIGKILL e kill sighup (SIGHUP)."
meta_keywords: "comando kill, kill sigterm, kill sighup, linux kill -0, kill vs terminar, kill -15 linux, SIGTERM, SIGKILL, gerenciamento de processos, terminar processo"
---

## Lesson Content

No Linux, você pode gerenciar processos enviando sinais a eles. O comando principal para isso é o `kill`, que, apesar do nome, pode enviar vários sinais, não apenas aqueles que terminam um processo.

### Terminação Padrão com kill sigterm

Quando você usa o comando `kill` apenas com um ID de Processo (PID), ele envia um sinal `TERM` por padrão. Esta é a maneira padrão e elegante de solicitar que um programa termine.

```bash
kill 12445
```

O sinal `kill sigterm` (também conhecido como `SIGTERM` ou sinal 15) solicita que o processo seja encerrado de forma limpa. Isso dá ao processo a chance de salvar seu progresso e liberar recursos adequadamente. Você também pode usar explicitamente o número do sinal, tornando `kill -15 12445` equivalente ao comando acima. Isso aborda a consulta comum `kill -15 linux`.

### Forçando a Terminação com SIGKILL

Às vezes, um processo fica sem resposta e não reage a um sinal `SIGTERM`. Nesses casos, você pode forçá-lo a parar usando o sinal `KILL`.

```bash
kill -9 12445
```

O sinal `SIGKILL` (sinal 9) termina o processo imediatamente, sem dar a ele a chance de limpeza. Esta é uma diferença fundamental no debate `kill vs terminate`; `SIGKILL` é uma terminação incondicional, enquanto `SIGTERM` é um pedido educado.

### Entendendo Outros Sinais Comuns

Embora `SIGTERM` e `SIGKILL` sejam os mais comuns, outros sinais também são úteis para o gerenciamento de processos.

- **SIGHUP**: O sinal `kill sighup` (Hangup, sinal 1) é tradicionalmente enviado a um processo quando seu terminal de controle é fechado. Ele pode ser usado para instruir processos daemon a recarregar seus arquivos de configuração.
- **SIGINT**: O sinal de Interrupção (sinal 2) é enviado quando você pressiona `Ctrl-C`. Ele solicita que o processo interrompa sua operação atual.
- **SIGSTOP**: Este sinal (sinal 19) pausa um processo sem terminá-lo. O processo pode ser retomado mais tarde com o sinal `SIGCONT`.

### Verificando a Existência do Processo com kill -0

Um caso de uso especial é `linux kill -0`. Este comando não envia um sinal de fato, mas verifica se um processo com o PID especificado existe e se você tem permissão para enviar um sinal a ele.

```bash
kill -0 12445
```

Se o comando for executado com sucesso (código de saída 0), o processo existe. Se falhar, o processo não existe ou você não tem permissões.

## Exercise

Para aplicar o que você aprendeu, experimente este laboratório prático para reforçar sua compreensão sobre gerenciamento e terminação de processos:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Neste laboratório, você aprenderá habilidades essenciais para gerenciar e monitorar processos em um sistema Linux. Você explorará como interagir com processos em primeiro plano e em segundo plano, inspecioná-los com `ps`, monitorar recursos com `top`, ajustar a prioridade com `renice` e terminá-los com `kill`.

Este laboratório ajudará você a aplicar os conceitos de controle e terminação de processos em cenários reais e a ganhar confiança no gerenciamento de processos Linux.

## Quiz Question

Qual é o nome do sinal para o comando `kill` padrão? Por favor, responda em inglês. Observe que a resposta diferencia maiúsculas de minúsculas.

## Quiz Answer

SIGTERM
