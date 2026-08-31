---
lesson_id: "listing-devices"
course_id: "devices"
lang: "ko"
order_index: 6
title: "lsusb, lspci, lsscsi"
description: "USB 토폴로지, PCI 기능, SCSI 계층 장치 및 활성 드라이버를 검사하는 방법을 알아봅니다."
meta_title: "lsusb, lspci, lsscsi - 장치"
meta_description: "리눅스 시스템에서 USB, PCI 및 SCSI 하드웨어를 나열하고 검사하는 방법을 알아봅니다. lsusb, lspci, lsscsi와 장치 트리를 보여 주는 lsusb -t를 설명합니다."
meta_keywords: "lsusb, lspci, lsscsi, lsusb -t, USB 장치 목록, PCI 장치 목록, SCSI 장치 목록, 리눅스 하드웨어, 장치 정보"
---

리눅스는 버스와 하위 시스템별 장치 목록 도구를 제공합니다. 명령마다 서로 다른 뷰를 보여 주므로, 하나의 완전한 하드웨어 목록을 기대하지 말고 식별자, 토폴로지, 드라이버, sysfs 경로 및 로그를 함께 확인하십시오.

## USB 장치 검사하기

`lsusb`는 USB 하위 시스템에서 보이는 USB 장치를 나열합니다.

```bash
$ lsusb
```

출력에는 일반적으로 버스 및 장치 번호, 공급업체와 제품 ID 쌍, 로컬 USB ID 데이터베이스에서 가져온 설명이 포함됩니다. 숫자로 된 버스 및 장치 주소는 다시 연결하거나 재부팅하면 바뀔 수 있으므로 영구적인 식별자로 취급해서는 안 됩니다.

다음 명령으로 컨트롤러, 허브, 포트, 인터페이스, 드라이버 및 속도의 관계를 표시합니다.

```bash
$ lsusb -t
```

상세 디스크립터 출력도 사용할 수 있지만 일부 정보에는 더 높은 읽기 권한이 필요합니다. 검사 명령의 경고를 없애겠다는 이유로 USB 장치에 광범위한 권한을 부여하지 마십시오.

:::single-choice{#listing-devices-usb-tree}
USB 장치를 토폴로지 트리로 표시하는 명령은 무엇입니까?

::option[`lspci -k`]{#listing-devices-lspci-tree explanation="이 명령은 USB 토폴로지가 아니라 PCI 기능과 커널 드라이버 정보를 나열합니다."}
::option[`lsscsi -t`]{#listing-devices-lsscsi-tree explanation="이 수업에서 소개한 USB 트리 명령이 아닙니다."}
::option[`lsusb -t`]{#listing-devices-lsusb-tree .correct explanation="트리 옵션은 컨트롤러와 허브 아래의 장치를 포트 및 인터페이스 관계와 함께 보여 줍니다."}
:::

## PCI 기능 검사하기

`lspci`는 PCI 및 PCI Express 버스에서 발견된 기능을 나열합니다.

```bash
$ lspci
```

내부 또는 외부에 연결된 PCIe 장치에는 그래픽, 네트워크, 저장 장치, USB, 오디오 및 브리지 컨트롤러가 포함될 수 있습니다. 사용 중인 커널 드라이버와 후보 모듈은 다음 명령으로 표시합니다.

```bash
$ lspci -k
```

PCI 컨트롤러가 이 목록에 나타난다고 해서 그 뒤의 모든 장치가 초기화되어 정상이라는 뜻은 아닙니다. 문제를 해결할 때는 드라이버 바인딩과 커널 로그를 확인하십시오.

:::single-choice{#listing-devices-pci-driver}
PCI 목록에 커널 드라이버 정보를 추가하는 명령은 무엇입니까?

::option[`lspci -k`]{#listing-devices-lspci-k .correct explanation="`-k` 옵션은 활성 커널 드라이버와 각 PCI 장치를 처리할 수 있는 모듈을 표시합니다."}
::option[`lsusb -t`]{#listing-devices-usb-not-pci explanation="이 명령은 USB 계층 및 인터페이스 드라이버를 설명합니다."}
::option[`lsblk -f`]{#listing-devices-lsblk-filesystem explanation="이 명령은 PCI 드라이버 바인딩이 아니라 블록 장치와 파일 시스템 필드를 보고합니다."}
:::

## SCSI 계층 장치 검사하기

`lsscsi`는 리눅스 SCSI 중간 계층을 통해 표현되는 장치를 나열합니다.

```bash
$ lsscsi
```

여기에는 네이티브 SCSI 장치와 SCSI 호환 계층을 통해 제공되는 SATA, USB 저장 장치 또는 가상 디스크가 포함될 수 있습니다. NVMe 네임스페이스는 일반적으로 다른 하위 시스템에 속하며 `lsscsi`가 완전하게 조사하지 않습니다.

여러 블록 장치 유형을 포함하는 저장 장치 중심 계층을 보려면 `lsblk`도 사용합니다.

```bash
$ lsblk -o NAME,TYPE,SIZE,MODEL,SERIAL,TRAN,FSTYPE,MOUNTPOINTS
```

:::single-choice{#listing-devices-lsscsi-scope}
`lsscsi`가 주로 나열하는 것은 무엇입니까?

::option[모든 NVMe 네임스페이스와 컨트롤러만 나열합니다.]{#listing-devices-only-nvme explanation="NVMe는 자체 하위 시스템과 도구를 사용하지만 관련 블록 뷰가 다른 곳에 나타날 수 있습니다."}
::option[이름이 `.scsi`로 끝나는 파일만 나열합니다.]{#listing-devices-scsi-extension explanation="이 명령은 파일 이름 확장자가 아니라 커널 장치 인터페이스를 조회합니다."}
::option[리눅스 SCSI 중간 계층을 통해 표현되는 장치입니다.]{#listing-devices-scsi-mid-layer .correct explanation="이 명령은 SCSI 호스트, 대상, 논리 장치 및 가능한 경우 해당 장치 노드를 보고합니다."}
:::

## 장치 목록 결과 해석하기

설명은 로컬 ID 데이터베이스에서 가져오는 경우가 많아 일반적이거나 오래되었을 수 있습니다. 목록에 나온 장치에 작동하는 드라이버가 없을 수도 있고, 가상화 환경에서는 에뮬레이션 또는 반가상화 하드웨어를 제공할 수 있습니다. 조사 중인 문제와 권한에 맞춰 `udevadm info`, sysfs, `lsblk`, 네트워크 도구 및 `journalctl -k` 또는 `dmesg` 결과를 서로 연결하십시오.

이 유틸리티들은 일반적으로 `usbutils`, `pciutils` 및 `lsscsi` 같은 별도 패키지로 제공될 수 있습니다. 명령이 없을 때는 출처를 알 수 없는 대체품을 다운로드하지 말고 배포판 패키지 관리자를 사용하십시오.

:::single-choice{#listing-devices-listed-not-working}
`lspci`에 장치가 보이면 드라이버가 활성화되어 올바르게 작동한다는 사실이 증명됩니까?

::option[아닙니다. 드라이버 바인딩과 관련 커널 메시지도 검사해야 합니다.]{#listing-devices-needs-correlation .correct explanation="열거 결과는 PCI 기능이 보인다는 사실만 보여 줄 뿐 상위 수준 초기화의 성공을 보장하지 않습니다."}
::option[그렇습니다. PCI 열거가 완전한 기능 테스트를 수행합니다.]{#listing-devices-complete-test explanation="목록 조회는 모든 하드웨어 기능을 실행하거나 서비스 동작을 검증하지 않습니다."}
::option[그렇습니다. `lspci`가 적합한 드라이버를 자동으로 설치합니다.]{#listing-devices-installs-driver explanation="이 명령은 장치 목록 도구이며 드라이버 패키지를 설치하지 않습니다."}
:::

[리눅스 하드웨어 장치 살펴보기](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)에서 한 제어된 호스트의 여러 하위 시스템 뷰를 비교해 보십시오.

## 요약

이제 확인하려는 장치 하위 시스템에 맞는 목록 명령을 선택할 수 있습니다.

1. USB 식별 정보와 토폴로지에는 `lsusb`와 `lsusb -t`를 사용합니다.
2. PCI 기능과 드라이버 바인딩에는 `lspci -k`를 사용합니다.
3. SCSI 계층 장치에는 `lsscsi`를, 블록 토폴로지에는 `lsblk`를 사용합니다.
4. 열거 결과를 드라이버, sysfs 및 커널 메시지와 연결합니다.
