---
lesson_id: "process-states"
course_id: "processes"
lang: "ko"
order_index: 9
title: "프로세스 상태"
description: "ps 스냅샷에서 흔한 Linux 프로세스 상태 코드를 해석하는 방법을 배웁니다."
meta_title: "프로세스 상태 - Processes"
meta_description: "Linux 프로세스 상태 종합 가이드입니다. Linux의 여러 프로세스 상태(R, S, D, Z, T)와 ps 명령으로 해석하는 방법을 배웁니다."
meta_keywords: "linux 프로세스 상태, linux의 프로세스 상태, linux process state, linux 프로세스 상태 설명, ps 명령, STAT 코드, 프로세스 관리"
---

Linux 작업은 실행하고 기다리고 정지하고 종료하면서 여러 실행 상태 사이를 이동합니다. `ps`의 `STAT` 필드는 한 순간을 포착하므로 동작을 진단할 때 한 글자보다 반복 관찰이 더 유용합니다.

```bash
$ ps -o pid,ppid,stat,wchan:24,cmd
```

`STAT`의 첫 문자는 기본 상태입니다. 추가 문자는 세션 리더 또는 포그라운드 프로세스 그룹 멤버십 같은 속성을 설명하는 수정자입니다. 전체 집합은 로컬 `ps` 매뉴얼을 확인하세요.

## 실행과 중단 가능한 대기

- `R`: 실행 중 또는 실행 가능. CPU에서 실행 중이거나 CPU 시간을 기다리며 실행 큐에 있음
- `S`: 중단 가능한 대기. 이벤트를 기다리며 적절한 시그널이나 이벤트로 깨어날 수 있음

대기는 정상입니다. 대화형 프로그램과 서비스는 CPU를 계속 사용하기보다 입력, 타이머, 네트워크 트래픽, 잠금 또는 다른 이벤트를 기다리는 데 많은 시간을 보냅니다.

:::single-choice{#process-states-runnable-code}
기본 상태 `R`은 무엇을 뜻하나요?

::option[CPU에서 실행 중이거나 실행할 준비가 됨]{#process-states-r-running .correct explanation="`R`은 현재 실행 중인 작업과 CPU 서비스를 기다리는 실행 가능 작업을 함께 나타냅니다."}
::option[부모가 상태를 수집한 뒤 수거됨]{#process-states-r-reaped explanation="완전히 수거된 프로세스는 더 이상 일반 프로세스 테이블 항목으로 나타나지 않습니다."}
::option[중단 불가능한 대기 중]{#process-states-r-uninterruptible explanation="중단 불가능한 대기는 `D`로 표현됩니다."}
:::

:::single-choice{#process-states-interruptible-code}
중단 가능한 대기를 나타내는 기본 상태는 무엇인가요?

::option[`D`]{#process-states-sleep-d explanation="`D`는 중단 불가능한 대기를 나타냅니다."}
::option[`Z`]{#process-states-sleep-z explanation="`Z`는 상태가 수거되지 않은 종료 자식을 나타냅니다."}
::option[`S`]{#process-states-sleep-s .correct explanation="`S`는 중단 가능한 기다리기를 나타내는 일반적인 `ps` 코드입니다."}
:::

## 중단 불가능한 대기

`D`는 중단 불가능한 대기를 뜻하며 흔히 일부 저장소나 네트워크 파일 시스템 입출력 같은 커널 작업을 기다릴 때 나타납니다. 작업은 그 대기에서 나올 때까지 일반 시그널에 반응하지 않으며 시그널은 그동안 대기 상태로 남을 수 있습니다.

짧은 `D` 상태는 정상일 수 있습니다. 지속되거나 많은 `D` 작업은 느리거나 사용할 수 없거나 결함 있는 입출력을 나타낼 수 있지만 상태만으로 원인을 식별하지 못합니다. 결론을 내리기 전에 대기 채널, 커널 로그, 저장소 및 네트워크 상태, 관련 하위 시스템을 확인하세요.

:::single-choice{#process-states-uninterruptible-code}
중단 불가능한 대기를 나타내는 기본 상태는 무엇인가요?

::option[`T`]{#process-states-d-stopped explanation="`T`는 정지된 작업을 식별합니다."}
::option[`D`]{#process-states-d-uninterruptible .correct explanation="`D`는 중단 불가능한 커널 대기 중인 작업에 사용됩니다."}
::option[`R`]{#process-states-d-runnable explanation="`R`은 실행 중이거나 실행 가능한 작업을 식별합니다."}
:::

## 정지 및 좀비 상태

- `T`: 일반적으로 `SIGTSTP` 같은 작업 제어 동작이나 `SIGSTOP`으로 정지됨. 일부 도구는 추적 정지에 소문자 `t`를 사용
- `Z`: 좀비. 프로세스는 종료했지만 부모가 종료 레코드를 아직 수집하지 않음

적절한 경우 `SIGCONT`로 작업 제어 정지를 재개합니다. 좀비는 더 이상 실행하지 않으므로 재개하거나 종료할 수 없습니다. 부모나 입양한 수거 프로세스가 수집해야 합니다.

:::single-choice{#process-states-zombie-code}
기본 상태 `Z`는 무엇을 식별하나요?

::option[종료했으며 종료 레코드가 수거를 기다리는 프로세스]{#process-states-z-zombie .correct explanation="좀비는 실행이 끝난 뒤 부모에게 보이는 최소 상태를 유지합니다."}
::option[터미널 일시 중단 시그널로 일시 정지된 프로세스]{#process-states-z-terminal-stop explanation="작업 제어 정지는 일반적으로 `T`로 표시됩니다."}
::option[현재 CPU 코어 하나를 모두 사용하는 프로세스]{#process-states-z-cpu explanation="활발히 실행 중인 작업은 `R`로 나타나고 좀비는 명령을 실행하지 않습니다."}
:::

## 문맥 속에서 상태 읽기

상태 코드는 진단이 아니라 관찰 결과입니다. 경과 시간, CPU 사용량, 대기 채널, 부모 관계, 로그, 반복 표본과 함께 사용하세요. 커널이 보고하는 순간과 화면을 읽는 순간 사이에도 작업 상태가 바뀔 수 있습니다.

[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864) 실습은 포그라운드, 대기, 정지, 종료 작업을 관찰할 수 있는 안전한 환경을 제공합니다.

## 요약

이제 가장 흔한 기본 프로세스 상태를 해석할 수 있습니다.

1. `R`을 실행 중 또는 실행 가능, `S`를 중단 가능한 대기로 읽을 수 있습니다.
2. 지속되는 `D`를 진단이 아니라 대기 증상으로 조사할 수 있습니다.
3. 정지된 `T`와 종료했지만 수거되지 않은 `Z`를 구분할 수 있습니다.
4. 반복 관찰과 주변 증거를 사용할 수 있습니다.
