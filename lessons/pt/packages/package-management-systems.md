---
index: 6
lang: "pt"
title: "yum e apt"
meta_title: "yum e apt - Pacotes"
meta_description: "Aprenda yum e apt para gerenciamento de pacotes Linux. Instale, remova e atualize software em sistemas Debian/RPM com este tutorial para iniciantes. Comece hoje!"
meta_keywords: "yum, apt, gerenciamento de pacotes Linux, tutorial apt, tutorial yum, comandos Linux, guia para iniciantes, instalação de pacotes"
---

## Lesson Content

Ah, os Batmans do gerenciamento de pacotes! Esses sistemas vêm com todos os recursos para facilitar a instalação, remoção e alteração de pacotes, incluindo a instalação de dependências de pacotes. Dois dos sistemas de gerenciamento mais populares são o **yum** e o **apt**. O Yum é exclusivo da família Red Hat, e o apt é exclusivo da família Debian.

### Instalar um pacote de um repositório

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### Remover um pacote

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### Atualizando pacotes para um repositório

É sempre uma boa prática atualizar seus repositórios de pacotes para que estejam atualizados antes de instalar e atualizar um pacote.

```bash
Debian: apt update; apt upgrade
RPM: yum update
```

### Obter informações sobre um pacote instalado

```bash
Debian: apt show package_name
RPM: yum info package_name
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento de pacotes Linux:

1. **[Consultar e Atualizar Pacotes com YUM no Linux](https://labex.io/pt/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - Pratique o gerenciamento de pacotes de software em sistemas Linux baseados em RHEL usando YUM, incluindo inspeção, atualização e exploração de repositórios.
2. **[Instalação de Software no Linux](https://labex.io/pt/labs/linux-software-installation-on-linux-18005)** - Aprenda vários métodos para instalar e gerenciar software em sistemas Ubuntu, incluindo o uso de apt, dpkg e o manuseio de arquivos .deb.
3. **[Instalando e Removendo Pacotes](https://labex.io/pt/labs/linux-installing-and-removing-packages-385380)** - Pratique a atualização do sistema, a instalação e remoção de pacotes e a otimização da configuração de software em um sistema baseado em Debian usando `apt`.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com o gerenciamento de pacotes Linux.

## Quiz Question

Qual comando é usado para mostrar informações de pacotes em um sistema Debian?

## Quiz Answer

apt show
