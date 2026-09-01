---
lesson_id: "vim-editing"
course_id: "advanced-text-fu"
lang: "pt"
order_index: 7
title: "Edição no Vim"
description: "Aprenda como o Vim combina operadores, movimentos, registros, inserções e comandos de desfazer na edição de texto."
meta_title: "Edição no Vim - Text-Fu Avançado"
meta_description: "Aprenda comandos essenciais de edição no Vim para excluir, alterar, copiar, colar, desfazer e refazer texto com eficiência."
meta_keywords: "edição Vim, comandos Vim, editor texto Linux, tutorial Vim, guia Vim, Vim para iniciantes, comando dd, excluir Vim"
---

Os comandos de edição do Vim frequentemente combinam um operador com um movimento ou objeto de texto. Essa gramática permite aplicar as mesmas ações a caracteres, palavras, linhas e escopos maiores. Pressione `Esc` antes de praticar para retornar ao modo Normal.

## Combinação de um Operador com um Movimento

A forma geral é:

```text
[count] operator [count] motion
```

Alguns operadores comuns são:

- `d`: exclui texto.
- `c`: altera o texto e entra no modo de Inserção.
- `y`: copia, ou “yank”, o texto.

Por exemplo, `dw` exclui pelo movimento `w`, enquanto `d$` exclui do cursor até o final da linha. `2dw` aplica a exclusão ao longo de dois movimentos por palavras.

:::single-choice{#vim-edit-operator-motion} No modo Normal, o que `d$` faz?

::option[Exclui o arquivo inteiro a partir do cursor.]{#vim-edit-delete-file-end explanation="O movimento cifrão indica o final da linha atual, não o final de todo o buffer."}
::option[Exclui do cursor até o final da linha.]{#vim-edit-delete-line-end .correct explanation="O operador `d` se aplica ao movimento `$` para o final da linha."}
::option[Move-se ao final da linha sem alterar o texto.]{#vim-edit-move-line-end explanation="`$` sozinho é um movimento, mas o `d` anterior transforma o intervalo coberto em uma exclusão."}
:::

## Edição de Caracteres e Linhas

Alguns comandos são atalhos convenientes:

- `x`: exclui o caractere sob o cursor.
- `dd`: exclui a linha atual como linha inteira.
- `3dd`: exclui três linhas a partir da atual.
- `cc`: altera a linha atual e entra no modo de Inserção.
- `r{char}`: substitui o caractere sob o cursor por `{char}`.
- `R`: entra no modo de Substituição até que `Esc` seja pressionado.

Repetir um operador, como em `dd`, torna a ação orientada por linha. Uma quantidade amplia o número de linhas.

:::single-choice{#vim-edit-delete-three-lines} Qual comando do modo Normal exclui a linha atual e as duas linhas seguintes?

::option[`dd3`]{#vim-edit-dd-three explanation="Nessa forma, a quantidade deve vir antes do operador repetido."}
::option[`3x`]{#vim-edit-three-x explanation="Essa forma exclui três caracteres sob e depois do cursor, não três linhas completas."}
::option[`3dd`]{#vim-edit-three-dd .correct explanation="A quantidade se aplica ao comando por linha `dd` e exclui três linhas começando na atual."}
:::

## Alteração de Texto e Entrada no Modo de Inserção

O operador `c` remove o texto selecionado e entra no modo de Inserção para que você digite a substituição:

- `ce`: altera até o final da palavra.
- `c$`: altera até o final da linha.
- `cc`: altera toda a linha atual.
- `ciw`: altera a palavra interna sob o cursor.
- `caw`: altera um objeto de palavra, incluindo os espaços ao redor conforme a definição do Vim.

O comportamento de `cw` possui um caso especial histórico e frequentemente age como `ce`. Objetos de texto como `iw` podem deixar o limite pretendido mais claro.

:::single-choice{#vim-edit-change-inner-word} Qual comando do modo Normal substitui a palavra interna sob o cursor, excluindo-a e entrando no modo de Inserção?

::option[`diw`]{#vim-edit-delete-inner-word explanation="Essa forma exclui a palavra interna, mas permanece no modo Normal em vez de iniciar o texto de substituição."}
::option[`yiw`]{#vim-edit-yank-inner-word explanation="Essa forma copia a palavra interna sem alterar o buffer nem entrar no modo de Inserção."}
::option[`ciw`]{#vim-edit-change-inner-word-answer .correct explanation="O operador `c` altera o objeto de texto `iw` e depois entra no modo de Inserção."}
:::

## Cópia e Inserção de Texto

O Vim chama a cópia de **yank** e a colagem de **put**:

- `yw`: copia ao longo de um movimento por palavra.
- `yy`: copia a linha atual.
- `p`: insere depois do cursor para texto por caracteres ou abaixo da linha atual para texto por linhas.
- `P`: insere antes do cursor ou acima da linha atual.

Exclusões e alterações também armazenam texto em registros; por isso, um `p` posterior pode inserir o texto excluído mais recentemente, não uma cópia anterior. Registros nomeados permitem preservar textos específicos, mas comece observando o que a última operação armazenou.

:::single-choice{#vim-edit-yank-put-line} Depois que `yy` copia a linha atual, qual comando insere essa linha abaixo da atual?

::option[`p`]{#vim-edit-put-below .correct explanation="Para texto copiado como linha, `p` minúsculo insere a linha armazenada abaixo da atual."}
::option[`P`]{#vim-edit-put-above explanation="`P` maiúsculo insere o texto por linha acima da linha atual."}
::option[`u`]{#vim-edit-undo-not-put explanation="`u` minúsculo desfaz uma alteração; ele não insere a linha copiada."}
:::

## Desfazer, Refazer e Repetir

No modo Normal:

- `u`: desfaz a alteração mais recente.
- `Ctrl+R`: refaz uma alteração desfeita.
- `.`: repete a alteração mais recente no local atual quando aplicável.
- `J`: une a linha atual à seguinte.

O histórico de desfazer se aplica a alterações no buffer, não apenas a movimentos do cursor. Salve pontos de controle e examine as edições em vez de depender de um histórico ilimitado ou permanente.

:::single-choice{#vim-edit-redo-change} Qual comando do modo Normal refaz uma alteração que acabou de ser desfeita?

::option[`Ctrl+U`]{#vim-edit-control-u explanation="No modo Normal, `Ctrl+U` rola para cima aproximadamente meia tela; ele não refaz."}
::option[`.`]{#vim-edit-dot-repeat explanation="O ponto repete a última alteração como uma nova ação, em vez de avançar pelo histórico de desfazer."}
::option[`Ctrl+R`]{#vim-edit-control-r .correct explanation="O Vim usa `Ctrl+R` no modo Normal para avançar pelo histórico de desfazer."}
:::

Para praticar operadores, movimentos e recuperação em textos descartáveis, experimente este laboratório:

1. **[Edição de Arquivos de Texto no Linux com Vim e Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** — Pratique a criação de arquivos, a edição de texto, o salvamento de arquivos e a navegação tanto com vi/vim quanto com nano. Este laboratório ajudará você a aplicar em situações reais conceitos como excluir, alterar, copiar e inserir texto.

## Resumo

Agora você sabe compor edições no Vim e se recuperar de erros no modo Normal.

1. Combine operadores com movimentos, objetos de texto e quantidades.
2. Exclua caracteres ou linhas completas no escopo escolhido.
3. Altere o texto e entre no modo de Inserção para substituí-lo.
4. Copie e insira texto por caracteres ou linhas.
5. Desfaça, refaça ou repita alterações conscientemente.
