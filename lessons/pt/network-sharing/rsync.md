---
lesson_id: "rsync"
course_id: "network-sharing"
lang: "pt"
order_index: 2
title: "rsync"
description: "Aprenda a prever, executar e verificar com segurança sincronizações locais ou por SSH usando rsync."
meta_title: "rsync - Compartilhamento de Rede"
meta_description: "Descubra como usar o poderoso comando rsync no Linux para sincronização eficiente de arquivos, transferência remota de dados e backups confiáveis. Este guia abrange os principais comandos e opções do rsync."
meta_keywords: "rsync, rsync linux, sincronização de arquivos, backup de dados, sincronização remota, comando rsync, transferência de arquivos linux, tutorial rsync"
---

`rsync` reconcilia arquivos e árvores evitando transferir dados inalterados. Essa eficiência não torna toda invocação segura: sintaxe da origem, barras finais, metadados, exclusões e política de remoção determinam o resultado.

## Leitura da origem e do destino

Sincronize o conteúdo de `source/` em `destination/`:

```bash
$ rsync -a -- source/ destination/
```

A barra em `source/` significa “copie o conteúdo deste diretório”. Sem ela, `rsync -a source destination/` cria ou atualiza `destination/source`. Sempre preveja os caminhos ao mudar a barra.

:::single-choice{#rsync-source-trailing-slash} O que significa a barra final em `rsync -a source/ destination/`?

::option[Excluir a origem após uma transferência bem-sucedida.]{#rsync-delete-source explanation="Remover a origem exige outra opção e política explícita."}
::option[Copiar o conteúdo de `source` para o destino.]{#rsync-copy-contents .correct explanation="Remover a barra muda o layout de nível superior no destino."}
::option[Interpretar o destino como compartilhamento Windows.]{#rsync-windows-share explanation="A barra controla o conteúdo do diretório, não o transporte."}
:::

## Entendendo o modo archive

O modo archive, `-a`, equivale a um conjunto de opções recursivas e de preservação de metadados normalmente resumido como `-rlptgoD`. Ele preserva links simbólicos, permissões, horários de modificação, grupos, proprietários e arquivos de dispositivos ou especiais quando as permissões e o suporte da plataforma permitem.

O modo archive não inclui a preservação de hard links, ACLs nem atributos estendidos; eles normalmente exigem `-H`, `-A` e `-X`. Ele também não cria versões históricas por si só.

:::single-choice{#rsync-archive-limit} Qual metadado não está incluído em `-a` sozinho?

::option[Relações de hard links.]{#rsync-hard-links .correct explanation="Preservar hard links exige a opção `-H`."}
::option[Recursão de diretórios.]{#rsync-archive-recursion explanation="Archive inclui percurso recursivo."}
::option[Horários de modificação.]{#rsync-archive-times explanation="Archive inclui preservação dos horários."}
:::

## Previsão da transferência

Faça um dry run com mudanças detalhadas antes de uma sincronização importante:

```bash
$ rsync -a --dry-run --itemize-changes -- source/ destination/
```

Uma execução de teste prevê ações usando a varredura atual; ela não pode garantir que os arquivos não mudarão antes do comando real. Salve e revise o comando exato e só o execute sem `--dry-run` depois de confirmar os dois pontos de extremidade.

:::single-choice{#rsync-dry-run-purpose} O que `--dry-run --itemize-changes` oferece?

::option[Um snapshot permanente em outro dispositivo.]{#rsync-dry-backup explanation="O dry run não copia dados nem cria retenção independente."}
::option[Garantia de que a origem não mudará depois.]{#rsync-dry-lock explanation="A previsão não bloqueia a árvore."}
::option[Uma previsão das mudanças planejadas no momento.]{#rsync-dry-preview .correct explanation="A saída detalhada expõe decisões de caminho e metadados antes da alteração."}
:::

## Sincronização por SSH

Envie ou receba usando o operando remoto:

```bash
$ rsync -a -- source/ alice@example.net:/srv/data/
$ rsync -a -- alice@example.net:/srv/data/ destination/
```

Rsync moderno costuma usar SSH nessa forma, mas confirme shell remoto, chave do host, privilégios e disponibilidade do rsync remoto. `-z` pode ajudar dados compressíveis em link limitado, mas desperdiçar CPU em dados já comprimidos.

:::single-choice{#rsync-pull-direction} Qual ordem puxa dados remotos para um diretório local?

::option[`rsync -a local/ host:/data/`]{#rsync-local-first explanation="Essa ordem envia conteúdo local ao destino remoto."}
::option[`rsync --delete host local`]{#rsync-missing-path explanation="Isso não expressa o caminho remoto mostrado e acrescenta opção destrutiva."}
::option[`rsync -a host:/data/ local/`]{#rsync-remote-first .correct explanation="A árvore remota é a origem e a local é o destino."}
:::

## Tratando a exclusão como destrutiva

`--delete` remove do destino entradas ausentes na origem dentro do escopo. Pontas invertidas, barra errada ou exclusão ruim podem apagar dados válidos. Faça dry run num destino de teste, garanta backups recuperáveis, revise montagens e considere limites de exclusão.

Depois da execução real, examine o status de saída e os logs, compare as quantidades de arquivos e os metadados esperados e teste um conteúdo ou uma restauração representativa. A sincronização com rsync, por si só, replica exclusões ou corrupções indesejadas e não constitui uma estratégia completa de backup.

:::single-choice{#rsync-delete-effect} O que `--delete` pode fazer durante a sincronização?

::option[Criptografar todo arquivo com a chave do host SSH.]{#rsync-delete-encrypt explanation="Política de exclusão não é criptografia."}
::option[Impedir todas as mudanças no destino.]{#rsync-delete-readonly explanation="Ela autoriza mudanças adicionais no destino."}
::option[Remover do destino entradas ausentes no escopo de origem selecionado.]{#rsync-delete-destination .correct explanation="A opção faz a composição do destino espelhar a origem e exige uma visualização prévia revisada e um plano de recuperação."}
:::

## Resumo

Agora você consegue prever e verificar `rsync` sem ocultar casos destrutivos.

1. Usar barras finais para expressar o layout.
2. Adicionar opções de metadados não cobertas por archive.
3. Revisar dry run detalhado antes da sincronização real.
4. Verificar identidade SSH e direção das pontas.
5. Tratar exclusão e retenção como políticas explícitas.
