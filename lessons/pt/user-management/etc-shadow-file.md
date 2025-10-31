---
index: 4
lang: "pt"
title: "/etc/shadow"
meta_title: "/etc/shadow - Gerenciamento de Usuários"
meta_description: "Explore o arquivo /etc/shadow no Linux, um componente crítico para a autenticação de usuários. Aprenda a visualizá-lo com 'cat /etc/shadow' e entenda a estrutura do arquivo etc shadow, que armazena senhas criptografadas e informações de política."
meta_keywords: "etc shadow, arquivo etc/shadow no linux, cat /etc/shadow, etc shadow no linux, /etc/shadow, autenticação de usuário, segurança de senha, administração de sistema Linux"
---

## Lesson Content

O arquivo `/etc/shadow` é um componente crítico nos sistemas Linux para armazenar informações sensíveis de autenticação de usuário. Diferentemente do arquivo `/etc/passwd`, que pode ser lido por qualquer um, o `/etc/shadow` requer privilégios de superusuário para acesso, fornecendo um local seguro para os dados de senha.

### O Papel do Arquivo etc/shadow no Linux

O principal objetivo do **arquivo etc/shadow no Linux** é armazenar senhas de usuário criptografadas e políticas de envelhecimento de senha. Ao separar esses dados sensíveis das informações gerais do usuário em `/etc/passwd`, o sistema aumenta a segurança. Se um usuário sem privilégios pudesse ler os hashes de senha, ele poderia tentar quebrá-los offline.

### Visualizando o Arquivo com cat /etc/shadow

Para inspecionar o conteúdo deste arquivo, você deve usar um comando com privilégios de superusuário, como `sudo`. O comando `cat /etc/shadow` é comumente usado para este fim.

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

O formato de saída do arquivo **etc shadow** é uma série de campos separados por dois pontos, com cada linha representando um único usuário.

### Entendendo a Estrutura do Arquivo

Cada linha em `/etc/shadow` contém nove campos, separados por dois pontos:

1. **Nome de Usuário**: O nome de login do usuário.
2. **Senha Criptografada**: A senha do usuário em formato hash. Um asterisco (`*`) ou ponto de exclamação (`!`) aqui significa que a conta está bloqueada.
3. **Data da Última Alteração de Senha**: O número de dias desde 1º de janeiro de 1970 em que a senha foi alterada pela última vez. Um valor de `0` força uma alteração de senha no próximo login.
4. **Idade Mínima da Senha**: O número mínimo de dias que devem passar antes que o usuário possa alterar sua senha novamente.
5. **Idade Máxima da Senha**: O número máximo de dias que a senha é válida. Após esse período, o usuário deve alterá-la.
6. **Período de Aviso de Senha**: O número de dias antes do vencimento da senha em que o usuário receberá uma mensagem de aviso.
7. **Período de Inatividade da Senha**: O número de dias após o vencimento da senha em que a conta é desativada.
8. **Data de Expiração da Conta**: Uma data absoluta, expressa em dias desde 1º de janeiro de 1970, em que a conta do usuário será desativada.
9. **Campo Reservado**: Este campo é reservado para uso futuro.

Embora o arquivo `/etc/shadow` seja fundamental, a maioria das distribuições modernas o complementa com outros mecanismos de autenticação, como os Módulos de Autenticação Conectáveis (PAM), que oferecem esquemas de autenticação mais flexíveis e avançados.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre autenticação de usuário e gerenciamento de senhas no Linux:

1. **[Gerenciar Contas de Usuário Linux com useradd, usermod e userdel](https://labex.io/pt/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratique o ciclo de vida completo da administração de usuários, desde a criação e proteção de novas contas com `useradd` e `passwd` até a modificação e exclusão delas.
2. **[Configurar Contas de Usuário e Privilégios Sudo no Linux](https://labex.io/pt/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprenda técnicas essenciais para gerenciar contas de usuário e privilégios sudo, incluindo a aplicação de políticas de senha e a proteção de contas.

Esses laboratórios ajudarão você a aplicar os conceitos de gerenciamento de usuários e senhas em cenários reais e a ganhar confiança com a administração de sistemas Linux.

## Quiz Question

Sem perguntas, siga em frente!
