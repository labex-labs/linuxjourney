---
lesson_id: "device-names"
course_id: "devices"
lang: "ko"
order_index: 3
title: "장치 이름"
description: "리눅스가 일반 저장 장치, 파티션, 논리 장치 및 영구 장치 링크에 이름을 붙이는 방법을 알아봅니다."
meta_title: "장치 이름 - 장치"
meta_description: "저장 장치와 주변 장치에 쓰이는 일반적인 리눅스 장치 이름을 살펴봅니다. SCSI 디스크의 sda 명명 규칙과 /dev/null 같은 의사 장치를 설명합니다."
meta_keywords: "리눅스 장치 이름, sda 의미, /dev, SCSI 장치, 의사 장치, 저장 장치 이름, 리눅스 파티션 이름"
---

리눅스 장치 이름은 하드웨어에 표시된 물리 커넥터가 아니라 인터페이스를 제공하는 커널 하위 시스템과 드라이버를 반영합니다. 일반적인 패턴을 익히되 저장 장치를 변경하기 전에는 현재 시스템에서 실제 매핑을 확인하십시오.

## SCSI 계층 디스크 이름

SCSI 디스크 계층을 통해 제공되는 디스크는 일반적으로 `sd` 이름을 사용합니다. 여기에는 여러 SCSI, SATA, USB 저장 장치 및 가상 디스크가 포함됩니다.

- `/dev/sda`: 전체 디스크 하나
- `/dev/sdb`: 또 다른 전체 디스크
- `/dev/sda3`: `/dev/sda`의 3번 파티션
- `/dev/sdb1`: `/dev/sdb`의 1번 파티션

문자는 영구적인 식별자가 아니라 열거 순서를 반영합니다. 컨트롤러를 추가하거나 펌웨어 순서를 바꾸거나 장치를 연결하면 특정 문자를 받는 디스크가 달라질 수 있습니다.

:::single-choice{#device-names-sdb-first-partition} `sd` 명명 패턴에서 `/dev/sdb`의 1번 파티션을 나타내는 경로는 무엇입니까?

::option[`/dev/sda2`]{#device-names-sda-two explanation="현재 `/dev/sda`라는 이름을 가진 디스크의 2번 파티션을 나타냅니다."}
::option[`/dev/sdbp1`]{#device-names-sdb-p-one explanation="`p` 구분자는 기본 이름이 이미 숫자로 끝나는 패턴에 사용하며 일반 `sd` 이름에는 사용하지 않습니다."}
::option[`/dev/sdb1`]{#device-names-sdb-one .correct explanation="`sd` 디스크에서는 파티션 번호를 전체 디스크 이름 바로 뒤에 붙입니다."}
:::

## 숫자로 끝나는 이름

일부 전체 장치 이름은 이미 숫자를 포함하므로 파티션 이름에 `p`를 구분자로 사용합니다.

- `/dev/nvme0n1`: 컨트롤러 0의 NVMe 네임스페이스 1
- `/dev/nvme0n1p2`: 해당 네임스페이스의 2번 파티션
- `/dev/mmcblk0`: MMC 블록 장치
- `/dev/mmcblk0p1`: 해당 장치의 1번 파티션

NVMe 장치는 일반적으로 `/dev/sdX`라고 부르지 않으며 NVMe 하위 시스템의 명명 규칙을 사용합니다.

:::single-choice{#device-names-nvme-partition} `/dev/nvme0n1`의 2번 파티션을 나타내는 경로는 무엇입니까?

::option[`/dev/nvme0n1p2`]{#device-names-nvme-p-two .correct explanation="NVMe 파티션 이름은 파티션 번호 앞에 `p`를 넣습니다."}
::option[`/dev/nvme0n12`]{#device-names-nvme-no-p explanation="구분자가 없으면 끝의 숫자를 네임스페이스 번호와 구분하기 어렵습니다."}
::option[`/dev/sda2`]{#device-names-nvme-sda explanation="이는 `sd` 계층 디스크 파티션이며 지정된 NVMe 네임스페이스를 가리키지 않습니다."}
:::

## 논리 및 가상 블록 장치

리눅스는 물리 디스크 하나와 일대일로 대응하지 않는 블록 장치도 만듭니다.

- 장치 매퍼 장치에는 `/dev/dm-N`을 사용하며, 보통 `/dev/mapper/` 아래에 설명적인 링크도 함께 제공
- 리눅스 소프트웨어 RAID 배열에는 `/dev/mdN` 사용
- 일반 파일을 루프 블록 장치로 연결한 경우 `/dev/loopN` 사용

파티션, 암호화 계층, RAID, 논리 볼륨 및 파일 시스템은 하나의 스택을 이룹니다. 이름만 보고 스택을 추정하지 말고 `lsblk` 같은 도구로 부모-자식 관계를 확인하십시오.

:::single-choice{#device-names-device-mapper-link} 장치 매퍼 장치의 설명적인 링크가 일반적으로 제공되는 위치는 어디입니까?

::option[`/dev/mapper/`]{#device-names-mapper-directory .correct explanation="LVM 및 디스크 암호화 같은 장치 매퍼 사용자는 일반적으로 이 디렉터리에 이름 있는 링크를 노출합니다."}
::option[`/dev/null/`]{#device-names-null-directory explanation="`/dev/null`은 문자 장치이며 매핑된 블록 장치의 디렉터리가 아닙니다."}
::option[`/proc/partitions/mapper/`]{#device-names-proc-mapper explanation="장치 매퍼 이름 링크의 일반적인 경로가 아닙니다."}
:::

## 영구 저장 장치 링크

사용자 공간 장치 관리는 `/dev/disk/` 아래에 링크를 만들며, 일반적으로 다음과 같이 분류합니다.

- `by-id`: 하드웨어 또는 전송 식별자
- `by-uuid`: 파일 시스템 UUID
- `by-label`: 파일 시스템 레이블
- `by-partuuid`: 파티션 테이블 UUID
- `by-path`: 토폴로지에 의존하는 경로

안정적으로 유지되어야 하는 대상에 맞는 식별자를 선택하십시오. 파일 시스템 UUID는 파일 시스템을 식별할 뿐 그 아래의 물리 디스크를 반드시 식별하지는 않습니다. 파일 시스템을 복제하면 UUID가 중복될 수 있으므로 이를 사용하기 전에 고유성을 확인하십시오.

:::single-choice{#device-names-persistent-config} 장치별 설정에서 `/dev/disk/by-id/` 링크가 `/dev/sdX`보다 더 적합한 경우가 많은 이유는 무엇입니까?

::option[파괴적인 쓰기를 자동으로 되돌릴 수 있게 하기 때문입니다.]{#device-names-by-id-reversible explanation="안정적인 이름은 스냅샷, 백업 또는 쓰기 보호를 제공하지 않습니다."}
::option[블록 장치를 일반 파일로 변환하기 때문입니다.]{#device-names-by-id-regular explanation="이 항목은 여전히 블록 장치 노드로 해석되는 심볼릭 링크입니다."}
::option[현재 열거 순서가 아니라 장치 식별자에서 파생되기 때문입니다.]{#device-names-by-id-stable .correct explanation="링크 대상은 바뀔 수 있지만 식별자 기반 링크는 인식된 같은 장치와 계속 연결됩니다."}
:::

## 의사 장치 이름

`/dev/null`, `/dev/zero` 및 `/dev/urandom` 같은 이름은 물리 저장 장치가 아니라 커널 의사 장치를 나타냅니다. `/dev/null`은 쓰기를 버리고 읽기에서 파일 끝을 반환합니다. `/dev/zero`는 0 바이트를 제공하며, `/dev/urandom`은 커널 난수 생성기의 바이트를 제공합니다.

:::single-choice{#device-names-zero-read} `/dev/zero`를 읽으면 무엇이 생성됩니까?

::option[사용되지 않는 저장 장치 목록입니다.]{#device-names-zero-storage-list explanation="이는 바이트를 생성하는 문자 장치이며 검색 명령이 아닙니다."}
::option[값이 0인 바이트 스트림입니다.]{#device-names-zero-bytes .correct explanation="zero 의사 장치는 요청한 읽기에 널 바이트를 반환합니다."}
::option[`/dev/null`을 읽을 때처럼 즉시 파일 끝이 반환됩니다.]{#device-names-zero-eof explanation="`/dev/zero`는 계속 바이트를 생성하지만 `/dev/null`의 읽기는 파일 끝을 반환합니다."}
:::

파티션 작업을 시도하기 전에 [리눅스 하드웨어 장치 살펴보기](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)에서 이름, 영구 링크 및 `lsblk` 관계를 비교해 보십시오.

## 요약

이제 일반적인 리눅스 저장 장치 이름을 영구적인 식별자로 오해하지 않고 해석할 수 있습니다.

1. `sdXNUMBER`를 `sd` 디스크의 파티션으로 읽습니다.
2. 전체 장치 이름이 이미 숫자로 끝나면 `pNUMBER`를 사용합니다.
3. 장치 매퍼, RAID 및 루프 장치 같은 논리 장치를 식별합니다.
4. 필요한 식별 특성에 맞는 영구 링크를 우선 사용합니다.
5. 저장 장치 이름과 커널 의사 장치를 구분합니다.
