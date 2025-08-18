---
lang: "pt"
title: "/etc/fstab"
meta_description: "Aprenda sobre /etc/fstab no Linux, como configurar montagens de sistema de arquivos na inicialização e gerenciar entradas de dispositivos. Entenda o fstab para iniciantes!"
meta_keywords: "/etc/fstab, Linux fstab, montar sistemas de arquivos, inicialização Linux, tutorial fstab, iniciante, guia"
---

## Lesson Content

Quando queremos montar automaticamente sistemas de arquivos na inicialização, podemos adicioná-los a um arquivo chamado `/etc/fstab` (pronuncia-se "éfe és táb", não "éfe stáb"), abreviação de tabela de sistema de arquivos. Este arquivo contém uma lista permanente de sistemas de arquivos que são montados.

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

Cada linha representa um sistema de arquivos; os campos são:

- UUID - Identificador do dispositivo
- Mount point - Diretório onde o sistema de arquivos é montado
- Filesystem type
- Options - Outras opções de montagem; veja a página man para mais detalhes
- Dump - Usado pelo utilitário dump para decidir quando fazer um backup; você deve apenas usar o valor padrão 0
- Pass - Usado pelo fsck para decidir a ordem em que os sistemas de arquivos devem ser verificados; se o valor for 0, ele não será verificado

Para adicionar uma entrada, basta modificar diretamente o arquivo `/etc/fstab` usando a sintaxe de entrada acima. Tenha cuidado ao modificar este arquivo; você pode potencialmente dificultar um pouco sua vida se cometer erros.

## Exercise

Adicione o pendrive em que estamos trabalhando como uma entrada em `/etc/fstab`. Ao reiniciar, você ainda deverá vê-lo montado.

## Quiz Question

Qual arquivo é usado para definir como os sistemas de arquivos devem ser montados?

## Quiz Answer

/etc/fstab
