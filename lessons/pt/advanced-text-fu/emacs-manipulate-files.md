---
lesson_id: "emacs-manipulate-files"
course_id: "advanced-text-fu"
lang: "pt"
order_index: 10
title: "Manipulação de Arquivos no Emacs"
description: "Aprenda a visitar, salvar, renomear, recarregar e revisar buffers associados a arquivos no Emacs."
meta_title: "Manipulação de Arquivos no Emacs - Text-Fu Avançado"
meta_description: "Aprenda a abrir e salvar arquivos no Emacs e usar Salvar como com as sequências C-x C-f, C-x C-s e C-x C-w."
meta_keywords: "Emacs, salvar arquivo Emacs, abrir arquivo Emacs, tutorial Emacs, comandos Linux, Emacs para iniciantes, guia Emacs"
---

O Emacs visita arquivos em buffers. A edição altera primeiro o buffer; o salvamento grava seu conteúdo atual no caminho associado. Leia as mensagens do minibuffer, pois permissões, alterações conflitantes no disco ou outros erros podem impedir uma gravação.

## Visita a um Arquivo

Use `C-x C-f`, que executa `find-file`, insira um caminho no minibuffer e pressione Enter:

```text
C-x C-f
```

O Emacs abre um arquivo existente e legível em um buffer ou prepara um novo buffer de visita quando o caminho está ausente. No segundo caso, nenhum arquivo existe no disco até que um salvamento tenha sucesso.

Você pode usar a conclusão com Tab enquanto insere o caminho. Visitar um diretório normalmente abre o Dired, o editor de diretórios do Emacs, em vez de tratá-lo como arquivo de texto.

:::single-choice{#emacs-find-file-key} Qual sequência de teclas do Emacs solicita um caminho e o visita?

::option[`C-x C-s`]{#emacs-file-save explanation="Essa sequência salva o buffer atual associado a um arquivo e não solicita outro caminho para visitar."}
::option[`C-x C-c`]{#emacs-file-exit explanation="Essa sequência inicia a saída do Emacs, não a abertura de um arquivo."}
::option[`C-x C-f`]{#emacs-find-file .correct explanation="Essa sequência executa `find-file` e solicita no minibuffer o caminho que será visitado."}
:::

:::single-choice{#emacs-find-missing-file} Quando `C-x C-f` visita um caminho inexistente, em que momento o arquivo normalmente é criado no disco?

::option[Somente depois que o novo buffer é salvo com sucesso.]{#emacs-file-created-on-save .correct explanation="O buffer pode manter edições antes de existir um arquivo, e o salvamento realiza a criação."}
::option[Imediatamente depois que o caminho é inserido.]{#emacs-file-created-immediately explanation="O Emacs primeiro cria um buffer associado ao novo caminho; a criação no disco é adiada."}
::option[Somente depois que o próprio Emacs é fechado.]{#emacs-file-created-on-exit explanation="A saída pode solicitar o salvamento, mas a criação está ligada a um salvamento bem-sucedido, não necessariamente ao fechamento."}
:::

## Salvamento do Buffer Atual

Use `C-x C-s`, que executa `save-buffer`, para salvar o buffer atual associado a um arquivo:

```text
C-x C-s
```

Se o buffer não possuir um nome associado, o Emacs solicitará um. Uma gravação bem-sucedida limpa o indicador de modificação; uma falha mantém os dados não salvos no buffer e informa um erro.

:::single-choice{#emacs-save-current-buffer} Qual sequência de teclas salva o buffer atual associado a um arquivo?

::option[`C-x C-s`]{#emacs-save-buffer-key .correct explanation="`C-x C-s` executa `save-buffer` para o buffer atual."}
::option[`C-x C-w`]{#emacs-write-file-key explanation="Essa sequência solicita outro nome e muda o arquivo que o buffer visita."}
::option[`C-x s`]{#emacs-save-some-key explanation="Essa sequência verifica vários buffers associados a arquivos e pergunta se devem ser salvos, em vez de atuar apenas no atual."}
:::

## Gravação com Outro Nome

Use `C-x C-w`, que executa `write-file`, para solicitar um caminho, gravar o buffer nele e fazer o buffer visitar esse novo arquivo:

```text
C-x C-w
```

Esse é o comportamento “Salvar como” do Emacs. Ele difere de simplesmente gravar uma cópia separada e continuar visitando o caminho original.

:::single-choice{#emacs-write-file-as} Qual sequência de teclas realiza a operação comum de Salvar como para o buffer atual?

::option[`C-x C-f`]{#emacs-find-file-other explanation="Essa sequência visita um arquivo e pode mudar para outro buffer; ela não é Salvar como para o buffer atual."}
::option[`C-x k`]{#emacs-write-as-kill-buffer explanation="Essa sequência solicita o encerramento de um buffer e pode perguntar sobre alterações não salvas; ela não salva com outro nome."}
::option[`C-x C-w`]{#emacs-write-file-answer .correct explanation="`write-file` grava no caminho escolhido e faz o buffer visitar esse arquivo."}
:::

## Revisão de Vários Buffers Modificados

Use `C-x s`, que executa `save-some-buffers`, para examinar os buffers modificados associados a arquivos:

```text
C-x s
```

O Emacs normalmente pergunta se deve salvar cada buffer modificado elegível. Leia o nome do buffer e responda conscientemente; esse não é um atalho incondicional para salvar tudo.

:::single-choice{#emacs-save-some-buffers} O que `C-x s` normalmente faz?

::option[Pergunta se deve salvar os buffers modificados associados a arquivos.]{#emacs-prompt-save-some .correct explanation="`save-some-buffers` examina os buffers modificados elegíveis e pergunta quais devem ser gravados."}
::option[Salva silenciosamente todos os buffers sem mostrar seus nomes.]{#emacs-silent-save-all explanation="O comando interativo normal faz perguntas, em vez de gravar incondicionalmente todos os buffers."}
::option[Fecha todos os buffers depois de salvar o atual.]{#emacs-close-all-buffers explanation="O comando trata do salvamento de vários buffers e normalmente não os fecha."}
:::

## Reversão a Partir do Disco

Se um arquivo mudou no disco e você quiser conscientemente descartar o conteúdo atual do buffer, execute `M-x revert-buffer` e examine a confirmação. A reversão pode destruir edições não salvas; por isso, use-a somente depois de confirmar qual fonte deve prevalecer.

Para comparar antes de decidir, salve uma cópia separada ou use controle de versão e ferramentas de diff. Não trate operações de recarga como inofensivas quando o buffer estiver modificado.

## Resumo

Agora você sabe gerenciar buffers associados a arquivos sem confundir visitas e gravações.

1. Visite um caminho com `C-x C-f`.
2. Crie um arquivo ausente somente quando seu buffer for salvo.
3. Salve o buffer atual com `C-x C-s`.
4. Salve com um novo nome visitado usando `C-x C-w`.
5. Revise vários buffers modificados com `C-x s`.
