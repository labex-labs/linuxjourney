---
title: "커널 로깅"
description: "dmesg 및 kern.log 를 사용하여 Linux 커널 로깅에 대해 알아보세요. 부팅 메시지 및 하드웨어 문제를 이해합니다. 시스템 통찰력을 위해 커널 로그를 탐색합니다."
keywords: "dmesg, kern.log, Linux 로깅, 커널 메시지, 부팅 로그, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

### /var/log/dmesg

부팅 시 시스템은 커널 링 버퍼에 대한 정보를 기록합니다. 이는 하드웨어 드라이버, 커널 정보, 부팅 중 상태 등에 대한 정보를 보여줍니다. 이 로그 파일은 `/var/log/dmesg`에서 찾을 수 있으며, 부팅할 때마다 재설정됩니다. 지금은 이 파일의 용도를 알지 못할 수도 있지만, 부팅 중 문제가 발생하거나 하드웨어 문제가 발생할 경우 `dmesg`가 가장 먼저 확인해야 할 곳입니다. `dmesg` 명령어를 사용하여 이 로그를 볼 수도 있습니다.

### /var/log/kern.log

커널 정보를 볼 수 있는 또 다른 로그는 `/var/log/kern.log` 파일입니다. 이 파일은 시스템의 커널 정보와 이벤트를 기록하며, `dmesg` 출력도 기록합니다.

## Exercise

`dmesg` 및 `kern` 로그를 살펴보세요. 어떤 차이점을 발견했나요?

## Quiz Question

커널 부팅 메시지를 확인하는 데 사용할 수 있는 명령어는 무엇입니까?

## Quiz Answer

dmesg
