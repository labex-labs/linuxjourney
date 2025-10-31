---
index: 12
lang: "pt"
title: "symlinks"
meta_title: "symlinks - O Sistema de Arquivos"
meta_description: "Explore symlinks (links simbólicos) e hard links no Linux. Aprenda a criá-los com o comando ln, verificar a contagem de links com ls e entender a diferença nas saídas do ls para symlinks e hard links."
meta_keywords: "symlinks Linux, hard links, comando ln, links simbólicos, ls symlink, contagem de links no linux, ls symlinks, ls links, sistema de arquivos Linux, tutorial Linux"
---

## Lesson Content

Ao listar arquivos em detalhes, você verá muitas informações. Vamos analisar um exemplo anterior de informações de inode do comando `ls -li`:

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Anteriormente, ignoramos o terceiro campo nesta saída. Este campo é a contagem de links.

### A Contagem de Links no Linux

A **contagem de links no linux** é o número total de hard links que um arquivo possui. Para entender o que isso significa, primeiro precisamos discutir o que são links. No Linux, existem dois tipos de links: links simbólicos (symlinks) e hard links.

### Entendendo Symlinks

No sistema operacional Windows, você tem atalhos, que são essencialmente aliases que apontam para outros arquivos. No Linux, o equivalente é um link simbólico, também conhecido como link suave ou **symlink**. Um symlink é um tipo especial de arquivo que aponta para outro arquivo ou diretório pelo seu nome.

Vamos ver isso na prática. Criaremos alguns arquivos e, em seguida, um symlink.

```bash
pete@icebox:~/Desktop$ echo 'myfile' > myfile
pete@icebox:~/Desktop$ echo 'myfile2' > myfile2
pete@icebox:~/Desktop$ echo 'myfile3' > myfile3

pete@icebox:~/Desktop$ ln -s myfile myfilelink
pete@icebox:~/Desktop$ ls -li
total 12
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
```

Aqui, criamos um link simbólico chamado `myfilelink` que aponta para `myfile`. Quando você usa `ls` para ver um `ls symlink`, ele é claramente identificado pelo `l` no início da string de permissões e pelo símbolo `->` apontando para o alvo. Observe que o symlink tem seu próprio número de inode exclusivo (93403). Como os symlinks apontam para nomes de arquivos em vez de inodes, eles podem abranger diferentes sistemas de arquivos.

### Entendendo Hard Links

O outro tipo de link é o hard link. Um hard link cria outra entrada de arquivo que aponta diretamente para o mesmo inode do arquivo original.

Vamos criar um hard link para `myfile2`:

```bash
pete@icebox:~/Desktop$ ln myfile2 myhardlink
pete@icebox:~/Desktop$ ls -li
total 16
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myhardlink
```

Observe que `myhardlink` compartilha o mesmo número de inode (93401) que `myfile2`. A contagem de links para ambos os arquivos também aumentou para 2. Isso ocorre porque duas entradas de arquivo agora apontam para o mesmo inode. Se você modificar o conteúdo de `myfile2`, as alterações serão refletidas em `myhardlink`, e vice-versa. Se você excluir `myfile2`, os dados do arquivo ainda estarão acessíveis através de `myhardlink`. O inode e seus dados só são removidos do disco quando a contagem de links cai para zero. Como os hard links apontam para inodes, que são exclusivos dentro de um único sistema de arquivos, eles não podem abranger diferentes sistemas de arquivos.

### Criando Symlinks e Hard Links

Você pode criar ambos os tipos de links usando o comando `ln`. A sintaxe é simples.

Para criar um link simbólico, use a flag `-s`:

```bash
ln -s /caminho/para/original /caminho/para/link
```

Para criar um hard link, omita a flag `-s`:

```bash
ln /caminho/para/original /caminho/para/link
```

Usar os comandos `ls symlinks` ou `ls links` em geral com a opção `-l` é essencial para gerenciar e identificar esses diferentes tipos de arquivos.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de gerenciamento de arquivos, links e inodes:

1. **[Gerenciar Arquivos e Diretórios no Linux](https://labex.io/pt/labs/comptia-manage-files-and-directories-in-linux-590835)** - Pratique a criação, cópia, movimentação e remoção de arquivos e diretórios, e aprenda especificamente sobre links simbólicos e hard links, e como analisar inodes.
2. **[Navegar no Sistema de Arquivos no Linux](https://labex.io/pt/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Domine comandos essenciais como `pwd`, `cd` e `ls` para se mover eficientemente pelo sistema de arquivos Linux, uma habilidade fundamental para entender onde os arquivos e seus inodes residem.

Esses laboratórios ajudarão você a aplicar os conceitos de gerenciamento de arquivos e links em cenários reais e a construir confiança com o sistema de arquivos Linux.

## Quiz Question

Qual é o comando e sua opção principal usada para criar um symlink? Sua resposta deve estar em inglês e diferencia maiúsculas de minúsculas. Por favor, inclua o espaço entre o comando e a opção.

## Quiz Answer

ln -s
