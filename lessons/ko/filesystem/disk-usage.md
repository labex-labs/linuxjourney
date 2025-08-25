---
index: 9
lang: "ko"
title: "디스크 사용량"
meta_title: "디스크 사용량 - 파일 시스템"
meta_description: "df 및 du 명령어를 사용하여 Linux 에서 디스크 사용량과 여유 공간을 확인하는 방법을 배우십시오. 두 명령어의 차이점과 사용 시기를 이해하십시오. Linux 디스크 관리 튜토리얼."
meta_keywords: "df command, du command, Linux 디스크 사용량, 여유 공간 확인, Linux 튜토리얼, 초보자 Linux, 디스크 관리, Linux 가이드"
---

## Lesson Content

디스크 활용도를 확인하는 데 사용할 수 있는 몇 가지 도구가 있습니다:

```bash
pete@icebox:~$ df -h
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

`df` 명령어는 현재 마운트된 파일 시스템의 활용도를 보여줍니다. `-h` 플래그는 사람이 읽기 쉬운 형식을 제공합니다. 장치가 무엇인지, 얼마나 많은 용량이 사용 가능하고 사용 중인지 확인할 수 있습니다.

디스크가 가득 차서 어떤 파일이나 디렉토리가 공간을 차지하는지 알고 싶다면 **du** 명령어를 사용할 수 있습니다.

```bash
du -h
```

이것은 현재 디렉토리의 디스크 사용량을 보여줍니다. `du -h /`로 루트 디렉토리를 엿볼 수 있지만, 다소 복잡해질 수 있습니다.

이 두 명령어는 구문이 너무 비슷해서 어떤 것을 사용해야 할지 기억하기 어려울 수 있습니다. **디스크**에 **남은 공간**이 얼마나 되는지 확인하려면 `df`를 사용하십시오. **디스크 사용량**을 확인하려면 `du`를 사용하십시오.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 에서 디스크 공간 관리 및 활용에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 파티션 및 파일 시스템 관리](https://labex.io/ko/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - `df` 및 `du`가 보고하는 기본 구조인 파일 시스템 생성, 포맷 및 마운트를 연습합니다.
2. **[Linux 에서 스왑 파일 생성 및 활성화](https://labex.io/ko/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - 디스크의 가상 메모리를 관리하는 방법을 배우십시오. 이는 디스크 공간에 영향을 미치는 시스템 리소스 관리의 중요한 측면입니다.

이 실습들은 실제 시나리오에 개념을 적용하고 디스크 리소스 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

디스크에 남은 공간이 얼마나 되는지 보여주는 데 사용되는 명령어는 무엇입니까?

## Quiz Answer

df
