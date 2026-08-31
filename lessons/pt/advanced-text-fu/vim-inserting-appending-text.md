---
lesson_id: "vim-inserting-appending-text"
course_id: "advanced-text-fu"
lang: "pt"
order_index: 6
title: "Inserção e Acréscimo de Texto no Vim"
description: "Aprenda como o Vim entra no modo de Inserção antes, depois, acima ou abaixo da posição atual do cursor."
meta_title: "Inserção e Acréscimo de Texto no Vim - Text-Fu Avançado"
meta_description: "Aprenda a diferença entre inserir e acrescentar no Vim. Domine comandos como i, a, I, A, o e O para editar texto com eficiência."
meta_keywords: "acrescentar Vim, inserir vs acrescentar Vim, adicionar linha Vim, edição texto Vim, comandos Vim, tutorial Vim, modo inserção"
---

No modo Normal, o Vim interpreta as teclas como comandos. O modo de Inserção insere o texto digitado no buffer. Vários comandos do modo Normal entram no modo de Inserção em posições diferentes, permitindo começar a digitar sem uma navegação separada.

Pressione `Esc` para sair do modo de Inserção e retornar ao modo Normal. Se não souber qual modo está ativo, pressionar `Esc` é uma forma segura de restabelecer o modo Normal, embora possa cancelar uma operação pendente.

:::single-choice{#vim-insert-return-normal}
Qual tecla normalmente retorna do modo de Inserção ao modo Normal?

::option[`Esc`]{#vim-insert-escape .correct explanation="Escape encerra a inserção atual e retorna o Vim ao modo Normal."}
::option[`Enter`]{#vim-insert-enter explanation="Enter insere uma quebra de linha e permanece no modo de Inserção."}
::option[`Tab`]{#vim-insert-tab explanation="Tab insere um recuo ou ativa um comportamento configurado de conclusão; normalmente, não sai do modo de Inserção."}
:::

## Inserção Antes ou Depois do Cursor

A partir do modo Normal:

- `i`: entra no modo de Inserção antes do cursor.
- `a`: entra no modo de Inserção depois do cursor.

Por exemplo, se o cursor estiver sobre `b` em `abc`, `i` começa antes de `b`, enquanto `a` começa depois. Os dois comandos mudam de modo; o texto digitado em seguida realiza a inserção.

:::single-choice{#vim-insert-before-cursor}
Qual tecla do modo Normal entra no modo de Inserção imediatamente antes do cursor?

::option[`a`]{#vim-insert-a-after explanation="`a` minúsculo acrescenta depois do cursor, em vez de inserir antes dele."}
::option[`o`]{#vim-insert-o-below explanation="`o` minúsculo abre uma nova linha abaixo da atual antes de entrar no modo de Inserção."}
::option[`i`]{#vim-insert-i-before .correct explanation="`i` minúsculo começa a inserção na posição atual, antes do caractere sob o cursor."}
:::

## Inserção nos Limites da Linha

Comandos em maiúsculas indicam posições significativas da linha atual:

- `I`: entra no modo de Inserção antes do primeiro caractere não vazio.
- `A`: entra no modo de Inserção no final da linha.

Em uma linha recuada, `I` ignora o recuo e começa antes do primeiro texto não vazio. Use `0i` se precisar especificamente inserir na coluna zero.

:::single-choice{#vim-insert-first-nonblank}
Qual comando do modo Normal começa a inserção antes do primeiro caractere não vazio da linha atual?

::option[`i`]{#vim-insert-lower-i explanation="`i` minúsculo usa a posição atual do cursor e não vai primeiro ao texto inicial da linha."}
::option[`A`]{#vim-insert-capital-a explanation="`A` maiúsculo começa a inserção no final da linha atual."}
::option[`I`]{#vim-insert-capital-i .correct explanation="`I` maiúsculo vai ao primeiro caractere não vazio e entra no modo de Inserção antes dele."}
:::

:::single-choice{#vim-append-line-end}
Qual comando do modo Normal vai ao final da linha atual e entra no modo de Inserção?

::option[`A`]{#vim-append-capital-a .correct explanation="`A` maiúsculo combina um salto ao final da linha com a entrada no modo de Inserção."}
::option[`$`]{#vim-move-line-end explanation="O movimento cifrão chega ao final da linha, mas permanece no modo Normal."}
::option[`a`]{#vim-append-one-position explanation="`a` minúsculo começa depois do cursor atual, em vez de saltar ao final da linha."}
:::

## Abertura de uma Nova Linha

A partir do modo Normal:

- `o`: abre uma nova linha abaixo da atual e entra no modo de Inserção.
- `O`: abre uma nova linha acima da atual e entra no modo de Inserção.

O Vim aplica o recuo conforme as configurações atuais e as regras do tipo de arquivo. Uma quantidade pode repetir a operação de abertura, mas primeiro aprenda a forma de uma única linha para que a posição resultante do cursor seja previsível.

:::single-choice{#vim-open-line-above}
Qual comando do modo Normal abre uma nova linha acima da atual e entra no modo de Inserção?

::option[`o`]{#vim-open-lower-o explanation="`o` minúsculo abre abaixo da linha atual."}
::option[`O`]{#vim-open-upper-o .correct explanation="`O` maiúsculo abre uma nova linha acima e inicia a inserção nela."}
::option[`A`]{#vim-open-upper-a explanation="`A` maiúsculo acrescenta no final da linha existente e não abre uma nova linha acima."}
:::

Para praticar a alternância entre os modos Normal e de Inserção, experimente este laboratório:

1. **[Edição de Arquivos de Texto no Linux com Vim e Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** — Pratique a criação, edição, gravação e navegação de arquivos com vi/vim e nano e domine os fundamentos dos modos Normal e de Inserção.

## Resumo

Agora você sabe entrar no modo de Inserção na posição em que o novo texto deve ficar.

1. Retorne ao modo Normal com `Esc`.
2. Insira antes ou depois do cursor com `i` ou `a`.
3. Insira no primeiro texto ou no final da linha com `I` ou `A`.
4. Abra uma linha abaixo com `o`.
5. Abra uma linha acima com `O`.
