---
lesson_id: "compose-environment-variables"
course_id: "docker-compose"
lang: "pt"
order_index: 5
title: "Variáveis de ambiente"
description: "Aprenda a distinguir um valor inserido no arquivo do Compose de um valor passado para o contêiner."
meta_title: "Variáveis de ambiente - Docker Compose"
meta_description: "Aprenda a distinguir um valor inserido no arquivo do Compose de um valor passado para o contêiner."
meta_keywords: "variáveis de ambiente, interpolação, Docker Compose, DevOps, Linux Journey"
---

Uma variável de ambiente é um valor com nome que um programa pode ler. O Compose pode usar variáveis de duas maneiras: para inserir um valor ao ler o arquivo e para passar valores a um programa dentro do contêiner.

## Como inserir um valor no arquivo

Salve o exemplo como `compose.env.yaml` na pasta de prática. A expressão `${PAGE_MODE:-demo}` usa o valor de `PAGE_MODE` se a variável estiver definida e não estiver vazia. Caso contrário, usa `demo`.

```yaml
services:
  toolbox:
    image: busybox:1.36
    environment:
      PAGE_MODE: "${PAGE_MODE:-demo}"
```

O Compose resolve a expressão antes de criar o contêiner. Isso se chama **interpolação**. Você pode encontrar a mesma técnica em outros arquivos, por exemplo, para escolher uma porta do host ou uma tag de imagem.

:::single-choice{#compose-environment-variables-interpolate-default} Se PAGE_MODE não estiver definida, que valor aparece na configuração exibida?

::option[A expressão tal como está no arquivo.]{#compose-environment-variables-interpolate-default-a explanation="O Compose resolve a expressão quando lê o arquivo."}
::option[Um nome de contêiner gerado automaticamente.]{#compose-environment-variables-interpolate-default-c explanation="O nome do contêiner e o valor da variável são configurações distintas."}
::option[Demo, o valor que vem depois do operador de valor padrão.]{#compose-environment-variables-interpolate-default-b .correct explanation="A expressão especifica demo como valor padrão."}
:::

## Como conferir o valor escolhido

Uma atribuição antes de um comando define a variável só para aquela execução. Faça isso para ver como a configuração fica com outro valor. O comando `config` exibe as configurações depois da interpolação, sem criar contêineres.

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml config
```

Procure `PAGE_MODE: review` no ambiente do serviço. O valor `review` é apenas para demonstração. Mantenha dados secretos fora das configurações de exemplo e da saída exibida.

:::single-choice{#compose-environment-variables-config-scope} A configuração exibida contém review. O que aconteceu até aqui?

::option[Um serviço já iniciou com esse valor.]{#compose-environment-variables-config-scope-b explanation="Exibir a configuração e iniciar um contêiner são operações separadas."}
::option[O Compose inseriu esse valor ao ler a configuração.]{#compose-environment-variables-config-scope-a .correct explanation="O comando config mostra a configuração com os valores resolvidos, antes de iniciar serviços."}
::option[Todos os contêineres existentes agora usam o valor.]{#compose-environment-variables-config-scope-c explanation="Esse comando não modifica contêineres em execução."}
:::

## Como passar um valor para o contêiner

A seção `environment` passa o valor escolhido para um novo contêiner. Use `printenv` para exibir o valor de dentro do contêiner criado para essa execução.

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml run --rm toolbox printenv PAGE_MODE
```

Você deve ver `review`. A interpolação escolheu o valor e a configuração de ambiente o passou para o contêiner. Uma variável usada apenas para escolher a porta do host não entra automaticamente no ambiente do programa.

:::single-choice{#compose-environment-variables-actual-value} Como conferir o valor que o programa dentro do contêiner de ferramentas recebe?

::option[Exibir PAGE_MODE de dentro do contêiner.]{#compose-environment-variables-actual-value-c .correct explanation="O ambiente do próprio programa mostra o valor recebido."}
::option[Ler apenas o valor padrão no arquivo original.]{#compose-environment-variables-actual-value-a explanation="Outro valor pode substituir o padrão do arquivo."}
::option[Encontrar o endereço IP do contêiner de ferramentas.]{#compose-environment-variables-actual-value-b explanation="O endereço não revela as configurações do programa."}
:::

## Resumo

Agora você consegue distinguir os dois usos das variáveis de ambiente.

1. Leia uma expressão com valor padrão em um arquivo do Compose.
2. Confira a configuração após a interpolação, antes de iniciar o contêiner.
3. Verifique o valor no ambiente do programa iniciado.
