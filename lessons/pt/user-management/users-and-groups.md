---
index: 1
lang: "pt"
title: "Usuários e Grupos"
meta_title: "Usuários e Grupos - Gerenciamento de Usuários"
meta_description: "Uma parte fundamental dos conceitos básicos do Linux é entender o gerenciamento de usuários e grupos. Este guia aborda usuários e grupos do Linux, o superusuário root e o uso do comando sudo para privilégios elevados. Uma das melhores lições de tutorial de Linux para iniciantes."
meta_keywords: "usuários e grupos linux, conceitos básicos de linux, sudo, usuário root, UID, GID, gerenciamento de usuários, melhor tutorial linux, caminho mais rápido para linux avançado"
---

## Lesson Content

Em qualquer sistema operacional multiusuário, gerenciar usuários e grupos é um conceito fundamental. Esta é uma parte central dos **basics of linux**, projetada para controle de acesso e permissões. Quando um processo é executado, ele o faz como o usuário que o iniciou. Da mesma forma, o acesso a arquivos e a propriedade dependem de permissões, impedindo que um usuário acesse os documentos privados de outro.

### The Basics of Linux Users and Groups

Cada usuário em um sistema Linux recebe um diretório pessoal (home directory), geralmente localizado em `/home/username`. Este diretório é onde seus arquivos e configurações específicos do usuário são armazenados, embora o caminho exato possa variar entre as distribuições Linux.

O sistema identifica usuários com um ID de Usuário (UID) e grupos com um ID de Grupo (GID). Embora usemos nomes de usuário legíveis por humanos, o sistema operacional depende desses IDs numéricos exclusivos para todas as tarefas relacionadas a permissões. Grupos são simplesmente coleções de usuários, facilitando o gerenciamento de permissões para várias contas de uma só vez.

### The Superuser and the Sudo Command

Dentro da hierarquia de **linux users and groups**, um usuário se destaca acima de todos os outros: `root`, também conhecido como superusuário. O usuário `root` tem poder ilimitado, capaz de acessar qualquer arquivo e gerenciar qualquer processo. Operar como `root` continuamente é arriscado, pois um erro simples pode danificar o sistema.

Para mitigar esse risco, usuários autorizados podem executar comandos com privilégios de root usando o comando `sudo` (superuser do). Isso permite tarefas administrativas sem fazer login como o usuário `root`. Entender como usar `sudo` corretamente é essencial para quem busca as habilidades administrativas `quickest way to linux advanced`.

Vamos tentar visualizar um arquivo protegido, como `/etc/shadow`, que armazena senhas de usuário criptografadas.

```bash
cat /etc/shadow
```

Você receberá um erro de "Permission denied". Vamos examinar as permissões do arquivo:

```bash
$ ls -la /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

Embora abordemos as permissões em detalhes mais tarde, esta saída mostra que apenas o usuário `root` e os membros do grupo `shadow` podem ler este arquivo. Agora, execute o comando novamente com `sudo`:

```bash
sudo cat /etc/shadow
```

Desta vez, será solicitada sua senha e, após a autenticação bem-sucedida, o conteúdo do arquivo será exibido.

## Exercise

Embora existam muitos aplicativos para aprender linux, a prática prática é essencial. Aqui estão alguns laboratórios para reforçar sua compreensão de usuários, grupos e `sudo` no Linux:

1. **[Manage Linux User Accounts with useradd, usermod, and userdel](https://labex.io/pt/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratique o ciclo de vida completo da administração de usuários, desde a criação e proteção de novas contas até a modificação e exclusão delas.
2. **[Manage Linux Groups with groupadd, usermod, and groupdel](https://labex.io/pt/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Ganhe experiência prática com utilitários de linha de comando essenciais para administração de grupos, incluindo a criação de novos grupos, modificação de associações de usuários e remoção de grupos.
3. **[Configure User Accounts and Sudo Privileges in Linux](https://labex.io/pt/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprenda técnicas essenciais para gerenciar contas de usuário e privilégios de `sudo` para aumentar a segurança de um sistema Linux, incluindo a concessão de permissões administrativas.

Esses laboratórios ajudarão você a aplicar os conceitos de gerenciamento de usuários e grupos, e o uso de `sudo`, em cenários reais e a construir confiança com a administração de sistemas Linux.

## Quiz Question

What command allows you to run a single command with `root` privileges? (Please answer in English, using only lowercase letters)

## Quiz Answer

sudo
