---
lesson_id: "filesystem-types"
course_id: "filesystem"
lang: "pt"
order_index: 2
title: "Tipos de Sistemas de Arquivos"
description: "Aprenda como o VFS do Linux apresenta sistemas de arquivos locais, de rede e virtuais por meio de uma única interface."
meta_title: "Tipos de Sistemas de Arquivos - O Sistema de Arquivos"
meta_description: "Conheça diferentes tipos de sistemas de arquivos Linux, incluindo ext4, Btrfs e XFS. Este guia explica conceitos importantes como journaling e o Virtual File System (VFS)."
meta_keywords: "tipos de sistemas de arquivos Linux, sistemas de arquivos, ext4, Btrfs, XFS, journaling, VFS, tutorial Linux"
---

O Linux oferece suporte a muitas implementações de sistemas de arquivos, com diferentes formatos em disco, protocolos de rede, modelos de consistência, recursos e ferramentas operacionais. A escolha adequada depende do suporte da distribuição, da carga de trabalho, dos requisitos de recuperação, da topologia do armazenamento e da experiência do administrador.

## A Camada de Sistema de Arquivos Virtual

A camada Virtual Filesystem do kernel, ou VFS, fornece operações comuns como abertura, leitura, escrita, renomeação e verificações de permissões. As implementações de sistemas de arquivos conectam essas operações às suas próprias estruturas de dados e meios de armazenamento.

Isso permite que um único processo acesse ext4, XFS, NFS, tmpfs e procfs por meio de um modelo compartilhado de caminhos e descritores de arquivos. Porém, não torna idênticos todos os recursos ou comportamentos: diferenciação entre maiúsculas e minúsculas, bloqueio, permissões, garantias de renomeação, atributos estendidos e tratamento de erros podem variar.

:::single-choice{#filesystem-types-vfs-role} Qual é a principal função do VFS do Linux?

::option[Converter em disco todos os sistemas de arquivos montados para ext4.]{#filesystem-types-vfs-convert-ext4 explanation="A abstração preserva as implementações e os formatos distintos dos sistemas de arquivos."}
::option[Fazer backup de cada arquivo antes de uma aplicação gravá-lo.]{#filesystem-types-vfs-backup explanation="O VFS encaminha operações e não fornece um histórico automático de backups."}
::option[Fornecer operações de arquivo comuns do kernel para várias implementações de sistemas de arquivos.]{#filesystem-types-vfs-common-interface .correct explanation="O VFS permite que as aplicações usem chamadas de sistema compartilhadas, enquanto cada sistema de arquivos implementa o comportamento subjacente."}
:::

## Journaling e Consistência após Falhas

Um sistema de arquivos com journaling registra atualizações selecionadas em um journal para poder repetir ou descartar transações incompletas após uma falha. O journaling serve principalmente para restaurar a consistência estrutural do sistema de arquivos mais rapidamente do que uma verificação completa.

Ele não garante que os dados mais recentes das aplicações tenham sobrevivido, que transações envolvendo vários arquivos sejam válidas nem que o hardware de armazenamento tenha respeitado todas as gravações concluídas. Os sistemas de arquivos oferecem diferentes modos de dados e garantias de ordenação, enquanto as aplicações devem usar padrões adequados de sincronização e atualização atômica. Um journal não é um backup e não protege contra exclusões, malware ou falhas do dispositivo.

:::single-choice{#filesystem-types-journal-scope} O que o journaling do sistema de arquivos ajuda principalmente a recuperar após uma falha?

::option[Metadados consistentes do sistema de arquivos e transações registradas.]{#filesystem-types-journal-consistency .correct explanation="A repetição do journal ajuda a devolver as estruturas do sistema de arquivos a um estado coerente."}
::option[Todas as versões históricas de todos os documentos dos usuários.]{#filesystem-types-journal-versions explanation="Um journal não é um armazenamento de backup com versões."}
::option[Dados de um dispositivo de armazenamento fisicamente destruído.]{#filesystem-types-journal-hardware-loss explanation="A recuperação após a perda de um dispositivo exige redundância ou backups fora do dispositivo com falha."}
:::

## Sistemas de Arquivos Locais Comuns

- **ext4** é um sistema de arquivos maduro com journaling e amplo suporte nas distribuições Linux e ferramentas de recuperação.
- **XFS** é um sistema de arquivos escalável com journaling, normalmente escolhido para sistemas de arquivos grandes e cargas de trabalho com E/S paralela.
- **Btrfs** é um sistema de arquivos copy-on-write com checksums, subvolumes, snapshots e recursos integrados para vários dispositivos.

Os recursos exigem contexto operacional. Um snapshot do Btrfs inicialmente compartilha o armazenamento com sua origem e não é um backup independente quando permanece no mesmo dispositivo sujeito a falhas. XFS e ext4 possuem capacidades diferentes de expansão, redução, reparo e ajuste. Confirme o suporte do kernel instalado, do ambiente de boot e das ferramentas de recuperação antes de escolher ou alterar um sistema de arquivos raiz.

:::single-choice{#filesystem-types-btrfs-snapshot} Por que um snapshot do Btrfs no mesmo dispositivo não é um backup completo?

::option[Snapshots sempre excluem o subvolume original imediatamente.]{#filesystem-types-snapshot-deletes explanation="Um snapshot cria outra visualização de subvolume e não remove sua origem por si só."}
::option[Ele compartilha o mesmo domínio de falha de armazenamento da origem.]{#filesystem-types-snapshot-failure-domain .correct explanation="A perda do dispositivo ou danos graves ao sistema de arquivos podem afetar tanto a origem quanto seu snapshot local."}
::option[O Btrfs não consegue representar mais de um arquivo.]{#filesystem-types-btrfs-one-file explanation="O Btrfs é um sistema de arquivos de uso geral para árvores de diretórios e muitos arquivos."}
:::

## Sistemas de Arquivos de Interoperabilidade, Rede e Virtuais

O Linux pode montar formatos de interoperabilidade como variantes FAT, exFAT e NTFS, mas suas semânticas de propriedade Unix, permissões, links e nomes de arquivos são diferentes. As opções de montagem e a implementação do driver determinam como o Linux apresenta os recursos ausentes.

Sistemas de arquivos de rede, como NFS e SMB, dependem de um servidor e de um protocolo de rede, com regras próprias de cache e identidade. Sistemas de arquivos virtuais, como tmpfs, procfs e sysfs, não usam um formato persistente comum em disco: o tmpfs armazena dados voláteis em páginas apoiadas por memória, enquanto procfs e sysfs expõem interfaces do kernel.

:::single-choice{#filesystem-types-procfs-category} Qual descrição corresponde melhor ao procfs?

::option[Um formato de intercâmbio do Windows para mídias removíveis.]{#filesystem-types-procfs-windows explanation="FAT ou exFAT correspondem melhor a esse uso; o procfs é voltado às interfaces do kernel Linux."}
::option[Um sistema de arquivos virtual que expõe interfaces de processos e do kernel.]{#filesystem-types-procfs-virtual .correct explanation="O procfs gera uma visualização ativa do kernel, em vez de armazenar arquivos persistentes comuns no disco."}
::option[Um sistema de arquivos de disco com journaling desenvolvido para volumes de bancos de dados.]{#filesystem-types-procfs-journal explanation="O procfs não possui um journal comum em disco nem a função de volume de dados."}
:::

## Descoberta dos Tipos Ativos

Mostre os tipos de sistemas de arquivos montados com:

```bash
$ findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Outras visualizações incluem `df -T` para contabilizar o espaço montado, `lsblk -f` para dispositivos de bloco e assinaturas de sistemas de arquivos detectadas e `/proc/filesystems` para os tipos reconhecidos ou suportados pelo kernel em execução. Elas respondem a perguntas diferentes; um sistema de arquivos desmontado não aparece em uma listagem comum de sistemas montados.

:::single-choice{#filesystem-types-findmnt-output} Qual comando lista diretamente os destinos montados com a origem, o tipo e as opções mostrados na lição?

::option[`findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS`]{#filesystem-types-findmnt .correct explanation="Findmnt lê a tabela de montagens e formata os campos solicitados dos sistemas de arquivos montados."}
::option[`lsblk -o NAME,SIZE,MODEL,SERIAL,ROTA`]{#filesystem-types-mkfs-destructive explanation="Esse comando lista detalhes de hardware dos dispositivos de bloco, não os tipos e opções efetivos dos sistemas de arquivos montados."}
::option[`cat /proc/filesystems | sort --unique`]{#filesystem-types-rm-proc explanation="Isso informa os tipos de sistemas de arquivos suportados pelo kernel, não as origens e opções efetivas das montagens."}
:::

Use o laboratório [Gerenciamento de Partições e Sistemas de Arquivos Linux](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) em um armazenamento descartável para comparar tipos, opções de montagem e visualizações de descoberta.

## Resumo

Agora você sabe comparar categorias de sistemas de arquivos sem presumir semânticas idênticas.

1. Relacione o VFS às operações comuns entre diferentes implementações.
2. Trate o journaling como suporte à consistência após falhas, não como backup.
3. Compare ext4, XFS e Btrfs pelas operações compatíveis e pela carga de trabalho.
4. Diferencie sistemas de arquivos de disco local, rede, interoperabilidade e virtuais.
5. Use ferramentas de montagem e dispositivos de bloco para responder a diferentes perguntas de inventário.
