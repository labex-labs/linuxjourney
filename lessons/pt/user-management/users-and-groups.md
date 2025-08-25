---
index: 1
lang: "pt"
title: "Usuários e Grupos"
meta_title: "Usuários e Grupos - Gerenciamento de Usuários"
meta_description: "Aprenda sobre usuários e grupos Linux, entenda UIDs, GIDs e o usuário root. Descubra como usar o comando sudo para permissões elevadas. Comece sua jornada Linux!"
meta_keywords: "usuários Linux, grupos Linux, comando sudo, usuário root, permissões Linux, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Em qualquer sistema operacional tradicional, existem usuários e grupos. Eles existem unicamente para acesso e permissões. Ao executar um processo, ele será executado como o proprietário desse processo, seja Jane ou Bob. O acesso a arquivos e a propriedade também dependem de permissões. Você não gostaria que Jane visse os documentos de Bob e vice-versa.

Cada usuário tem seu próprio diretório pessoal onde seus arquivos específicos de usuário são armazenados. Isso geralmente está localizado em `/home/username`, mas pode variar em diferentes distribuições.

O sistema usa IDs de usuário (UID) para gerenciar usuários. Nomes de usuário são a maneira amigável de associar usuários à identificação, mas o sistema identifica os usuários por seu UID. O sistema também usa grupos para gerenciar permissões. Grupos são apenas conjuntos de usuários com permissões definidas por esse grupo; eles são identificados pelo sistema com seu ID de grupo (GID).

No Linux, você terá usuários além dos humanos normais que usam o sistema. Às vezes, esses usuários são daemons do sistema que executam processos continuamente para manter o sistema funcionando. Um dos usuários mais importantes é o `root` ou `superuser`. O `root` é o usuário mais poderoso do sistema; o `root` pode acessar qualquer arquivo e iniciar e terminar qualquer processo. Por essa razão, pode ser perigoso operar como `root` o tempo todo; você poderia potencialmente remover arquivos críticos do sistema. Felizmente, se o acesso `root` for necessário e um usuário tiver acesso `root`, ele pode executar um comando como `root` em vez disso com o comando `sudo`. O comando `sudo` (superuser do) é usado para executar um comando com acesso `root`. Abordaremos mais a fundo como um usuário recebe acesso `root` em uma lição posterior.

Vá em frente e tente visualizar um arquivo protegido como `/etc/shadow`:

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

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre usuários, grupos e `sudo` no Linux:

1. **[Gerenciar Contas de Usuário Linux com useradd, usermod e userdel](https://labex.io/pt/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratique o ciclo de vida completo da administração de usuários, desde a criação e segurança de novas contas até a modificação e exclusão delas.
2. **[Gerenciar Grupos Linux com groupadd, usermod e groupdel](https://labex.io/pt/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Ganhe experiência prática com utilitários de linha de comando essenciais para a administração de grupos, incluindo a criação de novos grupos, a modificação de associações de usuários e a remoção de grupos.
3. **[Configurar Contas de Usuário e Privilégios Sudo no Linux](https://labex.io/pt/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprenda técnicas essenciais para gerenciar contas de usuário e privilégios `sudo` para aumentar a segurança de um sistema Linux, incluindo a concessão de permissões administrativas.

Esses laboratórios o ajudarão a aplicar os conceitos de gerenciamento de usuários e grupos, e o uso de `sudo`, em cenários reais e a construir confiança com a administração de sistemas Linux.

## Quiz Question

Qual comando você usa para executar como `root`?

## Quiz Answer

sudo
