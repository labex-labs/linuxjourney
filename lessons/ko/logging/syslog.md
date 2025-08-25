---
index: 2
lang: "ko"
title: "syslog"
meta_title: "syslog - 로깅"
meta_description: "Linux 에서 syslog 및 rsyslog 에 대해 배우고, 시스템 로그를 관리하고, logger 명령을 사용하는 방법을 알아보세요. 이 초보자 친화적인 튜토리얼로 시작하세요!"
meta_keywords: "syslog, rsyslog, Linux 로그, logger 명령, /var/log/syslog, Linux 튜토리얼, 초보자 Linux, 시스템 로깅"
---

## Lesson Content

syslog 서비스는 로그를 관리하고 시스템 로거로 보냅니다. Rsyslog 는 syslog 의 고급 버전입니다. 대부분의 Linux 배포판은 이 새 버전을 사용해야 합니다. syslog 서비스가 수집하는 모든 로그의 출력은 `/var/log/syslog`에서 찾을 수 있습니다 (인증 메시지를 제외한 모든 메시지).

시스템 로거가 유지 관리하는 파일을 확인하려면 `/etc/rsyslog.d`의 구성 파일을 살펴보십시오.

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

이러한 로그 파일 규칙은 왼쪽 열의 선택기와 오른쪽 열의 작업으로 표시됩니다. 작업은 로그 정보를 어디로 보낼지 알려줍니다: 파일, 콘솔 등. 모든 애플리케이션과 서비스가 rsyslog 를 사용하여 로그를 관리하는 것은 아니므로, 무엇이 로깅되는지 구체적으로 알고 싶다면 이 디렉토리를 살펴보아야 합니다.

실제로 로깅이 작동하는 것을 봅시다. `logger` 명령으로 수동으로 로그를 보낼 수 있습니다.

```bash
logger -s Hello
```

이제 `/var/log/syslog`를 살펴보십시오. 로그에 이 항목이 표시될 것입니다!

## Exercise

연습하면 완벽해집니다! 다음은 Linux 로깅 및 파일 보기에 대한 이해를 강화하기 위한 실습입니다.

1. **[Linux 에서 로그 및 구성 파일 보기](https://labex.io/ko/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 시스템 로그 및 구성 파일을 포함하여 텍스트 파일을 효율적으로 보고 탐색하기 위한 필수 Linux 명령줄 기술을 연습합니다.
2. **[Linux tail 명령: 파일 끝 표시](https://labex.io/ko/labs/linux-linux-tail-command-file-end-display-214303)** - 텍스트 파일의 끝을 보고 모니터링하는 Linux `tail` 명령을 배웁니다. 이는 실시간 로그 분석에 특히 유용합니다.
3. **[Linux 에서 grep 으로 텍스트 검색](https://labex.io/ko/labs/comptia-search-text-with-grep-in-linux-590841)** - 파일 내에서 특정 텍스트 패턴을 검색하는 방법을 배웁니다. 이는 중요한 정보를 찾기 위해 로그 항목을 샅샅이 뒤지는 데 매우 유용한 기술입니다.

이 실습은 실제 시나리오에서 로그 관리 및 파일 검사 개념을 적용하고 Linux 시스템 관리 능력을 향상시키는 데 도움이 될 것입니다.

## Quiz Question

메시지를 수동으로 로깅하는 데 사용할 수 있는 명령은 무엇입요?

## Quiz Answer

logger
