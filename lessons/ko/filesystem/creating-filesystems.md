---
title: "파일 시스템 생성"
description: "mkfs 를 사용하여 Linux 에서 파일 시스템을 생성하는 방법을 배우세요. 이 초보자 친화적인 가이드는 ext4 및 디스크 파티셔닝을 다룹니다. Linux 여정을 시작하세요!"
keywords: "mkfs, 파일 시스템 생성, ext4, Linux 파티셔닝, Linux 튜토리얼, 초보자 Linux, 디스크 관리, Linux 가이드"
---

## Lesson Content

이제 실제로 디스크를 분할했으니, 파일 시스템을 만들어 봅시다!

```bash
sudo mkfs -t ext4 /dev/sdb2
```

정말 간단하죠! **mkfs** (make filesystem) 도구를 사용하면 원하는 파일 시스템 유형과 위치를 지정할 수 있습니다. 새로 분할된 디스크에만 파일 시스템을 생성하거나, 오래된 디스크를 재분할할 때만 파일 시스템을 생성해야 합니다. 기존 파일 시스템 위에 새 파일 시스템을 생성하려고 하면 파일 시스템이 손상될 가능성이 높습니다.

## Exercise

USB 드라이브에 ext4 파일 시스템을 만드세요.

## Quiz Question

파일 시스템을 생성하는 데 사용되는 명령어는 무엇입니까?

## Quiz Answer

mkfs
