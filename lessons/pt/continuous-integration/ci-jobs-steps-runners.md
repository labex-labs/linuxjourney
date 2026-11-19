---
lesson_id: "ci-jobs-steps-runners"
course_id: "continuous-integration"
lang: "pt"
order_index: 3
title: "Jobs, etapas e runners"
description: "Aprenda a encontrar os jobs, as etapas e o runner de um fluxo em um arquivo curto do GitHub Actions."
meta_title: "Jobs, etapas e runners - Integração contínua"
meta_description: "Aprenda a encontrar os jobs, as etapas e o runner de um fluxo em um arquivo curto do GitHub Actions."
meta_keywords: "jobs, etapas, runners, GitHub Actions, integração contínua, DevOps, Linux Journey"
---

Um fluxo de trabalho é o processo automatizado completo. Um **job** reúne tarefas atribuídas a um **runner**, a máquina ou o ambiente que as executa. Uma **etapa** é uma operação dentro do job.

## Como ler um fluxo simples

O exemplo executa um job em um runner Ubuntu hospedado pelo GitHub. Um fluxo como esse fica em `.github/workflows/` em um repositório do GitHub.

```yaml
name: Page check
on: push
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Get the repository
        uses: actions/checkout@v6
      - name: Find the heading
        run: grep -q '<h1>Welcome</h1>' index.html
```

O identificador do job é `check`. O campo `runs-on` seleciona o ambiente. `uses` chama uma ação reutilizável, neste caso para disponibilizar os arquivos do repositório. `run` executa um comando no runner.

:::single-choice{#ci-jobs-steps-runners-job-fields} Que campo escolhe onde o job check vai rodar?

::option[runs-on.]{#ci-jobs-steps-runners-job-fields-a .correct explanation="Ele especifica o tipo de runner para esse job."}
::option[uses.]{#ci-jobs-steps-runners-job-fields-b explanation="Esta etapa chama a ação de checkout."}
::option[name.]{#ci-jobs-steps-runners-job-fields-c explanation="Esse campo dá um nome ao fluxo de trabalho."}
:::

## Como acompanhar as etapas

Por padrão, as etapas de um job são executadas na ordem da lista. Como a verificação lê um arquivo do repositório, o checkout vem primeiro. Dentro do mesmo job, uma etapa pode usar arquivos escritos por uma etapa anterior.

:::single-choice{#ci-jobs-steps-runners-step-order} O que faltaria à etapa grep em um runner novo se o checkout fosse movido para depois dela?

::option[O nome do job.]{#ci-jobs-steps-runners-step-order-a explanation="O fluxo já selecionou o job."}
::option[O próprio runner Ubuntu.]{#ci-jobs-steps-runners-step-order-c explanation="O runner é selecionado antes de executar as etapas."}
::option[O arquivo do projeto que a etapa precisa ler.]{#ci-jobs-steps-runners-step-order-b .correct explanation="O checkout disponibiliza os arquivos do repositório antes da verificação."}
:::

## Como separar os jobs

Jobs diferentes podem rodar em paralelo. Cada job hospedado pelo GitHub recebe seu próprio runner. Um arquivo criado em um só fica disponível em outro se o fluxo o transferir. Se um job depende do sucesso de outro, declare a dependência com `needs`. Quando também for preciso passar arquivos, use um artefato.

:::single-choice{#ci-jobs-steps-runners-separate-jobs} Um job de build grava site.tar.gz. Um job posterior roda em outro runner hospedado. Como ele deve receber o arquivo?

::option[Presumindo que o arquivo ficou no mesmo diretório de trabalho.]{#ci-jobs-steps-runners-separate-jobs-a explanation="Cada runner hospedado começa com seu próprio sistema de arquivos."}
::option[Transferindo o arquivo como um artefato.]{#ci-jobs-steps-runners-separate-jobs-c .correct explanation="O fluxo pode enviar o arquivo em um job e baixá-lo no outro."}
::option[Definindo needs para o segundo job aguardar o build.]{#ci-jobs-steps-runners-separate-jobs-b explanation="Needs controla a ordem. O arquivo do build ainda precisa ser transferido entre os runners."}
:::

Para escrever e executar um fluxo em um repositório do GitHub, experimente [GitHub Actions para iniciantes](https://labex.io/courses/github-actions-for-beginners). O curso prático exige uma conta do GitHub.

## Resumo

Agora você consegue ler as partes principais de um fluxo de CI.

1. Encontre um job e o runner correspondente.
2. Diferencie uma ação reutilizável de uma etapa que executa um comando no shell.
3. Reconheça quando os jobs precisam de uma dependência ou de uma transferência de arquivos.
