---
lang: "ko"
title: "niceness"
meta_description: "Linux niceness 와 프로세스 우선순위에 대해 알아보세요. nice 및 renice 명령을 이해하여 프로세스의 CPU 시간을 관리하세요. 시스템 성능을 향상시키세요!"
meta_keywords: "Linux niceness, 프로세스 우선순위, nice command, renice command, Linux 튜토리얼, CPU 스케줄링, 초보자 Linux, Linux 가이드"
---

## Lesson Content

컴퓨터에서 Chrome, Microsoft Word 또는 Photoshop 과 같은 여러 프로그램을 동시에 실행할 때, 이 프로세스들이 동시에 실행되는 것처럼 보일 수 있지만, 사실은 그렇지 않습니다.

프로세스는 타임 슬라이스 (time slice) 라고 불리는 짧은 시간 동안 CPU 를 사용합니다. 그런 다음 몇 밀리초 동안 일시 중지되고, 다른 프로세스가 작은 타임 슬라이스를 얻습니다. 기본적으로 프로세스 스케줄링은 이러한 라운드 로빈 (round-robin) 방식으로 이루어집니다. 모든 프로세스는 처리가 완료될 때까지 충분한 타임 슬라이스를 얻습니다. 커널은 이러한 모든 프로세스 전환을 처리하며, 대부분의 경우 아주 잘 작동합니다.

프로세스는 언제, 얼마나 오랫동안 CPU 시간을 얻을지 결정할 수 없습니다. 모든 프로세스가 정상적으로 작동한다면, 각 프로세스는 (대략) 동일한 양의 CPU 시간을 얻을 것입니다. 그러나 nice 값을 사용하여 커널의 프로세스 스케줄링 알고리즘에 영향을 줄 수 있는 방법이 있습니다. Niceness 는 다소 이상한 이름이지만, 이는 프로세스가 CPU 에 대한 우선순위를 결정하는 숫자를 가지고 있음을 의미합니다. 높은 숫자는 프로세스가 "nice"하여 CPU 에 대한 우선순위가 낮다는 것을 의미하고, 낮거나 음수 값은 프로세스가 그다지 "nice"하지 않아 가능한 한 많은 CPU 를 얻으려 한다는 것을 의미합니다.

```bash
top
```

지금 `NI` 열을 볼 수 있습니다. 이것은 프로세스의 niceness 수준입니다.

niceness 수준을 변경하려면 `nice` 및 `renice` 명령을 사용할 수 있습니다:

```bash
nice -n 5 apt upgrade
```

`nice` 명령은 새 프로세스의 우선순위를 설정하는 데 사용됩니다. `renice` 명령은 기존 프로세스의 우선순위를 설정하는 데 사용됩니다.

```bash
renice 10 -p 3245
```

## Exercise

어떤 프로세스들이 그다지 nice 하지 않으며, 그 이유는 무엇입니까?

## Quiz Question

프로세스가 더 많은 CPU 우선순위를 얻도록 하려면, 더 낮은 nice 숫자를 사용해야 합니까, 아니면 더 높은 nice 숫자를 사용해야 합니까?

## Quiz Answer

lower
