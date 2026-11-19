---
lesson_id: "web-access-logs"
course_id: "web-security"
lang: "pt"
order_index: 7
title: "Logs de acesso web"
description: "Aprenda a usar logs de acesso HTTP para descobrir o que um serviço retornou sem expor credenciais."
meta_title: "Logs de acesso web - Segurança web"
meta_description: "Aprenda a usar logs de acesso HTTP para descobrir o que um serviço retornou sem expor credenciais."
meta_keywords: "logs de acesso web, HTTP, segurança web, cibersegurança, Linux Journey"
---

Um servidor web pode gravar uma entrada no **log de acesso** para cada requisição. O log pode incluir horário, caminho, código de resposta e ID da requisição. Use apenas os campos necessários para responder à pergunta da investigação.

## Lendo o resultado da requisição

Este trecho simulado usa campos com nomes. As duas requisições foram feitas para caminhos distintos.

```text
t=09:18:01Z request=r31 method=GET path=/health status=200
t=09:18:04Z request=r32 method=GET path=/staff status=403
```

Um código `403` indica que o serviço recusou a requisição. Confira o caminho exato e o ID antes de comparar a resposta com outro registro.

:::single-choice{#web-access-logs-log-result} Qual requisição você deve acompanhar para investigar a recusa?

::option[r31 em /health.]{#web-access-logs-log-result-a explanation="Essa linha registra uma verificação de saúde bem-sucedida."}
::option[r32 em /staff.]{#web-access-logs-log-result-b .correct explanation="O status dessa requisição é 403, que indica a recusa no trecho."}
::option[As duas, como se fossem a mesma requisição.]{#web-access-logs-log-result-c explanation="Os IDs e os caminhos distinguem as requisições."}
:::

## Procurando a decisão de acesso

O log de acesso registra o que o servidor retornou. Ele pode não indicar o motivo da decisão sobre a permissão. Se a aplicação também registra decisões de autorização, procure o mesmo ID de requisição no mesmo horário. Nesse exemplo, isso pode indicar qual regra foi aplicada.

:::single-choice{#web-access-logs-refusal-reason} A linha de acesso informa 403. Qual registro adicional explicaria melhor o motivo?

::option[A decisão de autorização da aplicação para r32.]{#web-access-logs-refusal-reason-a .correct explanation="O registro correspondente pode indicar qual regra foi aplicada."}
::option[Uma resposta bem-sucedida de outro site.]{#web-access-logs-refusal-reason-b explanation="Essa resposta não tem relação com a recusa."}
::option[Uma requisição anterior ao caminho de verificação de saúde.]{#web-access-logs-refusal-reason-c explanation="Ela registra uma operação com outro resultado."}
:::

## Mantendo as credenciais fora dos logs

Evite registrar valores que permitam usar a sessão de outra pessoa, como um cookie de sessão completo ou um token de autorização. O ID da requisição e o status da resposta ainda ajudam no diagnóstico. Ao compartilhar uma amostra do log, remova os campos confidenciais e mantenha apenas os detalhes necessários à investigação.

:::single-choice{#web-access-logs-safe-fields} Qual par de dados pode ajudar a rastrear a requisição recusada sem copiar uma credencial?

::option[O cookie de sessão completo e a senha da conta.]{#web-access-logs-safe-fields-a explanation="Os dois valores são confidenciais e devem ficar fora dos logs compartilhados."}
::option[O token de autorização e um caminho público.]{#web-access-logs-safe-fields-b explanation="O caminho pode ser útil. O token é uma credencial privada."}
::option[O ID da requisição e o status da resposta.]{#web-access-logs-safe-fields-c .correct explanation="Esses dados permitem comparar os registros relevantes sem revelar um valor de sessão."}
:::

## Compartilhando um trecho pequeno

Imagine que alguém precise de contexto para revisar uma requisição recusada. Mantenha o horário, o ID, o método, o caminho sem dados sensíveis e o status se esses campos bastarem. Alguns caminhos podem incluir dados privados nos parâmetros da URL. Revise o trecho antes de compartilhá-lo.

:::single-choice{#web-access-logs-final-application} Qual trecho atende melhor a essa revisão?

::option[A requisição inteira e todos os cabeçalhos por padrão.]{#web-access-logs-final-application-b explanation="As requisições podem conter credenciais ou dados pessoais desnecessários."}
::option[Apenas o código de status, sem nenhum identificador.]{#web-access-logs-final-application-c explanation="Pode ser difícil associar apenas o código ao registro correspondente da política de acesso."}
::option[O caminho sem dados sensíveis, com o horário, o ID da requisição e o status da resposta.]{#web-access-logs-final-application-a .correct explanation="Isso mantém os campos necessários para relacionar os registros sem compartilhar valores de sessão."}
:::

## Resumo

Agora você consegue interpretar um log de acesso simples e preservar o contexto com segurança.

1. Associe o ID da requisição, o caminho e a resposta.
2. Procure um registro da política de acesso se precisar entender o motivo.
3. Mantenha as credenciais fora dos logs coletados e compartilhados.
