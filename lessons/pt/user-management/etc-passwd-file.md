---
index: 3
lang: "pt"
title: "/etc/passwd"
meta_title: "/etc/passwd - Gerenciamento de Usuários"
meta_description: "Um guia completo sobre o arquivo /etc/passwd no Linux. Aprenda a interpretar campos de dados de usuário, entender UIDs e ver exemplos como root:x:0:0:root:/root:/bin/bash."
meta_keywords: "/etc/passwd, /etc/passwd no linux, root:x:0:0:root:/root:/bin/bash, ID de usuário, UID, gerenciamento de usuários, tutorial Linux"
---

## Lesson Content

No Linux, nomes de usuário são rótulos legíveis por humanos, mas o sistema identifica os usuários com um ID de Usuário (UID) exclusivo. O mapeamento entre nomes de usuário e UIDs é armazenado no arquivo `/etc/passwd`, um componente crítico para o gerenciamento de usuários.

Para visualizar seu conteúdo, você pode usar um comando simples:

```bash
cat /etc/passwd
```

Este arquivo exibe uma lista de todos os usuários do sistema e informações detalhadas sobre eles. Cada linha representa uma única conta de usuário.

### Desmembrando os Campos do /etc/passwd

A linha típica neste arquivo, muitas vezes a primeira, se parece com isto:

```plaintext
root:x:0:0:root:/root:/bin/bash
```

Esta entrada para o usuário `root` contém sete campos separados por dois pontos (`:`). Entender a estrutura do `/etc/passwd` no Linux é fundamental para gerenciar usuários. Vamos detalhar cada campo:

1.  **Nome de Usuário**: O nome de login do usuário (ex: `root`).
2.  **Senha**: Um espaço reservado para a senha criptografada do usuário. A senha real não é armazenada aqui por razões de segurança.
    - Um `x` indica que a senha criptografada está no arquivo `/etc/shadow`.
    - Um `*` (asterisco) significa que a conta está bloqueada e não pode ser usada para login.
    - Um campo em branco significa que o usuário não tem senha.
3.  **ID de Usuário (UID)**: O identificador numérico exclusivo para o usuário. O usuário `root` sempre tem um UID de `0`.
4.  **ID do Grupo (GID)**: O identificador numérico para o grupo primário do usuário.
5.  **Campo GECOS**: Um campo de comentário que tradicionalmente contém informações extras como o nome completo do usuário, número de telefone ou localização do escritório. É delimitado por vírgulas.
6.  **Diretório Home**: O caminho absoluto para o diretório home do usuário (ex: `/root`).
7.  **Shell Padrão**: O interpretador de linha de comando padrão do usuário, que é executado no login (ex: `/bin/bash`).

### Usuários do Sistema e Contas Especiais

Ao inspecionar o arquivo `/etc/passwd`, você notará muitas contas que não pertencem a usuários humanos. Estas são contas de sistema usadas para executar serviços ou processos específicos com permissões limitadas, aumentando a segurança do sistema. Por exemplo, o usuário `daemon` é usado para executar processos em segundo plano (daemons).

### Editando o Arquivo /etc/passwd

Embora tecnicamente você possa editar o arquivo `/etc/passwd` diretamente usando um editor de texto ou o comando `vipw`, isso é fortemente desencorajado. Edições manuais podem facilmente introduzir erros de sintaxe, potencialmente bloqueando seu acesso ao sistema ou causando instabilidade.

É sempre mais seguro e confiável usar utilitários de linha de comando dedicados como `useradd`, `usermod` e `userdel` para gerenciar contas de usuário. Essas ferramentas são projetadas para modificar o arquivo corretamente e lidar com todas as configurações relacionadas.

## Exercise

Para solidificar seu conhecimento, experimente estes laboratórios práticos. Eles ajudarão você a aplicar os conceitos de IDs de usuário e gerenciamento de contas em cenários do mundo real e a construir confiança com a administração de usuários do Linux.

1.  **[Gerenciar Contas de Usuário Linux com useradd, usermod e userdel](https://labex.io/pt/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratique o ciclo de vida completo da administração de usuários, desde a criação e proteção de novas contas até a modificação e exclusão delas.
2.  **[Gerenciar Grupos Linux com groupadd, usermod e groupdel](https://labex.io/pt/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Ganhe experiência prática com utilitários de linha de comando essenciais para administração de grupos, incluindo a criação de novos grupos e a modificação de associações de usuários.
3.  **[Configurar Contas de Usuário e Privilégios Sudo no Linux](https://labex.io/pt/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprenda técnicas essenciais para gerenciar contas de usuário e privilégios sudo para aumentar a segurança de um sistema Linux.

## Quiz Question

Se uma conta de usuário for bloqueada e não puder ser usada para login, como isso é denotado no campo de senha do arquivo `/etc/passwd`? Responda usando apenas o caractere necessário.

## Quiz Answer

-
