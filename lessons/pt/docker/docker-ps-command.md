---
lesson_id: "docker-ps-command"
course_id: "docker"
lang: "pt"
order_index: 4
title: "docker ps"
description: "Aprenda a listar contêineres do Docker e saber quais estão em execução ou já terminaram."
meta_title: "docker ps - Docker"
meta_description: "Leia a saída de docker ps, encontre contêineres parados com docker ps -a e interprete nomes, estados e códigos de saída."
meta_keywords: "docker ps, listar contêineres Docker, contêineres parados, docker ps -a, estado do contêiner, códigos de saída"
---

O servidor web que você iniciou no Docker ainda está em execução? Use `docker ps` para verificar. Uma imagem reúne o programa e os arquivos de que ele precisa. Um contêiner é uma instância criada a partir dessa imagem. O comando mostra a lista de contêineres no momento da consulta.

## Listando os contêineres em execução

Por padrão, `docker ps` lista os contêineres em execução. Os exemplos mostram algumas colunas de um ambiente Docker já preparado, então você pode ler a saída sem configurar o Docker. No terminal, digite o comando que vem depois do prompt `$`.

```text
$ docker ps
IMAGE         STATUS         NAMES
nginx:alpine  Up 4 minutes   web
nginx:alpine  Up 30 seconds  demo
```

Se o Docker exibir apenas os cabeçalhos das colunas, a lista de contêineres em execução está vazia. O ambiente ainda pode ter contêineres parados.

:::single-choice{#docker-ps-running-list} Ao executar `docker ps`, o Docker mostra só os cabeçalhos. O que você pode concluir?

::option[Não há imagens disponíveis para execução.]{#docker-ps-running-list-images explanation="O comando lista contêineres. Pode haver imagens mesmo quando nenhum contêiner está em execução."}
::option[A lista de contêineres em execução está vazia.]{#docker-ps-running-list-empty .correct explanation="A lista padrão mostra os contêineres em execução. Ainda pode haver contêineres parados."}
::option[Não há contêineres parados para conferir.]{#docker-ps-running-list-stopped explanation="Contêineres parados ficam fora da seleção padrão. A lista vazia não informa se eles existem."}
:::

## Lendo nomes e estados

Comece pela coluna `NAMES` para localizar o contêiner desejado. As duas linhas mostram a mesma imagem, `nginx:alpine`, em `IMAGE`. Encontre `web` na última coluna e leia `STATUS` na mesma linha. `Up 4 minutes` significa que o contêiner está em execução há cerca de quatro minutos.

:::single-choice{#docker-ps-name-column} Qual linha corresponde a um contêiner que está em execução há cerca de 30 segundos?

::option[A linha com o nome `demo`.]{#docker-ps-name-demo .correct explanation="Encontre Up 30 seconds em STATUS e leia demo em NAMES na mesma linha."}
::option[A linha com o nome `web`.]{#docker-ps-name-web explanation="A linha de web mostra Up 4 minutes. Os contêineres usam a mesma imagem, mas foram iniciados em momentos diferentes."}
::option[As duas linhas com a imagem `nginx:alpine`.]{#docker-ps-name-image-reference explanation="Cada linha tem seu próprio estado. Usar a mesma imagem não implica a mesma hora de início."}
:::

## Incluindo contêineres que já terminaram

Se um contêiner que você esperava não aparecer, tente `docker ps -a`. A opção `-a` é a abreviação de `--all`. Ela inclui os contêineres parados que ainda existem. O exemplo também inclui uma tarefa de demonstração chamada `preview`.

```text
$ docker ps -a
IMAGE         STATUS                         NAMES
nginx:alpine  Up 4 minutes                   web
nginx:alpine  Up 30 seconds                  demo
busybox:1.36  Exited (0) 2 minutes ago       report
busybox:1.36  Exited (1) About a minute ago  preview
```

Um contêiner executa um programa principal, como um servidor web ou um script. `Exited` indica que esse programa parou. O número entre parênteses é o **código de saída**, o resultado que o programa informou ao terminar. Zero geralmente indica sucesso. Um código diferente de zero costuma indicar erro. A tarefa `report` mostra `Exited (0)`, o resultado esperado para uma tarefa concluída com sucesso.

![Terminal da LabEx com contêineres em execução e terminados, report com código 0 e preview com código 1](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-ps-command/running-and-exited.png)

A captura da LabEx mostra só os nomes e estados dos quatro contêineres de exemplo. Os tempos variam de acordo com o momento em que você executa o comando.

:::single-choice{#docker-ps-exit-code-reading} Pelo código de saída, em qual linha você investigaria um possível erro?

::option[`report`, porque terminou.]{#docker-ps-exit-code-report explanation="Uma tarefa curta pode parar depois de terminar. O código zero costuma indicar sucesso."}
::option[`demo`, porque iniciou mais recentemente entre os contêineres em execução.]{#docker-ps-exit-code-demo explanation="Up indica há quanto tempo o programa roda. Essa linha não tem código de saída."}
::option[`preview`, porque terminou com código 1.]{#docker-ps-exit-code-preview .correct explanation="Preview mostra Exited (1). Vale investigar esse resultado, embora o estado, por si só, não revele a causa."}
:::

## Escolhendo a próxima verificação

O código de saída ajuda a decidir o que investigar. Para ver se `preview` exibiu um erro, use `docker logs` seguido do nome. O comando mostra a saída que o Docker coletou desse contêiner.

```bash
$ docker logs preview
```

Se o servidor web estiver em execução, você também pode verificar se um visitante consegue abrir a página. Abra-a no computador que precisa acessá-la. `Up` descreve o programa dentro do contêiner. Uma solicitação bem-sucedida confirma que a página está acessível do computador usado no teste.

:::single-choice{#docker-ps-check-visitor-access} A página abre no computador que executa o Docker. Outra pessoa precisa abri-la de um computador diferente. Qual teste confirma se ela consegue acessar?

::option[Abrir a página no computador da outra pessoa.]{#docker-ps-next-check-visitor-browser .correct explanation="A solicitação testa a conexão que essa pessoa realmente vai usar."}
::option[Executar `docker ps` novamente no computador com Docker.]{#docker-ps-next-check-status-again explanation="A lista pode mostrar que web ainda está em execução. Para confirmar o acesso do outro computador, faça uma solicitação a partir dele."}
::option[Abrir a página de novo no computador com Docker.]{#docker-ps-next-check-host-browser explanation="Isso repete a verificação no primeiro computador. A conexão do outro pode se comportar de forma diferente."}
:::

## Resumo

Agora você pode usar a lista para localizar um contêiner, ler seu estado e escolher o que verificar depois.

1. Usar `docker ps` para listar contêineres em execução.
2. Localizar um contêiner pelo nome e ler seu estado.
3. Usar `docker ps -a` para incluir contêineres que já terminaram.
4. Consultar os logs ou fazer uma solicitação no navegador quando o estado não bastar.
