---
lesson_id: "sort-command"
course_id: "text-fu"
lang: "ko"
order_index: 12
title: "sort"
description: "sort로 텍스트 줄을 사전식, 숫자 또는 선택한 필드 값에 따라 정렬하는 방법을 배웁니다."
meta_title: "sort - Text-Fu"
meta_description: "Linux sort 명령어로 텍스트 파일을 정렬하는 방법을 배웁니다. 역순 및 숫자 정렬 같은 옵션을 알아보고 Linux 명령줄 기술을 향상하세요."
meta_keywords: "Linux sort 명령어, sort -r, sort -n, Linux 튜토리얼, 명령줄, 초보자 Linux, sort 가이드"
---

`sort` 명령어는 완전한 줄을 읽고 선택한 비교 규칙에 따라 순서를 정한 뒤 결과를 표준 출력에 씁니다. 출력 작업을 명시적으로 선택하지 않는 한 입력 파일은 변경하지 않습니다.

## 전체 줄 정렬하기

`animals.txt`가 다음과 같다고 가정합니다.

```text
dog
cow
cat
elephant
bird
```

줄을 오름차순으로 정렬합니다.

```bash
$ sort animals.txt
bird
cat
cow
dog
elephant
```

텍스트 순서는 현재 로캘을 따르며 대소문자, 악센트, 문장 부호의 순서에 영향을 줄 수 있습니다. 스크립트에서 재현 가능한 바이트 중심 배열이 필요하면 `LC_ALL=C` 같은 일관된 로캘을 사용합니다.

```bash
$ LC_ALL=C sort animals.txt
```

:::single-choice{#sort-lines-ascending}
키나 숫자 옵션 없이 `sort animals.txt`를 실행하면 무엇을 하나요?

::option[현재 로캘에 따라 전체 입력 줄의 순서를 정합니다.]{#sort-locale-lines .correct explanation="기본 `sort`는 활성 로캘의 배열 규칙을 사용하여 전체 줄을 비교합니다."}
::option[각 줄 안의 단어를 정렬하지만 줄 순서는 유지합니다.]{#sort-words-within-lines explanation="`sort`는 각 줄을 하나의 레코드로 취급하며 개별 줄 안의 단어를 재배열하지 않습니다."}
::option[`animals.txt`를 자동으로 제자리에서 다시 씁니다.]{#sort-auto-rewrite explanation="기본적으로 정렬 결과는 표준 출력으로 가며 입력 파일은 바뀌지 않습니다."}
:::

## 결과 뒤집기

비교 결과를 뒤집으려면 `-r`을 추가합니다.

```bash
$ sort -r animals.txt
elephant
dog
cow
cat
bird
```

:::single-choice{#sort-reverse-order}
`animals.txt`를 역순으로 정렬하는 명령어는 무엇인가요?

::option[`sort -n animals.txt`]{#sort-numeric-animals explanation="`-n` 옵션은 숫자 비교를 요청하며 역순을 의미하지 않습니다."}
::option[`sort -u animals.txt`]{#sort-unique-animals explanation="`-u` 옵션은 중복 키를 제외하며 출력을 뒤집지 않습니다."}
::option[`sort -r animals.txt`]{#sort-reverse-animals .correct explanation="`-r` 옵션은 다른 비교 규칙으로 선택한 순서를 뒤집습니다."}
:::

## 숫자 비교하기

사전식 순서는 문자를 비교하므로 일반적으로 `10`이 `2`보다 앞에 옵니다. 보통의 숫자 비교에는 `-n`을 사용합니다.

```bash
$ printf '10\n2\n30\n' | sort -n
2
10
30
```

필요하면 옵션을 결합합니다. `sort -nr scores.txt`는 숫자로 비교하고 큰 값을 먼저 배치합니다.

:::single-choice{#sort-numbers-descending}
`scores.txt`의 숫자 줄을 큰 값에서 작은 값 순으로 정렬하는 명령어는 무엇인가요?

::option[`sort -n scores.txt`]{#sort-numeric-ascending explanation="숫자 비교를 선택하지만 기본 방향은 작은 값을 먼저 둡니다."}
::option[`sort -nr scores.txt`]{#sort-numeric-reverse .correct explanation="`-n`은 숫자 비교를 선택하고 `-r`은 순서를 뒤집어 숫자 내림차순을 만듭니다."}
::option[`sort -r scores.txt`]{#sort-lexical-reverse explanation="텍스트 배열을 뒤집을 뿐 숫자 비교를 요청하지 않아 `10`과 `2` 같은 값이 예상 밖의 순서가 될 수 있습니다."}
:::

## 필드를 기준으로 정렬하기

키를 선택하려면 `-k START[,END]`를 사용합니다. 기본적으로 연속된 공백이 필드를 구분합니다. 콜론 구분 레코드에는 `-t ':'`를 사용합니다.

```bash
$ printf 'alice:30\nbob:8\ncarol:20\n' | sort -t ':' -k 2,2n
bob:8
carol:20
alice:30
```

여기서 `-t ':'`는 구분 기호를 선택하고 `-k 2,2`는 키를 필드 2로 제한하며 붙어 있는 `n`은 그 키를 숫자로 비교합니다. 끝의 `,2`가 없으면 필드 2에서 시작하는 키는 일반적으로 줄 끝까지 이어집니다.

:::single-choice{#sort-second-colon-field}
`users.txt`에서 콜론으로 구분된 두 번째 필드만을 숫자로 정렬하는 명령어는 무엇인가요?

::option[`sort -n -k 1,1 users.txt`]{#sort-first-blank-field explanation="기본 공백 구분 필드를 사용하고 필드 1을 선택하므로 콜론 구분 두 번째 필드가 아닙니다."}
::option[`cut -d ':' -f 2 users.txt`]{#cut-second-user-field explanation="`cut`은 필드 2를 추출하지만 그 키를 기준으로 원래 레코드를 정렬하지 않습니다."}
::option[`sort -t ':' -k 2,2n users.txt`]{#sort-colon-field-two .correct explanation="콜론이 필드 경계를 정하고 `2,2`가 키를 필드 2로 제한하며 `n`이 숫자 비교를 지정합니다."}
:::

## 중복 제거하고 출력 저장하기

같은 비교 키마다 한 줄만 출력하려면 `-u`를 사용합니다.

```bash
$ sort -u names.txt
```

선택한 비교 규칙에 따라 정렬과 중복 제거를 함께 수행합니다. 이미 정렬된 데이터에서 인접 중복만 제거하려면 뒤에서 다룰 `uniq` 명령어를 사용할 수 있습니다.

대상이 입력과 다르면 일반 리디렉션으로 결과를 파일에 쓸 수 있습니다.

```bash
$ sort names.txt > names-sorted.txt
```

`sort names.txt > names.txt`를 실행하지 마세요. 쉘은 `sort`가 읽기 전에 입력 파일을 비웁니다. 같은 경로를 의도적으로 사용하려면 GNU `sort -o names.txt names.txt`가 자체 출력을 안전하게 처리합니다.

```bash
$ sort -o names.txt names.txt
```

원본 데이터가 중요하면 백업을 만들거나 별도의 결과를 쓰고 확인하세요.

:::single-choice{#sort-safe-same-file}
GNU/Linux에서 쉘 리디렉션이 먼저 파일을 비우지 않도록 `sort`에 정렬 결과를 `names.txt`에 안전하게 다시 쓰라고 요청하는 명령어는 무엇인가요?

::option[`sort -o names.txt names.txt`]{#sort-output-same-file .correct explanation="GNU `sort`는 필요에 따라 읽은 뒤 `-o` 출력을 관리하므로 쉘이 `>`로 입력을 미리 비우지 않습니다."}
::option[`sort names.txt > names.txt`]{#sort-redirection-same-file explanation="쉘은 `sort`를 시작하기 전에 `names.txt`를 비우므로 입력을 잃을 수 있습니다."}
::option[`sort -u names.txt`]{#sort-unique-stdout explanation="고유한 정렬 줄을 표준 출력에 쓰며 입력 파일은 변경하지 않습니다."}
:::

줄 단위 데이터의 정렬과 분석을 연습하려면 다음 실습을 진행해 보세요.

1. **[Linux sort 명령어: 텍스트 정렬](https://labex.io/ko/labs/linux-linux-sort-command-text-sorting-219196)** - 오름차순과 내림차순을 포함해 텍스트 파일의 줄을 여러 방식으로 정렬합니다.
2. **[단어 수 세기와 정렬](https://labex.io/ko/labs/linux-word-count-and-sorting-388125)** - 단어 수 세기와 정렬을 함께 적용해 텍스트 데이터를 분석합니다.

## 요약

이제 정렬된 텍스트의 비교 규칙과 출력 대상을 선택할 수 있습니다.

1. 재현성이 중요할 때 명시적인 로캘로 전체 줄을 정렬할 수 있습니다.
2. `-r`로 결과를 뒤집을 수 있습니다.
3. `-n`으로 숫자 값을 비교할 수 있습니다.
4. `-t`와 `-k`로 범위가 제한된 필드 키를 선택할 수 있습니다.
5. 입력을 비우지 않고 중복을 제거하거나 출력을 저장할 수 있습니다.
