---
lesson_id: "git-repositories"
course_id: "git"
lang: "pt"
order_index: 1
title: "Repositórios"
description: "Entenda o que um repositório Git guarda e crie um repositório vazio para um pequeno site."
meta_title: "Repositórios - Git"
meta_description: "Entenda o que um repositório Git guarda e crie um repositório vazio para um pequeno site."
meta_keywords: "repositórios, git, devops, Linux Journey"
---

Um site começa com alguns arquivos. Com o Git, você pode registrar como esses arquivos estavam em determinados momentos. Os arquivos do projeto e o histórico formam seu ambiente local de trabalho com o Git.

## Como criar um repositório

Comece em um diretório de prática no qual você possa criar uma pasta. Execute os comandos abaixo uma vez. O cifrão indica o prompt do shell.

```bash
$ mkdir journey-git
$ cd journey-git
$ git init --initial-branch=main
```

A nova pasta é a sua **árvore de trabalho**, onde você edita os arquivos do projeto. O Git cria ali o diretório oculto `.git` para guardar o histórico e as configurações. O novo repositório ainda não tem nenhuma alteração salva. O Git chama a linha de trabalho inicial de `main`.

:::single-choice{#git-repositories-empty-history} Você inicializa um repositório que já contém index.html. O que acontece com o histórico desse arquivo?

::option[O Git registra o arquivo imediatamente no primeiro commit.]{#git-repositories-empty-history-b explanation="A inicialização não registra nenhum dos arquivos do projeto."}
::option[O Git pode registrá-lo em um commit futuro.]{#git-repositories-empty-history-a .correct explanation="Inicializar prepara o repositório. Para registrar o estado do arquivo, é preciso fazer um commit."}
::option[O Git move o arquivo para o diretório oculto.]{#git-repositories-empty-history-c explanation="Os arquivos do projeto continuam na árvore de trabalho para que você possa editá-los."}
:::

![Terminal do LabEx após inicializar um repositório Git vazio e exibir a pasta de prática como sua raiz](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-repositories/init-and-root.png)

## Como localizar a árvore de trabalho

Use `git rev-parse --show-toplevel` para mostrar a raiz do repositório atual. No terminal, dentro da pasta de prática, o comando deve mostrar um caminho que termina em `journey-git`. Uma pasta dentro dessa árvore de trabalho pertence ao mesmo repositório, a menos que contenha um repositório próprio.

```bash
$ git rev-parse --show-toplevel
```

:::single-choice{#git-repositories-find-root} Você entra no subdiretório images dentro de journey-git. Qual diretório o Git deve indicar como raiz?

::option[O diretório journey-git.]{#git-repositories-find-root-b .correct explanation="O Git encontra a raiz do repositório acima da sua localização atual."}
::option[O subdiretório images.]{#git-repositories-find-root-a explanation="A raiz corresponde ao repositório, mesmo quando o shell está em um subdiretório."}
::option[O diretório oculto .git.]{#git-repositories-find-root-c explanation="O comando mostra a raiz da árvore de trabalho, onde ficam os arquivos do projeto."}
:::

## Como começar com um histórico existente

Use `git clone` quando já houver um repositório que você queira copiar. Uma clonagem comum cria uma árvore de trabalho local e importa o histórico do repositório existente. Use `git init` para um projeto cujo histórico você está começando localmente. Você vai continuar usando `journey-git` nas próximas lições.

:::single-choice{#git-repositories-choose-start} Uma pessoa da sua equipe enviou o endereço de um repositório, e você precisa do histórico. Como começar?

::option[Crie uma pasta vazia e inicialize um repositório nela.]{#git-repositories-choose-start-a explanation="Um repositório novo começa sem o histórico da equipe."}
::option[Copie apenas os arquivos visíveis do site.]{#git-repositories-choose-start-b explanation="Os arquivos visíveis representam uma versão e não incluem o histórico."}
::option[Clone o repositório que você recebeu.]{#git-repositories-choose-start-c .correct explanation="A clonagem copia o histórico compartilhado e cria uma árvore de trabalho local."}
:::

## Resumo

Agora você sabe como iniciar um repositório Git local em cada situação.

1. Identifique a árvore de trabalho e o diretório oculto do Git.
2. Encontre a raiz a partir de um subdiretório.
3. Inicialize um repositório para criar um histórico ou clone um repositório para aproveitar o histórico existente.
