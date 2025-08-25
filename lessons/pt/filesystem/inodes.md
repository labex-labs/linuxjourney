---
index: 11
lang: "pt"
title: "Inodes"
meta_title: "Inodes - O Sistema de Arquivos"
meta_description: "Aprenda sobre os inodes do Linux, sua estrutura e como eles gerenciam arquivos. Entenda os números de inode e use `df -i` e `ls -li` para verificar o uso de inodes. Comece sua jornada no Linux!"
meta_keywords: "inodes Linux, tutorial de inode, df -i, ls -li, sistema de arquivos Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Lembra como nosso sistema de arquivos é composto por todos os nossos arquivos reais e um banco de dados que gerencia esses arquivos? O banco de dados é conhecido como tabela de inodes.

### O que é um inode?

Um inode (nó de índice) é uma entrada nesta tabela, e existe um para cada arquivo. Ele descreve tudo sobre o arquivo, como:

- Tipo de arquivo - arquivo regular, diretório, dispositivo de caractere, etc.
- Proprietário
- Grupo
- Permissões de acesso
- Timestamps - mtime (hora da última modificação do arquivo), ctime (hora da última alteração de atributo), atime (hora do último acesso)
- Número de hardlinks para o arquivo
- Tamanho do arquivo
- Número de blocos alocados para o arquivo
- Ponteiros para os blocos de dados do arquivo - o mais importante!

Basicamente, os inodes armazenam tudo sobre o arquivo, exceto o nome do arquivo e o próprio arquivo!

### Quando os inodes são criados?

Quando um sistema de arquivos é criado, o espaço para inodes também é alocado. Algoritmos determinam quanto espaço de inode você precisa, dependendo do volume do disco e muito mais. Você provavelmente já viu erros de falta de espaço em disco em algum momento da sua vida. O mesmo pode ocorrer com os inodes (embora menos comum); você pode ficar sem inodes e, portanto, não conseguir criar mais arquivos. Lembre-se, o armazenamento de dados depende tanto dos dados quanto do banco de dados (inodes).

Para ver quantos inodes restam no seu sistema, use o comando `df -i`.

### Informações do Inode

Os inodes são identificados por números. Quando um arquivo é criado, ele recebe um número de inode, e o número é atribuído em ordem sequencial. No entanto, você pode notar às vezes que, ao criar um novo arquivo, ele recebe um número de inode menor que outros. Isso ocorre porque, uma vez que os inodes são excluídos, eles podem ser reutilizados por outros arquivos. Para visualizar os números dos inodes, execute `ls -li`:

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

O primeiro campo neste comando lista o número do inode.

Você também pode ver informações detalhadas sobre um arquivo com `stat`; ele também fornece informações sobre o inode.

```bash
pete@icebox:~$ stat ~/Desktop/
  File: ‘/home/pete/Desktop/’
  Size: 6               Blocks: 0          IO Block: 4096   directory
Device: 806h/2054d      Inode: 140         Links: 2
Access: (0755/drwxr-xr-x)  Uid: ( 1000/   pete)   Gid: ( 1000/   pete)
Access: 2016-01-20 20:13:50.647435982 -0800
Modify: 2016-01-20 20:13:06.191675843 -0800
Change: 2016-01-20 20:13:06.191675843 -0800
 Birth: -
```

### Como os inodes localizam arquivos?

Sabemos que nossos dados estão em algum lugar no disco. Infelizmente, provavelmente não foram armazenados sequencialmente, então temos que usar inodes. Os inodes apontam para os blocos de dados reais de seus arquivos. Em um sistema de arquivos típico (nem todos funcionam da mesma forma), cada inode contém 15 ponteiros. Os primeiros 12 ponteiros apontam diretamente para os blocos de dados. O 13º ponteiro aponta para um bloco contendo ponteiros para mais blocos, o 14º ponteiro aponta para outro bloco aninhado de ponteiros, e o 15º ponteiro aponta novamente para outro bloco de ponteiros! Confuso, eu sei! A razão pela qual isso é feito dessa forma é para manter a estrutura do inode a mesma para cada inode, mas ser capaz de referenciar arquivos de tamanhos diferentes. Se você tivesse um arquivo pequeno, poderia encontrá-lo mais rapidamente com os primeiros 12 ponteiros diretos; arquivos maiores podem ser encontrados com os ninhos de ponteiros. De qualquer forma, a estrutura do inode é a mesma.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do sistema de arquivos Linux e gerenciamento de arquivos:

1. **[Gerenciar Arquivos e Diretórios no Linux](https://labex.io/pt/labs/comptia-manage-files-and-directories-in-linux-590835)** - Pratique a criação, remoção, cópia e movimentação de arquivos e diretórios, e explore a criação de links simbólicos e hard links enquanto analisa inodes.
2. **[Navegar no Sistema de Arquivos no Linux](https://labex.io/pt/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Aprenda as habilidades fundamentais para navegar no sistema de arquivos Linux usando comandos essenciais do shell como `pwd`, `cd` e `ls`.
3. **[Encontrar Arquivos e Comandos no Linux](https://labex.io/pt/labs/comptia-find-files-and-commands-in-linux-590834)** - Domine técnicas essenciais para localizar arquivos e comandos no Linux usando `find`, `locate`, `whereis`, `which` e `type`.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança no gerenciamento do sistema de arquivos Linux.

## Quiz Question

Como você vê quantos inodes restam no seu sistema?

## Quiz Answer

df -i
