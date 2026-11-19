---
lesson_id: "sudo-events"
course_id: "security-logs"
lang: "pt"
order_index: 3
title: "Eventos do sudo"
description: "Aprenda a ler nos registros do sudo qual conta solicitou um comando, com qual conta ele seria executado e se foi autorizado."
meta_title: "Eventos do sudo - Logs de segurança"
meta_description: "Leia os registros do sudo distinguindo a conta solicitante, a conta de destino, o comando e a decisão de permissão."
meta_keywords: "eventos do sudo, logs do sudo, autorização, conta de destino, permissões do Linux"
---

Uma pessoa pode fazer login com uma conta comum e depois precisar de mais permissões para uma tarefa. Em um sistema que usa `sudo`, ela pode pedir para executar um comando com outra conta. O registro do pedido pode mostrar quais permissões foram solicitadas e o que o sistema decidiu.

## Identificando as duas contas

Os registros simulados usam `account` para a conta que fez a solicitação e `target` para a conta com a qual o comando seria executado. A conta `root` tem privilégios de administração. Um pedido feito com `sudo` pode indicar outra conta de destino, como `backup`.

```text
t=09:15:10Z source=sudo host=web-01 account=alex target=root
command=systemctl status nginx decision=allowed session=42
```

A segunda linha é a continuação da entrada. Aqui, `alex` pediu para executar o comando como `root`.

:::single-choice{#sudo-events-account-target} No registro `account=sam target=backup`, quem pediu a execução do comando e com qual conta?

::option[Backup pediu para executar como sam.]{#sudo-events-target-swapped explanation="Account indica quem fez a solicitação. Target mostra a identidade que o comando usaria."}
::option[Sam pediu para executar como backup.]{#sudo-events-target-backup .correct explanation="Account é a conta solicitante. Target é a conta que o comando usaria."}
::option[Sam pediu para executar como root.]{#sudo-events-target-root explanation="Root é uma conta de destino possível. Este registro indica backup."}
:::

## Lendo o comando solicitado

O campo `command` indica o comando solicitado. No exemplo, `systemctl status nginx` pede o estado atual do serviço web Nginx. Outro registro poderia indicar `systemctl restart nginx`, uma solicitação para parar e iniciar o serviço novamente. Os dois citam o mesmo serviço e pedem ações diferentes.

:::single-choice{#sudo-events-command-scope} Qual solicitação pede uma mudança no estado do serviço web?

::option[`systemctl restart nginx`]{#sudo-events-command-restart .correct explanation="Restart pede para parar e iniciar o serviço de novo. Isso pode mudar seu estado."}
::option[`systemctl status nginx`]{#sudo-events-command-status explanation="Status pede informações sobre o serviço. Não é uma solicitação de reinicialização."}
::option[Qualquer uma, pois as duas mencionam nginx.]{#sudo-events-command-both explanation="O nome do serviço é igual. O verbo indica qual ação foi solicitada."}
:::

## Interpretando a decisão

A **política** é o conjunto de regras que o `sudo` usa para decidir se permite uma solicitação. Nos exemplos, `decision=allowed` indica que a política permitiu o pedido. `decision=denied` indica que o `sudo` o rejeitou.

```text
t=09:16:00Z source=sudo host=web-01 account=alex target=root
command=systemctl restart nginx decision=denied session=42
```

A autorização diz que havia permissão. Para saber como o comando terminou, procure um registro de resultado, se o sistema fornecer um.

![Terminal da LabEx com registros simulados do sudo mostrando uma consulta de estado permitida e uma reinicialização negada](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/sudo-events/sudo-decisions.png)

Compare os comandos e as decisões indicados nestes dois registros simulados.

:::single-choice{#sudo-events-denied-request} O que o segundo exemplo diz sobre a solicitação de reinicialização?

::option[O sudo negou a solicitação de reinicialização.]{#sudo-events-denied-refused .correct explanation="O comando indica a ação pedida. Denied mostra que a permissão foi negada."}
::option[O serviço reiniciou com sucesso.]{#sudo-events-denied-success explanation="Este registro mostra uma negação. Ele não comprova uma reinicialização bem-sucedida."}
::option[A consulta de estado anterior também foi negada.]{#sudo-events-denied-earlier explanation="Cada decisão vale para sua própria solicitação. O registro anterior mostra allowed."}
:::

## Levando a conta de login em consideração

Os dois exemplos identificam `alex` como solicitante e incluem `session=42`. Esse número indica a sessão, ou seja, o período de atividade que segue o login. Você pode usá-lo para localizar os registros de login relacionados. A conta de destino de cada exemplo se refere àquela solicitação. Use os dois campos de conta ao descrever o pedido.

:::single-choice{#sudo-events-session-interpretation} Qual resumo corresponde ao primeiro exemplo?

::option[Root fez login diretamente e abriu a sessão 42.]{#sudo-events-session-root-login explanation="Este é um registro do sudo. A conta de destino não descreve outro login."}
::option[Alex pediu permissões de root para todos os comandos da sessão.]{#sudo-events-session-all-commands explanation="A entrada cita um só comando. Ela não cobre todos os comandos da sessão."}
::option[Alex pediu para executar um comando específico como root na sessão 42.]{#sudo-events-session-one-command .correct explanation="A conta solicitante, a conta de destino, o comando e a sessão sustentam essa conclusão."}
:::

## Resumo

Agora você pode ler um registro do sudo e diferenciar uma autorização do resultado do comando.

1. Identificar as contas solicitante e de destino.
2. Usar o campo do comando para descrever a solicitação específica.
3. Distinguir uma solicitação permitida de uma negada.
4. Considerar a sessão de login ao descrever uma solicitação.
