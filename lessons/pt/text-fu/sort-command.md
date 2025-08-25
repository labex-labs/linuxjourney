---
index: 12
lang: "pt"
title: "sort"
meta_title: "sort - Text-Fu"
meta_description: "Aprenda a usar o comando sort do Linux para ordenar arquivos de texto. Descubra opções como ordenação inversa e numérica. Melhore suas habilidades de linha de comando Linux!"
meta_keywords: "comando sort Linux, sort -r, sort -n, tutorial Linux, linha de comando, Linux para iniciantes, guia sort"
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

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do comando `sort` e do processamento de texto:

1. **[Comando sort do Linux: Ordenação de Texto](https://labex.io/pt/labs/linux-linux-sort-command-text-sorting-219196)** - Este laboratório oferece uma introdução direta ao comando `sort`, permitindo que você pratique a ordenação de linhas de arquivos de texto de várias maneiras, incluindo ordem crescente e decrescente.
2. **[Contagem e Ordenação de Palavras](https://labex.io/pt/labs/linux-word-count-and-sorting-388125)** - Neste desafio, você aplicará seu conhecimento de ordenação juntamente com a contagem de palavras para analisar dados de texto, ajudando-o a encontrar padrões frequentes e ordenar dados de forma eficiente.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com a manipulação e ordenação de texto no Linux.

## Quiz Question

Qual flag você usa para realizar uma ordenação inversa?

## Quiz Answer

-r
