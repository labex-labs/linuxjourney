---
lesson_id: "compose-service-discovery"
course_id: "docker-compose"
lang: "pt"
order_index: 3
title: "Descoberta de serviços"
description: "Entenda como os serviços do Compose se encontram pelo nome e como o host usa uma porta publicada."
meta_title: "Descoberta de serviços - Docker Compose"
meta_description: "Entenda como os serviços do Compose se encontram pelo nome e como o host usa uma porta publicada."
meta_keywords: "descoberta de serviços, rede do Compose, porta publicada, Docker Compose, DevOps, Linux Journey"
---

Um navegador no host do Docker chega ao serviço web pelo endereço publicado. Outro contêiner no projeto usa um caminho diferente. Em geral, o Compose conecta os serviços de um projeto a uma rede compartilhada, onde eles podem se localizar pelo nome de serviço.

## Como pedir a página pelo contêiner de ferramentas

Volte à pasta de prática que contém `compose.yaml`. Se o contêiner de ferramentas parou desde a lição anterior, inicie-o novamente com `docker compose start toolbox`. Com os dois serviços rodando, use `docker compose exec` para executar um comando dentro do contêiner de ferramentas que já existe. O comando `wget` do BusyBox solicita a página. A opção `-q` oculta as mensagens de progresso, e `-O -` exibe a página no terminal.

```bash
$ docker compose exec -T toolbox wget -q -O - http://web:80/
```

A opção `-T` impede a alocação de um terminal interativo. A URL indica o nome do serviço web e a porta no contêiner. Se a requisição der certo, você verá o HTML da página do Nginx.

:::single-choice{#compose-service-discovery-sibling-url} Que endereço outro serviço na mesma rede do Compose deve usar para chegar ao contêiner web?

::option[http://web:80/]{#compose-service-discovery-sibling-url-c .correct explanation="Na rede compartilhada, web corresponde ao serviço indicado. A porta 80 chega ao programa que recebe as requisições."}
::option[http://127.0.0.1:8080/]{#compose-service-discovery-sibling-url-a explanation="O endereço de loopback aponta para o ambiente de rede do próprio serviço que faz a requisição."}
::option[http://web:8080/]{#compose-service-discovery-sibling-url-b explanation="Neste exemplo, o servidor web escuta na porta 80 dentro da rede."}
:::

![HTML exibido no contêiner de ferramentas após uma requisição pelo nome do serviço web](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-discovery/internal-request.png)

## Como escolher o endereço no host

No host do Docker, abra `http://127.0.0.1:8080/` se você manteve o mapeamento original. Se mudou a porta do host na lição anterior, use a nova porta no endereço do navegador. O contêiner de ferramentas continua usando `http://web:80/` porque se conecta de dentro da rede do Compose, onde o nome de serviço `web` está disponível.

:::single-choice{#compose-service-discovery-host-url} Imagine que você troque a porta do lado do host para 8081. Qual endereço do exemplo também precisa mudar?

::option[A URL que o contêiner de ferramentas usa para acessar web na porta 80.]{#compose-service-discovery-host-url-b explanation="Esse caminho ainda segue direto para a porta em que o servidor web escuta no contêiner."}
::option[Os dois endereços do exemplo.]{#compose-service-discovery-host-url-c explanation="Só a porta do lado do host mudou."}
::option[O endereço usado pelo navegador no host.]{#compose-service-discovery-host-url-a .correct explanation="O navegador se conecta pela nova porta publicada no host."}
:::

## Como usar um nome de serviço estável

Quando um contêiner é substituído, seu endereço de rede pode mudar. O nome do serviço no Compose continua igual. O cliente pode resolver o nome novamente e se reconectar. Uma conexão que estava aberta com o contêiner anterior pode cair.

:::single-choice{#compose-service-discovery-replacement} O contêiner web foi recriado e recebeu outro endereço. O que o contêiner de ferramentas pode usar na próxima requisição?

::option[O endereço antigo copiado do contêiner.]{#compose-service-discovery-replacement-a explanation="Um novo contêiner pode receber outro endereço de rede."}
::option[O mesmo nome de serviço web e a mesma porta do contêiner.]{#compose-service-discovery-replacement-b .correct explanation="Na rede do projeto, o nome pode indicar o contêiner atual."}
::option[O nome do próprio contêiner de ferramentas.]{#compose-service-discovery-replacement-c explanation="Esse outro nome identifica o serviço que executa o comando."}
:::

## Resumo

Agora você consegue escolher um endereço de serviço conforme a origem da requisição.

1. Na rede do projeto, use o nome do serviço e a porta do contêiner.
2. No navegador do host, use o endereço publicado.
3. Resolva o nome do serviço novamente após substituir o contêiner.
