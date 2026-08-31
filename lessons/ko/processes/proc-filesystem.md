---
lesson_id: "proc-filesystem"
course_id: "processes"
lang: "ko"
order_index: 10
title: "/proc 파일 시스템"
description: "Linux가 가상 /proc 파일 시스템을 통해 살아 있는 프로세스와 커널 정보를 노출하는 방법을 배웁니다."
meta_title: "/proc 파일 시스템 - Processes"
meta_description: "커널과 실행 중인 프로세스를 대시보드처럼 보여 주는 가상 디렉터리인 Linux /proc 파일 시스템을 알아봅니다. 표준 명령 이상의 프로세스 세부 정보에 접근하는 방법을 배웁니다."
meta_keywords: "/proc 파일 시스템, linux proc, 프로세스 정보, linux proc 추가 정보, 시스템 대시보드, Linux 프로세스, 커널 정보"
---

Linux는 일반적으로 `procfs`를 `/proc`에 마운트합니다. 이 가상 파일 시스템은 커널이 생성한 인터페이스를 파일과 디렉터리로 나타내며 내용은 디스크에 저장된 일반 영구 파일이 아닙니다. 프로세스 상태와 선택된 시스템 전체 커널 정보를 노출합니다.

## 프로세스 디렉터리 찾기

마운트와 최상위 항목을 나열합니다.

```bash
$ findmnt /proc
$ ls /proc
```

숫자 디렉터리 이름은 호출자의 PID 네임스페이스에서 보이는 프로세스 ID에 대응합니다. 예를 들어 `/proc/12345`는 존재하는 순간의 PID 12345를 나타냅니다. `/proc/self`는 관찰 프로세스 자체 디렉터리로 해석되는 심볼릭 링크이고 `/proc/thread-self`는 현재 스레드를 식별합니다.

가시성과 접근은 자격 증명, 네임스페이스, 보안 정책, `hidepid` 같은 procfs 마운트 옵션에 따라 달라집니다. 디렉터리를 나열한 뒤 파일을 열기 전에 프로세스가 종료될 수 있으므로 사라짐은 검사 도구가 처리해야 하는 정상적인 경쟁 조건입니다.

:::single-choice{#proc-filesystem-numeric-directory}
숫자 디렉터리 `/proc/12345`는 일반적으로 무엇을 나타내나요?

::option[번호가 12345인 디스크 블록]{#proc-filesystem-disk-block explanation="`/proc`는 원시 디스크 블록 디렉터리가 아니라 가상 커널 인터페이스입니다."}
::option[현재 PID 12345로 보이는 프로세스]{#proc-filesystem-pid-directory .correct explanation="프로세스별 procfs 데이터는 보이는 PID 이름의 디렉터리 아래에 모입니다."}
::option[UID가 12345인 사용자 계정]{#proc-filesystem-user-directory explanation="숫자 최상위 프로세스 디렉터리는 UID가 아니라 PID를 기준으로 합니다."}
:::

## 프로세스 정보 읽기

권한이 허용하면 프로세스 상태 파일을 검사합니다.

```bash
$ less /proc/12345/status
```

프로세스 이름, 상태, ID, 자격 증명, 메모리 카운터, capabilities, 시그널 마스크 같은 필드가 있습니다. 다른 유용한 항목은 다음과 같습니다.

- `/proc/12345/cmdline`: null 바이트로 구분된 명령줄 인자
- `/proc/12345/environ`: 접근이 제어되고 민감할 수 있는 환경 항목
- `/proc/12345/fd/`: 열린 파일 디스크립터를 나타내는 심볼릭 링크
- `/proc/12345/maps`: 현재 메모리 매핑
- `/proc/12345/cwd`: 현재 작업 디렉터리를 가리키는 심볼릭 링크

이를 변화하는 관찰 결과로 다루세요. 커널 버전에 따라 필드가 다르고 여러 파일을 읽는 동안 프로세스 상태가 바뀔 수 있으며 일부 카운터에는 이름만으로 알 수 없는 미묘한 의미가 있습니다.

:::single-choice{#proc-filesystem-status-file}
PID 12345의 읽기 가능한 필드 중심 요약이 있는 경로는 무엇인가요?

::option[`/proc/status/12345`]{#proc-filesystem-status-reversed explanation="프로세스별 파일은 최상위 `status` 디렉터리가 아니라 PID 이름 디렉터리 안에 있습니다."}
::option[`/proc/12345/status`]{#proc-filesystem-process-status .correct explanation="프로세스별 `status` 인터페이스는 식별자, 상태, 메모리, 시그널, 자격 증명 필드를 제공합니다."}
::option[`/proc/cpuinfo/12345`]{#proc-filesystem-cpuinfo-pid explanation="`/proc/cpuinfo`는 시스템 전체 인터페이스이며 PID별 상태 파일 디렉터리가 아닙니다."}
:::

## 시스템 전체 인터페이스 읽기

모든 `/proc` 항목이 프로세스에 속하는 것은 아닙니다.

- `/proc/cpuinfo`: 커널이 보고한 CPU 정보
- `/proc/meminfo`: 시스템 메모리 카운터
- `/proc/mounts`: 현재 프로세스가 보는 마운트
- `/proc/loadavg`: 부하 평균과 실행 가능 작업 정보
- `/proc/sys/`: 런타임 커널 매개변수

특히 `/proc/sys` 아래 일부 파일은 쓰기 가능한 구성 인터페이스입니다. 일반 파일처럼 보인다는 이유로 쓰지 마세요. 승인된 시스템 변경 전에 매개변수, 범위, 지속 방식, 롤백을 이해하세요.

:::single-choice{#proc-filesystem-system-interface}
프로세스 하나의 상태가 아니라 시스템 전체 메모리 카운터를 제공하는 항목은 무엇인가요?

::option[`/proc/self/status`]{#proc-filesystem-self-status explanation="관찰 프로세스 자체의 프로세스별 상태로 해석됩니다."}
::option[`/proc/meminfo`]{#proc-filesystem-memory-info .correct explanation="`meminfo`는 커널이 보고한 시스템 메모리 통계를 포함합니다."}
::option[`/proc/1/fd`]{#proc-filesystem-one-fd explanation="접근 제어에 따라 PID 1에 속한 파일 디스크립터를 나타냅니다."}
:::

## 도구를 통해 /proc 사용하기

`ps`, `top`, `free` 같은 Linux 도구 구현은 procfs와 다른 커널 인터페이스에서 많은 데이터를 얻은 뒤 레이블을 붙이고 계산하고 서식을 지정합니다. 필요한 필드를 제공한다면 일상 작업에는 해당 도구를 선호하세요. 특정 세부 정보나 스크립팅을 위해 `/proc`을 직접 읽을 때는 먼저 인터페이스 문서를 확인합니다.

직접 읽는 프로그램은 형식을 올바르게 분석하고 사라진 프로세스를 허용하며 민감한 출력을 보호하고 읽기 한 번이 원자적인 시스템 스냅샷이라고 가정하지 않아야 합니다.

:::single-choice{#proc-filesystem-live-data}
검사 명령 두 개 사이에 `/proc/PID`가 사라질 수 있는 이유는 무엇인가요?

::option[모든 procfs 파일은 매초 자동으로 이름이 바뀝니다.]{#proc-filesystem-renamed explanation="모든 procfs 항목에 주기적인 이름 변경 규칙은 없습니다."}
::option[`status`를 읽으면 프로세스 디렉터리가 삭제됩니다.]{#proc-filesystem-read-delete explanation="상태 검사는 읽기 전용이며 프로세스를 종료하거나 제거하지 않습니다."}
::option[관찰하는 동안 프로세스가 종료될 수 있습니다.]{#proc-filesystem-process-exit .correct explanation="Procfs는 살아 있는 상태를 반영하므로 프로세스가 사라지면 커널이 프로세스별 디렉터리를 제거합니다."}
:::

## 요약

이제 procfs를 살아 있고 접근이 제어되는 커널 인터페이스로 사용할 수 있습니다.

1. 숫자 `/proc` 디렉터리를 보이는 PID와 연결할 수 있습니다.
2. 경쟁 조건과 민감성을 고려하며 선택한 프로세스별 파일을 읽을 수 있습니다.
3. 프로세스 디렉터리와 시스템 전체 인터페이스를 구분할 수 있습니다.
4. 신뢰할 수 있는 일상 검사에는 문서화된 도구와 형식을 선호할 수 있습니다.
