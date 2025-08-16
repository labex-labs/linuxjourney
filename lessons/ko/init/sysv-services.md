---
lang: "ko"
title: "System V 서비스"
description: "명령줄 도구를 사용하여 System V 서비스를 관리하는 방법을 배웁니다. 이 초보자 친화적인 Linux 튜토리얼을 통해 서비스를 나열, 시작, 중지 및 다시 시작하는 방법을 알아보세요."
keywords: "System V 서비스, Linux 서비스, service 명령, SysV init, Linux 튜토리얼, 초보자 Linux, 서비스 관리, Linux 가이드"
---

## Lesson Content

Sys V 서비스를 관리하는 데 사용할 수 있는 많은 명령줄 도구가 있습니다.

### List services

```bash
service --status-all
```

### Start a service

```bash
sudo service networking start
```

### Stop a service

```bash
sudo service networking stop
```

### Restart a service

```bash
sudo service networking restart
```

이 명령들은 Sys V init 시스템에만 국한되지 않습니다. Upstart 서비스도 관리하는 데 사용할 수 있습니다. Linux 는 더 전통적인 Sys V init 스크립트에서 벗어나려고 노력하고 있기 때문에, 이러한 전환을 돕기 위한 것들이 여전히 존재합니다.

## Exercise

몇 가지 서비스를 관리하고 상태를 변경해 보세요. 무엇을 관찰할 수 있나요?

## Quiz Question

Sys V 를 사용하여 `peanut`이라는 서비스의 작동을 중지하는 명령은 무엇입니까?

## Quiz Answer

sudo service peanut stop
