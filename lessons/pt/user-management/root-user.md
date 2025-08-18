---
lang: "pt"
title: "root"
meta_title: "root - Gerenciamento de Usuários"
meta_description: "Aprenda sobre o usuário root do Linux, o comando su e o arquivo /etc/sudoers. Entenda o acesso e as permissões de superusuário no Linux com este guia para iniciantes."
meta_keywords: "Linux root, comando su, arquivo sudoers, permissões Linux, superusuário, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Analisamos uma forma de obter acesso de superusuário usando o comando `sudo`. Você também pode executar comandos como superusuário com o comando `su`. Este comando irá "substituir usuários" e abrir um shell root se nenhum nome de usuário for especificado. Você pode usar este comando para substituir qualquer usuário, desde que saiba a senha.

```bash
su
```

Existem algumas desvantagens em usar este método: é muito mais fácil cometer um erro crítico executando tudo como root, você não terá registros dos comandos que usa para alterar as configurações do sistema, etc. Basicamente, se você precisar executar comandos como superusuário, apenas use `sudo`.

Agora que você sabe quais comandos executar como superusuário, a questão é como saber quem tem acesso para fazer isso? O sistema não permite que qualquer pessoa execute comandos como superusuário, então como ele sabe? Existe um arquivo chamado `/etc/sudoers`; este arquivo lista os usuários que podem executar `sudo`. Você pode editar este arquivo com o comando **visudo**.

## Exercise

Abra o arquivo `/etc/sudoers` e veja quais permissões de superusuário outros usuários na máquina têm.

## Quiz Question

Qual arquivo mostra os usuários que têm acesso ao `sudo`?

## Quiz Answer

/etc/sudoers
