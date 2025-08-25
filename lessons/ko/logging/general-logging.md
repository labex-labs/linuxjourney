---
index: 3
lang: "ko"
title: "일반 로깅"
meta_title: "일반 로깅 - 로깅"
meta_description: "Linux 로그 파일 (예: /var/log/messages 및 syslog) 에 대해 알아보세요. 효과적인 시스템 문제 해결을 위해 이들의 차이점을 이해하세요. Linux 여정을 시작하세요!"
meta_keywords: "Linux 로그, syslog, var/log/messages, Linux 문제 해결, Linux 초보자, Linux 가이드, 시스템 로그"
---

## Lesson Content

시스템에서 볼 수 있는 많은 로그 파일이 있습니다. 많은 중요한 파일은 `/var/log` 아래에서 찾을 수 있습니다. 모든 파일을 다루지는 않겠지만, 주요 파일 몇 가지를 살펴보겠습니다.

시스템이 무엇을 하고 있는지 엿볼 수 있는 두 가지 일반적인 로그 파일이 있습니다:

### `/var/log/messages`

이 로그에는 부팅 중 (dmesg), 인증 (auth), cron, 데몬 (daemon) 등에서 기록된 메시지를 포함하여 중요하지 않거나 디버그가 아닌 모든 메시지가 포함됩니다. 시스템이 어떻게 작동하는지 엿보는 데 매우 유용합니다.

### `/var/log/syslog`

이 로그는 인증 메시지를 제외한 모든 것을 기록합니다. 시스템의 오류를 디버깅하는 데 매우 유용합니다.

이 두 로그는 시스템 문제를 해결할 때 충분할 것입니다. 그러나 특정 로그 구성 요소만 보려면 해당 구성 요소에 대한 별도의 로그도 있습니다.

## Exercise

연습이 완벽을 만듭니다! 로그 파일을 보고 분석하는 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux tail 명령어: 파일 끝 표시](https://labex.io/ko/labs/linux-linux-tail-command-file-end-display-214303)** - 로그 분석에 필수적인 텍스트 파일의 끝을 보고 모니터링하는 Linux `tail` 명령어를 배웁니다.
2. **[Linux head 명령어: 파일 시작 표시](https://labex.io/ko/labs/linux-linux-head-command-file-beginning-display-214302)** - 텍스트 파일의 초기 줄을 표시하는 `head` 명령어를 탐색하여 로그 헤더를 빠르게 확인하는 데 유용합니다.
3. **[빠른 위협 탐지](https://labex.io/ko/labs/linux-rapid-threat-detection-387930)** - `tail` 및 `head`를 사용하여 최근 로그 항목을 빠르게 추출하고 분석하는 사이버 보안 분석을 위한 필수 Linux 명령줄 기술을 연습합니다.

이 랩은 실제 시나리오에서 로그 파일 보기 개념을 적용하고 시스템 모니터링에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

인증 메시지를 제외한 모든 것을 기록하는 로그 파일은 무엇입니까?

## Quiz Answer

syslog
