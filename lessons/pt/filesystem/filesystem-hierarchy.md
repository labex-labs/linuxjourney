---
index: 1
lang: "pt"
title: "Hierarquia do Sistema de Arquivos"
meta_title: "Hierarquia do Sistema de Arquivos - O Sistema de Arquivos"
meta_description: "Explore a hierarquia padrão do sistema de arquivos Linux (FHS). Este guia explica a finalidade de diretórios chave como /bin, /etc, /home e /var, fornecendo uma visão clara da hierarquia do sistema de arquivos no Linux."
meta_keywords: "hierarquia do sistema de arquivos linux, hierarquia do sistema de arquivos no linux, estrutura de hierarquia de arquivos linux, hierarquia de arquivos linux, FHS, estrutura de diretórios linux"
---

## Lesson Content

Você provavelmente está se familiarizando com a estrutura de diretórios em seu sistema. A maioria das distribuições Linux organiza seus sistemas de arquivos de acordo com o Padrão de **Hierarquia do Sistema de Arquivos Linux** (FHS). Este padrão garante que os arquivos sejam armazenados em locais previsíveis, tornando os sistemas mais consistentes.

Para ver os diretórios de nível superior, execute o comando `ls -l /`. Embora seu sistema possa ter pequenas diferenças, a **estrutura da hierarquia de arquivos do linux** principal será muito semelhante à descrita abaixo.

### O Diretório Raiz

- `/` - Este é o diretório raiz, o ponto de partida para todo o sistema de arquivos. Cada arquivo e diretório em seu sistema está localizado sob este diretório.

### Diretórios Essenciais do Sistema

A **hierarquia de arquivos no linux** inclui vários diretórios críticos para a operação do sistema.

- `/bin` - Contém programas essenciais de linha de comando (binários) disponíveis para todos os usuários, como `ls`, `cp` e `mv`.
- `/sbin` - Contém binários essenciais do sistema, que são destinados principalmente à administração do sistema e geralmente só podem ser executados pelo usuário root.
- `/etc` - Este é o diretório central de configuração do sistema. Ele contém arquivos de configuração para o sistema operacional e aplicativos instalados, mas não deve conter binários executáveis.
- `/lib` - Contém arquivos de biblioteca compartilhada essenciais dos quais os binários do sistema em `/bin` e `/sbin` dependem para funcionar corretamente.
- `/boot` - Armazena os arquivos necessários para o processo de inicialização do sistema, incluindo o kernel Linux e os arquivos do carregador de inicialização.

### Dados do Usuário e Aplicações

- `/home` - Contém diretórios pessoais para cada usuário. É aqui que você armazena seus documentos, configurações de aplicativos e outros arquivos pessoais.
- `/root` - O diretório pessoal do usuário root, separado do diretório `/home` para garantir que o usuário root possa fazer login mesmo que `/home` não esteja disponível.
- `/opt` - Reservado para pacotes de software de aplicativos opcionais ou de terceiros.
- `/usr` - Este diretório contém software e utilitários instalados pelo usuário. Apesar do nome, geralmente não contém arquivos pessoais de usuários individuais. Ele tem sua própria estrutura de subdiretórios, como `/usr/bin` para binários de usuário não essenciais e `/usr/local` para software compilado a partir do código-fonte.

### Dados Dinâmicos e Temporários

- `/var` - Significa "variável" e armazena arquivos que se espera que mudem de tamanho e conteúdo, como logs do sistema (`/var/log`), caches e arquivos de spool.
- `/tmp` - Um espaço gravável por todos para armazenar arquivos temporários. Arquivos neste diretório são frequentemente excluídos na reinicialização do sistema.
- `/run` - Contém informações sobre o sistema em execução desde a última inicialização, como IDs de processo (PIDs) e outros dados de tempo de execução.

### Dispositivos e Pontos de Montagem

- `/dev` - Contém arquivos de dispositivo especiais que representam componentes de hardware como discos rígidos, terminais e dispositivos de entrada.
- `/media` - Um ponto de montagem padrão para mídia removível, como unidades USB, cartões SD e CD-ROMs.
- `/mnt` - Um ponto de montagem genérico para montar sistemas de arquivos temporariamente.

### Informações do Sistema

- `/proc` - Um sistema de arquivos virtual que fornece informações em tempo real sobre processos em execução e parâmetros do kernel.
- `/srv` - Destinado a dados específicos do site servidos pelo sistema, como arquivos para um servidor web.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do sistema de arquivos Linux:

1. **[Navegar no Sistema de Arquivos no Linux](https://labex.io/pt/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Pratique o uso de comandos essenciais do shell como `pwd`, `cd` e `ls` para se mover entre diretórios e explorar o sistema de arquivos.
2. **[Gerenciar Arquivos e Diretórios no Linux](https://labex.io/pt/labs/comptia-manage-files-and-directories-in-linux-590835)** - Aprenda a criar, remover, copiar e mover arquivos e diretórios, e entenda links simbólicos e rígidos.
3. **[Encontrar Arquivos e Comandos no Linux](https://labex.io/pt/labs/comptia-find-files-and-commands-in-linux-590834)** - Domine técnicas para localizar arquivos e comandos usando `find`, `locate`, `whereis`, `which` e `type`.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança no gerenciamento do sistema de arquivos Linux.

## Quiz Question

Qual diretório é usado para armazenar logs? (Por favor, forneça o caminho completo. A resposta diferencia maiúsculas de minúsculas e deve estar em inglês.)

## Quiz Answer

/var
