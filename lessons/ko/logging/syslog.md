---
lang: "ko"
title: "syslog"
meta_description: "Linux 에서 syslog 및 rsyslog 에 대해 배우고, 시스템 로그를 관리하는 방법과 logger 명령을 사용하는 방법을 알아보세요. 이 초보자 친화적인 튜토리얼로 시작하세요!"
meta_keywords: "syslog, rsyslog, Linux 로그, logger command, /var/log/syslog, Linux 튜토리얼, 초보자 Linux, 시스템 로깅"
---

## Lesson Content

syslog 서비스는 로그를 관리하고 시스템 로거로 보냅니다. Rsyslog 는 syslog 의 고급 버전입니다. 대부분의 Linux 배포판은 이 새 버전을 사용해야 합니다. syslog 서비스가 수집하는 모든 로그의 출력은 `/var/log/syslog`에서 찾을 수 있습니다 (인증 메시지를 제외한 모든 메시지).

시스템 로거가 유지 관리하는 파일을 확인하려면 `/etc/rsyslog.d`의 구성 파일을 살펴보십시오:

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

이러한 로그 파일 규칙은 왼쪽 열의 선택자와 오른쪽 열의 작업으로 표시됩니다. 작업은 로그 정보를 어디로 보낼지 알려줍니다: 파일, 콘솔 등. 모든 애플리케이션과 서비스가 로그를 관리하기 위해 rsyslog 를 사용하는 것은 아니므로, 무엇이 기록되는지 구체적으로 알고 싶다면 이 디렉토리를 살펴보아야 합니다.

실제로 로깅이 작동하는 것을 봅시다. `logger` 명령으로 수동으로 로그를 보낼 수 있습니다:

```bash
logger -s Hello
```

이제 `/var/log/syslog`를 살펴보면 로그에 이 항목이 표시될 것입니다!

## Exercise

`/etc/rsyslog.d` 구성 파일을 살펴보고 시스템 로거를 통해 무엇이 더 기록되는지 확인하십시오.

## Quiz Question

메시지를 수동으로 기록하는 데 사용할 수 있는 명령은 무엇입니까?

## Quiz Answer

logger
