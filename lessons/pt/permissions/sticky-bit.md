---
index: 8
lang: "pt"
title: "O Bit Pegajoso"
meta_title: "O Bit Pegajoso - Permissões"
meta_description: "Explore a finalidade do bit pegajoso nas permissões de arquivos Linux e Unix. Aprenda como o bit pegajoso protege arquivos em diretórios compartilhados como /tmp e como configurá-lo usando chmod."
meta_keywords: "bit pegajoso, bit pegajoso linux, permissões de arquivo unix bit pegajoso, chmod +t, diretório /tmp, permissões de arquivo, segurança linux"
---

## Lesson Content

Além das permissões padrão de leitura, gravação e execução, o Linux oferece permissões especiais para controle de acesso avançado. A última dessas permissões especiais que abordaremos é o **sticky bit** (bit pegajoso).

### O que é o Sticky Bit?

O sticky bit é uma configuração de permissão que pode ser aplicada a um diretório. Quando o sticky bit está definido em um diretório, os arquivos dentro desse diretório só podem ser excluídos ou renomeados pelo proprietário do arquivo, pelo proprietário do diretório ou pelo usuário root. Isso é particularmente útil para diretórios compartilhados onde vários usuários precisam criar e gerenciar seus próprios arquivos sem interferir nos outros. Este conceito é uma parte fundamental do gerenciamento de **permissões de arquivo Unix sticky bit**.

### Um Exemplo Prático: O Diretório /tmp

Um caso de uso comum para o **sticky bit no Linux** é o diretório `/tmp`, que é um local gravável por todos para arquivos temporários. Vamos examinar suas permissões:

```bash
$ ls -ld /tmp
drwxrwxrwt 17 root root 4096 Dez 15 11:45 /tmp
```

Note o `t` no final da string de permissão (`rwxrwxrwt`). Este `t` indica que o sticky bit está definido. Por causa disso, embora qualquer usuário possa criar arquivos em `/tmp`, eles não podem excluir ou mover arquivos criados por outros usuários. Isso impede que um usuário perturbe o trabalho de outro neste espaço compartilhado.

### Como Definir o Sticky Bit

Você pode definir o sticky bit usando o comando `chmod` de duas maneiras: modo simbólico ou modo octal (numérico).

Para adicionar o sticky bit usando o modo simbólico:

```bash
chmod +t meu_dir_compartilhado
```

Para definir permissões usando o modo octal, você antepõe um `1` ao código de permissão padrão de três dígitos. A representação numérica para o sticky bit é **1**.

```bash
# Isso define as permissões como rwxr-xr-x com o sticky bit
chmod 1755 meu_dir_compartilhado
```

Compreender o sticky bit é essencial para gerenciar ambientes multiusuário e proteger diretórios compartilhados de forma eficaz.

## Exercise

Para solidificar sua compreensão das permissões de arquivo, incluindo permissões especiais como o sticky bit, experimente estes laboratórios práticos. Eles ajudarão você a ver como esses conceitos se aplicam em cenários do mundo real.

1. **[Grupo de Usuários Linux e Permissões de Arquivo](https://labex.io/pt/labs/linux-linux-user-group-and-file-permissions-18002)** - Pratique a criação de usuários e grupos e a manipulação da propriedade e permissões de arquivos. Este laboratório fornece uma base para entender como as permissões especiais funcionam.
2. **[Excluir e Mover Arquivos](https://labex.io/pt/labs/linux-delete-and-move-files-7777)** - Aprenda a excluir e mover arquivos e veja como as permissões, incluindo o sticky bit em um diretório, podem restringir essas ações.
3. **[Encontrar um Arquivo](https://labex.io/pt/labs/linux-find-a-file-17993)** - Pratique a localização de arquivos e a definição de controles de acesso, reforçando a importância das permissões de arquivo no gerenciamento do acesso e modificação de arquivos.

## Quiz Question

Em uma listagem longa de diretório (ls -l), qual caractere único na string de permissões representa que o sticky bit está definido? Por favor, responda com uma única letra minúscula em inglês.

## Quiz Answer

t
