---
lesson_id: "cut-command"
course_id: "text-fu"
lang: "ko"
order_index: 6
title: "cut"
description: "cut으로 각 줄에서 문자 위치나 구분된 필드를 선택하는 방법을 배웁니다."
meta_title: "cut - Text-Fu"
meta_description: "Linux `cut` 명령어를 사용하여 파일에서 특정 텍스트 섹션을 추출하는 방법을 알아보세요. 이 가이드는 문자 및 필드 (`cut f`) 로 자르는 방법을 다루며, 사용자 지정 구분 기호로 f 를 자르는 방법도 포함합니다. Linux 텍스트 처리를 마스터하는 데 적합합니다."
meta_keywords: "cut 명령어, Linux 텍스트 처리, 텍스트 추출, cut f, f 자르는 방법, Linux 튜토리얼, cut 예제, Linux 가이드, 필드 자르기"
---

`cut` 명령어는 각 입력 줄에서 지정한 문자 위치나 필드를 선택합니다. 구분 기호와 필드 위치가 일정한 구조화된 텍스트에 가장 적합합니다.

예제에 사용할 탭 구분 파일을 만들어 보겠습니다. `printf`는 `\t`를 실제 탭으로, `\n`을 줄 바꿈으로 해석합니다.

```bash
$ printf 'name\trole\nalice\tadmin\nbob\tviewer\n' > team.tsv
```

## 문자 위치 선택하기

각 줄에서 위치를 선택하려면 `-c LIST`를 사용합니다. 위치는 1부터 시작합니다.

```bash
$ cut -c 1 team.tsv
n
a
b
```

목록에는 개별 위치와 범위를 지정할 수 있습니다.

```bash
$ cut -c 1-4 team.tsv
name
alic
bob
$ cut -c 1,3 team.tsv
nm
ai
bb
```

공백, 탭, 문장 부호도 한 위치를 차지합니다. `cut`은 각 줄을 독립적으로 처리합니다.

:::single-choice{#cut-first-character} `names.txt`의 모든 줄에서 첫 번째 문자를 출력하는 명령어는 무엇인가요?

::option[`cut -c 1 names.txt`]{#cut-character-one .correct explanation="`-c` 옵션은 문자 위치를 선택하며 위치 1은 각 줄의 첫 번째 문자입니다."}
::option[`cut -f 1 names.txt`]{#cut-field-one explanation="`-f` 옵션은 첫 번째 탭 구분 필드를 선택하며, 이 필드에는 여러 문자가 들어갈 수 있습니다."}
::option[`cut -d 1 names.txt`]{#cut-delimiter-one explanation="`-d` 옵션은 필드 구분 기호를 지정하므로 필드 선택과 함께 사용해야 합니다. 문자 위치를 선택하지는 않습니다."}
:::

## 탭으로 구분된 필드 선택하기

필드를 선택하려면 `-f LIST`를 사용합니다. 기본 구분 기호는 탭입니다.

```bash
$ cut -f 2 team.tsv
role
admin
viewer
```

문자 선택과 마찬가지로 목록에는 `1`, `1,3`, `2-4`, `-3`, `2-` 같은 값을 지정할 수 있습니다.

:::single-choice{#cut-second-tab-field} `team.tsv`의 모든 줄에서 탭으로 구분된 두 번째 필드를 출력하는 명령어는 무엇인가요?

::option[`cut -c 2 team.tsv`]{#cut-second-character explanation="탭으로 구분된 두 번째 필드가 아니라 각 줄의 두 번째 문자 위치를 선택합니다."}
::option[`cut -f 2 team.tsv`]{#cut-second-field .correct explanation="`-d`가 없으면 필드 모드는 탭을 구분 기호로 사용하며 `-f 2`는 두 번째 필드를 선택합니다."}
::option[`cut -d 2 team.tsv`]{#cut-delimiter-two explanation="`2`를 구분 기호로 사용하려 하지만 필드 목록을 제공하지 않습니다. 두 번째 필드를 선택하지 않습니다."}
:::

## 사용자 지정 구분 기호 선택하기

필드가 탭 이외의 문자로 구분되어 있으면 `-f`와 함께 `-d CHARACTER`를 사용합니다. 다음 예제는 세미콜론 구분 데이터를 만듭니다.

```bash
$ printf 'alice;admin\nbob;viewer\n' > team.txt
$ cut -d ';' -f 1 team.txt
alice
bob
```

이 형식의 구분 기호는 한 문자입니다. 따옴표로 묶지 않은 세미콜론은 쉘에서 제어 의미가 있으므로 `;`를 따옴표로 묶습니다.

:::single-choice{#cut-semicolon-role-field} `team.txt`에서 세미콜론으로 구분된 두 번째 필드를 출력하는 명령어는 무엇인가요?

::option[`cut -d ':' -f 2 team.txt`]{#cut-colon-second explanation="콜론으로 구분된 필드를 선택하지만 파일은 세미콜론을 사용합니다."}
::option[`cut -d ';' -f 2 team.txt`]{#cut-semicolon-second .correct explanation="따옴표로 묶은 세미콜론이 구분 기호를 설정하고 `-f 2`가 각 줄의 두 번째 필드를 선택합니다."}
::option[`cut -c 2 -f ';' team.txt`]{#cut-mixed-options explanation="문자 선택과 잘못된 필드 인자를 섞었습니다. 구분 기호는 `-d` 뒤에, 필드 번호는 `-f` 뒤에 와야 합니다."}
:::

## 구분 기호가 없는 줄 처리하기

필드 모드에서 `cut`은 일반적으로 구분 기호가 없는 줄을 그대로 출력합니다. 그런 줄을 제외하려면 `-s`를 추가합니다.

```bash
$ printf 'alice;admin\nheader\nbob;viewer\n' | cut -s -d ';' -f 2
admin
viewer
```

이 기능은 일반적인 CSV 파일을 검증하지 않습니다. CSV에는 따옴표로 묶은 구분 기호, 줄 바꿈, 이스케이프 규칙이 있을 수 있으며 한 문자 분할로는 이를 이해할 수 없습니다. 이런 데이터에는 CSV 전용 도구를 사용하세요.

:::single-choice{#cut-suppress-undelimited} `cut -d ':' -f 1`에서 `-s`는 무엇을 하나요?

::option[선택한 필드를 정렬한 뒤 출력합니다.]{#cut-s-sort explanation="`cut`은 입력을 정렬하지 않으며 `-s`는 순서와 관련이 없습니다."}
::option[연속된 구분 기호를 하나의 구분 기호로 처리합니다.]{#cut-s-squeeze explanation="`cut`에서 `-s`는 구분 기호를 합치지 않습니다. 빈 필드도 의미 있는 위치로 남습니다."}
::option[선택한 구분 기호가 없는 줄을 출력하지 않습니다.]{#cut-s-suppress .correct explanation="필드 모드에서 `-s`는 구분 기호가 없는 줄이 그대로 통과하지 않게 합니다."}
:::

## 표준 입력에서 읽기

파일을 지정하지 않거나 입력 피연산자로 `-`를 사용하면 `cut`은 표준 입력을 읽습니다. 따라서 파이프라인 단계로 자연스럽게 사용할 수 있습니다.

```bash
$ printf 'red:1\nblue:2\n' | cut -d ':' -f 1
red
blue
```

:::single-choice{#cut-pipeline-input} `generate-data | cut -d ':' -f 1`에서 `cut`은 어디에서 입력을 읽나요?

::option[파이프를 통해 `generate-data`의 표준 출력에서 읽습니다.]{#cut-pipe-stdin .correct explanation="파이프는 생성자의 표준 출력을 `cut`의 표준 입력에 연결하며 별도의 입력 파일은 지정되지 않았습니다."}
::option[이름이 문자 그대로 `generate-data`인 파일에서 읽습니다.]{#cut-pipe-file explanation="`generate-data`는 파이프 왼쪽 명령어로 실행되며 `cut`에 파일 이름으로 전달되지 않습니다."}
::option[`cut`의 표준 오류 스트림에서 읽습니다.]{#cut-pipe-stderr explanation="일반 파이프는 이전 명령어의 표준 출력을 표준 입력으로 공급하며 `cut`의 표준 오류를 사용하지 않습니다."}
:::

위치와 필드 선택을 연습하려면 다음 실습을 진행해 보세요.

1. **[Linux cut 명령어: 텍스트 자르기](https://labex.io/ko/labs/linux-linux-cut-command-text-cutting-219187)** - `cut` 명령어로 텍스트 파일의 특정 열이나 필드를 추출하는 방법을 직접 연습합니다.
2. **[시퀀스 제어 및 파이프라인](https://labex.io/ko/labs/linux-sequence-control-and-pipeline-17994)** - 명령 실행 순서와 파이프라인을 제어하고 `cut`, `grep`, `wc`, `sort`, `uniq` 같은 텍스트 처리 도구를 활용합니다.

## 요약

이제 `cut`으로 줄 단위 텍스트에서 예측 가능한 위치를 선택할 수 있습니다.

1. 개별 문자 위치나 범위를 선택할 수 있습니다.
2. `-f`로 탭 구분 필드를 추출할 수 있습니다.
3. `-d`로 한 문자 구분 기호를 지정할 수 있습니다.
4. 필요할 때 구분 기호가 없는 줄을 제외할 수 있습니다.
5. 파일이나 표준 입력에서 구조화된 텍스트를 읽을 수 있습니다.
