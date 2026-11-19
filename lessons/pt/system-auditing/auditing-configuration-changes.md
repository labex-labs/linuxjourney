---
lesson_id: "auditing-configuration-changes"
course_id: "system-auditing"
lang: "pt"
order_index: 5
title: "Alterações de configuração"
description: "Aprenda a relacionar uma mudança aprovada, uma diferença de arquivo e um evento de auditoria."
meta_title: "Alterações de configuração - Auditoria de sistemas"
meta_description: "Aprenda a relacionar uma mudança aprovada, uma diferença de arquivo e um evento de auditoria."
meta_keywords: "alterações de configuração, auditoria de sistemas, cibersegurança, Linux Journey"
---

Um chamado de mudança registra uma ação planejada. A comparação de arquivos mostra o que está diferente agora. Um evento de auditoria descreve uma ação observada dentro da cobertura da auditoria. Use essas três informações para avaliar o que você pode afirmar sobre uma alteração de configuração.

## Identificando a mudança esperada

Leia este registro simulado de manutenção.

```text
Approved: change banner.txt mode to 640
Window: 09:00–09:30 UTC
Host: web-01
```

Ele informa qual arquivo e qual propriedade foram aprovados para alteração. Uma diferença em outro lugar precisa de uma explicação própria, mesmo que apareça na mesma janela.

:::single-choice{#auditing-configuration-changes-approve-scope} Qual mudança corresponde à ação aprovada?

::option[O conteúdo de site.conf mudou em web-01.]{#auditing-configuration-changes-approve-scope-b explanation="Esse arquivo de configuração está fora do escopo da aprovação."}
::option[O arquivo banner.txt desapareceu de outro host.]{#auditing-configuration-changes-approve-scope-c explanation="Tanto a operação relatada quanto o host são diferentes."}
::option[As permissões de banner.txt passaram a 640 em web-01.]{#auditing-configuration-changes-approve-scope-a .correct explanation="A mudança corresponde ao arquivo, à propriedade, ao host e ao resultado aprovado no registro."}
:::

## Comparando observações

Uma comparação mostra que as permissões do banner mudaram e que os bytes de `site.conf` também mudaram. Outro registro, um evento de auditoria das 09:15, mostra uma gravação em `site.conf` no host `web-01`. O evento dá um horário para investigar. A aprovação da ação ainda precisa ser confirmada.

:::single-choice{#auditing-configuration-changes-source-comparison} Qual conclusão decorre das duas observações sobre site.conf?

::option[A gravação foi autorizada porque ocorreu dentro da janela.]{#auditing-configuration-changes-source-comparison-a explanation="O chamado descreve outra ação."}
::option[A gravação registrada e a mudança nos bytes indicam que vale revisar o arquivo.]{#auditing-configuration-changes-source-comparison-b .correct explanation="A comparação revela a diferença e o evento de auditoria delimita o horário."}
::option[A alteração do banner causou a gravação.]{#auditing-configuration-changes-source-comparison-c explanation="Essas observações não demonstram que uma ação causou a outra."}
:::

## Escrevendo a nota de revisão

Indique qual diferença corresponde ao planejamento e qual ainda está sem explicação. Inclua o arquivo, o host, o horário e uma referência à fonte. Um próximo passo útil é comparar a configuração atual com a cópia aprovada e verificar se outra mudança autorizada cobre a diferença.

:::single-choice{#auditing-configuration-changes-useful-review} O que o repasse deve informar sobre site.conf?

::option[Descrever a diferença, citar a gravação observada e pedir o registro da aprovação correspondente.]{#auditing-configuration-changes-useful-review-c .correct explanation="A nota preserva as evidências e a questão em aberto."}
::option[Marcar a alteração como aprovada e omitir o caminho.]{#auditing-configuration-changes-useful-review-a explanation="Isso elimina a identificação do arquivo e presume uma aprovação que os registros não mostram."}
::option[Atribuir a alteração a quem fez a mudança do banner.]{#auditing-configuration-changes-useful-review-b explanation="Os registros não permitem fazer essa atribuição."}
:::

## Comparando dois chamados de manutenção

Outro chamado autoriza uma edição posterior de site.conf. Compare o horário observado, o host de destino e o arquivo com o chamado antes de encerrar a revisão. Uma mudança aprovada para o arquivo certo ainda pode deixar um evento anterior sem explicação.

:::single-choice{#auditing-configuration-changes-final-application} O chamado cobre site.conf em web-01 das 09:40 às 10:00. Qual dúvida permanece sobre a gravação registrada às 09:15?

::option[Se site.conf existe fora do sistema de chamados.]{#auditing-configuration-changes-final-application-b explanation="A comparação dos arquivos já mostra a configuração."}
::option[Se o chamado posterior deve explicar automaticamente todas as gravações anteriores.]{#auditing-configuration-changes-final-application-c explanation="A aprovação vale para a ação e o horário especificados."}
::option[Se outra aprovação cobre aquela gravação anterior.]{#auditing-configuration-changes-final-application-a .correct explanation="O host e o caminho correspondem, mas o horário registrado fica fora da janela autorizada."}
:::

## Resumo

Agora você consegue reconstruir o que se sabe sobre uma alteração de configuração.

1. Leia o escopo previsto na mudança aprovada.
2. Use comparações e eventos de auditoria para descrever o que foi observado.
3. Explique o que falta comprovar e escolha a próxima verificação.
