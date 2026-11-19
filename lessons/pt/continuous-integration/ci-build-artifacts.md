---
lesson_id: "ci-build-artifacts"
course_id: "continuous-integration"
lang: "pt"
order_index: 6
title: "Artefatos de build"
description: "Aprenda a relacionar um arquivo gerado pela CI à execução e à revisão de origem."
meta_title: "Artefatos de build - Integração contínua"
meta_description: "Aprenda a relacionar um arquivo gerado pela CI à execução e à revisão de origem."
meta_keywords: "artefatos de build, revisão de origem, integração contínua, DevOps, Linux Journey"
---

Um **artefato de build** é um arquivo ou conjunto de arquivos que você guarda de uma execução para usar depois. Pode ser um relatório de teste ou um arquivo compactado do site. Registrar a execução e a revisão junto com o artefato ajuda a identificar quais arquivos de origem o produziram.

## Como empacotar o diretório de saída

Use a pasta de prática em que `dist` contém a página gerada pelo build. Este exemplo cria um arquivo compactado que reúne o conteúdo do diretório. Se já houver um arquivo compactado com o mesmo nome na pasta atual, ele será substituído.

```bash
$ tar -czf site.tar.gz -C dist .
$ tar -tzf site.tar.gz
```

No primeiro comando, `-c` cria o arquivo, `-z` o compacta e `-f` indica o nome do arquivo de saída. Com `-C dist .`, o tar começa em `dist`. O segundo comando usa `-t` para listar o conteúdo do pacote. Procure `./index.html` antes de disponibilizar o arquivo.

:::single-choice{#ci-build-artifacts-inspect-archive} Como conferir se a página foi incluída?

::option[Liste o conteúdo com tar -tzf site.tar.gz.]{#ci-build-artifacts-inspect-archive-b .correct explanation="A lista mostra se index.html está no pacote."}
::option[Crie o pacote outra vez.]{#ci-build-artifacts-inspect-archive-a explanation="Repetir a criação não mostra os itens para conferência."}
::option[Leia apenas o nome do arquivo.]{#ci-build-artifacts-inspect-archive-c explanation="O nome do pacote não revela o conteúdo."}
:::

![Listagem do tar com index.html dentro de site.tar.gz](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-build-artifacts/archive-contents.png)

## Como associar o artefato a uma execução

Um fluxo pode enviar o pacote pronto. A página da execução mostra qual revisão entrou no build. Dois artefatos chamados `site.tar.gz` podem ter conteúdos diferentes se vieram de revisões distintas. Para escolher o download, verifique tanto a execução quanto a revisão.

:::single-choice{#ci-build-artifacts-choose-run} As execuções 41 e 42 contêm site.tar.gz. Como identificar o pacote da revisão que você conferiu?

::option[Pelo primeiro download chamado site.tar.gz.]{#ci-build-artifacts-choose-run-b explanation="O nome não informa quais arquivos de origem o produziram."}
::option[Pela última execução bem-sucedida, qualquer que seja sua revisão.]{#ci-build-artifacts-choose-run-c explanation="Uma execução posterior pode ter sucesso com arquivos diferentes. Procure a revisão que você pretende usar."}
::option[Pela execução cuja revisão registrada corresponde à que você conferiu.]{#ci-build-artifacts-choose-run-a .correct explanation="Várias execuções podem usar o mesmo nome de arquivo."}
:::

## Como distinguir um pacote de uma imagem de contêiner

Um pacote do site contém arquivos que você pode extrair. Uma imagem de contêiner inclui o sistema de arquivos e as configurações que o Docker usa para iniciar um contêiner. Um fluxo pode publicar uma imagem em um registro de imagens. Se você pretende executá-la, guarde a referência da imagem junto com a revisão de origem.

:::single-choice{#ci-build-artifacts-deployable-type} A próxima etapa precisa iniciar um contêiner a partir de uma imagem em um registro. Que saída ela deve referenciar?

::option[Um relatório de teste baixado da execução.]{#ci-build-artifacts-deployable-type-a explanation="O relatório descreve resultados e não fornece um sistema de arquivos para o contêiner."}
::option[A referência da imagem de contêiner publicada.]{#ci-build-artifacts-deployable-type-c .correct explanation="O Docker pode usar essa referência para buscar a imagem preparada."}
::option[O nome do arquivo compactado do site.]{#ci-build-artifacts-deployable-type-b explanation="O arquivo contém os arquivos da página, mas seu nome não identifica uma imagem no registro."}
:::

## Resumo

Agora você consegue identificar um artefato de build e descobrir de onde ele veio.

1. Empacote os arquivos do build e confira o conteúdo do pacote.
2. Confira a execução e a revisão de origem que o produziram.
3. Escolha um artefato de arquivos ou uma imagem de contêiner conforme a necessidade da próxima etapa.
