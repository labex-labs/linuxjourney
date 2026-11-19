---
lesson_id: "ci-workflow-permissions"
course_id: "continuous-integration"
lang: "pt"
order_index: 7
title: "Permissões de fluxos de trabalho"
description: "Aprenda a conceder a uma verificação rotineira de CI apenas o acesso ao repositório de que ela precisa."
meta_title: "Permissões de fluxos de trabalho - Integração contínua"
meta_description: "Aprenda a conceder a uma verificação rotineira de CI apenas o acesso ao repositório de que ela precisa."
meta_keywords: "permissões, acesso de leitura, fluxos de trabalho, integração contínua, DevOps, Linux Journey"
---

Um job de CI pode executar comandos e também pode receber credenciais. Uma **permissão** determina o que essas credenciais podem ler ou alterar. Um job que só verifica a página normalmente precisa ler os arquivos de origem.

## Como dar acesso de leitura à verificação

Este trecho do GitHub Actions restringe o token integrado do fluxo ao acesso de leitura ao conteúdo do repositório.

```yaml
permissions:
  contents: read
```

O checkout e o teste local podem ler o repositório. Um job que publica um pacote precisa de permissão para outra operação em outro recurso. Dê a permissão de publicação ao job específico que precisa dela.

:::single-choice{#ci-workflow-permissions-choose-permission} Um job lê a página e executa grep. Que permissão sobre o conteúdo do repositório ele precisa?

::option[Escrita, porque o resultado do teste é escrito no terminal.]{#ci-workflow-permissions-choose-permission-a explanation="Escrever no terminal não exige permissão para alterar o conteúdo do repositório."}
::option[Leitura.]{#ci-workflow-permissions-choose-permission-c .correct explanation="O job precisa obter o conteúdo e não tem alterações a fazer no repositório."}
::option[Escrita, porque o código está em um repositório Git.]{#ci-workflow-permissions-choose-permission-b explanation="Para a verificação descrita, basta ler os arquivos de origem."}
:::

## Como lidar com valores sensíveis

Um **segredo** é um valor como um token privado. Use o armazenamento de segredos da plataforma quando um job aprovado precisar de um. Mantenha as configurações comuns da página separadas dos segredos. Verificações rotineiras de um exemplo local devem funcionar sem credenciais de publicação.

:::single-choice{#ci-workflow-permissions-secret-needed} Que valor deve ficar no armazenamento de segredos com acesso controlado?

::option[Uma credencial privada para enviar um pacote.]{#ci-workflow-permissions-secret-needed-a .correct explanation="Uma credencial pode conceder acesso a outro sistema."}
::option[O texto Welcome que aparece no teste.]{#ci-workflow-permissions-secret-needed-b explanation="Esse texto faz parte de um exemplo público."}
::option[O nome do diretório de saída dist.]{#ci-workflow-permissions-secret-needed-c explanation="O nome do diretório é uma configuração comum."}
:::

## Como manter os logs úteis

Outras pessoas podem ter acesso aos logs do fluxo. Registre a ação e seu resultado sem exibir valores secretos. Uma mensagem de falha pode indicar que faltava uma credencial obrigatória ou que o acesso foi negado. Informe o nome do job e a revisão à pessoa responsável para que ela possa investigar. Deixe o valor da credencial fora da mensagem.

:::single-choice{#ci-workflow-permissions-safe-diagnostic} Um job de publicação não consegue se autenticar. Que mensagem ajuda na investigação sem expor a credencial?

::option[Exibir a credencial completa para que ela possa ser copiada.]{#ci-workflow-permissions-safe-diagnostic-a explanation="Qualquer pessoa com acesso ao log poderia ver a credencial."}
::option[Exibir todos os valores do ambiente para mostrar o estado do job.]{#ci-workflow-permissions-safe-diagnostic-c explanation="Listar valores do ambiente sem filtrar pode expor dados sensíveis."}
::option[Indicar que etapa da publicação falhou e o resultado da tentativa de acesso.]{#ci-workflow-permissions-safe-diagnostic-b .correct explanation="Quem revisa consegue localizar a falha e verificar o acesso configurado separadamente."}
:::

## Como revisar um novo job

Uma proposta de fluxo verifica páginas em pull requests e acrescenta um job que publica um pacote. Os dois jobs precisam de permissões diferentes. Dê à verificação apenas a leitura de que precisa e reserve as permissões de publicação aprovadas para o job que publica de fato.

:::single-choice{#ci-workflow-permissions-final-application} Que mudança na proposta atende melhor às necessidades dos dois jobs?

::option[Dar acesso de escrita no repositório aos dois jobs.]{#ci-workflow-permissions-final-application-b explanation="A verificação só lê o código. A publicação de pacotes pode exigir outra permissão."}
::option[Usar uma credencial de envio compartilhada em todas as etapas para que as novas execuções se comportem do mesmo jeito.]{#ci-workflow-permissions-final-application-c explanation="A credencial de envio só é necessária no job de publicação."}
::option[Manter as verificações com acesso somente de leitura e dar ao job de publicação apenas o acesso necessário ao pacote.]{#ci-workflow-permissions-final-application-a .correct explanation="Assim, cada job tem o acesso de que precisa e os demais privilégios ficam limitados."}
:::

## Resumo

Agora você consegue avaliar as permissões necessárias em um pipeline de CI simples.

1. Ajuste as permissões do repositório à tarefa do job.
2. Guarde credenciais privadas em um local com acesso controlado.
3. Registre erros úteis sem exibir valores de credenciais.
