---
lesson_id: "docker-run-command"
course_id: "docker"
lang: "pt"
order_index: 3
title: "docker run"
description: "Aprenda como o Docker cria e inicia contêineres a partir de imagens com docker run."
meta_title: "docker run - Docker"
meta_description: "Leia um comando docker run, escolha um nome para o contêiner e diferencie uma tarefa curta em primeiro plano de um servidor em segundo plano."
meta_keywords: "docker run, iniciar contêiner Docker, nome de contêiner, primeiro plano, segundo plano"
---

Você já tem a imagem de um servidor web. Para iniciar o servidor, use `docker run` para criar e iniciar um contêiner a partir dessa imagem. Comece com um comando rápido para ver quando o terminal volta a aceitar comandos.

## Executando uma tarefa curta

BusyBox é uma imagem pequena com comandos básicos do Linux. No exemplo, `echo` exibe uma mensagem. Coloque a referência da imagem antes do comando que você quer executar no contêiner. Se a imagem não estiver disponível, o Docker normalmente a baixa. O `$` marca o prompt do terminal. Se o Docker precisar baixar a imagem, talvez apareçam mensagens de download antes da linha mostrada.

```text
$ docker run busybox:1.36 echo Hello
Hello
```

A saída aparece no terminal. Quando `echo` termina, o contêiner para e o prompt volta.

:::single-choice{#docker-run-command-short-task} O que é executado dentro do contêiner neste exemplo?

::option[`busybox:1.36` como comando do shell.]{#docker-run-command-short-image explanation="BusyBox é a imagem que fornece as ferramentas. O comando vem depois da referência."}
::option[`echo Hello` com as ferramentas da imagem.]{#docker-run-command-short-echo .correct explanation="Depois da referência da imagem vêm o comando echo e o texto que ele deve exibir."}
::option[`docker run` como um segundo comando do Docker.]{#docker-run-command-short-docker explanation="Você executa docker run no terminal. Ele inicia o comando dentro do contêiner."}
:::

## Dando um nome ao contêiner

Use `--name` antes da referência da imagem para dar um nome fácil de reconhecer. Esse comando chama de `report` o contêiner da tarefa curta.

```bash
$ docker run --name report busybox:1.36 echo Ready
```

Um contêiner conserva seu nome mesmo depois de parar. Para criar outro contêiner no mesmo ambiente Docker, escolha um nome que esteja livre.

:::single-choice{#docker-run-command-name-choice} Report terminou, mas o contêiner ainda existe. Você quer criar um segundo contêiner com a mesma imagem. O que pode mudar?

::option[Usar outro nome de contêiner e manter a referência da imagem.]{#docker-run-command-name-new .correct explanation="Com um nome livre, o Docker pode criar um contêiner separado a partir da mesma imagem."}
::option[Mudar a tag da imagem e manter o nome do contêiner.]{#docker-run-command-name-change-tag explanation="O contêiner original conserva o nome mesmo se você escolher outra imagem."}
::option[Mudar a mensagem e manter o nome do contêiner.]{#docker-run-command-name-change-message explanation="A mensagem é a entrada de echo. Mudá-la não libera o nome report."}
:::

## Iniciando um servidor em segundo plano

Uma imagem pode definir um comando padrão. A imagem `nginx:alpine` inicia um servidor web se você não informar um comando depois da referência. Use `-d` para executar o contêiner **em segundo plano** e recuperar o prompt enquanto o servidor continua funcionando.

```bash
$ docker run -d --name web nginx:alpine
```

O Docker exibe um ID, um identificador longo do contêiner que iniciou. Na próxima lição você vai verificar se o servidor ainda está em execução.

![Terminal da LabEx mostrando Hello e Ready de tarefas curtas e o ID de um servidor iniciado em segundo plano](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-run-command/foreground-and-detached.png)

As tarefas curtas exibem suas mensagens no terminal. O servidor em segundo plano retorna um ID de contêiner.

:::single-choice{#docker-run-command-detach-meaning} O Docker exibe um ID e o prompt volta. O que esse modo permite fazer?

::option[Usar o terminal apenas depois que o servidor parar.]{#docker-run-command-detach-wait explanation="O modo em segundo plano devolve o prompt enquanto o servidor continua em execução."}
::option[Deixar a imagem pronta sem iniciar o servidor.]{#docker-run-command-detach-skip explanation="O Docker também inicia o contêiner quando ele roda em segundo plano."}
::option[Usar o terminal enquanto o servidor está em execução.]{#docker-run-command-detach-continue .correct explanation="O modo em segundo plano devolve o controle do terminal depois que o contêiner é iniciado."}
:::

## Reconhecendo um novo contêiner

Cada execução bem-sucedida de `docker run` cria um contêiner. Ao usar novamente a imagem do servidor com um nome livre, o Docker cria um segundo contêiner. O primeiro mantém seu nome e estado.

:::single-choice{#docker-run-command-second-instance} Web está em execução. O que `docker run -d --name demo nginx:alpine` faz se o nome demo estiver livre?

::option[Renomeia o contêiner web em execução para demo.]{#docker-run-command-second-rename explanation="Docker run cria um contêiner. O contêiner web original mantém o nome."}
::option[Adiciona demo como mais uma tag da imagem.]{#docker-run-command-second-tag explanation="A opção dá nome a um contêiner. A referência da imagem continua sendo nginx:alpine."}
::option[Inicia outro contêiner com o nome demo.]{#docker-run-command-second-new .correct explanation="O Docker cria um novo contêiner com essa imagem e atribui o nome demo."}
:::

Para praticar como iniciar um contêiner e observar a saída, experimente [Seu primeiro laboratório de Docker](https://labex.io/labs/docker-your-first-docker-lab-92719).

## Resumo

Agora você pode ler um comando docker run e prever o que o Docker vai criar.

1. Identificar a imagem e o comando opcional que é executado no contêiner.
2. Usar `--name` para identificar um contêiner mais tarde.
3. Descrever o que acontece quando uma tarefa curta termina.
4. Usar `-d` para voltar ao prompt enquanto o servidor funciona.
