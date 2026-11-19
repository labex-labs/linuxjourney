---
lesson_id: "incident-reports"
course_id: "incident-response"
lang: "pt"
order_index: 6
title: "Relatórios de incidentes"
description: "Aprenda a escrever uma atualização breve com base nas evidências observadas e nas dúvidas em aberto."
meta_title: "Relatórios de incidentes - Resposta a incidentes"
meta_description: "Aprenda a escrever uma atualização breve com base nas evidências observadas e nas dúvidas em aberto."
meta_keywords: "relatórios de incidentes, resposta a incidentes, cibersegurança, Linux Journey"
---

Um relatório curto ajuda outra pessoa a assumir o incidente sem reconstruir toda a investigação. Inclua o serviço afetado, algumas observações com horários e a próxima ação.

## Relatando as observações

Veja três registros simulados do incidente no serviço.

```text
09:17 UTC  Deployment record: version 3 reached production
09:22 UTC  Visitor-path check: homepage returned 503
09:31 UTC  After rollback: version 2, homepage returned 200
```

Os registros descrevem uma mudança, uma falha e uma verificação bem-sucedida após a recuperação. Inclua o caminho afetado e o horário. Preserve os detalhes do que foi testado.

:::single-choice{#incident-reports-report-claim} O que você pode afirmar diretamente a partir dos registros?

::option[A verificação da página inicial falhou às 09:22 e funcionou depois do rollback.]{#incident-reports-report-claim-b .correct explanation="Isso resume os resultados observados e a ordem em que ocorreram."}
::option[A versão 3 certamente causou uma falha no banco de dados.]{#incident-reports-report-claim-a explanation="Os registros não mostram como a falha ocorreu."}
::option[Todos os usuários foram afetados durante a janela inteira.]{#incident-reports-report-claim-c explanation="Os resultados apresentados não medem cada requisição."}
:::

![Evidências simuladas de um incidente com uma mudança em produção, um erro 503 e uma verificação bem-sucedida após a recuperação](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-reports/evidence-timeline.png)

## Explicando a incerteza

Se uma requisição funciona depois de um rollback, vale investigar a implantação. Mantenha a causa em aberto até que as evidências a sustentem. Por exemplo, a pessoa responsável pela manutenção pode comparar os logs de serviço das duas versões na janela da requisição que falhou.

:::single-choice{#incident-reports-uncertainty-statement} Qual frase descreve uma questão em aberto?

::option[Não há nada que valha investigar.]{#incident-reports-uncertainty-statement-b explanation="Os registros da release e do erro indicam o que vale verificar a seguir."}
::option[O serviço ficou indisponível para sempre.]{#incident-reports-uncertainty-statement-c explanation="O sucesso posterior contradiz essa afirmação no caso da requisição de teste."}
::option[A causa do erro 503 ainda é desconhecida.]{#incident-reports-uncertainty-statement-a .correct explanation="As evidências mostram uma falha e uma verificação de recuperação. A causa ainda precisa ser demonstrada."}
:::

## Indicando a próxima tarefa

Informe quem pode assumir a próxima ação, quais registros a pessoa deve procurar e qual resultado responderia à dúvida em aberto. Mantenha segredos e dados pessoais fora de atualizações destinadas a um público amplo. Um relatório curto pode indicar onde encontrar as evidências protegidas para pessoas autorizadas.

:::single-choice{#incident-reports-useful-handoff} Qual ação faz mais sentido a seguir nesse caso?

::option[Pedir uma captura de tela genérica, sem identificar horário nem serviço.]{#incident-reports-useful-handoff-a explanation="Isso não especifica as evidências necessárias para investigar a falha."}
::option[Pedir à pessoa responsável pelo serviço que examine os logs da versão 3 na janela da falha na página inicial.]{#incident-reports-useful-handoff-c .correct explanation="A ação indica uma fonte e um período específicos para investigar a dúvida."}
::option[Pedir que a pessoa responsável repita apenas a verificação já bem-sucedida da versão 2.]{#incident-reports-useful-handoff-b explanation="Isso pode confirmar a recuperação outra vez. A falha anterior na versão 3 continua sem explicação."}
:::

## Registrando o alcance da recuperação

Um relatório pode precisar registrar o que foi observado na recuperação e indicar que o tamanho do impacto ainda é desconhecido. Uma verificação bem-sucedida após o rollback confirma a recuperação da página inicial pelo caminho testado. Para estimar quantos visitantes foram afetados, ainda é preciso consultar contagens de requisições ou outras observações adequadas da janela da falha.

:::single-choice{#incident-reports-final-application} Qual repasse descreve com precisão os dois tipos de evidência?

::option[O serviço voltou a funcionar para todos os visitantes porque uma requisição retornou 200.]{#incident-reports-final-application-b explanation="A requisição bem-sucedida verifica somente o caminho e o horário testados."}
::option[A verificação que falhou deve ser removida do relatório porque a recuperação funcionou.]{#incident-reports-final-application-c explanation="A falha anterior faz parte das evidências do incidente."}
::option[A verificação da página inicial voltou a funcionar após o rollback, e o total de requisições afetadas ainda é desconhecido.]{#incident-reports-final-application-a .correct explanation="O relato distingue a recuperação verificada de uma contagem que os registros disponíveis não fornecem."}
:::

Para um exercício mais longo depois de praticar a análise de evidências em pacotes e hosts, veja [Revisão dos fundamentos de SOC](https://labex.io/courses/project-soc-foundations-review).

## Resumo

Agora você consegue repassar um incidente com fatos, dúvidas em aberto e uma próxima ação.

1. Indique o caminho afetado e a sequência de observações.
2. Distinga uma causa suspeita das evidências confirmadas.
3. Atribua uma tarefa de acompanhamento com uma fonte e uma janela de tempo.
