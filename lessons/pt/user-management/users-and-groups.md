---
lang: "pt"
title: "Usuários e Grupos"
description: "Aprenda sobre usuários e grupos Linux, entenda UIDs, GIDs e o usuário root. Descubra como usar o comando sudo para permissões elevadas. Comece sua jornada no Linux!"
keywords: "usuários Linux, grupos Linux, comando sudo, usuário root, permissões Linux, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Em qualquer sistema operacional tradicional, existem usuários e grupos. Eles existem unicamente para acesso e permissões. Ao executar um processo, ele será executado como o proprietário desse processo, seja Jane ou Bob. O acesso e a propriedade de arquivos também dependem de permissões. Você não gostaria que Jane visse os documentos de Bob e vice-versa.

Cada usuário tem seu próprio diretório home onde seus arquivos específicos de usuário são armazenados. Isso geralmente está localizado em `/home/username`, mas pode variar em diferentes distribuições.

O sistema usa IDs de usuário (UID) para gerenciar usuários. Nomes de usuário são a maneira amigável de associar usuários à identificação, mas o sistema identifica os usuários por seu UID. O sistema também usa grupos para gerenciar permissões. Grupos são apenas conjuntos de usuários com permissões definidas por esse grupo; eles são identificados pelo sistema com seu ID de grupo (GID).

No Linux, você terá usuários além dos humanos normais que usam o sistema. Às vezes, esses usuários são daemons do sistema que executam processos continuamente para manter o sistema funcionando. Um dos usuários mais importantes é `root` ou `superuser`. `root` é o usuário mais poderoso do sistema; `root` pode acessar qualquer arquivo e iniciar e encerrar qualquer processo. Por essa razão, pode ser perigoso operar como `root` o tempo todo; você poderia potencialmente remover arquivos críticos do sistema. Felizmente, se o acesso `root` for necessário e um usuário tiver acesso `root`, ele pode executar um comando como `root` com o comando `sudo`. O comando `sudo` (superuser do) é usado para executar um comando com acesso `root`. Abordaremos mais a fundo como um usuário recebe acesso `root` em uma lição posterior.

Prossiga e tente visualizar um arquivo protegido como `/etc/shadow`:

```bash
cat /etc/shadow
```

Observe como você recebe um erro de permissão negada. Veja as permissões com:

```bash
$ ls -la /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

Ainda não passamos pelas permissões, mas o que está acontecendo aqui é que `root` é o proprietário do arquivo, e você precisará de acesso `root` ou fazer parte do grupo `shadow` para ler o conteúdo. Agora execute o comando com `sudo`:

```bash
sudo cat /etc/shadow
```

Agora você poderá ver o conteúdo do arquivo!

## Exercise

No exercises for this lesson.

## Quiz Question

Qual comando você usa para executar como `root`?

## Quiz Answer

sudo
