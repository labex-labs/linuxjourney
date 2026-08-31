---
lesson_id: "tr-translate-command"
course_id: "text-fu"
lang: "ko"
order_index: 13
title: "tr (변환)"
description: "표준 입력 스트림에서 문자 집합을 변환하고 삭제하며 반복을 압축하는 방법을 배웁니다."
meta_title: "tr (변환) - Text-Fu"
meta_description: "문자 변환, 문자 삭제, 반복 압축, 문자 클래스 사용, 텍스트 정리를 위한 예제로 Linux tr 명령어를 배웁니다."
meta_keywords: "linux tr 명령어, tr 명령어, tr -d, tr -s, 문자 변환, 문자 삭제, 문자 클래스, linux 텍스트 처리"
---

translate의 약자인 `tr` 명령어는 표준 입력에서 읽은 문자를 변환하거나 삭제하거나 반복을 압축합니다. 일반적인 입력 파일 피연산자를 받지 않으므로 파이프나 입력 리디렉션으로 데이터를 제공해야 합니다.

기본 구문은 다음과 같습니다.

```bash
tr [OPTIONS] SET1 [SET2]
```

`tr`은 단어나 일반 정규 표현식이 아니라 문자 집합을 다룹니다. 변환이 완전한 단어, 줄 구조 또는 주변 문맥에 의존한다면 다른 도구를 사용하세요.

## 문자 변환하기

집합이 두 개이면 `SET1`의 문자가 위치에 따라 `SET2`의 문자에 대응합니다.

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

여기서는 소문자 범위의 각 위치가 대응하는 대문자 위치에 매핑됩니다. 집합 표현식은 쉘이 바꾸지 않고 전달하도록 따옴표로 묶으세요.

한 문자를 다른 문자로 바꿀 수도 있습니다.

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

`SET1`에 없는 문자는 변경되지 않은 채 통과합니다.

:::single-choice{#tr-map-characters}
`printf '%s\n' 'abc123' | tr 'abc' 'ABC'`는 무엇을 출력하나요?

::option[`ABCABC`]{#tr-uppercase-digits explanation="숫자는 원본 집합의 구성원이 아니므로 `tr`은 숫자를 문자로 바꾸지 않습니다."}
::option[`ABC123`]{#tr-uppercase-abc .correct explanation="`a`, `b`, `c`는 각각 `ABC`의 같은 위치 문자에 매핑되고 숫자는 바뀌지 않습니다."}
::option[`abc123ABC`]{#tr-append-set explanation="`tr`은 일치하는 입력 문자를 변환하며 대상 집합을 스트림 뒤에 추가하지 않습니다."}
:::

## 문자 삭제하기

한 집합과 함께 `-d`를 사용하면 일치하는 모든 문자를 제거합니다.

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

각 숫자는 독립적으로 제거됩니다. `tr`이 완전한 숫자 토큰을 식별하는 것은 아닙니다.

문자 클래스는 현재 로캘에서 정의한 문자 그룹을 나타낼 수 있습니다.

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

줄 바꿈을 삭제하면 대체 구분 기호를 넣지 않고 입력 줄이 이어집니다.

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

:::single-choice{#tr-delete-digits}
다른 문자는 그대로 두고 표준 입력에서 모든 숫자를 제거하는 명령어는 무엇인가요?

::option[`tr -d '[:digit:]'`]{#tr-delete-digit-class .correct explanation="`-d` 옵션은 입력 스트림에서 숫자 클래스에 속하는 모든 문자를 삭제합니다."}
::option[`tr -s '[:digit:]'`]{#tr-squeeze-digits explanation="`-s` 옵션은 반복되는 숫자를 압축하지만 각 연속 구간에서 문자 하나는 남깁니다."}
::option[`tr '[:digit:]'`]{#tr-one-set-no-delete explanation="변환에는 보통 두 번째 집합이 필요합니다. 집합 하나만으로는 삭제를 요청하지 않습니다."}
:::

## 반복 문자 압축하기

`-s SET`을 사용하면 나열된 문자의 각 연속 구간을 해당 문자 하나로 바꿉니다.

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

이 집합에는 일반 공백 하나만 있으므로 탭과 줄 바꿈은 압축되지 않습니다.

반복된 줄 바꿈도 압축할 수 있습니다.

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

:::single-choice{#tr-squeeze-spaces}
표준 입력에서 일반 공백의 모든 연속 구간을 공백 하나로 줄이는 명령어는 무엇인가요?

::option[`tr -s ' '`]{#tr-squeeze-space .correct explanation="`-s` 옵션은 제공한 집합에 속하는 반복 문자를 압축하며 이 집합에는 일반 공백 하나가 있습니다."}
::option[`tr -d ' '`]{#tr-delete-space explanation="`-d` 옵션은 연속 구간마다 하나를 남기지 않고 모든 일반 공백을 제거합니다."}
::option[`tr ' ' ''`]{#tr-empty-destination explanation="빈 변환 집합은 압축을 요청하는 명확하고 이식 가능한 방법이 아닙니다. 반복 문자에는 `-s`를 사용하세요."}
:::

## 문자 클래스와 여집합 사용하기

많은 로캘에서 문자 클래스는 직접 작성한 범위보다 의도를 명확하게 표현합니다. 자주 쓰는 클래스는 다음과 같습니다.

- `[:lower:]`: 소문자
- `[:upper:]`: 대문자
- `[:digit:]`: 숫자
- `[:alpha:]`: 문자
- `[:alnum:]`: 문자와 숫자
- `[:space:]`: 공백 문자
- `[:punct:]`: 문장 부호

예를 들어 문자 클래스로 소문자 텍스트를 대문자로 변환합니다.

```bash
$ echo "linux journey" | tr '[:lower:]' '[:upper:]'
LINUX JOURNEY
```

`-c` 옵션은 `SET1`의 여집합, 즉 집합에 없는 모든 문자를 뜻합니다. 선택한 종류의 문자만 남기려면 `-d`와 함께 사용합니다.

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

줄 바꿈도 영숫자가 아니므로 함께 제거됩니다. 레코드 경계가 중요하면 구분 기호를 의도적으로 추가하거나 보존하세요.

:::single-choice{#tr-keep-alphanumeric}
`tr -cd '[:alnum:]'`는 표준 입력에 무엇을 하나요?

::option[영숫자를 삭제하고 나머지를 모두 유지합니다.]{#tr-delete-alnum explanation="여집합은 `-d`가 대상으로 삼는 문자를 바꾸므로 영숫자 집합 자체는 유지됩니다."}
::option[영숫자가 아닌 모든 문자를 삭제합니다.]{#tr-delete-nonalnum .correct explanation="`-c`가 영숫자 집합의 여집합을 만들고 `-d`가 그 결과인 비영숫자 집합을 삭제합니다."}
::option[모든 문자와 숫자를 대문자로 바꿉니다.]{#tr-uppercase-alnum explanation="대상 변환 집합이 없으므로 대소문자 변환을 수행하지 않습니다."}
:::

## 스트림 변환 구성하기

여러 변환을 별도 단계로 표현하는 편이 명확하면 `tr` 프로세스 여러 개를 연결할 수 있습니다.

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

단순한 탭 구분 입력에서는 탭 문자를 쉼표로 변환합니다.

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

`tr`은 표준 입력을 읽으므로 `<`로 파일을 제공할 수 있습니다.

```bash
$ tr '[:lower:]' '[:upper:]' < names.txt
```

결과를 저장하려면 표준 출력을 다른 파일로 리디렉션하세요. 입력 경로로 다시 리디렉션하면 쉘이 `tr`이 읽기 전에 파일을 비우므로 그렇게 하지 마세요.

:::single-choice{#tr-read-file-input}
`tr`이 `names.txt`를 표준 입력으로 읽고 소문자를 대문자로 변환하게 하는 명령어는 무엇인가요?

::option[`tr names.txt '[:lower:]' '[:upper:]'`]{#tr-file-operand explanation="`tr`은 이런 방식으로 일반 입력 파일 이름을 받지 않으며 추가 피연산자로 인해 구문이 잘못됩니다."}
::option[`tr -d '[:lower:]' < names.txt`]{#tr-delete-lowercase explanation="파일은 올바르게 읽지만 소문자를 변환하지 않고 삭제합니다."}
::option[`tr '[:lower:]' '[:upper:]' < names.txt`]{#tr-input-redirection .correct explanation="쉘이 `names.txt`를 표준 입력으로 열고 `tr`은 소문자 클래스를 대문자 클래스에 매핑합니다."}
:::

문자 단위 스트림 변환을 연습하려면 다음 실습을 진행해 보세요.

1. **[Linux tr 명령어: 문자 변환](https://labex.io/ko/labs/linux-linux-tr-command-character-translating-219198)** - 텍스트 스트림에서 문자 변환, 특정 문자 삭제, 문자 클래스 사용, 반복 문자 압축을 연습합니다.

## 요약

이제 집중된 `tr` 작업으로 문자 스트림을 변환할 수 있습니다.

1. 대응하는 집합 사이에서 문자를 매핑할 수 있습니다.
2. `-d`로 선택한 문자를 삭제할 수 있습니다.
3. `-s`로 반복 문자를 압축할 수 있습니다.
4. 로캘을 고려하는 클래스와 여집합을 의도적으로 사용할 수 있습니다.
5. 파일 이름 피연산자 대신 표준 입력으로 데이터를 제공할 수 있습니다.
