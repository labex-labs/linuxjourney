---
index: 7
lang: "ko"
title: "/etc/fstab"
meta_title: "/etc/fstab - 파일 시스템"
meta_description: "Linux 의 /etc/fstab에 대해 알아보고, 시작 시 파일 시스템 마운트를 구성하며, 장치 항목을 관리하는 방법을 배웁니다. 초보자를 위한 fstab 을 이해하세요!"
meta_keywords: "/etc/fstab, Linux fstab, 파일 시스템 마운트, Linux 부팅, fstab 튜토리얼, 초보자, 가이드"
---

## Lesson Content

시작 시 파일 시스템을 자동으로 마운트하려면 `/etc/fstab`("eff es tab"으로 발음하며 "eff stab"이 아님) 이라는 파일에 추가할 수 있습니다. 이 파일은 마운트되는 파일 시스템의 영구 목록을 포함합니다.

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

각 줄은 하나의 파일 시스템을 나타내며, 필드는 다음과 같습니다:

- UUID - 장치 식별자
- 마운트 지점 - 파일 시스템이 마운트되는 디렉터리
- 파일 시스템 유형
- 옵션 - 기타 마운트 옵션; 자세한 내용은 manpage 참조
- 덤프 - 덤프 유틸리티가 백업 시기를 결정하는 데 사용; 기본값은 0 으로 설정해야 합니다
- 패스 - fsck 가 파일 시스템을 검사할 순서를 결정하는 데 사용; 값이 0 이면 검사되지 않습니다

항목을 추가하려면 위 항목 구문을 사용하여 `/etc/fstab` 파일을 직접 수정하면 됩니다. 이 파일을 수정할 때는 주의해야 합니다. 실수하면 상황이 조금 더 어려워질 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! 파일 시스템을 관리하고 시스템 시작 시 올바르게 마운트되도록 하는 방법을 이해하는 데는 실습 경험이 중요합니다. 다음은 Linux 파일 시스템 관리 및 `/etc/fstab` 파일에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 파티션 및 파일 시스템 관리](https://labex.io/ko/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 파티션 생성, 포맷, 마운트 및 `/etc/fstab`을 사용한 영구 마운트 구성 연습.
2. **[Linux 에서 스왑 파일 생성 및 활성화](https://labex.io/ko/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - `/etc/fstab`에 항목이 포함되는 경우가 많은 스왑 파일 생성 및 활성화의 필수 관리 작업을 배웁니다.

이 랩들은 실제 시나리오에서 파일 시스템 마운트 및 구성 개념을 적용하고 Linux 에서 디스크 리소스를 관리하는 데 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

파일 시스템이 어떻게 마운트되어야 하는지 정의하는 데 사용되는 파일은 무엇입니까?

## Quiz Answer

/etc/fstab
