---
title: "uniq (Único)"
description: "Aprenda a usar o comando `uniq` do Linux para remover linhas duplicadas de arquivos de texto. Descubra opções como -c, -u, -d e combine com `sort` para uma limpeza de dados eficaz."
keywords: "comando uniq, Linux uniq, remover duplicatas, sort uniq, tutorial Linux, processamento de texto, Linux para iniciantes, guia Linux"
---

## Lesson Content

O comando `uniq` (unique) é outra ferramenta útil para analisar texto.

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

**Note**: `uniq` não detecta linhas duplicadas a menos que sejam adjacentes. Por exemplo:

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

Que resultado você obteria se tentasse `uniq -uc`?

## Quiz Question

Qual comando você usaria para remover duplicatas em um arquivo?

## Quiz Answer

uniq
