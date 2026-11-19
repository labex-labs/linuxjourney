---
lesson_id: "web-https"
course_id: "web-security"
lang: "pt"
order_index: 2
title: "HTTPS"
description: "Aprenda a identificar a parte de uma requisição web que o HTTPS protege."
meta_title: "HTTPS - Segurança web"
meta_description: "Aprenda a identificar a parte de uma requisição web que o HTTPS protege."
meta_keywords: "HTTPS, TLS, segurança web, cibersegurança, Linux Journey"
---

O HTTP define as mensagens trocadas entre o navegador e o servidor. O HTTPS envia essas mesmas mensagens por **TLS**, um protocolo que protege a conexão e ajuda o navegador a verificar o servidor.

## Identificando a conexão protegida

Imagine que o navegador se conecte a `https://site.example`. Depois de estabelecer o TLS, o navegador e o servidor podem trocar mensagens HTTP criptografadas. Quem observa esse trecho da rede não consegue simplesmente ler o corpo HTTP nem alterá-lo sem que isso seja detectado.

```text
Browser  ===== HTTPS connection =====  Website server
```

O navegador ainda precisa validar a identidade que o servidor apresenta.

:::single-choice{#web-https-protected-hop} O que o HTTPS protege nessa configuração simples?

::option[A página depois que o navegador já a exibiu.]{#web-https-protected-hop-b explanation="O navegador lê a página após descriptografar a resposta."}
::option[Todos os backups armazenados pelo site.]{#web-https-protected-hop-c explanation="Os backups exigem proteção própria."}
::option[As mensagens HTTP enviadas pela conexão protegida.]{#web-https-protected-hop-a .correct explanation="O TLS protege as mensagens em trânsito entre as extremidades da conexão."}
:::

## Lendo um caminho com vários trechos

Um proxy pode receber a requisição do navegador e encaminhá-la para outro servidor. Se a conexão TLS termina no proxy, ele pode ler a requisição antes de encaminhá-la. A conexão seguinte precisa de sua própria proteção. Avalie cada trecho da comunicação.

```text
Browser  === HTTPS ===  Proxy  --- HTTP ---  Internal server
```

No diagrama, a conexão externa usa TLS. A conexão interna usa HTTP sem criptografia.

:::single-choice{#web-https-inner-hop} Qual trecho exige uma mudança própria para ganhar proteção TLS?

::option[A conexão do navegador ao proxy.]{#web-https-inner-hop-a explanation="Esse trecho já usa HTTPS."}
::option[A conexão do proxy ao servidor interno.]{#web-https-inner-hop-b .correct explanation="O trecho interno do diagrama usa HTTP sem criptografia."}
::option[Uma aba do navegador que nunca solicita o site.]{#web-https-inner-hop-c explanation="Essa aba não tem uma conexão no diagrama."}
:::

## Verificando também o acesso na aplicação

Uma conexão segura e válida ajuda a confirmar a identidade do servidor e protege as mensagens em trânsito. A aplicação ainda decide qual conta pode ler uma página ou alterar uma configuração. Uma página privada pode usar TLS e ainda exigir uma política de acesso na aplicação.

:::single-choice{#web-https-access-vs-transport} O que o serviço deve verificar antes de devolver a página privada de uma conta?

::option[Se a conta autenticada pode ler essa página.]{#web-https-access-vs-transport-c .correct explanation="A autorização na aplicação controla o que a conta pode acessar."}
::option[Apenas se a conexão usa TLS.]{#web-https-access-vs-transport-a explanation="O HTTPS protege a troca de mensagens. O serviço ainda precisa decidir se o acesso é permitido."}
::option[Apenas se o certificado cobre o nome de host solicitado.]{#web-https-access-vs-transport-b explanation="O certificado ajuda a confirmar a identidade do servidor. A aplicação controla o acesso às páginas privadas."}
:::

## Resumo

Agora você consegue descrever o que o HTTPS protege no caminho de uma requisição web.

1. Identifique onde o TLS começa e termina.
2. Verifique cada trecho quando um proxy encaminha a requisição.
3. Entenda por que a aplicação ainda precisa de controles de acesso.
