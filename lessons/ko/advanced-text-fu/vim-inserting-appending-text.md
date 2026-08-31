---
lesson_id: "vim-inserting-appending-text"
course_id: "advanced-text-fu"
lang: "ko"
order_index: 6
title: "Vim에서 텍스트 삽입하고 덧붙이기"
description: "Vim이 현재 커서의 앞, 뒤, 위, 아래에서 입력 모드로 들어가는 방법을 배웁니다."
meta_title: "Vim에서 텍스트 삽입하고 덧붙이기 - Advanced Text-Fu"
meta_description: "Vim의 삽입과 덧붙이기 차이를 배웁니다. i, a, o 같은 명령을 익혀 텍스트를 효율적으로 편집하고 내용을 덧붙이며 줄을 추가하세요."
meta_keywords: "vim 덧붙이기, vim append와 insert, vim 삽입과 덧붙이기, vim 줄 추가, vim 텍스트 편집, vim 명령어, vim 튜토리얼, 입력 모드, append 모드"
---

일반 모드에서 Vim은 키를 명령으로 해석합니다. 입력 모드에서는 입력한 텍스트를 버퍼에 삽입합니다. 여러 일반 모드 명령은 서로 다른 위치에서 입력 모드로 들어가므로 별도로 이동하지 않고 곧바로 입력을 시작할 수 있습니다.

`Esc`를 눌러 입력 모드를 나가고 일반 모드로 돌아갑니다. 어떤 모드가 활성 상태인지 확실하지 않을 때 `Esc`를 누르면 일반 모드를 다시 확립하는 안전한 방법이지만 대기 중인 작업을 취소할 수 있습니다.

:::single-choice{#vim-insert-return-normal}
일반적으로 입력 모드에서 일반 모드로 돌아가는 키는 무엇인가요?

::option[`Esc`]{#vim-insert-escape .correct explanation="Escape는 현재 삽입을 끝내고 Vim을 일반 모드로 되돌립니다."}
::option[`Enter`]{#vim-insert-enter explanation="Enter는 입력 모드를 유지하면서 줄 바꿈을 삽입합니다."}
::option[`Tab`]{#vim-insert-tab explanation="Tab은 들여쓰기를 삽입하거나 구성된 자동 완성 동작을 실행하며 일반적으로 입력 모드를 나가지 않습니다."}
:::

## 커서 앞이나 뒤에 삽입하기

일반 모드에서 다음 키를 사용합니다.

- `i`: 커서 앞에서 입력 모드로 진입
- `a`: 커서 뒤에서 입력 모드로 진입

예를 들어 `abc`에서 커서가 `b` 위에 있으면 `i`는 `b` 앞에서 시작하고 `a`는 `b` 뒤에서 시작합니다. 두 명령 모두 모드를 바꾸며 이후에 입력하는 텍스트가 삽입됩니다.

:::single-choice{#vim-insert-before-cursor}
커서 바로 앞에서 입력 모드로 들어가는 일반 모드 키는 무엇인가요?

::option[`a`]{#vim-insert-a-after explanation="소문자 `a`는 앞에 삽입하지 않고 커서 뒤에 덧붙입니다."}
::option[`o`]{#vim-insert-o-below explanation="소문자 `o`는 입력 모드로 들어가기 전에 현재 줄 아래에 새 줄을 엽니다."}
::option[`i`]{#vim-insert-i-before .correct explanation="소문자 `i`는 커서 아래 문자 앞인 현재 커서 위치에서 삽입을 시작합니다."}
:::

## 줄 경계에 삽입하기

대문자 명령은 현재 줄의 의미 있는 위치를 대상으로 합니다.

- `I`: 첫 번째 비공백 문자 앞에서 입력 모드로 진입
- `A`: 줄 끝에서 입력 모드로 진입

들여쓴 줄에서 `I`는 들여쓰기를 건너뛰고 첫 번째 비공백 텍스트 앞에서 시작합니다. 0번 열에 삽입해야 한다면 `0i`를 사용합니다.

:::single-choice{#vim-insert-first-nonblank}
현재 줄의 첫 번째 비공백 문자 앞에서 삽입을 시작하는 일반 모드 명령은 무엇인가요?

::option[`i`]{#vim-insert-lower-i explanation="소문자 `i`는 현재 커서 위치를 사용하며 먼저 줄의 첫 텍스트로 이동하지 않습니다."}
::option[`A`]{#vim-insert-capital-a explanation="대문자 `A`는 현재 줄 끝에서 삽입을 시작합니다."}
::option[`I`]{#vim-insert-capital-i .correct explanation="대문자 `I`는 첫 번째 비공백 문자로 이동한 뒤 그 앞에서 입력 모드로 들어갑니다."}
:::

:::single-choice{#vim-append-line-end}
현재 줄 끝으로 이동하고 입력 모드로 들어가는 일반 모드 명령은 무엇인가요?

::option[`A`]{#vim-append-capital-a .correct explanation="대문자 `A`는 줄 끝 이동과 입력 모드 진입을 결합합니다."}
::option[`$`]{#vim-move-line-end explanation="달러 이동은 줄 끝에 도착하지만 일반 모드에 남습니다."}
::option[`a`]{#vim-append-one-position explanation="소문자 `a`는 줄 끝으로 이동하지 않고 현재 커서 뒤에서 시작합니다."}
:::

## 새 줄 열기

일반 모드에서 다음 키를 사용합니다.

- `o`: 현재 줄 아래에 새 줄을 열고 입력 모드로 진입
- `O`: 현재 줄 위에 새 줄을 열고 입력 모드로 진입

Vim은 현재 설정과 파일 형식 규칙에 따라 들여쓰기를 적용합니다. 횟수로 줄 열기 작업을 반복할 수 있지만 결과 커서 위치를 예측할 수 있도록 먼저 한 줄 형식을 익히세요.

:::single-choice{#vim-open-line-above}
현재 줄 위에 새 줄을 열고 입력 모드로 들어가는 일반 모드 명령은 무엇인가요?

::option[`o`]{#vim-open-lower-o explanation="소문자 `o`는 현재 줄 아래에 엽니다."}
::option[`O`]{#vim-open-upper-o .correct explanation="대문자 `O`는 위에 새 줄을 열고 그곳에서 삽입을 시작합니다."}
::option[`A`]{#vim-open-upper-a explanation="대문자 `A`는 기존 줄 끝에 덧붙이며 위에 새 줄을 열지 않습니다."}
:::

일반 모드와 입력 모드 사이의 전환을 연습하려면 다음 실습을 진행해 보세요.

1. **[Vim과 Nano로 Linux 텍스트 파일 편집하기](https://labex.io/ko/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - vi/vim과 nano로 파일을 만들고 텍스트를 편집하고 저장하고 탐색하며 Vim의 일반 모드와 입력 모드를 연습합니다.

## 요약

이제 새 텍스트가 들어갈 위치에서 입력 모드로 들어갈 수 있습니다.

1. `Esc`로 일반 모드로 돌아갈 수 있습니다.
2. `i` 또는 `a`로 커서 앞이나 뒤에 삽입할 수 있습니다.
3. `I` 또는 `A`로 첫 텍스트나 줄 끝에 삽입할 수 있습니다.
4. `o`로 아래에 줄을 열 수 있습니다.
5. `O`로 위에 줄을 열 수 있습니다.
