---
lesson_id: "dockerfile"
course_id: "docker"
lang: "pt"
order_index: 7
title: "Dockerfile"
description: "Aprenda como um Dockerfile transforma uma página e uma imagem base em uma imagem de servidor web reutilizável."
meta_title: "Dockerfile - Docker"
meta_description: "Leia FROM, COPY e CMD em um Dockerfile simples e diferencie criar uma imagem de executar um contêiner."
meta_keywords: "Dockerfile, build de imagem Docker, FROM, COPY, CMD, contexto de build"
---

Você já iniciou um contêiner usando uma imagem de servidor web pronta. Para servir sua própria página, pode criar uma imagem que já a inclua. Um **Dockerfile** é um arquivo de texto com instruções para criar essa imagem.

## Começando com uma imagem base

Uma **imagem base** fornece os programas e arquivos de partida. O Dockerfile abaixo parte da imagem do Nginx, adiciona uma página e registra o comando padrão do contêiner. Guarde o Dockerfile e um arquivo chamado `index.html` na mesma pasta de prática. Para a página, basta uma linha como `<h1>Hello from Docker</h1>`.

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
CMD ["nginx", "-g", "daemon off;"]
```

`FROM nginx:alpine` começa com a imagem indicada, que já contém o Nginx. O Docker usa essa imagem durante o build da nova imagem.

:::single-choice{#dockerfile-base-image-purpose} Qual linha fornece o Nginx antes de você adicionar a página?

::option[`COPY index.html /usr/share/nginx/html/index.html`]{#dockerfile-base-image-copy explanation="COPY adiciona a página. O servidor vem da imagem base."}
::option[`FROM nginx:alpine`]{#dockerfile-base-image-from .correct explanation="FROM seleciona a imagem de partida, que já contém o servidor."}
::option[A linha que começa com `CMD`.]{#dockerfile-base-image-cmd explanation="CMD configura o comando padrão de inicialização. O programa do servidor vem da imagem base."}
:::

## Adicionando um arquivo

`COPY` lê `index.html` entre os arquivos que você fornece ao build. A instrução grava a página no caminho à direita, de onde essa versão da imagem do Nginx serve a página padrão. Se você editar a página local depois, refaça o build para incluir a mudança.

:::single-choice{#dockerfile-copy-after-edit} Você alterou o título no index.html local depois do build. Como incluir a mudança em uma nova imagem?

::option[Iniciar outro contêiner com a imagem existente.]{#dockerfile-copy-edit-run explanation="Esse contêiner inicia com a página que já está armazenada na imagem."}
::option[Mudar apenas o nome do contêiner existente.]{#dockerfile-copy-edit-rename explanation="O nome do contêiner não muda os arquivos que a imagem contém."}
::option[Refazer o build com a página atualizada.]{#dockerfile-copy-edit-rebuild .correct explanation="Durante o build, COPY lê o arquivo local atual e o inclui na nova imagem."}
:::

## Configurando o comando de inicialização

`CMD` define o comando padrão de um novo contêiner. No exemplo, ele indica ao Nginx que continue em primeiro plano dentro do contêiner. Você ainda pode deixar o contêiner em segundo plano no terminal com `docker run -d`.

:::single-choice{#dockerfile-cmd-start-time} Quando o comando padrão de CMD é usado no exemplo?

::option[Quando o contêiner inicia com o comando padrão.]{#dockerfile-cmd-when-start .correct explanation="O Docker usa o comando padrão da imagem na inicialização do contêiner."}
::option[Enquanto o Docker copia a página para a imagem.]{#dockerfile-cmd-when-copy explanation="COPY adiciona a página durante o build. Nessa etapa, o servidor não é executado."}
::option[Quando o Docker termina de gravar a imagem.]{#dockerfile-cmd-when-build explanation="O build registra o comando de inicialização para uso posterior."}
:::

## Criando a imagem e iniciando o contêiner

Execute o build na pasta que contém os dois arquivos. A opção `-t` dá à imagem a referência `journey-web:1`. O ponto final indica ao Docker que use o diretório atual como origem dos arquivos para o build.

```bash
$ docker build -t journey-web:1 .
$ docker run -d --name custom-web -p 127.0.0.1:8082:80 journey-web:1
```

O segundo comando inicia um contêiner. Se a porta 8082 estiver livre, abra `http://127.0.0.1:8082` em um navegador no host do Docker para ver a sua página.

:::single-choice{#dockerfile-build-versus-run} O build terminou com sucesso e você ainda não executou o segundo comando. O que está pronto?

::option[A imagem existe e pode ser usada para criar um contêiner.]{#dockerfile-build-ready-image .correct explanation="O build produziu a imagem. O próximo comando inicia um contêiner a partir dela."}
::option[O contêiner com o nome escolhido já está servindo sua página.]{#dockerfile-build-ready-container explanation="O servidor inicia quando você executa a imagem em um contêiner."}
::option[O Docker já publicou a porta do navegador para a imagem.]{#dockerfile-build-ready-port explanation="O mapeamento de portas é uma opção de docker run. O build não configura a conexão."}
:::

![Terminal da LabEx mostrando o build da imagem, a inicialização do contêiner e a resposta HTML da página personalizada](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/dockerfile/build-and-run.png)

A última solicitação recebe a página incluída durante o build. As mensagens de progresso e os IDs das imagens podem variar no seu ambiente.

## Resumo

Agora você pode ler um Dockerfile pequeno e acompanhar o caminho de uma página local até um servidor em execução.

1. Identificar a imagem base em `FROM`.
2. Explicar de onde `COPY` lê o arquivo e onde o grava.
3. Reconhecer `CMD` como o comando padrão de inicialização do contêiner.
4. Criar uma imagem e iniciar um contêiner com ela.
