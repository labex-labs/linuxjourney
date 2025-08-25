---
index: 8
lang: "pt"
title: "O Sticky Bit"
meta_title: "O Sticky Bit - Permissões"
meta_description: "Aprenda sobre o sticky bit do Linux, seu propósito em diretórios compartilhados como /tmp e como configurá-lo usando chmod. Entenda esta permissão de arquivo chave!"
meta_keywords: "Linux sticky bit, chmod +t, diretório /tmp, permissões Linux, segurança de arquivo, tutorial Linux, Linux para iniciantes"
---

## Lesson Content

Um último bit de permissão especial sobre o qual quero falar é o sticky bit.

Este bit de permissão "fixa um arquivo/diretório", o que significa que apenas o proprietário ou o usuário root pode excluir ou modificar o arquivo. Isso é muito útil para diretórios compartilhados. Veja o exemplo abaixo:

```bash
$ ls -ld /tmp
drwxrwxrwx+t 6 root root 4096 Dec 15 11:45 /tmp
```

Você verá um bit de permissão especial no final aqui **t**. Isso significa que todos podem adicionar arquivos, gravar arquivos e modificar arquivos no diretório `/tmp`, mas apenas o root pode excluir o diretório `/tmp`.

### Modificar o sticky bit

```bash
sudo chmod +t mydir

sudo chmod 1755 mydir
```

A representação numérica para o sticky bit é **1**.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão das permissões de arquivo do Linux e seu impacto no gerenciamento de arquivos e diretórios:

1. **[Grupo de Usuários Linux e Permissões de Arquivo](https://labex.io/pt/labs/linux-linux-user-group-and-file-permissions-18002)** - Pratique a criação e o gerenciamento de usuários e grupos, compreendendo as permissões de arquivo e manipulando a propriedade do arquivo. Este laboratório fornece o conhecimento fundamental para entender como funcionam as permissões especiais, como o sticky bit.
2. **[Excluir e Mover Arquivos](https://labex.io/pt/labs/linux-delete-and-move-files-7777)** - Aprenda como excluir e mover arquivos em sistemas Linux. Este laboratório o ajudará a entender as implicações práticas das permissões, incluindo como elas podem restringir essas ações.
3. **[Encontrar um Arquivo](https://labex.io/pt/labs/linux-find-a-file-17993)** - Pratique a localização de arquivos e a definição de autoridade de acesso. Este laboratório reforça a importância das permissões de arquivo e como elas controlam o acesso e a modificação.

Esses laboratórios o ajudarão a aplicar os conceitos de permissões de arquivo em cenários reais e a construir confiança no gerenciamento de acesso a arquivos no Linux.

## Quiz Question

Qual símbolo representa o sticky bit?

## Quiz Answer

t
