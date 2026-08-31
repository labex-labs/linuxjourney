---
lesson_id: "emacs-buffer-navigation"
course_id: "advanced-text-fu"
lang: "pt"
order_index: 11
title: "Navegação por Buffers no Emacs"
description: "Aprenda a alternar e encerrar buffers do Emacs enquanto divide, seleciona e fecha janelas de exibição."
meta_title: "Navegação por Buffers no Emacs - Text-Fu Avançado"
meta_description: "Aprenda a alternar buffers, dividir e selecionar janelas e gerenciar seu fluxo de trabalho com comandos essenciais do Emacs."
meta_keywords: "navegação Emacs, alternar buffer Emacs, gerenciamento buffers Emacs, comandos Emacs, C-x b, C-x k, C-x 2, editor texto"
---

Um buffer do Emacs mantém texto ou estado do editor, enquanto uma janela exibe um buffer. Um buffer pode existir sem estar visível, e várias janelas podem exibir o mesmo buffer. Gerenciar um desses objetos não gerencia automaticamente o outro.

## Alternância entre Buffers

Use `C-x b`, que executa `switch-to-buffer`, para selecionar pelo nome um buffer na janela atual:

```text
C-x b
```

O minibuffer oferece conclusão para os nomes existentes. Inserir um novo nome pode criar um buffer sem arquivo com esse nome; isso não visita um caminho de arquivo.

Por padrão, `C-x Right` executa `next-buffer`, e `C-x Left` executa `previous-buffer`, percorrendo os buffers na janela selecionada.

:::single-choice{#emacs-switch-buffer-key}
Qual sequência de teclas solicita um nome de buffer para exibi-lo na janela atual?

::option[`C-x C-f`]{#emacs-buffer-find-file explanation="Essa sequência solicita um caminho e o visita, uma operação diferente de escolher pelo nome um buffer existente."}
::option[`C-x b`]{#emacs-switch-buffer .correct explanation="`switch-to-buffer` lê um nome e exibe esse buffer na janela selecionada."}
::option[`C-x k`]{#emacs-buffer-kill explanation="Essa sequência solicita o encerramento de um buffer, em vez de mudar a janela selecionada para ele."}
:::

## Divisão da Janela Selecionada

Use `C-x 2` para dividir a janela selecionada em uma janela superior e outra inferior:

```text
C-x 2
```

Use `C-x 3` para dividi-la em janelas à esquerda e à direita:

```text
C-x 3
```

A nova janela inicialmente exibe um buffer, muitas vezes o mesmo. Você pode alternar os buffers de cada janela independentemente.

:::single-choice{#emacs-split-side-by-side}
Qual sequência de teclas divide a janela selecionada do Emacs em janelas à esquerda e à direita?

::option[`C-x 1`]{#emacs-window-one explanation="Essa sequência exclui as outras janelas e torna a selecionada a única de seu frame."}
::option[`C-x 2`]{#emacs-window-below explanation="Essa sequência cria janelas superior e inferior, não uma divisão lado a lado."}
::option[`C-x 3`]{#emacs-window-right .correct explanation="`split-window-right`, associado a `C-x 3`, cria janelas à esquerda e à direita."}
:::

## Seleção e Fechamento de Janelas

Use `C-x o`, que executa `other-window`, para selecionar a próxima janela:

```text
C-x o
```

Use estes comandos para remover exibições:

- `C-x 0`: exclui a janela selecionada.
- `C-x 1`: exclui as outras janelas do frame atual.

Excluir uma janela normalmente mantém vivo o buffer exibido nela. Você pode mostrar esse buffer novamente em outra janela.

:::single-choice{#emacs-select-other-window}
Qual sequência de teclas move o ponto e o foco do teclado para outra janela do Emacs?

::option[`C-x 0`]{#emacs-delete-selected-window explanation="Essa sequência exclui a janela selecionada, em vez de mover o foco para outra."}
::option[`C-x o`]{#emacs-other-window .correct explanation="`other-window` alterna a seleção para outra janela do frame."}
::option[`C-x b`]{#emacs-switch-in-window explanation="Essa sequência muda o buffer exibido pela janela atual, não a janela selecionada."}
:::

:::single-choice{#emacs-keep-one-window}
Qual sequência de teclas preserva a janela selecionada e exclui as outras janelas de seu frame?

::option[`C-x 1`]{#emacs-delete-other-windows .correct explanation="`delete-other-windows` torna a janela selecionada a única do frame."}
::option[`C-x 0`]{#emacs-delete-current-window explanation="Essa sequência exclui a própria janela selecionada, em vez de preservá-la."}
::option[`C-x 2`]{#emacs-add-lower-window explanation="Essa sequência acrescenta outra janela em vez de reduzir o frame a uma."}
:::

## Encerramento de um Buffer

Use `C-x k`, que executa `kill-buffer`, para solicitar um buffer a remover do Emacs:

```text
C-x k
```

O buffer atual é a escolha padrão. Se um buffer associado a um arquivo possuir alterações não salvas, o Emacs avisará antes de encerrá-lo. Leia a pergunta: encerrar um buffer modificado pode descartar edições.

Encerrar um buffer é diferente de excluir uma janela. O Emacs substitui um buffer encerrado em qualquer janela que o exiba, enquanto excluir uma janela pode manter o buffer intacto.

:::single-choice{#emacs-kill-buffer-key}
Qual sequência de teclas solicita o encerramento de um buffer do Emacs?

::option[`C-x 0`]{#emacs-kill-window-only explanation="Essa sequência exclui uma janela de exibição, mas normalmente mantém o buffer vivo."}
::option[`C-x k`]{#emacs-kill-buffer-answer .correct explanation="`kill-buffer` remove o buffer selecionado do Emacs depois de qualquer confirmação necessária sobre modificações."}
::option[`C-x b`]{#emacs-kill-switch explanation="Essa sequência muda a janela atual para um buffer nomeado e não o encerra."}
:::

Pratique esses comandos com `*scratch*` e buffers descartáveis. Antes de encerrar qualquer buffer associado a um arquivo, confirme se o indicador de modificação mostra trabalho não salvo.

## Resumo

Agora você sabe gerenciar o que o Emacs armazena e o que cada janela exibe.

1. Alterne buffers na janela selecionada com `C-x b`.
2. Divida abaixo com `C-x 2` ou à direita com `C-x 3`.
3. Selecione outra janela com `C-x o`.
4. Remova exibições com `C-x 0` ou `C-x 1`.
5. Encerre um buffer com `C-x k` somente depois de revisar as alterações não salvas.
