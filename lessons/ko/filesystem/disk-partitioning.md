---
lang: "ko"
title: "디스크 파티션"
meta_title: "디스크 파티션 - 파일 시스템"
meta_description: "parted 를 사용하여 Linux 에서 디스크 파티션을 배우세요. 디스크를 파티션하고, 선택하고, 보고, 크기를 조정하는 방법을 이해하세요. 이 초보자 친화적인 가이드로 시작하세요!"
meta_keywords: "Linux 디스크 파티션, parted 명령어, fdisk, gparted, Linux 튜토리얼, 초보자 Linux, 디스크 관리, Linux 가이드"
---

## Lesson Content

USB 드라이브를 사용하여 파일 시스템으로 실질적인 작업을 해봅시다. USB 드라이브가 없어도 걱정하지 마세요. 다음 몇 가지 레슨을 계속 따라 할 수 있습니다.

먼저 디스크를 파티션해야 합니다. 이를 위해 사용할 수 있는 많은 도구가 있습니다:

- fdisk - 기본적인 명령줄 파티션 도구; GPT 를 지원하지 않습니다.
- parted - MBR 및 GPT 파티션을 모두 지원하는 명령줄 도구입니다.
- gparted - parted 의 GUI 버전입니다.
- gdisk - fdisk 와 유사하지만 MBR 은 지원하지 않고 GPT 만 지원합니다.

parted 를 사용하여 파티션을 해봅시다. USB 장치를 연결하고 장치 이름이 /dev/sdb2라고 가정해 봅시다.

### Launch parted

```bash
sudo parted
```

parted 도구로 진입하게 됩니다. 여기서 장치를 파티션하기 위한 명령을 실행할 수 있습니다.

### Select the device

```bash
select /dev/sdb2
```

작업할 장치를 선택하려면 장치 이름으로 선택합니다.

### View current partition table

```plaintext
(parted) print
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

여기서 장치에 사용 가능한 파티션을 볼 수 있습니다. **start** 및 **end** 지점은 파티션이 하드 드라이브에서 공간을 차지하는 위치입니다. 파티션에 적합한 시작 및 끝 위치를 찾아야 합니다.

### Partition the device

```bash
mkpart primary 123 4567
```

이제 시작 및 끝 지점을 선택하고 파티션을 만드세요. 사용한 테이블에 따라 파티션 유형을 지정해야 합니다.

### Resize a partition

공간이 없는 경우 파티션 크기를 조정할 수도 있습니다.

```bash
resize 2 1245 3456
```

파티션 번호를 선택한 다음 크기를 조정할 시작 및 끝 지점을 선택합니다.

Parted 는 매우 강력한 도구이므로 디스크를 파티션할 때 주의해야 합니다.

## Exercise

USB 드라이브를 절반은 ext4 로, 나머지 절반은 여유 공간으로 파티션하십시오.

## Quiz Question

파티션을 만드는 parted 명령어는 무엇입니까?

## Quiz Answer

mkpart
