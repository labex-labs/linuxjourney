---
lang: "ko"
title: "일반 로깅"
meta_title: "일반 로깅 - 로깅"
meta_description: "`/var/log/messages` 및 syslog 와 같은 Linux 로그 파일에 대해 알아보세요. 효과적인 시스템 문제 해결을 위해 이들의 차이점을 이해하세요. Linux 여정을 시작하세요!"
meta_keywords: "Linux 로그, syslog, var/log/messages, Linux 문제 해결, Linux 초보자, Linux 가이드, 시스템 로그"
---

## Lesson Content

시스템에서 볼 수 있는 많은 로그 파일이 있습니다. 많은 중요한 파일은 `/var/log` 아래에서 찾을 수 있습니다. 모든 파일을 다루지는 않겠지만, 주요 파일 몇 가지를 살펴보겠습니다.

시스템이 무엇을 하고 있는지 엿볼 수 있는 두 가지 일반 로그 파일이 있습니다:

### `/var/log/messages`

이 로그는 부팅 중 (dmesg), auth, cron, daemon 등에서 기록된 메시지를 포함하여 중요하지 않거나 디버그가 아닌 모든 메시지를 포함합니다. 시스템이 어떻게 작동하는지 파악하는 데 매우 유용합니다.

### `/var/log/syslog`

이것은 auth 메시지를 제외한 모든 것을 기록합니다. 시스템의 오류를 디버깅하는 데 매우 유용합니다.

이 두 로그는 시스템 문제를 해결할 때 충분할 것입니다. 그러나 특정 로그 구성 요소만 보려면 해당 구성 요소에 대한 별도의 로그도 있습니다.

## Exercise

`/var/log/messages` 및 `/var/log/syslog` 파일을 살펴보고 차이점이 무엇인지 확인하십시오.

## Quiz Question

auth 메시지를 제외한 모든 것을 기록하는 로그 파일은 무엇입니까?

## Quiz Answer

syslog
