---
lesson_id: "docker-port-mapping"
course_id: "docker"
lang: "pt"
order_index: 5
title: "Mapeamento de portas"
description: "Aprenda a publicar uma porta do contêiner e encontrar o endereço que o navegador local deve usar."
meta_title: "Mapeamento de portas - Docker"
meta_description: "Leia um mapeamento de portas do Docker, diferencie a porta do host da porta do contêiner e descubra se uma solicitação foi feita na porta errada."
meta_keywords: "mapeamento de portas Docker, portas publicadas, docker run -p, porta do host, porta do contêiner"
---

Um servidor web pode estar em execução no contêiner e ainda assim o navegador precisa de um caminho para alcançá-lo. Uma **porta** é um número que ajuda o computador a direcionar solicitações recebidas ao serviço certo. O Docker pode publicar uma porta no host e encaminhar as solicitações para uma porta dentro do contêiner.

## Lendo um mapeamento de portas

Neste exemplo, o Nginx recebe solicitações web na porta 80 dentro do contêiner. O contêiner `web` do exemplo anterior foi criado sem uma porta publicada. Agora dê outro nome ao contêiner e use `-p` para definir o mapeamento na criação.

```bash
$ docker run -d --name published-web -p 127.0.0.1:8080:80 nginx:alpine
```

Leia `8080:80` como um encaminhamento da **porta do host** 8080 para a **porta do contêiner** 80. O navegador se conecta à porta do host e o servidor recebe a solicitação na porta do contêiner. `127.0.0.1` vincula esse mapeamento ao endereço de loopback do host, usado pelo computador para acessar a si mesmo.

Use um ambiente de prática isolado. Em versões do Docker Engine anteriores à 28.0.0, outros computadores no mesmo segmento de rede local podem conseguir acessar portas publicadas no localhost. [Publicação de portas no Docker](https://docs.docker.com/engine/network/port-publishing/)

:::single-choice{#docker-port-mapping-request-target} Em `127.0.0.1:9090:80`, com qual porta o navegador no host do Docker deve se conectar?

::option[Com a porta 9090 do host.]{#docker-port-mapping-target-outer .correct explanation="O número do meio indica a porta do host com a qual o navegador se conecta."}
::option[Com a porta 80 do host.]{#docker-port-mapping-target-inner explanation="A porta 80 é o destino dentro do contêiner."}
::option[Com a porta 9090 do contêiner.]{#docker-port-mapping-target-wrong-side explanation="Neste exemplo, o servidor recebe a solicitação na porta 80 do contêiner."}
:::

## Testando a partir do host

Abra `http://127.0.0.1:8080` no navegador do computador em que o Docker publicou a porta. Se o Docker estiver em outro computador, digitar `127.0.0.1` no seu notebook aponta para o próprio notebook. Em um laboratório no navegador, use o método de acesso fornecido pelo ambiente de prática.

:::single-choice{#docker-port-mapping-local-browser} O Docker publicou a porta 8080 em outro computador de laboratório. Para onde `127.0.0.1` aponta quando você digita esse endereço no navegador do notebook?

::option[Para o outro computador de laboratório.]{#docker-port-mapping-local-lab explanation="O endereço só aponta para aquele computador se for usado nele próprio."}
::option[Para o contêiner web no Docker.]{#docker-port-mapping-local-container explanation="O navegador usa o endereço do próprio computador. Um mapeamento de portas pode encaminhar a solicitação para um contêiner."}
::option[Para o seu notebook.]{#docker-port-mapping-local-laptop .correct explanation="O endereço de loopback indica o computador no qual o navegador está em execução."}
:::

## Verificando o que o Docker publicou

A coluna `PORTS` de `docker ps` pode mostrar o mapeamento. A seta vai do endereço e da porta do host até a porta do contêiner. O sufixo `/tcp` indica o protocolo de rede usado no mapeamento.

```text
$ docker ps
STATUS         PORTS                   NAMES
Up 2 minutes   127.0.0.1:8080->80/tcp   published-web
```

Uma linha também pode mostrar apenas `80/tcp`. Se não há endereço do host nem seta de encaminhamento, essa entrada não mostra uma porta publicada no host.

![Terminal da LabEx mostrando o encaminhamento da porta 8080 do host à porta 80 do contêiner e uma resposta HTTP 200](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-port-mapping/loopback-mapping.png)

Na captura, a lista foi filtrada para mostrar apenas `published-web`. A solicitação com `curl` parte do host do Docker e confirma que o endereço publicado responde corretamente.

:::single-choice{#docker-port-mapping-read-listing} Uma linha mostra `80/tcp` sem seta. O que essa entrada indica?

::option[O Docker publicou a porta 80 no host.]{#docker-port-mapping-listing-host explanation="Um mapeamento publicado informa uma porta do host e aponta para a porta do contêiner."}
::option[A entrada mostra a porta do contêiner, sem indicar uma porta publicada no host.]{#docker-port-mapping-listing-container .correct explanation="Ela informa a porta 80 dentro do contêiner. Não há endereço do host nem seta de encaminhamento."}
::option[O Docker publicou a porta 8080 no host.]{#docker-port-mapping-listing-default explanation="A entrada não contém uma porta do host. O Docker não deduz que a porta seja 8080."}
:::

## Escolhendo o endereço a testar

Se a página não abrir, compare o endereço que você digitou com o lado esquerdo do mapeamento. O estado `Up` diz o que está em execução. A seta mostra para onde o Docker encaminha as solicitações. Uma solicitação no navegador verifica se o servidor realmente retorna a página.

:::single-choice{#docker-port-mapping-correct-misdirected} No host do Docker, você tenta a porta 8080 e a página não abre. A linha mostra `127.0.0.1:8081->80/tcp`. O que você deve tentar em seguida?

::option[Abrir `http://127.0.0.1:80`.]{#docker-port-mapping-misdirected-80 explanation="A porta 80 está no lado do contêiner."}
::option[Abrir `http://127.0.0.1:8081`.]{#docker-port-mapping-misdirected-8081 .correct explanation="Use a porta publicada no host, à esquerda da seta."}
::option[Tentar `http://127.0.0.1:8080` novamente.]{#docker-port-mapping-misdirected-8080 explanation="A porta do host indicada na lista é 8081. Tentar 8080 não testa esse mapeamento."}
:::

## Resumo

Agora você pode ler um mapeamento de portas e escolher o endereço certo no navegador.

1. Distinguir a porta do host da porta do contêiner.
2. Explicar para onde `127.0.0.1` aponta.
3. Reconhecer um mapeamento publicado na lista de contêineres.
4. Usar a porta publicada no host para testar o serviço.
