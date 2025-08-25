---
index: 1
lang: "pt"
title: "Hierarquia do Sistema de Arquivos"
meta_title: "Hierarquia do Sistema de Arquivos - O Sistema de Arquivos"
meta_description: "Aprenda o Filesystem Hierarchy Standard (FHS) do Linux e entenda diretórios chave como /bin, /etc e /var. Explore a estrutura de diretórios do Linux."
meta_keywords: "Hierarquia do Sistema de Arquivos Linux, FHS, estrutura de diretórios Linux, comandos Linux, Linux para iniciantes, tutorial Linux, guia Linux"
---

## Lesson Content

A esta altura, você provavelmente já está bem familiarizado com a estrutura de diretórios do seu sistema; se não, estará em breve. Os sistemas de arquivos podem variar na forma como são estruturados, mas, na maior parte, devem estar em conformidade com o Filesystem Hierarchy Standard.

Prossiga e execute um `ls -l /` para ver os diretórios listados sob o diretório raiz. O seu pode parecer diferente do meu, mas os diretórios devem, na maior parte, ser semelhantes ao seguinte:

- `/` - O diretório raiz de toda a hierarquia do sistema de arquivos; tudo está aninhado sob este diretório.
- `/bin` - Programas essenciais prontos para serem executados (binários); inclui os comandos mais básicos como `ls` e `cp`.
- `/boot` - Contém arquivos do carregador de inicialização do kernel.
- `/dev` - Arquivos de dispositivo.
- `/etc` - Diretório de configuração do sistema central; deve conter apenas arquivos de configuração e nenhum binário.
- `/home` - Diretórios pessoais para usuários; guarda seus documentos, arquivos, configurações, etc.
- `/lib` - Contém arquivos de biblioteca que os binários podem usar.
- `/media` - Usado como ponto de montagem para mídias removíveis como unidades USB.
- `/mnt` - Sistemas de arquivos montados temporariamente.
- `/opt` - Pacotes de software de aplicativos opcionais.
- `/proc` - Informações sobre processos atualmente em execução.
- `/root` - O diretório home do usuário root.
- `/run` - Informações sobre o sistema em execução desde a última inicialização.
- `/sbin` - Contém binários essenciais do sistema, geralmente só podem ser executados pelo root.
- `/srv` - Dados específicos do site que são servidos pelo sistema.
- `/tmp` - Armazenamento para arquivos temporários.
- `/usr` - Este nome é infeliz; na maioria das vezes, não contém arquivos de usuário no sentido de uma pasta home. Destina-se a software e utilitários instalados pelo usuário; no entanto, isso não quer dizer que você não possa adicionar diretórios pessoais lá. Dentro deste diretório estão subdiretórios para `/usr/bin`, `/usr/local`, etc.
- `/var` - Diretório variável; é usado para registro do sistema, rastreamento de usuários, caches, etc. Basicamente, tudo o que está sujeito a mudanças o tempo todo.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do sistema de arquivos Linux:

1. **[Navegar no Sistema de Arquivos no Linux](https://labex.io/pt/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Pratique o uso de comandos essenciais do shell como `pwd`, `cd` e `ls` para mover-se entre diretórios e explorar o sistema de arquivos.
2. **[Gerenciar Arquivos e Diretórios no Linux](https://labex.io/pt/labs/comptia-manage-files-and-directories-in-linux-590835)** - Aprenda a criar, remover, copiar e mover arquivos e diretórios, e entenda links simbólicos e rígidos.
3. **[Encontrar Arquivos e Comandos no Linux](https://labex.io/pt/labs/comptia-find-files-and-commands-in-linux-590834)** - Domine técnicas para localizar arquivos e comandos usando `find`, `locate`, `whereis`, `which` e `type`.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com o gerenciamento do sistema de arquivos Linux.

## Quiz Question

Qual diretório é usado para armazenar logs?

## Quiz Answer

/var
