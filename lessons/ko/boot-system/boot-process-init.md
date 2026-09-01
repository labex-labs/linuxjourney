---
lesson_id: "boot-process-init"
course_id: "boot-system"
lang: "ko"
order_index: 5
title: "부팅 과정: Init"
description: "PID 1이 사용자 공간을 초기화하고 서비스를 감독하며 자식 프로세스를 회수하고 종료를 조정하는 방법을 알아봅니다."
meta_title: "부팅 과정: Init - 시스템 부팅"
meta_description: "리눅스 부팅 과정의 init을 살펴봅니다. 전통적인 System V, Upstart, systemd 및 다른 init 시스템이 서비스를 시작하고 관리하는 방법을 설명합니다."
meta_keywords: "리눅스 init, systemd, System V init, Upstart, 리눅스 부팅 과정, PID 1, 리눅스 튜토리얼"
---

커널은 PID 네임스페이스에서 첫 사용자 공간 프로세스를 PID 1로 시작합니다. 완전한 리눅스 시스템에서는 이 init 프로세스가 서비스 환경을 구성합니다. 컨테이너에서는 작은 init 래퍼나 애플리케이션 자체가 PID 1일 수 있지만 여전히 특별한 신호 및 자식 프로세스 회수 책임을 가집니다.

## PID 1의 책임

init 시스템은 일반적으로 다음 작업을 수행합니다.

- 서비스, 로그인, 마운트 및 기타 작업 단위를 시작하고 감독
- 의존성과 설정된 대상 상태에 따라 작업 순서 지정
- 고아가 된 자식 프로세스를 입양하고 회수
- 정책에 따라 서비스 실패에 대응
- 질서 있는 종료와 재부팅 조정

정확한 경계는 시스템마다 다릅니다. 장치 관리, 네트워킹, 로깅 및 예약 작업은 PID 1에 내장된 코드가 아니라 init이 감독하는 별도 프로그램일 수 있습니다.

:::single-choice{#boot-init-pid-one-role} PID 네임스페이스에서 PID 1에 특별히 부여되는 책임은 무엇입니까?

::option[부팅할 때마다 모든 애플리케이션을 소스에서 컴파일합니다.]{#boot-init-compile-apps explanation="일반적인 서비스 시작은 모든 소프트웨어를 다시 빌드하지 않고 설치된 프로그램을 사용합니다."}
::option[디스크의 물리 섹터 크기를 정의합니다.]{#boot-init-sector-size explanation="init이 서비스를 관리하기 전에 저장 하드웨어와 드라이버가 섹터 구조를 노출합니다."}
::option[고아가 된 자식 프로세스를 입양하고 회수합니다.]{#boot-init-reap-orphans .correct explanation="PID 1은 최종 부모이며 좀비 레코드가 쌓이지 않도록 종료 상태를 수집해야 합니다."}
:::

## System V Init과 런레벨

전통적인 sysvinit은 `/etc/inittab` 같은 설정과 런레벨별 시작 및 종료 스크립트를 사용합니다. 런레벨은 운영 모드를 나타내지만 숫자 레벨의 의미는 배포판마다 다를 수 있습니다. 스크립트 순서는 관례에 따라 정해지며 배포판 도구가 이를 확장하거나 병렬화할 수 있습니다.

`/etc/init.d/`가 있다는 이유만으로 호스트의 활성 init 시스템을 추정하지 마십시오. PID 1이 다른 구현인 시스템에도 호환성 스크립트가 남아 있을 수 있습니다.

:::single-choice{#boot-init-sysv-runlevel} System V 런레벨은 무엇을 나타냅니까?

::option[부트 로더가 선택한 커널 버전 번호입니다.]{#boot-init-runlevel-kernel explanation="커널 선택은 로더의 역할이며 init 런레벨로 인코딩되지 않습니다."}
::option[서비스 작업과 연결된 설정 운영 모드입니다.]{#boot-init-runlevel-mode .correct explanation="SysV 레이아웃은 레벨을 시작 또는 종료 스크립트 집합 및 순서와 연결합니다."}
::option[파일 시스템의 현재 inode 사용률입니다.]{#boot-init-runlevel-inodes explanation="파일 시스템 메타데이터 용량은 서비스 운영 모드와 관련이 없습니다."}
:::

## 이벤트 및 의존성 기반 시스템

Upstart는 이벤트 구동 작업 모델을 도입했으며 구형 우분투 릴리스와 일부 다른 시스템에서 사용되었습니다. 현재는 주로 역사적 또는 레거시 운영 환경에서 중요합니다.

systemd는 현재 여러 범용 배포판에서 널리 사용됩니다. 서비스, 소켓, 마운트, 타이머, 장치, 대상 및 기타 리소스를 단위로 모델링합니다. 선언적 의존성과 활성화 메커니즘을 통해 필요한 순서를 유지하면서 독립적인 작업을 동시에 진행할 수 있습니다.

그 밖에 활발히 사용되는 init 및 감독 설계로 OpenRC, runit, s6 및 BusyBox init이 있습니다. “가장 최신”이라는 기준은 호환성 규칙으로 유용하지 않습니다. 실제 시스템이 무엇을 실행하는지 식별하고 해당 문서를 사용하십시오.

:::single-choice{#boot-init-systemd-unit-model} systemd는 서비스와 마운트 같은 관리 리소스를 어떻게 표현합니까?

::option[MBR 주 파티션 항목으로 표현합니다.]{#boot-init-systemd-partitions explanation="디스크 파티션 메타데이터는 서비스 관리자 단위와 관련이 없습니다."}
::option[PID 1 실행 파일을 가리키는 하드 링크로만 표현합니다.]{#boot-init-systemd-hard-links explanation="단위는 단순한 inode 별칭이 아니라 설정 및 런타임 객체입니다."}
::option[의존성과 활성화 관계를 가진 단위로 표현합니다.]{#boot-init-systemd-units .correct explanation="단위 유형은 순서, 상태 및 감독을 위한 공통 모델을 제공합니다."}
:::

## 실행 중인 Init 식별하기

설치된 파일을 보고 추측하지 말고 PID 1을 검사합니다.

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

권한, 컨테이너 및 네임스페이스에 따라 보이는 결과가 달라집니다. 컨테이너 안에서 실행한 명령은 호스트 init이 아니라 해당 네임스페이스의 PID 1을 보고합니다. 식별한 뒤에는 다른 init 계열의 명령을 섞지 말고 고유한 상태 및 로그 도구를 사용하십시오.

:::single-choice{#boot-init-detect-running} 레거시 스크립트 디렉터리의 존재를 확인하는 것보다 PID 1을 검사하는 편이 나은 이유는 무엇입니까?

::option[모든 리눅스 시스템에서 PID 1의 실행 파일 이름이 같기 때문입니다.]{#boot-init-same-name explanation="systemd, sysvinit, BusyBox, 컨테이너 init 프로그램 등이 PID 1을 차지할 수 있습니다."}
::option[다른 init 구현이 실행 중이어도 호환성 파일이 존재할 수 있기 때문입니다.]{#boot-init-compatibility-files .correct explanation="실행 중인 PID 1 실행 파일이 활성 init 시스템을 보여 주는 더 강한 증거입니다."}
::option[레거시 디렉터리가 부팅할 때마다 자동으로 삭제되기 때문입니다.]{#boot-init-directories-deleted explanation="설치된 호환성 파일은 여러 부팅 동안 유지될 수 있습니다."}
:::

## 요약

이제 init을 하나의 필수 구현이 아니라 역할로 설명할 수 있습니다.

1. PID 1을 서비스 초기화, 프로세스 회수 및 종료와 연결합니다.
2. System V 런레벨을 배포판에서 정의한 운영 모드로 이해합니다.
3. systemd 리소스와 의존성을 단위에 연결합니다.
4. 도구를 선택하기 전에 관련 네임스페이스에서 실행 중인 PID 1을 검사합니다.
