---
index: 4
lang: "ko"
title: "sysfs"
meta_title: "sysfs - 장치 정보"
meta_description: "sysfs 가 무엇이며 Linux 시스템에서 어떤 역할을 하는지 알아보세요. 이 가이드는 장치 정보를 위한 가상 파일시스템인 리눅스 /sys 디렉터리를 설명하고 /dev 와 비교합니다."
meta_keywords: "sysfs, sysfs 란, /sys, 리눅스 /sys, 리눅스 sys, sys 시스템, 가상 파일시스템, 리눅스 장치, /dev"
---

## Lesson Content

sysfs 파일 시스템은 장치 관리에서 /dev 디렉토리가 완전히 갖추지 못한 부분을 개선하기 위해 도입되었습니다. **리눅스에서 /sys 란 무엇인가**를 이해하는 것은 현대 시스템 관리의 핵심입니다.

### sysfs 란 무엇인가?

`sysfs`는 일반적으로 `/sys`에 마운트되는 가상 파일 시스템으로, 커널의 장치 모델에서 사용자 공간으로 커널 객체, 하드웨어 장치 및 드라이버에 대한 정보를 내보냅니다. 물리적 디스크의 파일과 달리, `/sys` 내의 파일과 디렉토리는 즉석에서 생성되며 **sys 시스템**의 현재 상태를 나타냅니다.

### linux /sys 디렉토리의 역할

**linux /sys** 디렉토리의 주요 목적은 시스템의 모든 장치에 대한 구조화된 보기를 제공하는 것입니다. 제조업체 및 모델, 장치가 연결된 위치, 현재 상태, 장치 계층 구조 내의 위치와 같은 세부 정보를 포함합니다.

여기서 보는 파일은 `/dev`의 장치 노드와 같지 않습니다. `/sys`를 통해 장치 자체와 직접 상호 작용하는 것이 아니라, 정보를 보거나 장치의 속성을 관리하는 데 사용합니다.

### sysfs 대 /dev

`/sys`와 `/dev` 모두 장치와 관련이 있지만 기능은 다릅니다.

- `/dev` 디렉토리는 프로그램이 장치 자체에 액세스할 수 있도록 하는 특수 파일인 장치 노드를 제공합니다.
- `/sys` 파일 시스템은 장치에 대한 정보를 보거나 장치를 관리하는 데 사용됩니다. 이는 기본 장치 모델을 노출합니다.

예를 들어, `/sys` 내의 블록 장치 디렉토리 내용을 살펴보겠습니다.

```bash
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
```

이 출력은 `sda` 하드 드라이브와 관련된 다양한 속성과 하위 디렉토리를 보여주며, `/dev/sda`만 보는 것보다 훨씬 자세한 보기를 제공합니다.

## Exercise

연습이 완벽하게 만듭니다! 리눅스에서 하드웨어 장치 탐색에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[리눅스에서 하드웨어 장치 탐색하기](https://labex.io/ko/labs/comptia-explore-hardware-devices-in-linux-590861)** - `/sys` 파일 시스템이 장치 정보를 제공하는 방식과 유사하게 리눅스 환경 내에서 하드웨어 장치를 식별하고 검사하는 연습을 합니다.

이 랩은 시스템 하드웨어에 대한 이해와 리눅스에서의 표현을 적용하고, 장치 탐색에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

장치에 대한 자세한 정보를 보는 데 사용되는 디렉토리는 무엇입니까? 영어로 답하십시오.

## Quiz Answer

/sys
