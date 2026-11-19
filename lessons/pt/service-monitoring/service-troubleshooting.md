---
lesson_id: "service-troubleshooting"
course_id: "service-monitoring"
lang: "pt"
order_index: 7
title: "Diagnóstico de problemas em serviços"
description: "Aprenda a escolher a próxima verificação diante de uma interrupção, de erros de dependência ou de requisições lentas."
meta_title: "Diagnóstico de problemas em serviços - Monitoramento de serviços"
meta_description: "Aprenda a escolher a próxima verificação diante de uma interrupção, de erros de dependência ou de requisições lentas."
meta_keywords: "diagnóstico de serviços, monitoramento de serviços, DevOps, Linux Journey"
---

Comece com um sintoma concreto, como uma falha na requisição à página inicial. Depois, compare observações feitas em horários próximos e a partir do local relevante para os usuários.

## Quando um servidor para

No primeiro caso, o navegador informa que a conexão foi recusada e o contêiner do serviço exibe `Exited (1)`. As duas observações justificam investigar por que o programa parou. Consulte os logs que foram preservados. Anote o horário de encerramento antes de compará-lo com outros eventos.

:::single-choice{#service-troubleshooting-stopped-case} Qual verificação tem mais chance de explicar por que o processo parou?

::option[Consultar a mesma página inicial para obter um status mais recente.]{#service-troubleshooting-stopped-case-a explanation="Uma nova tentativa verifica o sintoma. Os logs preservados podem explicar por que o programa encerrou."}
::option[Ler as últimas linhas disponíveis do log do contêiner.]{#service-troubleshooting-stopped-case-b .correct explanation="As mensagens de inicialização ou encerramento podem mostrar em que ponto o programa parou."}
::option[Examinar os logs de outro contêiner em execução que usa a mesma imagem.]{#service-troubleshooting-stopped-case-c explanation="Esse contêiner tem outro histórico de execução e pode nunca ter encontrado a falha."}
:::

## Quando uma dependência falha

No segundo caso, o processo web está em execução, mas a página retorna um erro de servidor. O log indica que o tempo de espera se esgotou ao consultar o catálogo para a requisição `r17`. Isso dá motivo para examinar os registros da dependência para a mesma requisição. A primeira etapa pode funcionar mesmo se outro serviço estiver com problemas.

:::single-choice{#service-troubleshooting-dependency-case} Qual evidência você deve procurar a seguir para r17?

::option[O registro do catálogo para a mesma requisição e horário.]{#service-troubleshooting-dependency-case-a .correct explanation="Ele mostra o que aconteceu na chamada à dependência."}
::option[O tamanho da imagem Docker arquivada.]{#service-troubleshooting-dependency-case-b explanation="O tamanho não descreve o que aconteceu durante a chamada."}
::option[Uma verificação bem-sucedida da página inicial feita ontem e sem relação com o caso.]{#service-troubleshooting-dependency-case-c explanation="Essa verificação corresponde a outro momento e não explica a requisição."}
:::

## Quando as requisições ficam mais lentas

Uma terceira amostra mostra que a maioria das respostas funciona, mas os usuários relatam demora. A latência aumenta na mesma janela em que a fila dos workers cresce. Verifique a demanda e a atividade dos workers antes de atribuir uma causa. Se houver uma mudança, repita a verificação pelo caminho usado pelo público e volte a consultar os mesmos sinais.

:::single-choice{#service-troubleshooting-slow-case} Qual comparação indica melhor se a mudança ajudou nesse caso?

::option[Capturas do repositório do código-fonte antes e depois da mudança.]{#service-troubleshooting-slow-case-a explanation="As capturas não medem o tempo das requisições nem as filas."}
::option[O tamanho do cache em relação à quantidade de branches implantadas.]{#service-troubleshooting-slow-case-b explanation="Esses dados não explicam o tempo de espera relatado."}
::option[Tempos de requisição dos usuários e tamanho das filas dos workers em condições comparáveis antes e depois.]{#service-troubleshooting-slow-case-c .correct explanation="Isso verifica tanto o sintoma original quanto o possível limite de capacidade."}
:::

## Interpretando resultados diferentes

Imagine que uma verificação local funcione, mas os usuários continuem vendo erros. Registre o caminho que cada teste usou. Uma verificação local pode demonstrar que o processo responde no host, enquanto uma requisição do cliente pode revelar um problema no caminho até esse host.

:::single-choice{#service-troubleshooting-final-application} Qual resultado deve orientar a próxima verificação sobre os usuários afetados?

::option[Uma verificação feita pela rota e pelo local usados por esses usuários.]{#service-troubleshooting-final-application-a .correct explanation="Ela observa a parte do serviço em que o sintoma foi relatado."}
::option[Apenas o resultado do host.]{#service-troubleshooting-final-application-b explanation="O resultado ajuda a delimitar o problema, mas o caminho externo ainda precisa ser verificado."}
::option[A capacidade atual do registro de imagens.]{#service-troubleshooting-final-application-c explanation="O registro pode fornecer imagens enquanto a rota usada pelo público apresenta outro problema."}
:::

## Resumo

Agora você consegue escolher a próxima verificação com base nas evidências disponíveis.

1. Use o estado do processo e os logs para investigar uma interrupção.
2. Siga a requisição que falhou até a dependência.
3. Verifique a melhora a partir do sintoma original percebido pelo usuário.
