---
index: 2
lang: "pt"
title: "Raiz"
meta_title: "Raiz - Gerenciamento de Usuários"
meta_description: "Explore a função do usuário root no Linux. Esta lição aborda as diferenças entre su e sudo para obter privilégios de superusuário e explica como o arquivo /etc/sudoers gerencia o acesso."
meta_keywords: "usuário root no linux, usuário root linux, su, sudo, sudoers, visudo, superusuário, gerenciamento de usuários, permissões linux"
---

## Lesson Content

No Linux, certas tarefas administrativas exigem privilégios elevados. Esses privilégios pertencem a uma conta especial conhecida como **usuário root no Linux**. Embora você possa fazer login diretamente como root, é frequentemente mais seguro e gerenciável obter acesso de superusuário temporariamente.

### O Comando `su`

Além do comando `sudo`, você pode usar `su` (substituir usuário) para obter privilégios de superusuário. Quando executado sem um nome de usuário, `su` tenta abrir uma nova sessão de shell para o **usuário root do linux**, solicitando a senha de root.

```bash
su
```

Você também pode usar este comando para mudar para qualquer outro usuário no sistema, desde que saiba a senha dele.

### Riscos de um Shell Root Persistente

Usar `su` para abrir um shell root tem desvantagens significativas. Operar continuamente como usuário root aumenta o risco de cometer um erro crítico que altera o sistema. Além disso, as ações realizadas em um shell root não são registradas sob sua conta de usuário pessoal, dificultando a auditoria das alterações do sistema. Por essas razões, a melhor prática é usar `sudo` para comandos individuais que exigem acesso de superusuário.

### O Arquivo `sudoers`

Então, como o sistema determina quem tem permissão para usar `sudo`? O acesso é controlado por um arquivo de configuração localizado em `/etc/sudoers`. Este arquivo lista os usuários e grupos que têm permissão para executar comandos como superusuário.

Para editar este arquivo com segurança, você deve sempre usar o comando `visudo`. Este utilitário abre o arquivo `sudoers` em um editor de texto e realiza uma verificação de sintaxe antes de salvar, o que ajuda a prevenir erros de configuração que poderiam bloquear seu acesso administrativo.

## Exercise

Coloque seu conhecimento em prática. O seguinte laboratório prático ajudará a reforçar sua compreensão sobre acesso e privilégios de superusuário:

1. **[Configurar Contas de Usuário e Privilégios Sudo no Linux](https://labex.io/pt/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Pratique a aplicação de políticas de senha, o bloqueio e desbloqueio de contas de usuário, a proteção da conta root e a concessão de permissões administrativas, relacionados diretamente ao gerenciamento de acesso de superusuário.

Este laboratório o ajudará a aplicar os conceitos em cenários reais e a ganhar confiança no gerenciamento de privilégios de usuário e acesso de superusuário.

## Quiz Question

Qual arquivo lista os usuários e grupos com privilégios `sudo`? Por favor, forneça o caminho completo. (Nota: Sua resposta deve estar em inglês e diferencia maiúsculas de minúsculas).

## Quiz Answer

/etc/sudoers
