---
index: 2
lang: "ko"
title: "syslog"
meta_title: "syslog - 로깅"
meta_description: "Linux 에서 syslog 및 rsyslog 에 대해 알아보고, 시스템 로그를 관리하고, logger 명령을 사용하는 방법을 알아보세요. 이 초보자 친화적인 튜토리얼로 시작하세요!"
meta_keywords: "syslog, rsyslog, Linux 로그, logger 명령, /var/log/syslog, Linux 튜토리얼, 초보자 Linux, 시스템 로깅"
---

## Lesson Content

syslog 서비스는 로그를 시스템 로거로 관리하고 전송합니다. Rsyslog 는 syslog 의 고급 버전이며, 대부분의 Linux 배포판은 이 새로운 버전을 사용해야 합니다. syslog 서비스가 수집하는 모든 로그의 출력은 `/var/log/syslog`에서 찾을 수 있습니다 (인증 메시지를 제외한 모든 메시지).

시스템 로거가 어떤 파일을 유지 관리하는지 확인하려면 `/etc/rsyslog.d`의 구성 파일을 확인하십시오.

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

로그 파일에 대한 이러한 규칙은 왼쪽 열의 선택자 (selector) 와 오른쪽 열의 동작 (action) 으로 표시됩니다. 동작은 로그 정보를 파일, 콘솔 등으로 보낼 위치를 알려줍니다. 모든 애플리케이션과 서비스가 로그 관리를 위해 rsyslog 를 사용하는 것은 아니므로, 구체적으로 무엇이 기록되는지 알고 싶다면 이 디렉터리 내부를 확인해야 합니다.

실제로 로깅이 작동하는지 확인해 봅시다. `logger` 명령을 사용하여 수동으로 로그를 보낼 수 있습니다.

```bash
logger -s Hello
```

이제 `/var/log/syslog` 내부를 확인하면 로그에 이 항목이 표시되어야 합니다.

## Exercise

연습이 완벽을 만듭니다! Linux 로깅 및 파일 보기에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[Linux 에서 로그 및 구성 파일 보기](https://labex.io/ko/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 시스템 로그 및 구성 파일을 포함하여 텍스트 파일을 효율적으로 보고 탐색하기 위한 필수 Linux 명령줄 기술을 연습합니다.
2. **[Linux tail 명령: 파일 끝 표시](https://labex.io/ko/labs/linux-linux-tail-command-file-end-display-214303)** - 텍스트 파일의 끝을 보고 모니터링하는 Linux `tail` 명령을 학습하며, 이는 실시간 로그 분석에 특히 유용합니다.
3. **[Linux 에서 grep 을 사용하여 텍스트 검색](https://labex.io/ko/labs/comptia-search-text-with-grep-in-linux-590841)** - 파일 내에서 특정 텍스트 패턴을 검색하는 방법을 학습하며, 이는 로그 항목을 선별하여 중요한 정보를 찾는 데 매우 유용한 기술입니다.

이 랩들은 로그 관리 및 파일 검사 개념을 실제 시나리오에 적용하고 Linux 시스템 관리 역량을 키우는 데 도움이 될 것입니다.

## Quiz Question

메시지를 수동으로 기록하는 데 사용할 수 있는 명령은 무엇입니까?

## Quiz Answer

logger
