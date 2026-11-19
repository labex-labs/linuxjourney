---
lesson_id: "git-pull-requests"
course_id: "git"
lang: "pt"
order_index: 7
title: "Pull requests"
description: "Aprenda a ler uma pull request e a identificar o que uma revisão ou verificação automatizada cobre."
meta_title: "Pull requests - Git"
meta_description: "Aprenda a ler uma pull request e a identificar o que uma revisão ou verificação automatizada cobre."
meta_keywords: "pull requests, revisão de código, git, devops, Linux Journey"
---

Uma **pull request**, também chamada de PR, propõe levar alterações de uma branch para outra. O Git acompanha os commits e as branches. O serviço de hospedagem oferece uma página onde você pode revisar e discutir as alterações e conferir os resultados das verificações.

## Como identificar a origem e o destino

Imagine que alguém da equipe proponha uma página de status para o site. A página de revisão mostra `health-page → main`. A branch de origem, às vezes chamada de **head**, contém o trabalho proposto. A branch de destino, às vezes chamada de **base**, é a que receberia as alterações.

```text
Source: health-page at 3ab4501
Target: main
Changed file: health.txt
```

Neste ponto, a página de revisão mostra uma proposta. A branch de destino recebe as alterações quando a PR é mesclada.

:::single-choice{#git-pull-requests-pr-direction} Que branch recebe a página de status quando esta PR é mesclada?

::option[Uma branch com o mesmo nome do identificador do commit.]{#git-pull-requests-pr-direction-a explanation="O identificador aponta para um estado salvo. A branch de destino tem seu próprio nome."}
::option[Main.]{#git-pull-requests-pr-direction-b .correct explanation="O destino é main, então a alteração revisada entra nessa branch."}
::option[Health-page.]{#git-pull-requests-pr-direction-c explanation="Health-page é a branch de origem, que fornece a alteração."}
:::

## Como conferir as diferenças

Abra a lista de arquivos alterados e leia as diferenças em relação à branch de destino da PR. Acrescentar uma linha em `health.txt` faz sentido para uma página de status simples. Se você também vir uma alteração em `index.html`, avalie se ela cabe na mesma proposta. Examine os arquivos que a PR realmente lista.

:::single-choice{#git-pull-requests-unexpected-file} Uma PR com o título “Add a health page” também edita a página inicial. Onde você confere o que foi editado?

::option[Na comparação dos arquivos alterados.]{#git-pull-requests-unexpected-file-a .correct explanation="A comparação mostra quais linhas a proposta altera."}
::option[Só no título da PR.]{#git-pull-requests-unexpected-file-b explanation="O título resume a intenção e pode deixar detalhes de fora."}
::option[No nome da branch.]{#git-pull-requests-unexpected-file-c explanation="O nome da branch identifica uma linha de trabalho e não detalha cada mudança."}
:::

## Como ler os resultados das verificações automáticas

Um serviço de hospedagem pode executar um teste quando uma PR muda. Veja a qual commit ou revisão o resultado se refere. Se alguém enviar outro commit depois que o teste passou, confirme que a nova revisão passou pelas verificações exigidas. Um resultado positivo mostra o que aconteceu com as verificações que foram realmente executadas.

:::single-choice{#git-pull-requests-changed-revision} Um teste passou para 3ab4501. Agora a PR aponta para 78ac900. O que você deve verificar antes de confiar no resultado?

::option[Se a mensagem do primeiro commit estava bem escrita.]{#git-pull-requests-changed-revision-a explanation="A mensagem não mostra se os testes cobriram o commit mais recente."}
::option[Se a PR ainda tem o mesmo título.]{#git-pull-requests-changed-revision-b explanation="O título pode continuar o mesmo quando o código muda."}
::option[Se as verificações rodaram para a revisão nova.]{#git-pull-requests-changed-revision-c .correct explanation="O resultado anterior cobria outra revisão."}
:::

## Resumo

Agora você consegue ler o que uma pull request propõe e avaliar as informações que apoiam sua mesclagem.

1. Identifique as branches de origem e de destino.
2. Confira as alterações propostas na lista de arquivos modificados.
3. Descubra a qual revisão o resultado automatizado corresponde.
