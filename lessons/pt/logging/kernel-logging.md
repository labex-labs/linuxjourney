---
index: 4
lang: "pt"
title: "Registro do Kernel"
meta_title: "Registro do Kernel - Registro"
meta_description: "Aprenda sobre o registro do kernel Linux com dmesg e kern.log. Entenda as mensagens de inicialização e problemas de hardware. Explore os logs do kernel para obter insights do sistema."
meta_keywords: "dmesg, kern.log, registro Linux, mensagens do kernel, log de inicialização, tutorial Linux, guia para iniciantes"
---

## Lesson Content

### /var/log/dmesg

No momento da inicialização, seu sistema registra informações sobre o buffer de anel do kernel. Isso nos mostra informações sobre drivers de hardware, informações do kernel e status durante a inicialização, entre outras coisas. Este arquivo de log pode ser encontrado em `/var/log/dmesg` e é redefinido a cada inicialização. Você pode não ver nenhum uso nele agora, mas se você tivesse algum problema durante a inicialização ou um problema de hardware, `dmesg` é o melhor lugar para procurar. Você também pode visualizar este log usando o comando `dmesg`.

### /var/log/kern.log

Outro log que você pode usar para visualizar informações do kernel é o arquivo `/var/log/kern.log`. Este registra informações e eventos do kernel em seu sistema; ele também registra a saída de `dmesg`.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento de usuários e grupos do Linux:

1. **[Gerenciar Contas de Usuário Linux com useradd, usermod e userdel](https://labex.io/pt/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratique o ciclo de vida completo da administração de usuários, desde a criação e segurança de novas contas até a modificação e exclusão delas.
2. **[Gerenciar Grupos Linux com groupadd, usermod e groupdel](https://labex.io/pt/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Obtenha experiência prática com utilitários de linha de comando essenciais para a administração de grupos, incluindo a criação de novos grupos, a modificação de associações de usuários e a remoção de grupos.
3. **[Configurar Contas de Usuário e Privilégios Sudo no Linux](https://labex.io/pt/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprenda técnicas essenciais para gerenciar contas de usuário e privilégios sudo para aumentar a segurança de um sistema Linux, incluindo a aplicação de políticas de senha e a concessão de permissões administrativas.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e a construir confiança com o gerenciamento de usuários e grupos no Linux.

## Quiz Question

Qual comando pode ser usado para visualizar as mensagens de inicialização do kernel?

## Quiz Answer

dmesg
