---
lesson_id: "incident-timelines"
course_id: "incident-response"
lang: "pt"
order_index: 3
title: "Linhas do tempo de incidentes"
description: "Aprenda a reunir evidências em uma linha do tempo e a sinalizar horários incertos."
meta_title: "Linhas do tempo de incidentes - Resposta a incidentes"
meta_description: "Aprenda a reunir evidências em uma linha do tempo e a sinalizar horários incertos."
meta_keywords: "linhas do tempo de incidentes, fusos horários, resposta a incidentes, cibersegurança, Linux Journey"
---

Uma linha do tempo de incidente ordena observações de fontes diferentes. Use o mesmo fuso horário e mantenha o horário original visível nos registros. A sequência ajuda você a perguntar quais eventos podem estar relacionados.

## Convertendo um horário

Aqui, um relato sobre a web usa UTC e um registro de implantação usa um fuso duas horas à frente do UTC.

```text
Deployment record:  2026-11-19 11:17:00 +02:00
Web report:         2026-11-19 09:22:00 UTC
```

Em um sistema Linux com o comando date do GNU, a opção `-d` recebe o horário informado e `-u` pede a saída em UTC. O argumento que começa com `+` define o formato de exibição.

```bash
$ date -u -d '2026-11-19 11:17:00+02:00' '+%Y-%m-%d %H:%M:%S UTC'
```

O resultado é `2026-11-19 09:17:00 UTC`. No exemplo, isso ocorre cinco minutos antes do relato sobre a web.

:::single-choice{#incident-timelines-earlier-event} Qual registro ocorreu antes na linha do tempo com horários convertidos?

::option[O registro de implantação.]{#incident-timelines-earlier-event-a .correct explanation="A conversão dá 09:17 UTC, antes do relato das 09:22."}
::option[O relato sobre a web.]{#incident-timelines-earlier-event-b explanation="Antes da conversão, a hora parece menor porque os registros usam fusos diferentes."}
::option[Os dois ocorreram exatamente ao mesmo tempo.]{#incident-timelines-earlier-event-c explanation="Após a conversão, os horários têm uma diferença de cinco minutos."}
:::

![Saída do GNU date convertendo 11:17 no fuso +02:00 para 09:17 UTC](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-timelines/normalize-utc.png)

## Distinguindo observações de estimativas

Um relato pode dizer que a primeira falha ocorreu por volta de 09:19. Mantenha esse horário como estimativa. O momento em que um usuário relata a falha pode ser diferente do momento da primeira requisição malsucedida. Anote em cada linha a fonte e a precisão do horário.

:::single-choice{#incident-timelines-estimated-time} Uma pessoa da equipe informa que o evento aconteceu por volta de 09:19. Como registrar isso?

::option[Como exatamente 09:19:00, confirmado por um log.]{#incident-timelines-estimated-time-a explanation="A fonte fornece uma estimativa."}
::option[Como um evento sem fonte.]{#incident-timelines-estimated-time-c explanation="A fonte ajuda a determinar quanto confiar no horário."}
::option[Como um horário aproximado atribuído ao relato.]{#incident-timelines-estimated-time-b .correct explanation="Assim você preserva o que a fonte disse e o grau de precisão."}
:::

## Ordenando eventos sem atribuir uma causa

Uma implantação pode acontecer antes de um problema no serviço sem tê-lo causado. Verifique se a rota afetada mudou e se outros sinais sustentam a relação. Mantenha as dúvidas em aberto junto à linha do tempo.

:::single-choice{#incident-timelines-timeline-cause} O que a ordem dos eventos estabelece por si só?

::option[A implantação causou a falha no caminho público.]{#incident-timelines-timeline-cause-a explanation="A ordem indica uma possibilidade. Para estabelecer a causa, são necessárias mais evidências."}
::option[A implantação registrada antecede o relato sobre a web.]{#incident-timelines-timeline-cause-c .correct explanation="Essa é a relação de tempo demonstrada pelos registros."}
::option[Nenhum outro evento pode ser relevante.]{#incident-timelines-timeline-cause-b explanation="A linha do tempo contém apenas as observações selecionadas."}
:::

## Resumo

Agora você consegue montar uma linha do tempo que mostra tanto as evidências quanto as incertezas.

1. Converta os horários registrados para um fuso comum.
2. Indique a fonte de cada horário e marque as estimativas.
3. Use a sequência para escolher as próximas verificações.
