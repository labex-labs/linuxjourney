---
index: 5
lang: "pt"
title: "Setuid"
meta_title: "Setuid - Permissões"
meta_description: "Aprenda sobre as permissões Setuid (SUID) do Linux, como elas funcionam e como modificá-las. Entenda o SUID para acesso seguro a arquivos no Linux."
meta_keywords: "Linux Setuid, SUID, permissões Linux, chmod, comando passwd, segurança Linux, Linux para iniciantes, tutorial Linux"
---

## Lesson Content

Existem muitos casos em que usuários normais precisam de acesso elevado para realizar tarefas. O administrador do sistema nem sempre pode estar presente para digitar uma senha de root toda vez que um usuário precisa de acesso a um arquivo protegido, então existem bits de permissão de arquivo especiais para permitir esse comportamento. O Set User ID (SUID) permite que um usuário execute um programa como o proprietário do arquivo do programa, em vez de como ele mesmo.

Vamos ver um exemplo:

Digamos que eu queira mudar minha senha, simples, certo? Eu apenas uso o comando `passwd`:

```bash
passwd
```

O que o comando `passwd` está fazendo? Ele está modificando alguns arquivos, mas o mais importante é que ele está modificando o arquivo `/etc/shadow`. Vamos dar uma olhada nesse arquivo por um segundo:

```bash
$ ls -l /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

Ah, espere um minuto, este arquivo pertence ao root? Como é possível que possamos modificar um arquivo que pertence ao root?

Vamos olhar para outro conjunto de permissões, desta vez do comando que executamos:

```bash
$ ls -l /usr/bin/passwd

-rwsr-xr-x 1 root root 47032 Dec 1 11:45 /usr/bin/passwd
```

Você notará um novo bit de permissão aqui **s**. Este bit de permissão é o SUID. Quando um arquivo tem essa permissão definida, ele permite que os usuários que iniciaram o programa obtenham a permissão do proprietário do arquivo, bem como a permissão de execução, neste caso, root. Então, essencialmente, enquanto um usuário está executando o comando `passwd`, ele está executando como root.

É por isso que somos capazes de acessar um arquivo protegido como `/etc/shadow` quando executamos o comando `passwd`. Agora, se você remover esse bit, verá que não poderá modificar `/etc/shadow` e, portanto, não poderá alterar sua senha.

### Modificando SUID

Assim como as permissões regulares, existem duas maneiras de modificar as permissões SUID.

_Forma simbólica:_

```bash
sudo chmod u+s myfile
```

_Forma numérica:_

```bash
sudo chmod 4755 myfile
```

Como você pode ver, o SUID é denotado por um 4 e é prefixado ao conjunto de permissões. Você pode ver o SUID denotado como um **S** maiúsculo. Isso significa que ele ainda faz a mesma coisa, mas não tem permissões de execução.

## Exercise

Prática leva à perfeição! Entender como funcionam as permissões de arquivo, grupos de usuários e bits especiais como o SUID é crucial para gerenciar e proteger sistemas Linux. A experiência prática solidificará seu conhecimento.

Aqui está um laboratório prático para reforçar sua compreensão das permissões de arquivo e gerenciamento de usuários:

1. **[Grupo de Usuários Linux e Permissões de Arquivo](https://labex.io/pt/labs/linux-linux-user-group-and-file-permissions-18002)** - Pratique a criação e o gerenciamento de usuários e grupos, a compreensão das permissões de arquivo e a manipulação da propriedade de arquivos. Este laboratório fornece o conhecimento fundamental necessário para entender como o SUID aproveita esses conceitos para acesso elevado.

Este laboratório o ajudará a aplicar os conceitos em um cenário real e a construir confiança com o gerenciamento de usuários e arquivos do Linux.

## Quiz Question

Qual número representa o SUID?

## Quiz Answer

4
