---
index: 5
lang: "pt"
title: "/etc/group"
meta_title: "/etc/group - Gerenciamento de Usuários"
meta_description: "Aprenda sobre o arquivo /etc/group no Linux, entendendo o gerenciamento de grupos, GID e permissões de usuário. Tutorial essencial sobre o arquivo de grupo Linux para iniciantes."
meta_keywords: "/etc/group, grupos Linux, gerenciamento de grupos, GID, permissões Linux, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Outro arquivo usado no gerenciamento de usuários é o arquivo `/etc/group`. Este arquivo permite diferentes grupos com diferentes permissões.

```bash
$ cat /etc/group

root:*:0:pete
```

Muito parecido com o arquivo `/etc/passwd`, os campos do `/etc/group` são os seguintes:

1. Nome do grupo
2. Senha do grupo - não há necessidade de definir uma senha de grupo; usar um privilégio elevado como `sudo` é padrão. Um asterisco (`*`) será colocado como valor padrão.
3. ID do Grupo (GID)
4. Lista de usuários - você pode especificar manualmente os usuários que deseja em um grupo específico

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento de usuários e grupos no Linux:

1. **[Gerenciar Contas de Usuário Linux com useradd, usermod e userdel](https://labex.io/pt/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratique o ciclo de vida completo da administração de usuários, desde a criação e segurança de novas contas até a modificação e exclusão delas.
2. **[Gerenciar Grupos Linux com groupadd, usermod e groupdel](https://labex.io/pt/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Ganhe experiência prática com utilitários de linha de comando essenciais para a administração de grupos, incluindo `groupadd`, `usermod` e `groupdel`.
3. **[Adicionar Novo Usuário e Grupo](https://labex.io/pt/labs/linux-add-new-user-and-group-17987)** - Simule a adição de novos membros da equipe a um ambiente de servidor, criando novas contas de usuário, configurando grupos personalizados e gerenciando associações a grupos.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com o gerenciamento de usuários e grupos no Linux.

## Quiz Question

Qual é o GID de root?

## Quiz Answer

0
