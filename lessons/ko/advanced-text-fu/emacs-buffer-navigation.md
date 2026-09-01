---
lesson_id: "emacs-buffer-navigation"
course_id: "advanced-text-fu"
lang: "ko"
order_index: 11
title: "Emacs 버퍼 탐색"
description: "Emacs 버퍼를 전환하고 종료하며 표시 창을 분할하고 선택하고 닫는 방법을 배웁니다."
meta_title: "Emacs 버퍼 탐색 - Advanced Text-Fu"
meta_description: "Emacs 버퍼 탐색 종합 가이드입니다. 핵심 Emacs 명령으로 버퍼를 효율적으로 전환하고 창을 분할하며 작업 흐름을 관리하는 방법을 배웁니다."
meta_keywords: "emacs 탐색, emacs 버퍼 전환, emacs 버퍼 관리, emacs 명령어, C-x b, C-x k, C-x 2, 텍스트 편집기, linux"
---

Emacs 버퍼는 텍스트나 편집기 상태를 보관하고 창은 버퍼를 표시합니다. 버퍼는 보이지 않아도 존재할 수 있고 여러 창이 하나의 버퍼를 표시할 수 있습니다. 한 객체를 관리해도 다른 객체가 자동으로 함께 관리되지는 않습니다.

## 버퍼 전환하기

`switch-to-buffer`를 실행하는 `C-x b`로 현재 창에 표시할 버퍼 이름을 선택합니다.

```text
C-x b
```

미니버퍼는 기존 이름의 자동 완성을 제공합니다. 새 이름을 입력하면 그 이름을 가진 파일이 아닌 버퍼를 만들 수 있으며 파일 경로를 방문하지는 않습니다.

기본적으로 `C-x Right`는 `next-buffer`, `C-x Left`는 `previous-buffer`를 실행하여 선택된 창에서 버퍼를 순환합니다.

:::single-choice{#emacs-switch-buffer-key} 현재 창에 표시할 버퍼 이름을 묻는 키 시퀀스는 무엇인가요?

::option[`C-x C-f`]{#emacs-buffer-find-file explanation="파일 경로를 묻고 방문하며 기존 버퍼를 이름으로 고르는 작업과는 다릅니다."}
::option[`C-x b`]{#emacs-switch-buffer .correct explanation="`switch-to-buffer`는 버퍼 이름을 읽고 선택된 창에 해당 버퍼를 표시합니다."}
::option[`C-x k`]{#emacs-buffer-kill explanation="선택된 창을 버퍼로 전환하지 않고 종료할 버퍼를 묻습니다."}
:::

## 선택된 창 분할하기

`C-x 2`로 선택된 창을 위아래 창으로 나눕니다.

```text
C-x 2
```

`C-x 3`으로 왼쪽과 오른쪽 창으로 나눕니다.

```text
C-x 3
```

새 창은 처음에 버퍼 하나를 표시하며 흔히 같은 버퍼를 표시합니다. 어느 창에서든 독립적으로 버퍼를 전환할 수 있습니다.

:::single-choice{#emacs-split-side-by-side} 선택된 Emacs 창을 왼쪽과 오른쪽 창으로 나누는 키 시퀀스는 무엇인가요?

::option[`C-x 1`]{#emacs-window-one explanation="다른 창을 삭제하고 선택된 창을 프레임의 유일한 창으로 만듭니다."}
::option[`C-x 2`]{#emacs-window-below explanation="나란한 분할이 아니라 위아래 창을 만듭니다."}
::option[`C-x 3`]{#emacs-window-right .correct explanation="`C-x 3`에 연결된 `split-window-right`는 왼쪽과 오른쪽 창을 만듭니다."}
:::

## 창 선택하고 닫기

`other-window`를 실행하는 `C-x o`로 다음 창을 선택합니다.

```text
C-x o
```

창 표시를 제거할 때는 다음 명령을 사용합니다.

- `C-x 0`: 선택된 창 삭제
- `C-x 1`: 현재 프레임의 다른 창 삭제

창을 삭제해도 일반적으로 표시하던 버퍼는 살아 있습니다. 다른 창에서 해당 버퍼를 다시 표시할 수 있습니다.

:::single-choice{#emacs-select-other-window} 포인트와 키보드 포커스를 다른 Emacs 창으로 옮기는 키 시퀀스는 무엇인가요?

::option[`C-x 0`]{#emacs-delete-selected-window explanation="다른 창으로 포커스를 옮기지 않고 선택된 창을 삭제합니다."}
::option[`C-x o`]{#emacs-other-window .correct explanation="`other-window`는 프레임의 다른 창으로 선택을 순환합니다."}
::option[`C-x b`]{#emacs-switch-in-window explanation="선택된 창 자체가 아니라 현재 창이 표시하는 버퍼를 바꿉니다."}
:::

:::single-choice{#emacs-keep-one-window} 선택된 창은 유지하고 해당 프레임의 다른 창을 삭제하는 키 시퀀스는 무엇인가요?

::option[`C-x 1`]{#emacs-delete-other-windows .correct explanation="`delete-other-windows`는 선택된 창을 프레임의 유일한 창으로 만듭니다."}
::option[`C-x 0`]{#emacs-delete-current-window explanation="선택된 창을 보존하지 않고 그 창 자체를 삭제합니다."}
::option[`C-x 2`]{#emacs-add-lower-window explanation="프레임을 창 하나로 줄이지 않고 다른 창을 추가합니다."}
:::

## 버퍼 종료하기

`kill-buffer`를 실행하는 `C-x k`로 Emacs에서 제거할 버퍼를 묻습니다.

```text
C-x k
```

현재 버퍼가 기본 선택입니다. 파일 방문 버퍼에 저장하지 않은 변경이 있으면 Emacs가 종료하기 전에 경고합니다. 수정된 버퍼를 종료하면 편집 내용을 버릴 수 있으므로 요청을 읽으세요.

버퍼 종료는 창 삭제와 다릅니다. Emacs는 종료된 버퍼를 표시하던 모든 창에서 다른 버퍼로 교체하지만 창을 삭제해도 버퍼는 그대로 남을 수 있습니다.

:::single-choice{#emacs-kill-buffer-key} 종료할 Emacs 버퍼를 묻는 키 시퀀스는 무엇인가요?

::option[`C-x 0`]{#emacs-kill-window-only explanation="창 표시를 삭제하지만 일반적으로 버퍼는 살아 있습니다."}
::option[`C-x k`]{#emacs-kill-buffer-answer .correct explanation="`kill-buffer`는 필요한 수정 버퍼 확인을 거친 뒤 선택한 버퍼를 Emacs에서 제거합니다."}
::option[`C-x b`]{#emacs-kill-switch explanation="현재 창을 이름이 지정된 버퍼로 전환하며 버퍼를 종료하지 않습니다."}
:::

`*scratch*`와 일회용 버퍼로 이 명령들을 연습하세요. 파일 방문 버퍼를 종료하기 전에 수정 표시가 저장하지 않은 작업을 나타내는지 확인합니다.

## 요약

이제 Emacs가 저장하는 내용과 각 창이 표시하는 내용을 관리할 수 있습니다.

1. `C-x b`로 선택된 창의 버퍼를 전환할 수 있습니다.
2. `C-x 2`로 아래에, `C-x 3`으로 오른쪽에 창을 나눌 수 있습니다.
3. `C-x o`로 다른 창을 선택할 수 있습니다.
4. `C-x 0` 또는 `C-x 1`로 창 표시를 제거할 수 있습니다.
5. 저장하지 않은 변경을 검토한 뒤에만 `C-x k`로 버퍼를 종료할 수 있습니다.
