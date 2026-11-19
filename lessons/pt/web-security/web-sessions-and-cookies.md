---
lesson_id: "web-sessions-and-cookies"
course_id: "web-security"
lang: "pt"
order_index: 5
title: "Sessões e cookies"
description: "Aprenda como um cookie associa as requisições do navegador a uma sessão web."
meta_title: "Sessões e cookies - Segurança web"
meta_description: "Aprenda como um cookie associa as requisições do navegador a uma sessão web."
meta_keywords: "sessões, cookies, segurança web, cibersegurança, Linux Journey"
---

Depois do login, o navegador geralmente envia outra requisição. Uma **sessão** permite que a aplicação associe essas requisições à conta autenticada. Uma forma comum usa um identificador curto armazenado em um cookie no navegador.

## Acompanhando um cookie

Estes exemplos são abreviados. A resposta envia um cookie chamado `session` com um token fictício.

```http
Set-Cookie: session=sample-token; Secure; HttpOnly; SameSite=Lax
```

O navegador pode então incluir o cookie em uma requisição posterior que atenda às regras de envio.

```http
Cookie: session=sample-token
```

O servidor usa o token para localizar a sessão que criou.

:::single-choice{#web-sessions-and-cookies-direction} Qual cabeçalho envia de volta o valor do cookie em uma requisição que atende às regras?

::option[O cabeçalho Set-Cookie.]{#web-sessions-and-cookies-direction-a explanation="O servidor envia esse cabeçalho na resposta para definir o cookie."}
::option[O cabeçalho Content-Type.]{#web-sessions-and-cookies-direction-c explanation="Esse cabeçalho descreve o formato do corpo da mensagem."}
::option[O cabeçalho Cookie.]{#web-sessions-and-cookies-direction-b .correct explanation="O navegador inclui esse cabeçalho na requisição quando as regras permitem."}
:::

## Lendo os atributos

`Secure` restringe o envio normal do cookie a conexões HTTPS. `HttpOnly` impede que scripts da página leiam o cookie pela interface usual do navegador. `SameSite` controla quando o navegador inclui o cookie em requisições iniciadas a partir de outro site. Cada atributo controla um aspecto diferente do comportamento do navegador.

:::single-choice{#web-sessions-and-cookies-secure-attribute} Qual atributo instrui o navegador a restringir o envio desse cookie ao HTTPS?

::option[O atributo HttpOnly.]{#web-sessions-and-cookies-secure-attribute-b explanation="Esse atributo restringe o acesso ao cookie por scripts da página."}
::option[O atributo Secure.]{#web-sessions-and-cookies-secure-attribute-a .correct explanation="Esse atributo exige o transporte protegido para o envio do cookie."}
::option[O nome session.]{#web-sessions-and-cookies-secure-attribute-c explanation="O nome do cookie é um rótulo escolhido pela aplicação."}
:::

## Encerrando uma sessão

Quando um usuário sai da conta, o serviço pode invalidar a sessão no servidor e pedir ao navegador que remova o cookie armazenado. É importante invalidar a sessão no servidor porque o navegador ainda pode ter o valor antigo por algum tempo. Trate um token de sessão real como uma credencial e deixe-o fora de capturas de tela e logs compartilhados.

:::single-choice{#web-sessions-and-cookies-after-sign-out} O que deve acontecer se um token de sessão invalidado voltar a chegar ao servidor?

::option[O servidor deve tratar a requisição como não autenticada.]{#web-sessions-and-cookies-after-sign-out-c .correct explanation="A sessão associada ao valor já perdeu a validade no servidor."}
::option[O servidor deve restaurar a sessão antiga automaticamente.]{#web-sessions-and-cookies-after-sign-out-a explanation="A sessão antiga foi encerrada."}
::option[O servidor deve aceitar o token porque o cookie ainda tem um nome.]{#web-sessions-and-cookies-after-sign-out-b explanation="O nome do cookie não torna seu valor válido."}
:::

## Resumo

Agora você consegue acompanhar um cookie de sessão entre o navegador e o serviço.

1. Identifique o cabeçalho que define o cookie e o que o envia de volta.
2. Explique para que servem os atributos mais comuns dos cookies.
3. Descreva como a invalidação no servidor encerra a sessão.
