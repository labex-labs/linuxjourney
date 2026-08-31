---
lesson_id: "vim-navigation"
course_id: "advanced-text-fu"
lang: "ko"
order_index: 5
title: "Vim 탐색"
description: "Vim 일반 모드에서 문자, 단어, 줄, 파일 위치를 기준으로 이동하는 방법을 배웁니다."
meta_title: "Vim 탐색 - Advanced Text-Fu"
meta_description: "h, j, k, l 키를 사용하는 Vim 탐색의 기초를 배웁니다. 초보자에게 필요한 Vim 이동을 이해하고 Linux 명령줄 기술을 향상하세요."
meta_keywords: "Vim 탐색, Vim 튜토리얼, Linux Vim, Vim 이동, Vim 기초, 초보자 Vim, Linux 텍스트 편집기, Vim 가이드"
---

Vim은 마우스 없이 터미널에서 사용할 수 있는 키보드 이동 명령을 제공합니다. 일부 Vim 구성은 마우스 입력도 지원하지만 이동 명령을 익히면 편집 명령과 조합하여 사용할 수 있습니다.

연습하기 전에 `Esc`를 눌러 일반 모드로 돌아가세요.

## 문자와 화면 줄을 기준으로 이동하기

일반 모드의 기본 이동 키는 다음과 같습니다.

- `h`: 왼쪽으로 한 문자 이동
- `j`: 아래로 한 화면 줄 이동
- `k`: 위로 한 화면 줄 이동
- `l`: 오른쪽으로 한 문자 이동

화살표 키도 일반적으로 비슷하게 움직이지만 `h`, `j`, `k`, `l`은 손을 다른 명령 가까이에 두게 합니다. 화면에서 줄 바꿈된 표시 줄에서는 `j`와 `k`가 보통 파일의 실제 줄을 기준으로 움직이고 `gj`와 `gk`는 표시된 화면 줄을 기준으로 움직입니다.

:::single-choice{#vim-navigation-down}
일반 모드에서 커서를 한 줄 아래로 이동하는 키는 무엇인가요?

::option[`k`]{#vim-nav-k-up explanation="`k` 이동은 한 줄 위로 이동합니다."}
::option[`l`]{#vim-nav-l-right explanation="`l` 이동은 오른쪽으로 한 문자 이동합니다."}
::option[`j`]{#vim-nav-j-down .correct explanation="`j` 이동은 일반 모드에서 한 줄 아래로 이동합니다."}
:::

## 이동 명령 앞에 횟수 붙이기

많은 이동 명령 앞에 양의 횟수를 입력하면 해당 동작을 반복합니다. 예를 들면 다음과 같습니다.

```text
5j
3l
```

`5j`는 다섯 줄 아래로 이동하고 `3l`은 가능할 때 오른쪽으로 세 문자 위치 이동합니다. 횟수는 단어 이동 및 편집 명령과도 결합됩니다.

:::single-choice{#vim-navigation-count}
일반 모드에서 `4k`는 무엇을 하나요?

::option[가능할 때 네 줄 아래로 이동합니다.]{#vim-nav-four-down explanation="아래쪽 이동은 `j`를 사용하며 `k`는 반대 방향으로 움직입니다."}
::option[가능할 때 네 줄 위로 이동합니다.]{#vim-nav-four-up .correct explanation="횟수 `4`가 위쪽 `k` 이동을 네 번 반복합니다."}
::option[커서 위의 네 줄을 삭제합니다.]{#vim-nav-delete-four explanation="이동 명령 자체는 커서 위치만 바꿉니다. 삭제에는 `d` 같은 연산자가 필요합니다."}
:::

## 단어를 기준으로 이동하기

유용한 단어 이동 명령은 다음과 같습니다.

- `w`: 다음 단어의 시작으로 이동
- `b`: 현재 또는 이전 단어의 시작으로 이동
- `e`: 현재 또는 다음 단어의 끝으로 이동

대문자 `W`, `B`, `E`는 공백으로 구분된 WORD를 사용하여 문장 부호를 다르게 처리합니다. `3w`처럼 앞에 횟수를 붙이면 여러 단어를 지나 이동합니다.

:::single-choice{#vim-navigation-next-words}
앞으로 이동하여 세 번째 다음 단어 위치의 시작으로 가는 일반 모드 명령은 무엇인가요?

::option[`3w`]{#vim-nav-three-words .correct explanation="횟수가 다음 단어 이동을 세 번 적용합니다."}
::option[`w3`]{#vim-nav-word-three explanation="이 명령 형식에서 횟수는 이동 명령 앞에 옵니다. 뒤에 `3`을 두면 요청한 이동을 표현하지 않습니다."}
::option[`3b`]{#vim-nav-three-back explanation="`b` 이동은 앞으로가 아니라 이전 단어의 시작을 향해 움직입니다."}
:::

## 한 줄 안에서 이동하기

다음 이동 명령은 현재 줄의 위치를 대상으로 합니다.

- `0`: 0번 열로 이동
- `^`: 첫 번째 비공백 문자로 이동
- `$`: 줄 끝으로 이동

들여쓴 줄에서는 `0`과 `^`의 차이가 중요합니다.

:::single-choice{#vim-navigation-first-nonblank}
들여쓴 줄의 첫 번째 비공백 문자로 이동하는 명령은 무엇인가요?

::option[`0`]{#vim-nav-column-zero explanation="0은 들여쓰기 공백이 있을 수 있는 첫 번째 열로 이동합니다."}
::option[`$`]{#vim-nav-line-end explanation="달러 이동은 줄 끝을 대상으로 합니다."}
::option[`^`]{#vim-nav-first-nonblank .correct explanation="캐럿 이동은 선행 공백을 건너뛰고 첫 번째 비공백 문자에 도착합니다."}
:::

## 파일 안에서 이동하기

큰 범위를 이동할 때는 다음 일반 모드 명령을 사용합니다.

- `gg`: 첫 번째 줄로 이동
- `G`: 마지막 줄로 이동
- `42G`: 42번째 줄로 이동
- `Ctrl+F`: 약 한 화면 앞으로 이동
- `Ctrl+B`: 약 한 화면 뒤로 이동

`:42`를 입력하고 Enter를 누르는 것도 42번째 줄로 이동하는 방법입니다.

:::single-choice{#vim-navigation-file-end}
버퍼의 마지막 줄로 이동하는 일반 모드 명령은 무엇인가요?

::option[`gg`]{#vim-nav-first-line explanation="소문자 `gg`는 마지막이 아니라 첫 번째 줄로 이동합니다."}
::option[`$`]{#vim-nav-current-line-end explanation="달러 이동은 파일 끝이 아니라 현재 줄 끝으로 이동합니다."}
::option[`G`]{#vim-nav-last-line .correct explanation="횟수 없는 대문자 `G`는 마지막 줄로 이동합니다."}
:::

일회용 파일을 편집하면서 키보드 탐색을 연습하려면 다음 실습을 진행해 보세요.

1. **[Vim과 Nano로 Linux 텍스트 파일 편집하기](https://labex.io/ko/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - 실제 Linux 환경에서 Vim과 Nano로 파일을 만들고 편집하고 저장하고 탐색합니다.

## 요약

이제 여러 유용한 범위에서 Vim 버퍼를 탐색할 수 있습니다.

1. `h`, `j`, `k`, `l`로 문자나 줄 단위로 이동할 수 있습니다.
2. 숫자 접두사로 이동을 반복할 수 있습니다.
3. `w`, `b`, `e`로 단어 경계 사이를 이동할 수 있습니다.
4. 줄의 시작, 첫 텍스트 또는 끝을 대상으로 이동할 수 있습니다.
5. `gg`, `G` 또는 줄 번호로 파일 위치에 이동할 수 있습니다.
