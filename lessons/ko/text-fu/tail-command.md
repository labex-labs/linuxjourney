---
title: "tail"
description: "`tail` 명령을 사용하여 Linux 에서 파일 끝을 보고 로그를 모니터링하는 방법을 배웁니다. 실시간 업데이트를 위한 `tail -f`를 알아보세요. Linux 여정을 시작하세요!"
keywords: "tail command, Linux tail, tail -f, 로그 보기, Linux 튜토리얼, Linux 초보자, Linux 가이드"
---

## Lesson Content

`head` 명령과 유사하게, `tail` 명령은 기본적으로 파일의 마지막 10 줄을 보여줍니다.

```bash
tail /var/log/syslog
```

`head`와 마찬가지로, 보고 싶은 줄 수를 변경할 수 있습니다.

```bash
tail -n 10 /var/log/syslog
```

사용할 수 있는 또 다른 훌륭한 옵션은 `-f` (follow) 플래그입니다. 이 플래그는 파일이 커짐에 따라 파일을 계속 추적합니다. 한번 시도해보고 어떤 일이 일어나는지 확인해보세요.

```bash
tail -f /var/log/syslog
```

시스템과 상호 작용하는 동안 `syslog` 파일은 계속 변경되며, `tail -f`를 사용하면 해당 파일에 추가되는 모든 내용을 볼 수 있습니다.

## Exercise

`tail`의 man 페이지를 보고 우리가 논의하지 않은 다른 명령들을 읽어보세요.

```bash
man tail
```

## Quiz Question

`tail`에서 파일을 추적하는 데 사용되는 플래그는 무엇입니까?

## Quiz Answer

-f
