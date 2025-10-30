---
index: 4
lang: "pt"
title: "Umask"
meta_title: "Umask - Permissões"
meta_description: "Aprenda a usar o comando `umask` para controlar as permissões padrão de arquivos no Linux. Entenda as permissões numéricas e gerencie o acesso a novos arquivos facilmente."
meta_keywords: "umask, permissões linux, permissões de arquivo, comandos linux, linux para iniciantes, tutorial linux, permissões padrão"
---

## Lesson Content

Todo arquivo que é criado vem com um conjunto padrão de permissões. Se você quiser alterar esse conjunto padrão de permissões, pode fazê-lo com o comando `umask`. Este comando usa o conjunto de permissões de 3 bits que vemos nas permissões numéricas.

No entanto, em vez de adicionar essas permissões, `umask` as remove.

```bash
umask 021
```

No exemplo acima, estamos afirmando que queremos que as permissões padrão de novos arquivos permitam aos usuários acesso a tudo, mas para grupos, queremos remover sua permissão de escrita, e para outros, queremos remover sua permissão de execução. O `umask` padrão na maioria das distribuições é `022`, o que significa acesso total para o usuário, mas sem acesso de escrita para o grupo e outros usuários.

Quando você executa o comando `umask`, ele aplicará esse conjunto padrão de permissões a qualquer novo arquivo que você criar. No entanto, se você quiser que ele persista, terá que modificar seu arquivo de inicialização (`.profile`), mas discutiremos isso em uma lição posterior.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão das permissões de arquivo e como elas se relacionam com as configurações padrão:

1. **[Grupo de Usuários Linux e Permissões de Arquivo](https://labex.io/pt/labs/linux-linux-user-group-and-file-permissions-18002)** - Pratique a criação e gerenciamento de usuários, explorando associações de grupo, entendendo permissões de arquivo e manipulando a propriedade de arquivos. Este laboratório oferece experiência prática na segurança de um ambiente Linux multiusuário, o que é crucial para entender como `umask` influencia as permissões de novos arquivos.

Este laboratório o ajudará a aplicar os conceitos de permissões de arquivo em cenários reais e a construir confiança no gerenciamento de acesso no Linux.

## Quiz Question

Qual comando é usado para alterar as permissões padrão de arquivos?

## Quiz Answer

umask
