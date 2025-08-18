---
index: 4
lang: "pt"
title: "/etc/shadow"
meta_title: "/etc/shadow - Gerenciamento de Usuários"
meta_description: "Aprenda sobre o arquivo /etc/shadow no Linux, seus campos e como ele protege as senhas dos usuários. Entenda a autenticação Linux para iniciantes."
meta_keywords: "/etc/shadow, segurança Linux, autenticação de usuário, gerenciamento de senhas, tutorial Linux, guia para iniciantes"
---

## Lesson Content

O arquivo `/etc/shadow` é usado para armazenar informações sobre a autenticação do usuário. Ele requer permissões de leitura de superusuário.

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

Você notará que ele se parece muito com o conteúdo de `/etc/passwd`; no entanto, no campo da senha, você verá uma senha criptografada. Os campos são separados por dois pontos, da seguinte forma:

1. Nome de usuário
2. Senha criptografada
3. Data da última alteração de senha - expressa como o número de dias desde 1º de janeiro de 1970. Se houver um 0, isso significa que o usuário deve alterar sua senha na próxima vez que fizer login.
4. Idade mínima da senha - Dias que um usuário terá que esperar antes de poder alterar sua senha novamente.
5. Idade máxima da senha - Número máximo de dias antes que um usuário tenha que alterar sua senha.
6. Período de aviso de senha - Número de dias antes que uma senha expire.
7. Período de inatividade da senha - Número de dias após uma senha ter expirado para permitir o login com sua senha.
8. Data de expiração da conta - Data em que um usuário não poderá fazer login.
9. Campo reservado para uso futuro.

Na maioria das distribuições atuais, a autenticação do usuário não depende apenas do arquivo `/etc/shadow`; existem outros mecanismos em vigor, como o PAM (Pluggable Authentication Modules), que substituem a autenticação.

## Exercise

Observe o arquivo `/etc/shadow`.

## Quiz Question

Sem perguntas, siga em frente!

## Quiz Answer
