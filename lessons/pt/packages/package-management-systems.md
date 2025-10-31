---
index: 6
lang: "pt"
title: "yum e apt"
meta_title: "yum e apt - Pacotes"
meta_description: "Explore as principais diferenças no debate yum vs apt. Este guia aborda como usar yum e apt para instalar, remover e atualizar pacotes em sistemas Linux baseados em RPM e Debian."
meta_keywords: "yum vs apt, yum apt, gerenciamento de pacotes linux, apt, yum, debian, red hat, instalar pacotes, atualizar pacotes, comandos linux"
---

## Lesson Content

Gerenciadores de pacotes são ferramentas essenciais no Linux que simplificam a instalação, atualização e remoção de software. Eles gerenciam automaticamente as dependências, garantindo que todas as bibliotecas e componentes necessários sejam instalados corretamente. Dois dos sistemas de gerenciamento de pacotes mais proeminentes são **yum** e **apt**.

### Yum vs Apt

A principal diferença entre esses dois sistemas reside nas distribuições Linux que eles atendem. O gerenciador de pacotes `yum` (Yellowdog Updater, Modified) é usado por distribuições baseadas em RPM, como Red Hat, CentOS e Fedora. Em contraste, o `apt` (Advanced Package Tool) é o padrão para distribuições baseadas em Debian, incluindo o Ubuntu. Embora tanto o `yum` quanto o `apt` atinjam os mesmos objetivos, sua sintaxe de comando difere.

### Instalando e Removendo Pacotes

Para instalar um novo software de um repositório, você usa o comando `install`.

```bash
Debian: $ apt install nome_do_pacote
RPM: $ yum install nome_do_pacote
```

Para remover um pacote, os comandos também são diretos. O `apt` usa `remove`, enquanto o `yum` usa `erase`.

```bash
Debian: $ apt remove nome_do_pacote
RPM: $ yum erase nome_do_pacote
```

### Atualizando e Inspecionando Pacotes

É uma boa prática atualizar seu índice de pacotes local antes de instalar ou atualizar software. Isso garante que você está obtendo as versões mais recentes disponíveis.

Para sistemas Debian, este é um processo de duas etapas: `apt update` atualiza a lista de pacotes e `apt upgrade` instala as novas versões. Para sistemas RPM, `yum update` lida com ambas as ações com um único comando.

```bash
Debian: $ apt update; apt upgrade
RPM: $ yum update
```

Se você precisar obter mais detalhes sobre um pacote específico, pode usar os seguintes comandos para exibir informações como sua versão, tamanho e descrição.

```bash
Debian: $ apt show nome_do_pacote
RPM: $ yum info nome_do_pacote
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento de pacotes no Linux:

1. **[Consultar e Atualizar Pacotes com YUM no Linux](https://labex.io/pt/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - Pratique o gerenciamento de pacotes de software em sistemas Linux baseados em RHEL usando YUM, incluindo inspeção, atualização e exploração de repositórios.
2. **[Instalação de Software no Linux](https://labex.io/pt/labs/linux-software-installation-on-linux-18005)** - Aprenda vários métodos para instalar e gerenciar software em sistemas Ubuntu, incluindo o uso de apt, dpkg e o manuseio de arquivos .deb.
3. **[Instalando e Removendo Pacotes](https://labex.io/pt/labs/linux-installing-and-removing-packages-385380)** - Pratique a atualização do sistema, a instalação e remoção de pacotes e a otimização da configuração de software em um sistema baseado em Debian usando `apt`.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança no gerenciamento de pacotes do Linux.

## Quiz Question

What command is used to show package information on a Debian system? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

apt show
