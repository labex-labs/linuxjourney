---
lesson_id: "git-status-command"
course_id: "git"
lang: "pt"
order_index: 2
title: "git status"
description: "Aprenda a usar git status para identificar arquivos não rastreados, arquivos na área de preparação e arquivos modificados."
meta_title: "git status - Git"
meta_description: "Aprenda a usar git status para identificar arquivos não rastreados, arquivos na área de preparação e arquivos modificados."
meta_keywords: "git status, git, devops, Linux Journey, área de preparação"
---

Ao trabalhar em um repositório, `git status` mostra o que o Git encontrou na árvore de trabalho e o que você selecionou para salvar em seguida. Use o repositório vazio `journey-git` da lição anterior.

## Como identificar um arquivo novo

Crie uma página simples e use o formato abreviado para que o resultado fique mais fácil de ler.

```bash
$ printf '%s\n' '<h1>Hello</h1>' > index.html
$ git status --short
```

Aqui, `>` grava no arquivo indicado, substituindo seu conteúdo caso ele já exista. Para um arquivo novo, a saída abreviada é `?? index.html`. O Git chama esse arquivo de **não rastreado**. Ele existe, mas ainda não foi selecionado para o próximo registro do projeto.

:::single-choice{#git-status-command-untracked-file} O Git mostra dois pontos de interrogação ao lado de um arquivo novo. O que isso indica?

::option[O arquivo já faz parte do último estado salvo.]{#git-status-command-untracked-file-a explanation="Um arquivo não rastreado não aparece no último estado salvo."}
::option[O arquivo foi removido da árvore de trabalho.]{#git-status-command-untracked-file-c explanation="O Git encontrou esse arquivo na árvore de trabalho."}
::option[O arquivo existe, mas ainda está fora do próximo commit.]{#git-status-command-untracked-file-b .correct explanation="Você pode adicionar o arquivo à área de preparação."}
:::

![Saída abreviada do Git mostrando index.html passar de arquivo não rastreado para a área de preparação](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-status-command/staged-file.png)

## Como conferir o que está preparado

Execute `git add` para selecionar o conteúdo atual do arquivo para o próximo registro do estado do projeto, chamado de **commit**. Essa seleção fica na **área de preparação**. Na saída abreviada, aparece um `A` na primeira coluna para indicar uma adição que aguarda o commit.

```bash
$ git add index.html
$ git status --short
```

:::single-choice{#git-status-command-staged-new} Depois de git add, onde fica a versão selecionada de index.html?

::option[Já está em um commit novo.]{#git-status-command-staged-new-a explanation="Git add prepara o próximo commit. Ele ainda precisa ser criado."}
::option[Na área de preparação.]{#git-status-command-staged-new-c .correct explanation="O Git selecionou o conteúdo que existia no momento em que você executou git add."}
::option[No repositório de outra pessoa.]{#git-status-command-staged-new-b explanation="A alteração só afeta a área de preparação local."}
:::

## Como distinguir dois tipos de alteração

O formato abreviado tem duas colunas antes do nome do arquivo. A primeira indica mudanças na área de preparação. A segunda indica mudanças feitas depois que você preparou o arquivo. Por exemplo, `AM index.html` significa que você preparou um arquivo novo e depois modificou a cópia de trabalho. Se preferir ver os detalhes em grupos com títulos, use `git status` sem opções.

:::single-choice{#git-status-command-two-columns} Você vê AM ao lado de index.html. O que deve conferir antes do próximo commit?

::option[Se a cópia na área de preparação inclui a alteração que você quer salvar.]{#git-status-command-two-columns-a .correct explanation="O M na segunda coluna indica que há uma alteração mais recente na cópia de trabalho."}
::option[Se há outro arquivo chamado AM no repositório.]{#git-status-command-two-columns-b explanation="AM são dois indicadores de estado relativos a index.html."}
::option[Se o arquivo foi excluído do disco.]{#git-status-command-two-columns-c explanation="O M indica uma alteração na árvore de trabalho."}
:::

## Resumo

Agora você pode conferir quais alterações o Git salvaria no próximo commit.

1. Reconheça um arquivo novo ainda não rastreado.
2. Use git add para colocar um arquivo na área de preparação.
3. Leia separadamente as mudanças preparadas e as da árvore de trabalho.
