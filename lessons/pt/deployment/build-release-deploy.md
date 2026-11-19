---
lesson_id: "build-release-deploy"
course_id: "deployment"
lang: "pt"
order_index: 1
title: "Build, release e implantação"
description: "Aprenda a acompanhar uma revisão do código pelos registros de build, release e implantação."
meta_title: "Build, release e implantação - Implantação"
meta_description: "Aprenda a acompanhar uma revisão do código pelos registros de build, release e implantação."
meta_keywords: "build, release, implantação, DevOps, Linux Journey"
---

Alguém da equipe diz que a versão 2 está pronta. Isso pode significar que os arquivos foram gerados, que a versão foi aprovada ou que os visitantes já conseguem acessá-la. Acompanhe os registros para descobrir até onde o processo chegou.

## Identificando o build

Um build gera um artefato a partir de uma revisão específica do código-fonte. No exemplo, ele empacota um site pequeno em uma imagem de contêiner e a guarda em um registro de imagens. Anote o commit de origem junto com a referência da imagem gerada.

```text
Build 81
Source commit: 3ab4501
Image: registry.example/journey/site:2
Result: succeeded
```

Esse registro mostra o que foi gerado. O site pode continuar servindo uma versão anterior.

:::single-choice{#build-release-deploy-build-record} Qual registro liga a imagem empacotada à revisão do código?

::option[Um favorito do navegador.]{#build-release-deploy-build-record-b explanation="Um favorito guarda um endereço, sem indicar como os arquivos foram gerados."}
::option[O build 81.]{#build-release-deploy-build-record-a .correct explanation="Ele indica o commit de origem e a imagem gerada."}
::option[O nome da branch local mais recente.]{#build-release-deploy-build-record-c explanation="Uma branch pode passar a apontar para outro commit e seu nome não identifica esse build."}
:::

## Lendo a release

Uma **release** identifica uma versão aprovada para distribuição. Por exemplo, o registro de uma release pode aprovar para homologação a imagem exata do build 81. Assim você pode usar o mesmo artefato depois da aprovação sem gerar outra cópia.

:::single-choice{#build-release-deploy-release-record} A release 2 foi aprovada para homologação. O que isso confirma?

::option[O artefato registrado foi aprovado para esse uso.]{#build-release-deploy-release-record-b .correct explanation="A release registra qual artefato foi autorizado para homologação."}
::option[Todos os ambientes já servem a versão 2.]{#build-release-deploy-release-record-a explanation="A aprovação permite seguir com o processo. A versão em execução ainda precisa ser verificada."}
::option[A versão 2 recebe mais requisições.]{#build-release-deploy-release-record-c explanation="O registro de uma release não mede o tráfego."}
:::

## Descobrindo a versão implantada

Uma **implantação** coloca uma versão específica em um ambiente e inicia ou atualiza a aplicação ali. Um ambiente é um local como homologação ou produção, com recursos e configurações próprios. Uma requisição bem-sucedida ao endpoint de versão ajuda a verificar qual versão responde naquele ambiente.

```text
Staging version response: 2
Production version response: 1
```

Neste exemplo, a versão nova responde em homologação. Em produção, a versão 1 ainda responde.

:::single-choice{#build-release-deploy-running-version} Uma pessoa quer evidências de que a versão 2 atende em produção. Qual observação ajudaria diretamente?

::option[Outra resposta de homologação com a versão 2.]{#build-release-deploy-running-version-a explanation="Essa requisição continua verificando o ambiente de homologação."}
::option[A mensagem de aprovação da release.]{#build-release-deploy-running-version-b explanation="A aprovação não testa o serviço em execução."}
::option[Uma resposta com a versão no endereço de produção.]{#build-release-deploy-running-version-c .correct explanation="Essa requisição verifica o ambiente indicado na revisão."}
:::

## Resumo

Agora você consegue distinguir os registros gerados a cada etapa de uma release.

1. Associe o artefato do build ao código de origem.
2. Identifique o artefato aprovado na release.
3. Confirme qual versão responde no ambiente desejado.
