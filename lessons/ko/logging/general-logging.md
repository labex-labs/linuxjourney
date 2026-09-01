---
lesson_id: "general-logging"
course_id: "logging"
lang: "ko"
order_index: 3
title: "일반 로깅"
description: "일반적인 리눅스 시스템 로그를 찾고, 필터링하고, 추적하며, 서로 연관 짓는 방법을 알아봅니다."
meta_title: "일반 로깅 - 로깅"
meta_description: "일반 리눅스 로그를 위한 초보자 가이드입니다. /var/log/messages와 syslog를 활용한 시스템 모니터링, 로그 분석 및 리눅스 문제 해결을 알아봅니다."
meta_keywords: "리눅스 로그, syslog, var/log/messages, 리눅스 문제 해결, 시스템 로그, 로그 분석, 시스템 모니터링, /var/log"
---

일반 시스템 로그에는 여러 소스에서 생성된 일상적인 알림, 경고 및 오류가 함께 들어 있습니다. 조사하기 좋은 출발점이지만 파일 이름과 내용은 라우팅 정책에 따라 정해지며 모든 리눅스 시스템에 보편적으로 보장되지는 않습니다.

## 관련 소스 찾기

배포판과 설정에 따라 일반 메시지는 `/var/log/syslog`, `/var/log/messages`, systemd 저널 또는 둘 이상의 대상에 나타날 수 있습니다. 먼저 호스트와 사고 발생 시간대를 파악한 다음 사용 가능한 소스를 조사합니다.

```bash
$ ls -lh /var/log
$ journalctl --since '2026-08-31 09:00' --until '2026-08-31 09:15'
```

애플리케이션 로그는 자체 하위 디렉터리나 외부 서비스에 있을 수 있습니다. 인증, 감사, 패키지, 데이터베이스 및 웹 서버 레코드는 일반 로그 흐름에서 의도적으로 분리될 수 있습니다.

:::single-choice{#general-logs-universal-file} 모든 리눅스 호스트에 `/var/log/messages`가 있다고 가정하면 안 되는 이유는 무엇입니까?

::option[일반 로그 대상은 로컬 수집기와 라우팅 정책에 따라 달라지기 때문입니다.]{#general-logs-local-routing .correct explanation="저널 전용 시스템이나 다른 syslog 설정은 다른 대상을 사용할 수 있습니다."}
::option[리눅스는 각 디스크에 로그 파일을 하나만 허용하기 때문입니다.]{#general-logs-one-file explanation="시스템은 일반적으로 많은 로그 파일과 저널 저장소를 유지합니다."}
::option[이 경로는 사용자 문서 전용으로 예약되어 있기 때문입니다.]{#general-logs-user-documents explanation="/var/log 계층은 관례적으로 로그에 사용됩니다."}
:::

## 텍스트 로그 조사하기

제어된 탐색에는 `less`를, 최신 레코드에는 `tail`을 사용합니다.

```bash
$ sudo less /var/log/syslog
$ sudo tail -n 100 /var/log/messages
```

제한된 재현 작업 중에는 `tail -F FILE`로 새로 추가되는 줄을 추적합니다. `-F`는 단순한 스냅샷과 달리 로테이션 중 파일이 교체되면 다시 시도합니다. `Ctrl-C`로 추적을 중지하고 광범위한 권한이 있는 세션을 계속 열어 두지 마십시오.

:::single-choice{#general-logs-tail-f-capability} 통제된 재현 작업 중 `tail -F`는 무엇에 유용합니까?

::option[일반적인 로테이션으로 교체된 파일을 이름을 기준으로 계속 추적합니다.]{#general-logs-tail-follow .correct explanation="이름을 기준으로 다시 시도하므로 활성 파일의 이름이 바뀌고 새로 생성된 뒤에도 추적할 수 있습니다."}
::option[모든 로그 심각도를 debug로 변경합니다.]{#general-logs-tail-debug explanation="tail은 파일 내용을 읽으며 이벤트 생성기의 설정을 바꾸지 않습니다."}
::option[다른 프로그램 없이 압축된 아카이브를 복호화합니다.]{#general-logs-tail-decrypt explanation="일반적인 아카이브 압축 해제나 복호화 기능을 제공하지 않습니다."}
:::

## 맥락을 잃지 않고 필터링하기

처음부터 제한 없는 실시간 스트림을 파이프로 넘기지 말고 범위가 제한된 파일이나 저널 시간대를 검색합니다.

```bash
$ grep -n -C 3 'connection refused' /var/log/example.log
$ journalctl -u example.service --since '10 minutes ago' --grep='connection refused'
```

대소문자, 표현, 속도 제한 및 현지화 때문에 문자 그대로의 검색은 불완전할 수 있습니다. 성공한 이벤트와 실패한 이벤트를 모두 기록하고, 원인이 눈에 보이는 오류보다 앞서 발생할 수 있으므로 주변 줄도 보존합니다.

:::single-choice{#general-logs-context-lines} 일치하는 오류 주변의 줄을 함께 봐야 하는 이유는 무엇입니까?

::option[앞선 이벤트가 뒤의 실패를 설명할 수 있기 때문입니다.]{#general-logs-preceding-context .correct explanation="시간적 맥락은 문자열 하나를 사고 전체로 보지 않고 사건의 순서를 재구성하는 데 도움이 됩니다."}
::option[맥락을 보면 첫 번째 일치 항목이 근본 원인임이 보장되기 때문입니다.]{#general-logs-guaranteed-cause explanation="추가 증거도 서로 연관 지어야 하며, 맥락만으로 인과 관계가 입증되지는 않습니다."}
::option[서비스 설정이 자동으로 변경되기 때문입니다.]{#general-logs-context-config explanation="검색 출력은 읽기 전용이며 서비스 설정을 갱신하지 않습니다."}
:::

## 로테이션 및 보관된 로그 포함하기

사고가 로그 로테이션 경계에 걸쳐 있을 수 있습니다. 활성 파일, 번호가 붙은 아카이브 및 압축 파일에는 같은 사건 순서의 서로 다른 부분이 담길 수 있습니다. `zgrep`과 `zless` 같은 도구는 gzip으로 압축된 아카이브를 읽습니다.

```bash
$ sudo zgrep -n 'connection refused' /var/log/example.log*.gz
```

접미사만 보지 말고 실제 타임스탬프를 기준으로 결과를 정렬하십시오. 로그에는 개인 데이터나 자격 증명이 포함될 수 있으므로 증거를 복사하기 전에 메타데이터를 보존하고 접근을 제한합니다.

:::single-choice{#general-logs-rotation-boundary} 사고가 로그 로테이션에 걸쳐 있을 때 무엇을 확인해야 합니까?

::option[새로 생성된 빈 활성 파일만 확인합니다.]{#general-logs-active-only explanation="이전 레코드는 로테이션된 아카이브로 이동했을 수 있습니다."}
::option[이벤트 시간순으로 정렬한 활성 로그와 보관 로그를 확인합니다.]{#general-logs-all-intervals .correct explanation="관련 사건 순서가 현재 파일과 로테이션된 파일에 나뉘어 있을 수 있습니다."}
::option[레코드 타임스탬프와 관계없이 파일 이름만 확인합니다.]{#general-logs-filenames-only explanation="접미사 순서와 이벤트 시간은 항상 같지 않습니다."}
:::

## 요약

이제 파일, 저널 및 로테이션 경계 전체에서 일반 로그를 조사할 수 있습니다.

1. 보편적인 파일 이름을 가정하지 말고 대상을 찾습니다.
2. 제한된 시간대를 읽고 재현 작업 중에만 추적합니다.
3. 일치하는 레코드 주변의 시간적 맥락을 보존합니다.
4. 로테이션된 아카이브를 포함하고 민감한 증거를 보호합니다.
