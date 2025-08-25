---
index: 3
lang: "pt"
title: "Anatomia de um Disco"
meta_title: "Anatomia de um Disco - O Sistema de Arquivos"
meta_description: "Aprenda sobre particionamento de disco Linux, MBR vs. GPT e estrutura do sistema de arquivos. Entenda partições, tabelas e como organizar dados. Comece com este guia para iniciantes!"
meta_keywords: "particionamento de disco Linux, MBR, GPT, estrutura do sistema de arquivos, partições Linux, iniciante, tutorial, guia"
---

## Lesson Content

Discos rígidos podem ser subdivididos em partições, essencialmente criando múltiplos dispositivos de bloco. Lembre-se de exemplos como `/dev/sda1` e `/dev/sda2`. `/dev/sda` é o disco inteiro, mas `/dev/sda1` é a primeira partição nesse disco. As partições são extremamente úteis para separar dados, e se você precisar de um determinado sistema de arquivos, pode facilmente criar uma partição em vez de fazer do disco inteiro um único tipo de sistema de arquivos.

### Tabela de Partições

Todo disco terá uma tabela de partições. Esta tabela informa ao sistema como o disco está particionado. Esta tabela informa onde as partições começam e terminam, quais partições são inicializáveis, quais setores do disco são alocados para qual partição, etc. Existem dois esquemas principais de tabela de partições usados: Master Boot Record (MBR) e GUID Partition Table (GPT).

### Partição

Os discos são compostos por partições que nos ajudam a organizar nossos dados. Você pode ter várias partições em um disco, e elas não podem se sobrepor. Se houver espaço que não esteja alocado a uma partição, ele é conhecido como espaço livre. Os tipos de partições dependem da sua tabela de partições. Dentro de uma partição, você pode ter um sistema de arquivos ou dedicar uma partição a outras coisas, como swap (chegaremos a isso em breve).

_MBR_

- Tabela de partições tradicional, era usada como padrão
- Pode ter partições primárias, estendidas e lógicas
- MBR tem um limite de quatro partições primárias
- Partições adicionais podem ser criadas transformando uma partição primária em uma partição estendida (pode haver apenas uma partição estendida em um disco). Então, dentro da partição estendida, você adiciona partições lógicas. As partições lógicas são usadas como qualquer outra partição. Bobo, eu sei.
- Suporta discos de até 2 terabytes

_GPT_

- GUID Partition Table (GPT) está se tornando o novo padrão para particionamento de disco
- Tem apenas um tipo de partição, e você pode fazer muitas delas
- Cada partição tem um ID globalmente único (GUID)
- Usado principalmente em conjunto com a inicialização baseada em UEFI (entraremos em detalhes em outro curso)

### Estrutura do Sistema de Arquivos

Sabemos da nossa lição anterior que um sistema de arquivos é uma coleção organizada de arquivos e diretórios. Em sua forma mais simples, é composto por um banco de dados para gerenciar arquivos e os próprios arquivos; no entanto, vamos entrar em um pouco mais de detalhes.

- Bloco de inicialização - Este está localizado nos primeiros setores do sistema de arquivos, e não é realmente usado pelo sistema de arquivos. Em vez disso, ele contém informações usadas para inicializar o sistema operacional. Apenas um bloco de inicialização é necessário pelo sistema operacional. Se você tiver várias partições, elas terão blocos de inicialização, mas muitos deles não são usados.
- Superbloco - Este é um único bloco que vem depois do bloco de inicialização, e contém informações sobre o sistema de arquivos, como o tamanho da tabela de inodes, o tamanho dos blocos lógicos e o tamanho do sistema de arquivos.
- Tabela de Inodes - Pense nisso como o banco de dados que gerencia nossos arquivos (temos uma lição inteira sobre inodes, então não se preocupe). Cada arquivo ou diretório tem uma entrada única na tabela de inodes, e ela possui várias informações sobre o arquivo.
- Blocos de dados - Estes são os dados reais para os arquivos e diretórios.

Vamos dar uma olhada nas diferentes tabelas de partições. Abaixo está um exemplo de uma partição usando a tabela de particionamento MBR (msdos). Você pode ver as partições primárias, estendidas e lógicas na máquina.

```plaintext
pete@icebox:~$ sudo parted -l
Model: Seagate (scsi)
Disk /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos

Number  Start   End     Size    Type      File system     Flags
 1      1049kB  6860MB  6859MB  primary   ext4            boot
 2      6861MB  21.5GB  14.6GB  extended
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
 6      7381MB  21.5GB  14.1GB  logical   xfs
```

Este exemplo é GPT, usando apenas um ID único para as partições.

```plaintext
Model: Thumb Drive (scsi)
Disk /dev/sdb: 4041MB
Sector size (logical/physical): 512B/512B
Partition Table: gpt

Number  Start   End     Size     File system  Name        Flags
 1      17.4kB  1000MB  1000MB                first
 2      1000MB  4040MB  3040MB                second
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre particionamento de disco e sistemas de arquivos:

1. **[Gerenciar Partições e Sistemas de Arquivos Linux](https://labex.io/pt/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Pratique a criação de novas partições, formatando-as com sistemas de arquivos como ext4, montando-as e configurando a montagem persistente em `/etc/fstab`.

Este laboratório o ajudará a aplicar os conceitos de gerenciamento de disco em cenários reais e a construir confiança com o armazenamento Linux.

## Quiz Question

Qual tipo de partição é usado para criar mais de 4 partições no esquema de particionamento MBR?

## Quiz Answer

extended
