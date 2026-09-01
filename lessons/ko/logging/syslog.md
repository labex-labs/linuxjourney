---
lesson_id: "syslog"
course_id: "logging"
lang: "ko"
order_index: 2
title: "syslog"
description: "syslog 퍼실리티, 심각도, 라우팅 규칙 및 logger 명령의 동작 방식을 알아봅니다."
meta_title: "syslog - 로깅"
meta_description: "리눅스의 syslog와 rsyslog, 시스템 로그 관리 및 logger 명령 사용법을 초보자도 쉽게 알아봅니다."
meta_keywords: "syslog, rsyslog, 리눅스 로그, logger 명령, /var/log/syslog, 리눅스 튜토리얼, 시스템 로깅"
---

Syslog는 많은 유닉스 계열 시스템에서 사용하는 메시지 모델과 전송 규약을 정의합니다. Rsyslog는 메시지를 수신, 필터링, 변환, 저장 및 전달할 수 있는 구현체 중 하나입니다. `systemd-journald`와 함께 사용할 수도 있으며, 어느 이름도 모든 애플리케이션이 그 경로를 사용한다는 뜻은 아닙니다.

## 퍼실리티와 심각도

syslog 메시지는 대략적인 소스 범주를 설명하는 퍼실리티와 emergency부터 debug까지의 심각도를 가집니다. 흔한 퍼실리티에는 `auth`, `cron`, `daemon`, `kern`, `mail`, `user` 및 `local0`부터 `local7`까지가 있습니다.

심각도에는 순서가 있습니다. 고전적인 선택자 구문에서 `daemon.warning`은 일반적으로 warning뿐 아니라 daemon의 warning 이상으로 심각한 모든 메시지와 일치합니다. 고전 구문을 지원하는 구현체에서는 `daemon.=warning`처럼 등호 한정자를 사용해 정확히 일치시킬 수 있습니다.

:::single-choice{#syslog-warning-selector} `daemon.warning` 같은 고전적인 선택자는 일반적으로 무엇과 일치합니까?

::option[텍스트에 daemon이라는 단어가 있는 메시지만 일치합니다.]{#syslog-text-daemon explanation="메시지 텍스트 검색이 아니라 퍼실리티 메타데이터가 이 선택자를 결정합니다."}
::option[모든 퍼실리티의 모든 debug 메시지와 일치합니다.]{#syslog-all-debug explanation="이 선택자는 daemon 퍼실리티와 심각도 임계값으로 제한됩니다."}
::option[warning 및 그보다 심각한 daemon 메시지와 일치합니다.]{#syslog-warning-or-higher .correct explanation="우선순위 선택자는 지정한 심각도와 긴급도가 더 높은 수준을 포함합니다."}
:::

## rsyslog 규칙 읽기

Rsyslog는 일반적으로 주 설정 파일과 `/etc/rsyslog.d/` 아래의 조각 파일을 불러옵니다. 전통적인 규칙은 선택자와 그 뒤의 동작으로 구성됩니다.

```text
auth,authpriv.*          /var/log/auth.log
*.*;auth,authpriv.none  -/var/log/syslog
kern.*                  /var/log/kern.log
```

첫째 줄은 두 인증 퍼실리티의 모든 우선순위를 라우팅합니다. 둘째 줄은 메시지를 광범위하게 선택하되 해당 퍼실리티를 제외합니다. 셋째 줄은 커널 퍼실리티 메시지를 라우팅합니다. 파일 동작 앞의 `-`는 일반적으로 비동기 쓰기를 요청하며 제외를 뜻하지 않습니다.

프로덕션 라우팅을 변경하기 전에 포함된 모든 파일을 검사하고 설치된 버전에서 사용하는 정확한 구문을 검증하십시오.

:::single-choice{#syslog-selector-action} 전통적인 rsyslog 규칙에서 동작은 어느 부분입니까?

::option[왼쪽의 퍼실리티 및 심각도 표현식입니다.]{#syslog-left-selector explanation="이 부분은 메시지를 선택합니다."}
::option[오른쪽의 대상 또는 작업입니다.]{#syslog-right-action .correct explanation="동작은 선택된 레코드를 파일, 원격 대상 또는 다른 출력 중 어디로 보낼지 결정합니다."}
::option[패키지 버전을 설명하는 주석입니다.]{#syslog-comment-version explanation="주석은 메시지를 라우팅하지 않습니다."}
:::

## 테스트 메시지 보내기

`logger`를 사용해 식별 가능한 태그와 우선순위가 있는 통제된 테스트 메시지를 전송합니다.

```bash
$ logger -p user.notice -t lesson-test 'routing check 2026-08-31T10:00'
```

그런 다음 예상 대상을 조회합니다.

```bash
$ journalctl -t lesson-test --since '5 minutes ago'
```

전달 및 라우팅 설정에 따라 같은 이벤트가 저널과 텍스트 파일에 모두 나타날 수 있습니다. `logger -s`는 메시지를 표준 오류에도 복사할 뿐, 영구 저장을 입증하지는 않습니다.

:::single-choice{#syslog-logger-tag} `logger -t lesson-test`는 전송하는 메시지에 무엇을 추가합니까?

::option[오래된 테스트 레코드를 지우라는 요청을 추가합니다.]{#syslog-tag-delete explanation="이 옵션은 식별 태그를 설정하며 보존을 관리하지 않습니다."}
::option[메시지 태그로 `lesson-test` 식별자를 추가합니다.]{#syslog-tag-identifier .correct explanation="고유한 태그를 사용하면 설정된 대상에서 통제된 이벤트를 쉽게 찾을 수 있습니다."}
::option[5분의 전송 지연을 추가합니다.]{#syslog-tag-delay explanation="태그 옵션에는 전송 간격이 인코딩되지 않습니다."}
:::

## 라우팅 변경 및 검증

변경 전에 현재 설정을 보관하고 하위 소비자를 파악합니다. 구현체의 설정 검사 모드로 구문을 검증하십시오. 일반적인 명령은 다음과 같습니다.

```bash
$ sudo rsyslogd -N1
```

검증을 통과한 뒤에만 서비스 관리자를 통해 서비스를 다시 불러와야 합니다. 새 태그 메시지를 보내고, 필요한 모든 대상에서 확인하며, 서비스 상태와 내부 오류 로그를 검사합니다. 구문이 유효한 규칙도 범위를 지나치게 넓게 설정하거나 레코드를 중복시키거나 민감한 데이터를 노출할 수 있습니다.

신뢰할 수 없는 네트워크를 통과해 원격으로 전달할 때는 인증되고 암호화된 전송을 사용해야 합니다. UDP 전송에는 종단 간 확인 응답이 없습니다. 중요한 감사 요구 사항에는 큐, 손실, 무결성, 접근 제어 및 수신기 장애를 고려한 설계가 필요합니다.

:::single-choice{#syslog-change-verification} 새 라우팅 규칙이 작동한다는 충분한 증거는 무엇입니까?

::option[설정 파일의 수정 시간이 최근입니다.]{#syslog-mtime explanation="타임스탬프만으로는 구문 유효성이나 전송을 입증할 수 없습니다."}
::option[송신자가 ping으로 수신자에 도달할 수 있습니다.]{#syslog-ping explanation="네트워크 연결만으로는 로깅 프로토콜이나 저장 경로를 검증할 수 없습니다."}
::option[검증을 통과하고 태그가 있는 테스트가 모든 의도한 대상에 도달합니다.]{#syslog-validate-and-test .correct explanation="정적 검증과 관찰된 종단 간 이벤트가 모두 필요합니다."}
:::

## 요약

이제 메시지 메타데이터부터 설정된 대상까지 syslog 라우팅을 테스트할 수 있습니다.

1. 퍼실리티와 순서가 있는 심각도 수준을 구분합니다.
2. 선택자와 동작을 분리해 읽습니다.
3. `logger`로 태그와 우선순위가 지정된 이벤트를 보냅니다.
4. 설정을 검증하고 전송을 종단 간 확인합니다.
