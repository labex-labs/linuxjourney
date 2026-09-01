---
lesson_id: "system-logging"
course_id: "logging"
lang: "ko"
order_index: 1
title: "시스템 로깅"
description: "리눅스 로그 소스, 수집기, 저장소 및 조회 도구가 서로 어떻게 연결되는지 알아봅니다."
meta_title: "시스템 로깅 - 로깅"
meta_description: "시스템 로깅을 통해 리눅스를 배우는 효과적인 방법을 알아봅니다. syslog, rsyslogd 및 /var/log에서 로그 파일을 찾고 읽는 방법을 설명합니다."
meta_keywords: "리눅스 배우는 방법, 리눅스 시스템 로깅, syslog, rsyslogd, var log, 시스템 로그, 리눅스 명령줄"
---

로그는 커널, 서비스, 애플리케이션 및 보안 구성 요소가 내보낸 이벤트를 기록합니다. 문제 해결과 감사에 유용하지만, 수집이 정상적으로 작동하고 타임스탬프를 올바르게 이해하며 관련 소스가 포함되어 있을 때만 의미가 있습니다.

## 로그 메시지의 흐름

로깅 경로는 몇 가지 서로 다른 부분으로 구성됩니다.

1. 소스가 이벤트를 내보냅니다.
2. 수집기가 이벤트를 받아 부가 정보를 추가합니다.
3. 라우팅 및 보존 규칙이 저장 또는 전달 대상을 선택합니다.
4. 조회 도구가 저장된 레코드를 검색합니다.

systemd 호스트에서는 일반적으로 `systemd-journald`가 서비스의 표준 출력, 커널 메시지, 저널 네이티브 메시지 또는 syslog 메시지를 수집합니다. rsyslog 같은 syslog 데몬도 메시지를 받아 전통적인 텍스트 파일에 쓰거나 다른 곳으로 전달할 수 있습니다. 애플리케이션이 자체 파일이나 외부 텔레메트리를 직접 관리하기도 합니다.

:::single-choice{#system-logging-distinct-roles} 수신한 메시지를 어디에 저장하거나 전달할지 결정하는 구성 요소는 무엇입니까?

::option[터미널의 현재 작업 디렉터리입니다.]{#system-logging-cwd explanation="셸 디렉터리는 시스템 전체 로깅 경로를 정의하지 않습니다."}
::option[실행 중인 커널 이미지의 파일 이름입니다.]{#system-logging-kernel-file explanation="커널은 메시지를 내보낼 수 있지만 이미지 파일 이름은 라우팅 정책이 아닙니다."}
::option[라우팅 및 보존 설정입니다.]{#system-logging-routing .correct explanation="수집과 저장 사이의 규칙이 대상과 보존 동작을 결정합니다."}
:::

## 사용 가능한 로그 찾기

모든 호스트에 같은 파일이 있다고 가정하지 마십시오. 활성 로깅 서비스와 로컬 설정을 조사합니다.

```bash
$ systemctl --type=service --state=running | grep -E 'journal|syslog'
$ ls -la /var/log
$ journalctl --disk-usage
```

`/var/log/syslog`는 호환되는 라우팅을 사용하는 Debian 계열 시스템에서 흔하고, `/var/log/messages`는 다른 배포판에서 흔합니다. 저널만 사용하는 호스트에는 어느 파일도 없을 수 있습니다. 애플리케이션 문서와 유닛 설정에서 추가 대상을 확인할 수 있습니다.

:::single-choice{#system-logging-file-absence} `/var/log/syslog` 파일이 없다는 사실이 반드시 뜻하는 것은 무엇입니까?

::option[호스트가 설정된 다른 로깅 대상을 사용할 수 있습니다.]{#system-logging-other-destination .correct explanation="저널 전용 시스템과 다른 syslog 정책은 이 파일을 만들 필요가 없습니다."}
::option[커널이 지금까지 메시지를 한 번도 생성하지 않았습니다.]{#system-logging-no-kernel explanation="커널 레코드는 저널이나 다른 대상에 있을 수 있습니다."}
::option[모든 애플리케이션이 중지됐습니다.]{#system-logging-apps-stopped explanation="경로 하나가 없다는 사실만으로 애플리케이션 상태를 판단할 수 없습니다."}
:::

## 저널 조회하기

전체 저널을 한꺼번에 출력하지 말고 범위가 제한된 쿼리부터 시작합니다.

```bash
$ journalctl -b -p warning
$ journalctl -u ssh.service --since '1 hour ago'
```

`-b`는 현재 부팅을 선택하고, `-p`는 우선순위로 필터링하며, `-u`는 유닛으로 필터링합니다. 유닛 이름과 보존된 부팅 기록은 호스트마다 다릅니다. `journalctl --list-boots`로 사용 가능한 부팅을 확인하고, 문제를 재현하면서 `journalctl -f`로 새 레코드를 추적합니다.

:::single-choice{#system-logging-current-boot} `journalctl` 쿼리를 현재 부팅으로 제한하는 옵션은 무엇입니까?

::option[`-b`]{#system-logging-boot-option .correct explanation="인수를 지정하지 않은 부팅 선택자는 현재 부팅을 선택합니다."}
::option[`-u`]{#system-logging-unit-option explanation="systemd 유닛으로 필터링하는 옵션입니다."}
::option[`-f`]{#system-logging-follow-option explanation="새로 추가되는 레코드를 계속 추적하는 옵션입니다."}
:::

## 맥락 속에서 레코드 읽기

전통적인 syslog 형식의 한 줄은 다음과 같습니다.

```text
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

이 레코드는 타임스탬프, 호스트, 프로그램과 PID, 메시지를 담고 있습니다. 메시지 텍스트는 애플리케이션 출력이므로 구조화된 사실로 보장된다고 간주하지 마십시오. 시간대, 시계 동기화, 부팅 ID, PID 재사용 및 이벤트 직전과 직후 레코드를 확인합니다. 저널 필드는 렌더링된 텍스트만으로 얻는 것보다 강한 식별자를 제공할 수 있습니다.

로그에는 사용자 이름, 주소, 경로, 토큰 또는 기타 민감한 데이터가 포함될 수 있습니다. 최소 권한으로 접근하고, 외부로 내보내는 자료는 비식별화하며, 조사 중에는 원본과 타임스탬프를 보존하십시오.

:::single-choice{#system-logging-export-safety} 로그 일부를 외부에 공유하기 전에 무엇을 해야 합니까?

::option[모든 타임스탬프를 임의의 값으로 바꿉니다.]{#system-logging-random-time explanation="시간 정보를 훼손하면 상관관계를 찾지 못할 수 있으며 올바른 비식별화 방법이 아닙니다."}
::option[비밀 정보와 민감한 식별자가 있는지 검토합니다.]{#system-logging-review-sensitive .correct explanation="로그에는 통제된 비식별화가 필요한 운영 또는 개인 데이터가 자주 포함됩니다."}
::option[원본 로그를 누구나 쓸 수 있게 만듭니다.]{#system-logging-world-writable explanation="접근 제어를 약화하면 무결성을 훼손하고 추가 데이터를 노출할 수 있습니다."}
:::

## 요약

이제 보편적인 저장 경로 하나를 가정하지 않고 리눅스 로그를 찾고 조회할 수 있습니다.

1. 이벤트 소스, 수집기, 라우팅, 저장소 및 조회 도구를 구분합니다.
2. 호스트의 활성 로깅 설정을 확인합니다.
3. 유닛, 부팅, 시간 또는 우선순위로 범위를 제한한 저널 쿼리를 사용합니다.
4. 맥락 속에서 레코드의 상관관계를 찾고 민감한 로그 데이터를 보호합니다.
