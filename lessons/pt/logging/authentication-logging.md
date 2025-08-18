---
index: 5
lang: "pt"
title: "Registro de Autenticação"
meta_title: "Registro de Autenticação - Registro de Logs"
meta_description: "Aprenda sobre o registro de autenticação do Linux com /var/log/auth.log. Entenda os logins de usuários e solucione problemas de acesso com este guia essencial."
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

Realize algumas tentativas de login falhas e, em seguida, uma bem-sucedida. Depois, examine seu arquivo `/var/log/auth.log` para ver o que ocorreu.

## Quiz Question

Qual arquivo de log é usado para autenticação de usuário?

## Quiz Answer

auth.log
