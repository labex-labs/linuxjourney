---
lesson_id: "web-authorization"
course_id: "web-security"
lang: "pt"
order_index: 6
title: "Autorização"
description: "Aprenda a comparar a requisição de um usuário autenticado com a política de acesso de uma aplicação."
meta_title: "Autorização - Segurança web"
meta_description: "Aprenda a comparar a requisição de um usuário autenticado com a política de acesso de uma aplicação."
meta_keywords: "autorização, controle de acesso, segurança web, cibersegurança, Linux Journey"
---

Um usuário pode fazer login e ainda não ter permissão para uma ação específica. A **autorização** decide se uma conta pode realizar determinada ação sobre um recurso.

## Lendo uma política

Uma **função** é um conjunto de permissões com um nome. A política deste exercício se aplica a um serviço de pré-visualização.

```text
Role       View published page   Edit draft
Reader    Yes                   No
Editor    Yes                   Yes
```

Leia a linha da função do usuário e a coluna da operação solicitada. Um editor pode ver a página publicada e editar um rascunho. Um leitor pode ver a página publicada.

:::single-choice{#web-authorization-read-policy} Um leitor autenticado pede para editar um rascunho. O que diz a tabela?

::option[A ação é proibida para a função Reader.]{#web-authorization-read-policy-b .correct explanation="A linha Reader mostra No na coluna Edit draft."}
::option[A ação é permitida para qualquer conta autenticada.]{#web-authorization-read-policy-a explanation="A permissão para essa ação depende da função."}
::option[O usuário precisa mudar para HTTPS para ganhar permissão de edição.]{#web-authorization-read-policy-c explanation="A proteção do transporte não concede permissões na aplicação."}
:::

## Verificando o recurso certo

Muitos sistemas concedem permissões diferentes para cada recurso. Uma pessoa com função de edição pode alterar rascunhos do próprio projeto e apenas ler as páginas de outro. A verificação precisa identificar tanto a operação quanto o recurso de destino.

:::single-choice{#web-authorization-target-resource} Maya pode editar o Project A. O que determina se ela pode editar o Project B?

::option[O título do Project A.]{#web-authorization-target-resource-b explanation="O título não indica quem pode acessar outro projeto."}
::option[O fato de o login ter funcionado.]{#web-authorization-target-resource-c explanation="A autenticação identifica a conta de Maya. A permissão para o recurso ainda precisa ser verificada."}
::option[A política de permissões para Maya no Project B.]{#web-authorization-target-resource-a .correct explanation="A permissão anterior abrangia um recurso específico."}
:::

## Aplicando a política no serviço

A interface pode ocultar os controles de edição para leitores. O servidor ainda deve aplicar a política sempre que recebe uma requisição. Verifique os casos permitidos e negados por meio de ações normais e autorizadas no serviço de prática.

:::single-choice{#web-authorization-decision-location} Uma aplicação oculta o botão Edit para leitores. Onde a política de acesso também precisa ser aplicada?

::option[Apenas no navegador, ao decidir que botão mostrar.]{#web-authorization-decision-location-a explanation="O navegador controla a interface. O serviço toma a decisão de acesso para a requisição recebida."}
::option[No serviço que recebe a operação solicitada.]{#web-authorization-decision-location-c .correct explanation="O serviço pode avaliar a conta, a ação e o recurso pretendido a cada requisição."}
::option[Apenas na página que lista as funções.]{#web-authorization-decision-location-b explanation="Exibir o nome da função não impede uma operação restrita."}
:::

## Resumo

Agora você consegue analisar uma decisão de acesso na aplicação.

1. Associe a função da conta à ação solicitada.
2. Inclua o recurso específico na verificação.
3. Confirme que o serviço aplica a política às requisições.
