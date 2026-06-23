---
index: 14
lang: "ko"
title: "find"
meta_title: "find - 명령줄 명령어"
meta_description: "이름, 유형, 크기, 수정 시간으로 검색하고 일치하는 파일에 작업을 실행하는 Linux find 명령어를 예제와 함께 배워보세요."
meta_keywords: "리눅스 find 명령어, find 명령어, 리눅스에서 파일 찾기, 이름으로 찾기, 유형으로 찾기, 크기로 찾기, mtime으로 찾기, find exec"
---

## Lesson Content

시스템에 수많은 파일이 있을 때 특정 파일을 찾는 것은 어려울 수 있습니다. `find` 명령어는 이름, 유형, 크기, 수정 시간과 같은 기준을 사용하여 디렉터리 트리를 검색합니다.

### Using the find Command

기본 구문은 다음과 같습니다:

```bash
find [PATH] [EXPRESSION]
```

검색할 디렉터리와 찾고자 하는 기준을 지정합니다.

예를 들어 `/home` 디렉터리와 그 하위 디렉터리에서 `puppies.jpg`라는 파일을 찾으려면 다음과 같이 사용합니다:

```bash
$ find /home -name puppies.jpg
```

검색은 기본적으로 재귀적이므로 `find /home`은 `/home`과 그 하위 디렉터리를 모두 검색합니다.

### Searching by Name and Type

`find`의 가장 일반적인 용도 중 하나는 파일 이름으로 검색하는 것입니다. `-name` 옵션은 이름을 정확히 일치시키거나 셸 스타일 패턴으로 일치시킵니다.

```bash
$ find . -name "*.txt"
```

검색하려는 항목의 유형을 지정할 수도 있습니다. `-type` 옵션이 이 용도로 사용됩니다. 예를 들어, 파일 대신 디렉터리를 찾으려면 `d`를 사용할 수 있습니다.

```bash
$ find /home -type d -name MyFolder
```

이 명령어에서는 유형을 디렉터리인 `d`로 설정하고 `MyFolder`라는 이름의 항목을 찾고 있습니다. 일반 파일만 검색하려면 `-type f`를 사용합니다.

### Searching by Size and Time

파일 크기로 검색할 수 있습니다:

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

첫 번째 명령은 10메가바이트보다 큰 파일을 찾고, 두 번째는 1킬로바이트보다 작은 파일을 찾습니다.

수정 시간으로도 검색할 수 있습니다:

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime -7`은 최근 7일 이내에 수정된 파일을 의미합니다. `-mtime +30`은 30일 이전에 수정된 파일을 의미합니다.

### Running Actions on Results

기본적으로 `find`는 일치하는 경로를 출력합니다. `-print`, `-delete`, `-exec`와 같은 작업을 추가할 수 있습니다.

일치 항목을 명시적으로 출력하기:

```bash
$ find . -name "*.log" -print
```

각 일치 항목에 대해 `ls -l` 실행하기:

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

`{}` 자리 표시자는 각 일치하는 경로로 대체됩니다. 이스케이프된 세미콜론은 명령어의 끝을 표시합니다.

`-delete`와 같은 파괴적인 작업을 사용할 때는 주의하세요. 먼저 `-delete` 없이 동일한 검색을 실행하여 일치 항목을 확인하세요.

### Common find Options

- `-name PATTERN`: 파일 이름으로 일치시킴.
- `-iname PATTERN`: 대소문자를 구분하지 않고 파일 이름으로 일치시킴.
- `-type f`: 일반 파일과 일치.
- `-type d`: 디렉터리와 일치.
- `-size +10M`: 10메가바이트보다 큰 파일과 일치.
- `-mtime -7`: 최근 7일 이내에 수정된 파일과 일치.
- `-maxdepth N`: `find`가 검색할 최대 깊이를 제한.

### Common Questions

**왜 find가 "Permission denied"를 표시하나요?** 사용자가 일부 디렉터리를 읽을 권한이 없기 때문입니다. 더 좁은 경로를 검색하거나 적절한 권한으로 실행하세요.

**왜 "*.txt" 같은 패턴을 따옴표로 감싸야 하나요?** 따옴표를 사용하면 셸이 와일드카드를 확장하지 않고 `find`가 패턴을 그대로 받게 됩니다.

**find는 재귀적 검색을 하나요?** 네, 기본적으로 하위 디렉터리를 검색합니다.

## Exercise

`find` 명령어를 숙달하려면 연습이 중요합니다. 다음 실습을 통해 파일과 디렉터리 찾기 이해를 강화하세요:

1. **[Linux find Command: File Searching](https://labex.io/ko/labs/linux-linux-find-command-file-searching-219191)** - 이 실습은 다양한 기준으로 파일과 디렉터리를 검색하는 다용도 유틸리티인 `find` 명령어 소개를 제공합니다. 특정 파일을 찾는 연습을 하게 됩니다.
2. **[Discover Critical System Resources](https://labex.io/ko/labs/linux-discover-critical-system-resources-388032)** - `find`를 포함한 필수 Linux 명령어를 배우고 파일 시스템을 효율적으로 탐색하며 중요한 시스템 리소스를 발견하는 연습을 합니다.

이 실습들은 실제 시나리오에서 개념을 적용하고 `find` 명령어를 효과적으로 사용하는 자신감을 키우는 데 도움이 됩니다.

## Quiz Question

`find` 명령어에서 이름으로 검색하려면 어떤 옵션을 지정해야 하나요? 영어 옵션만, 형식에 맞게 (예: -option) 답해주세요.

## Quiz Answer

-name
