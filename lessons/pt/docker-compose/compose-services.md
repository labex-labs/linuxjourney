---
lesson_id: "compose-services"
course_id: "docker-compose"
lang: "pt"
order_index: 2
title: "Serviços do Compose"
description: "Aprenda a iniciar serviços do Compose e conferir o estado dos contêineres."
meta_title: "Serviços do Compose - Docker Compose"
meta_description: "Aprenda a iniciar serviços do Compose e conferir o estado dos contêineres."
meta_keywords: "serviços do Compose, estado dos contêineres, Docker Compose, DevOps, Linux Journey"
---

Use o `compose.yaml` da lição anterior, com `web` e `toolbox`. Os dois serviços pertencem ao mesmo **projeto** do Compose, o conjunto de recursos gerenciados juntos com essa configuração. Execute os comandos na pasta de prática.

## Como iniciar o projeto

Se a porta 8080 já estiver em uso, escolha outra porta livre do host em `compose.yaml`. Por exemplo, o contêiner `published-web` do curso de Docker usa a porta 8080 enquanto está em execução. Você pode deixá-lo rodando e usar o mapeamento `127.0.0.1:8081:80` no Compose se a porta 8081 estiver livre. Mantenha a porta 80 no contêiner e use a porta escolhida no host nas próximas requisições pelo navegador.

Use `docker compose up -d` para iniciar os serviços em segundo plano. O Compose cria os recursos necessários para o projeto e usa as configurações dos serviços para criar ou atualizar os contêineres.

```bash
$ docker compose up -d
```

:::single-choice{#compose-services-project-start} Você executa up -d nesta pasta de prática. Que configurações determinam o que será iniciado?

::option[Todas as imagens disponíveis no host do Docker.]{#compose-services-project-start-a explanation="O host pode guardar imagens que não fazem parte deste projeto."}
::option[Todos os contêineres que estiverem parados.]{#compose-services-project-start-c explanation="O Compose trabalha com o projeto que você pediu para iniciar."}
::option[Os serviços do arquivo do Compose selecionado.]{#compose-services-project-start-b .correct explanation="Neste exemplo, o Compose usa as definições de web e toolbox."}
:::

## Como ler a lista de serviços

Use `docker compose ps` para conferir o projeto. A coluna de serviços mostra os nomes definidos no arquivo YAML. O Docker também dá um nome a cada contêiner, que pode incluir o nome do projeto.

```bash
$ docker compose ps
```

Procure `web` e `toolbox` e confira seus estados. Um contêiner em execução indica que o programa está rodando naquele momento. Para verificar a resposta do servidor web, faça uma requisição no navegador.

:::single-choice{#compose-services-compose-list} O Compose indica que web está em execução. Qual verificação confirma diretamente que ele devolve a página esperada?

::option[Contar os serviços mostrados por config.]{#compose-services-compose-list-b explanation="A contagem não diz qual página o servidor web devolve."}
::option[Fazer uma requisição ao endereço web publicado.]{#compose-services-compose-list-a .correct explanation="A requisição permite verificar que página o servidor realmente entrega."}
::option[Conferir o nome de outro contêiner.]{#compose-services-compose-list-c explanation="O nome identifica o contêiner, mas não testa se o serviço responde."}
:::

![Saída de status do Compose com web e toolbox em execução e a porta 8080 publicada no host](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-services/project-status.png)

A captura usa a porta original do host, 8080. Se você escolheu outra, procure esse número no lado do host no mapeamento.

## Como verificar um serviço parado

O contêiner de ferramentas é temporário. Se o tempo de espera acabar ou você interromper o contêiner, acrescente `-a` para incluir os contêineres parados na lista do Compose. O comando abaixo interrompe o contêiner de ferramentas deste projeto de prática e deixa o serviço web em execução. Quando quiser continuar o curso, inicie o contêiner de ferramentas novamente.

```bash
$ docker compose stop toolbox
$ docker compose ps -a
$ docker compose start toolbox
```

:::single-choice{#compose-services-stopped-service} Onde procurar toolbox depois de interrompê-lo?

::option[Na saída de docker compose ps -a para este projeto.]{#compose-services-stopped-service-c .correct explanation="A opção inclui os contêineres parados do projeto."}
::option[Só na lista de imagens.]{#compose-services-stopped-service-a explanation="Depois de interromper o programa, o contêiner continua disponível para inspeção."}
::option[Na lista de contêineres de outro projeto.]{#compose-services-stopped-service-b explanation="Toolbox faz parte deste projeto."}
:::

Para praticar mais com contêineres e Compose, confira os [laboratórios de comandos do Docker](https://labex.io/courses/docker-command-labs).

## Resumo

Agora você consegue iniciar e conferir um grupo de serviços com um arquivo do Compose.

1. Inicie os serviços do projeto selecionado.
2. Localize o nome do serviço e confira seu estado.
3. Inclua serviços parados quando investigar o projeto.
