---
lesson_id: "ci-overview"
course_id: "continuous-integration"
lang: "pt"
order_index: 1
title: "Integração contínua"
description: "Aprenda como a integração contínua verifica pequenas mudanças antes de elas entrarem em uma branch compartilhada."
meta_title: "Integração contínua - Integração contínua"
meta_description: "Aprenda como a integração contínua verifica pequenas mudanças antes de elas entrarem em uma branch compartilhada."
meta_keywords: "integração contínua, CI, DevOps, Linux Journey"
---

Uma alteração na página inicial pode parecer correta no seu navegador e mesmo assim quebrar quando outra pessoa tenta acessar a página. A **integração contínua**, ou CI, reúne alterações com frequência e executa verificações que podem ser repetidas em versões específicas.

## Como associar uma alteração à sua verificação

Uma revisão identifica a versão dos arquivos que está sendo verificada. Quando uma mudança proposta modifica `index.html`, a CI pode checar essa versão e informar se ela atende a uma condição. Neste site, por exemplo, a verificação poderia procurar o título esperado. A equipe pode usar o resultado para decidir se vai mesclar as mudanças.

:::single-choice{#ci-overview-revision-result} Uma verificação passou na segunda-feira. Na terça-feira, um novo commit altera a página. O que o resultado antigo comprova?

::option[As duas revisões atendem à condição.]{#ci-overview-revision-result-b explanation="O commit mais recente precisa de um resultado próprio."}
::option[A revisão de segunda-feira passou nessa verificação.]{#ci-overview-revision-result-a .correct explanation="O resultado vale para a revisão em que a verificação rodou."}
::option[A nova página já está disponível para os visitantes.]{#ci-overview-revision-result-c explanation="Verificar os arquivos de origem não informa o que está disponível no ambiente publicado."}
:::

## Como ler uma verificação que falhou

Suponha que a verificação indique que o título esperado não foi encontrado. Quem propôs a alteração já tem por onde começar a investigar. Antes de editar a página, confira o que se esperava e qual foi o resultado. Talvez a edição contenha um erro. Ou talvez o comportamento desejado tenha mudado e a verificação também precise ser atualizada.

:::single-choice{#ci-overview-failed-action} O que você deve conferir primeiro quando a verificação do título falha?

::option[O título esperado e o arquivo na revisão verificada.]{#ci-overview-failed-action-b .correct explanation="A comparação ajuda a entender o que provocou essa diferença."}
::option[Primeiro o artefato da execução anterior que deu certo.]{#ci-overview-failed-action-a explanation="Esse artefato representa um resultado anterior. A falha atual e o arquivo verificado dão pistas mais diretas."}
::option[As configurações de rede dos visitantes.]{#ci-overview-failed-action-c explanation="Essa verificação lê um arquivo sem fazer requisições no navegador."}
:::

## Como distinguir verificação e entrega

Um pipeline pode verificar arquivos, gerar uma saída e repassá-la para uma implantação posterior. Um **build** prepara algo que as etapas seguintes podem usar, como uma pasta de arquivos prontos para serem servidos. Uma **implantação** instala ou inicia uma versão em um ambiente. Seu primeiro fluxo de CI vai verificar uma página antes de enviá-la à etapa seguinte.

:::single-choice{#ci-overview-output-vs-live} Os testes passaram e um arquivo compactado do site foi gerado. Como saber se os visitantes podem acessar essa versão?

::option[Com uma segunda cópia do log da verificação.]{#ci-overview-output-vs-live-a explanation="O log descreve a verificação e o build."}
::option[Pela existência do arquivo compactado.]{#ci-overview-output-vs-live-b explanation="O arquivo pode existir sem estar sendo servido."}
::option[Com um registro da implantação e uma requisição bem-sucedida à página esperada.]{#ci-overview-output-vs-live-c .correct explanation="Esses dados relacionam a versão produzida com uma resposta do ambiente de destino."}
:::

## Resumo

Agora você consegue explicar onde a CI entra no caminho de uma alteração.

1. Associe cada resultado a uma revisão específica.
2. Use a falha da verificação para identificar o que investigar primeiro.
3. Diferencie verificação, build e implantação.
