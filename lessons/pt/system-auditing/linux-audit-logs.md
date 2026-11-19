---
lesson_id: "linux-audit-logs"
course_id: "system-auditing"
lang: "pt"
order_index: 2
title: "Logs de auditoria do Linux"
description: "Aprenda a agrupar registros do Linux Audit que descrevem uma única operação registrada."
meta_title: "Logs de auditoria do Linux - Auditoria de sistemas"
meta_description: "Aprenda a agrupar registros do Linux Audit que descrevem uma única operação registrada."
meta_keywords: "logs de auditoria do Linux, Linux Audit, auditoria de sistemas, cibersegurança, Linux Journey"
---

O Linux Audit pode gravar vários registros sobre um evento. Uma linha pode descrever a operação e outra indicar um caminho. Agrupe as linhas relacionadas antes de decidir o que elas mostram.

## Lendo um evento com várias linhas

Os valores abaixo são registros abreviados de prática, do mesmo host e da mesma data. O número após os dois-pontos na referência de auditoria ajuda a agrupar registros que têm o mesmo horário e ID de evento. Essas linhas pertencem ao mesmo evento.

```text
type=SYSCALL msg=audit(1763456400.120:42) success=yes auid=1001 euid=0
type=PATH    msg=audit(1763456400.120:42) name="/etc/journey/site.conf"
```

A primeira linha informa o resultado e os campos da conta. A linha de caminho identifica um arquivo associado ao evento.

:::single-choice{#linux-audit-logs-group-rows} Quais campos ligam a operação ao caminho neste exemplo?

::option[Apenas os tipos de registro SYSCALL e PATH.]{#linux-audit-logs-group-rows-a explanation="Os tipos indicam a função de cada linha. Muitos eventos podem ter os mesmos tipos."}
::option[O fato de as duas linhas começarem com type.]{#linux-audit-logs-group-rows-c explanation="Todas as linhas podem conter um tipo e ainda descrever eventos diferentes."}
::option[A mesma referência de auditoria no mesmo host.]{#linux-audit-logs-group-rows-b .correct explanation="Ela agrupa as linhas que descrevem o evento 42."}
:::

![Linhas simuladas SYSCALL e PATH do Linux Audit com a mesma referência de evento de auditoria](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/linux-audit-logs/grouped-event.png)

## Lendo duas identidades

Nesta amostra, `auid` é o ID de usuário do login para fins de auditoria e `euid` é o ID de usuário efetivo da ação. Um programa pode usar uma identidade efetiva diferente da identidade de login. Um ID numérico identifica uma conta no host. Pode ser necessário consultar outros registros para identificar a pessoa por trás da conta.

:::single-choice{#linux-audit-logs-identify-login} Qual campo indica a identidade de login para fins de auditoria no exemplo?

::option[O valor 0 em euid.]{#linux-audit-logs-identify-login-b explanation="Ele indica a identidade efetiva do programa durante o evento."}
::option[O valor 1001 em auid.]{#linux-audit-logs-identify-login-a .correct explanation="O campo auid identifica o usuário que fez login. Já euid indica a identidade efetiva."}
::option[O número de evento 42.]{#linux-audit-logs-identify-login-c explanation="Esse número agrupa registros e independe das identidades das contas."}
:::

## Limitando a conclusão às evidências

O campo de resultado indica que a operação registrada foi bem-sucedida. Examine o evento completo para identificar a operação. Para verificar se o conteúdo mudou, compare o arquivo com uma referência conhecida.

:::single-choice{#linux-audit-logs-useful-follow-up} O que ajudaria a descobrir se o conteúdo é diferente do arquivo aprovado?

::option[Uma comparação com uma cópia de referência aprovada ou um registro de integridade.]{#linux-audit-logs-useful-follow-up-c .correct explanation="Essa evidência pode mostrar o que mudou no arquivo."}
::option[Outra entrada de auditoria que relata uma segunda operação bem-sucedida.]{#linux-audit-logs-useful-follow-up-a explanation="Ela pode comprovar outra ação registrada. Comparar os bytes atuais com os aprovados exige outra verificação."}
::option[O ID da conta de login no mesmo evento.]{#linux-audit-logs-useful-follow-up-b explanation="O ID de login ajuda a identificar a conta envolvida. Ele não descreve alterações nos bytes do arquivo."}
:::

## Resumo

Agora você consegue usar um grupo de registros para entender um evento de auditoria.

1. Associe os registros pelo host e pela referência do evento de auditoria.
2. Leia a identidade de login e a identidade efetiva separadamente.
3. Escolha a próxima verificação quando o resultado registrado deixar uma dúvida.
