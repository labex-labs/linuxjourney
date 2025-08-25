---
index: 1
lang: "pt"
title: "Permissões de Arquivo"
meta_title: "Permissões de Arquivo - Permissões"
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

As próximas três partes do modo de arquivo são as permissões reais. As permissões são agrupadas em 3 bits cada. Os primeiros 3 bits são permissões de usuário, depois permissões de grupo e depois outras permissões. Adicionei o pipe para facilitar a diferenciação.

```plaintext
d | rwx | r-x | r-x
```

Cada caractere representa uma permissão diferente:

- r: leitura
- w: escrita
- x: execução (basicamente um programa executável)
- -: vazio

Então, no exemplo acima, vemos que o usuário pete tem permissões de leitura, escrita e execução no arquivo. O grupo penguins tem permissões de leitura e execução. E, finalmente, os outros usuários (todos os outros) têm permissões de leitura e execução.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão das permissões de arquivo, usuários e grupos do Linux:

1. **[Grupo de Usuários Linux e Permissões de Arquivo](https://labex.io/pt/labs/linux-linux-user-group-and-file-permissions-18002)** - Aprenda conceitos essenciais de gerenciamento de usuários e grupos do Linux, incluindo a criação de usuários, exploração de associações de grupo, compreensão de permissões de arquivo e manipulação de propriedade de arquivo.
2. **[Adicionar Novo Usuário e Grupo](https://labex.io/pt/labs/linux-add-new-user-and-group-17987)** - Pratique a criação de novas contas de usuário, configuração de grupos personalizados e gerenciamento de associações de grupo, simulando tarefas de administração de sistema do mundo real.
3. **[Encontrar um Arquivo](https://labex.io/pt/labs/linux-find-a-file-17993)** - Aplique seu conhecimento de permissões de arquivo encontrando um arquivo específico e definindo sua autoridade de acesso, garantindo que você seja o único usuário autorizado.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança no gerenciamento de permissões e usuários no Linux.

## Quiz Question

Qual bit de permissão é usado para executável?

## Quiz Answer

x
