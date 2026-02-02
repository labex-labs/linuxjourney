---
index: 6
lang: "ko"
title: "lsusb, lspci, lsscsi"
meta_title: "lsusb, lspci, lsscsi - 장치 목록"
meta_description: "Linux 시스템에서 USB, PCI, SCSI 하드웨어를 나열하고 검사하는 방법을 알아보세요. 이 가이드는 lsusb -t 와 같은 옵션을 포함하여 lsusb, lspci, lsscsi 명령어를 다룹니다."
meta_keywords: "lsusb, lspci, lsscsi, lsusb -t, usb 장치 목록, pci 장치 목록, scsi 장치 목록, 리눅스 하드웨어, 장치 정보"
---

## Lesson Content

파일 목록을 보려면 `ls` 명령을 사용하는 것처럼, Linux 에는 하드웨어 장치를 나열하기 위한 유사한 도구가 있습니다. 이 명령들은 시스템에 연결된 하드웨어를 식별하는 데 필수적입니다.

### lsusb 를 사용하여 USB 장치 나열하기

시스템에 연결된 모든 USB 장치를 보려면 `lsusb` 명령을 사용할 수 있습니다. 이 명령은 USB 허브를 스캔하고 웹캠, 키보드, 외장 드라이브 등 발견된 장치에 대한 정보를 보고합니다.

```bash
lsusb
```

더 구조화된 보기를 위해 `lsusb -t` 명령을 사용할 수 있습니다. 이 옵션은 USB 장치를 트리와 유사한 구조로 표시하여 장치가 USB 컨트롤러 및 허브에 물리적으로 연결된 방식을 이해하는 데 유용합니다.

### lspci 를 사용하여 PCI 장치 나열하기

`lspci` 명령은 모든 PCI(Peripheral Component Interconnect) 장치를 나열하는 데 사용됩니다. 이들은 일반적으로 그래픽 카드, 네트워크 어댑터, 사운드 카드와 같이 마더보드에 연결된 내부 구성 요소입니다. 이 명령은 시스템의 핵심 하드웨어에 대한 빠른 개요를 제공합니다.

```bash
lspci
```

### lsscsi 를 사용하여 SCSI 및 SATA 장치 나열하기

저장 장치의 경우 `lsscsi` 명령이 특히 유용합니다. 이 명령은 일반적으로 하드 드라이브, SSD 및 광학 드라이브 (CD/DVD/Blu-ray) 를 포함하는 연결된 모든 SCSI 및 SATA 장치를 나열합니다. 다른 명령은 저장소 컨트롤러를 표시할 수 있지만, `lsscsi`는 저장 장치 자체에 대한 직접적인 정보를 제공하므로 시스템 관리자와 저장소를 관리하는 사용자에게 유용한 도구입니다.

```bash
lsscsi
```

## Exercise

Linux 에서 하드웨어 장치를 탐색하는 것에 대한 이해를 강화하기 위해 다음 실습 랩을 시도해 보세요:

1. **[Linux 에서 하드웨어 장치 탐색하기](https://labex.io/ko/labs/comptia-explore-hardware-devices-in-linux-590861)** - 이 랩에서는 Linux 환경 내에서 하드웨어 장치를 탐색, 식별 및 검사하는 필수 기술을 배우게 됩니다. 운영 체제가 물리적 구성 요소와 상호 작용하는 방식을 이해하기 위해 강력한 명령줄 유틸리티를 사용하여 실습 경험을 쌓게 될 것입니다.

이 랩은 이러한 개념을 실제 시나리오에 적용하고 장치 정보 관리 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

연결된 USB 장치 목록을 보는 데 사용되는 명령은 무엇입니까? (소문자 영어 문자만 사용하여 답변하십시오.)

## Quiz Answer

lsusb
