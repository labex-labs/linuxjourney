---
lesson_id: "docker-containers"
course_id: "docker"
lang: "pt"
order_index: 1
title: "Contêineres"
description: "Aprenda o que é executado dentro de um contêiner do Docker e como ele se relaciona com a máquina que executa o Docker."
meta_title: "Contêineres - Docker"
meta_description: "Entenda o que é um contêiner com o exemplo de um pequeno servidor web e veja o que muda quando seu programa principal é iniciado ou interrompido."
meta_keywords: "contêineres Docker, fundamentos de contêineres, host Docker, processo, servidor web"
---

Um navegador abre uma página de um servidor web que roda no Docker. Onde esse servidor está sendo executado? O que acontece com a página quando ele para? Comece pelo programa que responde ao navegador.

## Um programa dentro de um contêiner

Um **servidor web** é um programa que responde a solicitações de páginas. Imagine seu navegador e um pequeno servidor web chamado `web` na mesma máquina. O Docker executa o servidor em um **contêiner**, que dá ao programa sua própria visão dos arquivos e de outros recursos. Os exemplos do curso já estão prontos. Você pode acompanhar sem instalar o Docker.

:::single-choice{#docker-containers-page-request} Quando o navegador solicita uma página, o que envia o conteúdo de volta?

::option[O servidor web que está em execução no contêiner.]{#docker-containers-page-server .correct explanation="O programa do servidor recebe a solicitação e devolve a página."}
::option[Os arquivos que descrevem como iniciar o contêiner.]{#docker-containers-page-files explanation="Esses arquivos ajudam a definir a configuração. Quem responde à solicitação é um programa em execução."}
::option[A lista de contêineres do Docker na máquina.]{#docker-containers-page-list explanation="A lista mostra o que o Docker está executando. Ela não fornece a página."}
:::

## O contêiner e seu host

A máquina que executa os contêineres é chamada de **host**. Quando o Docker executa contêineres Linux no Linux, os programas são executados como processos desse host. Um **processo** é um programa em execução. Mesmo quando vários contêineres compartilham o host, cada um só tem acesso a um conjunto limitado de recursos. No Docker Desktop, os contêineres Linux são executados em uma máquina virtual Linux gerenciada pelo Docker.

:::single-choice{#docker-containers-shared-host} Dois contêineres Linux rodam no mesmo host Linux. O que isso permite concluir?

::option[Os programas deles precisam enxergar os mesmos arquivos.]{#docker-containers-host-shared-files explanation="Cada contêiner pode ter sua própria visão dos arquivos no mesmo host."}
::option[Os programas deles podem rodar como processos separados nesse host.]{#docker-containers-host-separate-processes .correct explanation="Um único host pode executar programas em contêineres separados."}
::option[Cada contêiner precisa iniciar outra máquina Linux.]{#docker-containers-host-separate-machines explanation="Contêineres Linux podem rodar como processos em um único host, sem precisar iniciar uma máquina para cada um."}
:::

## Partindo de uma imagem

O Docker cria um contêiner a partir de uma **imagem**, um pacote que contém o programa e os arquivos de que ele precisa. Você pode usar a mesma imagem de servidor web para criar `web` e `demo`. Quando iniciados, os contêineres executam o mesmo programa de servidor em processos separados. Você pode parar qualquer um deles de forma independente.

:::single-choice{#docker-containers-two-from-image} Você para demo enquanto web continua em execução. O que acontece com web?

::option[Ele fica suspenso até que demo seja iniciado novamente.]{#docker-containers-two-paused explanation="Cada contêiner executa seu próprio programa. Neste cenário, parar demo não interrompe web."}
::option[Ele precisa ser criado novamente a partir da imagem.]{#docker-containers-two-recreate explanation="O contêiner web foi criado separadamente e pode continuar em execução."}
::option[Ele continua funcionando no próprio contêiner.]{#docker-containers-two-independent .correct explanation="Os dois contêineres partem da mesma imagem e funcionam de forma independente."}
:::

## Verificando o serviço antes e depois de pará-lo

Suponha que o navegador já consiga enviar solicitações a `web`. Antes de parar o contêiner, o navegador recebe a página. Depois que o contêiner para, uma nova solicitação não recebe mais a página desse servidor. A imagem continua disponível para criar outro contêiner. Para que a página abra, o programa do servidor precisa estar em execução e o navegador precisa conseguir acessá-lo. Uma lição posterior mostra como conectar o navegador a um contêiner.

:::single-choice{#docker-containers-stopped-server} A imagem continua disponível, mas web está parado. De que web precisa para voltar a responder?

::option[O programa do servidor precisa voltar a funcionar.]{#docker-containers-stopped-program .correct explanation="A imagem fornece os arquivos. Um servidor em execução atende às novas solicitações."}
::option[A imagem precisa de outro nome para poder servir páginas.]{#docker-containers-stopped-rename explanation="Renomear a imagem não faz um servidor parado voltar a funcionar."}
::option[O navegador precisa de outra cópia da imagem do servidor.]{#docker-containers-stopped-browser-image explanation="O navegador envia as solicitações. O programa do servidor é executado no contêiner."}
:::

![Terminal da LabEx mostrando uma resposta HTTP 200 antes de parar o contêiner e uma falha na conexão depois](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-containers/server-response.png)

Neste exemplo da LabEx, o contêiner `page-demo` fornece a página. A primeira solicitação com `curl` recebe HTTP 200. Depois que o contêiner para, uma nova solicitação falha. Curl mostra `000` porque não recebeu nenhuma resposta HTTP.

## Resumo

Agora você pode explicar como um contêiner executa um programa em um host.

1. Identificar o programa que responde a uma solicitação do navegador.
2. Explicar como vários contêineres podem compartilhar um host.
3. Descrever como uma imagem pode servir de base para vários contêineres.
4. Fazer uma nova solicitação para verificar se um servidor que estava acessível continua respondendo.
