---
lesson_id: "docker-images"
course_id: "docker"
lang: "pt"
order_index: 2
title: "Imagens"
description: "Aprenda a ler uma referência de imagem e verificar se a imagem está disponível localmente."
meta_title: "Imagens - Docker"
meta_description: "Leia os nomes e as tags de imagens do Docker, entenda registros e downloads e diferencie a lista de imagens da lista de contêineres."
meta_keywords: "imagens Docker, tags de imagem, registro de imagens, docker pull, docker image ls"
---

Uma imagem do Docker reúne um programa, seus arquivos e as configurações padrão. O Docker usa esse pacote como ponto de partida para um contêiner. Aqui você vai ler nomes de imagens e descobrir quais já estão no ambiente do Docker.

## Lendo o nome e a tag de uma imagem

Em `nginx:alpine`, `nginx` é o nome da imagem e `alpine` é a **tag**, um rótulo usado para selecionar uma versão ou variante específica. Neste caso, ela seleciona a variante baseada no Alpine Linux. Os dois-pontos separam o nome da tag. `nginx:alpine` e `nginx:latest` são referências diferentes com o mesmo nome de imagem.

:::single-choice{#docker-images-read-reference} Em `busybox:1.36`, qual parte é a tag?

::option[`busybox`]{#docker-images-reference-name explanation="BusyBox é o nome que aparece antes dos dois-pontos."}
::option[`busybox:1.36`]{#docker-images-reference-whole explanation="A referência completa inclui o nome da imagem e a tag."}
::option[`1.36`]{#docker-images-reference-tag .correct explanation="O texto após os dois-pontos é a tag que seleciona a imagem."}
:::

## Escolhendo uma tag

Quando você omite a tag de uma referência como `nginx`, o Docker usa `latest`. Esse nome é uma convenção. Quem publica a imagem determina para qual imagem a tag aponta e pode mudar isso depois. Ao escrever `nginx:alpine`, você indica a variante que quer usar. A imagem associada a essa tag também pode receber atualizações.

:::single-choice{#docker-images-default-tag} Uma pessoa usa `nginx` sem tag e presume que o Docker escolheu a versão mais recente. O que a referência realmente selecionou?

::option[A imagem apontada pela tag latest.]{#docker-images-default-latest .correct explanation="Sem uma tag explícita, o Docker usa latest. Quem publica a imagem escolhe para qual imagem essa tag aponta."}
::option[A imagem do Nginx publicada mais recentemente.]{#docker-images-default-newest explanation="O Docker usa a tag com o nome latest. Ele não ordena as imagens pela data de publicação."}
::option[A menor imagem do Nginx disponível.]{#docker-images-default-smallest explanation="O tamanho da imagem não determina a tag padrão. Escolha a variante desejada pelo nome."}
:::

## Baixando uma imagem

Um **registro** armazena imagens e as disponibiliza para download. Para referências como `nginx:alpine`, o Docker Hub é o registro padrão. Para baixar a imagem no ambiente Docker ao qual você se conectou, use `docker pull`. Esse download também é conhecido como **pull** da imagem.

```bash
$ docker pull nginx:alpine
```

Quando o comando termina com sucesso, a imagem fica disponível nesse ambiente. Iniciar um contêiner é uma etapa separada. Nos exemplos de terminal, `$` é o prompt.

:::single-choice{#docker-images-pull-result} O download de uma imagem terminou com sucesso. O que o Docker fez?

::option[Iniciou um contêiner que responde a solicitações web.]{#docker-images-pull-started explanation="O contêiner só é iniciado quando você o executa. O download deixa a imagem disponível."}
::option[Deixou a imagem disponível para uso nesse ambiente.]{#docker-images-pull-available .correct explanation="Você já pode usar a imagem baixada como base para um contêiner."}
::option[Enviou uma cópia da imagem para o registro.]{#docker-images-pull-uploaded explanation="O pull transfere a imagem do registro para o armazenamento local do Docker."}
:::

## Consultando as imagens locais

Use `docker image ls` para ver as imagens já disponíveis. O exemplo mostra apenas as colunas de nome e tag. O Docker chama a coluna de nome da imagem de `REPOSITORY`.

```text
$ docker image ls
REPOSITORY   TAG
nginx        alpine
busybox      1.36
```

A primeira linha mostra `nginx:alpine`. A tabela responde quais imagens estão presentes. O estado dos contêineres criados a partir delas aparece em outra lista.

![Terminal da LabEx mostrando docker pull e as colunas REPOSITORY e TAG de docker image ls](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-images/pull-and-list.png)

Na captura, a lista foi filtrada para mostrar apenas as duas referências usadas na lição.

:::single-choice{#docker-images-local-list} Qual referência aparece como disponível nessa saída?

::option[`busybox:latest`]{#docker-images-local-busybox-latest explanation="A linha de busybox mostra a tag 1.36. Nenhuma linha do exemplo mostra busybox com a tag latest."}
::option[`busybox:1.36`]{#docker-images-local-busybox .correct explanation="Combine busybox da coluna REPOSITORY com 1.36 da coluna TAG."}
::option[`nginx:1.36`]{#docker-images-local-nginx-mixed explanation="O nome e a tag devem vir da mesma linha. Aqui, 1.36 pertence à linha de busybox."}
:::

## Resumo

Agora você pode ler uma referência de imagem e verificar se ela aparece na lista local.

1. Identificar o nome e a tag de uma referência.
2. Explicar o que acontece quando você omite a tag.
3. Usar `docker pull` para baixar uma imagem de um registro.
4. Ler as colunas de nome e tag em `docker image ls`.
