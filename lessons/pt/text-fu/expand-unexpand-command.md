---
title: "expand e unexpand"
description: "Aprenda a converter tabulações em espaços com o comando `expand` e espaços em tabulações com `unexpand`. Melhore a formatação de arquivos de texto com este tutorial de Linux."
keywords: "comando expand, comando unexpand, tabulações Linux, espaços Linux, formatação de texto, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Em nossa lição sobre o comando `cut`, tínhamos nosso arquivo `sample.txt` que continha uma tabulação. Normalmente, as tabulações mostram uma diferença notável, mas alguns arquivos de texto não mostram isso bem o suficiente. Ter tabulações em um arquivo de texto pode não fornecer o espaçamento desejado. Para transformar suas tabulações em espaços, use o comando `expand`.

```bash
expand sample.txt
```

O comando acima imprimirá a saída com cada tabulação convertida em um grupo de espaços. Para salvar esta saída em um arquivo, use o redirecionamento de saída como mostrado abaixo.

```bash
expand sample.txt > result.txt
```

Oposto ao `expand`, podemos converter de volta cada grupo de espaços em uma tabulação com o comando `unexpand`:

```bash
unexpand -a result.txt
```

## Exercise

O que acontece se você apenas digitar `expand` sem entrada de arquivo?

## Quiz Question

Qual comando é usado para converter tabulações em espaços?

## Quiz Answer

expand
