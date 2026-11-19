---
lesson_id: "incident-containment"
course_id: "incident-response"
lang: "pt"
order_index: 4
title: "Contenção"
description: "Aprenda a comparar opções autorizadas de contenção considerando o objetivo, o impacto e as evidências necessárias."
meta_title: "Contenção - Resposta a incidentes"
meta_description: "Aprenda a comparar opções autorizadas de contenção considerando o objetivo, o impacto e as evidências necessárias."
meta_keywords: "contenção, resposta a incidentes, cibersegurança, Linux Journey"
---

A **contenção** é uma medida de curto prazo para limitar os danos enquanto a equipe investiga. A medida adequada depende do que foi afetado e de quais acessos as pessoas ainda precisam.

## Definindo o que restringir

Imagine que um painel interno de pré-visualização esteja acessível por uma rota pública, enquanto a página inicial precisa continuar aberta. Uma opção é restringir a rota da pré-visualização. Uma medida mais ampla é tirar o site inteiro do ar. Compare o que mudaria em cada caso.

:::single-choice{#incident-containment-narrow-action} Qual opção atende melhor ao objetivo de bloquear o acesso público à pré-visualização e manter a página inicial disponível?

::option[Desativar todas as rotas públicas, independentemente da finalidade.]{#incident-containment-narrow-action-b explanation="Isso também tiraria a página inicial do ar."}
::option[Restringir a rota de pré-visualização afetada e verificar os dois caminhos.]{#incident-containment-narrow-action-a .correct explanation="Isso trata a exposição relatada e confirma que o serviço necessário continua disponível."}
::option[Mudar o rótulo do serviço de pré-visualização.]{#incident-containment-narrow-action-c explanation="Mudar um rótulo não impede que as requisições cheguem ao serviço."}
:::

## Planejando a preservação das evidências e do acesso

Consulte o plano de resposta e as pessoas autorizadas a fazer a mudança. Registre quem a aprovou, a duração prevista e quais evidências devem ser preservadas primeiro, se as circunstâncias permitirem. Considere se a medida pode interromper os logs do serviço ou bloquear o acesso de quem investiga.

:::single-choice{#incident-containment-action-impact} Uma medida de isolamento proposta também pode impedir que a equipe de investigação obtenha os registros. O que deve ser avaliado?

::option[O que preservar e como manter o acesso das pessoas autorizadas a responder ao incidente.]{#incident-containment-action-impact-b .correct explanation="Isso leva em conta o objetivo da contenção e as necessidades da investigação."}
::option[Apenas se o arquivo de configuração tem um nome curto.]{#incident-containment-action-impact-a explanation="O nome não preserva os registros nem o acesso."}
::option[Se é preciso publicar credenciais para que todos possam se reconectar.]{#incident-containment-action-impact-c explanation="As credenciais devem continuar protegidas e o acesso deve permanecer controlado."}
:::

## Verificando a medida de contenção

Confira se o caminho indevido foi bloqueado. Teste também um caminho que deve continuar acessível para entender possíveis efeitos colaterais. Anote quando você aplicou a medida e quando a equipe deve reavaliá-la. A contenção pode funcionar enquanto a causa ainda está em investigação.

:::single-choice{#incident-containment-containment-success} A rota pública de pré-visualização está bloqueada e a página inicial ainda funciona. Qual afirmação tem respaldo?

::option[A causa raiz foi definitivamente corrigida.]{#incident-containment-containment-success-a explanation="As verificações confirmam a restrição de acesso. A correção da causa ainda precisa ser demonstrada."}
::option[Todos os caminhos possíveis para a pré-visualização foram testados.]{#incident-containment-containment-success-b explanation="Os testes cobrem os caminhos específicos que foram usados."}
::option[O caminho público de pré-visualização testado está bloqueado e a página inicial necessária continua disponível.]{#incident-containment-containment-success-c .correct explanation="Isso relata o resultado dentro do escopo verificado."}
:::

## Resumo

Agora você consegue avaliar uma medida de contenção de curto prazo.

1. Identifique o caminho ou acesso que a medida deve restringir.
2. Confira a autorização, as evidências e os efeitos esperados.
3. Verifique a restrição prevista e o funcionamento do serviço essencial.
