---
lesson_id: "deployment-records"
course_id: "deployment"
lang: "pt"
order_index: 6
title: "Registros de implantação"
description: "Aprenda a reconstruir uma implantação e um rollback a partir de uma breve linha do tempo da release."
meta_title: "Registros de implantação - Implantação"
meta_description: "Aprenda a reconstruir uma implantação e um rollback a partir de uma breve linha do tempo da release."
meta_keywords: "registros de implantação, rollback, implantação, DevOps, Linux Journey"
---

Um registro de implantação ajuda outra pessoa a associar o que os usuários viram a uma mudança. Comece pelo horário, pelo ambiente, pela revisão do código e pelo artefato. Inclua o resultado da verificação e as medidas tomadas depois.

## Identificando o que mudou

O registro de exemplo acompanha uma implantação. Os identificadores foram abreviados para facilitar a leitura.

```text
UTC    Target   Commit   Artifact  Observation
09:00  staging  8a61e1   digest-C  version 3, home returned 200
09:12  prod     8a61e1   digest-C  version 3, home returned 503
09:18  prod     72b110   digest-B  version 2, home returned 200
```

HTTP 200 indica uma resposta bem-sucedida. HTTP 503 indica que o serviço estava indisponível para aquela requisição. Em um registro real, anote como você fez a verificação e em qual endereço.

:::single-choice{#deployment-records-first-prod-change} Qual linha registra o primeiro comportamento observado em produção com digest-C?

::option[A linha de prod às 09:12.]{#deployment-records-first-prod-change-b .correct explanation="Ela mostra a versão que se tentou implantar em produção e a falha na verificação."}
::option[A linha de staging às 09:00.]{#deployment-records-first-prod-change-a explanation="Essa verificação ocorreu em outro ambiente."}
::option[A linha de prod às 09:18.]{#deployment-records-first-prod-change-c explanation="Essa linha registra outro artefato depois do rollback."}
:::

![Linha do tempo simulada com sucesso em homologação, erro 503 em produção e rollback para a versão 2](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-records/release-timeline.png)

## Explicando o rollback

A última linha mostra o retorno a digest-B. A verificação da versão e o resultado da consulta à página inicial descrevem o que ocorreu depois do rollback. A causa da falha anterior ainda precisa ser investigada. Registre as hipóteses como tal até ter evidências que as sustentem.

:::single-choice{#deployment-records-rollback-evidence} O que você pode afirmar sobre o resultado das 09:18?

::option[A falha das 09:12 ocorreu porque faltava um banco de dados.]{#deployment-records-rollback-evidence-b explanation="O registro não traz evidências sobre as dependências."}
::option[Todas as requisições funcionaram a partir daquele momento.]{#deployment-records-rollback-evidence-c explanation="Uma verificação bem-sucedida confirma o resultado daquela requisição."}
::option[A produção voltou à versão 2 e a requisição à página inicial funcionou.]{#deployment-records-rollback-evidence-a .correct explanation="A linha registra a versão restaurada e a resposta HTTP observada."}
:::

## Repassando o registro

Quem assumir a revisão precisa conseguir reproduzir a verificação. Inclua como ela foi feita, o horário com o fuso e, se houver, um link para o build que gerou o artefato. Se a causa ainda for desconhecida, indique o que examinar a seguir.

:::single-choice{#deployment-records-handoff-detail} Qual detalhe ajudaria outra pessoa a repetir a verificação da página inicial?

::option[Somente o identificador da release anterior.]{#deployment-records-handoff-detail-a explanation="A versão anterior ajuda na comparação. Para repetir a requisição é preciso saber onde e quando ela foi feita."}
::option[O endereço exato consultado e o horário da verificação.]{#deployment-records-handoff-detail-c .correct explanation="Esses dados permitem verificar o mesmo caminho e consultar outros sinais na janela relevante."}
::option[O horário em que o commit foi criado.]{#deployment-records-handoff-detail-b explanation="O horário do commit identifica um evento anterior. A pessoa precisa do horário e do destino da verificação."}
:::

## Registrando o que realmente foi executado

Uma tag anotada na implantação pode mudar de destino depois da release. Se o serviço já informa a versão 2, anote qual artefato está em execução e qual é a sua tag. Com esses dados, outra pessoa poderá comparar a release mais tarde, mesmo se a tag tiver mudado no registro de imagens.

:::single-choice{#deployment-records-final-application} A nota de release indica site:2. Qual detalhe adicional torna a comparação posterior mais confiável?

::option[O digest de quem baixou site:2 mais recentemente.]{#deployment-records-final-application-c explanation="Um download posterior pode receber conteúdo diferente do que o serviço está executando."}
::option[O digest completo da imagem que foi executada.]{#deployment-records-final-application-a .correct explanation="Ele identifica o conteúdo selecionado, mesmo se a tag passar a apontar para outra imagem."}
::option[A mesma tag copiada para um segundo campo.]{#deployment-records-final-application-b explanation="Repetir a tag mantém a mesma dúvida sobre o conteúdo."}
:::

## Resumo

Agora você consegue ler a linha do tempo de uma release e repassá-la a outra pessoa.

1. Identifique o ambiente, a revisão do código e o artefato no registro.
2. Descreva o rollback com base no resultado observado.
3. Guarde os detalhes necessários para repetir a verificação.
