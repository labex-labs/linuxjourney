---
index: 5
lang: "ko"
title: "파일 시스템 생성"
meta_title: "파일 시스템 생성 - 파일 시스템"
meta_description: "mkfs 를 사용하여 Linux 에서 파일 시스템을 생성하는 방법을 배웁니다. 이 초보자 친화적인 가이드는 ext4 및 디스크 분할을 다룹니다. Linux 여정을 시작하세요!"
meta_keywords: "mkfs, 파일 시스템 생성, ext4, Linux 파티션, Linux 튜토리얼, 초보자 Linux, 디스크 관리, Linux 가이드"
---

## Lesson Content

이제 실제로 디스크를 분할했으니, 파일 시스템을 만들어 봅시다!

```bash
sudo mkfs -t ext4 /dev/sdb2
```

정말 간단하죠! **mkfs** (make filesystem) 도구를 사용하면 원하는 파일 시스템 유형과 위치를 지정할 수 있습니다. 파일 시스템은 새로 분할된 디스크에만 만들거나, 기존 디스크를 재분할할 때만 만들어야 합니다. 기존 파일 시스템 위에 새 파일 시스템을 만들려고 하면 파일 시스템이 손상될 가능성이 높습니다.

## Exercise

연습하면 완벽해집니다! 다음은 Linux 파일 시스템 관리에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 파티션 및 파일 시스템 관리](https://labex.io/ko/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 이 실습에서는 Linux 에서 디스크 파티션 및 파일 시스템을 관리하는 방법을 배웁니다. fdisk 를 사용하여 새 파티션을 생성하고, `mkfs`를 사용하여 ext4 로 포맷하고, 마운트하고, /etc/fstab에 영구 마운트를 구성하고, 스왑 파티션을 생성하는 모든 작업을 안전한 보조 가상 디스크에서 수행합니다.

이 실습은 실제 시나리오에서 파일 시스템 생성 및 관리 개념을 적용하고 Linux 디스크 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

파일 시스템을 생성하는 데 사용되는 명령어는 무엇입니까?

## Quiz Answer

mkfs
