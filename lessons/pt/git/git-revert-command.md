---
lesson_id: "git-revert-command"
course_id: "git"
lang: "pt"
order_index: 8
title: "git revert"
description: "Entenda como git revert registra a reversão de uma alteração e mantém o commit original no histórico."
meta_title: "git revert - Git"
meta_description: "Entenda como git revert registra a reversão de uma alteração e mantém o commit original no histórico."
meta_keywords: "git revert, reverter um commit, git, devops, Linux Journey"
---

Mesmo depois de compartilhar uma alteração, você pode desfazê-la. Use `git revert` para aplicar a mudança inversa em um novo commit. Assim, o histórico mostra o que mudou originalmente e o que foi feito para desfazer essa mudança.

## Como encontrar a alteração a desfazer

No repositório de prática, `main` contém os commits da página inicial e da página de status. Consulte o histórico abreviado para confirmar qual entrada é a mais recente. Os identificadores abaixo são exemplos.

```text
$ git log --oneline
3ab4501 Add a health page
a12c345 Set the homepage heading
```

`HEAD` indica o commit que está ativo na sua cópia de trabalho. Confira se é a alteração que você quer desfazer. Use `git status` para confirmar que a árvore de trabalho está limpa antes de continuar.

:::single-choice{#git-revert-command-newest-commit} Neste exemplo, que alteração seria desfeita ao reverter HEAD?

::option[A alteração anterior no título da página inicial.]{#git-revert-command-newest-commit-b explanation="A mudança de título está no commit anterior."}
::option[As duas mudanças em uma única operação.]{#git-revert-command-newest-commit-c explanation="Aqui, HEAD indica um commit, e a reversão se aplica a esse commit."}
::option[A inclusão da página de status.]{#git-revert-command-newest-commit-a .correct explanation="HEAD aponta para a entrada mais recente mostrada nessa branch."}
:::

## Como registrar a reversão

No repositório de prática com a árvore de trabalho limpa, reverta o commit da página de status. A operação altera os arquivos da árvore de trabalho e cria um commit. Use `--no-edit` para manter a mensagem de reversão sugerida pelo Git.

```bash
$ git revert --no-edit HEAD
```

Neste exemplo, o arquivo de status é removido porque tinha sido adicionado pelo commit original. Se alguém alterou as mesmas linhas depois, o Git pode parar e pedir que você resolva os conflitos. Consulte o status antes de continuar.

:::single-choice{#git-revert-command-undo-effect} Se a reversão do exemplo der certo, o que você verá nos arquivos do projeto?

::option[O arquivo da página inicial é excluído junto com o da página de status.]{#git-revert-command-undo-effect-a explanation="O commit anterior, que altera a página inicial, continua em vigor."}
::option[O arquivo da página de status é removido.]{#git-revert-command-undo-effect-b .correct explanation="A reversão desfaz a inclusão feita pelo commit escolhido."}
::option[A página de status é adicionada pela segunda vez.]{#git-revert-command-undo-effect-c explanation="A reversão aplica a mudança inversa à original."}
:::

![Histórico do Git com a nova entrada de reversão e o commit original da página de status](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-revert-command/recorded-undo.png)

## Como conferir o histórico depois da reversão

Execute `git log --oneline` de novo. A nova entrada de reversão deve aparecer acima do commit original da página de status. Use `git status --short` para conferir se ficaram alterações locais pendentes. Você pode revisar e compartilhar o novo commit da mesma forma que qualquer outra alteração.

:::single-choice{#git-revert-command-history-after-revert} O que ainda deve aparecer abaixo da nova entrada de reversão?

::option[O commit original da página de status.]{#git-revert-command-history-after-revert-c .correct explanation="As duas entradas registram a mudança original e a operação que a desfez."}
::option[Apenas o commit inicial que alterou o título.]{#git-revert-command-history-after-revert-a explanation="O commit original da página de status continua no histórico."}
::option[Nenhum commit.]{#git-revert-command-history-after-revert-b explanation="Uma reversão acrescenta um commit ao histórico existente da branch."}
:::

## Como preservar outras alterações

Imagine um histórico com três mudanças separadas. Primeiro alguém adicionou o arquivo de status, depois corrigiu um erro de digitação na página inicial, e as duas mudanças foram compartilhadas. Ao reverter o commit que adicionou o arquivo de status, você pode desfazer essa inclusão e manter a correção independente. Leia o histórico e confira os arquivos afetados antes de escolher o commit.

:::single-choice{#git-revert-command-final-application} Que verificação mostra que a reversão preservou a alteração desejada?

::option[O commit que adicionou o arquivo de status sumiu do histórico.]{#git-revert-command-final-application-b explanation="A reversão mantém a entrada original no histórico."}
::option[A correção do erro de digitação também sumiu da página inicial.]{#git-revert-command-final-application-c explanation="A correção foi uma mudança separada e deve permanecer."}
::option[O arquivo de status sumiu, a página inicial continua corrigida e a reversão aparece no histórico.]{#git-revert-command-final-application-a .correct explanation="Esses sinais mostram qual mudança foi desfeita, qual foi preservada e o que entrou no histórico."}
:::

## Resumo

Agora você consegue desfazer uma alteração já salva e manter um registro das duas operações.

1. Identifique exatamente qual commit quer reverter.
2. Reverta-o com a árvore de trabalho limpa.
3. Confira se as duas entradas aparecem no histórico.
