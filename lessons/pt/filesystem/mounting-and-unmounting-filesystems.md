---
index: 6
lang: "pt"
title: "mount e umount"
meta_title: "mount e umount - O Sistema de Arquivos"
meta_description: "Aprenda a usar os comandos mount e umount do Linux para gerenciar sistemas de arquivos. Entenda a montagem, desmontagem de dispositivos e UUIDs para iniciantes."
meta_keywords: "Linux mount, comando umount, montar sistema de arquivos, Linux UUID, Linux para iniciantes, tutorial Linux, ponto de montagem, guia Linux"
---

## Lesson Content

Antes de poder visualizar o conteúdo do seu sistema de arquivos, você terá que montá-lo. Para fazer isso, precisarei do local do dispositivo, do tipo de sistema de arquivos e de um ponto de montagem. O ponto de montagem é um diretório no sistema onde o sistema de arquivos será anexado. Então, basicamente, queremos montar nosso dispositivo em um ponto de montagem.

Primeiro, crie o ponto de montagem; em nosso caso, **mkdir /mydrive**.

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

Simples assim! Agora, quando vamos para /mydrive, podemos ver o conteúdo do nosso sistema de arquivos. O **-t** especifica o tipo de sistema de arquivos, depois temos o local do dispositivo e, em seguida, o ponto de montagem.

Para desmontar um dispositivo de um ponto de montagem:

```bash
sudo umount /mydrive
```

ou

```bash
sudo umount /dev/sdb2
```

Lembre-se de que o kernel nomeia os dispositivos na ordem em que os encontra. E se o nome do nosso dispositivo mudar por algum motivo depois de montá-lo? Bem, felizmente, você pode usar o ID universalmente exclusivo (UUID) de um dispositivo em vez de um nome.

Para visualizar os UUIDs em seu sistema para dispositivos de bloco:

```bash
pete@icebox:~$ sudo blkid
/dev/sda1: UUID="130b882f-7d79-436d-a096-1e594c92bb76" TYPE="ext4"
/dev/sda5: UUID="22c3d34b-467e-467c-b44d-f03803c2c526" TYPE="swap"
/dev/sda6: UUID="78d203a0-7c18-49bd-9e07-54f44cdb5726" TYPE="xfs"
```

Podemos ver os nomes dos nossos dispositivos, seus tipos de sistema de arquivos correspondentes e seus UUIDs. Agora, quando queremos montar algo, podemos usar:

```bash
sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mydrive
```

Na maioria das vezes, você não precisará montar dispositivos via seus UUIDs; é muito mais fácil usar o nome do dispositivo, e muitas vezes o sistema operacional saberá montar dispositivos comuns como unidades USB. No entanto, se você precisar montar automaticamente um sistema de arquivos na inicialização, como se você adicionou um disco rígido secundário, você vai querer usar o UUID, e abordaremos isso na próxima lição.

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão sobre o gerenciamento de sistemas de arquivos Linux:

- **[Gerenciar Partições e Sistemas de Arquivos Linux](https://labex.io/pt/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Neste laboratório, você aprenderá a gerenciar partições de disco e sistemas de arquivos no Linux. Você usará o fdisk para criar uma nova partição, formatá-la com ext4, montá-la, configurar a montagem persistente em /etc/fstab e criar uma partição swap, tudo em um disco virtual secundário seguro.

Este laboratório o ajudará a aplicar os conceitos de montagem e desmontagem em cenários reais e a construir confiança com o gerenciamento de sistemas de arquivos.

## Quiz Question

Qual comando é usado para anexar um sistema de arquivos?

## Quiz Answer

mount
