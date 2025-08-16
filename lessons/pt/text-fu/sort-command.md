---
title: "sort"
description: "Aprenda a usar o comando sort do Linux para ordenar arquivos de texto. Descubra opções como ordenação inversa e numérica. Melhore suas habilidades na linha de comando do Linux!"
keywords: "comando sort Linux, sort -r, sort -n, tutorial Linux, linha de comando, Linux para iniciantes, guia sort"
---

## Lesson Content

O comando `sort` é útil para ordenar linhas.

```plaintext
file1.txt
dog
cow
cat
elephant
bird

$ sort file1.txt
bird
cat
cow
dog
elephant
```

Você também pode fazer uma ordenação inversa:

```bash
$ sort -r file1.txt
elephant
dog
cow
cat
bird
```

E também ordenar por valor numérico:

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

O verdadeiro poder do `sort` vem com sua capacidade de ser combinado com outros comandos. Tente o seguinte comando e veja o que acontece:

```bash
ls /etc | sort -rn
```

## Quiz Question

Qual flag você usa para realizar uma ordenação inversa?

## Quiz Answer

-r
