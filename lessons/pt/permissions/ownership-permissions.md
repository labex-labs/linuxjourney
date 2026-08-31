---
lesson_id: "ownership-permissions"
course_id: "permissions"
lang: "pt"
order_index: 3
title: "Permissões de Propriedade"
description: "Aprenda a inspecionar e alterar a propriedade de usuário e grupo dos objetos do sistema de arquivos Linux."
meta_title: "Permissões de Propriedade - Permissões"
meta_description: "Domine a propriedade de arquivos Linux aprendendo a usar os comandos chown e chgrp. Este tutorial explica como alterar a propriedade de usuário e grupo dos arquivos, uma habilidade essencial para gerenciar permissões Linux."
meta_keywords: "chown, chgrp, propriedade de arquivos Linux, alterar proprietário de arquivo, alterar grupo de arquivo, permissões Linux, comandos Linux, tutorial Linux, propriedade de usuário, propriedade de grupo"
---

Todo objeto do sistema de arquivos Linux registra um usuário proprietário e um grupo proprietário. Essas identidades determinam qual trio de permissões do proprietário ou do grupo se aplica, mas não concedem por si só uma permissão específica. Inspecione tanto a propriedade quanto o modo com `ls -l`.

## Alteração do Usuário Proprietário

Use `chown`, abreviação de change owner, para atribuir outro usuário proprietário:

```bash
$ sudo chown patty myfile
```

Esse comando altera o usuário proprietário de `myfile` para `patty` e mantém seu grupo inalterado. Alterar o usuário proprietário de um arquivo normalmente exige privilégios adequados, mesmo que você seja seu proprietário atual. Essa restrição impede que usuários transfiram arquivos para evitar cotas ou outros controles baseados em propriedade.

:::single-choice{#ownership-permissions-change-user}
Qual comando altera o usuário proprietário de `myfile` para `patty`, mantendo seu grupo inalterado?

::option[`chown patty myfile`]{#ownership-permissions-user-with-chown .correct explanation="Somente um nome de usuário como operando de propriedade de `chown` altera o usuário proprietário e preserva o grupo."}
::option[`chgrp patty myfile`]{#ownership-permissions-user-with-chgrp explanation="`chgrp` altera o grupo proprietário, não o usuário proprietário."}
::option[`chmod patty myfile`]{#ownership-permissions-user-with-chmod explanation="`chmod` altera bits de modo e não aceita um nome de usuário como novo proprietário."}
:::

## Alteração do Grupo Proprietário

Use `chgrp` para atribuir outro grupo proprietário:

```bash
$ chgrp whales myfile
```

Em sistemas comuns, um proprietário sem privilégios pode alterar o grupo de um arquivo somente para um grupo do qual esse usuário seja membro. Processos privilegiados podem realizar alterações mais amplas. A forma equivalente com `chown` começa com dois-pontos:

```bash
$ chown :whales myfile
```

Depois disso, os bits de modo do grupo se aplicam quando o kernel seleciona a classe do grupo; alterar o grupo não adiciona automaticamente bits de leitura, escrita ou execução.

:::single-choice{#ownership-permissions-change-group}
O que `chgrp whales myfile` altera?

::option[O usuário proprietário registrado para `myfile`.]{#ownership-permissions-group-not-user explanation="O usuário proprietário é alterado com `chown`, não com `chgrp`."}
::option[Os membros listados no grupo `whales`.]{#ownership-permissions-group-members explanation="O comando altera os metadados do arquivo; ele não edita o banco de dados de associações a grupos do sistema."}
::option[O grupo proprietário registrado para `myfile`.]{#ownership-permissions-group-owner .correct explanation="`chgrp` atribui o grupo indicado como proprietário de grupo do objeto do sistema de arquivos."}
:::

## Alteração Conjunta do Usuário e do Grupo

Forneça `USER:GROUP` a `chown` para atualizar os dois campos em uma única operação:

```bash
$ sudo chown patty:whales myfile
```

O comando atribui `patty` como usuário proprietário e `whales` como grupo proprietário. Verifique o resultado em vez de presumir que a operação foi bem-sucedida:

```bash
$ ls -l myfile
```

:::single-choice{#ownership-permissions-change-both}
Qual especificação de propriedade atribui o usuário `patty` e o grupo `whales` em um único comando `chown`?

::option[`patty:whales`]{#ownership-permissions-both-colon .correct explanation="Dois-pontos separam os nomes do usuário e do grupo na especificação conjunta de propriedade."}
::option[`patty/whales`]{#ownership-permissions-both-slash explanation="Uma barra não é o separador apresentado para um operando de usuário e grupo de `chown`."}
::option[`patty+whales`]{#ownership-permissions-both-plus explanation="Um sinal de adição não é usado para combinar os dois campos de propriedade em `chown`."}
:::

## Cuidados com Alterações Recursivas

A opção `-R` altera a propriedade recursivamente, mas um comando recursivo amplo pode atravessar árvores de diretórios inesperadas ou afetar dados de serviços. Confirme o destino exato, entenda o comportamento de sua implementação para links simbólicos, examine previamente a árvore e verifique uma pequena amostra antes de alterar uma hierarquia extensa. Não copie comandos privilegiados de propriedade de exemplos para sistemas reais sem revisar seu escopo.

:::single-choice{#ownership-permissions-mode-separate}
Depois de alterar o grupo proprietário de um arquivo, o que acontece com seus bits comuns de permissão do grupo?

::option[Eles sempre se tornam automaticamente leitura e escrita.]{#ownership-permissions-mode-read-write explanation="`chgrp` não seleciona automaticamente um modo fixo para o grupo."}
::option[Eles são copiados do trio de permissões do proprietário.]{#ownership-permissions-mode-copied explanation="Os trios do proprietário e do grupo permanecem independentes quando a propriedade é alterada."}
::option[Eles permanecem como estavam, a menos que outra operação os altere.]{#ownership-permissions-mode-unchanged .correct explanation="Os campos de propriedade e os bits de modo são metadados separados; alterar o grupo não concede por si só novos bits ao grupo."}
:::

Para praticar em um ambiente isolado, o laboratório [Usuários, Grupos e Permissões de Arquivos no Linux](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002) aborda a inspeção e a modificação da propriedade junto com os modos dos arquivos.

## Resumo

Agora você sabe diferenciar os metadados de propriedade dos bits de permissão e alterá-los deliberadamente.

1. Use `chown USER FILE` para alterar o usuário proprietário.
2. Use `chgrp GROUP FILE` ou `chown :GROUP FILE` para alterar o grupo proprietário.
3. Use `chown USER:GROUP FILE` para definir os dois campos.
4. Verifique os resultados e controle cuidadosamente o escopo das alterações recursivas.
