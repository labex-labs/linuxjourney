---
lang: "pt"
title: "Setgid"
meta_title: "Setgid - Permissões"
meta_description: "Aprenda sobre as permissões SGID (Set Group ID) do Linux, como elas funcionam e como modificá-las. Entenda este conceito crucial de segurança do Linux."
meta_keywords: "Linux SGID, Set Group ID, permissões Linux, chmod g+s, segurança Linux, Linux para iniciantes, tutorial Linux"
---

## Lesson Content

Semelhante ao bit de permissão set user ID, existe um bit de permissão set group ID (SGID). Este bit permite que um programa seja executado como se fosse um membro desse grupo.

Vamos ver um exemplo:

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

Agora podemos ver que o bit de permissão está no conjunto de permissões do grupo.

### Modifying SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

A representação numérica para SGID é 2.

## Exercise

No exercises for this lesson.

## Quiz Question

Qual número representa o SGID?

## Quiz Answer

2
