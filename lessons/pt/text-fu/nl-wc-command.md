---
title: "wc e nl"
description: "Aprenda os comandos wc e nl do Linux. Entenda a contagem de palavras, numeração de linhas e análise de arquivos. Melhore suas habilidades de linha de comando Linux hoje!"
keywords: "comando wc, comando nl, contagem de palavras Linux, números de linha Linux, análise de arquivo, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

O comando `wc` (word count) mostra a contagem total de palavras em um arquivo.

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

Ele exibe o número de linhas, número de palavras e número de bytes, respectivamente.

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

Como você obteria a contagem total de linhas usando o comando `nl` sem pesquisar toda a saída? Dica: Use alguns dos outros comandos que você aprendeu neste curso.

## Quiz Question

Qual comando você usaria para obter o número total de palavras em um arquivo e apenas as palavras?

## Quiz Answer

wc -w
