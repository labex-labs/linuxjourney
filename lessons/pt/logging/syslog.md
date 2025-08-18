---
lang: "pt"
title: "syslog"
meta_title: "syslog - Registro de Logs"
meta_description: "Aprenda sobre syslog e rsyslog no Linux, como gerenciar logs do sistema e usar o comando logger. Comece com este tutorial para iniciantes!"
meta_keywords: "syslog, rsyslog, logs Linux, comando logger, /var/log/syslog, tutorial Linux, Linux para iniciantes, registro de sistema"
---

## Lesson Content

O serviço syslog gerencia e envia logs para o registrador do sistema. Rsyslog é uma versão avançada do syslog; a maioria das distribuições Linux deve estar usando esta nova versão. A saída de todos os logs que o serviço syslog coleta pode ser encontrada em `/var/log/syslog` (todas as mensagens, exceto as de autenticação).

Para descobrir quais arquivos são mantidos pelo nosso registrador de sistema, veja os arquivos de configuração em `/etc/rsyslog.d`:

```plaintext
pete@icebox:~$ less /etc/rsyslog.d/50-default.conf
# First some standard log files.  Log by facility.
#
auth,authpriv.*                 /var/log/auth.log
*.*;auth,authpriv.none          -/var/log/syslog
#cron.*                         /var/log/cron.log
#daemon.*                       -/var/log/daemon.log
kern.*                          -/var/log/kern.log
#lpr.*                          -/var/log/lpr.log
mail.*                          -/var/log/mail.log
#user.*                         -/var/log/user.log
```

Essas regras para arquivos de log são denotadas pelo seletor na coluna esquerda e pela ação na coluna direita. A ação nos diz para onde enviar as informações de log: para um arquivo, console, etc. Lembre-se, nem todo aplicativo e serviço usa rsyslog para gerenciar seus logs, então se você quiser saber especificamente o que é registrado, você terá que procurar dentro deste diretório.

Vamos ver o registro em ação; você pode enviar um log manualmente com o comando `logger`:

```bash
logger -s Hello
```

Agora, olhe dentro do seu `/var/log/syslog`, e você deverá ver esta entrada em seus logs!

## Exercise

Olhe para o seu arquivo de configuração `/etc/rsyslog.d` e veja o que mais está sendo registrado via o registrador do sistema.

## Quiz Question

Qual comando você pode usar para registrar uma mensagem manualmente?

## Quiz Answer

logger
