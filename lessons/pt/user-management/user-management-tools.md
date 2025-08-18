---
lang: "pt"
title: "Ferramentas de Gerenciamento de Usuários"
meta_description: "Aprenda o gerenciamento de usuários Linux: adicione, remova e altere senhas com os comandos useradd, userdel e passwd. Comece com este guia para iniciantes!"
meta_keywords: "gerenciamento de usuários Linux, adduser, userdel, passwd, tutorial Linux, Linux para iniciantes, contas de usuário, comandos Linux"
---

## Lesson Content

A maioria dos ambientes corporativos utiliza sistemas de gerenciamento para administrar usuários, contas e senhas. No entanto, em um computador de máquina única, existem comandos úteis para gerenciar usuários.

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

Isso permitirá que você altere a sua própria senha ou a de outro usuário (se você for root).

## Exercise

Crie um novo usuário, depois altere a senha dele e faça login como o novo usuário.

## Quiz Question

Qual comando é usado para alterar uma senha?

## Quiz Answer

passwd
