---
lesson_id: "process-threads"
course_id: "process-utilization"
lang: "ko"
order_index: 3
title: "프로세스 스레드"
description: "리눅스 스레드가 프로세스 리소스를 공유하는 방식과 ps로 검사하는 방법을 알아봅니다."
meta_title: "프로세스 스레드 - 프로세스 사용량"
meta_description: "리눅스 프로세스 스레드를 알아봅니다. 단일 스레드와 다중 스레드 프로세스의 차이 및 ps 명령으로 스레드를 표시하는 방법을 설명합니다."
meta_keywords: "리눅스 스레드, 프로세스 스레드, ps 스레드 표시, 다중 스레드, 단일 스레드, 경량 프로세스, 리눅스 프로세스 관리"
---

스레드는 프로세스 안에서 스케줄링되는 실행 흐름입니다. 실행 중인 모든 프로세스에는 스레드가 하나 이상 있으며 다중 스레드 프로세스에는 동시에 진행할 수 있는 여러 흐름이 있습니다.

## 프로세스와 스레드

한 프로세스의 스레드는 가상 주소 공간과 열린 파일 디스크립터 같은 리소스를 공유합니다. 각 스레드는 레지스터와 스택을 포함한 자체 실행 상태도 가집니다. 공유하면 효율적으로 통신할 수 있지만 한 스레드의 동기화되지 않은 변경이 다른 스레드에 영향을 줄 수도 있습니다.

별도의 프로세스는 일반적으로 서로 다른 주소 공간을 가지며 명시적인 프로세스 간 메커니즘으로 통신합니다. 어느 설계도 자동으로 더 빠르거나 안전하지는 않습니다. 작업 부하와 구현에 따라 절충이 결정됩니다.

:::single-choice{#threads-shared-resource}
같은 프로세스의 스레드가 일반적으로 공유하는 리소스는 무엇입니까?

::option[프로세스 가상 주소 공간입니다.]{#threads-shared-address-space .correct explanation="프로그램이 적절히 동기화하면 스레드들이 같은 프로세스 메모리에 접근할 수 있습니다."}
::option[스레드마다 별도의 커널 설치입니다.]{#threads-separate-kernel explanation="모든 스레드는 실행 중인 시스템 커널을 사용합니다."}
::option[스레드마다 서로 다른 파일 시스템 루트입니다.]{#threads-different-root explanation="스레드는 일반적으로 별도 루트를 받지 않고 프로세스 파일 시스템 컨텍스트를 공유합니다."}
:::

## 스레드 식별자

리눅스는 각 스레드를 자체 스레드 ID를 가진 스케줄 가능한 작업으로 표현합니다. 스레드 그룹 리더의 ID는 일반적으로 프로세스 ID로 표시되며 모든 멤버가 스레드 그룹 ID를 공유합니다. 도구는 `PID`, `TID`, `LWP` 및 `SPID` 같은 레이블을 사용합니다. 모든 레이블의 의미가 같다고 가정하지 말고 도구의 필드 정의를 확인하십시오.

:::single-choice{#threads-own-scheduling-state}
각 스레드가 독립적으로 유지하는 것은 무엇입니까?

::option[프로세스의 전체 열린 파일 표입니다.]{#threads-open-files-shared explanation="한 프로세스의 스레드는 일반적으로 열린 파일 디스크립터를 공유합니다."}
::option[시스템 전체 사용자 데이터베이스입니다.]{#threads-user-database explanation="계정 데이터베이스는 비공개 스레드 상태가 아닙니다."}
::option[자체 실행 상태와 스택입니다.]{#threads-stack-state .correct explanation="프로세스 리소스를 공유해도 스레드에는 자체 실행 컨텍스트가 필요합니다."}
:::

## ps로 스레드 나열하기

모호한 기본 레이아웃을 피하려면 출력 필드를 명시합니다.

```bash
$ ps -eLo pid,tid,psr,stat,comm
```

procps `ps`에서 `-L`은 스레드를 표시하고 `-e`는 모든 프로세스를 선택합니다. `pid`는 스레드 그룹을, `tid`는 개별 스레드를 식별합니다. `psr`은 마지막으로 실행된 CPU를, `stat`은 상태를 보고합니다. 프로세스 하나를 검사합니다.

```bash
$ ps -L -p 1234 -o pid,tid,stat,pcpu,comm
```

스레드 목록은 스냅샷입니다. 스레드는 그 직후 종료되거나 상태가 바뀔 수 있습니다.

:::single-choice{#threads-ps-one-process}
명시적인 필드로 PID 1234에 속한 스레드를 나열하는 명령은 무엇입니까?

::option[`ps -p 1234 -o pid,ppid,stat,pcpu,comm`]{#threads-process-only explanation="이 출력은 스레드별 행을 요청하지 않습니다."}
::option[`ps -L -p 1234 -o pid,tid,stat,pcpu,comm`]{#threads-ps-l .correct explanation="`-L` 옵션은 선택한 프로세스의 스레드 행을 요청합니다."}
::option[`ps -e -o pid,user,stat,pcpu,comm`]{#threads-all-processes explanation="스레드 ID 없이 시스템 전체 프로세스를 선택합니다."}
:::

## 스레드 활동 해석하기

스레드 하나의 높은 CPU 사용량이 프로세스 전체 평균에 가려질 수 있습니다. 스레드 수준 CPU 표본을 애플리케이션 로그, 스택 추적 및 프로파일링 도구와 결합하십시오. 일시 정지, 권한 및 서비스 영향을 이해하지 않고 운영 작업에 디버거를 연결하거나 신호를 보내지 마십시오.

:::single-choice{#threads-snapshot-limit}
`ps` 스레드 목록을 영구 상태로 취급해서는 안 되는 이유는 무엇입니까?

::option[`ps`가 행마다 대체 스레드를 만들기 때문입니다.]{#threads-ps-creates explanation="이 명령은 작업을 관찰하며 나열한 작업을 복제하지 않습니다."}
::option[모든 리눅스 호스트에서 스레드 ID가 같기 때문입니다.]{#threads-identical-ids explanation="식별자는 실행 중인 시스템 안에서 배정되며 보편적이지 않습니다."}
::option[스레드가 스냅샷 후 상태를 바꾸거나 종료할 수 있기 때문입니다.]{#threads-change-after-snapshot .correct explanation="프로세스 검사는 계속 변하는 시스템의 한 순간을 관찰합니다."}
:::

## 요약

이제 프로세스 리소스와 스레드별 실행 상태를 구분할 수 있습니다.

1. 모든 프로세스에 스레드가 하나 이상 있음을 이해합니다.
2. 한 프로세스의 스레드가 공유하는 리소스를 식별합니다.
3. `ps -L`로 명시적인 프로세스 및 스레드 ID를 나열합니다.
4. 스레드 출력을 스냅샷으로 취급하고 다른 증거와 연결합니다.
