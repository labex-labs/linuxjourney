---
lesson_id: "emacs-editing"
course_id: "advanced-text-fu"
lang: "pt"
order_index: 12
title: "Edição no Emacs"
description: "Aprenda a mover o ponto, ativar uma região e usar os comandos do kill ring do Emacs para editar texto."
meta_title: "Edição no Emacs - Text-Fu Avançado"
meta_description: "Domine os fundamentos da edição no Emacs. Aprenda comandos essenciais de navegação, seleção, recorte, cópia e colagem neste editor para Linux."
meta_keywords: "Emacs, tutorial Emacs, comandos Emacs, editor texto, editor Linux, navegação Emacs, Emacs para iniciantes"
---

O Emacs chama a posição atual do cursor de **ponto**. Comandos de movimento reposicionam o ponto; comandos de edição inserem, excluem, recortam, copiam ou colam texto ao redor dele. Na notação abaixo, `C-` significa Control e `M-` significa Meta, normalmente Alt.

## Movimento por Caracteres e Linhas

As teclas de seta e outras teclas de navegação da plataforma podem funcionar, mas os comandos de movimento padrão do Emacs permanecem disponíveis em sessões de terminal e gráficas:

- `C-f`: avança um caractere.
- `C-b`: recua um caractere.
- `C-n`: vai à próxima linha.
- `C-p`: vai à linha anterior.
- `C-a`: vai ao início da linha.
- `C-e`: vai ao final da linha.

:::single-choice{#emacs-edit-next-line} Qual tecla do Emacs move o ponto para a próxima linha?

::option[`C-p`]{#emacs-edit-previous-line explanation="`C-p` vai à linha anterior, na direção oposta."}
::option[`C-n`]{#emacs-edit-next-line-answer .correct explanation="`C-n`, de next-line, move o ponto para baixo até a posição da próxima linha na tela."}
::option[`C-f`]{#emacs-edit-forward-character explanation="`C-f` avança um caractere, não uma linha."}
:::

## Movimento por Palavras e Limites do Buffer

Comandos Meta se movem por unidades maiores:

- `M-f`: avança uma palavra.
- `M-b`: recua uma palavra.
- `M-<`: vai ao início do buffer.
- `M->`: vai ao final do buffer.

Em muitos teclados, Alt atua como Meta. Quando essa combinação não está disponível, pressionar `Esc` e depois a tecla seguinte frequentemente envia o comando Meta equivalente.

:::single-choice{#emacs-edit-buffer-end} Qual tecla do Emacs move o ponto para o final do buffer?

::option[`C-e`]{#emacs-edit-line-end explanation="`C-e` vai ao final da linha atual, não de todo o buffer."}
::option[`M-<`]{#emacs-edit-buffer-start explanation="`M-<` vai ao início do buffer."}
::option[`M->`]{#emacs-edit-buffer-end-answer .correct explanation="`M->` move o ponto para o final do buffer atual."}
:::

## Definição de uma Região

A **marca** é uma posição salva no buffer. O texto entre o ponto e a marca é a **região**. Pressione `C-SPC`, escrito como `C-space` em algumas documentações, para executar `set-mark-command`; depois, mova o ponto para ampliar a região ativa.

Em um terminal, `C-SPC` pode ser codificado como `C-@`. O destaque depende das configurações de transient-mark, mas o ponto e a marca ainda definem uma região.

:::single-choice{#emacs-edit-set-mark} Qual tecla começa a definir uma região colocando a marca no ponto?

::option[`C-w`]{#emacs-edit-kill-region-before-mark explanation="`C-w` recorta uma região já definida; ele não é o comando inicial para definir a marca."}
::option[`C-y`]{#emacs-edit-yank-before-mark explanation="`C-y` insere texto do kill ring e não inicia uma seleção."}
::option[`C-SPC`]{#emacs-edit-control-space .correct explanation="`set-mark-command` coloca a marca; depois disso, o movimento altera a região entre a marca e o ponto."}
:::

## Recorte ou Cópia de uma Região

O Emacs armazena texto recortado e copiado no **kill ring**:

- `C-w`: recorta a região ativa, removendo-a e acrescentando-a ao kill ring.
- `M-w`: copia a região ativa para o kill ring sem removê-la.
- `C-k`: recorta do ponto até o final da linha; o uso repetido pode incluir a nova linha.

Recortar é mais do que uma exclusão comum, pois o texto removido é preservado para uma colagem posterior.

:::single-choice{#emacs-edit-copy-region} Qual tecla copia a região ativa para o kill ring sem removê-la?

::option[`M-w`]{#emacs-edit-copy-active-region .correct explanation="`kill-ring-save`, associado a `M-w`, copia a região sem excluí-la."}
::option[`C-w`]{#emacs-edit-kill-active-region explanation="`C-w` remove a região enquanto a salva no kill ring."}
::option[`C-k`]{#emacs-edit-kill-line explanation="`C-k` recorta texto em direção ao final da linha, em vez de copiar a região selecionada sem alterações."}
:::

## Colagem a Partir do Kill Ring

Use `C-y` para colar no ponto a entrada mais recente do kill ring. Imediatamente depois de uma colagem, `M-y` substitui o texto inserido por uma entrada anterior; repetir `M-y` percorre as entradas.

```text
C-y
M-y
```

Se outro comando não relacionado ocorrer depois de `C-y`, `M-y` deixará de ter o mesmo contexto de yank-pop.

:::single-choice{#emacs-edit-yank-latest} Qual tecla insere no ponto a entrada mais recente do kill ring?

::option[`C-y`]{#emacs-edit-yank-answer .correct explanation="`yank`, associado a `C-y`, insere no buffer atual o texto mais recente do kill ring."}
::option[`M-y`]{#emacs-edit-yank-pop explanation="`M-y` normalmente substitui uma entrada que acabou de ser colada por uma anterior; ele depende do contexto da colagem precedente."}
::option[`C-d`]{#emacs-edit-delete-character explanation="`C-d` exclui o caractere depois do ponto e não recupera texto do kill ring."}
:::

Pratique em `*scratch*` ou em um arquivo descartável: mova o ponto, defina a marca, copie uma região, recorte outra e cole as duas novamente. Salve apenas quando o arquivo resultante merecer ser preservado.

## Resumo

Agora você sabe navegar e reorganizar textos no Emacs usando ponto, marca e kill ring.

1. Mova-se por caracteres ou linhas com comandos Control.
2. Mova-se por palavras ou limites do buffer com comandos Meta.
3. Defina a marca com `C-SPC` para criar uma região.
4. Recorte com `C-w` ou copie com `M-w`.
5. Cole com `C-y` e percorra as entradas com `M-y` imediatamente depois.
