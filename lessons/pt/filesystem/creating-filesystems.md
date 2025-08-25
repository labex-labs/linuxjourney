---
index: 5
lang: "pt"
title: "Criando Sistemas de Arquivos"
meta_title: "Criando Sistemas de Arquivos - O Sistema de Arquivos"
meta_description: "Aprenda a criar sistemas de arquivos no Linux usando mkfs. Este guia para iniciantes cobre ext4 e particionamento de disco. Comece sua jornada no Linux!"
meta_keywords: "mkfs, criar sistema de arquivos, ext4, particionamento Linux, tutorial Linux, Linux para iniciantes, gerenciamento de disco, guia Linux"
---

## Lesson Content

Agora que você realmente particionou um disco, vamos criar um sistema de arquivos!

```bash
sudo mkfs -t ext4 /dev/sdb2
```

Simples assim! A ferramenta **mkfs** (make filesystem) nos permite especificar o tipo de sistema de arquivos que queremos e onde o queremos. Você só vai querer criar um sistema de arquivos em um disco recém-particionado ou se estiver reparticionando um antigo. Você provavelmente deixará seu sistema de arquivos em um estado corrompido se tentar criar um em cima de um existente.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre o gerenciamento de sistemas de arquivos Linux:

1. **[Gerenciar Partições e Sistemas de Arquivos Linux](https://labex.io/pt/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Neste laboratório, você aprenderá a gerenciar partições de disco e sistemas de arquivos no Linux. Você usará fdisk para criar uma nova partição, formatá-la com ext4 (usando `mkfs`), montá-la, configurar a montagem persistente em /etc/fstab e criar uma partição swap, tudo em um disco virtual secundário seguro.

Este laboratório o ajudará a aplicar os conceitos de criação e gerenciamento de sistemas de arquivos em cenários reais e a construir confiança com o gerenciamento de disco no Linux.

## Quiz Question

Qual comando é usado para criar um sistema de arquivos?

## Quiz Answer

mkfs
