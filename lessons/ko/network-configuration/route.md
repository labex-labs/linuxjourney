---
title: "route"
description: "Linux route 및 ip 명령을 사용하여 네트워크 경로를 추가하고 삭제하는 방법을 배웁니다. 초보자 및 중급 사용자를 위한 라우팅 테이블 관리를 이해합니다."
keywords: "route command, ip route, add route, delete route, Linux networking, routing table, Linux tutorial, beginner guide"
---

## Lesson Content

`route` 명령을 사용하여 라우팅 테이블을 보는 방법에 대해 이미 논의했습니다. 경로를 수동으로 추가하거나 제거할 수 있습니다.

### 새 경로 추가

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

### 경로 삭제

```bash
sudo route del -net 192.168.2.1/23
```

**ip** 명령으로도 이러한 변경을 수행할 수 있습니다:

### 경로 추가

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

### 경로 삭제

```bash
$ ip route delete 192.168.2.1/23 via 10.11.12.3
or
$ ip route delete 192.168.2.1/23
```

## Exercise

이 레슨에는 연습 문제가 없지만, 여기서 논의된 명령에 대한 더 많은 정보를 man pages 에서 읽을 수 있습니다.

```bash
man route
```

```bash
man ip-route
```

## Quiz Question

경로를 삭제하는 명령 플래그는 무엇입니까?

## Quiz Answer

del
