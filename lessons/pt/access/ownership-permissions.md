---
title: "Permissões de Propriedade"
description: "Aprenda como alterar a propriedade de arquivos no Linux usando os comandos chown e chgrp. Entenda as permissões de usuário e grupo com este tutorial de Linux para iniciantes."
keywords: "chown, chgrp, propriedade de arquivo Linux, permissões Linux, comandos Linux, Linux para iniciantes, tutorial Linux, guia Linux"
---

## Lesson Content

Além de modificar as permissões em arquivos, você também pode modificar a propriedade de grupo e usuário do arquivo.

### Modificar a propriedade do usuário

```bash
sudo chown patty myfile
```

Este comando definirá o proprietário de `myfile` para `patty`.

### Modificar a propriedade do grupo

```bash
sudo chgrp whales myfile
```

Este comando definirá o grupo de `myfile` para `whales`.

### Modificar a propriedade de usuário e grupo ao mesmo tempo

Se você adicionar dois pontos e o nome do grupo após o usuário, poderá definir tanto o usuário quanto o grupo ao mesmo tempo.

```bash
sudo chown patty:whales myfile
```

## Exercise

Modifique o grupo e o usuário de alguns arquivos de teste. Depois, verifique as permissões com `ls -l`.

## Quiz Question

Qual comando você usa para alterar a propriedade do usuário?

## Quiz Answer

chown
