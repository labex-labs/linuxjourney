---
lesson_id: "deployment-image-versions"
course_id: "deployment"
lang: "pt"
order_index: 2
title: "Versões de imagens"
description: "Aprenda a distinguir a tag de uma imagem do seu digest e a comparar as imagens exatas usadas em dois ambientes."
meta_title: "Versões de imagens - Implantação"
meta_description: "Aprenda a distinguir a tag de uma imagem do seu digest e a comparar as imagens exatas usadas em dois ambientes."
meta_keywords: "versões de imagens, tags, digest, implantação, DevOps, Linux Journey"
---

Uma tag como `site:2` facilita a leitura de uma referência de imagem. Quem publica a imagem pode mover a tag ao enviar uma substituta. Para identificar o conteúdo exato, registre seu **digest**, um valor calculado a partir do conteúdo referenciado.

## Lendo uma tag

Imagine que o registro de imagens mostre estes registros em dois dias diferentes. Os digests abreviados servem apenas de exemplo. Para baixar uma imagem, é preciso usar o valor completo.

```text
Monday    site:2    sha256:a1b2…
Tuesday   site:2    sha256:c3d4…
```

A mesma tag passou a apontar para outro conteúdo. Uma máquina que baixou a imagem na segunda-feira pode continuar usando a versão anterior.

:::single-choice{#deployment-image-versions-moving-tag} Ambos os ambientes informam a tag site:2. O que revela qual imagem cada um baixou?

::option[A tag que eles têm em comum.]{#deployment-image-versions-moving-tag-b explanation="As duas imagens do exemplo usam a mesma tag, embora tenham conteúdos diferentes."}
::option[A quantidade de contêineres em cada máquina.]{#deployment-image-versions-moving-tag-c explanation="A contagem não identifica as imagens."}
::option[Os digests registrados.]{#deployment-image-versions-moving-tag-a .correct explanation="A tag pode mudar de destino. O digest identifica o conteúdo selecionado no momento do download."}
:::

## Lendo uma referência por digest

Uma referência de imagem pode usar `@` seguido do digest completo. Assim, a requisição ao registro aponta para aquele objeto específico. Use o digest completo fornecido pelo registro de imagens ou pelo registro de build. Os valores abreviados ajudam na leitura dos exemplos, mas são insuficientes para obter a imagem.

:::single-choice{#deployment-image-versions-fixed-reference} Qual formato seleciona um objeto específico no registro de imagens?

::option[O nome da imagem sem tag.]{#deployment-image-versions-fixed-reference-a explanation="O Docker aplica uma tag padrão que pode mudar de destino."}
::option[O nome da imagem seguido do digest completo.]{#deployment-image-versions-fixed-reference-c .correct explanation="O digest identifica o conteúdo exato."}
::option[Um comentário indicando o dia do build.]{#deployment-image-versions-fixed-reference-b explanation="O registro de imagens não consegue buscar um objeto pelo comentário."}
:::

## Comparando imagens da mesma plataforma

Um nome de imagem pode apontar para uma lista de builds para diferentes tipos de máquina ou para uma imagem de uma plataforma específica. Para comparar o que dois hosts executam, anote a plataforma de cada um e compare as referências das imagens correspondentes. Guarde a referência original completa no registro da release.

:::single-choice{#deployment-image-versions-compare-platform} Uma release oferece imagens para arm64 e amd64. Que comparação ajuda ao verificar dois hosts amd64?

::option[Comparar as referências das imagens amd64 selecionadas pelos hosts.]{#deployment-image-versions-compare-platform-b .correct explanation="Você compara o conteúdo feito para a mesma plataforma."}
::option[Comparar objetos de imagem de arquiteturas diferentes.]{#deployment-image-versions-compare-platform-a explanation="É esperado que esses objetos correspondam a plataformas diferentes."}
::option[Comparar os nomes dos hosts.]{#deployment-image-versions-compare-platform-c explanation="Os nomes identificam os hosts. O conteúdo implantado exige uma referência de imagem."}
:::

## Resumo

Agora você consegue identificar a imagem exata a que uma tag aponta.

1. Explique por que uma mesma tag pode apontar para conteúdos diferentes.
2. Reconheça uma referência com o digest completo.
3. Compare as imagens da plataforma pertinente.
