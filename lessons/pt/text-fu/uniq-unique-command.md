---
index: 14
lang: "pt"
title: "uniq (Único)"
meta_title: "uniq (Único) - Text-Fu"
meta_description: "Aprenda a usar o comando `uniq` do Linux para remover linhas duplicadas de arquivos de texto. Descubra opções como -c, -u, -d e combine com `sort` para uma limpeza de dados eficaz."
meta_keywords: "comando uniq, Linux uniq, remover duplicatas, sort uniq, tutorial Linux, processamento de texto, Linux para iniciantes, guia Linux"
---

## Lesson Content

O comando `uniq` (único) é outra ferramenta útil para analisar texto.

Digamos que você tivesse um arquivo com muitas duplicatas:

```plaintext
reading.txt
book
book
paper
paper
article
article
magazine
```

E você quisesse remover as duplicatas; bem, você pode usar o comando `uniq`:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

Vamos obter a contagem de quantas ocorrências de uma linha:

```bash
$ uniq -c reading.txt
2 book
2 paper
2 article
1 magazine
```

Vamos obter apenas valores únicos:

```bash
$ uniq -u reading.txt
magazine
```

Vamos obter apenas valores duplicados:

```bash
$ uniq -d reading.txt
book
paper
article
```

**Nota**: `uniq` não detecta linhas duplicadas a menos que sejam adjacentes. Por exemplo:

Digamos que você tivesse um arquivo com duplicatas que não são adjacentes:

```plaintext
reading.txt
book
paper
book
paper
article
magazine
article
```

```bash
$ uniq reading.txt
reading.txt
book
paper
book
paper
article
magazine
article
```

O resultado retornado por `uniq` conterá todas as entradas, ao contrário do primeiro exemplo.

Para superar essa limitação do `uniq`, podemos usar `sort` em combinação com `uniq`:

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do processamento de texto com `uniq` e `sort`:

1. **[Comando Linux uniq: Filtragem de Duplicatas](https://labex.io/pt/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - Aprenda a usar o comando Linux `uniq` em combinação com `sort` para identificar, filtrar e analisar linhas duplicadas em arquivos de texto.
2. **[Comando Linux sort: Classificação de Texto](https://labex.io/pt/labs/linux-linux-sort-command-text-sorting-219196)** - Pratique o uso do comando `sort` para organizar linhas de arquivos de texto, um passo crucial antes de usar `uniq` de forma eficaz.
3. **[Contagem e Classificação de Palavras](https://labex.io/pt/labs/linux-word-count-and-sorting-388125)** - Aprenda as ferramentas essenciais de processamento de texto do Linux `wc` (contagem de palavras) e `sort` neste desafio prático. Aprenda a contar linhas, palavras e caracteres, encontrar padrões frequentes e classificar dados de forma eficiente para várias tarefas de análise de texto.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com o processamento de texto e manipulação de dados no Linux.

## Quiz Question

Qual comando você usaria para remover duplicatas em um arquivo?

## Quiz Answer

uniq
