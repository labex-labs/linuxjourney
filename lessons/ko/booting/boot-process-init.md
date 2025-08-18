---
lang: "ko"
title: "부팅 과정: Init"
meta_title: "부팅 과정: Init - 시스템 부팅"
meta_description: "Linux init 시스템: System V, Upstart, systemd 에 대해 알아보세요. 부팅 과정에서의 역할과 서비스 관리 방법을 이해하세요. Linux 여정을 시작하세요!"
meta_keywords: "Linux init, systemd, System V init, Upstart, Linux 부팅 과정, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

이전 수업에서 init 에 대해 논의했으며, init 이 시작되는 첫 번째 프로세스이며 시스템의 다른 모든 필수 서비스를 시작한다는 것을 알고 있습니다. 하지만 어떻게 그럴까요?

Linux 에는 실제로 세 가지 주요 init 구현이 있습니다:

### System V init (sysv)

이것은 전통적인 init 시스템입니다. 시작 스크립트를 기반으로 프로세스를 순차적으로 시작하고 중지합니다. 머신의 상태는 runlevel 로 표시됩니다. 각 runlevel 은 다른 방식으로 머신을 시작하거나 중지합니다.

### Upstart

이것은 오래된 Ubuntu 설치에서 찾을 수 있는 init 입니다. Upstart 는 작업 (jobs) 과 이벤트 (events) 의 개념을 사용하며, 이벤트에 반응하여 특정 작업을 수행하는 작업을 시작함으로써 작동합니다.

### Systemd

이것은 init 의 새로운 표준이며, 목표 지향적입니다. 기본적으로 달성하고자 하는 목표가 있고, systemd 는 목표를 완료하기 위해 목표의 종속성을 충족시키려고 노력합니다.

각 시스템에 대해 더 자세히 알아볼 Init 시스템에 대한 전체 과정이 있습니다.

## Exercise

No exercises for this lesson.

## Quiz Question

init 의 최신 표준은 무엇입요?

## Quiz Answer

systemd
