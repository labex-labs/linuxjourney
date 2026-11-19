---
lesson_id: "git-remotes"
course_id: "git"
lang: "pt"
order_index: 6
title: "Repositórios remotos"
description: "Entenda como um remoto conecta repositórios no Git e como distinguir o recebimento do envio de alterações."
meta_title: "Repositórios remotos - Git"
meta_description: "Entenda como um remoto conecta repositórios no Git e como distinguir o recebimento do envio de alterações."
meta_keywords: "git remote, repositórios remotos, git fetch, git push, git, devops, Linux Journey"
---

Um **remoto** é um endereço com nome que seu repositório Git local pode usar para entrar em contato com outro repositório. O outro repositório pode estar em um serviço de hospedagem ou em um diretório na mesma máquina. Este exemplo usa um diretório local separado e funciona sem uma conta em um serviço de hospedagem.

## Como adicionar um endereço

A partir do repositório de prática, crie um repositório separado do tipo **bare**. Esse tipo guarda o histórico e as referências, sem uma árvore de trabalho para os arquivos do projeto. Ele pode receber commits do seu ambiente de trabalho. Para começar do zero, use um diretório `journey-remote.git` que ainda não esteja em uso.

```bash
$ git init --bare --initial-branch=main ../journey-remote.git
$ git remote add origin ../journey-remote.git
$ git remote -v
```

O nome `origin` é uma convenção comum. A lista de remotos mostra a que endereço esse nome corresponde.

:::single-choice{#git-remotes-add-address} Você executou git remote add e viu origin na lista. O que o Git fez?

::option[Registrou um nome para o outro repositório.]{#git-remotes-add-address-b .correct explanation="Nos comandos seguintes, você pode usar origin para indicar esse endereço."}
::option[Enviou todos os commits locais.]{#git-remotes-add-address-a explanation="Adicionar um remoto registra um endereço. Para enviar commits, você usa push."}
::option[Clonou outra árvore de trabalho dentro do seu projeto.]{#git-remotes-add-address-c explanation="A árvore de trabalho que você já tinha continua no mesmo lugar."}
:::

## Como enviar uma branch

Use `git push` para enviar commits locais e solicitar que o remoto atualize sua branch. A opção `-u` registra a branch remota como upstream, ou seja, a branch que o Git associa à sua para comandos futuros.

```bash
$ git push -u origin main
```

Neste exercício, o push envia mudanças apenas para o diretório de prática separado. Um remoto compartilhado pode exigir autorização e recusar atualizações. Confira a resposta para saber se o envio deu certo.

:::single-choice{#git-remotes-push-direction} Qual comando envia um novo commit de main local para este remoto?

::option[git fetch origin]{#git-remotes-push-direction-b explanation="Fetch traz informações do remoto para o repositório local."}
::option[git remote -v]{#git-remotes-push-direction-c explanation="Esse comando mostra qual endereço origin usa."}
::option[git push origin main]{#git-remotes-push-direction-a .correct explanation="Push transfere os commits de que o remoto precisa e solicita a atualização da branch."}
:::

## Como receber uma atualização

Use `git fetch origin` para atualizar a cópia local do histórico remoto. O Git registra o último estado recebido em uma **branch de acompanhamento remoto**, como `origin/main`. Você pode conferir esse estado com `git log --oneline origin/main`. Executar apenas fetch mantém a árvore de trabalho na branch local atual.

```bash
$ git fetch origin
$ git log --oneline origin/main
```

:::single-choice{#git-remotes-after-fetch} Você executou fetch, e origin/main avançou. A branch main local ficou no mesmo lugar. O que aconteceu?

::option[Fetch sobrescreveu os arquivos que você estava editando.]{#git-remotes-after-fetch-a explanation="Fetch atualiza as informações locais sobre a branch remota."}
::option[O Git recebeu as informações sobre a mudança remota. Integrá-la é uma etapa separada.]{#git-remotes-after-fetch-c .correct explanation="Sua branch local pode ficar na posição original mesmo quando origin/main avança."}
::option[Seu push atualizou o remoto durante o fetch.]{#git-remotes-after-fetch-b explanation="Fetch recebe informações do remoto."}
:::

## Resumo

Agora você consegue identificar qual repositório é afetado por cada comando.

1. Adicione um endereço remoto e confira o valor registrado.
2. Envie uma branch e identifique sua upstream.
3. Busque o histórico remoto atualizado sem alterar os arquivos da branch atual.
