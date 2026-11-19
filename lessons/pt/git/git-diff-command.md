---
lesson_id: "git-diff-command"
course_id: "git"
lang: "pt"
order_index: 3
title: "git diff"
description: "Aprenda a usar git diff para comparar a versão de um arquivo na árvore de trabalho com a da área de preparação."
meta_title: "git diff - Git"
meta_description: "Aprenda a usar git diff para comparar a versão de um arquivo na árvore de trabalho com a da área de preparação."
meta_keywords: "git diff, comparação de versões, git, devops, Linux Journey"
---

O status mostra quais arquivos mudaram. Para ver quais linhas mudaram, use `git diff`. Neste exemplo, a versão de `index.html` com o título Hello foi colocada na área de preparação na lição anterior.

## Como comparar um arquivo com a versão preparada

Troque o título no arquivo de prática e compare a cópia de trabalho com a versão na área de preparação.

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
$ git diff -- index.html
```

O `--` separa as opções do caminho do arquivo que você quer conferir. Na saída, a linha que começa com `-` vem da versão anterior. A que começa com `+` é a linha que entrou no lugar. As duas linhas abaixo são o trecho da comparação que mostra essa alteração.

```diff
-<h1>Hello</h1>
+<h1>Welcome</h1>
```

:::single-choice{#git-diff-command-changed-heading} Qual título está na cópia de trabalho agora?

::option[Welcome.]{#git-diff-command-changed-heading-b .correct explanation="Neste caso, a linha com o sinal de mais mostra o texto novo na árvore de trabalho."}
::option[Hello.]{#git-diff-command-changed-heading-a explanation="A linha com o sinal de menos mostra o texto que já estava na área de preparação."}
::option[Os dois títulos.]{#git-diff-command-changed-heading-c explanation="As duas linhas mostram a versão anterior e a versão atual de uma mesma linha do arquivo."}
:::

## Como comparar a área de preparação com o histórico

Use `git diff --staged -- index.html` para comparar a versão preparada com o último commit. Antes do primeiro commit, o Git usa um estado vazio como referência. Aqui, a comparação mostra que o título Hello foi adicionado. Já `git diff` sem opções mostra a mudança posterior para Welcome.

```bash
$ git diff --staged -- index.html
```

:::single-choice{#git-diff-command-preview-commit} Que comando mostra o que entraria em um commit se você o criasse agora?

::option[git diff -- index.html]{#git-diff-command-preview-commit-b explanation="Esse comando compara o arquivo de trabalho com a versão na área de preparação."}
::option[git status --short]{#git-diff-command-preview-commit-c explanation="O status indica onde há alterações, mas não mostra as linhas modificadas."}
::option[git diff --staged -- index.html]{#git-diff-command-preview-commit-a .correct explanation="Esse comando compara o conteúdo selecionado com o último estado salvo."}
:::

![Terminal do LabEx comparando o título Welcome na árvore de trabalho com o título Hello na área de preparação](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-diff-command/working-and-staged.png)

## O que significa uma comparação sem saída

Adicione novamente o arquivo atual para atualizar a cópia na área de preparação.

```bash
$ git add index.html
$ git diff -- index.html
```

Agora, `git diff` sem opções pode não mostrar nada, porque a cópia de trabalho e a preparada são iguais. Para ver a alteração que ainda aguarda o commit, compare a área de preparação com o histórico. O Git também deixa arquivos não rastreados fora dessas comparações comuns. Consulte o status quando tiver dúvidas sobre o estado de uma alteração.

:::single-choice{#git-diff-command-empty-diff} Logo depois de preparar a alteração, git diff sem opções não mostra nada. Onde você ainda pode conferir a mudança em relação ao histórico?

::option[Em uma segunda execução de git diff sem opções.]{#git-diff-command-empty-diff-a explanation="Repetir essa comparação continua comparando duas cópias iguais."}
::option[Em git diff --staged.]{#git-diff-command-empty-diff-c .correct explanation="Esse comando compara a cópia preparada com o estado de referência no histórico."}
::option[Somente depois de criar um commit.]{#git-diff-command-empty-diff-b explanation="Você pode conferir o conteúdo do commit antes de salvá-lo."}
:::

## Resumo

Agora você pode escolher a comparação que responde à sua dúvida.

1. Identifique as linhas removidas e adicionadas na saída.
2. Compare o arquivo de trabalho com a área de preparação.
3. Confira as alterações preparadas antes de criar um commit.
