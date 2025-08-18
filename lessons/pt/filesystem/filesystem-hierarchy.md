---
lang: "pt"
title: "Hierarquia do Sistema de Arquivos"
meta_title: "Hierarquia do Sistema de Arquivos - O Filesystem"
meta_description: "Aprenda o Filesystem Hierarchy Standard (FHS) do Linux e entenda diretórios chave como /bin, /etc e /var. Explore a estrutura de diretórios do Linux."
meta_keywords: "Hierarquia do Sistema de Arquivos Linux, FHS, estrutura de diretórios Linux, comandos Linux, Linux para iniciantes, tutorial Linux, guia Linux"
---

## Lesson Content

A esta altura, você provavelmente já está bem familiarizado com a estrutura de diretórios do seu sistema; se não, estará em breve. Os sistemas de arquivos podem variar na forma como são estruturados, mas, na maior parte, devem estar em conformidade com o Filesystem Hierarchy Standard.

Prossiga e execute um `ls -l /` para ver os diretórios listados sob o diretório raiz. O seu pode parecer diferente do meu, mas os diretórios, na maior parte, devem ser semelhantes aos seguintes:

- `/` - O diretório raiz de toda a hierarquia do sistema de arquivos; tudo está aninhado sob este diretório.
- `/bin` - Programas essenciais prontos para execução (binários); inclui os comandos mais básicos, como `ls` e `cp`.
- `/boot` - Contém arquivos do carregador de inicialização do kernel.
- `/dev` - Arquivos de dispositivo.
- `/etc` - Diretório de configuração central do sistema; deve conter apenas arquivos de configuração e nenhum binário.
- `/home` - Diretórios pessoais para usuários; contém seus documentos, arquivos, configurações, etc.
- `/lib` - Contém arquivos de biblioteca que os binários podem usar.
- `/media` - Usado como ponto de montagem para mídias removíveis, como unidades USB.
- `/mnt` - Sistemas de arquivos montados temporariamente.
- `/opt` - Pacotes de software de aplicação opcionais.
- `/proc` - Informações sobre processos em execução atualmente.
- `/root` - O diretório home do usuário root.
- `/run` - Informações sobre o sistema em execução desde a última inicialização.
- `/sbin` - Contém binários essenciais do sistema, geralmente só podem ser executados pelo root.
- `/srv` - Dados específicos do site que são servidos pelo sistema.
- `/tmp` - Armazenamento para arquivos temporários.
- `/usr` - Este nome é infeliz; na maioria das vezes, não contém arquivos de usuário no sentido de uma pasta home. Destina-se a softwares e utilitários instalados pelo usuário; no entanto, isso não significa que você não possa adicionar diretórios pessoais lá. Dentro deste diretório, existem subdiretórios para `/usr/bin`, `/usr/local`, etc.
- `/var` - Diretório variável; é usado para registro do sistema, rastreamento de usuários, caches, etc. Basicamente, qualquer coisa que esteja sujeita a mudanças o tempo todo.

## Exercise

Look inside your `/usr` directory. What kind of information is located there?

## Quiz Question

Qual diretório é usado para armazenar logs?

## Quiz Answer

/var
