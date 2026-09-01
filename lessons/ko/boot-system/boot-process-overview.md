---
lesson_id: "boot-process-overview"
course_id: "boot-system"
lang: "ko"
order_index: 1
title: "부팅 과정 개요"
description: "플랫폼 펌웨어에서 커널을 거쳐 첫 번째 사용자 공간 프로세스까지 이어지는 주요 제어권 전달을 알아봅니다."
meta_title: "부팅 과정 개요 - 시스템 부팅"
meta_description: "리눅스 부팅 과정의 BIOS, 부트 로더, 커널 및 init이라는 주요 단계를 살펴봅니다. 전원을 켠 순간부터 로그인 프롬프트까지의 전체 흐름을 설명합니다."
meta_keywords: "리눅스 부팅 과정, BIOS, UEFI, 부트 로더, 커널, init, initramfs, 리눅스 튜토리얼"
---

부팅은 플랫폼 재설정 상태를 실행 중인 사용자 공간 환경으로 바꾸는 신뢰 및 제어권 전달의 연쇄입니다. 일반적인 PC 경로는 펌웨어, 부트 관리자 또는 로더, 선택적인 초기 사용자 공간을 포함한 커널, PID 1 init 시스템으로 요약할 수 있습니다. 아키텍처, 가상 머신, 임베디드 시스템 및 컨테이너는 다른 경로를 사용할 수 있습니다.

## 펌웨어 초기화

플랫폼 펌웨어는 부팅 대상을 선택할 수 있을 정도로 CPU, 메모리 및 장치 상태를 초기화합니다. 전통적인 PC는 BIOS 규칙을 사용하고 현재 PC는 일반적으로 UEFI를 사용합니다. 펌웨어 설정, 부팅 순서, 플랫폼 검증 및 보안 부팅 정책에 따라 다음 단계에서 실행할 수 있는 파일이 결정될 수 있습니다.

펌웨어가 설치된 리눅스 루트 파일 시스템을 반드시 이해하는 것은 아닙니다. 인터페이스에 따라 부팅 경로를 찾습니다. 예를 들어 BIOS는 선택한 디스크의 부트 코드를 사용하고, UEFI 부팅 항목은 EFI 시스템 파티션의 EFI 실행 파일을 가리킵니다.

:::single-choice{#boot-overview-first-stage} 일반적인 PC가 재설정된 뒤 플랫폼 초기화를 시작하는 구성 요소는 무엇입니까?

::option[사용자의 대화형 셸입니다.]{#boot-overview-shell explanation="셸은 훨씬 나중에 사용자 공간 서비스나 로그인 처리에서 시작됩니다."}
::option[BIOS 또는 UEFI 같은 플랫폼 펌웨어입니다.]{#boot-overview-firmware .correct explanation="펌웨어는 리눅스가 실행되기 전에 초기 하드웨어 상태를 설정하고 다음 부팅 대상을 선택합니다."}
::option[파일 시스템 복구 유틸리티입니다.]{#boot-overview-fsck explanation="검사 도구는 부팅 정책에 따라 나중에 참여할 수 있지만 최초 펌웨어 단계는 아닙니다."}
:::

## 부트 로더 또는 부트 관리자

GRUB 같은 로더는 부팅 항목을 표시하고, 선택한 리눅스 커널과 초기 RAM 파일 시스템을 메모리에 불러오며, 커널 명령줄을 구성하고, 제어권을 넘길 수 있습니다. UEFI는 EFI 실행 파일로 빌드된 커널을 직접 불러올 수도 있으므로 별도의 다단계 로더는 흔하지만 보편적이지는 않습니다.

선택된 결과물은 서로 맞아야 합니다. 커널 버전, initramfs 내용, 루트 식별자, 보안 서명 및 명령줄 옵션이 모두 다음 제어권 전달의 성공 여부에 영향을 줍니다.

:::single-choice{#boot-overview-loader-role} 리눅스 부트 로더가 일반적으로 담당하는 작업은 무엇입니까?

::option[선택한 커널을 불러오고 명령줄을 전달합니다.]{#boot-overview-load-kernel .correct explanation="로더는 흔히 initramfs와 함께 커널 이미지와 매개변수를 준비합니다."}
::option[부팅할 때마다 모든 사용자 계정을 처음부터 만듭니다.]{#boot-overview-create-users explanation="영구 계정 데이터베이스는 사용자 공간 설정이며 로더가 매번 다시 만들지 않습니다."}
::option[로그인 후 모든 애플리케이션 프로세스를 스케줄링합니다.]{#boot-overview-schedule-apps explanation="CPU 스케줄링은 실행 중인 커널의 책임입니다."}
:::

## 커널과 초기 사용자 공간

커널은 필요에 따라 압축을 풀거나 위치를 재배치하고, 핵심 하위 시스템을 초기화하고, 명령줄을 해석하며, 사용 가능한 하드웨어를 검색합니다. initramfs는 실제 루트 파일 시스템을 구성하는 데 필요한 저장 장치 검색, RAID, 암호화, LVM, 네트워킹 또는 기타 작업을 위한 모듈과 초기 도구를 제공할 수 있습니다.

의도한 루트를 사용할 수 있게 되면 초기 사용자 공간이 그곳으로 전환하고 커널이 설정된 첫 사용자 공간 프로그램을 실행합니다. 파일 시스템 검사나 읽기-쓰기 재마운트를 누가 수행하는지 같은 세부 사항은 하나의 보편적 순서가 아니라 배포판의 부팅 설계에 속합니다.

:::single-choice{#boot-overview-initramfs-purpose} 시스템에서 initramfs를 사용할 수 있는 이유는 무엇입니까?

::option[모든 사용자의 데스크톱 세션을 펌웨어에 영구 보존합니다.]{#boot-overview-desktop-firmware explanation="initramfs는 부팅 시 사용하는 파일 시스템 이미지이며 펌웨어 세션 저장소가 아닙니다."}
::option[실제 루트 파일 시스템에 도달하는 데 필요한 초기 도구와 드라이버를 제공합니다.]{#boot-overview-early-root-tools .correct explanation="초기 사용자 공간은 암호화, 논리, 네트워크 또는 드라이버 의존적인 루트 저장 장치를 구성할 수 있습니다."}
::option[로그인 후 커널의 프로세스 스케줄러를 대체합니다.]{#boot-overview-replace-scheduler explanation="커널은 시스템이 작동하는 동안 계속 스케줄링을 담당합니다."}
:::

## PID 1과 시스템 준비 상태

첫 사용자 공간 프로세스에는 PID 1이 부여됩니다. 여러 배포판에서는 systemd이지만 다른 시스템은 sysvinit, OpenRC, runit, BusyBox init 또는 특수 프로그램을 사용합니다. PID 1은 사용자 공간 서비스 환경을 구성하고, 고아가 된 자식 프로세스를 회수하며, 종료 책임을 처리합니다.

PID 1에 도달했다고 해서 시스템이 완전히 준비되었다는 뜻은 아닙니다. 서비스가 아직 시작 중이고, 저장 장치가 마운트 중이며, 네트워크 설정이 완료되지 않았을 수 있습니다. 그래픽 또는 콘솔 로그인도 가능한 대상 상태 중 하나일 뿐입니다.

:::single-choice{#boot-overview-final-stage} 주요 사용자 공간 초기화 단계를 시작하는 것은 무엇입니까?

::option[부팅할 때마다 디스크의 보호 MBR을 만듭니다.]{#boot-overview-create-mbr explanation="파티션 테이블 생성은 일반적으로 반복되는 부팅 단계가 아닙니다."}
::option[모든 커널 명령줄 매개변수를 삭제합니다.]{#boot-overview-delete-command-line explanation="커널은 명령줄을 해석하고 노출하며 이를 삭제할 필요가 없습니다."}
::option[PID 1 init 프로그램을 실행합니다.]{#boot-overview-pid-one .correct explanation="루트 설정 후 첫 사용자 공간 프로세스가 설정된 시스템 상태에 필요한 서비스를 시작하거나 감독합니다."}
:::

[GRUB2 부팅 메뉴 사용자 지정하기](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) 실습은 로더 설정 경로 하나를 보여 줍니다. 복구 가능한 실습 시스템에서만 변경을 적용하십시오.

## 요약

이제 주요 리눅스 부팅 제어권 전달을 보편적인 구현 세부 사항으로 오해하지 않고 추적할 수 있습니다.

1. 펌웨어 초기화와 대상 선택에서 시작합니다.
2. 로더를 커널, initramfs 및 명령줄 선택과 연결합니다.
3. 복잡한 루트 구성을 이해할 때 초기 사용자 공간을 고려합니다.
4. PID 1을 준비 완료의 증거가 아니라 서비스 초기화의 시작으로 취급합니다.
