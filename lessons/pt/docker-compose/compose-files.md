---
lesson_id: "compose-files"
course_id: "docker-compose"
lang: "pt"
order_index: 1
title: "Arquivos do Compose"
description: "Aprenda a localizar serviços, imagens, comandos e portas em um arquivo do Compose."
meta_title: "Arquivos do Compose - Docker Compose"
meta_description: "Aprenda a localizar serviços, imagens, comandos e portas em um arquivo do Compose."
meta_keywords: "arquivos do Compose, serviços, Docker Compose, DevOps, Linux Journey"
---

Para rodar um servidor web e seu programa auxiliar uma só vez, dá para usar comandos separados. Um **arquivo do Compose** reúne as configurações para que você consiga iniciar os mesmos serviços de novo. Neste curso, você vai usar o Docker com o plug-in do Compose, que fornece o comando `docker compose`.

## Como definir dois serviços

Crie uma pasta de prática chamada `journey-compose` e salve o exemplo abaixo como `compose.yaml`. Um **serviço** descreve como o Compose deve executar um contêiner. Este arquivo define um servidor web e um pequeno contêiner de ferramentas que fica em execução para as verificações seguintes.

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "127.0.0.1:8080:80"
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
```

Use espaços para fazer o recuo. As chaves recuadas abaixo de `web` pertencem a esse serviço. O hífen em `ports` inicia um item da lista. Os colchetes de `command` também formam uma lista, que neste caso contém o nome do programa e seu argumento.

:::single-choice{#compose-files-service-images} Qual serviço usa a imagem do BusyBox?

::option[O serviço web.]{#compose-files-service-images-a explanation="A linha da imagem de web indica nginx."}
::option[O serviço toolbox.]{#compose-files-service-images-c .correct explanation="O campo image de toolbox indica busybox:1.36."}
::option[Os dois serviços.]{#compose-files-service-images-b explanation="Cada serviço tem sua própria configuração de imagem."}
:::

## Como ler a configuração do serviço web

O serviço web publica a porta 80 do contêiner na porta 8080 do host. Depois que o serviço iniciar, uma requisição a `http://127.0.0.1:8080` na máquina que executa o Docker pode chegar ao Nginx. O contêiner de ferramentas não publica nenhuma porta. O comando `sleep` o mantém em execução por 3.600 segundos durante a prática.

:::single-choice{#compose-files-mapping-owner} Que parte do arquivo define como o navegador no host do Docker chega ao Nginx?

::option[A configuração ports em web.]{#compose-files-mapping-owner-a .correct explanation="Esse item associa o endereço e a porta do host ao contêiner web."}
::option[A tag da imagem em toolbox.]{#compose-files-mapping-owner-b explanation="Esse ajuste seleciona a imagem do contêiner de ferramentas."}
::option[O argumento de sleep em toolbox.]{#compose-files-mapping-owner-c explanation="O argumento determina o tempo de execução desse programa."}
:::

## Como conferir a configuração interpretada

Execute este comando na pasta que contém o arquivo. Digite o que aparece depois do símbolo `$` do prompt. O Compose lê `compose.yaml` e mostra a configuração que interpretou. Procure as entradas `web` e `toolbox`. Na saída, algumas configurações abreviadas podem aparecer de forma mais detalhada.

```bash
$ docker compose config
```

:::single-choice{#compose-files-config-scope} O comando exibe os dois serviços sem erro. O que você verificou?

::option[Os dois contêineres iniciaram.]{#compose-files-config-scope-a explanation="O comando lê as configurações e as exibe."}
::option[O navegador recebeu uma resposta bem-sucedida.]{#compose-files-config-scope-c explanation="Você pode testar uma requisição depois que o servidor estiver em execução."}
::option[O Compose consegue ler as duas definições de serviço.]{#compose-files-config-scope-b .correct explanation="Você pode conferir a configuração interpretada antes de iniciar os serviços."}
:::

## Resumo

Agora você consegue identificar as partes de um arquivo do Compose simples.

1. Leia os nomes e as referências de imagem em services.
2. Relacione a configuração de cada serviço ao contêiner que ela descreve.
3. Confira a configuração interpretada com docker compose config.
