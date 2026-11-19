---
lesson_id: "web-http-requests-responses"
course_id: "web-security"
lang: "pt"
order_index: 1
title: "Requisições e respostas HTTP"
description: "Aprenda a identificar método, caminho, status e tipo de conteúdo em uma troca HTTP."
meta_title: "Requisições e respostas HTTP - Segurança web"
meta_description: "Aprenda a identificar método, caminho, status e tipo de conteúdo em uma troca HTTP."
meta_keywords: "requisições HTTP, respostas HTTP, segurança web, cibersegurança, Linux Journey"
---

O navegador ou outro cliente pede algo a um servidor web ao enviar uma **requisição HTTP**. O servidor devolve uma **resposta HTTP**. Ler as duas mensagens mostra o que o cliente pediu e o que o servidor retornou.

## Lendo a requisição

Veja uma requisição HTTP/1.1 curta. `GET` é o método, que descreve a ação solicitada pelo cliente. `/health` é o caminho. O cabeçalho `Host` identifica o site ao qual o cliente se dirige.

```http
GET /health HTTP/1.1
Host: site.example
```

Um **cabeçalho** é um campo com nome e valor que leva informações sobre a mensagem. O método e o caminho ficam na primeira linha da requisição.

:::single-choice{#web-http-requests-responses-request-path} O que o cliente solicita ao servidor?

::option[Um arquivo chamado HTTP/1.1.]{#web-http-requests-responses-request-path-b explanation="Esse campo indica a versão do protocolo."}
::option[O recurso em /health.]{#web-http-requests-responses-request-path-a .correct explanation="O caminho aparece depois de GET na primeira linha."}
::option[Um recurso em /site.example.]{#web-http-requests-responses-request-path-c explanation="O cabeçalho Host identifica o site. O caminho aparece na primeira linha."}
:::

## Lendo uma resposta

Em uma pasta de prática vazia, crie uma página e inicie um servidor HTTP do Python em loopback. O redirecionamento grava a página. Deixe o servidor em execução nesse terminal até a requisição terminar. Depois, encerre-o com Ctrl+C.

```bash
$ mkdir web-demo
$ printf '%s\n' ready > web-demo/health.txt
$ python3 -m http.server 8094 --bind 127.0.0.1 --directory web-demo
```

Em outro terminal na mesma máquina, execute `curl -i`. A opção inclui os cabeçalhos da resposta antes do conteúdo.

```bash
$ curl -i http://127.0.0.1:8094/health.txt
```

A resposta começa com uma linha que inclui o **código de status**. O código `200` indica sucesso para essa requisição. Uma linha vazia separa os cabeçalhos do corpo. O cabeçalho `Content-Type` indica como o cliente deve interpretar o corpo, por exemplo, como texto simples.

:::single-choice{#web-http-requests-responses-response-parts} Qual parte ajuda o cliente a decidir como exibir o conteúdo?

::option[O cabeçalho Content-Type da resposta.]{#web-http-requests-responses-response-parts-b .correct explanation="Ele descreve o tipo do corpo da resposta."}
::option[O nome do host na requisição original.]{#web-http-requests-responses-response-parts-a explanation="Ele identifica o site com o qual o cliente entrou em contato."}
::option[Apenas o caminho.]{#web-http-requests-responses-response-parts-c explanation="O caminho identifica o recurso sem especificar o formato retornado."}
:::

![Resposta HTTP na LabEx com status 200, tipo de conteúdo de texto e ready no corpo](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-http-requests-responses/http-response.png)

## Comparando dois resultados

Uma resposta `404` informa que o servidor não encontrou o recurso solicitado ou optou por não indicar que ele existe. Um site pode retornar 200 em um caminho e 404 em outro. Use o método e o caminho exatos ao comparar os resultados.

:::single-choice{#web-http-requests-responses-health-scope} Uma requisição a /health recebe 200. O que você pode concluir sobre /welcome?

::option[/welcome também retornou 200.]{#web-http-requests-responses-health-scope-a explanation="A amostra testou outro caminho."}
::option[O host estava inacessível.]{#web-http-requests-responses-health-scope-b explanation="A verificação de saúde recebeu uma resposta."}
::option[Você precisa consultar /welcome para saber o resultado.]{#web-http-requests-responses-health-scope-c .correct explanation="Os caminhos podem se comportar de maneiras diferentes."}
:::

Para praticar a verificação de cabeçalhos de resposta e de conectividade, faça [Como testar a conexão com um servidor usando curl no Linux](https://labex.io/tutorials/linux-how-to-test-server-connectivity-with-curl-in-linux-415082).

## Resumo

Agora você consegue interpretar as partes principais de uma troca HTTP simples.

1. Encontre o método, o caminho e o host da requisição.
2. Leia o status e o tipo de conteúdo da resposta.
3. Descreva o resultado da requisição exata que foi feita.
