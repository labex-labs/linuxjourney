---
lesson_id: "grep-command"
course_id: "text-fu"
lang: "ko"
order_index: 16
title: "grep"
description: "고정 문자열이나 정규 표현식으로 줄을 선택하고 grep 결과를 해석하는 방법을 배웁니다."
meta_title: "grep - Text-Fu"
meta_description: "강력한 Linux grep 명령어로 텍스트 패턴을 검색하는 방법을 배웁니다. 기본 사용법, grep -e 명령어, 계산을 위한 grep -c와 효과적인 텍스트 처리에 필요한 옵션을 다룹니다."
meta_keywords: "grep 명령어, grep -e 명령어, grep -c, grep -f, grep -o, grep -e 예제, linux grep, 텍스트 검색, 패턴 일치, 텍스트 처리, linux 튜토리얼"
---

`grep` 명령어는 패턴과 일치하는 입력 줄을 선택합니다. 지정한 파일이나 표준 입력을 검색하고 일치 항목 주변의 문맥을 출력하거나 선택한 줄을 세며 종료 상태로 일치 항목이 있었는지 전달할 수 있습니다.

## 파일에서 일치하는 줄 찾기

패턴 뒤에 입력 파일을 하나 이상 전달합니다.

```bash
$ grep 'fox' sample.txt
```

기본적으로 GNU `grep`은 패턴을 기본 정규 표현식으로 해석하고 선택한 모든 줄을 출력합니다. 공백과 쉘 메타문자를 쉘이 먼저 해석하지 않도록 패턴을 따옴표로 묶으세요.

패턴을 정규 표현식이 아닌 고정 문자열로 처리해야 할 때는 `-F`를 사용합니다.

```bash
$ grep -F 'price: $5.00' products.txt
```

:::single-choice{#grep-fixed-string}
패턴 문자를 정규 표현식 구문으로 처리하지 않고 `products.txt`에서 문자 그대로 `price: $5.00`을 검색하는 명령어는 무엇인가요?

::option[`grep -F 'price: $5.00' products.txt`]{#grep-fixed-price .correct explanation="`-F`는 고정 문자열 일치를 선택하고 작은따옴표는 달러 기호를 쉘 확장에서 보호합니다."}
::option[`grep -E 'price: $5.00' products.txt`]{#grep-extended-price explanation="`-E`는 확장 정규 표현식을 활성화하며 여기서는 `$`와 `.`가 문자 그대로가 아니라 특별한 의미를 갖습니다."}
::option[`grep -v 'price: $5.00' products.txt`]{#grep-invert-price explanation="`-v`는 일치하지 않는 줄을 선택하고 기본적으로 여전히 정규 표현식 해석을 사용합니다."}
:::

## 패턴 구문 선택하기

GNU `grep`에는 자주 쓰는 패턴 모드 세 가지가 있습니다.

- 기본값: 기본 정규 표현식
- `-E`: 백슬래시 없이 `|`, `+`, `?` 같은 연산자를 포함하는 확장 정규 표현식
- `-F`: 정규 표현식 연산자가 없는 고정 문자열

`^`와 `$` 같은 앵커는 줄의 시작과 끝에 일치합니다. 텍스트 목록에서 문자 그대로 `.txt` 접미사로 끝나는 파일 이름을 찾으려면 다음과 같이 실행합니다.

```bash
$ grep -E '\.txt$' filenames.txt
```

백슬래시는 점을 문자 그대로 만듭니다. 정규 표현식에서 이스케이프하지 않은 `.`은 임의의 문자 하나와 일치합니다.

:::single-choice{#grep-literal-txt-suffix}
문자 그대로 `.txt` 접미사로 끝나는 줄에 일치하는 확장 정규 표현식은 무엇인가요?

::option[`'.txt$'`]{#grep-anychar-txt explanation="점이 이스케이프되지 않아 문자 그대로의 마침표가 아니라 `txt` 앞의 임의 문자 하나와 일치합니다."}
::option[`'\.txt$'`]{#grep-dot-txt-end .correct explanation="`\.`은 문자 그대로의 마침표와 일치하고 `$`는 줄 끝에 일치를 고정합니다."}
::option[`'^.txt'`]{#grep-start-anychar-txt explanation="줄 시작에 고정하고 이스케이프되지 않은 점도 사용하므로 다른 일치를 표현합니다."}
:::

## 패턴을 안전하게 제공하기

패턴을 명시적으로 제공하려면 `-e PATTERN`을 사용합니다. 따옴표만으로는 옵션 분석을 막지 못하므로 패턴이 `-`로 시작할 때 특히 유용합니다.

```bash
$ grep -e '-v' settings.conf
```

`-e`를 반복하면 제공한 패턴 중 하나와 일치하는 줄을 선택할 수 있습니다. `-f patterns.txt`는 파일에서 한 줄에 하나씩 패턴을 읽습니다.

:::single-choice{#grep-hyphen-pattern}
`-v`를 옵션으로 해석하지 않고 `settings.conf`에서 해당 패턴을 검색하는 명령어는 무엇인가요?

::option[`grep '-v' settings.conf`]{#grep-quoted-v explanation="따옴표는 쉘 확장에서 문자를 보호하지만 `grep`은 전달된 `-v` 인자를 여전히 일치 반전 옵션으로 해석할 수 있습니다."}
::option[`grep -v settings.conf`]{#grep-invert-settings explanation="일치 반전을 활성화하며 요청한 방식으로 `settings.conf`를 패턴과 입력 모두로 제공하지 않습니다."}
::option[`grep -e '-v' settings.conf`]{#grep-explicit-v .correct explanation="`-e` 옵션은 다음 인자가 하이픈으로 시작해도 패턴임을 선언합니다."}
:::

## 선택된 출력 제어하기

- `-i`: 대소문자 차이 무시
- `-n`: 선택된 줄 앞에 줄 번호 표시
- `-v`: 일치하지 않는 줄 선택
- `-c`: 각 입력 파일에서 선택된 줄 수 출력
- `-o`: 선택된 전체 줄 대신 비어 있지 않은 각 일치 부분만 출력

예를 들어 대소문자를 무시하고 `fox`가 들어 있는 줄 수를 셉니다.

```bash
$ grep -ic 'fox' sample.txt
```

`-c`는 한 줄 안의 전체 일치 횟수가 아니라 선택된 줄 수를 셉니다. `fox fox`가 들어 있는 한 줄은 개수에 1을 더합니다. GNU `grep`에서 겹치지 않는 일치 횟수가 필요하면 `grep -o PATTERN | wc -l` 같은 파이프라인을 사용할 수 있습니다.

:::single-choice{#grep-count-lines}
`data.txt`에는 `error error`가 들어 있는 줄 하나와 일치하지 않는 줄 두 개가 있습니다. `grep -c 'error' data.txt`는 무엇을 보고하나요?

::option[한 줄에 단어가 두 번 있으므로 `2`입니다.]{#grep-count-occurrences explanation="`-c`는 한 줄 안의 개별 일치가 아니라 선택된 줄을 셉니다."}
::option[정확히 한 줄이 일치하므로 `1`입니다.]{#grep-count-one-line .correct explanation="패턴이 한 줄 안에 두 번 나타나도 그 줄은 한 번만 선택됩니다."}
::option[파일에 총 세 줄이 있으므로 `3`입니다.]{#grep-count-total-lines explanation="`grep -c`에는 선택된 줄만 포함되며 일치하지 않는 줄은 제외됩니다."}
:::

## 표준 입력 필터링하고 디렉터리 검색하기

입력 파일을 지정하지 않으면 `grep`은 표준 입력을 읽으므로 파이프라인에 자연스럽게 들어갑니다.

```bash
$ env | grep '^USER='
```

디렉터리 아래에서 읽을 수 있는 파일을 재귀적으로 검색하려면 `-r`을 사용합니다.

```bash
$ grep -r 'listen_port' config/
```

권한 오류 같은 진단 메시지는 표준 오류로 가며 일치 대상으로 삼는 입력이 아닙니다. 곧바로 권한을 높이기보다는 검색 경로를 좁히고 권한을 이해하세요.

:::single-choice{#grep-pipeline-input}
`generate-report | grep 'failed'`에서 `grep`은 어떤 입력을 검색하나요?

::option[현재 디렉터리에서 이름이 `generate-report`인 파일입니다.]{#grep-report-file explanation="왼쪽 단어는 명령어로 실행되며 `grep`에 파일 피연산자로 전달되지 않습니다."}
::option[`generate-report`가 만든 표준 출력 스트림입니다.]{#grep-report-stdout .correct explanation="파이프가 생성자의 표준 출력을 `grep`의 표준 입력에 연결합니다."}
::option[`generate-report`가 만든 표준 오류 스트림입니다.]{#grep-report-stderr explanation="일반 파이프는 표준 출력을 전달합니다. 명시적으로 리디렉션하지 않으면 표준 오류는 분리되어 있습니다."}
:::

## 종료 상태 해석하기

일반 검색에서 GNU `grep`은 하나 이상의 줄이 선택되면 상태 `0`, 선택된 줄이 없으면 `1`, 오류가 발생하면 `2`를 반환합니다. 따라서 스크립트는 “일치 없음”을 읽을 수 없는 파일이나 잘못된 패턴과 구분해 검사할 수 있습니다.

`-q` 같은 옵션은 정상 출력을 숨기고 일치 항목을 찾으면 중단하므로 조건 검사에 유용합니다. 화면에 아무것도 없다는 사실만으로 성공 여부를 추론하지 마세요. `-q`, 리디렉션, 일치 없음, 오류 모두 표준 출력이 거의 없거나 전혀 없을 수 있지만 상태는 서로 다릅니다.

고정 문자열과 정규 표현식 검색을 연습하려면 다음 실습을 진행해 보세요.

1. **[Linux에서 grep으로 텍스트 검색](https://labex.io/ko/labs/comptia-search-text-with-grep-in-linux-590841)** - 기본 검색, 줄 번호 표시, 앵커, 기본 및 확장 정규 표현식을 활용한 복잡한 패턴 일치를 연습합니다.
2. **[Linux grep 명령어: 패턴 검색](https://labex.io/ko/labs/linux-linux-grep-command-pattern-searching-219192)** - 텍스트 파일에서 패턴을 검색하고 일치시키며 복잡한 패턴을 정의하는 정규 표현식을 익힙니다.
3. **[건초 더미에서 바늘 찾기](https://labex.io/ko/labs/linux-needle-in-the-haystack-388109)** - `grep`으로 특정 패턴을 검색하고 개수를 세며 고유 값을 추출하고 여러 로그 파일에서 검색 조건을 결합합니다.

## 요약

이제 줄 단위 텍스트를 검색하고 일치와 오류를 구분할 수 있습니다.

1. 기본, 확장, 고정 문자열 일치 중 하나를 선택할 수 있습니다.
2. 패턴을 따옴표로 묶고 하이픈으로 시작할 때 `-e`를 사용할 수 있습니다.
3. 선택된 줄 수와 일치 횟수를 혼동하지 않고 셀 수 있습니다.
4. 표준 입력을 필터링하거나 범위가 명확한 디렉터리를 재귀적으로 검색할 수 있습니다.
5. 일치, 일치 없음, 오류의 종료 상태를 해석할 수 있습니다.
