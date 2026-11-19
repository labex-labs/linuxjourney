---
lesson_id: "deployment-health-checks"
course_id: "deployment"
lang: "pt"
order_index: 4
title: "Verificações de saúde do serviço"
description: "Aprenda a combinar uma verificação de processo, uma de serviço e uma requisição de cliente após a implantação."
meta_title: "Verificações de saúde do serviço - Implantação"
meta_description: "Aprenda a combinar uma verificação de processo, uma de serviço e uma requisição de cliente após a implantação."
meta_keywords: "verificação de saúde, health checks, implantação, DevOps, Linux Journey"
---

Um programa pode estar em execução logo após ser iniciado e ainda levar algum tempo para ficar pronto. Verifique o serviço em etapas para entender o que cada resultado confirma.

## Verificando o processo

Uma lista de contêineres pode mostrar que o programa principal está em execução. Isso responde à primeira pergunta sobre uma implantação recente. Ainda falta descobrir se o programa terminou de inicializar e se um navegador consegue acessá-lo.

:::single-choice{#deployment-health-checks-process-scope} O contêiner novo aparece como Up. O que você pode concluir?

::option[Os visitantes certamente estão recebendo a página nova.]{#deployment-health-checks-process-scope-a explanation="O estado de um contêiner não informa o que aconteceu com a requisição de um visitante."}
::option[O programa principal do contêiner estava em execução na hora da verificação.]{#deployment-health-checks-process-scope-b .correct explanation="Up indica o estado do processo."}
::option[Todas as dependências passaram pela verificação.]{#deployment-health-checks-process-scope-c explanation="A lista não mostra resultados sobre as dependências."}
:::

## Verificando um endpoint do serviço

Um **endpoint** é um endereço com um caminho que o serviço atende. Escolha um caminho que corresponda ao comportamento que você quer verificar. Para praticar localmente, use uma pasta de exercícios vazia. O redirecionamento grava o arquivo de versão. Deixe o servidor Python rodando no endereço de loopback nesse terminal e encerre com Ctrl+C ao terminar.

```bash
$ mkdir site
$ printf '%s\n' 2 > site/version.txt
$ python3 -m http.server 8091 --bind 127.0.0.1 --directory site
```

Em outro terminal, solicite o arquivo de versão. No curl, a opção `-f` trata respostas de erro HTTP como falhas. Já `-sS` suprime o medidor de progresso, mantém as mensagens de erro e permite que o conteúdo da resposta apareça.

```bash
$ curl -fsS http://127.0.0.1:8091/version.txt
```

O resultado esperado no exercício é `2`. Conseguir ler o arquivo confirma apenas uma parte do funcionamento do site.

:::single-choice{#deployment-health-checks-endpoint-mismatch} A requisição funciona e imprime 1. O que você deve investigar?

::option[Qual versão está respondendo naquele endereço.]{#deployment-health-checks-endpoint-mismatch-a .correct explanation="A conexão funcionou, mas a versão observada é diferente da esperada."}
::option[Por que o curl não consegue se conectar.]{#deployment-health-checks-endpoint-mismatch-b explanation="O valor retornado mostra que houve conexão e resposta."}
::option[Se há um número no nome do serviço.]{#deployment-health-checks-endpoint-mismatch-c explanation="O nome do serviço não indica qual versão respondeu."}
:::

![Endpoint de versão em loopback retornando a versão 2 no servidor de prática da LabEx](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-health-checks/version-response.png)

## Verificando a partir do local do cliente

Se a requisição funcionar no host do serviço, repita uma verificação segura a partir de onde os usuários costumam se conectar. Um balanceador de carga, um proxy ou uma regra de rede pode mudar o caminho da requisição. Anote o endereço verificado e a resposta recebida. Se o resultado divergir da release, continue investigando a implantação.

:::single-choice{#deployment-health-checks-user-path} Uma requisição local retorna 2, mas o endereço público de teste retorna 1. O que seria mais útil verificar em seguida?

::option[A quantidade de linhas que a requisição local imprimiu.]{#deployment-health-checks-user-path-a explanation="A quantidade de linhas não identifica o que atende o endereço público."}
::option[Apenas a mesma requisição local mais uma vez.]{#deployment-health-checks-user-path-b explanation="O caminho local já retornou a versão 2."}
::option[Qual versão do serviço recebe as requisições pela rota pública.]{#deployment-health-checks-user-path-c .correct explanation="Os dois caminhos retornaram respostas diferentes."}
:::

## Resumo

Agora você consegue identificar o que cada verificação confirma depois da implantação.

1. Confirme se o programa principal está em execução.
2. Consulte um endpoint que informe a versão esperada.
3. Verifique também o caminho que os usuários percorrem.
