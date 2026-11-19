---
lesson_id: "incident-triage"
course_id: "incident-response"
lang: "pt"
order_index: 1
title: "Triagem de incidentes"
description: "Aprenda a usar o relato inicial de um incidente para delimitar a primeira investigação."
meta_title: "Triagem de incidentes - Resposta a incidentes"
meta_description: "Aprenda a usar o relato inicial de um incidente para delimitar a primeira investigação."
meta_keywords: "triagem de incidentes, impacto, resposta a incidentes, cibersegurança, Linux Journey"
---

Um relato inicial pode dizer que uma página falhou ou que um alerta disparou. **Triagem** significa decidir o que precisa de atenção primeiro. Anote o serviço afetado, o horário e o comportamento observado antes de escolher como responder.

## Lendo o relato

Uma pessoa da equipe escreveu este relato simulado.

```text
09:22 UTC: Visitors received 503 from the public homepage.
The staff preview still loaded during the same check.
First failure observed at approximately 09:19 UTC.
```

O relato indica duas rotas e duas observações diferentes. Confirme o resultado da página inicial pública e anote o horário e o endereço verificado.

:::single-choice{#incident-triage-affected-service} Qual sintoma deve orientar a primeira verificação?

::option[A pré-visualização da equipe retornando 503.]{#incident-triage-affected-service-b explanation="O relato diz que a pré-visualização ainda abriu."}
::option[A página inicial pública retornando 503.]{#incident-triage-affected-service-a .correct explanation="Esse é o caminho afetado identificado no relato."}
::option[Uma página ausente em um host sem relação com o incidente.]{#incident-triage-affected-service-c explanation="Esse caminho está fora do escopo do relato."}
:::

## Estimando o impacto

Verifique quantos usuários ou requisições foram afetados e se o serviço continua utilizável. Descubra se o evento ainda está acontecendo. Indique quando um valor é estimado até ter evidências melhores. Use o plano de resposta para decidir quem deve ser avisado.

:::single-choice{#incident-triage-triage-scope} Qual observação ajuda a decidir se o problema ainda é urgente?

::option[Uma verificação atual do caminho com falha e dos resultados das requisições recentes.]{#incident-triage-triage-scope-b .correct explanation="Isso mostra se o sintoma continua e até que ponto ele aparece."}
::option[A idade do primeiro commit do repositório.]{#incident-triage-triage-scope-a explanation="Isso não mostra o efeito atual."}
::option[Apenas a classificação de gravidade do relato original.]{#incident-triage-triage-scope-c explanation="A classificação inicial dá contexto. O impacto atual ajuda a decidir se o problema continua urgente."}
:::

## Escolhendo a primeira ação

Se a requisição atual também falhar, guarde o resultado e examine as mudanças recentes no serviço e os logs do período afetado. Um caminho alternativo que funciona ajuda a delimitar o problema. Trate a primeira explicação plausível como hipótese até reunir evidências.

:::single-choice{#incident-triage-first-next-step} O caminho público ainda falha e a pré-visualização da equipe ainda funciona. O que examinar a seguir?

::option[Todos os projetos da empresa sem relação com o incidente.]{#incident-triage-first-next-step-a explanation="O relato aponta para um serviço e um período mais específicos."}
::option[Um erro antigo escolhido ao acaso em outra data.]{#incident-triage-first-next-step-b explanation="Comece pelas evidências próximas à falha observada."}
::option[Os registros da rota pública durante a janela relatada.]{#incident-triage-first-next-step-c .correct explanation="Eles podem ajudar a distinguir um problema de roteamento de uma falha do serviço."}
:::

## Resumo

Agora você consegue definir uma primeira resposta ao relato de um incidente.

1. Identifique o caminho afetado, o horário e o sintoma.
2. Confira o impacto atual para os usuários.
3. Escolha a próxima fonte de evidências para o caminho afetado.
