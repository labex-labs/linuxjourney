---
index: 3
lang: "pt"
title: "Permissões de Propriedade"
meta_title: "Permissões de Propriedade - Permissões"
meta_description: "Aprenda como mudar a propriedade de arquivos no Linux usando os comandos chown e chgrp. Entenda as permissões de usuário e grupo com este tutorial de Linux para iniciantes."
meta_keywords: "chown, chgrp, propriedade de arquivo Linux, permissões Linux, comandos Linux, Linux para iniciantes, tutorial Linux, guia Linux"
---

## Lesson Content

Além de modificar as permissões em arquivos, você também pode modificar o grupo e a propriedade do usuário do arquivo.

### Modificar a propriedade do usuário

```bash
sudo chown patty myfile
```

Este comando definirá o proprietário de `myfile` como `patty`.

### Modificar a propriedade do grupo

```bash
sudo chgrp whales myfile
```

Este comando definirá o grupo de `myfile` como `whales`.

### Modificar a propriedade do usuário e do grupo ao mesmo tempo

Se você adicionar dois pontos e o nome do grupo após o usuário, poderá definir o usuário e o grupo ao mesmo tempo.

```bash
sudo chown patty:whales myfile
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre propriedade e permissões de arquivos:

1. **[Grupo de Usuários Linux e Permissões de Arquivos](https://labex.io/pt/labs/linux-linux-user-group-and-file-permissions-18002)** - Aprenda conceitos essenciais de gerenciamento de usuários e grupos Linux, incluindo a compreensão de permissões de arquivos e a manipulação da propriedade de arquivos. Este laboratório oferece experiência prática na segurança de um ambiente Linux multiusuário.
2. **[Adicionar Novo Usuário e Grupo](https://labex.io/pt/labs/linux-add-new-user-and-group-17987)** - Neste desafio, você simulará a adição de novos membros da equipe a um ambiente de servidor, criando novas contas de usuário, configurando grupos personalizados e gerenciando associações de grupo. Isso testará suas habilidades em administração de usuários e grupos Linux.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança no gerenciamento de propriedade e permissões de arquivos no Linux.

## Quiz Question

Qual comando você usa para mudar a propriedade do usuário?

## Quiz Answer

chown
