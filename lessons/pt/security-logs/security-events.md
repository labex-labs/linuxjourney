---
lesson_id: "security-events"
course_id: "security-logs"
lang: "pt"
order_index: 1
title: "Eventos de segurança"
description: "Aprenda a distinguir um evento de segurança, o registro que o descreve e o alerta que pede uma verificação."
meta_title: "Eventos de segurança - Logs de segurança"
meta_description: "Leia um registro de segurança do Linux, compare-o com um alerta e decida o que investigar quando os dados disponíveis não bastarem."
meta_keywords: "eventos de segurança, logs de segurança, entradas de log, alertas, logs do Linux"
---

Um servidor informa que houve uma falha de login. O que aconteceu? O que podemos concluir? Comece separando as informações que o computador registrou das conclusões que você pode tirar.

## Eventos e entradas de log

Um **evento** é algo que aconteceu, como a rejeição de uma tentativa de login. Uma **entrada de log** guarda a descrição de um evento. Um **log** reúne essas entradas. Os exemplos do curso usam registros simulados com nomes de campos uniformes para facilitar a leitura. Ferramentas reais podem dar outros nomes aos campos e armazenar os registros de maneiras diferentes.

```text
t=08:55:00Z source=ssh host=web-01 account=alex login=rejected
```

Essa entrada indica que uma tentativa de login remoto na conta `alex` foi rejeitada. Você pode ler a entrada guardada mesmo depois da tentativa. Em outras lições, você vai comparar horários de diferentes fontes.

![Terminal da LabEx mostrando um registro simulado de login SSH rejeitado para alex em web-01](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-events/event-fields.png)

O terminal da LabEx mostra o mesmo registro simulado, lido de um arquivo de texto.

:::single-choice{#security-events-event-versus-record} Qual parte do exemplo é o evento em si?

::option[A linha guardada que descreve a rejeição.]{#security-events-event-line explanation="A linha é o registro que você pode consultar depois do evento."}
::option[A leitura posterior da linha guardada.]{#security-events-event-review explanation="A leitura acontece depois. O evento descrito é a rejeição da tentativa."}
::option[A tentativa de login foi rejeitada.]{#security-events-event-attempt .correct explanation="A rejeição aconteceu no servidor. A linha de log registra o que ocorreu."}
:::

## Lendo os campos

Um **campo** contém um dado do registro. Nestes exemplos, `t` indica o horário registrado, `host` identifica o computador onde o evento ocorreu e `source` identifica a ferramenta que o relatou. `account` indica a conta e `login` mostra o resultado da tentativa.

:::single-choice{#security-events-field-host} Você quer identificar o computador que registrou o login rejeitado. Qual valor deve consultar?

::option[`alex`, do campo account.]{#security-events-field-host-account explanation="O campo account indica a conta envolvida na tentativa."}
::option[`web-01`, do campo host.]{#security-events-field-host-web .correct explanation="O campo host identifica o computador onde o evento ocorreu."}
::option[`ssh`, do campo source.]{#security-events-field-host-tool explanation="O campo source indica qual ferramenta relatou o evento."}
:::

## Alertas e regras

Um **alerta** chama atenção para algo que pode precisar de verificação. Uma regra de monitoramento pode gerar um alerta após três tentativas rejeitadas da mesma conta no mesmo host em um intervalo de cinco minutos. Ela agrupa os registros por conta, host e horário. O alerta indica que as condições da regra foram atendidas. Pode ser apenas alguém que digitou a senha errada várias vezes.

:::single-choice{#security-events-alert-interpretation} A regra gera um alerta para três falhas de alex em web-01. O que esse alerta permite afirmar?

::option[As falhas registradas atenderam às condições da regra.]{#security-events-alert-condition .correct explanation="O alerta aponta um padrão que merece atenção. A regra não identifica quem o causou."}
::option[Três pessoas diferentes tentaram fazer login.]{#security-events-alert-people explanation="As tentativas podem vir de uma ou mais pessoas. A regra conta os registros."}
::option[Alguém conseguiu fazer login depois de três tentativas.]{#security-events-alert-success explanation="A regra conta tentativas rejeitadas. Ela não informa se houve um login bem-sucedido depois."}
:::

## Escolhendo o que verificar em seguida

Para saber se `alex` conseguiu fazer login mais tarde, procure em `web-01` um resultado posterior às falhas. Antes de concluir, confira o período coberto pelos registros. Uma exportação de log é uma cópia de entradas selecionadas e pode terminar antes do período que você precisa.

:::single-choice{#security-events-next-record} A exportação termina às 09:00. Você quer verificar se houve um login bem-sucedido às 09:05. O que deve procurar?

::option[A mesma exportação ordenada da entrada mais recente para a mais antiga.]{#security-events-next-sort explanation="Ordenar muda a sequência. Isso não acrescenta entradas depois das 09:00."}
::option[Registros de login de web-01 que incluam as 09:05.]{#security-events-next-window .correct explanation="Você precisa da fonte pertinente e de um intervalo que abranja o evento que está verificando."}
::option[Uma nova contagem das falhas anteriores às 09:00.]{#security-events-next-count explanation="Essa contagem descreve outro resultado de um período anterior."}
:::

## Resumo

Agora você pode ler um registro de segurança e decidir o que verificar depois de receber um alerta.

1. Distinguir um evento da linha que o registra.
2. Encontrar a conta, o host e o resultado em um exemplo.
3. Usar a regra de um alerta para entender o que foi observado.
4. Verificar se a fonte e o intervalo de tempo respondem à sua pergunta.
