---
lesson_id: "file-integrity-baselines"
course_id: "system-auditing"
lang: "pt"
order_index: 4
title: "Referências de integridade"
description: "Aprenda a interpretar um relatório de integridade e a decidir quando aprovar uma nova referência."
meta_title: "Referências de integridade - Auditoria de sistemas"
meta_description: "Aprenda a interpretar um relatório de integridade e a decidir quando aprovar uma nova referência."
meta_keywords: "referências de integridade, integridade de arquivos, auditoria de sistemas, cibersegurança, Linux Journey"
---

Uma **referência de integridade** é um registro confiável das propriedades esperadas dos arquivos em um momento conhecido. Uma verificação posterior pode comparar os arquivos atuais com essa referência e apontar diferenças.

## Lendo um relatório de diferenças

Este trecho simulado compara um host com seu último estado aprovado.

```text
File                      Property  Previous  Current
/etc/journey/site.conf    content   hash-A    hash-B
/etc/journey/banner.txt   mode      644       640
/etc/journey/site.prev    present   yes       no
```

A primeira linha mostra uma alteração nos bytes. A segunda mostra uma mudança de permissões. A terceira informa que um arquivo antes monitorado estava ausente durante a verificação.

:::single-choice{#file-integrity-baselines-report-mode} Qual linha registra uma mudança nas permissões de acesso?

::option[A linha de site.conf.]{#file-integrity-baselines-report-mode-a explanation="Ela informa que o hash do conteúdo mudou."}
::option[A linha de banner.txt.]{#file-integrity-baselines-report-mode-b .correct explanation="As permissões passaram de 644 para 640."}
::option[A linha de site.prev.]{#file-integrity-baselines-report-mode-c explanation="Essa linha informa se o caminho estava presente."}
:::

![Relatório simulado de integridade comparando conteúdo, permissões e presença de arquivos](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/file-integrity-baselines/reference-comparison.png)

## Verificando a referência

O relatório só é útil se a referência anterior for confiável. Guarde a identificação e a data de criação da referência. Um arquivo capturado quando já havia um problema pode levar a uma comparação enganosa. Pergunte qual estado aprovado a referência representa.

:::single-choice{#file-integrity-baselines-reference-source} Qual referência ajuda mais a revisar a configuração atual?

::option[Uma cópia anterior à mudança, registrada e aprovada.]{#file-integrity-baselines-reference-source-a .correct explanation="Ela fornece uma referência conhecida que pode ser verificada."}
::option[Uma referência criada a partir dos arquivos atuais cujas mudanças ainda não foram explicadas.]{#file-integrity-baselines-reference-source-b explanation="Ela incorporaria as diferenças antes da revisão."}
::option[As configurações de um host sem relação com a análise e sem contexto para comparação.]{#file-integrity-baselines-reference-source-c explanation="Hosts com funções diferentes podem exigir outros arquivos e permissões."}
:::

## Revisando as diferenças antes de atualizar

Compare cada diferença com uma mudança aprovada e verifique o resultado no serviço. Se a alteração de permissões do banner foi planejada, mas a mudança de configuração não foi, revise cada caso. Atualize a referência depois de entender e aprovar as diferenças autorizadas. Guarde um registro da referência anterior.

:::single-choice{#file-integrity-baselines-update-timing} A alteração de permissões do banner foi aprovada e a mudança em site.conf continua sem explicação. O que deve acontecer antes de aceitar uma nova referência?

::option[Aprovar tudo porque uma das linhas era esperada.]{#file-integrity-baselines-update-timing-a explanation="As diferenças nos arquivos dizem respeito a mudanças distintas."}
::option[Descartar o relatório de diferenças.]{#file-integrity-baselines-update-timing-b explanation="Ele registra o que ainda precisa ser revisado."}
::option[Investigar a alteração sem explicação em site.conf.]{#file-integrity-baselines-update-timing-c .correct explanation="A adoção de uma nova referência deve ocorrer depois da revisão do estado atual."}
:::

Para criar e comparar uma referência de integridade em um ambiente de prática, faça [Monitoramento de integridade de arquivos](https://labex.io/tutorials/linux-file-integrity-monitoring-fim-656122).

## Resumo

Agora você consegue usar uma referência como evidência em uma comparação específica.

1. Distinga conteúdo, permissões e presença no relatório.
2. Confirme que a referência representa um estado confiável.
3. Revise diferenças inesperadas antes de aceitar uma nova referência.
