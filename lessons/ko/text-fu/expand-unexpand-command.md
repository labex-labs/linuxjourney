---
lesson_id: "expand-unexpand-command"
course_id: "text-fu"
lang: "ko"
order_index: 10
title: "expand와 unexpand"
description: "expand와 unexpand에서 탭 정지 위치가 탭과 공백 사이의 변환을 제어하는 방식을 배웁니다."
meta_title: "expand와 unexpand - Text-Fu"
meta_description: "expand 및 unexpand 명령어 가이드로 Linux의 텍스트 서식을 익혀 보세요. 일관된 파일 레이아웃을 위해 탭을 공백으로, 공백을 다시 탭으로 변환하는 방법을 배웁니다."
meta_keywords: "expand 명령어, unexpand 명령어, Linux 탭, Linux 공백, 텍스트 서식, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

탭은 고정된 수의 눈에 보이는 공백이 아니라 다음 탭 정지 위치까지의 이동을 저장합니다. 표시 너비는 현재 열과 탭 정지 설정에 따라 달라집니다. `expand`와 `unexpand` 명령어는 이러한 위치를 고려하며 탭 문자와 공백을 서로 변환합니다.

## 탭을 공백으로 변환하기

`expand`는 입력을 읽고 탭을 알맞은 탭 정지 위치에 도달하는 데 필요한 공백으로 바꾼 뒤 결과를 표준 출력에 씁니다.

```bash
$ expand sample.txt
```

기본적으로 탭 정지 위치는 8열마다 있습니다. 따라서 1열의 탭과 6열의 탭은 서로 다른 수의 공백으로 확장되며 항상 공백 여덟 개로 바뀌지는 않습니다.

:::single-choice{#expand-default-tab-stops}
기본 설정에서 `expand`는 탭 문자를 어떻게 바꾸나요?

::option[다음 기본 탭 정지 위치에 도달할 만큼 공백을 삽입합니다.]{#expand-next-stop .correct explanation="`expand`는 현재 열에서 필요한 공백 수를 계산해 탭 정렬을 보존합니다."}
::option[항상 정확히 공백 여덟 개를 삽입합니다.]{#expand-eight-spaces explanation="기본 정지 위치는 8열 간격이지만 필요한 공백 수는 현재 열에 따라 달라집니다."}
::option[다른 문자를 추가하지 않고 탭을 제거합니다.]{#expand-remove-tab explanation="이후 텍스트가 선택한 탭 정지 위치에 계속 정렬되도록 탭을 공백으로 바꿉니다."}
:::

## 탭 정지 위치 선택하기

지정한 열 간격마다 탭 정지 위치를 두려면 `-t NUMBER`를 사용합니다. 4열 간격은 다음과 같습니다.

```bash
$ expand -t 4 sample.txt
```

GNU `expand`는 명시적인 탭 위치를 쉼표로 구분한 목록도 받습니다. 각 줄의 첫 번째 비공백 문자 앞에 있는 탭만 변환하려면 `-i`를 사용합니다.

:::single-choice{#expand-four-column-stops}
4열마다 탭 정지 위치를 사용해 탭을 변환하는 명령어는 무엇인가요?

::option[`expand -i 4 sample.txt`]{#expand-initial-four explanation="`-i` 옵션은 변환을 줄 앞쪽 탭으로 제한하며 `4`를 탭 정지 간격으로 받지 않습니다."}
::option[`unexpand -t 4 sample.txt`]{#unexpand-tabs-four explanation="`unexpand`는 적합한 공백을 탭으로 바꾸므로 요청한 작업과 반대 방향입니다."}
::option[`expand -t 4 sample.txt`]{#expand-tabs-four .correct explanation="`-t` 옵션은 탭 정지 간격을 설정하며 `4`는 4열마다 정지 위치를 요청합니다."}
:::

## 변환된 출력 안전하게 저장하기

`expand`는 입력 파일을 직접 편집하지 않습니다. 변환한 텍스트를 저장하려면 표준 출력을 다른 경로로 리디렉션합니다.

```bash
$ expand sample.txt > result.txt
```

`expand sample.txt > sample.txt`를 사용하지 마세요. 쉘은 `expand`가 읽기 전에 대상 파일을 비우므로 원본 데이터를 잃을 수 있습니다. 별도로 쓴 결과를 확인한 뒤 적절한 파일 관리 단계로 원본을 의도적으로 교체할 수 있습니다.

:::single-choice{#expand-safe-output-file}
`sample.txt`를 읽기 전에 비우지 않고 확장한 텍스트를 저장하는 명령어는 무엇인가요?

::option[`expand sample.txt > sample.txt`]{#expand-same-file explanation="쉘은 `expand`를 시작하기 전에 출력용으로 `sample.txt`를 열고 비우므로 입력이 지워질 수 있습니다."}
::option[`expand sample.txt > result.txt`]{#expand-separate-result .correct explanation="입력과 출력 경로가 다르므로 쉘은 원본을 손상하지 않고 `result.txt`를 만들 수 있습니다."}
::option[`> sample.txt expand result.txt`]{#expand-leading-redirection explanation="여전히 `sample.txt`를 비우며 원본 파일을 안전하게 변환하는 명령도 아닙니다."}
:::

## 공백을 탭으로 변환하기

`unexpand`는 선택한 탭 정지 위치에서 정렬을 유지하면서 변환 가능한 공백을 탭으로 바꿉니다. 기본적으로 GNU `unexpand`는 각 줄의 첫 번째 비공백 문자 앞에 있는 초기 공백만 변환합니다.

```bash
$ unexpand result.txt
```

각 줄 전체에서 적합한 공백을 고려하려면 `-a`를 사용합니다.

```bash
$ unexpand -a result.txt
```

단순히 공백 여덟 개의 모든 연속 구간을 바꾸는 것은 아닙니다. `expand`와 마찬가지로 변환은 열 위치와 탭 정지 위치에 따라 달라집니다. 파일이 다른 규칙을 따르면 `-t 4` 또는 다른 탭 정지 지정을 사용하세요.

:::single-choice{#unexpand-default-scope}
`-a`가 없을 때 GNU `unexpand`는 일반적으로 어떤 공백의 변환을 고려하나요?

::option[파일 어디에나 있는 모든 공백 묶음입니다.]{#unexpand-every-group explanation="줄 전체의 공백을 고려하려면 `-a`가 필요하며 변환 여부는 여전히 탭 정지 위치에 따라 달라집니다."}
::option[마지막 단어 뒤에 있는 공백만입니다.]{#unexpand-trailing-blanks explanation="기본 범위는 줄 끝 공백이 아니라 초기 공백입니다."}
::option[첫 번째 비공백 문자 앞의 초기 공백만입니다.]{#unexpand-initial-blanks .correct explanation="GNU `unexpand`의 기본 동작은 각 줄의 선행 공백으로 제한됩니다."}
:::

:::single-choice{#unexpand-all-blanks}
GNU `unexpand`가 첫 번째 비공백 문자 뒤의 공백도 고려하도록 하는 옵션은 무엇인가요?

::option[`-i`]{#unexpand-initial-option explanation="`expand`에서 `-i`는 작업을 초기 탭으로 제한합니다. `unexpand`의 전체 공백 옵션이 아닙니다."}
::option[`-a`]{#unexpand-all-option .correct explanation="`-a` 옵션은 각 입력 줄 전체에서 적합한 공백을 변환하도록 합니다."}
::option[`-t`]{#unexpand-tab-list-option explanation="`-t` 옵션은 탭 정지 위치를 설정합니다. GNU 동작에서 범위가 넓어질 수 있지만 모든 공백을 명시적으로 요청하는 옵션은 `-a`입니다."}
:::

두 명령어 모두 파일을 지정하지 않으면 표준 입력을 읽으므로 파이프라인에서 사용할 수 있습니다. 표시 정렬이 같더라도 공백으로 변환했다가 다시 탭으로 바꾸면 원래 탭과 공백의 선택이 복원되지 않을 수 있습니다.

## 요약

이제 탭 정지 정렬을 유지하면서 탭과 공백을 변환할 수 있습니다.

1. 탭을 다음 설정된 정지 위치까지의 공백으로 확장할 수 있습니다.
2. `-t`로 사용자 지정 탭 정지 위치를 설정할 수 있습니다.
3. 입력을 교체하기 전에 출력을 다른 파일에 안전하게 저장할 수 있습니다.
4. 기본 `unexpand` 동작으로 선행 공백을 변환할 수 있습니다.
5. 각 줄 전체의 공백을 고려해야 할 때 `-a`를 사용할 수 있습니다.
