---
lesson_id: "emacs-exiting-and-help"
course_id: "advanced-text-fu"
lang: "pt"
order_index: 13
title: "Saída e Ajuda no Emacs"
description: "Aprenda a sair do Emacs com segurança, cancelar comandos pendentes, consultar tópicos de ajuda e desfazer alterações."
meta_title: "Saída e Ajuda no Emacs - Text-Fu Avançado"
meta_description: "Aprenda a sair do Emacs, acessar a ajuda, cancelar comandos pendentes e desfazer alterações com segurança."
meta_keywords: "sair Emacs, ajuda Emacs, desfazer Emacs, tutorial Emacs, editor texto Linux, guia para iniciantes"
---

O Emacs oferece ajuda contextual para teclas, funções, variáveis e modos ativos. Ele também protege os buffers modificados associados a arquivos durante a saída, oferecendo a oportunidade de salvar ou recusar cada gravação.

## Saída do Emacs

Use `C-x C-c`, que executa `save-buffers-kill-terminal`, para solicitar o fechamento da sessão ou da conexão de terminal do Emacs:

```text
C-x C-c
```

O Emacs verifica os buffers modificados relevantes associados a arquivos e pergunta se deve salvá-los. Leia o nome de cada buffer e responda conscientemente. Ele também pode perguntar sobre processos ativos. Cancele a saída se precisar inspecionar o trabalho antes de decidir.

Em um fluxo com `emacsclient` ou um servidor do Emacs, o comportamento exato do frame e do servidor pode variar, mas as perguntas sobre buffers modificados continuam merecendo atenção.

:::single-choice{#emacs-exit-key}
Qual sequência de teclas solicita uma saída normal do Emacs e verifica os buffers modificados?

::option[`C-x k`]{#emacs-exit-kill-buffer explanation="Essa sequência encerra um buffer selecionado e não solicita a saída da sessão do Emacs."}
::option[`C-g`]{#emacs-exit-keyboard-quit explanation="Essa tecla cancela um comando ou uma pergunta pendente, em vez de fechar o Emacs."}
::option[`C-x C-c`]{#emacs-exit-save-buffers .correct explanation="Essa sequência executa o fluxo normal de salvar buffers e sair, incluindo perguntas sobre trabalho não salvo relevante."}
:::

## Abertura do Seletor de Ajuda

O prefixo padrão da ajuda é `C-h`. Use `C-h C-h`, que executa a ajuda sobre a própria ajuda, para exibir orientações sobre os comandos disponíveis:

```text
C-h C-h
```

A segunda tecla escolhe o tipo de ajuda necessária.

:::single-choice{#emacs-help-for-help}
Qual sequência de teclas explica como usar o sistema de ajuda do Emacs?

::option[`C-h C-h`]{#emacs-help-help .correct explanation="O prefixo de ajuda seguido de outro `C-h` abre a explicação do próprio seletor de ajuda."}
::option[`C-x C-h`]{#emacs-help-prefix-list explanation="Essa não é a sequência de ajuda sobre a ajuda apresentada aqui."}
::option[`C-h t`]{#emacs-help-tutorial-other explanation="Essa sequência abre diretamente o tutorial, em vez de explicar o menu de ajuda mais amplo."}
:::

## Descrição de Teclas e do Estado do Editor

Alguns comandos úteis de ajuda são:

- `C-h k KEY`: descreve o que uma sequência de teclas executa.
- `C-h f FUNCTION`: descreve uma função Emacs Lisp.
- `C-h v VARIABLE`: descreve uma variável Emacs Lisp.
- `C-h m`: descreve os modos principal e secundários atuais.
- `C-h t`: abre o tutorial interativo.

Por exemplo, digite `C-h k C-x C-s` para ver a documentação da associação de `save-buffer`.

:::single-choice{#emacs-describe-key}
Você quer descobrir o que `C-x C-s` faz. Qual prefixo de ajuda deve inserir antes dessa sequência?

::option[`C-h k`]{#emacs-describe-key-answer .correct explanation="`describe-key` aguarda uma sequência e explica o comando associado a ela."}
::option[`C-h f`]{#emacs-describe-function explanation="Essa forma solicita um nome de função, em vez de ler uma sequência para identificar sua associação."}
::option[`C-h v`]{#emacs-describe-variable explanation="Essa forma solicita um nome de variável e não inspeciona uma associação de teclas."}
:::

## Cancelamento de um Comando Pendente

Use `C-g`, associado a `keyboard-quit`, quando estiver preso em uma pergunta, sequência parcialmente inserida, pesquisa incremental ou outro comando que queira cancelar:

```text
C-g
```

Ele não desfaz alterações do buffer que já ocorreram nem sai do Emacs. Ele interrompe a interação atual e devolve o controle à edição comum quando possível.

:::single-choice{#emacs-cancel-pending-command}
Qual tecla normalmente cancela a pergunta ou o comando pendente atual do Emacs?

::option[`C-x C-c`]{#emacs-cancel-exit explanation="Essa sequência inicia o fluxo de saída do Emacs, em vez de apenas cancelar a pergunta atual."}
::option[`C-y`]{#emacs-cancel-yank explanation="Essa tecla cola texto do kill ring e não cancela um comando."}
::option[`C-g`]{#emacs-keyboard-quit-answer .correct explanation="`keyboard-quit` aborta a interação do comando atual e devolve o controle ao Emacs."}
:::

## Como Desfazer Alterações do Buffer

Use `C-/`, `C-_` ou `C-x u` para invocar o recurso de desfazer em configurações comuns do Emacs:

```text
C-/
```

Comandos repetidos de desfazer percorrem para trás as alterações recentes do buffer. O movimento do cursor por si só normalmente não é uma alteração. Versões e configurações do Emacs podem oferecer `undo-redo` e ferramentas de histórico mais avançadas; use `C-h k` nas associações reais de desfazer e refazer para verificar o comportamento local.

:::single-choice{#emacs-undo-change}
Qual sequência é uma associação padrão para desfazer uma alteração recente do buffer no Emacs?

::option[`C-/`]{#emacs-undo-control-slash .correct explanation="`C-/` é uma associação padrão para desfazer, junto com `C-_` e `C-x u` em configurações comuns."}
::option[`C-x C-s`]{#emacs-undo-save explanation="Essa sequência salva o buffer atual, não percorre seu histórico de desfazer."}
::option[`C-w`]{#emacs-undo-kill explanation="Essa tecla recorta a região ativa e cria outra alteração, em vez de desfazer uma."}
:::

Pratique abrindo `*scratch*`, fazendo uma alteração descartável, usando desfazer, consultando `C-h k` sobre uma tecla desconhecida e cancelando uma pergunta do minibuffer com `C-g` antes de sair normalmente.

## Resumo

Agora você sabe recuperar ajuda e sair do Emacs sem ignorar trabalho não salvo.

1. Saia passando pelas verificações de buffers modificados com `C-x C-c`.
2. Abra a ajuda sobre a ajuda com `C-h C-h`.
3. Descreva teclas, funções, variáveis ou modos ativos.
4. Cancele um comando pendente com `C-g`.
5. Desfaça alterações recentes do buffer com uma associação local verificada.
