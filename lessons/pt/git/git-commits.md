---
lesson_id: "git-commits"
course_id: "git"
lang: "pt"
order_index: 4
title: "Commits"
description: "Aprenda a salvar o conteúdo da área de preparação e a encontrar o commit no histórico do Git."
meta_title: "Commits - Git"
meta_description: "Aprenda a salvar o conteúdo da área de preparação e a encontrar o commit no histórico do Git."
meta_keywords: "commits, git, devops, Linux Journey, histórico do Git"
---

Um **commit** registra os arquivos selecionados na área de preparação. Ele também guarda uma mensagem, um autor e a ligação com os commits anteriores. Com o identificador que o Git atribui, você pode encontrar esse ponto exato no histórico.

## Como definir o autor no repositório de prática

O Git registra um nome e um e-mail junto com o commit. Defina valores de exemplo apenas para este repositório. Esses dados aparecem no histórico e não concedem acesso a um serviço remoto.

```bash
$ git config --local user.name "Journey Learner"
$ git config --local user.email "learner@example.com"
```

Use o repositório de prática com `index.html` na área de preparação. Execute `git status` para conferir quais arquivos entrarão no commit, se precisar.

:::single-choice{#git-commits-identity-scope} O que a opção --local faz neste caso?

::option[Inicia uma sessão em um serviço de hospedagem compartilhado.]{#git-commits-identity-scope-b explanation="Nome e e-mail são dados do commit. A autenticação em um serviço remoto é feita à parte."}
::option[Define os dados de autoria para este repositório.]{#git-commits-identity-scope-a .correct explanation="As configurações locais se aplicam ao repositório atual."}
::option[Muda o autor de todos os commits existentes.]{#git-commits-identity-scope-c explanation="As configurações serão usadas nos próximos commits."}
:::

## Como salvar o estado do projeto

Execute `git commit` depois de preparar a versão desejada. A opção `-m` permite passar a mensagem na linha de comando.

```bash
$ git commit -m "Set the homepage heading"
```

O commit salva a versão do arquivo que está na área de preparação. Se você voltar a editar o arquivo na árvore de trabalho, essa alteração posterior só entrará no commit quando você a colocar na área de preparação.

:::single-choice{#git-commits-staged-snapshot} Você preparou o título Welcome e depois digitou Hi no arquivo sem adicioná-lo novamente à área de preparação. Que título o commit vai conter?

::option[Welcome, porque essa é a versão que você preparou.]{#git-commits-staged-snapshot-c .correct explanation="O commit registra o conteúdo que está na área de preparação."}
::option[Hi, porque é o texto mais recente no disco.]{#git-commits-staged-snapshot-a explanation="A cópia de trabalho mais recente pode ser diferente da cópia na área de preparação."}
::option[Os dois, porque o Git salva cada edição automaticamente.]{#git-commits-staged-snapshot-b explanation="O estado preparado contém uma única versão selecionada do arquivo."}
:::

## Como ler o histórico abreviado

Use `git log --oneline` para ver o histórico em formato compacto. Cada linha começa com o identificador abreviado do commit, seguido da mensagem. O identificador que aparecer para você será diferente do exemplo.

```text
$ git log --oneline
a12c345 Set the homepage heading
```

Use o identificador para indicar o commit exato, pois dois commits podem ter a mesma mensagem. Normalmente, o primeiro item é o commit mais recente da linha atual do histórico.

:::single-choice{#git-commits-identify-snapshot} Dois commits têm a mensagem Set the homepage heading. O que permite distinguir os estados salvos nos dois?

::option[A mensagem que os dois commits têm em comum.]{#git-commits-identify-snapshot-a explanation="O mesmo texto pode aparecer em vários commits."}
::option[O nome do arquivo alterado nos dois commits.]{#git-commits-identify-snapshot-c explanation="Um mesmo arquivo pode aparecer em muitos commits."}
::option[O identificador do commit.]{#git-commits-identify-snapshot-b .correct explanation="O identificador permite apontar para uma entrada específica."}
:::

Para praticar a preparação de alterações e a criação de commits no terminal do navegador, experimente [seu primeiro laboratório de Git](https://labex.io/tutorials/git-your-first-git-lab-92739).

## Resumo

Agora você pode salvar as alterações preparadas e encontrá-las no histórico.

1. Defina os dados de autoria no repositório de prática.
2. Salve as alterações preparadas com uma mensagem clara.
3. Identifique um commit no histórico abreviado.
