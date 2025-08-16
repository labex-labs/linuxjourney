---
title: "yum e apt"
description: "Aprenda yum e apt para gerenciamento de pacotes Linux. Instale, remova e atualize software em sistemas Debian/RPM com este tutorial para iniciantes. Comece hoje mesmo!"
keywords: "yum, apt, gerenciamento de pacotes Linux, tutorial apt, tutorial yum, comandos Linux, guia para iniciantes, instalação de pacotes"
---

## Lesson Content

Ah, os Batmans do gerenciamento de pacotes! Esses sistemas vêm com todos os recursos para facilitar a instalação, remoção e alteração de pacotes, incluindo a instalação de dependências de pacotes. Dois dos sistemas de gerenciamento mais populares são o **yum** e o **apt**. O Yum é exclusivo da família Red Hat, e o apt é exclusivo da família Debian.

### Install a package from a repository

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### Remove a package

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### Updating packages for a repository

É sempre uma boa prática atualizar seus repositórios de pacotes para que estejam atualizados antes de instalar e atualizar um pacote.

```bash
Debian: apt update; apt upgrade
RPM: yum update
```

### Get information about an installed package

```bash
Debian: apt show package_name
RPM: yum info package_name
```

## Exercise

Execute cada um desses comandos de pacote e veja a saída que você recebe.

## Quiz Question

Qual comando é usado para mostrar informações de pacote em um sistema Debian?

## Quiz Answer

apt show
