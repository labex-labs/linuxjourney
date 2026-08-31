---
lesson_id: "vim-search-patterns"
course_id: "advanced-text-fu"
lang: "pt"
order_index: 4
title: "Padrões de Pesquisa no Vim"
description: "Aprenda a pesquisar para a frente ou para trás no Vim e repetir, refinar ou limpar correspondências."
meta_title: "Padrões de Pesquisa no Vim - Text-Fu Avançado"
meta_description: "Aprenda a pesquisar para a frente e para trás no Vim usando padrões e a navegar pelos resultados com n e N."
meta_keywords: "pesquisa Vim, busca Vim, comandos Vim, editor texto Linux, tutorial Vim, guia Vim, padrões pesquisa"
---

O Vim pesquisa padrões a partir da posição atual do cursor. Comece no modo Normal, inicie uma pesquisa para a frente ou para trás e depois repita as correspondências sem redigitar o padrão.

## Pesquisa para a Frente

No modo Normal, digite `/`, insira um padrão e pressione Enter. O Vim avança para a próxima correspondência depois do cursor:

```vim
/pretty
```

As pesquisas usam a sintaxe de expressões regulares do Vim; portanto, caracteres como `.`, `*`, `[` e `\` podem ter significados especiais. Use `\V` no início quando o restante do padrão deva ser tratado como “very nomagic”, ou escape os caracteres especiais conscientemente.

:::single-choice{#vim-search-forward-key}
Partindo do modo Normal, qual comando inicia uma pesquisa para a frente por `pretty`?

::option[`?pretty`, seguido de Enter]{#vim-backward-pretty explanation="Um ponto de interrogação inicia uma pesquisa para trás a partir da posição atual do cursor."}
::option[`/pretty`, seguido de Enter]{#vim-forward-pretty .correct explanation="Uma barra inicia uma pesquisa para a frente, e Enter envia o padrão."}
::option[`:pretty`, seguido de Enter]{#vim-command-pretty explanation="Dois-pontos entram no modo de Linha de Comando para um comando Ex; `pretty` não é introduzido como pesquisa dessa forma."}
:::

## Pesquisa para Trás

Digite `?`, insira um padrão e pressione Enter para ir à correspondência anterior ao cursor:

```vim
?pretty
```

Isso não significa necessariamente “a última correspondência do arquivo”. O resultado depende da posição atual do cursor. Com a configuração padrão `wrapscan` do Vim, uma pesquisa pode recomeçar no início ou no final; `:set nowrapscan` desativa essa continuidade.

:::single-choice{#vim-search-backward-key}
Qual prefixo de pesquisa do modo Normal procura o texto anterior ao cursor?

::option[`/`]{#vim-slash-forward explanation="Uma barra pesquisa para a frente a partir do cursor, não em direção ao texto anterior."}
::option[`?`]{#vim-question-backward .correct explanation="Um ponto de interrogação inicia uma pesquisa de padrão para trás a partir da posição atual."}
::option[`:`]{#vim-colon-command explanation="Dois-pontos iniciam uma linha de comando Ex. Eles não são o prefixo de pesquisa para trás."}
:::

## Repetição de uma Pesquisa

Depois de qualquer tipo de pesquisa:

- Pressione `n` para repetir na direção original.
- Pressione `N` para repetir na direção oposta.

Portanto, depois de `/pretty`, `n` avança e `N` recua. Depois de `?pretty`, `n` recua e `N` avança.

:::single-choice{#vim-repeat-backward-search}
Depois de executar `?error`, qual tecla repete a pesquisa na mesma direção para trás?

::option[`n`]{#vim-same-question-search .correct explanation="`n` minúsculo repete a pesquisa mais recente em sua direção original, que neste caso é para trás."}
::option[`N`]{#vim-opposite-question-search explanation="`N` maiúsculo inverte a direção original; portanto, avançaria depois de uma pesquisa com `?`."}
::option[`/`]{#vim-new-forward-search explanation="Uma barra inicia uma nova pesquisa para a frente e aguarda um padrão, em vez de repetir a anterior."}
:::

## Pesquisa da Palavra sob o Cursor

No modo Normal, coloque o cursor sobre uma palavra e use:

- `*` para pesquisá-la inteira para a frente;
- `#` para pesquisá-la inteira para trás.

Esses comandos definem o padrão de pesquisa mais recente; assim, `n` e `N` podem continuar a partir dele.

:::single-choice{#vim-current-word-forward}
Qual tecla do modo Normal pesquisa para a frente a palavra inteira sob o cursor?

::option[`#`]{#vim-hash-current-word explanation="A tecla cerquilha pesquisa para trás a palavra sob o cursor."}
::option[`*`]{#vim-star-current-word .correct explanation="O comando asterisco cria um padrão de palavra inteira a partir da palavra sob o cursor e pesquisa para a frente."}
::option[`n`]{#vim-repeat-current-pattern explanation="A tecla `n` repete uma pesquisa existente; ela não cria primeiro um padrão com a palavra atual."}
:::

## Controle de Maiúsculas e do Destaque

Opções do Vim podem mudar o comportamento de maiúsculas e minúsculas:

- `:set ignorecase` faz as pesquisas ignorarem a diferença;
- `:set smartcase` restaura a sensibilidade quando o padrão contém uma letra maiúscula e `ignorecase` também está ativo;
- `\c` dentro de um padrão força essa pesquisa a ignorar a diferença;
- `\C` força essa pesquisa a respeitá-la.

Por exemplo, `/\cerror` corresponde a `error`, `Error` e `ERROR`, independentemente das opções atuais.

Quando o destaque das pesquisas está ativo, `:nohlsearch` limpa os destaques visuais atuais sem excluir o padrão. A próxima pesquisa ou repetição poderá destacá-los novamente.

:::single-choice{#vim-force-case-insensitive}
Qual padrão força uma pesquisa do Vim por `error` a ignorar maiúsculas e minúsculas, independentemente das opções atuais?

::option[`/\Cerror`]{#vim-pattern-match-case explanation="`\C` maiúsculo força a correspondência sensível, o comportamento oposto."}
::option[`/:error`]{#vim-pattern-colon-error explanation="Os dois-pontos dentro desse padrão são um caractere literal e não selecionam o tratamento de maiúsculas."}
::option[`/\cerror`]{#vim-pattern-ignore-case .correct explanation="O átomo `\c` torna a pesquisa insensível, permitindo a correspondência de variantes de capitalização."}
:::

Para praticar a navegação e a pesquisa do Vim em um arquivo controlado, experimente este laboratório:

1. **[Edição de Arquivos de Texto no Linux com Vim e Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** — Pratique a criação, edição, gravação, navegação e pesquisa de arquivos com Vim e Nano.

## Resumo

Agora você sabe pesquisar um buffer do Vim e se mover previsivelmente entre as correspondências.

1. Inicie pesquisas para a frente com `/` e para trás com `?`.
2. Repita na mesma direção com `n` ou na direção oposta com `N`.
3. Pesquise a palavra inteira sob o cursor com `*` ou `#`.
4. Controle maiúsculas e minúsculas em um padrão ou pelas opções.
5. Limpe os destaques sem perder o padrão de pesquisa atual.
