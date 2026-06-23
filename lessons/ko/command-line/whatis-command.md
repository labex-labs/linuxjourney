---
index: 17
lang: "ko"
title: "whatis"
meta_title: "whatis - 커맨드 라인"
meta_description: "man 페이지에서 한 줄 명령어 설명을 얻고 여러 매뉴얼 섹션을 이해하는 Linux whatis 명령어를 예제와 함께 배워보세요."
meta_keywords: "whatis 명령어, 리눅스 whatis, 명령어 설명 리눅스, man 페이지 요약, 커맨드 라인 도움말, apropos"
---

## Lesson Content

리눅스 커맨드 라인을 탐색하다 보면 수많은 명령어를 접하게 됩니다. 특정 명령어가 무슨 역할을 하는지 잊어버리는 것은 자연스러운 일입니다. 다행히도 이를 도와주는 간단한 유틸리티가 있습니다.

### whatis 명령어란?

`whatis` 명령어는 명령어의 매뉴얼 페이지에서 간결한 한 줄 설명을 보여줍니다. 전체 man 페이지를 읽지 않고도 명령어의 주요 기능을 빠르게 확인할 수 있는 방법입니다.

### whatis 명령어 사용법

`whatis` 사용법은 간단합니다. `whatis` 뒤에 알고 싶은 명령어를 입력하세요.

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

### 출력 결과 이해하기

`whatis`가 제공하는 설명은 명령어 매뉴얼 페이지의 `NAME` 섹션에서 가져옵니다. 만약 이름이 여러 매뉴얼 섹션에 걸쳐 있다면, `whatis`는 여러 줄을 표시할 수 있습니다.

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

괄호 안의 숫자는 매뉴얼 페이지 섹션 번호입니다.

### whatis, man, apropos 차이점

- `whatis ls`: 정확한 명령어 이름에 대한 한 줄 설명을 보여줍니다.
- `man ls`: 전체 매뉴얼 페이지를 엽니다.
- `apropos keyword`: 매뉴얼 페이지 설명에서 키워드를 검색합니다.

예를 들어:

```bash
$ apropos password
```

명령어 이름은 알지만 기능이 기억나지 않을 때 `whatis`를 사용하세요.

### 자주 묻는 질문

**whatis이 "nothing appropriate"라고 나오는 이유는?** 해당 명령어의 매뉴얼 페이지가 설치되어 있지 않거나, 매뉴얼 데이터베이스를 업데이트해야 할 수 있습니다.

**whatis이 명령어 옵션을 보여주나요?** 아닙니다. 옵션은 `man COMMAND` 또는 `COMMAND --help`를 사용하세요.

**whatis과 which는 같은 건가요?** 아닙니다. `whatis`은 명령어를 설명하고, `which`는 실행 파일 경로를 보여줍니다.

## Exercise

연습이 완벽을 만듭니다! `whatis` 명령어에 대한 특정 실습은 없지만, 명령어와 파일 정보를 찾는 방법을 이해하는 것은 매우 중요합니다. 다음은 리눅스에서 명령어와 파일을 찾는 이해를 강화할 수 있는 실습들입니다:

1. **[Linux which Command: Command Locating](https://labex.io/ko/labs/linux-linux-which-command-command-locating-215210)** - `which` 명령어를 사용해 실행 파일 위치를 찾고 시스템 PATH에서 명령어 우선순위를 이해하는 연습을 합니다.
2. **[Linux whereis Command: File and Command Finding](https://labex.io/ko/labs/linux-linux-whereis-command-file-and-command-finding-215211)** - `whereis`를 사용해 명령어의 바이너리, 소스, 매뉴얼 페이지를 찾으며 명령어 구조를 깊이 이해합니다.
3. **[Discover Critical System Resources](https://labex.io/ko/labs/linux-discover-critical-system-resources-388032)** - `which`, `whereis`, `find`를 결합해 파일 시스템을 효율적으로 탐색하고 중요한 시스템 리소스를 발견하는 도전 과제입니다.

이 실습들은 실제 상황에서 명령어와 파일 탐색 개념을 적용하고 필수 리눅스 유틸리티 사용에 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

명령어의 간단한 설명을 볼 수 있는 명령어는 무엇인가요? 영어 소문자로 답해주세요.

## Quiz Answer

whatis
