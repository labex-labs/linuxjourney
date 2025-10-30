---
index: 6
lang: "pt"
title: "Setgid"
meta_title: "Setgid - Permissões"
meta_description: "Aprenda sobre as permissões SGID (Set Group ID) do Linux, como elas funcionam e como modificá-las. Entenda este conceito crucial de segurança do Linux."
meta_keywords: "Linux SGID, Set Group ID, permissões Linux, chmod g+s, segurança Linux, Linux para iniciantes, tutorial Linux"
---

## Lesson Content

Semelhante ao bit de permissão set user ID, existe um bit de permissão set group ID (SGID). Este bit permite que um programa seja executado como se fosse um membro desse grupo.

Vamos ver um exemplo:

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

Agora podemos ver que o bit de permissão está no conjunto de permissões do grupo.

### Modificando SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

A representação numérica para SGID é 2.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão das permissões de usuário, grupo e arquivo do Linux:

1. **[Permissões de Usuário, Grupo e Arquivo do Linux](https://labex.io/pt/labs/linux-linux-user-group-and-file-permissions-18002)** - Aprenda conceitos essenciais de gerenciamento de usuário e grupo do Linux, incluindo a criação e gerenciamento de usuários, exploração de associações de grupo, compreensão de permissões de arquivo e manipulação de propriedade de arquivo.
2. **[Adicionar Novo Usuário e Grupo](https://labex.io/pt/labs/linux-add-new-user-and-group-17987)** - Pratique a criação de novas contas de usuário, configuração de grupos personalizados e gerenciamento de associações de grupo, simulando tarefas de administração de sistema do mundo real.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com as permissões e o gerenciamento de usuários do Linux.

## Quiz Question

Qual número representa o SGID?

## Quiz Answer

2
