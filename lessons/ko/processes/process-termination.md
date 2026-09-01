---
lesson_id: "process-termination"
course_id: "processes"
lang: "ko"
order_index: 5
title: "프로세스 종료"
description: "종료 상태, 기다리기, 좀비, 부모 재지정이 Linux 프로세스 수명 주기를 완성하는 방식을 배웁니다."
meta_title: "프로세스 종료 - Processes"
meta_description: "Linux 프로세스 종료, wait 시스템 호출, 좀비와 고아 프로세스의 핵심 차이를 알아봅니다. 안정적인 시스템을 위한 자식 프로세스 상태 관리를 배웁니다."
meta_keywords: "Linux 프로세스 종료, 좀비 프로세스, 고아 프로세스, 좀비와 고아 프로세스, linux 자식 프로세스 종료, wait 시스템 호출, _exit, 프로세스 관리"
---

프로세스는 main 함수에서 반환하거나 종료 인터페이스를 호출하거나 시그널로 종료될 수 있습니다. 커널은 대부분의 자원을 해제하지만 부모가 종료 정보를 수집할 때까지 부모-자식 계산은 계속됩니다.

## 종료 상태

정상 종료하는 프로그램은 정수 상태를 제공합니다. 관례적으로 상태 `0`은 성공을 뜻하고 0이 아닌 값은 어떤 형태의 실패나 다른 결과를 보고합니다. 0이 아닌 값의 정확한 의미는 프로그램 인터페이스에 속합니다.

쉘에서 가장 최근 포그라운드 파이프라인의 상태를 확인합니다.

```bash
$ command
$ printf '%s\n' "$?"
```

쉘은 제한된 인코딩 상태 범위를 노출하고 시그널 종료도 표현하므로 이 값이 완전한 진단 기록은 아닙니다. 프로그램은 자체 종료 코드를 문서화해야 합니다.

:::single-choice{#process-termination-success-status} Unix 관례에서 성공을 나타내는 정상 종료 상태는 무엇인가요?

::option[`1`]{#process-termination-status-one explanation="의미는 명령마다 다르지만 많은 프로그램이 `1`을 일반 실패에 사용합니다."}
::option[`0`]{#process-termination-status-zero .correct explanation="정상 상태 0은 관례적으로 성공적인 완료를 나타냅니다."}
::option[`255`]{#process-termination-status-255 explanation="0이 아닌 값이며 관례적으로 성공을 나타내지 않습니다."}
:::

## 기다리고 수거하기

커널은 자식이 어떻게 종료되었는지 기록하고 부모에게 알립니다. 부모는 `wait()` 시스템 호출 계열의 하나를 사용해 정보를 가져갑니다. 레코드를 수집하는 것을 수거(reaping)라고 합니다.

기다리기는 실행을 조정할 수도 있습니다. 쉘은 포그라운드 명령이 끝날 때까지 기다린 뒤 다음 프롬프트를 표시하고 백그라운드 작업은 기다리기를 미룰 수 있습니다. 잘 설계된 장기 실행 부모는 관련 없는 작업을 막지 않으면서 자식을 수거하도록 준비해야 합니다.

:::single-choice{#process-termination-wait-purpose} 성공적인 wait 작업은 부모가 무엇을 가져가게 하나요?

::option[자식의 종료 정보]{#process-termination-wait-status .correct explanation="wait 계열은 자식이 어떻게 멈추거나 종료되었는지 보고하고 완료된 자식을 수거합니다."}
::option[자식의 이전 주소 공간 사본]{#process-termination-wait-memory explanation="대부분의 프로세스 메모리는 이미 해제되었고 `wait()`가 부모에게 반환하지 않습니다."}
::option[자식이 연 모든 파일의 소유권]{#process-termination-wait-files explanation="기다리기는 파일 시스템 소유권 메타데이터를 이전하지 않습니다."}
:::

## 좀비 프로세스

자식이 종료된 뒤 종료 레코드가 수거되기 전에는 좀비로 나타나며 `ps`에서 흔히 상태 `Z`로 표시됩니다. 더 이상 실행하지 않고 일반 주소 공간도 유지하지 않지만 최소 프로세스 테이블 항목과 계산 정보가 남습니다.

좀비에 시그널을 보내도 다시 종료하게 할 수 없습니다. 좀비가 계속 쌓이면 기다리지 않는 부모를 진단하고 적절한 운영 절차로 그 부모를 재시작하거나 수정하거나 수거할 프로세스로 부모가 재지정되도록 해야 합니다. 수가 많으면 PID나 프로세스 테이블 용량을 소진할 수 있습니다.

:::single-choice{#process-termination-zombie-definition} 좀비 프로세스를 설명하는 것은 무엇인가요?

::option[부모가 이미 종료된 실행 중인 자식]{#process-termination-zombie-orphan explanation="좀비 상태가 아니라 고아가 된 자식을 설명합니다."}
::option[종료했지만 종료 레코드가 수거되지 않은 자식]{#process-termination-zombie-unreaped .correct explanation="프로세스는 실행을 멈췄지만 커널이 부모를 위해 최소 상태를 유지합니다."}
::option[중단할 수 없는 루프에서 CPU를 사용하는 프로세스]{#process-termination-zombie-cpu explanation="좀비는 명령을 실행하거나 CPU 시간을 사용하지 않습니다."}
:::

## 고아와 부모 재지정

자식이 남은 상태에서 부모가 종료되면 커널은 자식을 적절한 subreaper 또는 관련 PID 네임스페이스의 init 프로세스로 부모 재지정합니다. 자식은 실행 중, 대기 중, 정지 상태일 수 있고 나중에 좀비가 될 수도 있습니다. “고아”는 한 실행 상태가 아니라 원래 부모 관계를 잃은 사실을 설명합니다.

입양한 프로세스가 종료 상태 수집을 책임집니다. 현대 서비스 관리자와 컨테이너 환경에서는 새 부모가 항상 호스트의 PID 1이라고 가정하면 안 됩니다.

:::single-choice{#process-termination-orphan-definition} 프로세스가 원래 부모보다 오래 살아남으면 어떻게 되나요?

::option[적절한 subreaper 또는 네임스페이스 init 프로세스로 부모가 재지정됩니다.]{#process-termination-orphan-reparented .correct explanation="커널은 입양 프로세스를 할당하여 유효한 부모 관계를 보존합니다."}
::option[종료하지 않았어도 즉시 좀비가 됩니다.]{#process-termination-orphan-zombie explanation="좀비 상태는 실행이 끝나고 상태가 수집을 기다릴 때만 시작됩니다."}
::option[PID를 영구적으로 잃고 익명으로 계속됩니다.]{#process-termination-orphan-no-pid explanation="살아 있는 고아 프로세스는 부모 관계가 바뀌는 동안 프로세스 신원을 유지합니다."}
:::

[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864) 실습에서 운영 작업 부하를 방해하지 않고 종료 코드와 프로세스 상태를 관찰할 수 있습니다.

## 요약

이제 실행 종료와 부모 측 정리를 구분할 수 있습니다.

1. 0을 관례적인 성공으로 해석하고 0이 아닌 상태는 프로그램 문서를 따를 수 있습니다.
2. 기다리기로 자식의 종료 정보를 수집할 수 있습니다.
3. 좀비를 종료했지만 수거되지 않은 프로세스로 이해할 수 있습니다.
4. 고아를 원래 부모 종료 후 부모가 재지정된 자식으로 이해할 수 있습니다.
