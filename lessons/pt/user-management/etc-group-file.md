---
title: "/etc/group"
description: "Aprenda sobre o arquivo /etc/group no Linux, entendendo o gerenciamento de grupos, GID e permissões de usuário. Tutorial essencial do arquivo de grupo Linux para iniciantes."
keywords: "/etc/group, grupos Linux, gerenciamento de grupos, GID, permissões Linux, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Outro arquivo usado no gerenciamento de usuários é o arquivo `/etc/group`. Este arquivo permite diferentes grupos com diferentes permissões.

```bash
$ cat /etc/group

root:*:0:pete
```

Muito semelhante ao arquivo `/etc/passwd`, os campos do `/etc/group` são os seguintes:

1. Nome do grupo
2. Senha do grupo - não há necessidade de definir uma senha de grupo; usar um privilégio elevado como `sudo` é o padrão. Um asterisco (`*`) será colocado como valor padrão.
3. Group ID (GID)
4. Lista de usuários - você pode especificar manualmente os usuários que deseja em um grupo específico

## Exercise

Execute o comando `groups`. O que você vê?

## Quiz Question

Qual é o GID de root?

## Quiz Answer

0
