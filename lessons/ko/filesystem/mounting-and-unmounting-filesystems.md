---
index: 6
lang: "ko"
title: "mount 및 umount"
meta_title: "mount 및 umount - 파일 시스템"
meta_description: "Linux mount 및 umount 명령을 사용하여 파일 시스템을 관리하는 방법을 배웁니다. 초보자를 위한 장치 마운트, 언마운트 및 UUID 를 이해합니다."
meta_keywords: "Linux mount, umount command, mount filesystem, Linux UUID, beginner Linux, Linux tutorial, mount point, Linux guide"
---

## Lesson Content

파일 시스템의 내용을 보려면 마운트해야 합니다. 이를 위해 장치 위치, 파일 시스템 유형 및 마운트 지점이 필요합니다. 마운트 지점은 파일 시스템이 연결될 시스템의 디렉터리입니다. 따라서 기본적으로 장치를 마운트 지점에 마운트하려고 합니다.

먼저 마운트 지점을 생성합니다. 이 경우 **mkdir /mydrive**를 사용합니다.

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

정말 간단하죠! 이제 /mydrive 로 이동하면 파일 시스템 내용을 볼 수 있습니다. **-t**는 파일 시스템의 유형을 지정하고, 그 다음에는 장치 위치, 그 다음에는 마운트 지점이 옵니다.

마운트 지점에서 장치를 언마운트하려면:

```bash
sudo umount /mydrive
```

or

```bash
sudo umount /dev/sdb2
```

커널은 장치를 찾은 순서대로 이름을 지정한다는 것을 기억하십시오. 마운트 후 어떤 이유로 장치 이름이 변경되면 어떻게 될까요? 다행히 이름 대신 장치의 범용 고유 ID(UUID) 를 사용할 수 있습니다.

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

대부분의 경우 UUID 를 통해 장치를 마운트할 필요는 없습니다. 장치 이름을 사용하는 것이 훨씬 쉽고, 종종 운영 체제는 USB 드라이브와 같은 일반적인 장치를 마운트하는 방법을 알고 있습니다. 하지만 보조 하드 드라이브를 추가한 경우처럼 시작 시 파일 시스템을 자동으로 마운트해야 하는 경우 UUID 를 사용해야 하며, 다음 강의에서 이에 대해 다룰 것입니다.

## Exercise

`mount` 및 `umount`의 manpage 를 보고 사용할 수 있는 다른 옵션이 무엇인지 확인하십시오.

## Quiz Question

파일 시스템을 연결하는 데 사용되는 명령은 무엇입니까?

## Quiz Answer

mount
