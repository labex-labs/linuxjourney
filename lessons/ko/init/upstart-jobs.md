---
lesson_id: "upstart-jobs"
course_id: "init"
lang: "ko"
order_index: 4
title: "Upstart 작업"
description: "확인된 레거시 Upstart 시스템에서 `initctl`로 작업을 검사하고 제어하는 방법을 알아봅니다."
meta_title: "Upstart 작업 - Init"
meta_description: "리눅스 환경에서 Upstart 작업으로 서비스를 관리하는 방법을 알아봅니다. initctl로 작업을 나열하고 시작, 중지 및 재시작하는 방법을 설명합니다."
meta_keywords: "Upstart 작업, initctl, 리눅스 Upstart, 리눅스 서비스, 시스템 관리, init 시스템"
---

`initctl`은 실행 중인 Upstart init 데몬과 통신합니다. 관련 PID 네임스페이스가 실제로 Upstart를 실행하는지 확인한 뒤에만 사용하십시오. 현재 systemd 호스트에서는 systemd 고유 도구를 사용합니다.

## 작업 목록과 상태 읽기

알려진 작업과 인스턴스를 나열합니다.

```bash
$ initctl list
```

작업 하나를 검사합니다.

```bash
$ initctl status networking
networking start/running
```

Upstart는 `start` 또는 `stop` 같은 **목표**와 `running` 또는 `waiting` 같은 현재 **상태**를 모두 보고합니다. `stop/waiting`은 작업이 실행되지 않고 시작 조건이나 수동 요청을 기다린다는 뜻이며 반드시 오류를 나타내지는 않습니다.

:::single-choice{#upstart-jobs-stop-waiting}
Upstart 상태 출력의 `stop/waiting`은 일반적으로 무엇을 뜻합니까?

::option[작업이 실행 중이지만 CPU를 사용하지 않습니다.]{#upstart-jobs-running-idle explanation="실행 중인 작업은 일반적으로 start 목표와 running 상태를 표시합니다."}
::option[작업 목표가 중지이며 실행 중인 프로세스 인스턴스가 없습니다.]{#upstart-jobs-stopped-waiting .correct explanation="정의는 알려진 상태로 남고 Upstart는 이후 조건이나 명령을 기다립니다."}
::option[전체 운영체제가 전원 끄기를 기다리고 있습니다.]{#upstart-jobs-system-poweroff explanation="이 쌍은 전체 시스템 상태가 아니라 해당 작업 인스턴스를 설명합니다."}
:::

## 작업 시작 및 중지

의존성과 영향을 검토한 뒤 다음 명령을 사용합니다.

```bash
$ sudo initctl start JOB_NAME
$ sudo initctl stop JOB_NAME
```

작업은 환경 변수를 키로 사용하는 여러 인스턴스를 정의할 수 있습니다. 이 경우 설정에서 요구하는 정확한 변수를 제공하고 인스턴스를 조회하거나 중지할 때도 일관되게 포함하십시오. 네트워크, 저장 장치, 인증 또는 원격 접근 작업을 시작하거나 중지하면 세션이 끊길 수 있으므로 콘솔 복구 경로를 유지합니다.

:::single-choice{#upstart-jobs-start-command}
작업 `peanuts`의 수동 시작을 요청하는 명령은 무엇입니까?

::option[`sudo initctl start peanuts`]{#upstart-jobs-start-peanuts .correct explanation="start 하위 명령 다음에 설정된 작업 이름과 필요한 인스턴스 변수를 지정합니다."}
::option[`sudo initctl peanuts start`]{#upstart-jobs-name-first explanation="initctl 구문은 작업 이름보다 하위 명령을 먼저 둡니다."}
::option[`sudo systemctl initctl peanuts`]{#upstart-jobs-systemctl-mixed explanation="서로 다른 두 서비스 관리자 인터페이스를 잘못 섞은 명령입니다."}
:::

## 재시작과 설정 변경

실행 중인 작업의 재시작을 요청합니다.

```bash
$ sudo initctl restart peanuts
```

Upstart의 `restart`는 작업 파일을 편집한 뒤 새로 `stop`하고 `start`하는 것과 항상 같지 않습니다. 실행 중인 작업의 기존 설정이 계속 기준으로 남을 수 있습니다. 변경된 `.conf`를 검증하고 설치된 버전에 맞는 방식으로 Upstart에 설정 다시 불러오기를 요청한 뒤, 새 설정을 적용해야 할 때는 문서화된 중지/시작 절차를 따르십시오.

재시작은 중단을 일으키고 서비스가 다시 작동하지 못할 수도 있습니다. 작업 후 실제 엔드포인트와 로그를 검증하십시오.

:::single-choice{#upstart-jobs-restart-peanuts}
실행 중인 Upstart 작업 `peanuts`의 재시작을 요청하는 명령은 무엇입니까?

::option[`sudo initctl restart peanuts`]{#upstart-jobs-restart-command .correct explanation="restart 하위 명령은 Upstart 제어 인터페이스를 통해 지정한 작업을 조작합니다."}
::option[`sudo initctl emit peanuts`]{#upstart-jobs-emit-not-restart explanation="이벤트 내보내기는 일치하는 모든 작업 조건에 영향을 주며 직접 재시작 요청이 아닙니다."}
::option[`sudo service --status-all peanuts`]{#upstart-jobs-status-all explanation="상태 목록은 재시작을 요청하지 않습니다."}
:::

## 작업 설정 검증하기

수정한 작업 파일을 설치하기 전에 레거시 배포판이 제공한 검증 도구, 일반적으로 `init-checkconf`를 사용하십시오. 포함된 스크립트, 환경, 사용자/그룹 설정, 재시작 정책 및 이벤트 표현식을 검토합니다. 그런 다음 버전에 맞는 `initctl reload-configuration` 작업 흐름으로 정의를 다시 불러옵니다.

구문 검증은 경로의 존재, 실행에 필요한 자격 증명, 이벤트 도착 또는 프로세스 준비 완료를 증명할 수 없습니다. 복구 가능한 환경에서 테스트하십시오.

:::single-choice{#upstart-jobs-syntax-validation-limit}
작업 구문 검증으로 증명할 수 없는 것은 무엇입니까?

::option[서비스가 성공적으로 시작되어 준비 상태가 된다는 사실입니다.]{#upstart-jobs-runtime-not-proven .correct explanation="런타임 경로, 권한, 의존성 및 이벤트 흐름은 실제 제어 테스트가 필요합니다."}
::option[설정 텍스트를 구문 분석할 수 있다는 사실입니다.]{#upstart-jobs-parse-purpose explanation="구문 분석은 바로 구문 검증의 주된 목적입니다."}
::option[검증 도구에 파일이 제공되었다는 사실입니다.]{#upstart-jobs-file-supplied explanation="입력이 없으면 도구가 즉시 보고할 수 있습니다."}
:::

## 신중하게 이벤트 내보내기

Upstart는 이름 있는 이벤트를 내보낼 수 있습니다.

```bash
$ sudo initctl emit EVENT_NAME
```

시작 또는 중지 표현식이 일치하는 모든 작업이 반응할 수 있습니다. 이벤트는 작업 하나에만 보내는 것이 아니며 추가 이벤트를 통해 영향이 연쇄될 수 있습니다. 사용자 정의 또는 시스템 이벤트를 내보내기 전에 일치하는 모든 설정을 검사하고 운영 호스트에서 핵심 부팅 이벤트를 가볍게 재생하지 마십시오.

:::single-choice{#upstart-jobs-emit-scope}
`initctl emit EVENT_NAME`을 실행하면 어떤 일이 생길 수 있습니까?

::option[해당 이벤트와 일치하는 모든 작업 표현식이 전환할 수 있습니다.]{#upstart-jobs-event-matches .correct explanation="이벤트는 이름 있는 서비스 하나가 아니라 Upstart 의존성 모델 전체로 브로드캐스트됩니다."}
::option[이벤트와 이름이 정확히 같은 작업만 반응할 수 있습니다.]{#upstart-jobs-event-name-only explanation="일치는 작업 이름 동일 여부가 아니라 `start on` 및 `stop on` 표현식으로 정의합니다."}
::option[이벤트가 영구 큐 메시지로 영원히 저장됩니다.]{#upstart-jobs-event-durable explanation="Upstart 이벤트는 범용 영구 메시지 큐가 아니라 수명 주기 알림입니다."}
:::

## 요약

이제 명시적인 상태와 이벤트 범위를 고려해 Upstart 작업을 조작할 수 있습니다.

1. `initctl` 출력에서 목표와 상태를 따로 읽습니다.
2. 영향을 검토한 뒤 정확한 작업 인스턴스를 시작하고 중지합니다.
3. 재시작과 변경된 작업 설정 적용을 별개의 문제로 취급합니다.
4. 구문을 검증한 뒤 런타임 준비 상태를 테스트합니다.
5. 이벤트를 내보내기 전에 모든 일치 항목을 검사합니다.
