---
lesson_id: "modifying-permissions"
course_id: "permissions"
lang: "pt"
order_index: 2
title: "Modificação de Permissões"
description: "Aprenda a alterar os bits de permissão do Linux com modos simbólicos e octais de `chmod`."
meta_title: "Modificação de Permissões - Permissões"
meta_description: "Aprenda a alterar permissões no Linux usando o comando chmod. Este guia aborda os métodos simbólico e numérico para ajudar você a gerenciar com segurança o acesso a arquivos e diretórios."
meta_keywords: "alterar permissão Linux, como alterar permissões no Linux, como alterar permissões de arquivos Linux, chmod, permissões de arquivos, segurança Linux, permissões simbólicas, permissões numéricas"
---

O comando `chmod` altera os bits de modo de arquivos e diretórios. Normalmente, apenas o proprietário do arquivo ou um processo com os privilégios necessários pode realizar essa alteração. Inspecione o modo atual com `ls -l` antes e depois de executar `chmod`.

## Uso do Modo Simbólico

Um modo simbólico indica qual classe de permissão será alterada, como alterá-la e quais permissões estão envolvidas.

- `u` seleciona a classe do proprietário.
- `g` seleciona a classe do grupo.
- `o` seleciona a classe dos outros.
- `a` seleciona as três classes.
- `+` adiciona permissões, `-` as remove e `=` define exatamente a classe selecionada.

Por exemplo, adicione a permissão de execução para o proprietário:

```bash
$ chmod u+x myfile
```

Remova a permissão de escrita do grupo:

```bash
$ chmod g-w myfile
```

Adicione a permissão de escrita para o proprietário e para o grupo:

```bash
$ chmod ug+w myfile
```

Várias cláusulas podem ser separadas por vírgulas. Este comando define leitura e escrita para o proprietário, somente leitura para o grupo e nenhuma permissão para os outros:

```bash
$ chmod u=rw,g=r,o= myfile
```

Se a classe for omitida, como em `chmod +x myfile`, o umask do processo afeta quais classes são alteradas. Indicar a classe explicitamente facilita a revisão do resultado pretendido.

:::single-choice{#modifying-permissions-remove-group-write}
Qual modo simbólico remove a permissão de escrita do grupo sem alterar os outros bits desse grupo?

::option[`chmod u-w myfile`]{#modifying-permissions-user-minus-write explanation="Esse comando remove a permissão de escrita da classe do proprietário, não da classe do grupo."}
::option[`chmod g-w myfile`]{#modifying-permissions-group-minus-write .correct explanation="`g` seleciona a classe do grupo, `-` remove um bit e `w` identifica a permissão de escrita."}
::option[`chmod g=w myfile`]{#modifying-permissions-group-equals-write explanation="O operador `=` substitui a classe selecionada por uma permissão somente de escrita, em vez de remover a escrita."}
:::

## Uso do Modo Octal

Um modo octal define cada trio básico de permissões com um dígito. Some estes valores dentro de cada classe:

- `4` para leitura
- `2` para escrita
- `1` para execução
- `0` para nenhuma permissão

Os três dígitos mais à direita representam o proprietário, o grupo e os outros, nessa ordem. Por exemplo:

```bash
$ chmod 755 myfile
```

O modo `755` se expande da seguinte forma:

- O `7` do proprietário é `4 + 2 + 1`, ou `rwx`.
- O `5` do grupo é `4 + 1`, ou `r-x`.
- O `5` dos outros é `4 + 1`, ou `r-x`.

Ao contrário das operações simbólicas com `+` ou `-`, um modo octal fornece o conjunto completo de permissões comuns. Uma lição posterior aborda o dígito inicial opcional usado para os bits de modo especiais.

:::single-choice{#modifying-permissions-octal-read-value}
Qual valor octal representa a permissão de leitura?

::option[`1`]{#modifying-permissions-value-one explanation="O valor `1` representa a permissão de execução."}
::option[`2`]{#modifying-permissions-value-two explanation="O valor `2` representa a permissão de escrita."}
::option[`4`]{#modifying-permissions-value-four .correct explanation="A permissão de leitura contribui com o valor octal `4` para o dígito de uma classe."}
:::

:::single-choice{#modifying-permissions-mode-640}
Quais permissões comuns `chmod 640 report` define?

::option[Leitura para o proprietário, escrita para o grupo e execução para os outros.]{#modifying-permissions-640-separated explanation="Os dígitos octais são somas para cada classe, não colunas separadas de leitura, escrita e execução."}
::option[Leitura/execução para o proprietário, escrita para o grupo e nenhuma para os outros.]{#modifying-permissions-640-wrong-sums explanation="O valor `6` do proprietário é leitura mais escrita, enquanto o valor `4` do grupo é leitura."}
::option[Leitura/escrita para o proprietário, leitura para o grupo e nenhuma para os outros.]{#modifying-permissions-640-correct .correct explanation="Os dígitos se expandem para proprietário `6` (`rw-`), grupo `4` (`r--`) e outros `0` (`---`)."}
:::

## Aplicação Segura das Alterações

Conceda somente o acesso necessário aos usuários e serviços. Evite usar `chmod 777` como atalho de solução de problemas, pois ele concede leitura, escrita e execução a todas as classes, frequentemente criando mais riscos sem resolver questões de propriedade, travessia de diretórios, ACLs ou políticas de serviços.

Alterações recursivas exigem cuidados adicionais. Examine previamente a árvore de destino, considere links simbólicos e sistemas de arquivos montados e teste em um escopo pequeno antes de usar `chmod -R`. Após uma alteração, verifique o modo resultante em vez de presumir que o comando afetou os objetos pretendidos.

:::single-choice{#modifying-permissions-least-privilege}
Por que `chmod 777` costuma ser uma solução geral inadequada para um problema de acesso?

::option[Ele remove todas as permissões do proprietário.]{#modifying-permissions-777-removes explanation="Cada `7` concede leitura, escrita e execução; ele não remove as permissões do proprietário."}
::option[Ele concede todas as permissões básicas ao proprietário, ao grupo e aos outros.]{#modifying-permissions-777-grants-all .correct explanation="As três classes recebem `rwx`, o que normalmente excede o acesso realmente necessário."}
::option[Ele altera somente a propriedade de grupo do arquivo.]{#modifying-permissions-777-group explanation="`chmod` altera os bits de modo; a propriedade de grupo é alterada com uma ferramenta como `chgrp` ou `chown`."}
:::

Para praticar em um ambiente isolado, use o laboratório [Usuários, Grupos e Permissões de Arquivos no Linux](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002) e inspecione cada modo antes e depois de alterá-lo.

## Resumo

Agora você sabe alterar os bits de modo comuns do Linux com expressões `chmod` deliberadas.

1. Use o modo simbólico para adições, remoções ou atribuições específicas.
2. Construa dígitos octais com leitura `4`, escrita `2` e execução `1`.
3. Interprete as classes octais na ordem proprietário, grupo e outros.
4. Verifique as alterações e aplique apenas o privilégio mínimo necessário.
