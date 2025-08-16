---
lang: "ko"
title: "/etc/fstab"
description: "Linux 에서 /etc/fstab에 대해 배우고, 시작 시 파일 시스템 마운트를 구성하고, 장치 항목을 관리하는 방법을 알아보세요. 초보자를 위한 fstab 이해!"
keywords: "/etc/fstab, Linux fstab, 파일 시스템 마운트, Linux 부팅, fstab 튜토리얼, 초보자, 가이드"
---

## Lesson Content

시작 시 파일 시스템을 자동으로 마운트하려면 `/etc/fstab` ("eff es tab"으로 발음하며 "eff stab"이 아님) 이라는 파일에 추가할 수 있습니다. 이 파일은 마운트된 파일 시스템의 영구 목록을 포함합니다.

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

각 줄은 하나의 파일 시스템을 나타내며, 필드는 다음과 같습니다:

- UUID - 장치 식별자
- Mount point - 파일 시스템이 마운트되는 디렉토리
- Filesystem type
- Options - 기타 마운트 옵션; 자세한 내용은 manpage 를 참조하십시오
- Dump - dump 유틸리티가 백업을 만들 시기를 결정하는 데 사용됩니다; 기본값은 0 으로 설정해야 합니다
- Pass - fsck 가 파일 시스템을 검사할 순서를 결정하는 데 사용됩니다; 값이 0 이면 검사되지 않습니다

항목을 추가하려면 위 항목 구문을 사용하여 `/etc/fstab` 파일을 직접 수정하십시오. 이 파일을 수정할 때는 주의하십시오; 실수하면 상황이 조금 더 어려워질 수 있습니다.

## Exercise

우리가 작업해 온 USB 드라이브를 `/etc/fstab`에 항목으로 추가하십시오. 재부팅하면 여전히 마운트되어 있는 것을 볼 수 있을 것입니다.

## Quiz Question

파일 시스템이 어떻게 마운트되어야 하는지 정의하는 데 사용되는 파일은 무엇입니까?

## Quiz Answer

/etc/fstab
