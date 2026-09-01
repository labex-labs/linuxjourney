---
lesson_id: "vim-navigation"
course_id: "advanced-text-fu"
lang: "pt"
order_index: 5
title: "Navegação no Vim"
description: "Aprenda a se mover por caracteres, palavras, linhas e posições do arquivo no modo Normal do Vim."
meta_title: "Navegação no Vim - Text-Fu Avançado"
meta_description: "Aprenda os fundamentos da navegação no Vim com as teclas h, j, k e l e movimentos por palavras, linhas e posições do arquivo."
meta_keywords: "navegação Vim, tutorial Vim, Vim Linux, movimentos Vim, fundamentos Vim, Vim para iniciantes, editor texto Linux"
---

O Vim oferece movimentos pelo teclado que funcionam em um terminal sem exigir um mouse. Algumas configurações também aceitam a entrada do mouse, mas aprender os movimentos torna a navegação combinável com comandos de edição.

Pressione `Esc` antes de praticar para retornar ao modo Normal.

## Movimento por Caracteres e Linhas da Tela

Os movimentos fundamentais do modo Normal são:

- `h`: move um caractere para a esquerda.
- `j`: move uma linha para baixo.
- `k`: move uma linha para cima.
- `l`: move um caractere para a direita.

As teclas de seta normalmente realizam movimentos semelhantes, mas `h`, `j`, `k` e `l` mantêm suas mãos próximas dos outros comandos. Em uma linha visual quebrada, `j` e `k` normalmente se movem pelas linhas do arquivo; `gj` e `gk` se movem pelas linhas exibidas na tela.

:::single-choice{#vim-navigation-down} No modo Normal, qual tecla move o cursor uma linha para baixo?

::option[`k`]{#vim-nav-k-up explanation="O movimento `k` sobe uma linha."}
::option[`l`]{#vim-nav-l-right explanation="O movimento `l` avança um caractere para a direita."}
::option[`j`]{#vim-nav-j-down .correct explanation="O movimento `j` desce uma linha no modo Normal."}
:::

## Prefixo Numérico nos Movimentos

Digite uma quantidade positiva antes de muitos movimentos para repeti-los. Por exemplo:

```text
5j
3l
```

`5j` desce cinco linhas, enquanto `3l` avança três posições de caracteres para a direita quando possível. As quantidades também se combinam com palavras e comandos de edição.

:::single-choice{#vim-navigation-count} O que `4k` faz no modo Normal?

::option[Desce quatro linhas quando possível.]{#vim-nav-four-down explanation="O movimento para baixo usa `j`; `k` segue na direção oposta."}
::option[Sobe quatro linhas quando possível.]{#vim-nav-four-up .correct explanation="A quantidade `4` repete quatro vezes o movimento `k` para cima."}
::option[Exclui quatro linhas acima do cursor.]{#vim-nav-delete-four explanation="Um movimento por si só muda a posição do cursor. A exclusão exigiria um operador como `d`."}
:::

## Movimento por Palavras

Alguns movimentos úteis por palavras são:

- `w`: vai ao início da próxima palavra.
- `b`: vai ao início da palavra atual ou anterior.
- `e`: vai ao final da palavra atual ou seguinte.

`W`, `B` e `E` maiúsculos usam WORDS delimitadas por espaços em branco e tratam a pontuação de forma diferente. Use uma quantidade para percorrer várias palavras, como `3w`.

:::single-choice{#vim-navigation-next-words} Qual comando do modo Normal avança até o início da terceira posição de palavra seguinte?

::option[`3w`]{#vim-nav-three-words .correct explanation="A quantidade aplica três vezes o movimento para a palavra seguinte."}
::option[`w3`]{#vim-nav-word-three explanation="Nessa forma, as quantidades precedem os movimentos; colocar `3` depois não expressa o deslocamento solicitado."}
::option[`3b`]{#vim-nav-three-back explanation="O movimento `b` segue em direção ao início de palavras anteriores, não para a frente."}
:::

## Movimento Dentro de uma Linha

Estes movimentos indicam posições da linha atual:

- `0`: vai à coluna zero.
- `^`: vai ao primeiro caractere não vazio.
- `$`: vai ao final da linha.

A diferença entre `0` e `^` importa em linhas com recuo.

:::single-choice{#vim-navigation-first-nonblank} Qual movimento vai ao primeiro caractere não vazio de uma linha recuada?

::option[`0`]{#vim-nav-column-zero explanation="Zero vai à primeira coluna, que pode conter espaços de recuo."}
::option[`$`]{#vim-nav-line-end explanation="O movimento cifrão indica o final da linha."}
::option[`^`]{#vim-nav-first-nonblank .correct explanation="O movimento circunflexo ignora os espaços iniciais e chega ao primeiro caractere não vazio."}
:::

## Movimento pelo Arquivo

Use estes comandos do modo Normal para saltos maiores:

- `gg`: vai à primeira linha.
- `G`: vai à última linha.
- `42G`: vai à linha 42.
- `Ctrl+F`: avança aproximadamente uma tela.
- `Ctrl+B`: recua aproximadamente uma tela.

O comando `:42`, seguido de Enter, é outra forma de ir à linha 42.

:::single-choice{#vim-navigation-file-end} Qual comando do modo Normal vai à última linha do buffer?

::option[`gg`]{#vim-nav-first-line explanation="`gg` minúsculo vai à primeira linha, não à última."}
::option[`$`]{#vim-nav-current-line-end explanation="O movimento cifrão vai ao final da linha atual, não ao final do arquivo."}
::option[`G`]{#vim-nav-last-line .correct explanation="`G` maiúsculo sem uma quantidade salta para a última linha."}
:::

Para praticar a navegação pelo teclado enquanto edita um arquivo descartável, experimente este laboratório:

1. **[Edição de Arquivos de Texto no Linux com Vim e Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** — Pratique a criação, edição, gravação e navegação de arquivos com Vim e Nano em um ambiente Linux real.

## Resumo

Agora você sabe percorrer um buffer do Vim em várias escalas úteis.

1. Mova-se por caracteres ou linhas com `h`, `j`, `k` e `l`.
2. Repita movimentos com um prefixo numérico.
3. Percorra limites de palavras com `w`, `b` e `e`.
4. Vá ao início, ao primeiro texto ou ao final de uma linha.
5. Salte para posições do arquivo com `gg`, `G` ou um número de linha.
