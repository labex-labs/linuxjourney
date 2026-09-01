---
lesson_id: "regular-expressions-regex"
course_id: "advanced-text-fu"
lang: "pt"
order_index: 1
title: "regex (Expressões Regulares)"
description: "Aprenda como âncoras, conjuntos de caracteres, repetições e variantes de regex controlam a correspondência de textos."
meta_title: "regex (Expressões Regulares) - Text-Fu Avançado"
meta_description: "Domine os fundamentos das expressões regulares no Linux. Aprenda correspondência de padrões com grep usando âncoras, conjuntos e quantificadores."
meta_keywords: "expressão regular Linux, regex, fundamentos Linux, correspondência padrões, grep, processamento texto, aprender Linux, tutorial Linux"
---

Expressões regulares, frequentemente abreviadas como **regex**, descrevem padrões de texto. Ferramentas como `grep`, `sed` e `awk` usam regex, mas a sintaxe aceita pode variar; por isso, sempre identifique a ferramenta e a variante de expressão regular.

O GNU `grep` usa expressões regulares básicas (BRE) por padrão e expressões regulares estendidas (ERE) com `-E`. Esta lição apresenta construções compartilhadas pelas duas e depois destaca algumas extensões comuns de ERE.

Use esta entrada nos exemplos:

```text
sally sells seashells
by the seashore
```

## Correspondência de Texto Literal

A maioria dos caracteres comuns corresponde a si mesma. O padrão `seashells` seleciona uma linha que contenha essa sequência exata em qualquer posição:

```bash
$ grep 'seashells' sample.txt
sally sells seashells
```

Coloque padrões regex entre aspas para que o shell não os expanda nem os divida antes que a ferramenta os receba. Regex também é diferente da expansão de caminhos do shell: em uma regex, `*` repete o átomo anterior; em um glob do shell, `*` é por si só um curinga para uma sequência de caracteres de um caminho.

:::single-choice{#regex-versus-shell-star} O que `*` faz em uma expressão regular como `ab*`?

::option[Corresponde a qualquer nome de arquivo no diretório atual.]{#regex-shell-glob explanation="Isso descreve a expansão de caminhos do shell no contexto de um comando, não o significado de `*` dentro de uma regex."}
::option[Repete o `b` anterior zero ou mais vezes.]{#regex-repeat-b .correct explanation="Um quantificador de regex se aplica ao átomo imediatamente anterior; portanto, `ab*` corresponde a `a`, `ab`, `abb` e assim por diante."}
::option[Repete a cadeia completa `ab` exatamente duas vezes.]{#regex-repeat-ab-twice explanation="O asterisco se aplica apenas ao átomo anterior e permite zero ou mais repetições, não exatamente duas repetições da cadeia completa."}
:::

## Ancoragem de uma Correspondência

Fora de uma expressão entre colchetes, `^` no início de um padrão ancora a correspondência no início da linha:

```plaintext
^by
```

A âncora `$` corresponde ao final de uma linha:

```plaintext
seashore$
```

Combine as duas âncoras quando a linha inteira precisar se ajustar ao padrão:

```text
^by the seashore$
```

:::single-choice{#regex-complete-line} Qual padrão corresponde apenas a uma linha cujo texto completo é `by the seashore`?

::option[`^by the seashore$`]{#regex-anchored-line .correct explanation="O circunflexo exige que a correspondência comece no início, e o cifrão exige que termine com a linha."}
::option[`by the seashore`]{#regex-unanchored-line explanation="Sem âncoras, essa sequência pode corresponder dentro de uma linha maior com texto antes ou depois."}
::option[`$by the seashore^`]{#regex-reversed-anchors explanation="A âncora de fim não pode preceder o texto, e a de início não pode vir depois dele no padrão pretendido."}
:::

## Correspondência de um Caractere

O ponto corresponde a um caractere no modo comum de regex orientada por linhas:

```plaintext
b.
```

Isso corresponde a `by`, mas também pode corresponder a `ba` ou `b7`. Não corresponde a um `b` isolado, pois exige um caractere depois dele. Para corresponder a um ponto literal, use o escape `\.` ou coloque-o em uma expressão adequada entre colchetes.

:::single-choice{#regex-dot-character} Qual cadeia não corresponde ao padrão de linha completa `^b.$`?

::option[`by`]{#regex-dot-by explanation="O ponto corresponde a `y`; portanto, a linha de dois caracteres satisfaz o padrão."}
::option[`b`]{#regex-dot-b .correct explanation="O ponto exige um caractere depois de `b`, mas essa cadeia termina imediatamente."}
::option[`b7`]{#regex-dot-b7 explanation="O ponto corresponde ao dígito `7`; portanto, a linha de dois caracteres satisfaz o padrão."}
:::

## Uso de Expressões entre Colchetes

Uma expressão entre colchetes corresponde a um caractere de um conjunto especificado:

```plaintext
s[ae]lls
```

Isso corresponde a `sells` ou `salls` nessa posição.

Quando `^` é o primeiro caractere depois de `[`, ele nega o conjunto:

```plaintext
s[^e]lls
```

Isso corresponde a `salls`, mas não a `sells`, pois o caractere depois do primeiro `s` não pode ser `e`.

:::single-choice{#regex-negated-bracket} Ao que `[^e]` corresponde?

::option[Exatamente um caractere diferente de `e`.]{#regex-not-e .correct explanation="Um circunflexo inicial dentro dos colchetes complementa o conjunto, enquanto a expressão ainda consome um caractere."}
::option[Ao início de uma linha seguido de `e`.]{#regex-caret-e-anchor explanation="Dentro de uma expressão entre colchetes, um circunflexo inicial nega o conjunto, em vez de ancorar a linha."}
::option[A zero ou mais ocorrências da letra `e`.]{#regex-repeat-e explanation="A repetição exigiria um quantificador como `*`; essa expressão corresponde a um caractere que não seja `e`."}
:::

Intervalos podem descrever caracteres entre dois extremos:

```plaintext
d[a-c]g
```

Isso pode corresponder a `dag`, `dbg` ou `dcg`. O comportamento dos intervalos pode depender da ordenação do locale. Classes como `[[:lower:]]`, `[[:upper:]]` e `[[:digit:]]` muitas vezes expressam a intenção com mais clareza.

## Repetição e Combinação de Padrões

Tanto em BRE quanto em ERE, `*` significa zero ou mais repetições do átomo anterior:

```text
seashells*
```

Isso corresponde a `seashell` seguido de zero ou mais caracteres `s` adicionais. No modo ERE com `grep -E`, alguns operadores comuns são:

- `+`: uma ou mais repetições;
- `?`: zero ou uma repetição;
- `|`: a expressão à esquerda ou à direita;
- `(...)`: agrupa expressões.

Por exemplo:

```bash
$ grep -E '^(cat|dog)s?$' animals.txt
```

Esse comando seleciona linhas completas iguais a `cat`, `cats`, `dog` ou `dogs`. No modo BRE, esses operadores possuem regras de escape diferentes; portanto, não copie um padrão entre variantes sem verificá-lo.

:::single-choice{#regex-extended-alternation} Qual comando ativa a sintaxe de regex estendida para o padrão `^(cat|dog)s?$`?

::option[`grep -F '^(cat|dog)s?$' animals.txt`]{#regex-fixed-animals explanation="`-F` trata todos os operadores de regex como texto literal; assim, agrupamento, alternância e repetição opcional são desativados."}
::option[`grep -E '^(cat|dog)s?$' animals.txt`]{#regex-extended-animals .correct explanation="`-E` seleciona expressões regulares estendidas e ativa o agrupamento, a alternância e o `s` opcional mostrados."}
::option[`grep '^(cat|dog)s?$' animals.txt`]{#regex-basic-animals explanation="O grep padrão usa BRE, em que esses caracteres de agrupamento e alternância sem escape não possuem os significados ERE pretendidos."}
:::

Para praticar a seleção com regex nas ferramentas de texto do Linux, experimente estes laboratórios:

1. **[Pesquisa de Texto com grep no Linux](https://labex.io/labs/comptia-search-text-with-grep-in-linux-590841)** — Neste laboratório, você aprenderá a pesquisar textos em arquivos de um sistema Linux com o comando `grep`. Você realizará pesquisas básicas, exibirá números de linha, usará âncoras como `^` e `$` para corresponder a posições nas linhas e aplicará expressões regulares básicas e estendidas para correspondências complexas de padrões.
2. **[Processamento de Texto e Expressões Regulares](https://labex.io/labs/linux-text-processing-and-regular-expressions-18003)** — Aprenda ferramentas como `grep`, `sed` e `awk` e use expressões regulares para manipular e corresponder textos.
3. **[Extração de E-mails e Números](https://labex.io/labs/linux-extracting-mails-and-numbers-17991)** — Neste desafio, você aprenderá a usar `grep` e expressões regulares para extrair endereços de e-mail e números de um arquivo, demonstrando habilidades essenciais de processamento de texto no Linux.

## Resumo

Agora você sabe ler e criar expressões regulares fundamentais orientadas por linhas.

1. Diferencie operadores regex de curingas de caminhos do shell.
2. Ancore correspondências no início ou no final de uma linha.
3. Corresponda a um caractere com ponto ou expressão entre colchetes.
4. Negue conjuntos e use classes de caracteres dependentes do locale.
5. Escolha conscientemente a sintaxe BRE ou ERE.
