---
lesson_id: "process-creation"
course_id: "processes"
lang: "ko"
order_index: 4
title: "프로세스 생성"
description: "fork, exec, PID, 부모 관계가 Linux 프로세스 생성에 참여하는 방식을 배웁니다."
meta_title: "프로세스 생성 - Processes"
meta_description: "Linux 프로세스 생성의 기초를 알아봅니다. fork와 execve 시스템 호출, 부모-자식 관계(PID와 PPID), init 프로세스의 역할을 배웁니다."
meta_keywords: "linux 프로세스 생성, linux에서 프로세스 만들기, 운영체제 프로세스 생성, 프로세스 생성, fork, execve, PID, PPID, init 프로세스, Linux 프로세스"
---

Linux 프로세스는 부모-자식 관계를 형성합니다. 쉘은 일반적으로 자식 프로세스를 만들고 그 자식이 요청한 프로그램을 실행하도록 준비하여 외부 명령을 시작합니다. 전통적인 설명은 이 작업을 `fork`와 `exec` 작업으로 나눕니다.

## fork로 자식 만들기

`fork()` 시스템 호출은 호출 프로세스를 기반으로 자식 프로세스를 만듭니다. 부모와 자식은 `fork`의 반환 지점부터 계속하지만 서로 다른 반환 값을 받고 서로 다른 PID를 갖습니다.

자식은 논리적으로 분리된 프로세스 상태를 받습니다. Linux는 처음에 copy-on-write로 물리 메모리 페이지를 공유하고 한 프로세스가 페이지를 수정할 때만 복사할 수 있습니다. 열린 파일 디스크립터는 상속되고 같은 기반 열린 파일 설명을 가리키므로 파일 오프셋 같은 세부 사항이 공유될 수 있습니다.

:::single-choice{#process-creation-fork-result}
성공한 `fork()`는 무엇을 만드나요?

::option[같은 프로세스 안의 대체 프로그램만 만듭니다.]{#process-creation-fork-replacement explanation="현재 프로그램 이미지를 교체하는 것은 `exec` 작업의 역할입니다."}
::option[새 PID를 가진 자식 프로세스를 만듭니다.]{#process-creation-fork-child .correct explanation="`fork()`는 별도의 자식 프로세스와 부모-자식 관계를 설정합니다."}
::option[모든 물리 메모리 페이지의 영구 사본을 즉시 만듭니다.]{#process-creation-fork-full-copy explanation="Linux는 일반적으로 모든 물리 페이지를 곧바로 복제하지 않고 copy-on-write를 사용합니다."}
:::

## execve로 프로그램 교체하기

`execve()` 호출은 호출 프로세스에 새 프로그램을 불러옵니다. 성공하면 프로세스 이미지를 교체하고 이전 프로그램으로 돌아오지 않습니다. `execve()`는 새 프로세스를 만들지 않으므로 PID는 그대로입니다.

따라서 많은 쉘 명령은 fork-exec 패턴을 따릅니다.

1. 쉘이 자식을 만듭니다.
2. 자식이 리디렉션과 다른 실행 상태를 준비합니다.
3. 자식이 요청한 프로그램을 실행합니다.
4. 포그라운드 또는 백그라운드 실행에 따라 쉘이 기다리거나 계속합니다.

라이브러리와 애플리케이션은 `posix_spawn()` 같은 상위 수준 인터페이스를 제공할 수 있고 Linux에는 `clone()` 같은 추가 기본 요소도 있습니다. 익숙한 fork-exec 모델은 유일한 인터페이스는 아니지만 여전히 유용합니다.

:::single-choice{#process-creation-exec-pid}
`execve()`가 성공하면 프로세스 PID에는 어떤 일이 생기나요?

::option[부모 PID와 같아집니다.]{#process-creation-exec-parent-pid explanation="부모와 자식은 별도의 프로세스 ID를 유지합니다."}
::option[프로그램 이미지가 교체되는 동안 그대로 유지됩니다.]{#process-creation-exec-same-pid .correct explanation="`execve()`는 다른 프로세스를 만들지 않고 호출 프로세스를 변환합니다."}
::option[새 프로그램이 시작되기 전에 제거됩니다.]{#process-creation-exec-pid-removed explanation="기존 프로세스는 새 코드, 데이터, 스택 및 관련 프로그램 상태를 가지고 같은 PID로 계속됩니다."}
:::

## 부모와 자식 ID 확인하기

`PID`는 프로세스를 식별하고 `PPID`는 부모를 식별합니다. 해당 필드를 명시적으로 요청합니다.

```bash
$ ps -o pid,ppid,stat,cmd
```

쉘이 `ps`를 시작하면 일반적으로 쉘의 PID가 해당 `ps` 프로세스의 `PPID`로 나타납니다. 시점이 중요합니다. 수명이 짧은 프로세스는 별도 관찰에서 잡기 전에 종료될 수 있습니다.

:::single-choice{#process-creation-ppid}
프로세스 목록에서 `PPID`는 무엇을 나타내나요?

::option[이전에 프로세스에 할당되었던 PID]{#process-creation-previous-pid explanation="PID는 재사용될 수 있지만 `PPID`는 식별자 기록을 저장하지 않습니다."}
::option[프로세스의 스케줄링 우선순위 식별자]{#process-creation-priority-id explanation="스케줄링 우선순위는 priority나 nice 값 같은 다른 필드로 표현됩니다."}
::option[부모 프로세스의 프로세스 ID]{#process-creation-parent-pid .correct explanation="`PPID`는 프로세스의 현재 부모 관계를 기록합니다."}
:::

## PID 1과 부모 재지정

커널은 첫 번째 사용자 공간 프로세스를 PID 1로 시작합니다. 시스템에 따라 `systemd`, 다른 init 구현 또는 컨테이너나 PID 네임스페이스 안의 작은 init일 수 있습니다. PID 1은 사용자 공간 환경의 일부를 시작하고 감독하며 특별한 시그널 및 고아 프로세스 수거 책임을 갖습니다.

부모가 자식보다 먼저 종료되면 자식은 적절한 subreaper 또는 해당 PID 네임스페이스의 init 프로세스로 부모가 재지정됩니다. 원래 부모가 끝났다는 이유만으로 종료될 필요는 없습니다.

:::single-choice{#process-creation-pid-one}
PID 1에 대한 정확한 설명은 무엇인가요?

::option[실행 파일 이름이 반드시 정확히 `init`인 프로그램이어야 합니다.]{#process-creation-pid-one-name explanation="구현은 `systemd`, 다른 init 또는 컨테이너 전용 프로그램일 수 있습니다."}
::option[현재 실행 중인 모든 프로세스를 직접 만든 부모입니다.]{#process-creation-pid-one-direct explanation="대부분의 프로세스는 여러 세대의 중간 부모를 통해 만들어집니다."}
::option[해당 PID 네임스페이스의 첫 프로세스이며 init과 같은 책임을 가집니다.]{#process-creation-pid-one-init .correct explanation="PID 1은 PID 네임스페이스 안에서 사용자 공간 프로세스 감독과 수거의 중심입니다."}
:::

[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864) 실습에서 포그라운드 및 백그라운드 명령을 실행하며 부모와 자식 ID를 관찰할 수 있습니다.

## 요약

이제 전통적인 Linux 프로세스 생성 순서를 추적할 수 있습니다.

1. `fork()`로 고유한 PID를 가진 자식을 만들 수 있습니다.
2. `execve()`로 PID를 바꾸지 않고 프로세스 이미지를 교체할 수 있습니다.
3. PID와 PPID를 읽어 부모-자식 관계를 식별할 수 있습니다.
4. PID 1과 subreaper를 부모가 재지정된 자식의 대상으로 이해할 수 있습니다.
