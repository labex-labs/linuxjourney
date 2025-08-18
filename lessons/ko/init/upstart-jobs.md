---
index: 4
lang: "ko"
title: "Upstart 작업"
meta_title: "Upstart 작업 - Init"
meta_description: "initctl 명령을 사용하여 Linux 에서 Upstart 작업을 관리하는 방법을 배웁니다. 작업 상태를 이해하고 서비스를 시작, 중지 및 재시작합니다. Linux 시스템 관리 기술을 향상시키세요."
meta_keywords: "Upstart 작업, initctl, Linux 서비스, 시스템 관리, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

Upstart 는 많은 이벤트와 작업을 트리거하여 실행할 수 있습니다. 안타깝게도 이벤트나 작업이 어디에서 시작되었는지 쉽게 확인할 수 있는 방법이 없으므로 `/etc/init`에 있는 작업 구성을 살펴보아야 합니다. 대부분의 경우 Upstart 작업 구성 파일을 볼 필요는 없지만, 특정 작업을 더 쉽게 제어하고 싶을 것입니다. Upstart 시스템에서 사용할 수 있는 유용한 명령이 많이 있습니다.

### View jobs

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

Upstart 작업 목록과 적용된 다양한 상태를 볼 수 있습니다. 각 줄에서 작업 이름은 첫 번째 값이며, 두 번째 필드 (`/` 앞) 는 실제로 작업의 목표입니다. 세 번째 값 (`/` 뒤) 은 현재 상태입니다. 따라서 `shutdown` 작업은 결국 중지되기를 원하지만 현재 대기 상태임을 알 수 있습니다. 작업을 시작하거나 중지하면 작업 상태와 목표가 변경됩니다.

### View specific job

```plaintext
initctl status networking
networking start/running
```

Upstart 작업 구성 파일을 작성하는 방법에 대한 자세한 내용은 다루지 않겠지만, 이미 이러한 구성에서 작업이 중지, 시작 및 재시작된다는 것을 알고 있습니다. 이러한 작업은 또한 이벤트를 발생시켜 다른 작업을 시작할 수 있습니다. Upstart 작업의 수동 명령을 살펴보겠지만, 궁금하다면 `.conf` 파일을 더 자세히 살펴보아야 합니다.

### Manually start a job

```bash
sudo initctl start networking
```

### Manually stop a job

```bash
sudo initctl stop networking
```

### Manually restart a job

```bash
sudo initctl restart networking
```

### Manually emit an event

```bash
sudo initctl emit some_event
```

## Exercise

Upstart 작업 목록을 관찰하십시오. 이제 오늘 배운 명령 중 하나로 작업 상태를 변경하십시오. 그 후에 무엇을 알아차렸습니까?

## Quiz Question

`peanuts`라는 Upstart 작업을 수동으로 재시작하려면 어떻게 해야 합니까?

## Quiz Answer

sudo initctl restart peanuts
