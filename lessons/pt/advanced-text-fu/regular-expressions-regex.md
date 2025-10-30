---
index: 1
lang: "pt"
title: "regex (Expressões Regulares)"
meta_title: "regex (Expressões Regulares) - Domínio Avançado de Texto"
meta_description: "Domine o básico do Linux com nosso guia sobre expressões regulares (regex). Aprenda correspondência de padrões com grep, usando sintaxes como ^, $, e []. Esta é uma das melhores formas de aprender manipulação de texto no Linux e avançar suas habilidades."
meta_keywords: "expressão regular linux, regex, fundamentos do linux, correspondência de padrões, grep, processamento de texto, aprender linux, tutorial linux, caminho mais rápido para o linux avançado"
---

## Lesson Content

Expressões regulares, frequentemente abreviadas como regex, são uma ferramenta poderosa para seleção de texto baseada em padrões. Entendê-las é fundamental para dominar a manipulação de texto no Linux. Embora existam muitos aplicativos para aprender Linux, mergulhar em conceitos centrais como `regular expression linux` é o caminho mais rápido para a proficiência avançada em Linux. Elas usam notações especiais, algumas das quais são semelhantes a curingas como `*`.

Vamos explorar alguns dos operadores de regex mais comuns, que são quase universais em linguagens de programação. Usaremos o seguinte texto como nosso exemplo:

```plaintext
sally sells seashells
by the seashore
```

### Ancoragem ao Início de uma Linha

O símbolo circunflexo `^` corresponde ao início de uma linha. Ele garante que seu padrão apareça apenas no começo.

```plaintext
^by
```

Este padrão corresponderia à linha "by the seashore", mas não a "sally sells seashells".

### Ancoragem ao Fim de uma Linha

O símbolo cifrão `$` corresponde ao fim de uma linha. É o equivalente à âncora `^`.

```plaintext
seashore$
```

Este padrão corresponderia à linha "by the seashore", porque ela termina com "seashore".

### Correspondência de Qualquer Caractere Único

O ponto `.` é um curinga que corresponde a qualquer caractere único.

```plaintext
b.
```

Em nosso exemplo, isso corresponderia a "by".

### Usando Colchetes para Conjuntos de Caracteres

Colchetes `[]` permitem que você especifique um conjunto de caracteres a serem correspondidos. Isso oferece mais controle do que o curinga `.`.

```plaintext
s[ae]lls
```

Isso corresponderia a "sells" e também corresponderia a "salls".

You can also use brackets to specify what _not_ to match. When the caret `^` is the first character inside brackets, it negates the set, matching any character _except_ those listed.

```plaintext
s[^e]lls
```

Isso corresponderia a "salls", mas não a "sells".

Finalmente, os colchetes suportam intervalos para definir um grande conjunto de caracteres de forma eficiente.

```plaintext
d[a-c]g
```

Este padrão corresponderá a "dag", "dbg" e "dcg". Esteja ciente de que os intervalos diferenciam maiúsculas de minúsculas. Por exemplo, `[a-c]` não corresponderá a `A`, `B` ou `C`.

Aprender esses operadores é uma das melhores maneiras de aprender a eficiência da linha de comando do Linux.

## Exercise

Coloque seu conhecimento em prática. Aqui estão alguns laboratórios práticos para reforçar sua compreensão de expressões regulares e correspondência de padrões:

1.  **[Pesquisar Texto com grep no Linux](https://labex.io/pt/labs/comptia-search-text-with-grep-in-linux-590841)** - Neste laboratório, você aprenderá a pesquisar texto em arquivos em um sistema Linux usando o comando `grep`. Você realizará pesquisas básicas, exibirá números de linha, usará âncoras como `^` e `$` para corresponder a posições de linha e utilizará expressões regulares básicas e estendidas para correspondência de padrões complexos.
2.  **[Processamento de Texto e Expressões Regulares](https://labex.io/pt/labs/linux-text-processing-and-regular-expressions-18003)** - Aprenda as poderosas ferramentas de processamento de texto grep, sed e awk. Aprenda a usar expressões regulares para manipulação eficiente de texto e correspondência de padrões no Linux.
3.  **[Extraindo E-mails e Números](https://labex.io/pt/labs/linux-extracting-mails-and-numbers-17991)** - Neste desafio, você aprenderá a usar grep e expressões regulares para extrair endereços de e-mail e números de um arquivo, demonstrando habilidades essenciais de processamento de texto no Linux.

Estes laboratórios ajudarão você a aplicar os conceitos em cenários reais e a construir confiança com expressões regulares e processamento de texto.

## Quiz Question

Qual expressão regular você usaria para corresponder a qualquer caractere único?

## Quiz Answer

.
