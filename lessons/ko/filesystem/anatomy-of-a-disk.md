---
lang: "ko"
title: "디스크의 해부학"
meta_description: "Linux 디스크 파티셔닝, MBR 대 GPT, 파일 시스템 구조에 대해 알아보세요. 파티션, 테이블, 데이터 구성 방법을 이해하세요. 이 초보자 가이드로 시작하세요!"
meta_keywords: "Linux 디스크 파티셔닝, MBR, GPT, 파일 시스템 구조, Linux 파티션, 초보자, 튜토리얼, 가이드"
---

## Lesson Content

하드 디스크는 파티션으로 세분화될 수 있으며, 이는 본질적으로 여러 블록 장치를 만듭니다. `/dev/sda1` 및 `/dev/sda2`와 같은 예시를 떠올려보세요. `/dev/sda`는 전체 디스크이지만, `/dev/sda1`은 해당 디스크의 첫 번째 파티션입니다. 파티션은 데이터를 분리하는 데 매우 유용하며, 특정 파일 시스템이 필요한 경우 전체 디스크를 하나의 파일 시스템 유형으로 만드는 대신 쉽게 파티션을 생성할 수 있습니다.

### Partition Table

모든 디스크에는 파티션 테이블이 있습니다. 이 테이블은 시스템에 디스크가 어떻게 파티션되어 있는지 알려줍니다. 이 테이블은 파티션이 시작하고 끝나는 위치, 부팅 가능한 파티션, 디스크의 어떤 섹터가 어떤 파티션에 할당되었는지 등을 알려줍니다. 사용되는 두 가지 주요 파티션 테이블 체계는 Master Boot Record (MBR) 와 GUID Partition Table (GPT) 입니다.

### Partition

디스크는 데이터를 구성하는 데 도움이 되는 파티션으로 구성됩니다. 하나의 디스크에 여러 파티션을 가질 수 있으며, 서로 겹칠 수 없습니다. 파티션에 할당되지 않은 공간이 있다면, 이는 여유 공간으로 알려져 있습니다. 파티션 유형은 파티션 테이블에 따라 달라집니다. 파티션 내부에는 파일 시스템을 가질 수 있거나, 스왑과 같은 다른 용도로 파티션을 전용으로 사용할 수 있습니다 (이에 대해서는 곧 다룰 것입니다).

_MBR_

- 전통적인 파티션 테이블로, 표준으로 사용되었습니다.
- primary, extended, logical 파티션을 가질 수 있습니다.
- MBR 은 4 개의 primary 파티션으로 제한됩니다.
- primary 파티션을 extended 파티션으로 만들어 추가 파티션을 만들 수 있습니다 (디스크에는 하나의 extended 파티션만 있을 수 있습니다). 그런 다음, extended 파티션 내부에 logical 파티션을 추가합니다. logical 파티션은 다른 파티션과 동일하게 사용됩니다. 좀 이상하죠.
- 최대 2 테라바이트 디스크를 지원합니다.

_GPT_

- GUID Partition Table (GPT) 은 디스크 파티셔닝의 새로운 표준이 되고 있습니다.
- 한 가지 유형의 파티션만 있으며, 많은 파티션을 만들 수 있습니다.
- 각 파티션은 전역적으로 고유한 ID (GUID) 를 가집니다.
- 주로 UEFI 기반 부팅과 함께 사용됩니다 (자세한 내용은 다른 과정에서 다룰 것입니다).

### Filesystem Structure

이전 강의에서 파일 시스템이 파일과 디렉토리의 조직화된 모음이라는 것을 알고 있습니다. 가장 간단한 형태로, 파일 시스템은 파일을 관리하는 데이터베이스와 실제 파일 자체로 구성됩니다. 하지만, 좀 더 자세히 살펴보겠습니다.

- Boot block - 파일 시스템의 첫 몇 섹터에 위치하며, 파일 시스템 자체에서는 실제로 사용되지 않습니다. 오히려 운영 체제를 부팅하는 데 사용되는 정보를 포함합니다. 운영 체제에는 하나의 boot block 만 필요합니다. 여러 파티션이 있는 경우, 각 파티션에 boot block 이 있지만, 그 중 많은 수는 사용되지 않습니다.
- Super block - boot block 다음에 오는 단일 블록으로, inode 테이블의 크기, logical 블록의 크기, 파일 시스템의 크기와 같은 파일 시스템에 대한 정보를 포함합니다.
- Inode table - 이것을 파일 관리 데이터베이스라고 생각하세요 (inode 에 대한 전체 강의가 있으니 걱정하지 마세요). 각 파일 또는 디렉토리는 inode 테이블에 고유한 항목을 가지며, 파일에 대한 다양한 정보를 포함합니다.
- Data blocks - 이것은 파일과 디렉토리의 실제 데이터입니다.

다양한 파티션 테이블을 살펴보겠습니다. 아래는 MBR 파티셔닝 테이블 (msdos) 을 사용하는 파티션의 예시입니다. 머신에서 primary, extended, logical 파티션을 볼 수 있습니다.

```plaintext
pete@icebox:~$ sudo parted -l
Model: Seagate (scsi)
Disk /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos

Number  Start   End     Size    Type      File system     Flags
 1      1049kB  6860MB  6859MB  primary   ext4            boot
 2      6861MB  21.5GB  14.6GB  extended
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
 6      7381MB  21.5GB  14.1GB  logical   xfs
```

이 예시는 GPT 이며, 파티션에 고유 ID 만 사용합니다.

```plaintext
Model: Thumb Drive (scsi)
Disk /dev/sdb: 4041MB
Sector size (logical/physical): 512B/512B
Partition Table: gpt

Number  Start   End     Size     File system  Name        Flags
 1      17.4kB  1000MB  1000MB                first
 2      1000MB  4040MB  3040MB                second
```

## Exercise

자신의 머신에서 **parted -l**을 실행하고 결과를 평가하세요.

## Quiz Question

MBR 파티셔닝 체계에서 4 개 이상의 파티션을 생성하는 데 사용되는 파티션 유형은 무엇입니까?

## Quiz Answer

extended
