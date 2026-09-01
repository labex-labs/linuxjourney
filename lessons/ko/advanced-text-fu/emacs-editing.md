---
lesson_id: "emacs-editing"
course_id: "advanced-text-fu"
lang: "ko"
order_index: 12
title: "Emacs 편집"
description: "포인트를 이동하고 영역을 활성화하며 Emacs 킬 링 명령으로 텍스트를 편집하는 방법을 배웁니다."
meta_title: "Emacs 편집 - Advanced Text-Fu"
meta_description: "초보자용 가이드로 Emacs 편집의 기초를 익혀 보세요. 강력한 Linux 텍스트 편집기에서 텍스트 탐색, 잘라내기, 붙여넣기에 필요한 핵심 Emacs 명령을 배웁니다."
meta_keywords: "Emacs, Emacs 튜토리얼, Emacs 명령어, 텍스트 편집기, Linux 편집기, Emacs 탐색, 초보자 Emacs, Emacs 가이드"
---

Emacs는 현재 커서 위치를 **포인트**라고 부릅니다. 이동 명령은 포인트의 위치를 바꾸고 편집 명령은 주변 텍스트를 삽입, 삭제, kill, 복사 또는 yank합니다. 아래 키 표기에서 `C-`는 Control, `M-`은 일반적으로 Alt인 Meta를 뜻합니다.

## 문자와 줄을 기준으로 이동하기

화살표와 다른 플랫폼 탐색 키도 작동할 수 있지만 Emacs의 표준 이동 명령은 터미널과 그래픽 세션 모두에서 사용할 수 있습니다.

- `C-f`: 한 문자 앞으로 이동
- `C-b`: 한 문자 뒤로 이동
- `C-n`: 다음 줄로 이동
- `C-p`: 이전 줄로 이동
- `C-a`: 줄 시작으로 이동
- `C-e`: 줄 끝으로 이동

:::single-choice{#emacs-edit-next-line} 포인트를 다음 줄로 이동하는 Emacs 키는 무엇인가요?

::option[`C-p`]{#emacs-edit-previous-line explanation="`C-p`는 반대 방향인 이전 줄로 이동합니다."}
::option[`C-n`]{#emacs-edit-next-line-answer .correct explanation="next-line을 뜻하는 `C-n`은 포인트를 다음 화면 줄 위치로 아래쪽 이동합니다."}
::option[`C-f`]{#emacs-edit-forward-character explanation="`C-f`는 다음 줄이 아니라 한 문자 앞으로 이동합니다."}
:::

## 단어와 버퍼 경계를 기준으로 이동하기

Meta 명령은 더 큰 단위를 지나 이동합니다.

- `M-f`: 한 단어 앞으로 이동
- `M-b`: 한 단어 뒤로 이동
- `M-<`: 버퍼 시작으로 이동
- `M->`: 버퍼 끝으로 이동

많은 키보드에서 Alt가 Meta 역할을 합니다. 해당 조합을 사용할 수 없으면 `Esc`를 누른 뒤 다음 키를 누르는 방식으로 동등한 Meta 명령을 보낼 수 있습니다.

:::single-choice{#emacs-edit-buffer-end} 포인트를 버퍼 끝으로 이동하는 Emacs 키는 무엇인가요?

::option[`C-e`]{#emacs-edit-line-end explanation="`C-e`는 전체 버퍼가 아니라 현재 줄 끝으로 이동합니다."}
::option[`M-<`]{#emacs-edit-buffer-start explanation="`M-<`는 버퍼 시작으로 이동합니다."}
::option[`M->`]{#emacs-edit-buffer-end-answer .correct explanation="`M->`는 포인트를 현재 버퍼 끝으로 이동합니다."}
:::

## 영역 정의하기

**마크**는 저장된 버퍼 위치입니다. 포인트와 마크 사이의 텍스트를 **영역**이라고 합니다. 일부 문서에서 `C-space`로 쓰는 `C-SPC`를 눌러 `set-mark-command`를 실행한 뒤 포인트를 이동하여 활성 영역을 확장합니다.

터미널에서 `C-SPC`는 `C-@`로 인코딩될 수 있습니다. 강조 표시는 transient-mark 설정에 따라 달라지지만 포인트와 마크는 여전히 영역을 정의합니다.

:::single-choice{#emacs-edit-set-mark} 포인트에 마크를 설정하여 영역 정의를 시작하는 키는 무엇인가요?

::option[`C-w`]{#emacs-edit-kill-region-before-mark explanation="`C-w`는 이미 정의된 영역을 kill하며 초기 마크 설정 명령이 아닙니다."}
::option[`C-y`]{#emacs-edit-yank-before-mark explanation="`C-y`는 킬 링의 텍스트를 삽입하며 선택을 시작하지 않습니다."}
::option[`C-SPC`]{#emacs-edit-control-space .correct explanation="`set-mark-command`가 마크를 놓은 뒤 이동하면 마크와 포인트 사이 영역이 바뀝니다."}
:::

## 영역 kill하거나 복사하기

Emacs는 kill하거나 복사한 텍스트를 **킬 링**에 저장합니다.

- `C-w`: 활성 영역을 제거하고 킬 링에 추가
- `M-w`: 활성 영역을 제거하지 않고 킬 링에 복사
- `C-k`: 포인트에서 줄 끝까지 kill. 반복하면 줄 바꿈도 포함할 수 있음

kill은 제거한 텍스트를 나중에 yank할 수 있도록 보관하므로 일반 삭제와 다릅니다.

:::single-choice{#emacs-edit-copy-region} 활성 영역을 제거하지 않고 킬 링에 복사하는 키는 무엇인가요?

::option[`M-w`]{#emacs-edit-copy-active-region .correct explanation="`M-w`에 연결된 `kill-ring-save`는 영역을 삭제하지 않고 복사합니다."}
::option[`C-w`]{#emacs-edit-kill-active-region explanation="`C-w`는 영역을 킬 링에 저장하면서 제거합니다."}
::option[`C-k`]{#emacs-edit-kill-line explanation="`C-k`는 선택한 영역을 그대로 복사하지 않고 줄 끝을 향한 텍스트를 kill합니다."}
:::

## 킬 링에서 yank하기

`C-y`로 가장 최근 킬 링 항목을 포인트에 yank합니다. yank 직후 `M-y`를 누르면 삽입된 텍스트를 이전 킬 링 항목으로 바꾸고 `M-y`를 반복하면 항목을 순환합니다.

```text
C-y
M-y
```

`C-y` 뒤에 관련 없는 다른 명령이 실행되면 `M-y`는 더 이상 같은 yank-pop 문맥을 갖지 않습니다.

:::single-choice{#emacs-edit-yank-latest} 가장 최근 킬 링 항목을 포인트에 삽입하는 키는 무엇인가요?

::option[`C-y`]{#emacs-edit-yank-answer .correct explanation="`C-y`에 연결된 `yank`는 최신 킬 링 텍스트를 현재 버퍼에 삽입합니다."}
::option[`M-y`]{#emacs-edit-yank-pop explanation="`M-y`는 일반적으로 방금 yank한 항목을 이전 항목으로 바꾸며 앞선 yank 문맥에 의존합니다."}
::option[`C-d`]{#emacs-edit-delete-character explanation="`C-d`는 포인트 뒤 문자를 삭제하며 킬 링 텍스트를 가져오지 않습니다."}
:::

`*scratch*`나 일회용 파일에서 포인트를 이동하고 마크를 설정하고 한 영역을 복사하고 다른 영역을 kill한 뒤 둘을 다시 yank해 보세요. 결과 파일을 보관할 가치가 있을 때만 저장합니다.

## 요약

이제 포인트, 마크, 킬 링을 사용하여 Emacs 텍스트를 탐색하고 재배치할 수 있습니다.

1. Control 명령으로 문자나 줄 단위로 이동할 수 있습니다.
2. Meta 명령으로 단어나 버퍼 경계를 기준으로 이동할 수 있습니다.
3. `C-SPC`로 마크를 설정하여 영역을 정의할 수 있습니다.
4. `C-w`로 kill하거나 `M-w`로 복사할 수 있습니다.
5. `C-y`로 yank하고 바로 이어 `M-y`로 순환할 수 있습니다.
