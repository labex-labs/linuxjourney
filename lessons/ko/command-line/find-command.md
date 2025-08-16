---
lang: "ko"
title: "find"
description: "Linux 'find' 명령어를 사용하여 파일과 디렉토리를 찾는 방법을 배우세요. 기본적인 검색 옵션을 알아보고 Linux 파일 관리 기술을 향상시키세요."
keywords: "Linux find 명령어, Linux 파일 찾기, Linux 디렉토리 검색, find 명령어 튜토리얼, Linux 파일 관리, 초보자 Linux, Linux 가이드"
---

## Lesson Content

시스템에 있는 이 모든 파일들 때문에 특정 파일을 찾으려고 하면 다소 혼란스러울 수 있습니다. 하지만 이를 위해 사용할 수 있는 명령어가 있습니다: `find`!

```bash
find /home -name puppies.jpg
```

`find`를 사용하려면 검색할 디렉토리와 찾을 대상을 지정해야 합니다. 이 경우, 우리는 `puppies.jpg`라는 이름의 파일을 찾으려고 합니다.

찾으려는 파일의 유형을 지정할 수 있습니다.

```bash
find /home -type d -name MyFolder
```

제가 찾으려는 파일의 유형을 디렉토리 (`d`) 로 설정했고, 여전히 `MyFolder`라는 이름으로 검색하고 있음을 알 수 있습니다.

한 가지 흥미로운 점은 `find`가 검색하는 디렉토리에서 멈추지 않는다는 것입니다. 해당 디렉토리가 가질 수 있는 모든 하위 디렉토리 내부도 검색합니다.

## Exercise

1. 루트 디렉토리에서 "net"이라는 단어가 포함된 파일을 찾으세요.

## Quiz Question

이름으로 검색하려면 `find`에 어떤 옵션을 지정해야 합니까?

## Quiz Answer

-name
