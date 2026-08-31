---
lesson_id: "filesystem-hierarchy"
course_id: "filesystem"
lang: "pt"
order_index: 1
title: "Hierarquia do Sistema de Arquivos"
description: "Aprenda as funções pretendidas dos principais diretórios Linux e como os layouts modernos unificados podem ser diferentes."
meta_title: "Hierarquia do Sistema de Arquivos - O Sistema de Arquivos"
meta_description: "Conheça a hierarquia padrão do sistema de arquivos Linux (FHS). Este guia explica a finalidade de diretórios importantes como /bin, /etc, /home e /var."
meta_keywords: "hierarquia do sistema de arquivos Linux, sistema de arquivos Linux, estrutura hierárquica Linux, hierarquia de arquivos Linux, FHS, estrutura de diretórios Linux"
---

O Linux apresenta os sistemas de arquivos montados como uma única árvore de diretórios enraizada em `/`. O Filesystem Hierarchy Standard, ou FHS, atribui funções convencionais a muitos diretórios, mas distribuições, contêineres, sistemas imutáveis e políticas locais podem ser diferentes. Inspecione o host real antes de depender de um caminho.

```bash
$ ls -ld /*
```

## Raiz e Caminhos Essenciais do Sistema

- `/` é a raiz da árvore visível do sistema de arquivos.
- `/etc` contém a configuração do sistema específica do host. Ele pode conter scripts auxiliares ou de inicialização executáveis, portanto é incorreto afirmar que nunca possui conteúdo executável.
- `/boot` contém arquivos relacionados à inicialização, como dados do carregador de boot e, em muitos sistemas, kernels e imagens iniciais do sistema de arquivos em RAM.
- `/bin` e `/sbin` tradicionalmente contêm comandos essenciais para usuários e para a administração do sistema.
- `/lib` e suas variantes específicas de arquitetura tradicionalmente contêm bibliotecas compartilhadas essenciais e componentes do carregador.

Muitas distribuições atuais usam um layout `/usr` unificado, no qual `/bin`, `/sbin` e `/lib` são links simbólicos para os diretórios correspondentes em `/usr`. Use a descoberta de comandos e os registros de pacotes em vez de presumir se um caminho é um diretório físico ou um link.

:::single-choice{#filesystem-hierarchy-configuration-directory}
Qual diretório contém convencionalmente a configuração do sistema específica do host?

::option[`/proc`]{#filesystem-hierarchy-proc-config explanation="O procfs apresenta interfaces ativas de processos e do kernel, não arquivos persistentes de configuração do host."}
::option[`/etc`]{#filesystem-hierarchy-etc .correct explanation="A configuração do sistema e dos serviços é convencionalmente organizada em `/etc`."}
::option[`/dev`]{#filesystem-hierarchy-dev-config explanation="`/dev` contém objetos voltados aos dispositivos em tempo de execução, não a hierarquia geral de configuração."}
:::

## Software da Distribuição e Software Local

- `/usr` contém a principal hierarquia compartilhável e predominantemente somente para leitura do sistema operacional e das aplicações, incluindo comandos, bibliotecas e dados independentes da arquitetura.
- `/usr/local` é reservado para software e dados instalados pelo administrador local fora do gerenciamento normal de `/usr` pela distribuição.
- `/opt` pode conter pacotes de aplicações adicionais em subárvores autocontidas.

Apesar do nome, `/usr` não é o local onde normalmente ficam os arquivos pessoais de cada usuário. Os gerenciadores de pacotes da distribuição geralmente controlam grande parte desse diretório, portanto copiar arquivos compilados localmente para `/usr/bin` pode entrar em conflito com os pacotes gerenciados.

:::single-choice{#filesystem-hierarchy-local-software}
Qual prefixo é convencionalmente reservado ao software instalado localmente fora do conteúdo de `/usr` gerenciado pela distribuição?

::option[`/usr/local`]{#filesystem-hierarchy-usr-local .correct explanation="A hierarquia local separa o software instalado pelo administrador da árvore principal `/usr` da distribuição."}
::option[`/proc/local`]{#filesystem-hierarchy-proc-local explanation="O procfs é uma interface virtual do kernel, não um prefixo persistente de software."}
::option[`/dev/local`]{#filesystem-hierarchy-dev-local explanation="O armazenamento de nós de dispositivos não é o local convencional para aplicações locais."}
:::

## Dados de Usuários e Serviços

- `/home` contém convencionalmente os diretórios pessoais dos usuários que não são root, embora serviços de diretório e políticas locais possam colocá-los em outros locais.
- `/root` é o diretório pessoal convencional da conta root.
- `/srv` é destinado aos dados específicos do local servidos por este sistema.

O caminho do diretório pessoal vem das informações da conta, não apenas da combinação de `/home` com um nome de usuário. Use `getent passwd USER` ou o diretório pessoal resolvido pelo shell em vez de codificar suposições.

:::single-choice{#filesystem-hierarchy-root-home}
Qual é o diretório pessoal convencional da conta root?

::option[`/home/root`]{#filesystem-hierarchy-home-root explanation="Diretórios pessoais comuns muitas vezes ficam em `/home`, mas o root possui um caminho convencional distinto."}
::option[`/root`]{#filesystem-hierarchy-root .correct explanation="O diretório pessoal da conta privilegiada fica convencionalmente diretamente abaixo da raiz do sistema de arquivos."}
::option[`/usr/root`]{#filesystem-hierarchy-usr-root explanation="`/usr` é a hierarquia de software e dados compartilhados, não o diretório pessoal do root."}
:::

## Dados Variáveis, de Execução e Temporários

- `/var` contém dados variáveis, como logs, caches, filas e estados de aplicações. Os logs do sistema normalmente aparecem em `/var/log`, embora alguns sistemas dependam principalmente de uma interface de journal.
- `/run` contém o estado volátil em tempo de execução da inicialização atual, como sockets, estados de serviços e arquivos PID. Ele normalmente é recriado durante o boot.
- `/tmp` é destinado a arquivos temporários e geralmente permite escrita por todos com a proteção do sticky bit.
- `/var/tmp` é destinado a arquivos temporários que devem sobreviver por mais tempo que os arquivos de `/tmp`.

A política de limpeza de `/tmp` varia; não presuma que os arquivos persistam até a reinicialização nem que sempre sejam excluídos durante ela. As aplicações devem criar arquivos temporários com segurança, em vez de usar nomes previsíveis.

:::single-choice{#filesystem-hierarchy-log-path}
Qual caminho armazena convencionalmente os arquivos de log do sistema?

::option[`/etc/log`]{#filesystem-hierarchy-etc-log explanation="`/etc` é destinado à configuração, não a dados comuns de log que se acumulam."}
::option[`/var/log`]{#filesystem-hierarchy-var-log .correct explanation="Os logs são uma categoria de dados mutáveis do sistema, organizada na hierarquia de dados variáveis."}
::option[`/boot/log`]{#filesystem-hierarchy-boot-log explanation="`/boot` é reservado a artefatos relacionados à inicialização, não aos logs gerais de serviços."}
:::

## Dispositivos, Interfaces do Kernel e Pontos de Montagem

- `/dev` contém nós de dispositivos e links relacionados em tempo de execução.
- `/proc` expõe interfaces de processos e do kernel por meio do procfs.
- `/sys` expõe objetos, dispositivos, drivers e atributos do kernel por meio do sysfs.
- `/media` costuma ser usado para mídias removíveis montadas automaticamente.
- `/mnt` é um local convencional para montagens temporárias realizadas pelo administrador.

Essas são convenções, não concessões de permissões. Montar outro sistema de arquivos sobre um diretório não vazio oculta temporariamente o conteúdo anterior do diretório até que ele seja desmontado.

:::single-choice{#filesystem-hierarchy-sysfs-path}
Qual caminho normalmente expõe o modelo de dispositivos do kernel por meio do sysfs?

::option[`/srv`]{#filesystem-hierarchy-srv explanation="`/srv` é destinado aos dados servidos pelo sistema."}
::option[`/sys`]{#filesystem-hierarchy-sys .correct explanation="O sysfs é convencionalmente montado em `/sys` e apresenta dispositivos, drivers, barramentos e atributos."}
::option[`/opt`]{#filesystem-hierarchy-opt explanation="`/opt` contém árvores de aplicações adicionais opcionais."}
:::

Use o laboratório [Navegação pelo Sistema de Arquivos no Linux](https://labex.io/labs/comptia-navigate-the-filesystem-in-linux-590971) para inspecionar esses caminhos e [Localização de Arquivos e Comandos no Linux](https://labex.io/labs/comptia-find-files-and-commands-in-linux-590834) para evitar depender de locais presumidos.

## Resumo

Agora você sabe relacionar os principais caminhos do Linux às suas funções pretendidas, considerando as variações dos sistemas reais.

1. Comece pela árvore unificada enraizada em `/`.
2. Separe configuração, software gerenciado, software local e dados variáveis.
3. Diferencie diretórios pessoais e dados de serviços do estado em tempo de execução.
4. Reconheça `/dev`, `/proc` e `/sys` como interfaces especiais em tempo de execução.
5. Inspecione links simbólicos, montagens, dados de contas e a política da distribuição antes de presumir um layout.
