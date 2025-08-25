---
index: 4
lang: "ko"
title: "sysfs"
meta_title: "sysfs - 장치"
meta_description: "sysfs, 자세한 Linux 장치 정보 및 관리를 위한 가상 파일 시스템에 대해 알아보세요. /sys 와 /dev 의 차이점을 이해하세요. Linux 여정을 시작하세요!"
meta_keywords: "sysfs, /sys 디렉토리, Linux 장치, 가상 파일 시스템, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

Sysfs 는 우리 시스템의 장치를 더 잘 관리하기 위해 오래 전에 만들어졌으며, 이는 `/dev` 디렉토리가 적절하게 수행하지 못했던 작업입니다. Sysfs 는 가상 파일 시스템이며, 대부분 `/sys` 디렉토리에 마운트됩니다. 이는 `/dev` 디렉토리에서 볼 수 있는 것보다 더 자세한 정보를 제공합니다. `/sys`와 `/dev` 두 디렉토리는 매우 비슷해 보이며 어떤 면에서는 그렇지만, 주요한 차이점이 있습니다. 기본적으로 `/dev` 디렉토리는 간단합니다. 다른 프로그램이 장치 자체에 접근할 수 있도록 하는 반면, `/sys` 파일 시스템은 정보를 보고 장치를 관리하는 데 사용됩니다.

`/sys` 파일 시스템은 기본적으로 제조업체 및 모델, 장치가 연결된 위치, 장치의 상태, 장치 계층 구조 등 시스템의 모든 장치에 대한 모든 정보를 포함합니다. 여기에 보이는 파일은 장치 노드가 아니므로 `/sys` 디렉토리에서 장치와 직접 상호 작용하는 것이 아니라 장치를 관리하는 것입니다.

`/sys` 디렉토리의 내용을 살펴보세요:

```bash
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
```

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 에서 하드웨어 장치 탐색에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 하드웨어 장치 탐색](https://labex.io/ko/labs/comptia-explore-hardware-devices-in-linux-590861)** - `/sys` 파일 시스템이 장치 정보를 제공하는 방식과 유사하게 Linux 환경 내에서 하드웨어 장치를 식별하고 검사하는 연습을 합니다.

이 랩은 시스템 하드웨어 및 Linux 에서의 표현을 이해하는 개념을 적용하고 장치 탐색에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

장치에 대한 자세한 정보를 보는 데 사용되는 디렉토리는 무엇입니까?

## Quiz Answer

/sys
