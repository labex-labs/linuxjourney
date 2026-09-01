---
lesson_id: "emacs-manipulate-files"
course_id: "advanced-text-fu"
lang: "ko"
order_index: 10
title: "Emacs 파일 다루기"
description: "Emacs에서 파일 기반 버퍼를 방문하고 저장하고 이름을 바꾸고 다시 불러오고 검토하는 방법을 배웁니다."
meta_title: "Emacs 파일 다루기 - Advanced Text-Fu"
meta_description: "Emacs 파일 조작을 배웁니다. C-x C-s, C-x C-w, C-x C-f 명령으로 파일을 저장하고 다른 이름으로 저장하고 여는 핵심 작업을 익히세요."
meta_keywords: "Emacs, Emacs 파일 저장, Emacs 파일 열기, Emacs 튜토리얼, Linux 명령어, 초보자 Emacs, Emacs 가이드"
---

Emacs는 버퍼에서 파일을 방문합니다. 편집은 먼저 버퍼를 바꾸고 저장하면 현재 내용을 연결된 경로에 씁니다. 권한, 충돌하는 디스크 변경 또는 다른 오류가 쓰기를 막을 수 있으므로 미니버퍼 메시지를 읽으세요.

## 파일 방문하기

`find-file`을 실행하는 `C-x C-f`를 사용하고 미니버퍼에 경로를 입력한 뒤 Enter를 누릅니다.

```text
C-x C-f
```

Emacs는 읽을 수 있는 기존 파일을 버퍼에 열거나 경로가 없으면 새 파일 방문 버퍼를 준비합니다. 두 번째 경우에는 저장에 성공할 때까지 디스크에 파일이 존재하지 않습니다.

경로를 입력할 때 Tab 자동 완성을 사용할 수 있습니다. 디렉터리를 방문하면 일반적으로 디렉터리를 텍스트 파일로 처리하지 않고 Emacs의 디렉터리 편집기인 Dired를 엽니다.

:::single-choice{#emacs-find-file-key} 경로를 묻고 방문하는 Emacs 키 시퀀스는 무엇인가요?

::option[`C-x C-s`]{#emacs-file-save explanation="현재 파일 방문 버퍼를 저장하며 다른 경로를 방문하라는 입력을 요청하지 않습니다."}
::option[`C-x C-c`]{#emacs-file-exit explanation="파일을 여는 대신 Emacs 종료를 시작합니다."}
::option[`C-x C-f`]{#emacs-find-file .correct explanation="`find-file`을 실행하여 방문할 경로를 미니버퍼에서 묻습니다."}
:::

:::single-choice{#emacs-find-missing-file} `C-x C-f`가 존재하지 않는 경로를 방문할 때 디스크 파일은 일반적으로 언제 만들어지나요?

::option[새 버퍼가 성공적으로 저장된 뒤에만 만들어집니다.]{#emacs-file-created-on-save .correct explanation="파일이 없어도 버퍼에 편집 내용을 담을 수 있고 저장이 파일 생성을 수행합니다."}
::option[경로를 입력하자마자 만들어집니다.]{#emacs-file-created-immediately explanation="Emacs는 먼저 새 경로와 연결된 버퍼를 만들고 디스크 생성은 미룹니다."}
::option[Emacs 자체를 닫은 뒤에만 만들어집니다.]{#emacs-file-created-on-exit explanation="종료할 때 저장 여부를 물을 수 있지만 파일 생성은 반드시 Emacs 종료가 아니라 성공적인 저장과 연결됩니다."}
:::

## 현재 버퍼 저장하기

`save-buffer`를 실행하는 `C-x C-s`로 현재 파일 방문 버퍼를 저장합니다.

```text
C-x C-s
```

버퍼에 연결된 파일 이름이 없으면 Emacs가 이름을 묻습니다. 쓰기에 성공하면 버퍼의 수정 표시가 사라지고 실패하면 저장하지 않은 데이터가 버퍼에 남으며 오류가 보고됩니다.

:::single-choice{#emacs-save-current-buffer} 현재 파일 방문 버퍼를 저장하는 키 시퀀스는 무엇인가요?

::option[`C-x C-s`]{#emacs-save-buffer-key .correct explanation="`C-x C-s`는 현재 버퍼에 대해 `save-buffer`를 실행합니다."}
::option[`C-x C-w`]{#emacs-write-file-key explanation="다른 파일 이름을 묻고 버퍼가 방문하는 파일을 바꿉니다."}
::option[`C-x s`]{#emacs-save-some-key explanation="현재 버퍼 하나만 대상으로 하지 않고 여러 파일 방문 버퍼를 확인하여 저장 여부를 묻습니다."}
:::

## 다른 이름으로 쓰기

`write-file`을 실행하는 `C-x C-w`를 사용하면 경로를 묻고 버퍼를 그곳에 쓴 뒤 버퍼가 새 파일을 방문하게 합니다.

```text
C-x C-w
```

Emacs의 “다른 이름으로 저장” 동작입니다. 원래 경로를 계속 방문하면서 별도의 사본만 쓰는 것과는 다릅니다.

:::single-choice{#emacs-write-file-as} 현재 버퍼에 일반적인 다른 이름으로 저장 작업을 수행하는 키 시퀀스는 무엇인가요?

::option[`C-x C-f`]{#emacs-find-file-other explanation="파일을 방문하고 다른 버퍼로 전환할 수 있지만 현재 버퍼의 다른 이름으로 저장은 아닙니다."}
::option[`C-x k`]{#emacs-write-as-kill-buffer explanation="버퍼 종료 여부를 묻고 저장하지 않은 변경을 확인할 수 있지만 새 이름으로 저장하지 않습니다."}
::option[`C-x C-w`]{#emacs-write-file-answer .correct explanation="`write-file`은 선택한 경로에 쓰고 버퍼가 해당 파일을 방문하게 합니다."}
:::

## 수정된 여러 버퍼 검토하기

`save-some-buffers`를 실행하는 `C-x s`로 수정된 파일 방문 버퍼를 검토합니다.

```text
C-x s
```

Emacs는 일반적으로 저장 가능한 수정 버퍼마다 저장할지 묻습니다. 버퍼 이름을 읽고 의도적으로 답하세요. 조건 없이 모두 저장하는 단축키가 아닙니다.

:::single-choice{#emacs-save-some-buffers} `C-x s`는 일반적으로 무엇을 하나요?

::option[수정된 파일 방문 버퍼의 저장 여부를 묻습니다.]{#emacs-prompt-save-some .correct explanation="`save-some-buffers`는 저장 가능한 수정 버퍼를 검토하고 어느 버퍼를 쓸지 묻습니다."}
::option[이름을 표시하지 않고 모든 버퍼를 조용히 저장합니다.]{#emacs-silent-save-all explanation="일반적인 대화형 명령은 모든 버퍼를 조건 없이 쓰지 않고 사용자에게 묻습니다."}
::option[현재 버퍼를 저장한 뒤 모든 버퍼를 닫습니다.]{#emacs-close-all-buffers explanation="여러 버퍼 저장을 다루며 일반적으로 버퍼를 닫지 않습니다."}
:::

## 디스크 내용으로 되돌리기

파일이 디스크에서 바뀌었고 현재 버퍼 내용을 의도적으로 버리려면 `M-x revert-buffer`를 실행하고 확인 요청을 검토합니다. 되돌리기는 저장하지 않은 버퍼 편집을 파괴할 수 있으므로 어느 원본을 유지할지 확인한 뒤에만 사용하세요.

결정하기 전에 별도의 사본을 저장하거나 버전 관리 및 diff 도구로 비교하세요. 버퍼가 수정된 상태에서는 다시 불러오기 작업을 무해하다고 여기지 마세요.

## 요약

이제 방문과 쓰기를 혼동하지 않고 파일 기반 버퍼를 관리할 수 있습니다.

1. `C-x C-f`로 경로를 방문할 수 있습니다.
2. 없는 파일은 버퍼를 저장할 때만 만들 수 있습니다.
3. `C-x C-s`로 현재 버퍼를 저장할 수 있습니다.
4. `C-x C-w`로 새로 방문할 이름에 저장할 수 있습니다.
5. `C-x s`로 수정된 여러 버퍼를 검토할 수 있습니다.
