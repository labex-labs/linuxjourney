---
index: 10
lang: "pt"
title: "expand e unexpand"
meta_title: "expand e unexpand - Text-Fu"
meta_description: "Aprenda a converter tabulações em espaços com o comando `expand` e espaços em tabulações com `unexpand`. Melhore a formatação de arquivos de texto com este tutorial de Linux."
meta_keywords: "comando expand, comando unexpand, tabulações Linux, espaços Linux, formatação de texto, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Em nossa lição sobre o comando `cut`, tínhamos nosso arquivo `sample.txt` que continha uma tabulação. Normalmente, as tabulações mostram uma diferença notável, mas alguns arquivos de texto não mostram isso muito bem. Ter tabulações em um arquivo de texto pode não fornecer o espaçamento desejado. Para mudar suas tabulações para espaços, use o comando `expand`.

```bash
expand sample.txt
```

O comando acima imprimirá a saída com cada tabulação convertida em um grupo de espaços. Para salvar esta saída em um arquivo, use o redirecionamento de saída como mostrado abaixo.

```bash
expand sample.txt > result.txt
```

Oposto a `expand`, podemos converter de volta cada grupo de espaços para uma tabulação com o comando `unexpand`:

```bash
unexpand -a result.txt
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da manipulação de texto e redirecionamento no Linux:

1. **[Redirecionando Entrada e Saída no Linux](https://labex.io/pt/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Pratique o controle do fluxo de dados de comandos manipulando a saída padrão (stdout), erro padrão (stderr) e entrada padrão (stdin) usando operadores como `>` e `>>`.
2. **[Processamento de Texto Simples](https://labex.io/pt/labs/linux-simple-text-processing-18004)** - Aprenda a usar comandos poderosos como `tr`, `col`, `join` e `paste` para manipular e analisar dados de texto de forma eficiente, aprimorando suas habilidades de linha de comando para processamento de dados.
3. **[Processamento de Texto e Expressões Regulares](https://labex.io/pt/labs/linux-text-processing-and-regular-expressions-18003)** - Aprenda as poderosas ferramentas de processamento de texto `grep`, `sed` e `awk`, e use expressões regulares para manipulação de texto eficiente e correspondência de padrões no Linux.

Esses laboratórios o ajudarão a aplicar os conceitos de transformação de texto e manipulação de arquivos em cenários reais e a construir confiança com as ferramentas de linha de comando do Linux.

## Quiz Question

Qual comando é usado para converter tabulações em espaços?

## Quiz Answer

expand
