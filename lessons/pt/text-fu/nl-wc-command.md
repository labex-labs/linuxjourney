---
index: 15
lang: "pt"
title: "wc e nl"
meta_title: "wc e nl - Text-Fu"
meta_description: "Aprenda os comandos wc e nl do Linux. Entenda a contagem de palavras, numeração de linhas e análise de arquivos. Melhore suas habilidades de linha de comando Linux hoje!"
meta_keywords: "comando wc, comando nl, contagem de palavras Linux, números de linha Linux, análise de arquivo, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

O comando `wc` (word count) mostra a contagem total de palavras em um arquivo.

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

Ele exibe o número de linhas, o número de palavras e o número de bytes, respectivamente.

Para ver apenas a contagem de um determinado campo, use as opções `-l`, `-w` ou `-c`, respectivamente.

```bash
$ wc -l /etc/passwd
96
```

Outro comando que você pode usar para verificar a contagem de linhas em um arquivo é o comando `nl` (number lines).

```plaintext
file1.txt
i
like
turtles
```

```bash
$ nl file1.txt
1. i
2. like
3. turtles
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da contagem de texto e numeração de linhas no Linux:

1. **[Comando Linux wc: Contagem de Texto](https://labex.io/pt/labs/linux-linux-wc-command-text-counting-219200)** - Pratique a contagem de palavras, linhas e caracteres em arquivos de texto usando o comando `wc`.
2. **[Comando Linux nl: Numeração de Linhas](https://labex.io/pt/labs/linux-linux-nl-command-line-numbering-210988)** - Aprenda a numerar linhas em arquivos de texto com o comando `nl`.
3. **[Contagem de Palavras e Classificação](https://labex.io/pt/labs/linux-word-count-and-sorting-388125)** - Aplique seu conhecimento de `wc` para contar linhas, palavras e caracteres, e combine-o com a classificação para tarefas práticas de análise de texto.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com o processamento de texto no Linux.

## Quiz Question

Qual comando você usaria para obter o número total de palavras em um arquivo e apenas as palavras?

## Quiz Answer

wc -w
