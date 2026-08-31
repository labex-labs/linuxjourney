---
lesson_id: "sysv-services"
course_id: "init"
lang: "ko"
order_index: 2
title: "System V 서비스"
description: "활성 시스템이 지원하는 래퍼를 통해 레거시 SysV 서비스 스크립트를 검사하고 조작하는 방법을 알아봅니다."
meta_title: "System V 서비스 - Init"
meta_description: "리눅스의 전통적인 System V 서비스를 관리하는 방법을 알아봅니다. service 명령으로 서비스를 나열하고 시작, 중지 및 재시작하는 방법을 설명합니다."
meta_keywords: "System V, sysvinit, 리눅스 서비스, service 명령어, 리눅스 서비스 관리, 서비스 시작, 서비스 중지, 서비스 재시작"
---

SysV 서비스는 일반적으로 `/etc/init.d/` 아래의 실행 가능한 스크립트로 표현됩니다. 스크립트는 구현과 배포판 관례에 따라 `start`, `stop`, `restart` 또는 `status` 같은 작업을 받습니다. `service` 명령은 이름 있는 스크립트를 더 제어된 환경에서 실행하는 래퍼를 제공합니다.

## 서비스와 작업 확인하기

먼저 스크립트 이름을 나열합니다.

```bash
$ ls -1 /etc/init.d/
```

일부 구현은 다음 명령을 제공합니다.

```bash
$ service --status-all
```

대괄호 표식과 종료 상태는 래퍼마다 다르고 스크립트가 알 수 없는 상태를 보고할 수도 있습니다. 서비스 하나에 대해서는 모든 작업이 있다고 가정하지 말고 스크립트의 사용법 출력이나 문서를 검사하십시오.

:::single-choice{#sysv-services-wrapper-purpose}
`service` 명령은 일반적으로 무엇을 감쌉니까?

::option[모든 서비스 파일에서 실행되는 디스크 파티션 편집기입니다.]{#sysv-services-partition-editor explanation="서비스 제어는 저장 장치 파티셔닝과 관련이 없습니다."}
::option[스크립트가 동적으로 추가한 커널 시스템 호출입니다.]{#sysv-services-new-syscall explanation="init 스크립트는 사용자 공간 프로세스 제어 프로그램입니다."}
::option[이름 있는 init 스크립트와 지원되는 작업 하나입니다.]{#sysv-services-script-action .correct explanation="래퍼는 레거시 서비스 스크립트를 찾아 정규화된 환경에서 호출합니다."}
:::

## 시작 및 중지

실제로 SysV가 관리하는 호스트에서는 다음 형태가 일반적입니다.

```bash
$ sudo service SERVICE_NAME start
$ sudo service SERVICE_NAME stop
```

서비스, 의존 항목, 현재 상태 및 운영 영향을 식별한 뒤에만 자리표시자를 바꾸십시오. 원격 세션에서 네트워킹, 원격 접근, 저장 장치 또는 인증을 중지하면 접근이 끊기거나 활성 작업이 손상될 수 있습니다.

직접 호출하는 `/etc/init.d/SERVICE_NAME ACTION` 형태도 있을 수 있지만 활성 관리자가 호환성을 제공하는 호스트에서는 상태와 의존성을 추적할 수 있도록 관리자 인터페이스 명령을 사용하십시오.

:::single-choice{#sysv-services-stop-peanut}
SysV 서비스 `peanut`의 중지를 요청하는 명령은 무엇입니까?

::option[`sudo service stop peanut`]{#sysv-services-stop-first explanation="일반적인 피연산자 순서는 작업보다 서비스 이름을 먼저 둡니다."}
::option[`sudo stop --partition peanut`]{#sysv-services-partition-stop explanation="SysV 서비스 래퍼 구문이 아닙니다."}
::option[`sudo service peanut stop`]{#sysv-services-peanut-stop .correct explanation="래퍼는 서비스 이름 다음에 요청한 중지 작업을 받습니다."}
:::

## 다시 불러오기, 재시작 및 상태

`restart`는 일반적으로 서비스를 중지한 뒤 시작하므로 중단이 발생합니다. `reload`는 완전히 재시작하지 않고 설정을 다시 읽도록 요청할 수 있지만 스크립트와 데몬이 지원할 때만 가능합니다. 일부 스크립트는 배포판에서 정의한 대체 동작을 가진 `force-reload`를 제공합니다.

다시 불러오거나 재시작하기 전에 설정을 검증하고, 원격 접근 변경에는 두 번째 관리 연결을 유지하며, 작업 후 “실행 중” 상태만 보지 말고 실제 엔드포인트와 로그를 통해 서비스를 검증하십시오.

```bash
$ sudo service SERVICE_NAME status
$ sudo service SERVICE_NAME reload
```

:::single-choice{#sysv-services-reload-versus-restart}
`reload`를 `restart`와 같다고 가정해서는 안 되는 이유는 무엇입니까?

::option[reload가 항상 전체 운영체제를 종료하기 때문입니다.]{#sysv-services-reload-shutdown explanation="서비스 다시 불러오기 작업의 일반적인 의미가 아닙니다."}
::option[restart는 설정만 출력하고 프로세스 상태를 절대 바꾸지 않기 때문입니다.]{#sysv-services-restart-readonly explanation="restart는 일반적으로 서비스를 중지한 뒤 시작합니다."}
::option[reload는 서비스별 작업이며 프로세스를 중지하지 않고 설정을 다시 읽을 수 있기 때문입니다.]{#sysv-services-reload-specific .correct explanation="지원 및 의미는 init 스크립트와 데몬에 속하지만 restart는 일반적으로 수명 주기를 중단합니다."}
:::

## 런타임 제어와 부팅 활성화

지금 서비스를 시작해도 이후 런레벨에서 자동으로 활성화되지는 않습니다. 부팅 활성화는 런레벨 링크로 표현되며 `update-rc.d`, `chkconfig` 또는 서비스 관리자 호환성 생성기 같은 배포판별 도구로 관리합니다.

배포판의 의존성 메타데이터와 관리 도구를 이해하기 전에는 `S`와 `K` 링크를 직접 만들지 마십시오. 수동 링크는 덮어써지거나 잘못된 순서로 배치될 수 있습니다.

:::single-choice{#sysv-services-start-versus-enable}
`service SERVICE start`가 이후 부팅에서 서비스를 반드시 활성화합니까?

::option[그렇습니다. 모든 start 작업이 모든 런레벨 링크를 자동으로 만듭니다.]{#sysv-services-start-links explanation="래퍼가 영구 활성화를 보편적으로 변경하지는 않습니다."}
::option[아닙니다. 런타임 상태와 런레벨 활성화는 별개입니다.]{#sysv-services-runtime-separate .correct explanation="현재 프로세스 시작과 별개로 부팅 링크나 관리자 정책이 이후 활성화를 결정합니다."}
::option[그렇습니다. 실행 중인 PID가 부트 섹터에 영구 저장됩니다.]{#sysv-services-pid-boot-sector explanation="PID는 런타임 식별자이며 부팅 활성화 메타데이터가 아닙니다."}
:::

## 요약

이제 런타임 제어와 부팅 정책을 혼동하지 않고 레거시 서비스를 조작할 수 있습니다.

1. 실제 스크립트와 지원되는 작업을 확인합니다.
2. 래퍼 구문에서 작업보다 서비스 이름을 먼저 사용합니다.
3. 다시 불러오기 또는 재시작 동작을 검증하고 확인합니다.
4. 배포판 도구로 이후 런레벨 활성화를 관리합니다.
