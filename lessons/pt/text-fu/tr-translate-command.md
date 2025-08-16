---
title: "tr (Traduzir)"
description: "Aprenda a usar o comando 'tr' do Linux para traduzir e deletar caracteres. Entenda a tradução de caracteres com exemplos e exercícios. Comece sua jornada no Linux!"
keywords: "comando tr, Linux tr, traduzir caracteres, deletar caracteres, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

O comando `tr` (translate) permite traduzir um conjunto de caracteres para outro conjunto de caracteres. Vamos tentar um exemplo de tradução de todos os caracteres minúsculos para caracteres maiúsculos.

```bash
$ tr a-z A-Z
hello
HELLO
```

Como você pode ver, transformamos os intervalos de `a-z` em `A-Z`, e todo o texto que digitamos em minúsculas é convertido para maiúsculas.

## Exercise

Experimente o seguinte comando. O que acontece?

```bash
$ tr -d ello
hello
```

## Quiz Question

Qual comando é usado para traduzir caracteres?

## Quiz Answer

tr
