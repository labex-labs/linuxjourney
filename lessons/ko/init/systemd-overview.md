---
lesson_id: "systemd-overview"
course_id: "init"
lang: "ko"
order_index: 5
title: "Systemd 개요"
description: "systemd가 단위를 불러오고 의존성을 해결하며 대상을 활성화하고 시스템 및 사용자 리소스를 관리하는 방법을 알아봅니다."
meta_title: "Systemd 개요 - Init"
meta_description: "systemd init 시스템의 기초를 알아봅니다. systemd가 단위와 대상을 이용해 리눅스 부팅 과정 및 시스템 서비스를 관리하는 방법을 설명합니다."
meta_keywords: "systemd, init 시스템, systemd 단위, systemd 대상, 리눅스 부팅 과정, 리눅스 서비스, 시스템 관리"
---

systemd는 현재 여러 리눅스 배포판에서 사용하는 PID 1 init 및 서비스 관리자입니다. systemd 프로젝트는 로깅, 장치, 로그인, 네트워크, 시간 및 기타 구성 요소도 제공하지만 배포판은 어떤 부분을 배포할지 선택할 수 있습니다.

## 실행 중인 관리자 확인하기

설치된 디렉터리의 존재가 아니라 실행 중인 상태를 검사합니다.

```bash
$ ps -p 1 -o pid,comm,args=
$ systemctl is-system-running
```

다른 프로그램이 PID 1인 시스템에도 `/usr/lib/systemd/`가 존재할 수 있고 컨테이너는 자체 PID 네임스페이스를 노출할 수 있습니다. `systemctl`에는 사용자 관리자와 원격/컨테이너 모드도 있으므로 작업이 어느 관리자를 대상으로 하는지 식별하십시오.

:::single-choice{#systemd-overview-detection} systemd가 시스템 init 관리자임을 가장 직접적으로 식별하는 것은 무엇입니까?

::option[`/usr/lib/systemd`라는 디렉터리가 존재합니다.]{#systemd-overview-directory explanation="systemd가 PID 1 역할을 하지 않아도 라이브러리와 단위 파일이 설치된 채 남을 수 있습니다."}
::option[사용자가 `systemctl`이라는 명령을 한 번 실행했습니다.]{#systemd-overview-command-executed explanation="시스템 systemd 관리자가 없어도 클라이언트 바이너리가 존재할 수 있습니다."}
::option[호스트의 PID 1이 systemd입니다.]{#systemd-overview-pid-one .correct explanation="실행 중인 첫 프로세스가 설치 파일이나 패키지 이름보다 강한 증거입니다."}
:::

## 관리 객체인 단위

단위는 systemd가 리소스나 활동에 이름을 붙여 만든 모델입니다. 일반적인 단위 유형은 다음과 같습니다.

- 프로세스와 데몬을 위한 `.service`
- 소켓 활성화를 위한 `.socket`
- 파일 시스템을 위한 `.mount` 및 `.automount`
- 이벤트 구동 활성화를 위한 `.timer` 및 `.path`
- 그룹화와 동기화를 위한 `.target`
- 다른 관리 리소스를 위한 `.device`, `.swap`, `.slice` 및 `.scope`

단위 상태가 항상 “실행 중”인 것은 아닙니다. 마운트는 마운트된 상태, 타이머는 대기 상태, 장치는 존재 상태이며 대상은 의존성이 도달된 뒤 활성 상태일 수 있습니다.

:::single-choice{#systemd-overview-group-unit} 다른 단위를 일반적으로 묶고 동기화 지점을 제공하는 단위 유형은 무엇입니까?

::option[`.socket`]{#systemd-overview-socket explanation="소켓 단위는 IPC 또는 네트워크 엔드포인트를 노출하고 서비스를 활성화할 수 있습니다."}
::option[`.target`]{#systemd-overview-target .correct explanation="대상 단위는 의존성을 모으고 부팅 또는 운영 이정표를 나타냅니다."}
::option[`.timer`]{#systemd-overview-timer explanation="타이머 단위는 달력 또는 단조 시간을 기준으로 활성화를 예약합니다."}
:::

## 단위 로드 경로와 재정의

시스템 단위는 다음과 같은 배포판 및 관리자 경로에서 불러올 수 있습니다.

- 여러 배포판에서 패키지가 제공한 단위를 위한 `/usr/lib/systemd/system/`
- 런타임에 생성된 또는 임시 설정을 위한 `/run/systemd/system/`
- 영구 로컬 관리자 설정 및 재정의를 위한 `/etc/systemd/system/`

정확한 공급업체 경로는 다를 수 있습니다. 우선순위가 높은 로컬 설정은 같은 단위 이름을 가진 낮은 우선순위 파일을 재정의합니다. 패키지 업데이트의 변경이 계속 보이도록 전체 공급업체 파일을 복사해 수정하지 말고 `systemctl edit UNIT`으로 만든 드롭인 재정의를 우선 사용하십시오.

:::single-choice{#systemd-overview-local-override} 영구적인 로컬 시스템 단위 재정의는 일반적으로 어디에 있어야 합니까?

::option[`/proc/systemd/` 안입니다.]{#systemd-overview-proc-systemd explanation="procfs는 런타임 커널 인터페이스이며 영구 단위 설정이 아닙니다."}
::option[`/etc/systemd/system/` 아래입니다.]{#systemd-overview-etc-system .correct explanation="관리자 설정 계층은 패키지에서 제공한 공급업체 단위보다 우선합니다."}
::option[디스크의 MBR 부트 코드 바이트 안입니다.]{#systemd-overview-mbr-units explanation="서비스 단위는 사용자 공간 설정 파일입니다."}
:::

## 의존성과 순서

systemd는 의존 관계에서 트랜잭션을 구성합니다. `Wants=`와 `Requires=`는 강도가 다른 방식으로 다른 단위를 트랜잭션에 포함합니다. `Before=`와 `After=`는 두 단위가 모두 예약되어 있을 때 순서를 지정하며 그 자체로 다른 단위를 시작하게 하지는 않습니다.

`After=network.target` 줄은 사용 가능한 연결, DNS 또는 특정 원격 엔드포인트의 준비 완료를 증명하지 않습니다. 서비스는 적절한 network-online 통합을 사용하거나 자체 재시도 및 준비 상태 동작을 구현해야 합니다.

:::single-choice{#systemd-overview-after-semantics} `After=other.service`만으로 지정되는 것은 무엇입니까?

::option[다른 서비스의 애플리케이션 엔드포인트가 정상이라는 보장입니다.]{#systemd-overview-after-health explanation="순서 작업 완료와 애플리케이션 준비 상태는 서로 다른 개념입니다."}
::option[두 단위가 모두 트랜잭션에 포함될 때의 순서입니다.]{#systemd-overview-after-ordering .correct explanation="다른 단위를 포함하려면 Wants나 Requires 같은 별도 요구 관계가 필요합니다."}
::option[이후 모든 부팅에서 두 단위의 자동 활성화입니다.]{#systemd-overview-after-enable explanation="활성화는 설치 메타데이터이며 순서 관계가 암시하지 않습니다."}
:::

## 대상과 기본 부팅 트랜잭션

`default.target`은 일반적으로 `multi-user.target` 또는 `graphical.target` 같은 대상의 별칭입니다. systemd는 해당 대상과 의존성의 트랜잭션을 시작하며 명시적인 순서를 적용하면서 관련 없는 작업을 동시에 진행시킵니다.

대상은 넓은 호환성 수준에서만 런레벨과 비슷합니다. 여러 대상이 동시에 활성화될 수 있고 사용자 정의 대상을 만들 수 있으며, 대상이 활성 상태라고 해서 시스템의 모든 서비스가 정상이라는 뜻은 아닙니다.

:::single-choice{#systemd-overview-default-target} `default.target`은 일반적으로 무엇을 선택합니까?

::option[`mkfs`가 지울 기본 블록 장치입니다.]{#systemd-overview-default-disk explanation="대상은 파괴적인 저장 장치 선택이 아니라 단위 활성화를 설명합니다."}
::option[항상 활성 상태일 수 있는 유일한 대상입니다.]{#systemd-overview-only-target explanation="대상은 그룹이며 한 번의 부팅에서 여러 대상이 활성화될 수 있습니다."}
::option[정상 시스템 부팅에 사용하는 대상 트랜잭션입니다.]{#systemd-overview-normal-boot .correct explanation="일반적으로 관리자가 선택한 다중 사용자 또는 그래픽 부팅 대상의 별칭입니다."}
:::

## 요약

이제 실행 중인 관리자, 단위 및 트랜잭션을 중심으로 systemd를 설명할 수 있습니다.

1. 관련 PID 1과 관리자 연결을 통해 systemd를 확인합니다.
2. 리소스 유형을 단위 접미사와 연결합니다.
3. 로컬 재정의를 공급업체 설정보다 높은 계층에 둡니다.
4. 의존성 강도, 순서 및 애플리케이션 준비 상태를 구분합니다.
5. 대상을 배타적인 상태가 아니라 그룹과 이정표로 취급합니다.
