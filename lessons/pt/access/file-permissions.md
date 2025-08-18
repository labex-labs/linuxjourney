---
lang: "pt"
title: "Permissões de Arquivo"
meta_description: "Aprenda as permissões de arquivo do Linux: entenda os bits rwx, usuário, grupo e outras permissões. Domine a saída de `ls -l` para iniciantes. Comece sua jornada no Linux!"
meta_keywords: "permissões de arquivo Linux, comando ls -l, permissões rwx, tutorial Linux, modos de arquivo, Linux para iniciantes, guia Linux"
---

## Lesson Content

Como aprendemos anteriormente, os arquivos têm diferentes permissões ou modos de arquivo. Vejamos um exemplo:

```bash
$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
```

Existem quatro partes nas permissões de um arquivo. A primeira parte é o tipo de arquivo, que é denotado pelo primeiro caractere nas permissões. No nosso caso, como estamos olhando para um diretório, ele mostra **d** para o tipo de arquivo. Mais comumente, você verá um **-** para um arquivo regular.

A próxima três partes do modo de arquivo são as permissões reais. As permissões são agrupadas em 3 bits cada. Os primeiros 3 bits são permissões de usuário, depois permissões de grupo e depois outras permissões. Adicionei o pipe para facilitar a diferenciação.

```plaintext
d | rwx | r-x | r-x
```

Cada caractere representa uma permissão diferente:

- r: readable
- w: writable
- x: executable (basicamente um programa executável)
- -: empty

Então, no exemplo acima, vemos que o usuário pete tem permissões de leitura, escrita e execução no arquivo. O grupo penguins tem permissões de leitura e execução. E, finalmente, os outros usuários (todos os outros) têm permissões de leitura e execução.

## Exercise

Use o comando `ls -l` em vários arquivos e recite suas permissões, usuário e grupo.

## Quiz Question

Qual bit de permissão é usado para executável?

## Quiz Answer

x
