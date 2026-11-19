---
lesson_id: "security-session-records"
course_id: "security-logs"
lang: "pt"
order_index: 4
title: "Registros de sessões"
description: "Aprenda a relacionar aberturas e encerramentos e verificar quais sessões um trecho do log pode descrever."
meta_title: "Registros de sessões - Logs de segurança"
meta_description: "Leia registros de sessões do Linux, associe os eventos de abertura e encerramento e decida o que verificar quando faltar um encerramento."
meta_keywords: "registros de sessões Linux, abertura de sessão, encerramento de sessão, ID de sessão, retenção de logs"
---

Uma verificação de login bem-sucedida confirma que alguém passou pela autenticação de uma conta. Uma **sessão** é o período de atividade após o login que termina quando a pessoa sai da sessão ou perde a conexão. Quando os dois eventos são registrados, você pode saber quando a sessão começou e quando terminou.

## Lendo um registro de abertura

O sistema pode atribuir um **ID de sessão** para distinguir uma sessão em um computador. Estas linhas simuladas mostram duas aberturas para a mesma conta em `web-01`. Todos os horários desta lição estão no mesmo fuso.

```text
t=09:14:05Z source=session host=web-01 account=alex session=42 state=opened
t=09:17:00Z source=session host=web-01 account=alex session=43 state=opened
```

A primeira linha informa o início da sessão 42. A segunda informa o início da sessão 43, uma sessão distinta no mesmo host.

:::single-choice{#security-session-records-two-openings} O que as duas aberturas permitem concluir?

::option[A primeira sessão terminou quando a segunda começou.]{#security-session-records-open-ended explanation="A segunda abertura indica que outra sessão começou. Não informa quando a primeira terminou."}
::option[Duas contas diferentes fizeram login no host.]{#security-session-records-open-accounts explanation="As duas linhas mostram a mesma conta. O campo de sessão distingue os dois períodos de atividade."}
::option[A mesma conta abriu duas sessões diferentes.]{#security-session-records-open-two .correct explanation="As duas linhas mostram alex e cada sessão tem um ID próprio em web-01."}
:::

## Associando uma abertura a um encerramento

Leia o host e o ID de sessão em conjunto antes de associar dois registros. Compare a linha de encerramento abaixo com os registros de abertura.

```text
t=09:20:05Z source=session host=web-01 account=alex session=42 state=closed
```

Em `web-01`, há seis minutos entre a abertura e o encerramento da sessão 42. O par indica o início e o fim registrados. Ele não lista as ações realizadas no intervalo.

![Terminal da LabEx mostrando as aberturas simuladas das sessões 42 e 43 e o encerramento da sessão 42](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-session-records/session-records.png)

A captura reúne os registros simulados de abertura e encerramento.

:::single-choice{#security-session-records-pair-ids} Se a linha de encerramento mostrasse `session=43`, sem mudar o host nem o horário, quando a sessão teria começado?

::option[Às 09:14:05.]{#security-session-records-pair-forty-two explanation="Essa abertura indica a mesma conta, mas pertence à sessão 42."}
::option[Às 09:17:00.]{#security-session-records-pair-forty-three .correct explanation="O host web-01 e a sessão 43 correspondem à segunda abertura, às 09:17:00."}
::option[Às 09:20:05.]{#security-session-records-pair-end-time explanation="Esse é o horário de encerramento registrado. O início está na abertura correspondente."}
:::

## Verificando um encerramento ausente

Volte ao registro original de encerramento da sessão 42. O trecho termina às 09:21 e não mostra o encerramento da sessão 43. Ela ainda podia estar ativa naquele momento. Também é possível que o registro esteja fora do intervalo disponível ou não exista nessa fonte. O **período de retenção** define por quanto tempo uma entrada permanece guardada e disponível para consulta.

:::single-choice{#security-session-records-missing-close} O que é possível afirmar sobre a sessão 43 usando apenas esse trecho?

::option[Ela ainda estava ativa ao final do trecho.]{#security-session-records-missing-active explanation="É possível, mas a ausência de encerramento não confirma o estado real."}
::option[O trecho não contém um horário de encerramento para a sessão.]{#security-session-records-missing-unknown .correct explanation="Isso descreve os registros disponíveis. Uma fonte diferente ou posterior pode indicar o horário."}
::option[Ela terminou junto com a sessão 42.]{#security-session-records-missing-together explanation="O encerramento registrado pertence à sessão 42. Aqui não há um que corresponda à sessão 43."}
:::

## Escolhendo a fonte certa

Para descobrir quando a sessão terminou, procure o encerramento correspondente em um trecho posterior do mesmo host. Para saber se está ativa agora, consulte a lista atual de sessões desse host. Um log salvo e uma lista atual respondem a perguntas sobre momentos distintos.

:::single-choice{#security-session-records-current-status} Você precisa saber se a sessão 43 está ativa agora. Qual fonte ajuda mais?

::option[Uma lista atual das sessões em web-01.]{#security-session-records-current-list .correct explanation="A lista mostra quais sessões o host informa como ativas neste momento."}
::option[Uma cópia antiga do registro de abertura.]{#security-session-records-current-opening explanation="Ela mostra que a sessão começou, mas não indica se ainda está ativa."}
::option[O registro de encerramento da sessão 42 em web-01.]{#security-session-records-current-other explanation="O encerramento de outra sessão não responde à pergunta sobre a sessão 43."}
:::

## Resumo

Agora você pode usar registros de sessão para descrever um início e um fim registrados.

1. Identificar uma abertura, seu host e seu ID de sessão.
2. Associar o encerramento à abertura correta.
3. Explicar o que não se sabe quando falta o registro de encerramento.
4. Escolher entre registros anteriores e uma lista atual de sessões.
