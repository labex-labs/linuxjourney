---
lesson_id: "network-monitoring-alerts"
course_id: "network-monitoring"
lang: "pt"
order_index: 6
title: "Alertas de rede"
description: "Aprenda a relacionar um alerta de rede às evidências necessárias para decidir como agir na defesa do sistema."
meta_title: "Alertas de rede - Monitoramento de redes"
meta_description: "Aprenda a relacionar um alerta de rede às evidências necessárias para decidir como agir na defesa do sistema."
meta_keywords: "alertas de rede, monitoramento de redes, cibersegurança, Linux Journey"
---

Um alerta de rede informa que uma condição de monitoramento foi atendida. Leia a condição e identifique sua fonte antes de decidir o que aconteceu. Os alertas podem indicar tráfego inesperado, falhas repetidas ou ausência de observações.

## Entendendo o escopo do alerta

O alerta simulado abaixo se baseia em registros DNS. Ele agrupa as falhas por cliente em uma janela de cinco minutos.

```text
Window: 09:20–09:25 UTC
Client: 192.0.2.10
Condition: at least 10 failed name lookups
Observed: 12 failures
```

Isso dá motivo para examinar as consultas e seus resultados. O programa que fez as consultas ainda não foi identificado.

:::single-choice{#network-monitoring-alerts-alert-scope} O que o alerta observou diretamente?

::option[Doze consultas malsucedidas para o cliente registrado naquela janela.]{#network-monitoring-alerts-alert-scope-b .correct explanation="O alerta informa essa contagem para esse cliente naquele intervalo."}
::option[Uma perda de dados confirmada.]{#network-monitoring-alerts-alert-scope-a explanation="A regra conta falhas na resolução de nomes."}
::option[Doze clientes diferentes.]{#network-monitoring-alerts-alert-scope-c explanation="O alerta agrupa registros de um único endereço de cliente."}
:::

## Procurando um registro relacionado no host

Imagine que a maioria das falhas envolva `preview.example`. Um log do serviço no cliente pode indicar que uma configuração antiga provocou novas tentativas. Procure registros de horários próximos no programa que você espera que faça as consultas. Confira o rótulo do host no monitoramento antes de atribuir a atividade.

:::single-choice{#network-monitoring-alerts-evidence-choice} Qual registro ajudaria a verificar se um serviço estava repetindo a consulta?

::option[Um acesso posterior à página pública em outro host.]{#network-monitoring-alerts-evidence-choice-b explanation="O endpoint e o horário não correspondem ao padrão investigado."}
::option[Uma lista de aplicativos instalados sem horários de atividade.]{#network-monitoring-alerts-evidence-choice-c explanation="Os programas instalados, por si só, não mostram qual deles fez a consulta."}
::option[Um log do serviço que indique a falha na mesma consulta durante a janela do alerta.]{#network-monitoring-alerts-evidence-choice-a .correct explanation="Esse log pode relacionar o padrão de consultas ao programa."}
:::

## Registrando a próxima decisão

Se o log do serviço corresponder ao alerta, registre o motivo e verifique uma consulta representativa após corrigir a configuração aprovada. Se as evidências ainda forem incompletas, indique o que falta. Mantenha juntos o alerta, o registro de apoio e o resultado da verificação.

:::single-choice{#network-monitoring-alerts-uncertainty} Você tem o alerta de DNS, mas nenhum registro correspondente no host. O que deve relatar?

::option[O programa exato foi identificado.]{#network-monitoring-alerts-uncertainty-a explanation="O registro de DNS sozinho não identificou o processo."}
::option[O padrão de consultas foi confirmado e o programa responsável é desconhecido.]{#network-monitoring-alerts-uncertainty-c .correct explanation="O relato preserva a observação e a dúvida que permanece."}
::option[O alerta não descreve absolutamente nada.]{#network-monitoring-alerts-uncertainty-b explanation="Ele ainda descreve a condição observada pelo resolvedor."}
:::

## Verificando um padrão esperado de novas tentativas

Imagine que a equipe tenha agendado uma tarefa que consulta repetidamente um nome de host de teste. Compare o horário programado, os nomes nos registros DNS e o próprio log da tarefa. Se vários campos coincidirem, isso reforça a explicação. Continue investigando as falhas sem correspondência.

:::single-choice{#network-monitoring-alerts-final-application} Qual descoberta daria mais força à explicação da tarefa agendada?

::option[O alerta veio de um host que executa outras tarefas agendadas.]{#network-monitoring-alerts-final-application-c explanation="Esse contexto não identifica o programa que fez as consultas."}
::option[O log da tarefa mostra o mesmo nome de host e novas tentativas na janela do alerta.]{#network-monitoring-alerts-final-application-a .correct explanation="A coincidência de nome e horário ajuda a ligar o padrão observado à tarefa conhecida."}
::option[A tarefa estava agendada para algum momento daquele dia.]{#network-monitoring-alerts-final-application-b explanation="Saber apenas o dia não confirma a janela do alerta nem os nomes consultados."}
:::

## Resumo

Agora você consegue escolher uma próxima verificação com base em um alerta de rede.

1. Identifique a regra de detecção e seu escopo.
2. Escolha um registro relacionado para testar uma explicação.
3. Documente a observação e a incerteza que permanece.
