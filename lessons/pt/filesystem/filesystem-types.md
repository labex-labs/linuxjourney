---
index: 2
lang: "pt"
title: "Tipos de Sistema de Arquivos"
meta_title: "Tipos de Sistema de Arquivos - O Sistema de Arquivos"
meta_description: "Aprenda sobre os tipos de sistema de arquivos Linux como ext4, Btrfs e XFS. Entenda o journaling e o VFS para dados consistentes. Explore os sistemas de arquivos Linux comuns neste guia para iniciantes."
meta_keywords: "tipos de sistema de arquivos Linux, ext4, Btrfs, XFS, journaling, VFS, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Existem muitas implementações de sistema de arquivos diferentes disponíveis. Algumas são mais rápidas que outras, algumas suportam armazenamento de maior capacidade e outras funcionam apenas em armazenamento de menor capacidade. Diferentes sistemas de arquivos têm diferentes maneiras de organizar seus dados, e entraremos em detalhes sobre quais tipos de sistemas de arquivos existem. Como há tantas implementações diferentes disponíveis, os aplicativos precisam de uma maneira de lidar com as diferentes operações. Então, existe algo chamado camada de abstração Virtual File System (VFS). É uma camada entre os aplicativos e os diferentes tipos de sistema de arquivos, então, não importa qual sistema de arquivos você tenha, seus aplicativos poderão trabalhar com ele.

Você pode ter muitos sistemas de arquivos em seus discos, dependendo de como eles são particionados, e abordaremos isso em uma próxima lição.

### Journaling

O journaling vem por padrão na maioria dos tipos de sistema de arquivos, mas caso não venha, você deve saber o que ele faz. Digamos que você esteja copiando um arquivo grande e, de repente, perca a energia. Bem, se você estiver em um sistema de arquivos sem journaling, o arquivo acabaria corrompido e seu sistema de arquivos ficaria inconsistente. Então, quando você inicializasse novamente, seu sistema executaria uma verificação do sistema de arquivos para garantir que tudo estivesse bem. No entanto, os reparos poderiam levar um tempo, dependendo do tamanho do seu sistema de arquivos.

Agora, se você estivesse em um sistema com journaling, antes mesmo de sua máquina começar a copiar o arquivo, ela escreveria o que você vai fazer em um arquivo de log (journal). Quando você realmente copia o arquivo, assim que ele é concluído, o journal marca essa tarefa como concluída. O sistema de arquivos está sempre em um estado consistente por causa disso, então ele saberá exatamente onde você parou se sua máquina desligar repentinamente. Isso também diminui o tempo de inicialização porque, em vez de verificar todo o sistema de arquivos, ele apenas olha para o seu journal.

### Tipos Comuns de Sistema de Arquivos para Desktop

- ext4 - Esta é a versão mais atual dos sistemas de arquivos nativos do Linux. É compatível com as versões mais antigas ext2 e ext3. Suporta volumes de disco de até 1 exabyte e tamanhos de arquivo de até 16 terabytes e muito mais. É a escolha padrão para sistemas de arquivos Linux.
- Btrfs - "Better or Butter FS" é um novo sistema de arquivos para Linux que vem com snapshots, backups incrementais, aumento de desempenho e muito mais. Está amplamente disponível, mas ainda não é totalmente estável e compatível.
- XFS - Sistema de arquivos com journaling de alto desempenho, ótimo para um sistema com arquivos grandes, como um servidor de mídia.
- NTFS e FAT - Sistemas de arquivos Windows
- HFS+ - Sistema de arquivos Macintosh

Verifique quais sistemas de arquivos estão em sua máquina:

```plaintext
pete@icebox:~$ df -T
Filesystem     Type     1K-blocks    Used Available Use% Mounted on
/dev/sda1      ext4       6461592 2402708   3707604  40% /
udev           devtmpfs    501356       4    501352   1% /dev
tmpfs          tmpfs       102544    1068    101476  2% /run
/dev/sda6      xfs       13752320  460112  13292208   4% /home
```

O comando **df** relata o uso do espaço em disco do sistema de arquivos e outros detalhes sobre seu disco; falaremos mais sobre essa ferramenta mais tarde.

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão dos sistemas de arquivos e partições Linux:

1. **[Gerenciar Partições e Sistemas de Arquivos Linux](https://labex.io/pt/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Pratique a criação de uma nova partição, formatando-a, montando-a e configurando a montagem persistente, todas as habilidades fundamentais relacionadas ao gerenciamento de diferentes implementações de sistema de arquivos.

Este laboratório o ajudará a aplicar os conceitos em cenários reais e a construir confiança no gerenciamento de armazenamento em disco no Linux.

## Quiz Question

Qual é o tipo comum de sistema de arquivos Linux?

## Quiz Answer

ext4
