---
index: 6
lang: "ko"
title: "mount 및 umount"
meta_title: "mount 및 umount - 파일 시스템"
meta_description: "Linux mount 및 umount 명령을 사용하여 파일 시스템을 관리하는 방법을 배웁니다. 초보자를 위한 장치 마운트, 언마운트 및 UUID 를 이해합니다."
meta_keywords: "Linux mount, umount 명령, 파일 시스템 마운트, Linux UUID, 초보자 Linux, Linux 튜토리얼, 마운트 지점, Linux 가이드"
---

## Lesson Content

파일 시스템의 내용을 보려면 먼저 마운트해야 합니다. 그러려면 장치 위치, 파일 시스템 유형 및 마운트 지점이 필요합니다. 마운트 지점은 파일 시스템이 연결될 시스템의 디렉토리입니다. 따라서 기본적으로 장치를 마운트 지점에 마운트하려고 합니다.

먼저 마운트 지점을 생성합니다. 이 경우 **mkdir /mydrive**를 사용합니다.

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

정말 간단하죠! 이제 /mydrive 로 이동하면 파일 시스템 내용을 볼 수 있습니다. **-t**는 파일 시스템 유형을 지정하고, 그 다음에는 장치 위치, 그 다음에는 마운트 지점이 옵니다.

마운트 지점에서 장치를 언마운트하려면:

```bash
sudo umount /mydrive
```

또는

```bash
sudo umount /dev/sdb2
```

커널은 장치를 찾은 순서대로 이름을 지정한다는 것을 기억하십시오. 마운트한 후 어떤 이유로 장치 이름이 변경되면 어떻게 될까요? 다행히도 이름 대신 장치의 범용 고유 ID(UUID) 를 사용할 수 있습니다.

블록 장치의 시스템에서 UUID 를 보려면:

```bash
pete@icebox:~$ sudo blkid
/dev/sda1: UUID="130b882f-7d79-436d-a096-1e594c92bb76" TYPE="ext4"
/dev/sda5: UUID="22c3d34b-467e-467c-b44d-f03803c2c526" TYPE="swap"
/dev/sda6: UUID="78d203a0-7c18-49bd-9e07-54f44cdb5726" TYPE="xfs"
```

장치 이름, 해당 파일 시스템 유형 및 UUID 를 볼 수 있습니다. 이제 무언가를 마운트하려면 다음을 사용할 수 있습니다:

```bash
sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mydrive
```

대부분의 경우 UUID 를 통해 장치를 마운트할 필요는 없습니다. 장치 이름을 사용하는 것이 훨씬 쉽고, 종종 운영 체제는 USB 드라이브와 같은 일반적인 장치를 마운트하는 방법을 알고 있습니다. 하지만 보조 하드 드라이브를 추가한 경우처럼 시작 시 파일 시스템을 자동으로 마운트해야 한다면 UUID 를 사용해야 하며, 다음 단원에서 이에 대해 다룰 것입니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 파일 시스템 관리에 대한 이해를 강화하기 위한 실습 랩입니다:

- **[Linux 파티션 및 파일 시스템 관리](https://labex.io/ko/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 이 랩에서는 Linux 에서 디스크 파티션 및 파일 시스템을 관리하는 방법을 배웁니다. fdisk 를 사용하여 새 파티션을 생성하고, ext4 로 포맷하고, 마운트하고, /etc/fstab에서 영구 마운트를 구성하고, 스왑 파티션을 생성하는 모든 작업을 안전한 보조 가상 디스크에서 수행합니다.

이 랩은 실제 시나리오에서 마운트 및 언마운트 개념을 적용하고 파일 시스템 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

파일 시스템을 연결하는 데 사용되는 명령은 무엇입니까?

## Quiz Answer

mount
