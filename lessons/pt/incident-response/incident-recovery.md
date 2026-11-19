---
lesson_id: "incident-recovery"
course_id: "incident-response"
lang: "pt"
order_index: 5
title: "Recuperação"
description: "Aprenda a verificar se o serviço voltou ao estado aprovado antes de concluir a recuperação."
meta_title: "Recuperação - Resposta a incidentes"
meta_description: "Aprenda a verificar se o serviço voltou ao estado aprovado antes de concluir a recuperação."
meta_keywords: "recuperação, verificação de serviços, resposta a incidentes, cibersegurança, Linux Journey"
---

A **recuperação** restaura o serviço esperado e verifica se ele continua utilizável. Um processo recém-iniciado é um primeiro sinal. A equipe também precisa confirmar que a configuração, as dependências e o comportamento percebido pelos usuários correspondem ao estado desejado.

## Identificando o estado restaurado

Registre a versão candidata aprovada e sua configuração. Se um serviço foi isolado, verifique quais acessos devem continuar restritos. Reabrir um caminho pode alterar o alcance da contenção.

:::single-choice{#incident-recovery-restore-target} Qual resultado indica se você restaurou a versão desejada?

::option[Um horário recente registrado em qualquer máquina virtual sem relação com o incidente.]{#incident-recovery-restore-target-b explanation="Isso não identifica o serviço restaurado."}
::option[Somente uma lista de pacotes disponíveis.]{#incident-recovery-restore-target-c explanation="A lista de pacotes disponíveis não indica o que está atendendo às requisições."}
::option[Uma resposta ou um registro de implantação que identifica a versão aprovada no destino.]{#incident-recovery-restore-target-a .correct explanation="Isso associa o serviço em execução à versão escolhida pela equipe."}
:::

## Verificando novamente o problema relatado

No incidente simulado, visitantes viram o código `503` na página inicial pública. Após a restauração, consulte o mesmo caminho a partir de um local de teste adequado. Confirme que a requisição obteve a resposta esperada e acompanhe os erros das requisições recentes. Uma pré-visualização interna bem-sucedida não testa o caminho público.

:::single-choice{#incident-recovery-verify-original-path} Qual teste indica melhor que o sintoma original percebido pelo usuário desapareceu?

::option[Verificar apenas se o binário do serviço existe.]{#incident-recovery-verify-original-path-a explanation="O arquivo pode existir sem atender às requisições públicas."}
::option[Verificar a página inicial pública a partir do caminho usado pelos clientes afetados.]{#incident-recovery-verify-original-path-b .correct explanation="Isso repete a verificação que havia falhado."}
::option[Verificar apenas a pré-visualização interna.]{#incident-recovery-verify-original-path-c explanation="Esse caminho é diferente da rota afetada."}
:::

## Continuando a observar

Combine um período curto de observação e critérios de sucesso. Acompanhe sinais relevantes, como erros, latência ou recusas de acesso. Anote as limitações, as ações pendentes e o horário da próxima revisão. Guarde as evidências da recuperação junto com o registro do incidente.

:::single-choice{#incident-recovery-observation-period} A primeira verificação passa, mas a falha era intermitente. O que você deve fazer antes de encerrar a verificação da recuperação?

::option[Continuar acompanhando os sinais combinados durante a janela de observação.]{#incident-recovery-observation-period-c .correct explanation="Isso ajuda a confirmar que o serviço restaurado continua funcionando como esperado."}
::option[Encerrar imediatamente porque uma resposta chegou.]{#incident-recovery-observation-period-a explanation="Uma única observação pode deixar passar uma falha intermitente."}
::option[Descartar todos os dados de comparação.]{#incident-recovery-observation-period-b explanation="Os resultados anteriores mostram o que melhorou."}
:::

## Resumo

Agora você consegue verificar o estado do serviço e o comportamento percebido pelo usuário após a recuperação.

1. Identifique a versão e a configuração aprovadas.
2. Teste novamente o sintoma percebido pelo usuário.
3. Observe os sinais combinados antes de encerrar a verificação da recuperação.
