---
index: 5
lang: "pt"
title: "Registro de Autenticação"
meta_title: "Registro de Autenticação - Registro"
meta_description: "Aprenda sobre o registro de autenticação do Linux com /var/log/auth.log. Entenda os logins de usuários e resolva problemas de acesso com este guia essencial."
meta_keywords: "autenticação Linux, auth.log, registro Linux, login de usuário, segurança Linux, iniciante, tutorial, guia"
---

## Lesson Content

O registro de autenticação pode ser muito útil para consultar se você estiver tendo problemas para fazer login.

### /var/log/auth.log

Este arquivo contém logs de autorização do sistema, como logins de usuários e os métodos de autenticação utilizados.

Exemplo de trecho:

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre autenticação de usuário e gerenciamento de contas:

1. **[Configurar Contas de Usuário e Privilégios Sudo no Linux](https://labex.io/pt/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Pratique a aplicação de políticas de senha, bloqueio/desbloqueio de contas de usuário, proteção da conta root e concessão de permissões administrativas, tudo isso crítico para entender a segurança da autenticação.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com o gerenciamento de usuários e segurança do Linux.

## Quiz Question

Qual arquivo de log é usado para autenticação de usuário?

## Quiz Answer

auth.log
