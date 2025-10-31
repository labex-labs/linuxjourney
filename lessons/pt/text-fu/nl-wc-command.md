---
index: 15
lang: "pt"
title: "wc e nl"
meta_title: "wc e nl - Text-Fu"
meta_description: "Domine os comandos wc e nl neste tutorial Linux. Aprenda a fazer contagem de palavras no Linux, adicionar números de linha a arquivos e realizar análises básicas de arquivos. Um guia perfeito para iniciantes aprimorarem suas habilidades de linha de comando."
meta_keywords: "comando wc, comando nl, contagem de palavras Linux, contar palavras em arquivo Linux, números de linha Linux, comando nl Linux, análise de arquivos, processamento de texto Linux, linha de comando Linux, tutorial Linux para iniciantes"
---

## Lesson Content

No Linux, analisar arquivos de texto é uma tarefa comum. Dois utilitários fundamentais para isso são `wc` e `nl`, que ajudam você a contar conteúdo e numerar linhas, respectivamente.

### Contagem com o Comando wc

O comando `wc` (word count - contagem de palavras) é uma ferramenta poderosa para análise básica de arquivos. Quando executado em um arquivo, ele fornece um resumo de seu conteúdo.

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

A saída exibe três números seguidos pelo nome do arquivo. Da esquerda para a direita, esses números representam:

1. O número de linhas.
2. O número de palavras (a contagem de palavras do Linux).
3. O número de bytes.

### Obtendo Contagens Específicas

Muitas vezes, você precisa apenas de uma informação. Você pode usar opções para exibir uma contagem específica em vez das três.

- `-l`: Mostra apenas a contagem de linhas.
- `-w`: Mostra apenas a contagem de palavras.
- `-c`: Mostra apenas a contagem de bytes.

Por exemplo, para ver apenas o número de linhas no arquivo `/etc/passwd`, você usaria:

```bash
$ wc -l /etc/passwd
96
```

### Numerando Linhas com o Comando nl

Outro comando útil para inspecionar arquivos é o `nl` (number lines - numerar linhas). Como o nome sugere, ele lê um arquivo e exibe seu conteúdo com números de linha adicionados ao início de cada linha. Isso é especialmente útil para revisar scripts ou arquivos de configuração.

Considere um arquivo chamado `file1.txt` com o seguinte conteúdo:

```plaintext
i
like
turtles
```

Usando o comando `nl`, você pode facilmente adicionar números de linha do Linux:

```bash
$ nl file1.txt
     1 i
     2 like
     3 turtles
```

Tanto `wc` quanto `nl` são comandos essenciais para o processamento de texto do dia a dia na linha de comando do Linux.

## Exercise

Para dominar esses comandos, a prática manual é fundamental. Tente estes exercícios para solidificar suas habilidades em contagem de texto e numeração de linhas no Linux:

1. **[Comando wc do Linux: Contagem de Texto](https://labex.io/pt/labs/linux-linux-wc-command-text-counting-219200)** - Pratique a contagem de palavras, linhas e caracteres em arquivos de texto usando o comando `wc`.
2. **[Comando nl do Linux: Numeração de Linhas](https://labex.io/pt/labs/linux-linux-nl-command-line-numbering-210988)** - Aprenda a numerar linhas em arquivos de texto com o comando `nl`.
3. **[Contagem de Palavras e Ordenação](https://labex.io/pt/labs/linux-word-count-and-sorting-388125)** - Aplique seu conhecimento de `wc` para contar linhas, palavras e caracteres, e combine-o com a ordenação para tarefas práticas de análise de texto.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários do mundo real e a ganhar confiança no processamento de texto no Linux.

## Quiz Question

Qual comando e opção você usaria para exibir apenas a contagem total de palavras de um arquivo? Por favor, responda usando apenas o comando e sua opção em inglês. A resposta diferencia maiúsculas de minúsculas.

## Quiz Answer

wc -w
