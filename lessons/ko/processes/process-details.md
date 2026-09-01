---
lesson_id: "process-details"
course_id: "processes"
lang: "ko"
order_index: 3
title: "프로세스 세부 정보"
description: "실행 중인 프로세스와 디스크에 저장된 프로그램을 구분하는 상태와 자원을 배웁니다."
meta_title: "프로세스 세부 정보 - Processes"
meta_description: "Linux 프로세스 세부 정보의 기초를 알아봅니다. 프로세스란 무엇인지, Linux 커널이 프로세스를 관리하고 CPU와 메모리 같은 시스템 자원을 할당하는 방법을 배웁니다."
meta_keywords: "Linux 프로세스, 프로세스 세부 정보, 커널, 프로세스 관리, 시스템 자원, ps aux, CPU, 메모리, Linux 튜토리얼, 초보자 가이드"
---

프로그램은 파일에 저장된 실행 코드와 데이터입니다. 프로세스는 살아 있는 실행 문맥으로 매핑된 코드, 메모리, 자격 증명, 열린 파일 디스크립터, 시그널 상태, 스케줄링 정보, 하나 이상의 스레드를 포함합니다. 같은 프로그램에 독립적인 프로세스 인스턴스가 여러 개 있을 수 있습니다.

## 프로그램 인스턴스와 PID

예를 들어 두 터미널에서 피연산자 없이 `cat`을 시작합니다. 각 인스턴스는 입력을 기다리고 자체 프로세스 ID를 갖습니다.

```bash
$ pgrep -a cat
18420 cat
18457 cat
```

두 프로세스는 같은 프로그램을 실행하지만 서로 다른 입력 스트림, 메모리 내용, 자격 증명, 작업 디렉터리, 수명을 가질 수 있습니다. PID는 한 시점의 살아 있는 프로세스 하나를 식별하고 해당 프로세스가 종료된 뒤 재사용될 수 있습니다.

:::single-choice{#process-details-program-versus-process} 같은 프로그램의 실행 인스턴스 두 개를 구분하는 것은 무엇인가요?

::option[각 인스턴스마다 실행 파일을 하나씩 복사해야 합니다.]{#process-details-copied-executable explanation="여러 프로세스가 파일을 복제하지 않고 같은 실행 파일의 코드 페이지를 매핑하고 공유할 수 있습니다."}
::option[인스턴스 하나만 메모리나 열린 파일을 가질 수 있습니다.]{#process-details-one-instance-resources explanation="각 프로세스는 자체 메모리 매핑과 파일 디스크립터 테이블을 가질 수 있습니다."}
::option[각 인스턴스에 자체 프로세스 문맥과 PID가 있습니다.]{#process-details-independent-context .correct explanation="실행 코드가 같은 파일에서 와도 별도 실행에는 고유한 살아 있는 프로세스 상태가 주어집니다."}
:::

## 커널이 추적하는 상태

커널은 각 프로세스를 스케줄하고 제어하는 데 필요한 정보를 유지합니다.

- 프로세스 및 부모 식별자
- 사용자 및 그룹 자격 증명
- 가상 메모리 매핑
- 열린 파일 디스크립터와 현재 디렉터리
- 시그널 처리 방식과 대기 중인 시그널
- 스케줄링 정책, 우선순위, 실행 상태
- CPU 시간 같은 계산 데이터

일부 기반 자원은 공유될 수 있습니다. 관련 프로세스가 매핑된 메모리를 공유할 수 있고 한 프로세스의 스레드는 주소 공간과 여러 프로세스 전체 자원을 공유합니다. 따라서 프로세스는 모든 바이트나 커널 객체가 물리적으로 비공개라는 뜻 없이 격리 경계를 제공합니다.

:::single-choice{#process-details-kernel-state} Linux 프로세스의 스케줄링과 자격 증명 상태를 유지하는 구성 요소는 무엇인가요?

::option[커널]{#process-details-kernel .correct explanation="커널은 프로세스 상태를 추적하고 스케줄링, 메모리, 시그널, 접근 제어 규칙을 적용합니다."}
::option[실행 파일의 디렉터리]{#process-details-directory explanation="디렉터리는 이름과 inode 매핑을 저장하며 실행 중인 프로세스를 스케줄하지 않습니다."}
::option[사용자의 터미널 에뮬레이터만]{#process-details-terminal explanation="터미널이 프로세스와 상호작용할 수 있지만 프로세스 관리는 커널의 책임입니다."}
:::

## CPU 스케줄링과 메모리

실행 가능한 스레드는 CPU 시간을 놓고 경쟁합니다. 커널 스케줄러는 스케줄링 클래스, 우선순위, CPU 선호도, 부하, 정책에 따라 어떤 스레드가 어느 CPU에서 실행될지 선택합니다. 모든 프로세스가 같은 몫을 받는다는 보장은 아닙니다.

각 프로세스는 일반적으로 가상 주소 공간을 봅니다. 커널과 하드웨어는 가상 주소를 물리 메모리나 다른 기반 저장소에 매핑하고 보호를 적용하며 적절한 경우 페이지를 공유할 수 있습니다. 따라서 `ps`나 `top`의 메모리 수치가 해당 프로세스에만 귀속되는 고유한 물리 RAM 양과 자동으로 같지는 않습니다.

:::single-choice{#process-details-scheduler-role} Linux 스케줄러는 무엇을 선택하나요?

::option[사용 가능한 CPU에서 실행할 실행 가능 스레드]{#process-details-runnable-thread .correct explanation="스케줄링 정책은 실행 가능한 실행 문맥 중에서 선택하고 CPU 시간을 할당합니다."}
::option[디스크를 포맷할 때 기록할 파일 소유자]{#process-details-format-owner explanation="파일 시스템 소유권은 CPU 스케줄링과 관련이 없습니다."}
::option[사용자가 입력할 수 있는 명령줄]{#process-details-command-entry explanation="스케줄러는 대화형 명령 구문이 아니라 실행 시간을 관리합니다."}
:::

## 프로세스 종료와 자원 정리

프로세스가 종료되면 커널은 대부분의 비공개 자원을 해제하고 남은 디스크립터를 닫으며 부모를 위해 종료 정보를 기록합니다. 부모가 종료 상태를 가져갈 때까지 작은 프로세스 테이블 레코드가 좀비로 남을 수 있습니다. 따라서 “프로세스 실행이 끝났다”와 “프로세스 테이블에서 모든 흔적이 사라졌다”가 항상 동시에 일어나지는 않습니다.

:::single-choice{#process-details-exit-status} 종료된 프로세스가 잠시 좀비로 남을 수 있는 이유는 무엇인가요?

::option[전체 메모리를 할당받은 채 여전히 명령을 실행하고 있습니다.]{#process-details-zombie-running explanation="좀비는 실행을 완료했고 일반적인 실행 주소 공간을 더 이상 유지하지 않습니다."}
::option[부모가 기록된 종료 상태를 아직 수집하지 않았습니다.]{#process-details-parent-wait .correct explanation="부모가 wait 작업을 수행할 때까지 커널이 최소 종료 정보를 유지합니다."}
::option[실행 파일이 커널에 영구적으로 잠겼습니다.]{#process-details-zombie-file-lock explanation="좀비 상태는 영구 실행 파일 잠금이 아니라 부모-자식 종료 계산에 관한 것입니다."}
:::

[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864) 실습에서 여러 인스턴스를 시작하고 PID와 상태를 비교하세요. [Linux top 명령](https://labex.io/ko/labs/linux-linux-top-command-real-time-system-monitoring-388500) 실습은 스케줄링과 자원 지표가 변하는 보기를 제공합니다.

## 요약

이제 프로세스를 단순한 프로그램 파일 이상의 것으로 설명할 수 있습니다.

1. 저장된 실행 코드와 살아 있는 프로세스 인스턴스를 구분할 수 있습니다.
2. 커널이 추적하는 상태와 자원을 식별할 수 있습니다.
3. 스케줄링을 동등한 몫이 아니라 실행 가능 스레드와 연결할 수 있습니다.
4. 부모가 수집할 때까지 종료 상태가 남을 수 있음을 이해할 수 있습니다.
