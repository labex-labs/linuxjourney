---
lesson_id: "system-calls"
course_id: "kernel"
lang: "ko"
order_index: 3
title: "시스템 호출"
description: "사용자 공간 코드가 리눅스 커널 서비스를 호출하는 방법과 `strace`로 호출을 안전하게 검사하는 방법을 알아봅니다."
meta_title: "시스템 호출 - 커널"
meta_description: "리눅스 시스템 호출의 기초를 살펴봅니다. 사용자 공간 프로세스가 커널 서비스를 요청하고 모드를 전환하는 방식, syscall ABI 및 strace 사용법을 설명합니다."
meta_keywords: "리눅스 시스템 호출, syscall, syscall 테이블, 커널 모드, 사용자 모드, strace, 리눅스 커널, syscall API"
---

시스템 호출은 사용자 공간 코드가 파일 열기, 메모리 매핑, 프로세스 생성 또는 네트워크 데이터 전송 같은 작업을 요청하는 정의된 커널 진입점입니다. 커널은 요청을 수행하기 전에 인수, 자격 증명, 객체 상태 및 보안 정책을 검증합니다.

## 라이브러리와 시스템 호출 ABI

애플리케이션은 아키텍처별 진입 명령어를 직접 작성하는 대신 일반적으로 C 라이브러리 함수를 호출합니다. 라이브러리 래퍼는 시스템 호출 ABI에 따라 레지스터와 메모리를 준비하고 커널에 진입한 뒤 결과를 해당 언어의 규칙에 맞게 변환합니다.

함수와 시스템 호출이 항상 일대일 관계인 것은 아닙니다.

- 라이브러리 함수 하나가 여러 시스템 호출을 결합할 수 있음
- 일부 함수는 완전히 사용자 공간에서 동작
- 최적화된 vDSO 함수는 전체 모드 전환 없이 커널이 유지하는 일부 데이터를 가져올 수 있음
- 시스템 호출 하나가 여러 상위 수준 API를 지원할 수 있음

:::single-choice{#system-calls-library-wrapper}
일반적인 libc 시스템 호출 래퍼는 무엇을 합니까?

::option[ABI 인수를 준비하고 커널에 진입한 뒤 결과를 변환합니다.]{#system-calls-wrapper-role .correct explanation="래퍼는 아키텍처별 호출 규칙을 일반 라이브러리 인터페이스 뒤에 숨깁니다."}
::option[애플리케이션에 커널 메모리의 제한 없는 접근 권한을 부여합니다.]{#system-calls-wrapper-unrestricted explanation="커널 진입은 계속 제어되며 요청을 검증합니다."}
::option[함수가 호출될 때마다 커널을 다시 컴파일합니다.]{#system-calls-wrapper-compile explanation="런타임 호출은 이미 실행 중인 커널을 사용합니다."}
:::

## 커널 진입과 반환

래퍼는 아키텍처에서 정의한 위치에 시스템 호출 번호와 인수를 배치한 다음 x86-64의 `syscall` 또는 AArch64의 `svc` 같은 진입 명령어를 실행합니다. 프로세서는 설정된 특권 진입점으로 전환하고 커널이 요청을 전달합니다.

작업을 마치면 커널은 값이나 오류 표시를 반환합니다. C 라이브러리 래퍼는 일반적으로 오류 시 `-1`을 반환하고 스레드 로컬 `errno`를 설정합니다. 다른 언어와 런타임은 서로 다른 오류 유형으로 노출합니다.

현재 아키텍처의 모든 진입을 “소프트웨어 인터럽트”라고 부르는 것은 정확하지 않습니다. 트랩, 고속 시스템 호출 명령어 및 감독자 호출은 서로 다른 방식으로 관련된 제어 전환을 구현합니다.

:::single-choice{#system-calls-entry-result}
시스템 호출의 인수와 권한을 검증하는 것은 누구입니까?

::option[프로세스 시작 전의 셸 프롬프트입니다.]{#system-calls-shell-validates explanation="프로세스는 셸과 독립적으로 시스템 호출을 수행할 수 있으며 커널 검사는 계속 필요합니다."}
::option[요청된 서비스의 커널 구현입니다.]{#system-calls-kernel-validates .correct explanation="특권 핸들러는 작업 전에 포인터, 객체 상태, 자격 증명 및 정책을 검사합니다."}
::option[디스크 파티션 테이블입니다.]{#system-calls-partition-validates explanation="저장 장치 레이아웃 메타데이터는 임의의 커널 서비스를 승인하지 않습니다."}
:::

## 번호와 호환성

시스템 호출 번호와 호출 규칙은 아키텍처별로 다릅니다. 같은 기호 호출도 다른 ABI에서는 번호나 구조 레이아웃이 다를 수 있습니다. 커널 릴리스는 새 시스템 호출을 추가할 수 있지만 안정적인 사용자 공간 ABI는 기존 동작을 보존하려고 합니다.

비특권 프로세스는 실행 중인 커널의 syscall 테이블에 임의의 새 핸들러를 삽입할 수 없습니다. 인터페이스 확장에는 커널 코드와 신중한 ABI 설계가 필요합니다. seccomp 같은 기능은 프로세스가 수행할 수 있는 호출을 필터링하지만 새 커널 구현을 만들지는 않습니다.

:::single-choice{#system-calls-number-portability}
애플리케이션이 다른 아키텍처의 syscall 번호를 하드 코딩해서는 안 되는 이유는 무엇입니까?

::option[번호와 호출 규칙이 ABI별로 다르기 때문입니다.]{#system-calls-abi-specific .correct explanation="한 아키텍처에서 의미 있는 번호가 다른 곳에서는 다른 작업을 나타내거나 존재하지 않을 수 있습니다."}
::option[시스템 호출 이름이 현재 작업 디렉터리에서 정해지기 때문입니다.]{#system-calls-directory-names explanation="경로 이름은 syscall 번호 ABI를 정의하지 않습니다."}
::option[모든 프로세스가 시작 시 임의의 syscall 테이블을 받기 때문입니다.]{#system-calls-random-table explanation="실행 중인 커널 ABI는 프로세스마다 무작위로 바뀌지 않고 아키텍처에서 안정적입니다."}
:::

## `strace`로 추적하기

간단한 명령을 추적하고 출력을 별도 파일에 저장합니다.

```bash
$ strace -o trace.log -- ls
```

권한이 있는 경우 `-f`로 자식 프로세스를 따라가거나 다음과 같은 표현식으로 출력 범위를 좁힙니다.

```bash
$ strace -f -e trace=%file -o trace.log -- command
```

`strace`에는 경로, 인수, 환경에서 파생된 데이터, 네트워크 주소, 파일 내용 일부 및 인수로 잘못 전달된 자격 증명이 나타날 수 있습니다. 추적 파일을 제한적인 권한으로 저장하고 사고 데이터 정책에 따라 제거하십시오.

:::single-choice{#system-calls-strace-purpose}
`strace`가 주로 관찰하는 것은 무엇입니까?

::option[애플리케이션 안에서 실행된 소스 코드 줄만 관찰합니다.]{#system-calls-strace-source-lines explanation="소스 수준 추적에는 심볼을 갖춘 디버거나 계측이 필요합니다."}
::option[사용자-커널 경계의 시스템 호출과 신호입니다.]{#system-calls-strace-boundary .correct explanation="추적된 프로세스의 요청, 인수, 결과 및 신호 이벤트를 보고합니다."}
::option[각 CPU 코어의 물리 전압입니다.]{#system-calls-strace-voltage explanation="하드웨어 텔레메트리는 시스템 호출 추적의 범위 밖입니다."}
:::

## 추적을 신중하게 해석하기

추적은 타이밍을 바꾸고 상당한 오버헤드를 만들 수 있습니다. 실패한 호출이 예상된 탐색일 수 있고, 최종적으로 보이는 오류는 더 이른 작업이나 애플리케이션 정책에서 비롯될 수 있습니다. 파일 디스크립터를 해석하고 프로세스 관계를 따라가며 애플리케이션 로그와 연결하십시오.

권한과 ptrace 보안 정책은 추적할 수 있는 프로세스를 제한합니다. 승인 없이 다른 사용자나 운영 프로세스에 연결하지 마십시오. 정지와 타이밍 변화가 서비스 동작에 영향을 줄 수 있습니다.

:::single-choice{#system-calls-strace-failure}
추적에서 시스템 호출 하나가 실패하면 애플리케이션이 반드시 고장 났다는 뜻입니까?

::option[그렇습니다. 0이 아닌 모든 반환은 즉시 리눅스를 종료합니다.]{#system-calls-nonzero-terminates explanation="애플리케이션은 시스템 실패 없이 시스템 호출 오류를 흔히 처리합니다."}
::option[아닙니다. 프로그램은 대안을 탐색하고 예상된 오류를 처리하는 경우가 많습니다.]{#system-calls-expected-failure .correct explanation="반환값을 따로 보지 말고 제어 흐름과 애플리케이션 맥락에서 해석해야 합니다."}
::option[그렇습니다. 커널은 예상된 오류를 절대 반환하지 않습니다.]{#system-calls-no-expected-errors explanation="없는 경로나 지원되지 않는 작업 같은 오류는 정상적인 API 결과입니다."}
:::

## 요약

이제 라이브러리 API에서 검증된 커널 작업까지 시스템 호출을 추적할 수 있습니다.

1. 상위 수준 함수와 시스템 호출 ABI를 구분합니다.
2. 아키텍처 진입 명령어를 제어된 커널 전달과 연결합니다.
3. syscall 번호와 구조를 아키텍처별 요소로 취급합니다.
4. 민감한 데이터를 보호하면서 필터링된 `strace` 출력을 사용합니다.
5. 오류와 추적 오버헤드를 애플리케이션 맥락에서 해석합니다.
