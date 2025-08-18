---
index: 2
lang: "ru"
title: "syslog"
meta_title: "syslog - Ведение журнала"
meta_description: "Узнайте о syslog и rsyslog в Linux, как управлять системными логами и использовать команду logger. Начните с этого удобного для новичков руководства!"
meta_keywords: "syslog, rsyslog, логи Linux, команда logger, /var/log/syslog, учебник Linux, Linux для начинающих, системное логирование"
---

## Lesson Content

Служба syslog управляет и отправляет логи системному логгеру. Rsyslog — это расширенная версия syslog; большинство дистрибутивов Linux должны использовать эту новую версию. Вывод всех логов, собираемых службой syslog, можно найти в `/var/log/syslog` (каждое сообщение, кроме сообщений аутентификации).

Чтобы узнать, какие файлы поддерживаются нашим системным логгером, посмотрите на конфигурационные файлы в `/etc/rsyslog.d`:

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

Эти правила для файлов логов обозначаются селектором в левом столбце и действием в правом столбце. Действие сообщает нам, куда отправлять информацию лога: в файл, консоль и т.д. Помните, что не каждое приложение и служба используют rsyslog для управления своими логами, поэтому, если вы хотите узнать, что именно логируется, вам придется заглянуть в этот каталог.

Давайте посмотрим логирование в действии; вы можете вручную отправить лог с помощью команды `logger`:

```bash
logger -s Hello
```

Теперь загляните в свой `/var/log/syslog`, и вы должны увидеть эту запись в своих логах!

## Exercise

Посмотрите свой конфигурационный файл `/etc/rsyslog.d` и узнайте, что еще логируется через системный логгер.

## Quiz Question

Какую команду вы можете использовать для ручного логирования сообщения?

## Quiz Answer

logger
