---
index: 6
lang: "pt"
title: "Ferramentas de Gerenciamento de Usuários"
meta_title: "Ferramentas de Gerenciamento de Usuários - Gerenciamento de Usuários"
meta_description: "Aprenda gerenciamento de usuários Linux: adicione, remova e altere senhas com os comandos useradd, userdel e passwd. Comece com este guia amigável para iniciantes!"
meta_keywords: "gerenciamento de usuários Linux, adduser, userdel, passwd, tutorial Linux, Linux para iniciantes, contas de usuário, comandos Linux"
---

## Lesson Content

A maioria dos ambientes empresariais utiliza sistemas de gestão para gerenciar usuários, contas e senhas. No entanto, em um computador de máquina única, existem comandos úteis para gerenciar usuários.

### Adicionando Usuários

Você pode usar o comando `adduser` ou `useradd`. O comando `adduser` contém recursos mais úteis, como a criação de um diretório home e muito mais. Existem arquivos de configuração para adicionar novos usuários que podem ser personalizados dependendo do que você deseja alocar para um usuário padrão.

```bash
sudo useradd bob
```

Você verá que o comando acima cria uma entrada em `/etc/passwd` para bob, configura grupos padrão e adiciona uma entrada ao arquivo `/etc/shadow`.

### Removendo Usuários

Para remover um usuário, você pode usar o comando `userdel`.

```bash
sudo userdel bob
```

Isso basicamente faz o possível para desfazer as alterações de arquivo feitas por `useradd`.

### Alterando Senhas

```bash
passwd bob
```

Isso permitirá que você altere a senha de si mesmo ou de outro usuário (se você for root).

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento de usuários e contas no Linux:

1. **[Gerenciar Contas de Usuário Linux com useradd, usermod e userdel](https://labex.io/pt/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratique o ciclo de vida completo da administração de usuários, desde a criação e segurança de novas contas até a modificação e exclusão delas.
2. **[Gerenciar Grupos Linux com groupadd, usermod e groupdel](https://labex.io/pt/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Ganhe experiência prática com utilitários de linha de comando essenciais para a administração de grupos, incluindo adicionar, modificar e excluir grupos.
3. **[Configurar Contas de Usuário e Privilégios Sudo no Linux](https://labex.io/pt/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprenda técnicas essenciais para gerenciar contas de usuário e privilégios sudo para aumentar a segurança de um sistema Linux.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com o gerenciamento de usuários e grupos no Linux.

## Quiz Question

Qual comando é usado para alterar uma senha?

## Quiz Answer

passwd
