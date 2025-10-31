---
index: 6
lang: "pt"
title: "montar e desmontar"
meta_title: "montar e desmontar - O Sistema de Arquivos"
meta_description: "Aprenda a usar os comandos mount e umount no Linux para anexar e desanexar sistemas de arquivos. Este guia abrange montagem de dispositivos, o processo sudo umount para um desmonte seguro no Linux e o uso de UUIDs."
meta_keywords: "montar, desmontar, sudo desmontar, desmontar linux, desmonte linux, desmontar debian, montar sistema de arquivos, desmontar dispositivo, UUID Linux, ponto de montagem"
---

## Lesson Content

Antes de poder acessar os arquivos em um dispositivo de armazenamento, você deve primeiro montar seu sistema de arquivos em um diretório no seu sistema. Este processo envolve a localização do dispositivo, um tipo de sistema de arquivos e um ponto de montagem. O ponto de montagem é simplesmente um diretório existente onde o sistema de arquivos será anexado.

### Como Montar um Sistema de Arquivos

Primeiro, você precisa criar um ponto de montagem. Vamos criar um diretório para este propósito:

```bash
sudo mkdir /mydrive
```

Com o ponto de montagem pronto, você pode usar o comando `mount` para anexar seu dispositivo. A flag `-t` especifica o tipo de sistema de arquivos.

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

É simples assim! Agora, se você navegar até o diretório `/mydrive`, verá o conteúdo do sistema de arquivos do seu dispositivo.

### Como Desmontar um Sistema de Arquivos no Linux

Quando terminar com um dispositivo, você deve desmontá-lo para garantir que todos os dados sejam gravados com segurança e que o sistema de arquivos seja desconectado de forma limpa. O comando padrão para esta operação no Linux é `umount`. Para realizar um `linux unmount`, você pode especificar o ponto de montagem ou o nome do dispositivo.

Usando o ponto de montagem:

```bash
sudo umount /mydrive
```

Alternativamente, usando o nome do dispositivo:

```bash
sudo umount /dev/sdb2
```

É uma boa prática usar `sudo umount` para garantir que você tenha as permissões necessárias para desconectar o sistema de arquivos. Este comando é universal em todas as distribuições Linux, então a mesma sintaxe se aplica se você estiver no Ubuntu, Fedora ou realizando um `debian umount`. Observe que você não pode `umount` um dispositivo se ele estiver atualmente em uso (por exemplo, se um arquivo estiver aberto ou seu diretório de trabalho atual estiver no dispositivo).

### Usando UUIDs para Montagem Estável

O kernel nomeia os dispositivos na ordem em que os descobre, o que significa que um nome de dispositivo como `/dev/sdb2` pode mudar entre reinicializações. Para evitar problemas, você pode usar o ID universalmente exclusivo (UUID) de um dispositivo, que permanece constante.

Para visualizar os UUIDs dos seus dispositivos de bloco, use o comando `blkid`:

```bash
pete@icebox:~$ sudo blkid
/dev/sda1: UUID="130b882f-7d79-436d-a096-1e594c92bb76" TYPE="ext4"
/dev/sda5: UUID="22c3d34b-467e-467c-b44d-f03803c2c526" TYPE="swap"
/dev/sda6: UUID="78d203a0-7c18-49bd-9e07-54f44cdb5726" TYPE="xfs"
```

Esta saída mostra os nomes dos dispositivos, seus tipos de sistema de arquivos e seus UUIDs correspondentes. Você pode então montar um dispositivo usando seu UUID:

```bash
sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mydrive
```

Embora você nem sempre precise montar dispositivos por meio de seus UUIDs, este é o método recomendado para montar sistemas de arquivos automaticamente na inicialização, como um disco rígido secundário. Abordaremos esse processo na próxima lição.

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão do gerenciamento de sistemas de arquivos Linux:

- **[Gerenciar Partições e Sistemas de Arquivos Linux](https://labex.io/pt/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Neste laboratório, você aprenderá a gerenciar partições de disco e sistemas de arquivos no Linux. Você usará o fdisk para criar uma nova partição, formatá-la com ext4, montá-la, configurar a montagem persistente em /etc/fstab e criar uma partição swap, tudo em um disco virtual secundário seguro.

Este laboratório o ajudará a aplicar os conceitos de montagem e desmontagem em cenários reais e a ganhar confiança no gerenciamento de sistemas de arquivos.

## Quiz Question

Qual comando é usado para anexar um sistema de arquivos? (Por favor, use uma única palavra em inglês minúscula para sua resposta.)

## Quiz Answer

mount
