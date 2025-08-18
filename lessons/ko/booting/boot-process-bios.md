---
index: 2
lang: "ko"
title: "부팅 프로세스: BIOS"
meta_title: "부팅 프로세스: BIOS - 시스템 부팅"
meta_description: "Linux 부팅 프로세스, BIOS 및 MBR 에 대해 알아보세요. 이 초보자 친화적인 가이드를 통해 시스템이 어떻게 시작되는지 이해하세요. UEFI 개념을 탐색하세요!"
meta_keywords: "Linux 부팅 프로세스, BIOS, MBR, UEFI, Linux 튜토리얼, 부트로더, 초보자 Linux, 시스템 시작"
---

## Lesson Content

### BIOS

Linux 부팅 프로세스의 첫 번째 단계는 시스템 무결성 검사를 수행하는 BIOS 입니다. BIOS 는 오늘날 가장 지배적인 컴퓨터 유형인 IBM PC 호환 컴퓨터에서 가장 흔한 펌웨어입니다. 아마도 하드 드라이브의 부팅 순서를 변경하거나, 시스템 시간, 컴퓨터의 MAC 주소 등을 확인하기 위해 BIOS 펌웨어를 사용해 보셨을 것입니다. BIOS 의 주요 목표는 시스템 부트로더를 찾는 것입니다.

따라서 BIOS 가 하드 드라이브를 부팅하면, 시스템을 부팅하는 방법을 알아내기 위해 부트 블록을 검색합니다. 디스크를 어떻게 분할했는지에 따라 MBR (Master Boot Record) 또는 GPT 를 찾습니다. MBR 은 하드 드라이브의 첫 번째 섹터, 즉 처음 512 바이트에 위치합니다. MBR 은 디스크의 다른 어딘가에 있는 프로그램을 로드하는 코드를 포함하며, 이 프로그램이 실제로 부트로더를 로드합니다.

이제 디스크를 GPT 로 분할했다면 부트로더의 위치가 약간 변경됩니다.

### UEFI

BIOS 를 사용하는 대신 시스템을 부팅하는 또 다른 방법은 UEFI ("Unified Extensible Firmware Interface") 를 사용하는 것입니다. UEFI 는 BIOS 의 후속으로 설계되었습니다. 오늘날 대부분의 하드웨어에는 UEFI 펌웨어가 내장되어 있습니다. Macintosh 컴퓨터는 수년 동안 EFI 부팅을 사용해 왔으며, Windows 는 대부분의 기능을 UEFI 부팅으로 전환했습니다. GPT 형식은 EFI 와 함께 사용하도록 고안되었습니다. GPT 디스크를 부팅하는 경우 반드시 EFI 가 필요한 것은 아닙니다. GPT 디스크의 첫 번째 섹터는 BIOS 기반 시스템을 부팅할 수 있도록 "보호 MBR"을 위해 예약되어 있습니다.

UEFI 는 시작에 대한 모든 정보를 `.efi` 파일에 저장합니다. 이 파일은 하드웨어의 EFI System Partition 이라는 특수 파티션에 저장됩니다. 이 파티션 내에는 부트로더가 포함됩니다. UEFI 는 기존 BIOS 펌웨어에 비해 많은 개선 사항을 제공합니다. 그러나 우리는 Linux 를 사용하고 있으므로, 대부분의 경우 BIOS 를 사용하고 있습니다. 따라서 이 모든 강의는 그 전제를 따를 것입니다.

## Exercise

BIOS 메뉴로 들어가서 UEFI 부팅이 활성화되어 있는지 확인하십시오.

## Quiz Question

BIOS 는 무엇을 로드합니까?

## Quiz Answer

bootloader
