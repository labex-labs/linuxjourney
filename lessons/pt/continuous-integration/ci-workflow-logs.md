---
lesson_id: "ci-workflow-logs"
course_id: "continuous-integration"
lang: "pt"
order_index: 5
title: "Logs de fluxos de trabalho"
description: "Aprenda a encontrar a etapa que falhou em um fluxo e a interpretar a primeira mensagem útil para o diagnóstico."
meta_title: "Logs de fluxos de trabalho - Integração contínua"
meta_description: "Aprenda a encontrar a etapa que falhou em um fluxo e a interpretar a primeira mensagem útil para o diagnóstico."
meta_keywords: "logs de fluxo, diagnóstico de falhas, integração contínua, DevOps, Linux Journey"
---

O resultado de um fluxo de trabalho mostra seu estado geral. Para entender uma falha, abra o job que falhou e leia as etapas em ordem. Quando uma etapa não termina com sucesso, as seguintes podem ser ignoradas.

## Como encontrar a primeira falha

Esta execução simulada mostra o estado de cada etapa no job que verifica a página.

```text
Prepare: passed
Build page: failed
Check heading: skipped
Package site: skipped
```

Comece por `Build page`. As verificações ignoradas não produziram resultados para a página. Depois de corrigir a falha, confira as etapas seguintes em uma nova execução.

:::single-choice{#ci-workflow-logs-first-failure} Qual saída você deve ler primeiro?

::option[Package site, porque aparece por último.]{#ci-workflow-logs-first-failure-a explanation="O comando de empacotamento foi ignorado nesta execução."}
::option[Check heading, porque o fluxo verifica uma página.]{#ci-workflow-logs-first-failure-c explanation="O estado mostra que a verificação do título não rodou."}
::option[Build page, porque a etapa falhou antes que as outras rodassem.]{#ci-workflow-logs-first-failure-b .correct explanation="O log dessa etapa mostra por que as seguintes foram ignoradas."}
:::

![Execução simulada de CI com falha no build e etapas seguintes ignoradas](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-workflow-logs/skipped-steps.png)

## Como seguir a pista da mensagem de erro

A etapa que falhou mostra estas linhas.

```text
Run cp index.html dist/index.html
cp: cannot create regular file 'dist/index.html': No such file or directory
Process completed with exit code 1.
```

A mensagem indica o caminho de destino. Se o diretório acima dele, `dist`, não existir, o comando de cópia não pode criar um arquivo dentro dele. Confira se um comando anterior criou esse diretório antes da cópia. O código de saída 1 indica a falha. A mensagem indica onde procurar.

:::single-choice{#ci-workflow-logs-actionable-log} Como dist está ausente, que mudança resolve o problema indicado?

::option[Alterar o título que grep vai verificar.]{#ci-workflow-logs-actionable-log-b explanation="A verificação do título não rodou, então não há evidência de que o texto esteja incorreto."}
::option[Criar dist antes de copiar o arquivo.]{#ci-workflow-logs-actionable-log-a .correct explanation="O diretório de destino precisa existir para que o arquivo seja criado."}
::option[Baixar um artefato da etapa ignorada.]{#ci-workflow-logs-actionable-log-c explanation="A etapa de empacotamento não chegou a gerar um artefato."}
:::

## Como conferir uma nova execução

Depois de corrigir o build, compare a revisão e o estado das etapas da nova execução. Se a cópia der certo, o arquivo de saída existe. Leia os resultados do teste e do empacotamento antes de concluir que o processo todo passou. Ao relatar um problema, guarde o primeiro erro útil junto com o nome da etapa.

:::single-choice{#ci-workflow-logs-rerun-evidence} Na nova execução, Build page passou e Check heading falhou. O que mudou?

::option[O build deu certo e agora há um resultado da verificação do título para investigar.]{#ci-workflow-logs-rerun-evidence-c .correct explanation="A primeira falha que ainda precisa de atenção está na etapa de teste."}
::option[A nova execução não importa porque o build anterior falhou.]{#ci-workflow-logs-rerun-evidence-a explanation="Cada execução fornece evidências sobre sua própria revisão."}
::option[O empacotamento deve ter passado porque o build passou.]{#ci-workflow-logs-rerun-evidence-b explanation="Uma etapa posterior ainda pode falhar ou ser ignorada."}
:::

## Resumo

Agora você consegue interpretar a falha de um fluxo no contexto das outras etapas.

1. Localize a primeira etapa que rodou e falhou.
2. Use a linha de log para decidir o que investigar.
3. Após a correção, confira a nova revisão e as etapas seguintes.
