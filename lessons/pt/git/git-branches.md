---
lesson_id: "git-branches"
course_id: "git"
lang: "pt"
order_index: 5
title: "Branches"
description: "Entenda como as branches do Git separam linhas de trabalho e como uma mesclagem leva uma alteração para main."
meta_title: "Branches - Git"
meta_description: "Entenda como as branches do Git separam linhas de trabalho e como uma mesclagem leva uma alteração para main."
meta_keywords: "branches, ramificações, mesclagem, git, devops, Linux Journey"
---

Uma **branch** é um nome que aponta para um commit. Quando você cria um commit na branch atual, o nome passa a apontar para o novo commit. As outras branches continuam em suas posições até você atualizá-las.

## Como começar uma linha de trabalho separada

A partir de `main` no repositório de prática, crie uma branch chamada `health-page` e mude para ela. A opção `-c` de `git switch` indica que é preciso criar a branch.

```bash
$ git switch -c health-page
```

No início, os dois nomes apontam para o mesmo commit. Use `git branch --show-current` para conferir qual branch será atualizada no próximo commit.

:::single-choice{#git-branches-start-pointer} Logo depois de git switch -c health-page, para qual commit o novo nome aponta?

::option[Para um commit vazio criado pelo comando.]{#git-branches-start-pointer-a explanation="O comando cria um nome que aponta para um commit existente."}
::option[Para um commit no repositório de outra pessoa.]{#git-branches-start-pointer-c explanation="O comando cria uma branch local no repositório atual."}
::option[Para o commit que serviu de ponto de partida.]{#git-branches-start-pointer-b .correct explanation="No início, os dois nomes apontam para o mesmo estado salvo."}
:::

## Como salvar uma alteração na branch

Com `health-page` como branch atual, adicione um arquivo de status de uma linha e crie um commit.

```bash
$ printf '%s\n' ready > health.txt
$ git add health.txt
$ git commit -m "Add a health page"
```

Imagine que A seja o commit da página inicial e B seja o da página de status.

```text
A (main) --- B (health-page)
```

Só `health-page` avançou para B. Se você voltar para `main` sem alterações pendentes na árvore de trabalho, seus arquivos voltam ao estado de A.

:::single-choice{#git-branches-branch-snapshot} Antes da mesclagem, qual branch contém o commit da página de status?

::option[As duas, porque fazem parte do mesmo repositório.]{#git-branches-branch-snapshot-a explanation="Branches do mesmo repositório podem apontar para estados salvos diferentes."}
::option[Apenas health-page.]{#git-branches-branch-snapshot-c .correct explanation="Essa era a branch atual quando você criou o commit B."}
::option[Apenas main, porque foi a branch inicial.]{#git-branches-branch-snapshot-b explanation="Main não avançou quando você fez um commit em health-page."}
:::

## Como mesclar em main

Mude para a branch que deve receber a alteração e indique a branch de origem.

```bash
$ git switch main
$ git merge health-page
```

Neste caso, `main` não tem mudanças próprias depois de A. O Git pode avançar esse ponteiro diretamente para B, numa operação chamada **fast-forward**. Se cada branch tiver novos commits, pode ser necessário combinar as mudanças. Leia a saída para confirmar que a mesclagem terminou.

:::single-choice{#git-branches-merge-direction} Você quer que main receba a alteração de health-page. Em qual branch você executa a mesclagem?

::option[Em main, indicando health-page como origem.]{#git-branches-merge-direction-a .correct explanation="O resultado da mesclagem entra na branch atual."}
::option[Em health-page, indicando main como origem.]{#git-branches-merge-direction-b explanation="Esse comando atualizaria health-page."}
::option[Em uma nova branch que nenhum dos dois lados usa.]{#git-branches-merge-direction-c explanation="Main continuaria na posição original até receber a alteração."}
:::

## Resumo

Agora você consegue acompanhar uma alteração desde uma branch local até main.

1. Crie uma branch no commit atual.
2. Salve uma alteração na branch escolhida.
3. Mescle a alteração na branch que deve recebê-la.
