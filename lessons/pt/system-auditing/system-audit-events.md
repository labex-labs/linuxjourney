---
lesson_id: "system-audit-events"
course_id: "system-auditing"
lang: "pt"
order_index: 1
title: "Eventos de auditoria"
description: "Aprenda a escolher eventos de auditoria que respondam a uma pergunta sobre um arquivo protegido."
meta_title: "Eventos de auditoria - Auditoria de sistemas"
meta_description: "Aprenda a escolher eventos de auditoria que respondam a uma pergunta sobre um arquivo protegido."
meta_keywords: "eventos de auditoria, arquivos protegidos, auditoria de sistemas, cibersegurança, Linux Journey"
---

Um log de serviço pode informar que alguém abriu uma página. Um **registro de auditoria** pode descrever uma ação que o sistema foi configurado para observar, como uma gravação na configuração de um serviço. Comece decidindo qual ação importa e de quais informações você precisa para analisá-la.

## Formulando uma pergunta de auditoria

Imagine que a configuração do serviço web determine quem pode abrir uma pré-visualização. Você quer revisar as alterações nesse arquivo. Um registro útil deve identificar o objeto, a operação, o horário, a conta envolvida e o resultado. Cada campo ajuda a reconstruir uma parte da ação.

:::single-choice{#system-audit-events-choose-object} O que um registro de auditoria deve identificar para essa revisão?

::option[Apenas a quantidade de requisições web daquele dia.]{#system-audit-events-choose-object-b explanation="O volume de requisições descreve outra atividade."}
::option[O arquivo de configuração que foi o alvo.]{#system-audit-events-choose-object-a .correct explanation="Identificar o objeto permite distinguir essa alteração de gravações em outros arquivos."}
::option[Apenas o tipo de operação, como gravação.]{#system-audit-events-choose-object-c explanation="A operação mostra o que foi tentado. O arquivo de destino indica se a tentativa interessa à revisão."}
:::

## Lendo o resultado

Um registro pode descrever uma gravação bem-sucedida ou uma tentativa malsucedida. Considere tanto a operação quanto o resultado. Uma gravação negada pode servir de evidência da tentativa. A conclusão difere da que você tiraria de uma gravação bem-sucedida.

:::single-choice{#system-audit-events-operation-result} Um registro indica uma tentativa de gravar na configuração e um resultado de acesso negado. O que ele mostra?

::option[A tentativa de gravação registrada foi bloqueada.]{#system-audit-events-operation-result-b .correct explanation="A operação e o resultado juntos descrevem a ação observada."}
::option[O arquivo certamente foi substituído.]{#system-audit-events-operation-result-a explanation="Uma operação negada não comprova uma modificação bem-sucedida."}
::option[A página esperada retornou HTTP 200.]{#system-audit-events-operation-result-c explanation="O registro não descreve uma requisição à página."}
:::

## Conferindo a cobertura

O sistema de auditoria registra apenas os eventos que seus mecanismos e suas políticas conseguem observar. Antes de usar uma busca vazia como evidência, confira se a política cobria o caminho, as operações e o horário corretos. Registre qual fonte você consultou.

:::single-choice{#system-audit-events-empty-audit} Você não encontra registros de gravação no log selecionado. O que verificar antes de concluir que nenhuma gravação ocorreu?

::option[Contar quantos editores estão instalados.]{#system-audit-events-empty-audit-a explanation="Os programas instalados não indicam a cobertura da auditoria."}
::option[Pesquisar no mesmo período apenas por uma segunda conta.]{#system-audit-events-empty-audit-b explanation="Uma nova busca pode ajudar se você já sabe que a coleta funciona. Primeiro confirme se os eventos relevantes poderiam ter sido registrados."}
::option[Verificar a política e o intervalo de tempo disponível.]{#system-audit-events-empty-audit-c .correct explanation="Uma lacuna na cobertura pode deixar a busca sem resultados mesmo que tenha havido atividade."}
:::

## Resumo

Agora você consegue selecionar evidências de auditoria para um recurso protegido.

1. Identifique a operação e o objeto que precisam ser revisados.
2. Leia o resultado registrado junto com a operação solicitada.
3. Confira a cobertura antes de usar uma busca vazia como evidência.
