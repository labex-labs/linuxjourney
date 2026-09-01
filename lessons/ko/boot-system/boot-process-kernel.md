---
lesson_id: "boot-process-kernel"
course_id: "boot-system"
lang: "ko"
order_index: 4
title: "부팅 과정: 커널"
description: "커널이 하드웨어를 초기화하고 initramfs 초기 사용자 공간을 실행해 실제 루트에 도달한 뒤 PID 1을 시작하는 방법을 알아봅니다."
meta_title: "부팅 과정: 커널 - 시스템 부팅"
meta_description: "리눅스 커널 부팅 과정을 살펴봅니다. initramfs가 임시 파일 시스템에서 드라이버를 불러와 최종 루트 파티션을 마운트하고 init을 실행하는 방법을 설명합니다."
meta_keywords: "부팅 루트, initramfs, 커널 부팅, 부트 파티션, 리눅스 부팅 과정, 루트 파일 시스템, 커널 초기화"
---

제어권이 리눅스 커널에 도달하면 커널은 메모리 관리, 스케줄링, 인터럽트, 내장 드라이버, 보안 프레임워크 및 기타 핵심 하위 시스템을 초기화합니다. 명령줄을 해석하고 첫 사용자 공간 프로세스를 시작할 준비를 합니다.

## 초기 사용자 공간이 존재하는 이유

단순한 루트 파일 시스템은 커널에 내장된 드라이버만으로 마운트할 수 있는 경우가 있습니다. 더 복잡한 시스템에서는 실제 루트에 도달하기 전에 모듈과 도구가 필요합니다. 예는 다음과 같습니다.

- 저장 장치 컨트롤러 또는 파일 시스템 모듈
- 암호화된 루트 잠금 해제
- LVM 또는 RAID 구성
- 네트워크 루트를 위한 네트워크 설정
- 장치 검색 및 영구 식별자 해석

initramfs는 이러한 구성 요소를 커널과 함께 제공되는 초기 사용자 공간 환경으로 묶습니다.

:::single-choice{#boot-kernel-initramfs-purpose} initramfs가 일반적으로 해결하는 문제는 무엇입니까?

::option[실제 루트를 사용할 수 있기 전에 필요한 초기 도구와 모듈을 제공합니다.]{#boot-kernel-early-tools .correct explanation="초기 사용자 공간은 커널 내장 지원만으로 접근할 수 없는 저장 장치를 검색하고 구성할 수 있습니다."}
::option[모든 사용자의 영구 홈 디렉터리를 펌웨어에 저장합니다.]{#boot-kernel-home-firmware explanation="이 아카이브는 부팅 결과물이며 영구 사용자 데이터 저장소가 아닙니다."}
::option[첫 로그인 후 리눅스 커널을 대체합니다.]{#boot-kernel-replace-kernel explanation="initramfs 코드가 사용자 공간에서 실행되는 동안에도 커널은 계속 작동합니다."}
:::

## Initramfs와 레거시 Initrd

최신 initramfs는 일반적으로 하나 이상의 cpio 아카이브이며 흔히 압축되어 있습니다. 커널은 이를 초기 루트 파일 시스템에 풉니다. 그런 다음 그 환경의 초기 `/init` 프로그램을 실행합니다.

레거시 initrd는 개념적으로 RAM 기반 블록 장치에 불러와 마운트하는 파일 시스템 이미지입니다. 파일 이름과 부트 로더 명령에서 두 용어를 느슨하게 사용하는 경우가 많으므로 단어만 보고 형식을 추정하지 말고 실제 도구를 검사하십시오.

initramfs는 커널 및 부팅 설계와 맞아야 합니다. 누락된 모듈, 오래된 장치 식별자 또는 빠진 암호화 및 LVM 도구 때문에 커널 이미지 자체가 유효해도 새로 설치한 커널을 부팅하지 못할 수 있습니다.

:::single-choice{#boot-kernel-initramfs-format} 최신 initramfs는 일반적으로 어떤 형태로 커널에 제공됩니까?

::option[HTTP로만 제공되는 대화형 패키지 저장소입니다.]{#boot-kernel-http-repository explanation="초기 사용자 공간에서 네트워크 접근을 설정할 수 있지만 그것이 initramfs 형식을 정의하지는 않습니다."}
::option[초기 루트에 풀리는 cpio 기반 아카이브입니다.]{#boot-kernel-cpio-archive .correct explanation="커널은 아카이브를 확장하고 초기 사용자 공간 초기화 프로그램을 실행합니다."}
::option[디스크의 GPT 백업 헤더입니다.]{#boot-kernel-gpt-header explanation="파티션 테이블 중복성은 초기 사용자 공간 아카이브와 독립적입니다."}
:::

## 실제 루트에 도달하기

초기 사용자 공간은 `root=` 같은 매개변수를 해석하고, 필요한 장치를 기다리며, 저장 장치 계층을 활성화하고, 의도한 루트 파일 시스템을 마운트합니다. 그런 다음 루트 전환 작업으로 그 파일 시스템을 새 `/`로 만들고 가능한 경우 임시 초기 환경을 해제합니다.

초기 `ro` 명령줄 요청은 일관성 검사와 제어된 시작을 지원할 수 있지만 정확한 순서는 배포판별로 다릅니다. 파일 시스템 검사는 사용자 공간 작업이며 정책에서 허용하면 initramfs나 이후 init 시스템이 루트를 읽기-쓰기로 다시 마운트할 수 있습니다.

:::single-choice{#boot-kernel-root-switch} 초기 사용자 공간이 의도한 실제 루트를 성공적으로 마운트한 뒤에는 어떻게 됩니까?

::option[모든 디스크의 파티션 테이블을 다시 만듭니다.]{#boot-kernel-recreate-tables explanation="루트 전환은 저장 장치를 다시 파티셔닝하지 않습니다."}
::option[커널이 종료되고 펌웨어가 일반 프로세스 스케줄링을 재개합니다.]{#boot-kernel-firmware-schedules explanation="제어권 전달 후에도 리눅스 커널이 프로세스와 하드웨어를 계속 담당합니다."}
::option[루트 뷰를 해당 파일 시스템으로 전환하고 사용자 공간 시작을 계속합니다.]{#boot-kernel-switch-root .correct explanation="임시 초기 루트가 설치된 시스템의 루트 계층으로 제어권을 넘깁니다."}
:::

## PID 1 시작하기

커널은 일반적으로 `/sbin/init` 같은 경로를 통해 도달하거나 `init=`으로 선택한 init 프로그램을 실행합니다. 해당 프로세스에는 PID 1이 부여되며 주 사용자 공간 서비스 환경을 책임집니다.

사용 가능한 init 프로그램을 실행할 수 없으면 커널은 정상적인 사용자 공간 시스템으로 진행할 수 없고 일반적으로 부팅 실패나 패닉을 보고합니다. 커널과 명령줄, initramfs 내용, 루트 검색, 루트 마운트 또는 PID 1 실행 가운데 가장 먼저 실패한 계층을 디버깅하십시오.

:::single-choice{#boot-kernel-pid-one} 단순화한 이 부팅 단계에서 커널이 수행하는 마지막 주요 제어권 전달은 무엇입니까?

::option[첫 사용자 공간 프로그램을 PID 1로 실행합니다.]{#boot-kernel-exec-init .correct explanation="그 뒤 PID 1이 서비스와 설정된 시스템 상태를 구성합니다."}
::option[`/proc`를 영구 패키지 데이터베이스로 바꿉니다.]{#boot-kernel-proc-package explanation="procfs는 계속 런타임 커널 인터페이스입니다."}
::option[이후 모든 프로세스에 같은 PID를 배정합니다.]{#boot-kernel-same-pid explanation="각 살아 있는 프로세스는 네임스페이스 안에서 고유한 PID를 받습니다."}
:::

## 요약

이제 초기 사용자 공간을 거쳐 PID 1에 이르는 커널 부팅을 추적할 수 있습니다.

1. 커널 내장 초기화와 불러올 수 있는 초기 모듈을 구분합니다.
2. initramfs를 cpio 기반 임시 루트 및 `/init`과 연결합니다.
3. 저장 장치 구성과 실제 루트로의 전환을 따라갑니다.
4. PID 1 실행을 사용자 공간으로의 제어권 전달로 식별합니다.
