---
lesson_id: "join-split-command"
course_id: "text-fu"
lang: "ko"
order_index: 11
title: "join과 split"
description: "키를 기준으로 정렬된 텍스트 파일 두 개를 결합하고 한 파일을 이름이 지정된 조각으로 나누는 방법을 배웁니다."
meta_title: "join과 split - Text-Fu"
meta_description: "Linux join 및 split 명령어 사용법을 익혀 보세요. 공통 필드를 기준으로 파일을 효율적으로 결합하고 큰 파일을 작은 부분으로 나누는 방법을 배웁니다."
meta_keywords: "linux 파일 결합, 파일 결합 명령어, linux join 명령어, linux split 명령어, 파일 조작, 명령줄, 텍스트 처리"
---

`join`과 `split` 명령어는 서로 다른 파일 처리 문제를 해결합니다. `join`은 정렬된 텍스트 입력 두 개에서 관련 레코드를 결합하고 `split`은 하나의 입력을 여러 작은 파일로 나눕니다.

## 첫 번째 필드로 두 파일 결합하기

기본적으로 `join`은 정확히 두 입력 파일에서 공백으로 구분된 첫 번째 필드를 비교합니다. 다음은 이미 정렬된 파일입니다.

`people.txt`:

```text
1 John
2 Jane
3 Mary
```

`surnames.txt`:

```text
1 Doe
2 Doe
3 Sue
```

키 필드가 같은 레코드를 결합합니다.

```bash
$ join people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

출력에는 공유 키가 한 번 나온 뒤 첫 번째와 두 번째 파일의 나머지 필드가 이어집니다. `join`은 한 번에 파일 두 개를 처리하며 일반 파일 피연산자 세 개를 3방향 관계형 조인으로 받지 않습니다.

:::single-choice{#join-default-key} 필드 옵션이 없을 때 `join first.txt second.txt`는 어떤 레코드를 결합하나요?

::option[공백으로 구분된 첫 번째 필드가 같은 줄입니다.]{#join-first-fields .correct explanation="기본 `join` 동작은 정렬된 두 입력의 필드 1을 비교합니다."}
::option[물리적으로 같은 줄 번호에 있는 줄입니다.]{#join-line-numbers explanation="일치는 단순한 레코드 위치가 아니라 키 필드 값을 기준으로 합니다."}
::option[첫 번째 파일의 모든 줄과 두 번째 파일의 모든 줄입니다.]{#join-all-pairs explanation="`join`은 모든 줄의 무제한 카테시안 곱이 아니라 키가 일치하는 레코드를 출력합니다."}
:::

## 조인 키 정렬하기

각 입력은 호환되는 비교 규칙을 사용하여 조인 필드를 기준으로 정렬되어야 합니다. 기본 필드 1에는 `sort -k 1,1`로 사본을 준비합니다.

```bash
$ LC_ALL=C sort -k 1,1 people-raw.txt > people.txt
$ LC_ALL=C sort -k 1,1 surnames-raw.txt > surnames.txt
$ LC_ALL=C join people.txt surnames.txt
```

정렬과 조인에 같은 로캘을 사용하면 배열 규칙이 일관되게 유지됩니다. 정렬 결과를 입력 파일 자체로 리디렉션하면 쉘이 먼저 파일을 비우므로 그렇게 하지 마세요.

:::single-choice{#join-sort-requirement} `join`으로 안정적으로 일치 항목을 찾으려면 일반적으로 어떤 준비가 필요한가요?

::option[두 파일의 물리적인 줄 수가 정확히 같아야 합니다.]{#join-equal-line-count explanation="입력 길이는 달라도 됩니다. 같은 줄 수가 아니라 키 일치가 결합 결과를 결정합니다."}
::option[두 파일의 이름이 알파벳순으로 서로 이웃하게 정렬되어야 합니다.]{#join-filename-order explanation="내용의 키를 정렬해야 하며 두 파일 이름 사이의 사전식 관계는 무관합니다."}
::option[두 파일이 각각의 조인 필드를 기준으로 호환되는 순서로 정렬되어야 합니다.]{#join-sorted-keys .correct explanation="`join`은 정렬된 키를 따라 진행하므로 각 입력은 수행할 비교와 일치하는 순서를 사용해야 합니다."}
:::

## 서로 다른 조인 필드 선택하기

첫 번째 파일의 키에는 `-1 FIELD`, 두 번째 파일의 키에는 `-2 FIELD`를 사용합니다. 첫 번째 입력이 다음과 같다고 가정합니다.

```text
John 1
Jane 2
Mary 3
```

두 번째 입력은 다음과 같습니다.

```text
1 Doe
2 Doe
3 Sue
```

첫 번째 파일을 필드 2로, 두 번째 파일을 필드 1로 정렬한 뒤 실행합니다.

```bash
$ join -1 2 -2 1 people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`:`처럼 공백이 아닌 한 문자가 필드를 구분할 때는 `-t CHARACTER`를 사용합니다. `-a 1`이나 `-a 2` 같은 옵션으로 한 입력에서 짝이 없는 줄을 포함할 수 있으며 기본 출력에는 키가 일치하는 항목만 들어갑니다.

:::single-choice{#join-different-fields} 첫 번째 파일의 필드 2를 두 번째 파일의 필드 1과 결합하는 옵션은 무엇인가요?

::option[`-1 1 -2 2`]{#join-fields-reversed explanation="첫 번째 입력의 필드 1과 두 번째 입력의 필드 2를 선택하므로 요청한 매핑과 반대입니다."}
::option[`-1 2 -2 1`]{#join-fields-two-one .correct explanation="`-1 2`는 첫 번째 파일의 필드 2를, `-2 1`은 두 번째 파일의 필드 1을 선택합니다."}
::option[`-f 2 -d 1`]{#join-cut-style-options explanation="다른 텍스트 도구의 필드와 구분 기호 옵션과 비슷하지만 `join`의 필드 선택 옵션은 아닙니다."}
:::

## 줄 수를 기준으로 나누기

`split`은 한 입력의 연속된 부분을 별도의 출력 파일에 씁니다. 키 기반 `join` 작업의 역연산은 아닙니다.

```bash
$ split large.txt
```

GNU의 기본 동작은 출력 파일마다 최대 1000줄을 쓰고 접두사 `x`를 사용하여 `xaa`, `xab`, `xac` 같은 이름을 만듭니다.

줄 수를 선택하려면 `-l NUMBER`를 사용하고 출력 접두사를 고르려면 마지막 피연산자를 추가합니다.

```bash
$ split -l 500 large.txt part-
```

각 조각에 최대 500줄이 들어가는 `part-aa`, `part-ab` 등이 만들어집니다.

:::single-choice{#split-lines-with-prefix} `large.txt`를 최대 500줄씩, `part-` 접두사가 붙은 조각으로 나누는 명령어는 무엇인가요?

::option[`split -b 500 large.txt part-`]{#split-five-hundred-bytes explanation="`-b` 옵션은 바이트를 선택하므로 일반 텍스트에서 조각은 500줄보다 훨씬 작아집니다."}
::option[`split -l 500 large.txt part-`]{#split-five-hundred-lines .correct explanation="`-l 500`은 최대 줄 수를 설정하고 마지막 피연산자는 출력 파일 이름 접두사를 제공합니다."}
::option[`join -l 500 large.txt part-`]{#join-split-lines explanation="`join`은 파일 두 개의 키 레코드를 결합하며 한 입력을 조각으로 나누지 않습니다."}
:::

## 크기를 기준으로 나누기

바이트 크기를 기준으로 입력을 나누려면 `-b SIZE`를 사용합니다. GNU에서 이 문맥의 `K`, `M`, `G` 같은 접미사는 1024의 거듭제곱을 나타냅니다.

```bash
$ split -b 10M archive.bin chunk-
```

마지막 조각은 더 작을 수 있으며 그 외에는 10메비바이트 크기의 조각을 요청합니다. `split`은 아카이브 목록이나 재조립 메타데이터를 만들지 않습니다. 재구성해야 한다면 접미사의 순서를 보존하고 조각들을 순서대로 이어 붙이세요.

:::single-choice{#split-ten-mebibytes} `archive.bin`을 `chunk-` 접두사를 사용하여 10MiB씩 나누는 명령어는 무엇인가요?

::option[`split -l 10M archive.bin chunk-`]{#split-lines-ten-m explanation="`-l` 옵션은 줄 수를 받으며 바이너리 조각의 바이트 크기 접미사를 받지 않습니다."}
::option[`join -b 10M archive.bin chunk-`]{#join-bytes explanation="`join`은 바이너리 입력을 나누거나 이 조각 크기 작업을 지원하지 않습니다."}
::option[`split -b 10M archive.bin chunk-`]{#split-ten-mib .correct explanation="`-b` 옵션은 조각 크기를 선택하고 `10M`은 10×1024×1024바이트를 요청하며 `chunk-`는 출력 접두사입니다."}
:::

키 조인과 구조화된 데이터 처리를 연습하려면 다음 실습을 진행해 보세요.

1. **[Linux join 명령어: 파일 결합](https://labex.io/ko/labs/linux-linux-join-command-file-joining-219193)** - 공통 필드를 기준으로 정렬된 텍스트 파일 두 개의 줄을 병합하는 방법을 직접 연습합니다.
2. **[직원 데이터 처리](https://labex.io/ko/labs/linux-processing-employees-data-388132)** - `join`과 `awk` 같은 명령줄 도구로 여러 출처의 데이터를 결합하고 처리합니다.

## 요약

이제 정렬된 레코드를 결합하거나 한 입력을 순서가 있는 조각으로 나눌 수 있습니다.

1. 정확히 두 파일을 같은 키 필드로 결합할 수 있습니다.
2. 두 입력을 조인 키 기준으로 일관되게 정렬할 수 있습니다.
3. `-1`과 `-2`로 기본값이 아닌 키 필드를 선택할 수 있습니다.
4. `-l`로 줄 수를 기준으로 나눌 수 있습니다.
5. `-b`와 명확한 접두사로 바이트 크기를 기준으로 나눌 수 있습니다.
