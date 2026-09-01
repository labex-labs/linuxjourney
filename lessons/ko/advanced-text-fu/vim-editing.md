---
lesson_id: "vim-editing"
course_id: "advanced-text-fu"
lang: "ko"
order_index: 7
title: "Vim 편집"
description: "Vim이 텍스트 편집을 위해 연산자, 이동, 레지스터, 붙여넣기, 실행 취소 명령을 결합하는 방법을 배웁니다."
meta_title: "Vim 편집 - Advanced Text-Fu"
meta_description: "핵심 편집 명령을 다루는 초보자용 Vim 튜토리얼입니다. Vim 텍스트 편집기에서 텍스트를 삭제하고 변경하고 복사하고 붙여넣는 방법을 배워 Linux 작업 흐름을 개선하세요."
meta_keywords: "Vim 편집, Vim 명령어, Linux 텍스트 편집기, Vim 튜토리얼, Vim 가이드, 초보자 Vim, dd 명령, Vim 삭제"
---

Vim 편집 명령은 흔히 연산자와 이동 또는 텍스트 객체를 결합합니다. 이 문법 덕분에 같은 동작을 문자, 단어, 줄 및 더 큰 범위에 사용할 수 있습니다. 연습하기 전에 `Esc`를 눌러 일반 모드로 돌아가세요.

## 연산자와 이동 결합하기

일반 형식은 다음과 같습니다.

```text
[count] operator [count] motion
```

자주 쓰는 연산자는 다음과 같습니다.

- `d`: 텍스트 삭제
- `c`: 텍스트를 변경한 뒤 입력 모드로 진입
- `y`: 텍스트를 yank, 즉 복사

예를 들어 `dw`는 `w` 이동 범위까지 삭제하고 `d$`는 커서부터 줄 끝까지 삭제합니다. `2dw`는 두 번의 단어 이동 범위에 삭제를 적용합니다.

:::single-choice{#vim-edit-operator-motion} 일반 모드에서 `d$`는 무엇을 하나요?

::option[커서부터 전체 파일을 삭제합니다.]{#vim-edit-delete-file-end explanation="달러 이동은 전체 버퍼의 끝이 아니라 현재 줄 끝을 대상으로 합니다."}
::option[커서부터 줄 끝까지 삭제합니다.]{#vim-edit-delete-line-end .correct explanation="`d` 연산자가 `$` 줄 끝 이동에 적용됩니다."}
::option[텍스트를 바꾸지 않고 줄 끝으로 이동합니다.]{#vim-edit-move-line-end explanation="`$`만 사용하면 이동하지만 앞의 `d`가 이동 범위를 삭제로 바꿉니다."}
:::

## 문자와 줄 편집하기

일부 명령은 편리한 단축 형식입니다.

- `x`: 커서 아래 문자 삭제
- `dd`: 현재 줄을 줄 단위로 삭제
- `3dd`: 현재 줄부터 세 줄 삭제
- `cc`: 현재 줄을 변경하고 입력 모드로 진입
- `r{char}`: 커서 아래 문자를 `{char}`로 교체
- `R`: `Esc`를 누를 때까지 바꾸기 모드로 진입

`dd`처럼 연산자를 반복하면 줄 단위가 됩니다. 횟수는 대상 줄 수를 늘립니다.

:::single-choice{#vim-edit-delete-three-lines} 현재 줄과 다음 두 줄을 삭제하는 일반 모드 명령은 무엇인가요?

::option[`dd3`]{#vim-edit-dd-three explanation="이 명령 형식에서 횟수는 반복된 연산자 앞에 옵니다."}
::option[`3x`]{#vim-edit-three-x explanation="완전한 세 줄이 아니라 커서 아래와 뒤의 문자 세 개를 삭제합니다."}
::option[`3dd`]{#vim-edit-three-dd .correct explanation="횟수가 줄 단위 `dd` 명령에 적용되어 현재 줄부터 세 줄을 삭제합니다."}
:::

## 텍스트 변경하고 입력 모드로 들어가기

`c` 연산자는 선택한 텍스트를 제거하고 입력 모드로 들어가 대체 내용을 입력할 수 있게 합니다.

- `ce`: 단어 끝까지 변경
- `c$`: 줄 끝까지 변경
- `cc`: 현재 줄 전체 변경
- `ciw`: 커서 아래 내부 단어 변경
- `caw`: Vim이 정의한 주변 공백을 포함한 단어 텍스트 객체 변경

`cw`의 동작에는 역사적인 특수 사례가 있어 흔히 `ce`처럼 작동합니다. `iw` 같은 텍스트 객체로 의도한 경계를 더 명확하게 표현할 수 있습니다.

:::single-choice{#vim-edit-change-inner-word} 커서 아래 내부 단어를 삭제하고 입력 모드로 들어가 대체하는 일반 모드 명령은 무엇인가요?

::option[`diw`]{#vim-edit-delete-inner-word explanation="내부 단어를 삭제하지만 대체 텍스트를 시작하지 않고 일반 모드에 남습니다."}
::option[`yiw`]{#vim-edit-yank-inner-word explanation="버퍼를 바꾸거나 입력 모드에 들어가지 않고 내부 단어를 yank합니다."}
::option[`ciw`]{#vim-edit-change-inner-word-answer .correct explanation="`c` 연산자는 `iw` 텍스트 객체를 변경한 뒤 입력 모드로 들어갑니다."}
:::

## 텍스트 yank하고 put하기

Vim에서는 복사를 **yank**, 붙여넣기를 **put**이라고 부릅니다.

- `yw`: 단어 이동 범위까지 yank
- `yy`: 현재 줄 yank
- `p`: 문자 단위 텍스트는 커서 뒤에, 줄 단위 텍스트는 현재 줄 아래에 put
- `P`: 커서 앞이나 현재 줄 위에 put

삭제와 변경도 텍스트를 레지스터에 저장하므로 이후 `p`는 이전에 yank한 내용이 아니라 가장 최근에 삭제한 내용을 붙일 수 있습니다. 이름 있는 레지스터로 특정 텍스트를 보존할 수 있지만 먼저 가장 최근 작업이 무엇을 저장했는지 살펴보는 것부터 시작하세요.

:::single-choice{#vim-edit-yank-put-line} `yy`로 현재 줄을 yank한 뒤 그 줄을 현재 줄 아래에 put하는 명령은 무엇인가요?

::option[`p`]{#vim-edit-put-below .correct explanation="줄 단위로 yank한 텍스트에서 소문자 `p`는 저장된 줄을 현재 줄 아래에 놓습니다."}
::option[`P`]{#vim-edit-put-above explanation="대문자 `P`는 줄 단위 텍스트를 현재 줄 위에 놓습니다."}
::option[`u`]{#vim-edit-undo-not-put explanation="소문자 `u`는 변경을 실행 취소하며 yank한 줄을 붙이지 않습니다."}
:::

## 실행 취소, 다시 실행, 반복하기

일반 모드에서 다음 명령을 사용합니다.

- `u`: 가장 최근 변경 실행 취소
- `Ctrl+R`: 실행 취소한 변경 다시 실행
- `.`: 적용 가능한 경우 현재 위치에서 가장 최근 변경 반복
- `J`: 현재 줄과 다음 줄 연결

실행 취소 기록은 단순한 커서 이동이 아니라 버퍼 변경에 적용됩니다. 무제한이거나 영구적인 실행 취소 기록에 의존하지 말고 저장 지점을 만들고 편집 내용을 검토하세요.

:::single-choice{#vim-edit-redo-change} 방금 실행 취소한 변경을 다시 실행하는 일반 모드 명령은 무엇인가요?

::option[`Ctrl+U`]{#vim-edit-control-u explanation="일반 모드에서 `Ctrl+U`는 약 반 화면 위로 스크롤하며 다시 실행이 아닙니다."}
::option[`.`]{#vim-edit-dot-repeat explanation="점은 실행 취소 기록을 앞으로 이동하지 않고 최신 변경을 새 동작으로 반복합니다."}
::option[`Ctrl+R`]{#vim-edit-control-r .correct explanation="Vim은 일반 모드에서 `Ctrl+R`로 실행 취소 기록을 앞으로 이동합니다."}
:::

일회용 텍스트에서 연산자, 이동, 복구를 연습하려면 다음 실습을 진행해 보세요.

1. **[Vim과 Nano로 Linux 텍스트 파일 편집하기](https://labex.io/ko/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - vi/vim과 nano로 파일을 만들고 편집하고 저장하고 탐색하며 삭제, 변경, yank, put을 실제 상황에 적용합니다.

## 요약

이제 일반 모드에서 Vim 편집을 구성하고 실수에서 복구할 수 있습니다.

1. 연산자를 이동, 텍스트 객체, 횟수와 결합할 수 있습니다.
2. 선택한 범위에서 문자나 전체 줄을 삭제할 수 있습니다.
3. 텍스트를 변경하고 대체를 위한 입력 모드로 들어갈 수 있습니다.
4. 문자 단위나 줄 단위 텍스트를 yank하고 put할 수 있습니다.
5. 변경을 의도적으로 실행 취소하고 다시 실행하거나 반복할 수 있습니다.
