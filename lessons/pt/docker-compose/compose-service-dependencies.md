---
lesson_id: "compose-service-dependencies"
course_id: "docker-compose"
lang: "pt"
order_index: 6
title: "Dependências entre serviços"
description: "Aprenda a distinguir a ordem de inicialização das dependências da capacidade de responder a requisições."
meta_title: "Dependências entre serviços - Docker Compose"
meta_description: "Aprenda a distinguir a ordem de inicialização das dependências da capacidade de responder a requisições."
meta_keywords: "dependências entre serviços, verificação de saúde, ordem de inicialização, Docker Compose, DevOps, Linux Journey"
---

Um programa auxiliar que depende de um servidor web pode enviar a primeira requisição cedo demais, mesmo se os dois iniciarem na ordem certa. Uma **verificação de saúde** é um teste curto executado pelo Docker para ver se o serviço consegue cumprir uma função, como responder a uma requisição HTTP.

## Como verificar se o serviço está pronto

Neste exemplo separado, a verificação roda dentro do contêiner web. Ela solicita a página local. Se a requisição passar, o Docker sabe que o servidor responde a partir daquele ponto.

```yaml
services:
  web:
    image: nginx:alpine
    healthcheck:
      test: ["CMD", "wget", "-q", "-O", "/dev/null", "http://127.0.0.1/"]
      interval: 3s
      timeout: 2s
      retries: 5
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
    depends_on:
      web:
        condition: service_healthy
```

Salve o exemplo como `compose.health.yaml` na mesma pasta de prática. A verificação se repete em intervalos e cada tentativa tem um limite de tempo. Ela testa uma resposta local dentro do contêiner web.

:::single-choice{#compose-service-dependencies-check-location} Onde wget é executado nessa verificação de saúde?

::option[Dentro do contêiner web.]{#compose-service-dependencies-check-location-c .correct explanation="O endereço de loopback é usado de dentro desse contêiner."}
::option[No navegador do host.]{#compose-service-dependencies-check-location-a explanation="O Docker executa o comando conforme a definição do serviço web."}
::option[Dentro do contêiner de ferramentas.]{#compose-service-dependencies-check-location-b explanation="A verificação está definida em web."}
:::

## Como aguardar uma dependência saudável

Com a condição `service_healthy`, o Compose aguarda uma verificação bem-sucedida antes de iniciar o contêiner de ferramentas que depende do servidor. Quando só a ordem de inicialização é definida, o serviço dependente pode iniciar assim que o servidor estiver rodando, mesmo antes que ele consiga responder a uma requisição.

```bash
$ docker compose -p journey-health -f compose.health.yaml up -d
$ docker compose -p journey-health -f compose.health.yaml ps
```

Procure um estado saudável na linha de web e confira se o contêiner de ferramentas está em execução.

:::single-choice{#compose-service-dependencies-ready-condition} O processo web iniciou, mas a requisição local ainda falha. Que condição deve fazer o contêiner de ferramentas esperar?

::option[Apenas a ordem de inicialização.]{#compose-service-dependencies-ready-condition-b explanation="Mesmo quando web inicia primeiro, pode levar um tempo para responder."}
::option[O modo em segundo plano.]{#compose-service-dependencies-ready-condition-c explanation="Esse modo muda a forma como o terminal espera. Ele não indica se o serviço está pronto."}
::option[A condição service_healthy.]{#compose-service-dependencies-ready-condition-a .correct explanation="Essa condição espera pelo resultado da verificação de saúde."}
:::

![Saída de status do Compose com o serviço web saudável e o contêiner de ferramentas em execução](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-dependencies/healthy-dependency.png)

## Como lidar com uma falha posterior

Uma condição de inicialização do Compose determina quando um serviço dependente vai começar a rodar. Um serviço que estava saudável pode deixar de responder depois. O cliente deve lidar com a falha da requisição e se reconectar quando a dependência voltar a ficar disponível. Consulte o estado do serviço e faça uma requisição direta para ver como ele se comporta agora.

:::single-choice{#compose-service-dependencies-later-failure} Uma requisição falha uma hora depois de iniciar os dois serviços. Que informação ajuda agora?

::option[Só a ordem de inicialização original.]{#compose-service-dependencies-later-failure-a explanation="Essa ordem descreve o que aconteceu na inicialização."}
::option[Um resultado recente da verificação de saúde e uma requisição do serviço dependente.]{#compose-service-dependencies-later-failure-b .correct explanation="Assim, você verifica o estado atual do serviço e o caminho usado pelo cliente."}
::option[O número de imagens no cache do Docker.]{#compose-service-dependencies-later-failure-c explanation="A disponibilidade das imagens diz pouco sobre a resposta de um serviço em execução."}
:::

## Como verificar de dois pontos diferentes

Uma verificação local bem-sucedida mostra o que o contêiner web alcança de dentro dele próprio. O contêiner de ferramentas ainda precisa da rede do projeto e de um endereço pelo qual possa acessar o serviço. Confira separadamente o resultado da verificação de saúde e a resposta à requisição feita do contêiner de ferramentas.

:::single-choice{#compose-service-dependencies-final-application} A verificação aparece em verde, mas uma requisição do contêiner de ferramentas falha. Qual comparação ajuda a localizar o problema?

::option[Consultar apenas o horário de início original.]{#compose-service-dependencies-final-application-b explanation="Esse horário não mostra quais caminhos estão funcionando agora."}
::option[Considerar as duas requisições bem-sucedidas porque a verificação de web está em verde.]{#compose-service-dependencies-final-application-c explanation="A verificação traz informações de um único ponto da rede."}
::option[Comparar a mesma requisição feita de dentro de web e do contêiner de ferramentas para web.]{#compose-service-dependencies-final-application-a .correct explanation="Você compara o resultado dentro do serviço com o caminho realmente usado pelo serviço dependente."}
:::

## Resumo

Agora você consegue usar uma verificação para avaliar se uma dependência está pronta.

1. Identifique o que uma verificação de saúde realmente observa.
2. Aguarde uma dependência saudável se a ordem de inicialização não for suficiente.
3. Confira o comportamento atual se um serviço falhar depois de iniciar.
