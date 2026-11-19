---
lesson_id: "incident-evidence-preservation"
course_id: "incident-response"
lang: "pt"
order_index: 2
title: "Preservação de evidências"
description: "Aprenda a preservar um registro de prática, sua cópia e a soma de verificação para análise posterior."
meta_title: "Preservação de evidências - Resposta a incidentes"
meta_description: "Aprenda a preservar um registro de prática, sua cópia e a soma de verificação para análise posterior."
meta_keywords: "preservação de evidências, soma de verificação, resposta a incidentes, cibersegurança, Linux Journey"
---

Durante a resposta a um incidente, um trecho de log pode ajudar a explicar o que aconteceu. Preserve a fonte original ou a exportação aprovada junto com os detalhes que outra pessoa precisa para analisá-la.

## Registrando o contexto

Anote o host, a fonte, o fuso horário e a janela de tempo. Registre quem coletou os dados e qual filtro foi usado. Sem esse contexto, uma linha copiada pode ter o mesmo texto que uma linha de outra máquina.

:::single-choice{#incident-evidence-preservation-context-fields} Uma pessoa recebe uma linha que só indica o horário 09:22, sem outro contexto. O que você deve acrescentar?

::option[O caminho onde a cópia foi salva localmente.]{#incident-evidence-preservation-context-fields-b explanation="Esse caminho ajuda a encontrar a cópia, mas ainda faltam a origem e o contexto do horário."}
::option[Uma suposição sobre a causa.]{#incident-evidence-preservation-context-fields-c explanation="Registre os detalhes da coleta separadamente da interpretação."}
::option[O host de origem, o fuso horário e a janela de coleta.]{#incident-evidence-preservation-context-fields-a .correct explanation="Esses dados permitem situar a linha na linha do tempo correta."}
:::

## Comparando uma cópia

Em uma pasta nova de prática, salve a linha de exemplo inofensiva, copie-a e calcule o SHA-256 dos dois arquivos. Use somente o arquivo de exemplo. As gravações substituem arquivos de mesmo nome nessa pasta.

```bash
$ printf '%s\n' '09:22 UTC public homepage returned 503' > sample.log
$ cp sample.log review-copy.log
$ sha256sum sample.log review-copy.log
```

A primeira coluna contém o hash do conteúdo. Os dois valores devem bater. Isso verifica, naquele momento, se os bytes da cópia correspondem aos do original. A precisão do registro do evento original precisa ser verificada por outros meios.

:::single-choice{#incident-evidence-preservation-copy-meaning} O que a correspondência entre os hashes permite afirmar?

::option[O horário da fonte certamente está correto.]{#incident-evidence-preservation-copy-meaning-a explanation="O hash mede o conteúdo do arquivo e não valida o relógio."}
::option[A cópia para análise tem os mesmos bytes medidos no exemplo.]{#incident-evidence-preservation-copy-meaning-b .correct explanation="Os dois hashes foram calculados com o mesmo algoritmo."}
::option[A cópia foi aprovada para compartilhamento público.]{#incident-evidence-preservation-copy-meaning-c explanation="A aprovação diz respeito a quem pode ver o arquivo. O hash verifica seu conteúdo."}
:::

![Saída da soma de verificação na LabEx com hashes iguais para o arquivo de prática e sua cópia para análise](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-evidence-preservation/matching-copy-hashes.png)

## Preparando uma cópia segura para análise

Mantenha o registro original intacto e restrinja o acesso a ele. Se outra equipe precisar de poucos campos, prepare um trecho separado e remova dele as informações confidenciais. Registre que o trecho foi reduzido e mantenha a referência à fonte protegida.

:::single-choice{#incident-evidence-preservation-redact-copy} De qual arquivo você deve remover os dados sensíveis antes de compartilhar?

::option[De um trecho separado para análise.]{#incident-evidence-preservation-redact-copy-c .correct explanation="Assim, você preserva a fonte e limita o material compartilhado."}
::option[Do original protegido, para que todas as cópias mudem.]{#incident-evidence-preservation-redact-copy-a explanation="Isso alteraria a evidência que você quer preservar."}
::option[Do texto da soma de verificação, para que um arquivo alterado pareça igual.]{#incident-evidence-preservation-redact-copy-b explanation="Preserve os valores medidos e os arquivos que eles descrevem."}
:::

## Resumo

Agora você consegue preparar evidências que outra pessoa pode interpretar.

1. Registre onde e quando o material foi coletado.
2. Verifique se os bytes da cópia correspondem aos da fonte.
3. Remova os dados sensíveis de um trecho separado antes de compartilhá-lo.
