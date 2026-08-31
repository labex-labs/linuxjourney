---
lesson_id: "upstart-overview"
course_id: "init"
lang: "ko"
order_index: 3
title: "Upstart 개요"
description: "레거시 Upstart init 시스템이 이벤트 표현식을 작업 수명 주기 목표와 연결하는 방법을 알아봅니다."
meta_title: "Upstart 개요 - Init"
meta_description: "Upstart와 이벤트 구동 모델을 살펴봅니다. Upstart 작업 설정과 리눅스 서비스 수명 주기를 관리하는 방식을 설명합니다."
meta_keywords: "Upstart, init 시스템, 리눅스 서비스, 우분투, SysV, 이벤트 구동 init, 리눅스 가이드"
---

Upstart는 Canonical이 개발한 레거시 이벤트 기반 init 및 서비스 관리 시스템입니다. 구형 우분투와 몇몇 다른 배포판이 사용했지만 현재 우분투 릴리스는 systemd를 사용합니다. 최신 설치의 기본값으로 가정하지 말고 확인된 레거시 호스트를 유지 관리할 때 Upstart를 학습하십시오.

## 레거시 Upstart 호스트 확인하기

PID 1과 활성 제어 인터페이스를 검사합니다.

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
$ initctl version
```

마지막 명령은 Upstart 제어 서비스와 클라이언트가 있는 곳에서만 의미 있게 성공합니다. `/usr/share/upstart` 같은 디렉터리나 `/etc/init` 아래에 남은 파일은 약한 증거입니다. 다른 init 시스템이 제어권을 가져간 뒤에도 패키지와 마이그레이션 잔여물이 남을 수 있습니다.

:::single-choice{#upstart-overview-active-evidence}
호스트가 실제로 Upstart를 사용한다는 가장 강한 증거는 무엇입니까?

::option[디렉터리 이름에 `upstart`라는 단어가 들어 있습니다.]{#upstart-overview-directory-only explanation="설치된 문서나 잔여물이 다른 init을 사용하는 시스템에 남을 수 있습니다."}
::option[시스템에 셸 스크립트가 하나 이상 있습니다.]{#upstart-overview-shell-script explanation="셸 스크립트는 모든 init 환경에서 일반적으로 사용됩니다."}
::option[PID 1과 실행 중인 `initctl` 인터페이스가 Upstart를 식별합니다.]{#upstart-overview-live-interface .correct explanation="런타임 프로세스와 제어 증거는 레거시 파일의 존재보다 강합니다."}
:::

## 작업과 이벤트

Upstart **작업**은 프로세스 명령과 수명 주기 조건을 포함해 서비스나 태스크를 설명합니다. **이벤트**는 선택적인 환경 변수가 있는 이름 붙은 알림입니다. 작업 설정은 목표가 언제 시작 또는 중지 상태로 바뀌어야 하는지 표현할 수 있습니다.

시스템 작업 파일은 일반적으로 `/etc/init/` 아래에 `.conf` 접미사로 있습니다. 예는 다음과 같습니다.

```text
description "Example worker"
start on runlevel [2345]
stop on runlevel [016]
exec /usr/local/sbin/example-worker
```

이 설정은 런레벨 이벤트를 호환성 입력으로 사용합니다. 시스템이 어떤 이벤트를 내보내는지에 따라 Upstart는 파일 시스템, 장치, 네트워크 또는 애플리케이션 정의 이벤트에도 반응할 수 있습니다.

:::single-choice{#upstart-overview-start-on}
Upstart `start on` 스탠자가 정의하는 것은 무엇입니까?

::option[다음에 컴파일해야 할 커널 버전입니다.]{#upstart-overview-kernel-version explanation="작업 이벤트 조건은 커널 빌드를 선택하지 않습니다."}
::option[작업의 목표를 시작 상태로 바꾸는 이벤트 표현식입니다.]{#upstart-overview-start-condition .correct explanation="표현식이 충족되면 Upstart가 설정된 작업 시작 전환을 시도합니다."}
::option[모든 작업이 데이터를 저장하는 디스크 파티션입니다.]{#upstart-overview-partition explanation="저장 위치는 Upstart 이벤트 구문과 관련이 없습니다."}
:::

## 이벤트 구동 시작

시작 중에 Upstart는 작업 정의를 불러오고 이벤트를 받습니다. 일치하는 `start on` 또는 `stop on` 표현식이 작업 목표를 갱신합니다. 작업 전환은 다른 작업을 진행시킬 추가 이벤트를 내보낼 수 있습니다. 독립적인 작업은 동시에 진행될 수 있습니다.

이 모델은 하나의 하드 코딩된 전역 스크립트 순서를 피하지만 이벤트 이름, 순서 및 조건이 암묵적이면 진단하기 어려울 수 있습니다. 이벤트는 기본적으로 영구 메시지 큐가 아니므로 나중에 작업을 추가하거나 조건을 바꿀 때 모든 과거 이벤트가 다시 전달된다고 가정해서는 안 됩니다.

:::single-choice{#upstart-overview-event-chain}
Upstart 작업 하나가 다른 작업의 시작으로 이어질 수 있는 방식은 무엇입니까?

::option[메모리에서 다른 작업의 실행 바이너리를 다시 씁니다.]{#upstart-overview-rewrite-binary explanation="조정은 코드 수정이 아니라 이벤트를 통해 이루어집니다."}
::option[모든 작업이 항상 파일 이름 순서로 엄격히 시작됩니다.]{#upstart-overview-filename-order explanation="Upstart는 하나의 파일 이름 순서 목록이 아니라 이벤트 표현식을 사용합니다."}
::option[전환이 다른 작업과 일치하는 이벤트를 내보낼 수 있습니다.]{#upstart-overview-emitted-event .correct explanation="이벤트 표현식이 서로 독립적인 작업의 수명 주기 전환을 연결합니다."}
:::

## 마이그레이션과 호환성

systemd는 일부 레거시 서비스 스크립트에 제한적인 호환성을 제공할 수 있지만 Upstart 작업 구문을 네이티브 systemd 단위로 실행하지는 않습니다. 마이그레이션할 때는 파일 이름만 기계적으로 바꾸지 말고 수명 주기 조건, 환경, 재시작 정책, 로깅, 의존성 및 준비 상태 의미를 옮기십시오.

:::single-choice{#upstart-overview-current-ubuntu}
현재 표준 우분투 릴리스가 사용하는 init 시스템은 무엇입니까?

::option[모든 설치에서 Upstart만 사용합니다.]{#upstart-overview-current-upstart explanation="과거 특정 릴리스와 설정에서만 사실이었습니다."}
::option[systemd입니다.]{#upstart-overview-current-systemd .correct explanation="Upstart는 구형 우분투 세대에 속하며 현재 릴리스는 systemd를 PID 1로 사용합니다."}
::option[init 프로세스를 전혀 사용하지 않습니다.]{#upstart-overview-no-init explanation="완전한 우분투 시스템에는 여전히 PID 1 서비스 관리자가 필요합니다."}
:::

## 요약

이제 Upstart를 레거시 이벤트 및 작업 모델로 이해할 수 있습니다.

1. 실행 중인 PID 1과 제어 인터페이스를 확인합니다.
2. 작업 정의와 이벤트 알림을 구분합니다.
3. `start on`과 `stop on`을 수명 주기 표현식으로 해석합니다.
4. 설정 파일 이름만 바꾸지 말고 의미를 명시적으로 마이그레이션합니다.
