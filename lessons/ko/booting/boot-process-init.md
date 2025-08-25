---
index: 5
lang: "ko"
title: "부팅 프로세스: Init"
meta_title: "부팅 프로세스: Init - 시스템 부팅"
meta_description: "Linux init 시스템: System V, Upstart, systemd 에 대해 알아보세요. 부팅 프로세스에서 이들의 역할과 서비스 관리 방법을 이해하세요. Linux 여정을 시작하세요!"
meta_keywords: "Linux init, systemd, System V init, Upstart, Linux 부팅 프로세스, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

우리는 이전 수업에서 init 에 대해 논의했으며, init 이 시작되는 첫 번째 프로세스이며 시스템의 다른 모든 필수 서비스를 시작한다는 것을 알고 있습니다. 하지만 어떻게 그럴까요?

Linux 에는 실제로 세 가지 주요 init 구현이 있습니다:

### System V init (sysv)

이것은 전통적인 init 시스템입니다. 시작 스크립트를 기반으로 프로세스를 순차적으로 시작하고 중지합니다. 기계의 상태는 런레벨로 표시됩니다. 각 런레벨은 다른 방식으로 기계를 시작하거나 중지합니다.

### Upstart

이것은 오래된 Ubuntu 설치에서 찾을 수 있는 init 입니다. Upstart 는 작업과 이벤트의 개념을 사용하며, 이벤트에 대한 응답으로 특정 작업을 수행하는 작업을 시작함으로써 작동합니다.

### Systemd

이것은 init 의 새로운 표준입니다. 목표 지향적입니다. 기본적으로 달성하고자 하는 목표가 있고, systemd 는 목표를 완료하기 위해 목표의 종속성을 충족시키려고 노력합니다.

우리는 이 시스템들을 더 자세히 다룰 Init 시스템에 대한 전체 과정을 가지고 있습니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 프로세스와 시스템이 프로세스를 관리하는 방법에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864)** - 포그라운드 및 백그라운드 프로세스와 상호 작용하고, `ps`로 검사하고, `top`으로 리소스를 모니터링하고, `kill`로 종료하는 연습을 합니다. 이 랩은 `init`이 작동하는 방식의 기본이 되는 프로세스의 수명 주기 및 제어를 이해하는 데 도움이 될 것입니다.

이 랩은 실제 시나리오에 개념을 적용하고 Linux 프로세스 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

init 의 최신 표준은 무엇입니까?

## Quiz Answer

systemd
