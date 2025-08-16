---
title: "커널 설치"
description: "Linux 커널을 설치하고 관리하는 방법을 배우십시오. 커널 버전을 확인하고, `uname -r` 및 apt 명령을 사용하는 방법을 알아보세요. Linux 커널 여정을 시작하세요!"
keywords: "Linux kernel, install kernel, uname -r, apt dist-upgrade, kernel management, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

이제 지루한 부분은 다 제쳐두고, 실제로 커널을 설치하고 수정하는 방법에 대해 이야기해 봅시다. 시스템에 여러 커널을 설치할 수 있습니다. 부팅 프로세스에 대한 수업에서 기억하시나요? GRUB 메뉴에서 부팅할 커널을 선택할 수 있습니다.

시스템에 설치된 커널 버전을 확인하려면 다음 명령을 사용하십시오:

```bash
$ uname -r
3.19.0-43-generic
```

`uname` 명령은 시스템 정보를 출력합니다. `-r` 옵션은 커널 릴리스 버전을 출력합니다.

Linux 커널은 다양한 방법으로 설치할 수 있습니다. 소스 패키지를 다운로드하여 소스에서 컴파일하거나, 패키지 관리 도구를 사용하여 설치할 수 있습니다.

```bash
sudo apt install linux-generic-lts-vivid
```

그리고 설치한 커널로 재부팅하기만 하면 됩니다. 간단하죠? 어느 정도는요. `linux-headers`, `linux-image-generic` 등과 같은 다른 Linux 패키지도 설치해야 합니다. 버전 번호를 지정할 수도 있으므로 위 명령은 다음과 같이 보일 수 있습니다: **`sudo apt install 3.19.0-43-generic`**

또는, 업데이트된 커널 버전만 원한다면 `dist-upgrade`를 사용하십시오. 이 명령은 시스템의 모든 패키지를 업그레이드합니다:

```bash
sudo apt dist-upgrade
```

다양한 커널 버전이 있습니다. 일부는 LTS (Long Term Support) 로 사용되고, 일부는 최신 버전입니다. 커널 버전 간의 호환성은 매우 다를 수 있으므로 다른 커널을 시도해 볼 수 있습니다.

## Exercise

1. 현재 사용 중인 커널 버전을 확인하십시오.
2. 사용 가능한 다양한 커널 버전을 조사하십시오.

## Quiz Question

시스템의 커널 버전을 어떻게 확인합니까?

## Quiz Answer

uname -r
