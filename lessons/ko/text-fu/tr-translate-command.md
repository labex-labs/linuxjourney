---
index: 13
lang: "ko"
title: "tr (변환)"
meta_title: "tr (변환) - Text-Fu"
meta_description: "문자 변환, 문자 삭제, 반복 문자 압축, 문자 클래스 사용, 텍스트 정리 예제로 배우는 Linux tr 명령어."
meta_keywords: "linux tr 명령어, tr 명령어, tr -d, tr -s, 문자 변환, 문자 삭제, 문자 클래스, 텍스트 처리 linux"
---

## Lesson Content

`tr` 명령어는 translate(변환)의 약자로, 표준 입력에서 문자를 변환, 삭제 또는 압축하는 명령줄 유틸리티입니다. 간단한 텍스트 조작에 유용하며, 다른 명령어의 출력을 처리할 때 파이프와 함께 자주 사용됩니다.

기본 구문은 다음과 같습니다:

```bash
tr [OPTIONS] SET1 [SET2]
```

`sed`나 `awk` 같은 도구와 달리, `tr`은 문자 단위로 작동합니다. 단어, 열, 정규 표현식을 같은 방식으로 이해하지 않습니다. 이로 인해 대소문자 변경, 숫자 제거, 반복된 공백 정규화 같은 작업에 빠르고 간단합니다.

### 기본 문자 변환

`tr`의 가장 일반적인 용도는 한 문자 집합을 다른 문자 집합으로 치환하는 것입니다. 예를 들어, 모든 소문자를 대문자로 쉽게 변환할 수 있습니다.

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

이 예제에서는 `echo`의 출력을 `tr` 명령어에 파이프로 전달했습니다. `tr` 명령어는 문자 범위 `a-z`를 대응하는 `A-Z` 범위의 문자로 변환했습니다.

한 문자씩 변환할 수도 있습니다:

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

`SET1`의 각 문자는 `SET2`의 같은 위치에 있는 문자로 매핑됩니다.

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

여기서 `a`는 `A`로, `b`는 `B`로, `c`는 `C`로 변환됩니다.

### -d 옵션으로 문자 삭제

또 다른 강력한 기능은 `-d` 옵션을 사용해 특정 문자를 삭제하는 것입니다. 텍스트 정리에 특히 유용합니다. 예를 들어, 문자열에서 모든 숫자를 제거하려면 다음과 같이 할 수 있습니다:

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

여기서 `tr -d`는 지정된 집합의 모든 문자, 즉 `0`부터 `9`까지의 문자를 삭제했습니다.

문자 클래스(character class)를 사용해 문자열에서 구두점(punctuation)을 제거할 수도 있습니다:

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

또한 줄바꿈 문자를 제거해 여러 줄을 한 줄로 합칠 수 있습니다:

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

### 반복 문자 압축

`tr` 명령어는 `-s` 옵션을 사용해 반복된 문자를 하나로 "압축"할 수 있습니다. 이는 불필요한 공백이 많은 텍스트를 정규화할 때 유용합니다.

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

이 경우 `tr -s ' '`는 여러 개의 공백을 하나의 공백으로 바꿔 출력 결과를 훨씬 깔끔하게 만들었습니다.

반복된 줄바꿈 문자도 압축할 수 있습니다:

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

### 문자 클래스 사용하기

문자 클래스는 `tr` 명령어를 더 읽기 쉽고 이식 가능하게 만듭니다. 자주 쓰이는 클래스는 다음과 같습니다:

- `[:lower:]`: 소문자
- `[:upper:]`: 대문자
- `[:digit:]`: 숫자
- `[:alpha:]`: 문자
- `[:alnum:]`: 문자와 숫자
- `[:space:]`: 공백 문자
- `[:punct:]`: 구두점 문자

예를 들어, 문자 클래스를 사용해 소문자를 대문자로 변환할 수 있습니다:

```bash
$ echo "linux journey" | tr '[:lower:]' '[:upper:]'
LINUX JOURNEY
```

`-c` 옵션과 `-d` 옵션을 함께 사용해 문자와 숫자를 제외한 모든 문자를 삭제할 수 있습니다. `-c` 옵션은 보완(complement), 즉 "이 집합에 속하지 않는 모든 것"을 의미합니다.

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

### 삭제와 압축 결합하기

텍스트 정리 시 옵션을 결합할 수 있습니다. 이 예제는 구두점을 삭제한 후 반복된 공백을 압축합니다:

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

탭으로 구분된 입력에서는 탭을 쉼표로 변환할 수 있습니다:

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

### 자주 쓰는 tr 옵션

가장 자주 사용하는 옵션은 다음과 같습니다:

- `-d`: `SET1`에 있는 문자를 삭제합니다.
- `-s`: `SET1`에 있는 반복 문자를 압축합니다.
- `-c`: `SET1`의 보완 집합을 사용합니다.
- `-t`: 변환 전에 `SET1`을 `SET2` 길이로 잘라냅니다.

### 자주 묻는 질문

**왜 tr은 파이프로부터 읽나요?** `tr`은 표준 입력을 읽기 때문에, `echo`, `cat`, `printf` 같은 텍스트를 출력하는 명령어 뒤에 자주 사용됩니다.

**tr은 단어를 바꾸나요?** 아닙니다. `tr`은 문자를 변환할 뿐 단어를 바꾸지 않습니다. 단어나 패턴 전체를 바꾸려면 `sed`를 사용하세요.

**왜 내 tr 명령어는 문자를 하나씩 바꾸나요?** 그것이 `tr`의 작동 방식입니다. `SET1`의 각 문자를 `SET2`의 대응 문자로 매핑합니다.

**왜 'a-z' 같은 집합을 따옴표로 감싸야 하나요?** 따옴표로 감싸면 셸이 특수 문자를 `tr`에 전달하기 전에 해석하는 것을 방지합니다.

## Exercise

배운 내용을 실습해 보세요. 다음 핸즈온 랩이 문자 변환과 텍스트 처리 이해를 강화하는 데 도움이 될 것입니다.

1. **[Linux tr 명령어: 문자 변환](https://labex.io/ko/labs/linux-linux-tr-command-character-translating-219198)** - 텍스트 스트림에서 문자 단위 변환을 위한 Linux `tr` 명령어를 배웁니다. 문자 변환, 특정 문자 삭제, 문자 클래스 사용, 반복 문자 압축을 연습할 수 있습니다.

이 랩을 통해 실제 상황에서 텍스트 조작 개념을 적용하고 `tr` 명령어 사용에 자신감을 가질 수 있습니다.

## Quiz Question

문자를 변환하는 데 사용되는 명령어는 무엇인가요? (영어 소문자만 사용해 답해주세요)

## Quiz Answer

tr
