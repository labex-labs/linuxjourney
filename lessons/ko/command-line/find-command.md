---
index: 14
lang: "ko"
title: "find"
meta_title: "find - 명령줄"
meta_description: "Linux 'find' 명령어를 사용하여 파일과 디렉토리를 찾는 방법을 배우세요. 기본적인 검색 옵션을 알아보고 Linux 파일 관리 기술을 향상시키세요."
meta_keywords: "Linux find 명령어, Linux 파일 찾기, Linux 디렉토리 검색, find 명령어 튜토리얼, Linux 파일 관리, 초보자 Linux, Linux 가이드"
---

## Lesson Content

시스템에 있는 이 모든 파일들 때문에 특정 파일을 찾으려고 하면 좀 혼란스러울 수 있습니다. 하지만, 이를 위해 사용할 수 있는 명령어가 있습니다: `find`!

```bash
find /home -name puppies.jpg
```

`find`를 사용하려면 검색할 디렉토리와 찾을 대상을 지정해야 합니다. 이 경우, 우리는 `puppies.jpg`라는 이름의 파일을 찾으려고 합니다.

찾으려는 파일의 유형을 지정할 수 있습니다.

```bash
find /home -type d -name MyFolder
```

보시다시피, 저는 찾으려는 파일의 유형을 디렉토리를 의미하는 `d`로 설정했고, 여전히 `MyFolder`라는 이름으로 검색하고 있습니다.

주목할 만한 한 가지 멋진 점은 `find`가 검색하는 디렉토리에서 멈추지 않는다는 것입니다. 해당 디렉토리가 가질 수 있는 모든 하위 디렉토리 내부도 찾아봅니다.

## Exercise

연습하면 완벽해집니다! 다음은 Linux 에서 파일과 디렉토리를 찾는 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux find 명령어: 파일 검색](https://labex.io/ko/labs/linux-linux-find-command-file-searching-219191)** - 이 랩은 다양한 기준에 따라 파일과 디렉토리를 검색하고 찾는 데 사용되는 다재다능한 유틸리티인 `find` 명령어에 대한 소개를 제공합니다. `find`를 사용하여 특정 파일을 찾는 연습을 하게 됩니다.
2. **[중요 시스템 리소스 발견](https://labex.io/ko/labs/linux-discover-critical-system-resources-388032)** - `find`를 포함하여 파일과 실행 파일을 찾는 데 필수적인 Linux 명령어를 배웁니다. 파일 시스템을 효율적으로 탐색하고 중요한 시스템 리소스를 발견하는 연습을 하게 됩니다.

이 랩들은 실제 시나리오에 개념을 적용하고 `find` 명령어를 효과적으로 사용하는 데 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

이름으로 검색하려면 `find`에 어떤 옵션을 지정해야 합니까?

## Quiz Answer

-name
