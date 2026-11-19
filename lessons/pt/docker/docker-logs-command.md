---
lesson_id: "docker-logs-command"
course_id: "docker"
lang: "pt"
order_index: 6
title: "docker logs"
description: "Aprenda a ler a saída coletada de um contêiner e usá-la para escolher o próximo passo da investigação."
meta_title: "docker logs - Docker"
meta_description: "Consulte logs de contêineres em execução ou terminados, veja as últimas linhas e diferencie erros da aplicação do estado do contêiner."
meta_keywords: "docker logs, logs de contêiner, diagnóstico Docker, erros de inicialização, últimos logs"
---

Um contêiner chamado `preview` terminou. Na lista de contêineres, você encontra o estado e o código de saída. Para descobrir o que o programa informou, veja a saída que o Docker coletou desse contêiner.

## Escolhendo o contêiner

Passe o nome do contêiner para `docker logs`. O comando consegue ler a saída armazenada de um contêiner parado que ainda existe. Neste exemplo, uma tarefa curta tentou ler um arquivo em `/site/title.txt` antes de parar.

```text
$ docker logs preview
cat: can't open '/site/title.txt': No such file or directory
```

Aqui, `cat` é o programa que tentou ler o arquivo. A mensagem indica o caminho que ele não conseguiu encontrar dentro do contêiner.

:::single-choice{#docker-logs-command-read-exited} Preview e report usaram a mesma imagem. Qual comando lê a saída de preview?

::option[`docker logs report`]{#docker-logs-command-exited-report explanation="O nome seleciona um contêiner. Report identifica outra execução."}
::option[`docker logs busybox:1.36`]{#docker-logs-command-exited-image explanation="Essa é a referência da imagem. Os logs pertencem a um contêiner criado a partir dela."}
::option[`docker logs preview`]{#docker-logs-command-exited-preview .correct explanation="O comando usa o nome do contêiner cuja saída você quer consultar."}
:::

## Lendo a mensagem no contexto

Os logs guardam mensagens escritas pelo programa. Uma mensagem de inicialização pode indicar que o programa começou a aceitar solicitações. Um erro pode mostrar qual operação ele não conseguiu concluir. Neste exemplo, a mensagem aponta para um caminho ausente em `preview`. Confira se o contêiner deveria ter um arquivo exatamente nesse caminho. A mensagem indica por onde começar.

:::single-choice{#docker-logs-command-error-boundary} O que a mensagem de arquivo ausente permite afirmar?

::option[O arquivo está ausente em todos os diretórios do host.]{#docker-logs-command-error-host-path explanation="O programa buscou um caminho dentro do contêiner. A mensagem não descreve todos os arquivos do host."}
::option[O programa não encontrou o arquivo indicado dentro de preview.]{#docker-logs-command-error-container-path .correct explanation="A mensagem informa o resultado da busca feita pelo programa que rodou em preview."}
::option[O navegador do host usou uma porta que não foi publicada.]{#docker-logs-command-error-network explanation="A mensagem é sobre a busca pelo arquivo. Ela não informa a porta usada pelo navegador."}
:::

## Consultando a saída recente

Para um contêiner com muitas linhas de saída, use `--tail` seguido de um número. O Docker retorna até esse número de linhas, contando do fim da saída coletada. Comece com poucas linhas. Se o primeiro erro estiver antes delas, aumente o limite.

```bash
$ docker logs --tail 5 web
```

![Terminal da LabEx mostrando o erro de arquivo ausente em preview e as cinco últimas linhas de web](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-logs-command/preview-and-tail.png)

Os dois comandos consultam contêineres diferentes. Na execução da LabEx, `preview` mostra a falta do arquivo e `web` informa que o Nginx iniciou.

:::single-choice{#docker-logs-command-tail-choice} Você quer ver só as duas linhas mais recentes disponíveis de web. Qual comando serve?

::option[`docker logs --tail 2 web`]{#docker-logs-command-tail-two .correct explanation="Tail 2 pede até duas linhas do fim da saída desse contêiner."}
::option[`docker logs --tail 5 web`]{#docker-logs-command-tail-five explanation="Esse comando pede até cinco linhas, então pode mostrar mais de duas."}
::option[`docker logs web`]{#docker-logs-command-tail-unlimited explanation="Sem limite, o Docker pode retornar todas as linhas disponíveis."}
:::

## O que fazer quando a saída está vazia

O Docker só pode mostrar a saída que coletou. Um comando pode rodar sem exibir nada, ou o programa pode escrever suas mensagens em um arquivo que o Docker não coleta. Se `docker logs` funcionar sem exibir saída, use `docker ps -a` para ver o estado do contêiner. Uma saída vazia não esclarece o estado por si só.

:::single-choice{#docker-logs-command-empty-result} A tarefa cleanup não tem linhas nos logs. Como saber se ela ainda está em execução ou já terminou?

::option[Pedir mais linhas de cleanup ao Docker.]{#docker-logs-command-empty-more-lines explanation="Mudar o limite de linhas não mostra se um programa que não gera saída parou."}
::option[Buscar a imagem que iniciou cleanup.]{#docker-logs-command-empty-image explanation="A imagem identifica os arquivos e as configurações iniciais. O estado aparece na lista de contêineres."}
::option[Ler o estado de cleanup na lista completa de contêineres.]{#docker-logs-command-empty-container-state .correct explanation="A lista completa inclui contêineres em execução e os que terminaram, mas ainda existem."}
:::

## Resumo

Agora você pode usar a saída de um contêiner para decidir o que verificar a seguir.

1. Ler a saída coletada de um contêiner pelo nome, mesmo que ele tenha terminado.
2. Usar a mensagem do programa para localizar o problema relatado.
3. Limitar a saída com `--tail`.
4. Fazer uma verificação separada quando o log deixar uma pergunta em aberto.
