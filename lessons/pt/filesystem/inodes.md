---
index: 11
lang: "pt"
title: "Inodos"
meta_title: "Inodos - O Sistema de Arquivos"
meta_description: "Explore o conceito do inode do Linux. Saiba o que é um i-node, como os inodos no Linux gerenciam metadados de arquivos e como verificar o uso de inodos com `df -i` e `ls -li`."
meta_keywords: "inode linux, inode no linux, i node, inode, inode linux, número de inode, sistema de arquivos, df -i, ls -li, stat"
---

## Lesson Content

Lembre-se de como nosso sistema de arquivos é composto por todos os nossos arquivos reais e um banco de dados que os gerencia? Este banco de dados é conhecido como tabela de inodes, uma parte fundamental de como o `inode no linux` funciona.

### O que é um Inode do Linux

Um inode (abreviação de nó de índice) é uma entrada nesta tabela. Cada arquivo e diretório tem seu próprio `inode`. Ele descreve tudo sobre o arquivo, como:

- Tipo de arquivo (ex: arquivo regular, diretório, dispositivo de caractere)
- Proprietário
- Grupo
- Permissões de acesso
- Carimbos de data/hora: mtime (última modificação), ctime (última alteração de atributo), atime (último acesso)
- Número de links físicos (hard links) para o arquivo
- Tamanho do arquivo
- Número de blocos alocados para o arquivo
- Ponteiros para os blocos de dados do arquivo (o mais importante!)

Essencialmente, um `i node` armazena todos os metadados sobre o arquivo, exceto seu nome e o conteúdo real.

### Criação e Alocação de Inodes

Quando um sistema de arquivos é criado, espaço para inodes também é alocado. Algoritmos determinam quanto espaço de `inode` você precisa com base no volume do disco e em outros fatores. Você provavelmente já viu erros de falta de espaço em disco antes. O mesmo pode acontecer com inodes, embora seja menos comum. Se você ficar sem inodes, não poderá criar novos arquivos. O armazenamento de dados depende tanto dos blocos de dados quanto do banco de dados (a tabela `inode`).

Para ver quantos inodes restam no seu sistema, use o comando `df -i`. Esta é uma verificação crucial para administradores de sistema que gerenciam um grande número de arquivos pequenos.

### Visualizando Informações do Inode

Cada `linux inode` é identificado por um número exclusivo. Quando um arquivo é criado, ele recebe um número de inode, geralmente sequencialmente. No entanto, você pode notar que um novo arquivo recebe um número de inode menor do que os mais antigos. Isso acontece porque os números de inode excluídos podem ser reutilizados para novos arquivos. Para visualizar os números de inode, execute `ls -li`:

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

O primeiro campo na saída deste comando é o número do inode. Você também pode ver informações detalhadas sobre o `i node` de um arquivo com o comando `stat`:

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

### Como um I-Node Aponta para Dados

Sabemos que nossos dados são armazenados no disco, mas provavelmente não estão em um bloco contínuo. É aqui que a estrutura `inode linux` se torna essencial. Os inodes apontam para os blocos de dados reais dos seus arquivos. Em um sistema de arquivos típico (embora as implementações variem), cada inode contém 15 ponteiros. Os primeiros 12 ponteiros apontam diretamente para blocos de dados. O 13º ponteiro aponta para um bloco que contém mais ponteiros. Os 14º e 15º ponteiros apontam para blocos de ponteiros ainda mais aninhados. Isso pode parecer confuso, mas essa estrutura permite que o `i node` permaneça com um tamanho fixo, sendo capaz de referenciar arquivos de tamanhos variados. Arquivos pequenos podem ser acessados rapidamente usando os ponteiros diretos, enquanto arquivos maiores são localizados através dos ponteiros aninhados.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do sistema de arquivos e gerenciamento de arquivos do Linux:

1. **[Gerenciar Arquivos e Diretórios no Linux](https://labex.io/pt/labs/comptia-manage-files-and-directories-in-linux-590835)** - Pratique a criação, remoção, cópia e movimentação de arquivos e diretórios, e explore a criação de links simbólicos e físicos enquanto analisa inodes.
2. **[Navegar no Sistema de Arquivos no Linux](https://labex.io/pt/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Aprenda as habilidades fundamentais para navegar no sistema de arquivos Linux usando comandos essenciais do shell como `pwd`, `cd` e `ls`.
3. **[Encontrar Arquivos e Comandos no Linux](https://labex.io/pt/labs/comptia-find-files-and-commands-in-linux-590834)** - Domine técnicas essenciais para localizar arquivos e comandos no Linux usando `find`, `locate`, `whereis`, `which` e `type`.

Estes laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança no gerenciamento do sistema de arquivos Linux.

## Quiz Question

Como você vê quantos inodes restam no seu sistema? (Por favor, responda em inglês, prestando atenção à sensibilidade a maiúsculas e minúsculas)

## Quiz Answer

df -i
