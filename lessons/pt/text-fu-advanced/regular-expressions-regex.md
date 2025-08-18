---
lang: "pt"
title: "regex (Expressões Regulares)"
meta_title: "regex (Expressões Regulares) - Text-Fu Avançado"
meta_description: "Aprenda expressões regulares (regex) para correspondência de padrões no Linux. Entenda a sintaxe regex como ^, $, ., e [] para manipulação de texto. Melhore suas habilidades com grep!"
meta_keywords: "expressões regulares, regex, regex Linux, grep regex, correspondência de padrões, tutorial regex, comandos Linux, iniciante"
---

## Lesson Content

Expressões regulares são uma ferramenta poderosa para seleção baseada em padrões. Elas usam notações especiais semelhantes às que já encontramos, como o curinga `*`.

Vamos abordar algumas das expressões regulares mais comuns; estas são quase universais em qualquer linguagem de programação.

Usaremos esta frase como nossa string de teste:

```plaintext
sally sells seashells
by the seashore
```

### 1. Início de uma linha com ^

```plaintext
^by
would match the line "by the seashore"
```

### 2. Fim de uma linha com $

```plaintext
seashore$
would match the line "by the seashore"
```

### 3. Correspondência de qualquer caractere único com

```plaintext
b.
would match by
```

### 4. Notação de colchetes com [] e ()

Isso pode ser um pouco complicado. Colchetes nos permitem especificar caracteres encontrados dentro do colchete.

```plaintext
d[iou]g
would match: dig, dog, dug
```

A âncora anterior `^`, quando usada em um colchete, significa qualquer coisa, exceto os caracteres dentro do colchete.

```plaintext
d[^i]g
would match: dog and dug but not dig
```

Colchetes também podem usar intervalos para aumentar a quantidade de caracteres que você deseja usar.

```plaintext
d[a-c]g
will match patterns like dag, dbg, and dcg
```

Tenha cuidado, no entanto, pois os colchetes diferenciam maiúsculas de minúsculas:

```plaintext
d[A-C]g
will match dAg, dBg and dCg but not dag, dbg and dcg
```

E essas são algumas expressões regulares básicas.

## Exercise

Experimente combinar expressões regulares com `grep` e pesquisar em alguns arquivos.

```bash
grep [regular expression here] [file]
```

## Quiz Question

Qual expressão regular você usaria para corresponder a um único caractere?

## Quiz Answer

.
