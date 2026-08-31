---
lesson_id: "authentication-logging"
course_id: "logging"
lang: "ko"
order_index: 5
title: "인증 로깅"
description: "리눅스 인증 레코드를 찾고 해석하며 안전하게 연관 지어 분석하는 방법을 알아봅니다."
meta_title: "인증 로깅 - 로깅"
meta_description: "/var/log/auth.log 파일을 살펴보며 리눅스 인증 로깅을 알아봅니다. 사용자 로그인 이벤트와 인증 방식을 이해하고 접근 문제를 해결해 리눅스 보안을 강화하는 방법을 설명합니다."
meta_keywords: "리눅스 인증, auth.log, 리눅스 로깅, 사용자 로그인, 리눅스 보안, 시스템 권한 부여, 로그인 문제 해결, 인증 방식, secure 로그"
---

인증 로그는 로그인 시도, 권한 변경 및 세션 활동을 설명하는 데 도움이 됩니다. 보안에 민감한 증거지만 한 줄만으로 사용자의 의도를 확정하거나 계정 침해를 입증할 수 있는 경우는 드뭅니다.

## 인증 레코드 찾기

Debian 계열 syslog 설정은 보통 인증 이벤트를 `/var/log/auth.log`로 라우팅하고, Red Hat 계열 설정은 흔히 `/var/log/secure`를 사용합니다. systemd 저널은 같은 이벤트를 유닛 및 프로세스 메타데이터와 함께 보존할 수 있으며, 중앙 로깅 시스템이 권위 있는 사본을 보관할 수도 있습니다.

로컬 대상을 찾고 관련 서비스를 조회합니다.

```bash
$ sudo journalctl -u ssh.service --since '1 hour ago'
$ sudo less /var/log/auth.log
```

SSH 유닛 이름은 `ssh.service` 또는 `sshd.service`일 수 있습니다. 이러한 레코드에는 계정과 접근 세부 정보가 드러나므로 일반적으로 권한으로 접근을 제한합니다.

:::single-choice{#auth-logs-file-location}
리눅스 인증 이벤트는 항상 어디에 저장되어야 합니까?

::option[로컬 로깅 정책이 선택한 대상입니다.]{#auth-logs-local-policy .correct explanation="파일, 저널 및 중앙 수집기는 배포판과 설정에 따라 달라집니다."}
::option[모든 배포판의 `/var/log/auth.log`입니다.]{#auth-logs-auth-only explanation="Debian 계열 시스템에서는 흔하지만 보편적인 경로는 아닙니다."}
::option[각 사용자의 셸 기록 파일 안입니다.]{#auth-logs-shell-history explanation="셸 기록은 사용자의 명령 기록이며 시스템 인증 이벤트 저장소가 아닙니다."}
:::

## 이벤트 해석하기

전통적인 레코드는 다음과 같은 내용을 담을 수 있습니다.

```text
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

이 레코드는 시간, 호스트, 이벤트를 내보낸 프로그램, PAM 모듈과 서비스, 요청한 세션 사용자 및 출발 UID를 식별합니다. 이것만으로 UID 1000 뒤의 실제 사람을 식별하거나 악의적인 작업임을 입증할 수는 없습니다. 사고 당시 유효했던 계정 레코드에서 UID를 확인하고 터미널, 원격 주소, 세션 및 주변 이벤트와 연관 지어 분석합니다.

:::single-choice{#auth-logs-uid-inference}
이 레코드에서 `uid=1000`이 확립하는 사실은 무엇입니까?

::option[root 암호가 천 번 잘못 입력됐다는 사실입니다.]{#auth-logs-thousand-passwords explanation="이 값은 시도 횟수가 아니라 숫자 식별자입니다."}
::option[작업을 시작한 프로세스와 연결된 숫자 계정 식별자입니다.]{#auth-logs-numeric-identity .correct explanation="작업을 특정 사람에게 귀속하려면 추가 세션 및 계정 증거가 필요합니다."}
::option[이벤트가 TCP 포트 1000에서 시작됐다는 사실입니다.]{#auth-logs-port explanation="UID는 네트워크 포트 필드가 아닙니다."}
:::

## 성공과 실패 조사하기

제한된 시간 범위에서 허용된 시도와 거부된 시도를 모두 검색합니다. SSH에서는 연결 소스, 인증 방식, 대상 계정, 세션 열기와 닫기 및 서비스 재시작도 조사합니다. 반복되는 실패는 사용자 실수, 오래된 자격 증명을 사용하는 자동화, 스캔 또는 공격일 수 있으며 빈도만으로 하나의 원인을 선택할 수 없습니다.

`last`와 `lastb`는 유지되고 있는 `wtmp` 및 `btmp` 레코드를 요약할 수 있지만, 이 바이너리 데이터베이스에도 자체 보존 및 무결성 한계가 있습니다. 저널 또는 syslog 레코드 및 중앙 소스와 교차 확인하십시오.

:::single-choice{#auth-logs-failed-attempts}
반복되는 로그인 실패는 어떤 정보와 연관 지어야 합니까?

::option[전체 디스크 여유 공간만 확인합니다.]{#auth-logs-disk-space explanation="용량으로는 인증 시도의 소스, 대상 또는 방식을 식별할 수 없습니다."}
::option[소스, 대상 계정, 방식, 시간 및 성공한 세션을 확인합니다.]{#auth-logs-correlated-fields .correct explanation="이 세부 정보는 잘못된 설정, 사용자 실수, 스캔 및 무단 접근을 구분하는 데 도움이 됩니다."}
::option[계정이 확실히 침해됐다는 결론과 연관 짓습니다.]{#auth-logs-certain-compromise explanation="실패에는 정상적이거나 적대적인 여러 원인이 있을 수 있습니다."}
:::

## 증거 보존 및 대응

사고가 의심되면 호스트 시간과 시간대를 기록하고 원본 로그와 메타데이터를 보존하며 내보낸 사본을 보호합니다. 증거를 원본에서 직접 편집하지 마십시오. 계정 잠금, 방화벽 변경 및 세션 종료는 정상적인 접근을 중단하거나 공격자에게 대응 사실을 알릴 수 있으므로 사고 대응 절차를 따르고 복구 경로를 유지합니다.

:::single-choice{#auth-logs-preservation}
조사 중 인증 증거는 어떻게 다뤄야 합니까?

::option[명확하게 보이도록 원본 파일의 의심스러운 줄을 편집합니다.]{#auth-logs-edit-original explanation="소스를 변경하면 증거 무결성이 훼손됩니다."}
::option[누구나 사용자를 식별할 수 있도록 전체 로그를 공개합니다.]{#auth-logs-publish explanation="인증 레코드는 민감한 신원 및 인프라 세부 정보를 노출할 수 있습니다."}
::option[원본을 보존하고 내보낸 사본을 보호합니다.]{#auth-logs-preserve .correct explanation="보안 로그에서는 무결성과 기밀성이 모두 중요합니다."}
:::

## 요약

이제 하나의 레코드가 입증하는 범위를 과장하지 않고 인증 이벤트를 조사할 수 있습니다.

1. 로컬에 설정된 인증 로그 대상을 찾습니다.
2. 맥락 속에서 신원, 서비스, 방식 및 세션 필드를 해석합니다.
3. 보존된 여러 소스에서 실패 및 성공 활동을 연관 지어 분석합니다.
4. 증거를 보존하고 운영에 영향을 주는 대응 작업을 조율합니다.
