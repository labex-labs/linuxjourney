---
lang: "pt"
title: "Inodes"
meta_title: "Inodes - O Filesystem"
meta_description: "Aprenda sobre os inodes do Linux, sua estrutura e como eles gerenciam arquivos. Entenda os números de inode e use `df -i` e `ls -li` para verificar o uso de inodes. Comece sua jornada no Linux!"
meta_keywords: "inodes Linux, tutorial de inode, df -i, ls -li, sistema de arquivos Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Lembra-se de como nosso filesystem é composto por todos os nossos arquivos reais e um banco de dados que gerencia esses arquivos? O banco de dados é conhecido como a tabela de inodes.

### O que é um inode?

Um inode (index node) é uma entrada nesta tabela, e existe um para cada arquivo. Ele descreve tudo sobre o arquivo, como:

- File type - arquivo regular, diretório, dispositivo de caractere, etc.
- Owner
- Group
- Access permissions
- Timestamps - mtime (hora da última modificação do arquivo), ctime (hora da última alteração de atributo), atime (hora do último acesso)
- Number of hardlinks para o arquivo
- Size do arquivo
- Number of blocks alocados para o arquivo
- Pointers para os blocos de dados do arquivo - o mais importante!

Basicamente, os inodes armazenam tudo sobre o arquivo, exceto o filename e o próprio arquivo!

### Quando os inodes são criados?

Quando um filesystem é criado, espaço para inodes também é alocado. Algoritmos determinam quanto espaço de inode você precisa, dependendo do volume do disco e mais. Você provavelmente já viu erros de falta de espaço em disco em algum momento da sua vida. O mesmo pode ocorrer com os inodes (embora menos comum); você pode ficar sem inodes e, portanto, ser incapaz de criar mais arquivos. Lembre-se, o armazenamento de dados depende tanto dos dados quanto do banco de dados (inodes).

Para ver quantos inodes restam no seu sistema, use o comando `df -i`.

### Informações do Inode

Os inodes são identificados por números. Quando um arquivo é criado, ele recebe um número de inode, e o número é atribuído em ordem sequencial. No entanto, você pode notar às vezes que, ao criar um novo arquivo, ele recebe um número de inode menor que outros. Isso ocorre porque, uma vez que os inodes são excluídos, eles podem ser reutilizados por outros arquivos. Para visualizar os números de inode, execute `ls -li`:

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

Sabemos que nossos dados estão em algum lugar no disco. Infelizmente, provavelmente não foram armazenados sequencialmente, então temos que usar inodes. Os inodes apontam para os blocos de dados reais dos seus arquivos. Em um filesystem típico (nem todos funcionam da mesma forma), cada inode contém 15 pointers. Os primeiros 12 pointers apontam diretamente para os blocos de dados. O 13º pointer aponta para um bloco contendo pointers para mais blocos, o 14º pointer aponta para outro bloco aninhado de pointers, e o 15º pointer aponta novamente para outro bloco de pointers! Confuso, eu sei! A razão pela qual isso é feito dessa forma é para manter a estrutura do inode a mesma para cada inode, mas ser capaz de referenciar arquivos de diferentes tamanhos. Se você tivesse um arquivo pequeno, poderia encontrá-lo mais rapidamente com os primeiros 12 pointers diretos; arquivos maiores podem ser encontrados com os ninhos de pointers. De qualquer forma, a estrutura do inode é a mesma.

## Exercise

Observe alguns números de inode para diferentes arquivos. Quais são geralmente criados primeiro?

## Quiz Question

Como você vê quantos inodes restam no seu sistema?

## Quiz Answer

df -i
