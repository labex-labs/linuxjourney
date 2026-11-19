---
lesson_id: "ssh-login-events"
course_id: "security-logs"
lang: "pt"
order_index: 2
title: "Eventos de login por SSH"
description: "Aprenda a ler registros de logins aceitos e rejeitados e a agrupar tentativas da mesma conexão."
meta_title: "Eventos de login por SSH - Logs de segurança"
meta_description: "Leia a conta, o endereço remoto, o método de autenticação e o resultado no log do SSH. Use o identificador de conexão para comparar tentativas."
meta_keywords: "eventos de login SSH, logs de SSH, login aceito, login rejeitado, métodos de autenticação"
---

**SSH**, sigla de Secure Shell, permite fazer login em outro computador pela rede. O computador que recebe a conexão pode registrar cada tentativa. O registro mostra qual conta foi apresentada e se o servidor aceitou a prova de autenticação.

## Lendo o resultado

Veja dois registros simulados de SSH. O campo `login` indica o resultado. Uma tentativa rejeitada não passou pela verificação. Uma tentativa aceita passou por essa verificação.

```text
t=09:13:48Z source=ssh host=web-01 account=alex login=rejected
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
```

O primeiro registro mostra uma rejeição para `alex`. O segundo mostra uma tentativa aceita para a mesma conta. Cada resultado vale para sua própria tentativa.

:::single-choice{#ssh-login-events-outcome-order} O que se pode concluir a partir desses registros?

::option[A tentativa mais recente passou pela verificação de login.]{#ssh-login-events-outcome-later .correct explanation="O segundo registro mostra login=accepted às 09:14:02."}
::option[As duas tentativas passaram pela verificação.]{#ssh-login-events-outcome-both explanation="A linha anterior registra uma tentativa rejeitada."}
::option[A tentativa mais recente falhou na verificação de login.]{#ssh-login-events-outcome-failed explanation="A primeira tentativa foi rejeitada. A segunda foi aceita."}
:::

## Lendo endereços e métodos de autenticação

O endereço remoto indica de onde veio a conexão, do ponto de vista do computador que a recebeu. No exemplo, ele aparece em `peer`. Um endereço de rede pode ser compartilhado. Só esse campo não identifica quem o usou.

```text
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
peer=192.0.2.10 method=publickey connection=17
```

A segunda linha é a continuação da mesma entrada. O campo `method` indica qual prova o SSH verificou. `password` quer dizer que o SSH verificou uma senha. `publickey` indica que o dispositivo que se conectou provou que podia usar uma chave aceita pelo servidor para aquela conta.

:::single-choice{#ssh-login-events-method-evidence} O que o registro permite afirmar sobre a tentativa aceita?

::option[O servidor aceitou um login com senha.]{#ssh-login-events-method-password explanation="Se fosse senha, o método apareceria com outro valor. O registro indica o método de chave pública."}
::option[O servidor identificou a pessoa que usou o endereço.]{#ssh-login-events-method-person explanation="O endereço indica como o host viu a conexão. Isso não demonstra quem estava no teclado."}
::option[O servidor aceitou um login com chave.]{#ssh-login-events-method-key .correct explanation="O registro mostra login=accepted e method=publickey."}
:::

## Agrupando tentativas por conexão

Uma **conexão** é o caminho de rede que o SSH usa para trocar mensagens. Nestes exemplos, o host atribui um identificador a cada conexão. Uma conexão pode conter várias tentativas de login, e o mesmo endereço pode abrir outra conexão.

```text
t=09:13:48Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=rejected
t=09:13:55Z host=web-01 account=alex peer=192.0.2.10 connection=18 login=rejected
t=09:14:02Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=accepted
```

Em `web-01`, a primeira e a última entrada têm o mesmo número de conexão, 17. Leia o identificador junto com o host.

![Terminal da LabEx mostrando tentativas simuladas de SSH a partir de um endereço e as conexões 17 e 18](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/ssh-login-events/ssh-connections.png)

O terminal exibe as três tentativas juntas para facilitar a comparação dos números de conexão.

:::single-choice{#ssh-login-events-group-connection} Quais registros se referem à conexão 18 em web-01?

::option[As tentativas das 09:13:48 e das 09:14:02.]{#ssh-login-events-group-seventeen explanation="Essas duas linhas têm o número de conexão 17."}
::option[Apenas a tentativa das 09:13:55.]{#ssh-login-events-group-eighteen .correct explanation="Só essa linha mostra a conexão 18 em web-01."}
::option[As três tentativas vindas de 192.0.2.10.]{#ssh-login-events-group-address explanation="Os dois números de conexão aparecem para o mesmo endereço."}
:::

## Acompanhando um login aceito

Um login bem-sucedido mostra que o SSH aceitou a prova de autenticação daquela conta. Para descobrir o que aconteceu depois, procure um registro de abertura de **sessão**. A sessão abrange a atividade após o login. O registro de login bem-sucedido, por si só, indica apenas o resultado da autenticação.

:::single-choice{#ssh-login-events-after-accepted} Qual registro ajudaria a saber se um login aceito abriu uma sessão?

::option[Outro registro de que o mesmo login foi aceito.]{#ssh-login-events-after-accepted-again explanation="Ele só repetiria o resultado da verificação de login."}
::option[Uma tentativa anterior rejeitada para a conta em outro host.]{#ssh-login-events-after-other-host explanation="Esse registro descreve outra tentativa em outro computador."}
::option[Um registro de abertura de sessão para aquele login.]{#ssh-login-events-after-session .correct explanation="A abertura descreve a etapa seguinte e pode ser associada ao login aceito."}
:::

## Resumo

Agora você pode ler o resultado de uma tentativa de SSH e identificar quais registros pertencem à mesma conexão.

1. Distinguir tentativas aceitas das rejeitadas.
2. Usar o endereço remoto e o método para descrever a tentativa.
3. Agrupar registros por host e conexão quando houver um identificador.
4. Procurar uma entrada de sessão para saber o que ocorreu depois de um login bem-sucedido.
