---
lesson_id: "security-event-correlation"
course_id: "security-logs"
lang: "pt"
order_index: 5
title: "Correlação de eventos"
description: "Aprenda a associar registros de segurança usando horário, host, conta e informações de sessão."
meta_title: "Correlação de eventos - Logs de segurança"
meta_description: "Compare registros de SSH e sudo, coloque os horários no mesmo fuso e decida quais evidências indicam que os eventos estão ligados."
meta_keywords: "correlação de eventos, logs de segurança, login por SSH, eventos do sudo, horários, IDs de sessão"
---

Um registro indica que alguém fez login em um computador. Outro indica que um comando foi autorizado. As duas coisas estão relacionadas? A **correlação de eventos** compara registros para verificar se eles descrevem atividades relacionadas.

## Lendo dois registros

O SSH permite fazer login em outro computador. Depois do login, uma pessoa pode usar `sudo` para pedir autorização para executar um comando com outra conta. Os dois registros simulados abaixo são do mesmo dia e usam nomes de campos iguais para facilitar a prática. Logs reais podem usar nomes diferentes ou omitir campos.

```text
t=09:14:02Z      source=ssh   host=web-01 account=alex session=42 login=accepted
t=11:15:10+02:00 source=sudo  host=web-01 account=alex session=42 decision=allowed
```

O campo `source` indica qual ferramenta relatou o evento. O campo `host` identifica o computador onde ele ocorreu. Os dois registros indicam atividade da conta `alex`. Para identificar quem usou essa conta, seriam necessárias outras evidências.

:::single-choice{#security-event-correlation-account-evidence} Uma pessoa da equipe afirma que Alex fez pessoalmente a solicitação ao sudo. O que esses registros comprovam até aqui?

::option[Alex fez pessoalmente a solicitação ao sudo.]{#security-event-correlation-account-person explanation="O nome de uma conta não basta para identificar a pessoa que a usou."}
::option[Os registros mostram atividade de duas contas diferentes.]{#security-event-correlation-account-different explanation="Os dois campos account indicam alex. Os valores de source identificam as ferramentas que registraram a atividade."}
::option[Os dois eventos indicam a mesma conta.]{#security-event-correlation-account-shared .correct explanation="Os dois registros indicam alex. Ainda faltam evidências para saber quem usou a conta."}
:::

## Comparando os horários dos eventos

O campo `t` contém o horário registrado. No primeiro registro, `Z` indica UTC, uma referência comum para comparar horários. No segundo, `+02:00` indica um horário duas horas à frente de UTC. Subtraia duas horas de `11:15:10` para obter `09:15:10` em UTC.

Compare `09:14:02` e `09:15:10`. O login foi registrado primeiro. Mesmo eventos próximos no tempo podem ter vindo de logins diferentes.

:::single-choice{#security-event-correlation-time-order} Em outro dia, um login foi registrado às `09:14Z` e uma solicitação às `11:13+02:00`. Qual foi a ordem?

::option[A solicitação aconteceu um minuto antes.]{#security-event-correlation-time-request-first .correct explanation="Subtraindo duas horas, o horário da solicitação é 09:13 UTC. O login foi às 09:14 UTC."}
::option[O login aconteceu um minuto antes.]{#security-event-correlation-time-login-first explanation="A solicitação corresponde a 09:13 UTC, um minuto antes do login de 09:14 UTC."}
::option[O login aconteceu quase duas horas antes.]{#security-event-correlation-time-unadjusted explanation="Isso compara as horas exibidas diretamente. Converta as duas para UTC antes de ordená-las."}
:::

## Verificando o host e a sessão

Uma **sessão** é o período de atividade entre o login e a saída ou desconexão. Nestes exemplos, o registro de SSH inclui o ID de sessão associado ao login aceito. As duas fontes usam o mesmo ID para aquele login no mesmo host. Os dois primeiros registros mostram `host=web-01` e `session=42`, o que associa o login e a solicitação a uma única sessão.

Nestes exemplos, o número de sessão é local a cada host. O próximo registro mostra a mesma conta e o mesmo número de sessão, apenas alguns segundos depois.

```text
t=09:15:18Z source=sudo host=web-02 account=alex session=42 decision=allowed
```

![Terminal da LabEx com registros simulados de web-01 e web-02 e uma conversão para 09:15:10 UTC](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-event-correlation/utc-correlation.png)

O terminal mostra os três registros simulados e confirma a conversão para UTC com o comando `date` do Ubuntu.

:::single-choice{#security-event-correlation-host-scope} Qual é a relação do terceiro registro com a sessão SSH original?

::option[Pertence à mesma sessão porque a conta é igual e os horários são próximos.]{#security-event-correlation-host-scope-account explanation="Dois hosts podem registrar atividades com a mesma conta com poucos segundos de diferença."}
::option[Pertence a outra sessão porque o host é diferente.]{#security-event-correlation-host-scope-machine .correct explanation="A sessão 42 de web-02 só vale para esse host. O login original ocorreu em web-01."}
::option[Pertence à mesma sessão porque o número é igual.]{#security-event-correlation-host-scope-session explanation="Neste exemplo, o número da sessão só tem significado junto com seu host. Os hosts são diferentes."}
:::

## Descrevendo o que as evidências permitem concluir

Em `web-01`, o login foi aceito e o `sudo` permitiu a execução de um comando durante aquela sessão. Isso é o que os registros permitem afirmar. Para saber como o comando terminou, procure um registro do resultado. Uma sessão pode conter vários comandos, então relacione o resultado à solicitação específica. Se não encontrar um registro correspondente, mantenha o resultado como desconhecido.

:::single-choice{#security-event-correlation-completion-evidence} Qual novo registro esclareceria se o comando terminou com êxito?

::option[O resultado de outro comando da mesma sessão.]{#security-event-correlation-completion-other-command explanation="Uma sessão pode executar vários comandos. O resultado precisa corresponder ao pedido que você está verificando."}
::option[Outro registro mostrando que a solicitação foi autorizada.]{#security-event-correlation-completion-permission explanation="Isso confirma a autorização. O resultado do comando ainda precisa de outro registro."}
::option[O resultado do comando solicitado naquele pedido específico.]{#security-event-correlation-completion-result .correct explanation="O resultado correspondente pode mostrar como o comando terminou."}
:::

Para praticar como filtrar e comparar outros registros de autenticação e do sudo, experimente a [análise de logs do sistema](https://labex.io/tutorials/linux-system-log-analysis-656124).

## Resumo

Agora você pode usar vários registros de segurança para chegar a uma conclusão e identificar o que ainda precisa verificar.

1. Identificar a conta indicada no evento.
2. Converter os horários para um mesmo fuso antes de compará-los.
3. Usar o host e a sessão juntos para relacionar atividades.
4. Dizer o que os registros comprovam e buscar evidências para a questão que resta.
