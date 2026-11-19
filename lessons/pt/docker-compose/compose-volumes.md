---
lesson_id: "compose-volumes"
course_id: "docker-compose"
lang: "pt"
order_index: 4
title: "Volumes"
description: "Entenda por que um volume nomeado conserva seus arquivos quando um contêiner é substituído."
meta_title: "Volumes - Docker Compose"
meta_description: "Entenda por que um volume nomeado conserva seus arquivos quando um contêiner é substituído."
meta_keywords: "volumes nomeados, armazenamento persistente, Docker Compose, DevOps, Linux Journey"
---

Um contêiner pode gravar arquivos na própria camada gravável. Se você remover o contêiner, o Docker remove essa camada junto. Um **volume nomeado** é um espaço de armazenamento que o Docker gerencia separadamente. Você pode montar o mesmo volume no contêiner que substituir o anterior.

## Como definir um volume para a prática

Salve este exemplo separado como `compose.volume.yaml` na pasta de prática. Ele monta o armazenamento chamado `notes` no caminho `/data` dentro do contêiner de ferramentas. A seção `volumes` no fim do arquivo declara o volume nomeado.

```yaml
services:
  toolbox:
    image: busybox:1.36
    volumes:
      - notes:/data
volumes:
  notes:
```

A definição do serviço indica onde o volume é montado dentro do contêiner. A declaração no nível principal indica que o Compose deve gerenciar o volume junto com o projeto.

:::single-choice{#compose-volumes-attached-path} Qual caminho dentro do contêiner de ferramentas usa o volume nomeado?

::option[/notes.]{#compose-volumes-attached-path-b explanation="Notes é o nome do volume. O caminho de montagem no contêiner vem depois dos dois-pontos."}
::option[/data.]{#compose-volumes-attached-path-a .correct explanation="O lado direito de notes:/data indica o caminho no contêiner."}
::option[Todos os caminhos do contêiner.]{#compose-volumes-attached-path-c explanation="O volume fica montado apenas no diretório configurado."}
:::

## Como gravar e ler com contêineres diferentes

A opção `-f` seleciona o outro arquivo, e `-p` dá a ele um nome de projeto distinto. O comando `run --rm` cria um contêiner para uma única execução e o remove quando termina. Execute estes comandos na pasta de prática isolada. O primeiro sobrescreve o arquivo de teste em `/data/note.txt`.

```bash
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox sh -c 'echo ready > /data/note.txt'
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox cat /data/note.txt
```

O segundo contêiner deve exibir `ready`. Ele monta o mesmo volume que o primeiro.

:::single-choice{#compose-volumes-persistence} Como o segundo contêiner consegue ler o arquivo depois que o primeiro foi removido?

::option[Os dois montaram o mesmo volume nomeado.]{#compose-volumes-persistence-b .correct explanation="O arquivo foi gravado no armazenamento separado montado em /data."}
::option[Os dois contêineres preservaram a camada gravável do primeiro.]{#compose-volumes-persistence-a explanation="A camada do primeiro foi removida junto com o contêiner."}
::option[O BusyBox acrescentou o arquivo automaticamente à imagem.]{#compose-volumes-persistence-c explanation="Executar um contêiner deixa a imagem original como estava."}
:::

![Dois contêineres de ferramentas distintos gravam e leem o mesmo arquivo em um volume nomeado](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-volumes/persisted-note.png)

## Como escolher quais dados preservar

Um arquivo como `/tmp/note.txt`, fora do diretório montado, fica no contêiner se não houver outro armazenamento montado nesse caminho. Confira os caminhos antes de assumir que um arquivo será conservado. Excluir o volume pode apagar seus dados. Um backup é uma cópia separada que permite restaurá-los se você perder o volume.

:::single-choice{#compose-volumes-inside-mount} Que arquivo o próximo contêiner de ferramentas verá por meio deste volume?

::option[/tmp/note.txt, da camada gravável do primeiro contêiner de ferramentas.]{#compose-volumes-inside-mount-a explanation="Esse caminho fica fora do ponto de montagem configurado."}
::option[Um arquivo armazenado em um volume com outro nome.]{#compose-volumes-inside-mount-b explanation="O novo contêiner precisa montar esse outro volume para ver o arquivo."}
::option[/data/note.txt, que o primeiro contêiner de ferramentas gravou.]{#compose-volumes-inside-mount-c .correct explanation="A montagem em /data dá aos dois contêineres acesso ao mesmo arquivo armazenado."}
:::

## Resumo

Agora você consegue explicar por que um arquivo pode continuar disponível depois que o contêiner que o gravou é removido.

1. Identifique o nome do volume e o caminho de montagem.
2. Leia o arquivo em outro contêiner para verificar que ele foi conservado.
3. Distinga a exclusão de um volume da substituição de um contêiner.
