---
index: 2
lang: "ko"
title: "부팅 프로세스: BIOS"
meta_title: "부팅 프로세스: BIOS - 시스템 부팅"
meta_description: "리눅스 부팅 프로세스의 첫 단계인 BIOS 에 대해 알아보세요. BIOS 가 MBR 또는 GPT 를 통해 부트로더를 찾는 방법과 UEFI 의 역할을 이해합니다. 이 가이드는 시스템 시작 과정을 설명하고 BIOS 설정으로 진입하는 방법을 간략히 다룹니다."
meta_keywords: "리눅스 부팅 프로세스, BIOS, MBR, UEFI, 리눅스 BIOS, BIOS 리눅스, BIOS 진입 방법, 부트로더, 시스템 시작"
---

## Lesson Content

Linux 부팅 프로세스의 첫 번째 단계는 시스템 시작 시 중요한 시스템 무결성 검사를 수행하는 BIOS(Basic Input/Output System) 입니다. BIOS 는 오늘날 사용되는 대부분의 컴퓨터를 나타내는 IBM PC 호환 컴퓨터에서 흔히 볼 수 있는 펌웨어입니다.

### Linux 에서 BIOS 의 역할

컴퓨터를 켜면 **Linux 시스템의 BIOS**가 가장 먼저 실행되는 소프트웨어입니다. 주요 기능은 CPU, 메모리, 하드 드라이브와 같은 시스템 하드웨어를 초기화하고 테스트하는 것입니다. 부팅 순서 변경, 시스템 시간 확인 또는 머신의 MAC 주소 확인을 위해 BIOS 펌웨어와 상호 작용한 적이 있을 것입니다. 하드웨어 검사가 완료되면 **bios linux** 프로세스의 주요 목표는 시스템 부트로더를 찾아서 제어권을 넘기는 것입니다.

### BIOS 가 부트로더를 찾는 방법

BIOS 가 하드 드라이브를 초기화하면 운영 체제를 시작하는 방법을 결정하기 위해 부트 블록을 검색합니다. 확인하는 위치는 디스크의 파티션 방식 (마스터 부트 레코드 (MBR) 또는 GUID 파티션 테이블 (GPT)) 에 따라 달라집니다.

MBR 은 하드 드라이브의 처음 512 바이트에 위치합니다. 이 작은 섹션에는 초기 부트 코드와 파티션 테이블이 포함되어 있습니다. MBR 의 코드는 실제 부트로더를 로드하는 또 다른 프로그램을 로드할 책임이 있습니다. GPT 로 파티션된 디스크를 사용하는 경우 프로세스가 약간 다릅니다.

### BIOS 로 부팅하는 방법

많은 사용자가 하드웨어 설정을 구성하기 위해 **BIOS 로 부팅하는 방법**을 알아야 합니다. 이를 위한 방법은 일반적으로 컴퓨터 전원을 켠 직후 특정 키 (예: F2, F10, DEL 또는 ESC) 를 누르는 것입니다. 부팅 장치 우선순위 변경 또는 가상화 기술 활성화와 같은 작업을 위해서는 **bios 로 부팅하는 방법**을 아는 것이 필수적입니다. 정확한 키는 제조사마다 다르므로 컴퓨터 설명서를 참조해야 할 수 있습니다.

### UEFI 의 부상

전통적인 BIOS 의 대안은 UEFI(Unified Extensible Firmware Interface) 입니다. BIOS 의 후속 제품으로 설계된 UEFI 는 이제 대부분의 최신 하드웨어에서 표준입니다. UEFI 는 전용 EFI 시스템 파티션 (ESP) 에 있는 .efi 파일에 모든 시작 정보를 저장합니다. 이 파티션에는 설치된 운영 체제의 부트로더가 포함되어 있습니다.

UEFI 는 더 빠른 부팅 시간과 더 큰 하드 드라이브 지원을 포함하여 BIOS 보다 많은 개선 사항을 제공합니다. GPT 형식은 UEFI 를 위해 설계되었지만, GPT 디스크의 "보호용 MBR"은 하위 호환성을 보장하여 이전 BIOS 기반 머신에서도 부팅할 수 있도록 합니다. 많은 Linux 시스템이 이제 UEFI 를 사용하지만, 이 가이드는 기본적인 이해를 위해 전통적인 BIOS 부팅 프로세스에 중점을 둘 것입니다.

## Exercise

연습이 완벽을 만듭니다! Linux 사용자 및 그룹 관리에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[useradd, usermod 및 userdel 을 사용하여 Linux 사용자 계정 관리](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성 및 보안부터 수정 및 삭제에 이르기까지 사용자 관리의 전체 수명 주기를 연습합니다.
2. **[groupadd, usermod 및 groupdel 을 사용하여 Linux 그룹 관리](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 새 그룹 생성, 사용자 멤버십 수정 및 그룹 제거를 포함하여 그룹 관리를 위한 명령줄 유틸리티에 대한 실습 경험을 얻습니다.
3. **[Linux 에서 사용자 계정 및 Sudo 권한 구성](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Linux 시스템의 보안을 강화하기 위해 사용자 계정 및 sudo 권한을 관리하는 필수 기술을 배웁니다.

이러한 랩은 실제 시나리오에서 개념을 적용하고 Linux 에서 사용자 및 그룹 관리에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

BIOS 는 무엇을 로드합니까? 영어로, 소문자로 된 한 단어로 답하십시오.

## Quiz Answer

bootloader
