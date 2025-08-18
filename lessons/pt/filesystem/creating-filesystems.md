---
index: 5
lang: "pt"
title: "Criando Sistemas de Arquivos"
meta_title: "Criando Sistemas de Arquivos - O Filesystem"
meta_description: "Aprenda a criar sistemas de arquivos no Linux usando mkfs. Este guia para iniciantes abrange ext4 e particionamento de disco. Comece sua jornada no Linux!"
meta_keywords: "mkfs, criar sistema de arquivos, ext4, particionamento Linux, tutorial Linux, Linux para iniciantes, gerenciamento de disco, guia Linux"
---

## Lesson Content

Agora que você realmente particionou um disco, vamos criar um sistema de arquivos!

```bash
sudo mkfs -t ext4 /dev/sdb2
```

Simples assim! A ferramenta **mkfs** (make filesystem) nos permite especificar o tipo de sistema de arquivos que queremos e onde o queremos. Você só vai querer criar um sistema de arquivos em um disco recém-particionado ou se estiver reparticionando um antigo. Você provavelmente deixará seu sistema de arquivos em um estado corrompido se tentar criar um em cima de um existente.

## Exercise

Crie um sistema de arquivos ext4 na unidade USB.

## Quiz Question

Qual comando é usado para criar um sistema de arquivos?

## Quiz Answer

mkfs
