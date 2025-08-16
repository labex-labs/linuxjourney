---
lang: "pt"
title: "O Sticky Bit"
description: "Aprenda sobre o sticky bit do Linux, seu propósito em diretórios compartilhados como /tmp, e como configurá-lo usando chmod. Entenda esta permissão de arquivo chave!"
keywords: "Linux sticky bit, chmod +t, diretório /tmp, permissões Linux, segurança de arquivos, tutorial Linux, Linux para iniciantes"
---

## Lesson Content

Um último bit de permissão especial sobre o qual quero falar é o sticky bit.

Este bit de permissão "fixa um arquivo/diretório", o que significa que apenas o proprietário ou o usuário root pode excluir ou modificar o arquivo. Isso é muito útil para diretórios compartilhados. Veja o exemplo abaixo:

```bash
$ ls -ld /tmp
drwxrwxrwx+t 6 root root 4096 Dec 15 11:45 /tmp
```

Você verá um bit de permissão especial no final aqui **t**. Isso significa que todos podem adicionar arquivos, escrever arquivos e modificar arquivos no diretório `/tmp`, mas apenas root pode excluir o diretório `/tmp`.

### Modify sticky bit

```bash
sudo chmod +t mydir

sudo chmod 1755 mydir
```

A representação numérica para o sticky bit é **1**.

## Exercise

Que outros arquivos e diretórios você acha que têm um sticky bit ativado?

## Quiz Question

Qual símbolo representa o sticky bit?

## Quiz Answer

t
