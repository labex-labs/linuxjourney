---
lang: "pt"
title: "Symlinks"
meta_description: "Aprenda sobre symlinks e hard links no Linux, incluindo como criá-los e gerenciá-los. Entenda suas diferenças e casos de uso com este guia para iniciantes."
meta_keywords: "Linux symlinks, hard links, comando ln, links simbólicos, sistema de arquivos Linux, tutorial Linux, Linux para iniciantes"
---

## Lesson Content

Vamos usar um exemplo anterior de informações de inode:

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Você deve ter notado que temos ignorado o terceiro campo no comando `ls`; esse campo é a contagem de links. A contagem de links é o número total de hard links que um arquivo possui. Bem, isso não significa nada para você agora, então vamos discutir os links primeiro.

### Symlinks

No sistema operacional Windows, existem coisas conhecidas como atalhos. Atalhos são apenas apelidos para outros arquivos. Se você fizer algo com o arquivo original, poderá potencialmente quebrar o atalho. No Linux, o equivalente aos atalhos são os links simbólicos (ou soft links ou symlinks). Symlinks nos permitem linkar para outro arquivo pelo seu nome de arquivo. Outro tipo de link encontrado no Linux são os hard links; estes são, na verdade, outro arquivo com um link para um inode. Vamos ver o que quero dizer na prática, começando com os symlinks.

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

Você pode ver que eu criei um link simbólico chamado `myfilelink` que aponta para `myfile`. Links simbólicos são denotados por `->`. Observe, no entanto, como obtive um novo número de inode; symlinks são apenas arquivos que apontam para nomes de arquivos. Quando você modifica um symlink, o arquivo também é modificado. Números de inode são únicos para sistemas de arquivos; você não pode ter dois números de inode iguais em um único sistema de arquivos, o que significa que você não pode referenciar um arquivo em um sistema de arquivos diferente pelo seu número de inode. No entanto, se você usar symlinks, eles não usam números de inode; eles usam nomes de arquivos, então podem ser referenciados entre diferentes sistemas de arquivos.

### Hardlinks

Vamos ver um exemplo de um hardlink:

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

Um hardlink apenas cria outro arquivo com um link para o mesmo inode. Então, se eu modificasse o conteúdo de `myfile2` ou `myhardlink`, a mudança seria vista em ambos. Mas se eu excluísse `myfile2`, o arquivo ainda estaria acessível através de `myhardlink`. É aqui que nossa contagem de links no comando `ls` entra em jogo. A contagem de links é o número de hardlinks que um inode possui. Quando você remove um arquivo, ele diminuirá essa contagem de links. O inode só é excluído quando todos os hardlinks para o inode foram excluídos. Quando você cria um arquivo, sua contagem de links é 1 porque é o único arquivo que está apontando para aquele inode. Ao contrário dos symlinks, os hardlinks não abrangem sistemas de arquivos porque os inodes são únicos para o sistema de arquivos.

### Criando um symlink

```bash
ln -s myfile mylink
```

Para criar um link simbólico, você usa o comando `ln` com `-s` para simbólico, e você especifica um arquivo de destino e então um nome de link.

### Criando um hardlink

```bash
ln somefile somelink
```

Semelhante à criação de um symlink, exceto que desta vez você omite o `-s`.

## Exercise

Brinque com a criação de symlinks e hardlinks. Exclua alguns e veja o que acontece.

## Quiz Question

Qual é o comando usado para criar um symlink?

## Quiz Answer

ln -s
