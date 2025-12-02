---
index: 4
lang: "ko"
title: "디스크 파티셔닝"
meta_title: "디스크 파티셔닝 - 파일 시스템"
meta_description: "parted 명령어를 사용하여 Linux 디스크 파티셔닝을 학습하세요. 이 가이드는 `sudo parted -l`로 파티션을 확인하고, 생성 및 크기 조절하는 방법을 다룹니다. 인기 있는 그래픽 대안인 gparted 도 소개합니다."
meta_keywords: "리눅스 디스크 파티셔닝, parted 명령어, sudo parted -l, gparted, gparted 윈도우 대안, fdisk, 디스크 관리, 파티션 생성, 파티션 크기 조절, 리눅스 가이드"
---

## Lesson Content

이 실습에서는 USB 드라이브와 같은 디스크를 분할하여 파일시스템을 관리하는 실용적인 가이드를 제공합니다. 여분의 드라이브가 없더라도 개념을 이해하기 위해 따라 할 수 있습니다.

먼저 디스크를 분할해야 합니다. 이 작업을 위해 사용할 수 있는 도구는 여러 가지가 있습니다:

- **fdisk**: GPT 를 지원하지 않는 기본적인 명령줄 분할 도구입니다.
- **parted**: MBR 및 GPT 분할을 모두 지원하는 강력한 명령줄 도구입니다.
- **gparted**: `parted`의 그래픽 버전입니다. 시각적 인터페이스를 선호하는 사용자에게 `gparted`는 직관적인 도구이며, 종종 훌륭한 `gparted windows alternative`(gparted 윈도우 대안) 로 간주됩니다.
- **gdisk**: `fdisk`와 유사하지만 GPT 만 지원합니다.

예제에서는 `parted`를 사용하겠습니다.

### 기존 파티션 나열하기

변경 사항을 적용하기 전에 디스크와 현재 레이아웃을 식별하는 것이 중요합니다. 이를 수행하는 빠른 방법은 `sudo parted -l` 명령을 사용하는 것입니다. 이 명령은 연결된 모든 블록 장치의 파티션 테이블을 나열합니다.

```bash
sudo parted -l
```

이 명령은 수정을 시작하기 전에 `/dev/sdb`와 같은 올바른 장치 이름을 찾는 데 도움이 됩니다.

### 대화형 모드 시작하기

변경 사항을 적용하려면 `parted`를 대화형 모드로 시작합니다. 대상 장치가 `/dev/sdb`라고 가정해 보겠습니다.

```bash
sudo parted
```

그러면 장치 파티션을 관리하기 위해 명령을 실행할 수 있는 `parted` 도구의 셸로 들어가게 됩니다.

### 장치 선택

`parted` 셸에 들어간 후에는 수정하려는 디스크를 선택해야 합니다. 데이터 손실을 방지하기 위해 올바른 디스크를 선택했는지 매우 주의해야 합니다.

```bash
select /dev/sdb
```

### 파티션 테이블 보기

`print` 명령을 사용하여 선택한 디스크의 파티션 테이블을 표시합니다.

```plaintext
(parted) print
Model: ATA VBOX HARDDISK (scsi)
Disk /dev/sdb: 10.7GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type      File system  Flags
 1      1049kB  10.7GB  10.7GB  primary   ext4         boot
```

이 출력은 장치에 사용 가능한 파티션을 보여줍니다. **Start**(시작) 및 **End**(끝) 열은 각 파티션이 디스크의 어디에 위치하는지를 나타냅니다.

### 파티션 생성하기

`mkpart` 명령은 새 파티션을 생성합니다. 파티션 유형 (예: `primary`), 선택적 파일시스템 유형, 시작 및 끝 지점을 지정해야 합니다.

```bash
mkpart primary ext4 1MB 5000MB
```

이 명령은 ext4 로 포맷된 주 파티션을 생성하며, 1MB 에서 시작하여 5000MB 에서 끝납니다.

### 파티션 크기 조정하기

`resizepart` 명령을 사용하여 기존 파티션의 크기를 조정할 수도 있습니다. 파티션 번호와 새 끝 지점이 필요합니다.

```bash
resizepart 1 8000MB
```

이 명령은 파티션 번호 1 의 크기를 8000MB 지점에서 끝나도록 조정합니다. 이는 파티션 크기만 변경한다는 점에 유의하십시오. 다른 도구 (예: `resize2fs`) 를 사용하여 파일시스템 자체의 크기를 조정해야 할 수도 있습니다.

`parted`는 매우 강력한 도구입니다. 실수로 데이터가 손실되는 것을 방지하기 위해 항상 명령을 실행하기 전에 다시 확인하십시오.

## Exercise

연습이 완벽을 만듭니다! 리눅스 디스크 분할 및 파일시스템 관리에 대한 이해를 강화하기 위한 실습 랩이 있습니다:

1. [리눅스 파티션 및 파일시스템 관리](https://labex.io/ko/labs/comptia-manage-linux-partitions-and-filesystems-590845) - 이 랩에서는 리눅스에서 디스크 파티션 및 파일시스템을 관리하는 방법을 배웁니다. fdisk 를 사용하여 새 파티션을 생성하고, ext4 로 포맷하고, 마운트하고, /etc/fstab에 영구 마운트를 구성하고, 안전한 보조 가상 디스크에 스왑 파티션을 생성할 것입니다.

이 랩은 디스크 분할 및 파일시스템 관리 개념을 실제 시나리오에 적용하고 이러한 필수 리눅스 관리 기술에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

파티션을 만들기 위한 `parted` 명령어는 무엇입니까? (대소문자를 구분하여 영어로 답변해 주십시오).

## Quiz Answer

mkpart
