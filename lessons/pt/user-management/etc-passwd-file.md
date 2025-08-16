---
title: "/etc/passwd"
description: "Aprenda sobre o arquivo /etc/passwd no Linux, entenda os campos de informação do usuário e como os UIDs funcionam. Explore este arquivo de configuração essencial."
keywords: "/etc/passwd, usuários Linux, ID de usuário, UID, tutorial Linux, iniciante, guia, comandos Linux"
---

## Lesson Content

Lembre-se de que os nomes de usuário não são realmente identificações para os usuários. O sistema usa um ID de usuário (UID) para identificar um usuário. Para descobrir quais usuários estão mapeados para qual ID, consulte o arquivo `/etc/passwd`.

```bash
cat /etc/passwd
```

Este arquivo mostra uma lista de usuários e informações detalhadas sobre eles. Por exemplo, a primeira linha neste arquivo provavelmente se parece com isto:

```plaintext
root:x:0:0:root:/root:/bin/bash
```

Cada linha exibe informações de usuário para um usuário; mais comumente, você verá o usuário root como a primeira linha. Existem muitos campos separados por dois pontos que fornecem informações adicionais sobre o usuário. Vamos examiná-los todos:

1. **Nome de usuário**
2. **Senha do usuário** - A senha não é realmente armazenada neste arquivo; ela geralmente é armazenada no arquivo `/etc/shadow`. Discutiremos mais sobre `/etc/shadow` na próxima lição, mas por enquanto, saiba que ele contém senhas de usuário criptografadas. Você pode ver muitos símbolos diferentes neste campo: se você vir um "x", isso significa que a senha está armazenada no arquivo `/etc/shadow`; um "\*" significa que o usuário não tem acesso de login; e se houver um campo em branco, isso significa que o usuário não tem uma senha.
3. **O ID do usuário** - Como você pode ver, o root tem o UID de 0.
4. **O ID do grupo**
5. **Campo GECOS** - Isso é usado para geralmente deixar comentários sobre o usuário ou conta, como seu nome real ou número de telefone. É delimitado por vírgulas.
6. **Diretório home do usuário**
7. **Shell do usuário** - Você provavelmente verá muitos usuários usando bash como seu shell padrão.

Normalmente, na página de configurações de um usuário, você esperaria ver apenas usuários humanos. No entanto, você notará que `/etc/passwd` contém outros usuários. Lembre-se de que os usuários estão realmente no sistema apenas para executar processos com diferentes permissões. Às vezes, queremos executar processos com permissões predeterminadas. Por exemplo, o usuário `daemon` é usado para processos daemon.

Além disso, deve-se notar que você pode editar o arquivo `/etc/passwd` manualmente se quiser adicionar usuários e modificar informações com a ferramenta `vipw`. No entanto, coisas como essas são melhor deixadas para as ferramentas que discutiremos em uma lição posterior, como `useradd` e `userdel`.

## Exercise

Observe seu arquivo `/etc/passwd`, examine alguns dos usuários e anote o acesso que eles têm.

## Quiz Question

Se um usuário não tem acesso de login, como isso é indicado em `/etc/passwd`?

## Quiz Answer

-
