---
lesson_id: "uniq-unique-command"
course_id: "text-fu"
lang: "ko"
order_index: 14
title: "uniq (고유 항목)"
description: "uniq로 인접한 동일 줄 그룹을 압축하고 세거나 필터링하는 방법을 배웁니다."
meta_title: "uniq (고유 항목) - Text-Fu"
meta_description: "Linux uniq 명령어로 텍스트에서 인접한 중복 줄을 필터링하고 제거하는 방법을 알아봅니다. -c, -u, -d 옵션과 sort를 결합한 강력한 텍스트 처리를 배웁니다."
meta_keywords: "uniq 명령어, Linux uniq, uniq linux, 중복 제거, sort uniq, 텍스트 처리, 데이터 정리, Linux 튜토리얼"
---

`uniq` 명령어는 각 입력 줄을 바로 앞 줄과 비교합니다. 인접한 동일 줄 그룹을 압축하거나 세거나 선택할 수 있지만 파일 전체에서 떨어져 있는 중복을 검색하지는 않습니다.

## 인접한 중복 줄 압축하기

`reading.txt`에 다음처럼 그룹화된 값이 있다고 가정합니다.

```plaintext
book
book
paper
paper
article
article
magazine
```

필터링 옵션 없이 `uniq`를 실행하면 인접한 각 그룹에서 대표 줄 하나를 출력합니다.

```bash
$ uniq reading.txt
book
paper
article
magazine
```

결과는 표준 출력으로 가므로 입력 파일은 변경되지 않습니다.

:::single-choice{#uniq-collapse-adjacent}
기본적으로 `uniq reading.txt`는 무엇을 하나요?

::option[전체 파일을 정렬한 뒤 모든 반복 값을 제거합니다.]{#uniq-auto-sort explanation="`uniq`는 입력 순서를 유지하고 정렬하지 않습니다. 떨어져 있는 같은 값은 별도 그룹으로 남습니다."}
::option[인접한 동일 줄 그룹마다 한 줄을 출력합니다.]{#uniq-one-per-group .correct explanation="기본 `uniq`는 연속된 동일 줄을 출력 줄 하나로 압축합니다."}
::option[`reading.txt`에서 중복 줄을 직접 삭제합니다.]{#uniq-edit-file explanation="기본적으로 필터링된 텍스트를 표준 출력에 쓰며 입력 파일을 편집하지 않습니다."}
:::

## 인접 그룹 세기

`-c`를 사용하면 각 출력 그룹 앞에 연속된 입력 줄 수를 붙입니다.

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

동일한 줄을 먼저 인접하게 만들지 않았다면 이 값은 전체 합계가 아니라 연속 구간의 길이입니다.

:::single-choice{#uniq-count-groups}
`uniq -c`의 개수는 무엇을 나타내나요?

::option[각 입력 줄의 문자 수입니다.]{#uniq-character-count explanation="문자 수 세기는 `uniq -c`의 목적이 아니며 `wc` 같은 도구가 문자와 바이트 합계를 다룹니다."}
::option[각 그룹에서 연속된 동일 줄의 수입니다.]{#uniq-consecutive-count .correct explanation="`-c`는 압축된 각 인접 그룹 앞에 그 그룹에 포함된 줄 수를 붙입니다."}
::option[파일 어디에나 있는 일치 줄의 총수입니다.]{#uniq-global-count explanation="데이터를 먼저 정렬하거나 그룹화하지 않으면 떨어진 동일 줄은 별도 그룹을 만듭니다."}
:::

## 고유 그룹이나 반복 그룹 선택하기

정확히 한 줄만 포함한 그룹을 출력하려면 `-u`를 사용합니다.

```bash
$ uniq -u reading.txt
magazine
```

두 줄 이상인 인접 그룹마다 대표 줄 하나를 출력하려면 `-d`를 사용합니다.

```bash
$ uniq -d reading.txt
book
paper
article
```

GNU `uniq -D`는 반복 그룹의 모든 줄을 출력하지만 소문자 `-d`는 각 반복 그룹의 값을 한 번만 출력합니다.

:::single-choice{#uniq-only-singletons}
인접 그룹 중 정확히 한 번만 나타난 그룹만 출력하는 명령어는 무엇인가요?

::option[`uniq -c reading.txt`]{#uniq-count-reading explanation="반복 그룹과 단일 그룹을 모두 개수와 함께 출력합니다."}
::option[`uniq -d reading.txt`]{#uniq-duplicate-reading explanation="소문자 `-d`는 반대로 각 반복 그룹에서 한 줄을 출력합니다."}
::option[`uniq -u reading.txt`]{#uniq-single-reading .correct explanation="`-u` 옵션은 인접 연속 길이가 정확히 1인 그룹을 선택합니다."}
:::

:::single-choice{#uniq-one-per-duplicate-group}
두 번 이상 나타난 인접 그룹마다 한 줄을 출력하는 명령어는 무엇인가요?

::option[`uniq -d reading.txt`]{#uniq-duplicate-groups .correct explanation="`-d` 옵션은 반복되는 인접 그룹을 선택하고 그룹마다 대표 줄 하나를 출력합니다."}
::option[`uniq -D reading.txt`]{#uniq-all-duplicate-lines explanation="GNU 대문자 `-D`는 대표 줄 하나만이 아니라 반복 그룹에 속한 모든 줄을 출력합니다."}
::option[`uniq -u reading.txt`]{#uniq-unique-groups explanation="`-u` 옵션은 반복 그룹이 아니라 단일 그룹을 선택합니다."}
:::

## 떨어져 있는 중복 그룹화하기

같은 줄이 떨어져 있으면 서로 다른 그룹을 만듭니다.

```plaintext
book
paper
book
paper
article
magazine
article
```

이 파일에 `uniq`를 실행하면 예상 밖의 결과가 나올 수 있습니다.

```bash
$ uniq reading.txt
book
paper
book
paper
article
magazine
article
```

이웃한 값이 다르므로 어떤 줄도 압축되지 않습니다. 순서가 바뀌어도 되고 같은 전체 줄을 함께 그룹화하려면 먼저 정렬합니다.

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

두 단계에서 일관된 로캘과 비교 정책을 사용하세요. `sort -u reading.txt`도 한 명령어로 정렬하고 동일 정렬 키마다 한 줄을 유지할 수 있습니다.

:::single-choice{#uniq-separated-duplicates}
같은 줄이 `reading.txt` 곳곳에 흩어져 있고 출력 순서가 바뀌어도 됩니다. 서로 다른 전체 줄마다 정렬된 사본 하나를 만드는 파이프라인은 무엇인가요?

::option[`sort reading.txt | uniq`]{#sort-then-uniq .correct explanation="정렬이 같은 전체 줄을 그룹화하고 `uniq`가 각 인접 그룹을 한 줄로 압축합니다."}
::option[`uniq reading.txt | sort`]{#uniq-before-sort explanation="떨어진 동일 줄이 인접하기 전에 `uniq`가 실행되므로 나중에 정렬해도 출력에 중복 줄이 남을 수 있습니다."}
::option[`uniq -c reading.txt | head`]{#uniq-count-head explanation="기존 인접 그룹을 세고 출력을 제한할 뿐 떨어져 있는 중복을 전체적으로 그룹화하지 않습니다."}
:::

입력 파일을 지정하지 않으면 `uniq`는 표준 입력을 읽으므로 `sort` 뒤에 자연스럽게 사용할 수 있습니다. GNU의 `-i`는 대소문자를 무시할 수 있고 `-f`, `-s`, `-w`는 비교 영역을 건너뛰거나 제한할 수 있습니다. 각 줄의 일부로 동등성을 정의해야 할 때만 사용하세요.

중복 그룹화, 계산, 필터링을 연습하려면 다음 실습을 진행해 보세요.

1. **[Linux uniq 명령어: 중복 필터링](https://labex.io/ko/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - `uniq`와 `sort`를 결합해 텍스트 파일의 중복 줄을 식별하고 필터링하며 분석합니다.
2. **[Linux sort 명령어: 텍스트 정렬](https://labex.io/ko/labs/linux-linux-sort-command-text-sorting-219196)** - `uniq`를 효과적으로 사용하기 위한 핵심 단계인 텍스트 줄 정렬을 연습합니다.
3. **[단어 수 세기와 정렬](https://labex.io/ko/labs/linux-word-count-and-sorting-388125)** - `wc`와 `sort`로 줄, 단어, 문자를 세고 자주 나타나는 패턴을 찾아 데이터를 정렬합니다.

## 요약

이제 `uniq`로 인접한 동일 줄 그룹을 분석할 수 있습니다.

1. 인접한 각 중복 그룹을 한 줄로 압축할 수 있습니다.
2. `-c`로 연속 출현 횟수를 셀 수 있습니다.
3. `-u`로 단일 그룹을 선택할 수 있습니다.
4. `-d` 또는 GNU `-D`로 반복 그룹을 선택할 수 있습니다.
5. 떨어진 중복을 그룹화해야 할 때 먼저 정렬할 수 있습니다.
