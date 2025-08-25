---
index: 8
lang: "ko"
title: "swap"
meta_title: "swap - 파일 시스템"
meta_description: "Linux swap 공간, 작동 방식, swap 파티션 생성 및 관리 방법에 대해 알아보세요. 이 가이드를 통해 시스템의 메모리 사용량을 최적화하세요!"
meta_keywords: "Linux swap, mkswap, swapon, swapoff, /etc/fstab, 가상 메모리, Linux 초보자, Linux 튜토리얼"
---

## Lesson Content

이전 예제에서 파티션 테이블을 보는 방법을 보여드렸습니다. 그 예제를 다시 살펴보겠습니다. 특히 다음 줄을 살펴보겠습니다.

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

이 swap 파티션은 무엇일까요? swap 은 시스템에 가상 메모리를 할당하는 데 사용하는 것입니다. 메모리가 부족할 때 시스템은 이 파티션을 사용하여 유휴 프로세스의 메모리 조각을 디스크로 "스왑"하여 메모리 부족으로 인해 시스템이 느려지지 않도록 합니다.

### swap 공간으로 파티션 사용하기

`/dev/sdb2` 파티션을 swap 공간으로 사용하고 싶다고 가정해 봅시다.

1. 먼저, 파티션에 아무것도 없는지 확인합니다.
2. `mkswap /dev/sdb2`를 실행하여 swap 영역을 초기화합니다.
3. `swapon /dev/sdb2`를 실행합니다. 이렇게 하면 swap 장치가 활성화됩니다.
4. 부팅 시 swap 파티션을 유지하려면 `/etc/fstab` 파일에 항목을 추가해야 합니다. `sw`는 사용할 파일 시스템 유형입니다.
5. swap 을 제거하려면: `swapoff /dev/sdb2`.

일반적으로 메모리의 약 두 배에 해당하는 swap 공간을 할당해야 합니다. 그러나 오늘날의 최신 시스템은 일반적으로 충분히 강력하고 충분한 RAM 을 가지고 있습니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux swap 공간 및 가상 메모리 관리에 대한 이해를 강화하기 위한 실습 랩입니다.

1. **[Linux 에서 스왑 파일 생성 및 활성화](https://labex.io/ko/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - 시스템의 가상 메모리를 관리하는 데 중요한 기술인 스왑 파일을 생성하고 활성화하는 연습을 합니다.

이 랩은 실제 시나리오에서 swap 파티션의 개념을 적용하고 시스템 리소스 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

장치에서 swap 공간을 활성화하는 명령은 무엇입니까?

## Quiz Answer

swapon
