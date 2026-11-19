---
lesson_id: "ci-workflow-triggers"
course_id: "continuous-integration"
lang: "pt"
order_index: 2
title: "Gatilhos de fluxos de trabalho"
description: "Aprenda a prever quando um fluxo do GitHub Actions é executado a partir de seus eventos e filtros de branch."
meta_title: "Gatilhos de fluxos de trabalho - Integração contínua"
meta_description: "Aprenda a prever quando um fluxo do GitHub Actions é executado a partir de seus eventos e filtros de branch."
meta_keywords: "gatilhos de fluxo, filtros de branch, integração contínua, DevOps, Linux Journey"
---

Um fluxo de trabalho começa quando algo o aciona. No GitHub Actions, a seção `on` indica quais eventos podem iniciá-lo. Um **evento** pode ser um push para uma branch, uma alteração em uma pull request ou outra ação compatível.

## Como conferir um push

Leia este trecho de um fluxo de trabalho. No YAML, o recuo mostra que `branches` é uma configuração de `push`.

```yaml
on:
  push:
    branches:
      - main
```

Este fluxo é executado quando um commit é enviado à branch `main`, desde que esteja habilitado e as demais condições sejam atendidas. Fazer um commit no terminal local não envia a alteração ao GitHub. É o push que este trecho monitora.

:::single-choice{#ci-workflow-triggers-push-filter} Qual ação corresponde a esse gatilho de push?

::option[Criar um commit em main no repositório local.]{#ci-workflow-triggers-push-filter-a explanation="O gatilho aguarda um evento no repositório do GitHub."}
::option[Fazer push de um commit para uma branch chamada draft.]{#ci-workflow-triggers-push-filter-b explanation="O filtro seleciona a branch main."}
::option[Fazer push do commit para main.]{#ci-workflow-triggers-push-filter-c .correct explanation="O evento corresponde a push e passa pelo filtro de branch."}
:::

## Como conferir uma pull request

Outro evento pode verificar mudanças propostas antes da mesclagem. Neste trecho, o filtro de branch vale para a branch de destino da pull request.

```yaml
on:
  pull_request:
    branches:
      - main
```

Uma proposta de `health-page` para `main` passa pelo filtro. Com os tipos de atividade padrão, abrir a solicitação ou enviar outro commit para a branch de origem são exemplos de ações que podem iniciar o fluxo.

:::single-choice{#ci-workflow-triggers-pr-target} Uma pull request propõe mesclar notes em main. Que nome é usado no filtro de branch?

::option[Notes, a branch de origem.]{#ci-workflow-triggers-pr-target-b explanation="Notes contém o trabalho proposto."}
::option[Main, a branch de destino.]{#ci-workflow-triggers-pr-target-a .correct explanation="O filtro da pull request se aplica à branch base, que vai receber as alterações."}
::option[O nome do arquivo editado pela proposta.]{#ci-workflow-triggers-pr-target-c explanation="O trecho filtra pelo nome da branch."}
:::

## Como ler mais de um gatilho

Um arquivo pode listar os dois eventos sob a mesma chave `on`. Uma execução associada a uma pull request pode verificar a mesclagem proposta. Quando uma mesclagem atualizar `main`, uma execução disparada pelo push pode verificar o estado atual dessa branch. Os resultados correspondem ao evento e à revisão de cada execução.

:::single-choice{#ci-workflow-triggers-after-merge} Um fluxo tem os dois gatilhos dos exemplos. Uma mesclagem atualiza main. Qual evento corresponde a essa atualização?

::option[Um push para main.]{#ci-workflow-triggers-after-merge-b .correct explanation="A branch de destino foi atualizada e passa pelo filtro de push."}
::option[A abertura de uma pull request em outra branch.]{#ci-workflow-triggers-after-merge-a explanation="A ação descrita foi uma atualização de main depois da mesclagem."}
::option[Um commit local sem atualização do remoto.]{#ci-workflow-triggers-after-merge-c explanation="No exemplo, main já mudou no GitHub."}
:::

## Resumo

Agora você consegue associar um gatilho do fluxo a um evento no repositório.

1. Leia um evento de push e seu filtro de branch.
2. Identifique a branch de destino à qual se aplica o filtro da pull request.
3. Relacione o resultado de cada execução ao evento que a iniciou.
