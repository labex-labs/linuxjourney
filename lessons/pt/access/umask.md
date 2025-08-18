---
lang: "pt"
title: "Umask"
meta_title: "Umask - Permissões"
meta_description: "Aprenda a usar o comando `umask` para controlar as permissões padrão de arquivos no Linux. Entenda as permissões numéricas e gerencie o acesso a novos arquivos facilmente."
meta_keywords: "umask, permissões linux, permissões de arquivo, comandos linux, linux para iniciantes, tutorial linux, permissões padrão"
---

## Lesson Content

Todo arquivo que é criado vem com um conjunto padrão de permissões. Se você quiser alterar esse conjunto padrão de permissões, pode fazê-lo com o comando `umask`. Este comando usa o conjunto de permissões de 3 bits que vemos nas permissões numéricas.

Em vez de adicionar essas permissões, no entanto, `umask` remove essas permissões.

```bash
umask 021
```

No exemplo acima, estamos declarando que queremos que as permissões padrão de novos arquivos permitam acesso total aos usuários, mas para grupos, queremos remover a permissão de escrita, e para outros, queremos remover a permissão de execução. O `umask` padrão na maioria das distribuições é `022`, significando acesso total para o usuário, mas sem acesso de escrita para o grupo e outros usuários.

Quando você executa o comando `umask`, ele aplicará esse conjunto padrão de permissões a qualquer novo arquivo que você criar. No entanto, se você quiser que ele persista, terá que modificar seu arquivo de inicialização (`.profile`), mas discutiremos isso em uma lição posterior.

## Exercise

1. Crie um novo arquivo e, em seguida, anote suas permissões.
2. Modifique o `umask` e, em seguida, crie outro novo arquivo.
3. Verifique as permissões novamente no novo arquivo. O que você espera ver?

## Quiz Question

Qual comando é usado para alterar as permissões padrão de arquivos?

## Quiz Answer

umask
