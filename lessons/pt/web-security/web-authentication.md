---
lesson_id: "web-authentication"
course_id: "web-security"
lang: "pt"
order_index: 4
title: "Autenticação"
description: "Aprenda como um serviço web verifica a identidade e como dois fatores podem fornecer tipos diferentes de evidência."
meta_title: "Autenticação - Segurança web"
meta_description: "Aprenda como um serviço web verifica a identidade e como dois fatores podem fornecer tipos diferentes de evidência."
meta_keywords: "autenticação, fatores de autenticação, segurança web, cibersegurança, Linux Journey"
---

A **autenticação** é a etapa que verifica a identidade declarada pelo usuário. Um formulário de login pode pedir o nome da conta e uma senha. O nome indica a identidade que o usuário declara. A senha fornece uma prova que o serviço pode verificar.

## Identificando a identidade declarada

Imagine que um usuário digite o nome da conta `alex`. Qualquer pessoa que conheça o nome pode digitá-lo. O serviço verifica a prova enviada com base nas informações e na política daquela conta.

:::single-choice{#web-authentication-username-claim} Qual dado indica a conta que o usuário quer acessar?

::option[O resultado da verificação da senha.]{#web-authentication-username-claim-a explanation="Esse resultado ajuda a aceitar ou rejeitar a identidade declarada."}
::option[O nome da conta.]{#web-authentication-username-claim-b .correct explanation="Ele diz ao serviço qual identidade deve ser verificada."}
::option[O formato da resposta da página inicial.]{#web-authentication-username-claim-c explanation="O tipo de conteúdo não indica a identidade usada no login."}
:::

## Comparando fatores de autenticação

Um **fator** é um tipo de prova. Uma senha é algo que o usuário sabe. Uma chave de segurança cadastrada fornece uma prova baseada em algo que o usuário possui. Usar a senha e uma chave cadastrada separada fornece dois tipos de evidência.

:::single-choice{#web-authentication-independent-factors} Qual exemplo combina conhecimento e posse?

::option[Uma senha e uma chave de segurança cadastrada.]{#web-authentication-independent-factors-a .correct explanation="Um fator verifica o que a pessoa sabe, e o outro verifica se ela tem acesso à chave."}
::option[Uma senha e outra senha memorizada.]{#web-authentication-independent-factors-b explanation="As duas são exemplos de algo que a pessoa sabe."}
::option[Um nome de usuário e um título de página.]{#web-authentication-independent-factors-c explanation="Esses rótulos dão pouca evidência de identidade."}
:::

## Entendendo o que um login bem-sucedido confirma

Depois de verificar a prova, o serviço pode permitir que o usuário inicie uma sessão. A verificação de identidade confirma qual conta o serviço considera conectada. Para saber o que a conta pode fazer, o serviço aplica suas regras de acesso a cada recurso solicitado.

:::single-choice{#web-authentication-auth-limit} Uma conta fez login com sucesso e solicita uma página de administração. O que deve acontecer em seguida?

::option[Toda conta conectada deve receber a página automaticamente.]{#web-authentication-auth-limit-a explanation="A conta ainda precisa da permissão exigida pela página."}
::option[O título original da página deve determinar o acesso.]{#web-authentication-auth-limit-b explanation="O título não contém as permissões da conta."}
::option[A aplicação deve verificar se a conta pode acessar aquele recurso.]{#web-authentication-auth-limit-c .correct explanation="Verificar a identidade e decidir o acesso ao recurso respondem a perguntas diferentes."}
:::

## Resumo

Agora você consegue explicar o que uma decisão de autenticação confirma.

1. Distinga a identidade declarada da prova apresentada.
2. Reconheça dois tipos diferentes de fatores de autenticação.
3. Use a política de autorização do serviço para decidir o acesso a cada recurso.
