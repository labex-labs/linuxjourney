---
lesson_id: "emacs-exiting-and-help"
course_id: "advanced-text-fu"
lang: "ko"
order_index: 13
title: "Emacs 종료와 도움말"
description: "Emacs를 안전하게 종료하고 대기 중인 명령을 취소하며 도움말 주제를 확인하고 변경을 실행 취소하는 방법을 배웁니다."
meta_title: "Emacs 종료와 도움말 - Advanced Text-Fu"
meta_description: "Emacs 종료 명령과 도움말 접근 방법을 배웁니다. 초보자용 튜토리얼에서 기본 Emacs 탐색과 실행 취소 기능을 이해하세요."
meta_keywords: "Emacs 종료, Emacs 도움말, Emacs 실행 취소, Emacs 튜토리얼, Linux 텍스트 편집기, 초보자 가이드"
---

Emacs는 키, 함수, 변수, 활성 모드에 대한 문맥별 도움말을 제공합니다. 종료할 때 수정된 파일 방문 버퍼도 보호하여 각 쓰기를 저장하거나 거절할 기회를 줍니다.

## Emacs 종료하기

`save-buffers-kill-terminal`을 실행하는 `C-x C-c`로 Emacs 세션이나 터미널 연결 종료를 요청합니다.

```text
C-x C-c
```

Emacs는 관련된 수정 파일 방문 버퍼를 확인하고 저장할지 묻습니다. 각 버퍼 이름을 읽고 의도적으로 답하세요. 실행 중인 프로세스에 대해서도 물을 수 있습니다. 결정하기 전에 작업을 검사해야 한다면 종료를 취소하세요.

`emacsclient` 작업 흐름이나 Emacs 서버에서는 정확한 프레임 및 서버 동작이 다를 수 있지만 수정된 버퍼 요청은 여전히 주의 깊게 확인해야 합니다.

:::single-choice{#emacs-exit-key} 수정된 버퍼를 확인하며 정상적인 Emacs 종료를 요청하는 키 시퀀스는 무엇인가요?

::option[`C-x k`]{#emacs-exit-kill-buffer explanation="선택한 버퍼 하나를 종료하며 Emacs 세션 종료를 요청하지 않습니다."}
::option[`C-g`]{#emacs-exit-keyboard-quit explanation="Emacs를 닫지 않고 대기 중인 명령이나 요청을 취소합니다."}
::option[`C-x C-c`]{#emacs-exit-save-buffers .correct explanation="관련된 저장하지 않은 작업에 대한 요청을 포함하는 일반 저장 버퍼 및 종료 작업 흐름을 실행합니다."}
:::

## 도움말 디스패처 열기

표준 도움말 접두사는 `C-h`입니다. help for help를 실행하는 `C-h C-h`로 사용할 수 있는 도움말 명령 안내를 표시합니다.

```text
C-h C-h
```

두 번째 키가 필요한 도움말 종류를 선택합니다.

:::single-choice{#emacs-help-for-help} Emacs 도움말 시스템 사용법을 설명하는 키 시퀀스는 무엇인가요?

::option[`C-h C-h`]{#emacs-help-help .correct explanation="도움말 접두사 뒤에 다시 `C-h`를 누르면 도움말 디스패처 자체에 대한 도움말이 열립니다."}
::option[`C-x C-h`]{#emacs-help-prefix-list explanation="여기서 소개한 help-for-help 시퀀스가 아닙니다."}
::option[`C-h t`]{#emacs-help-tutorial-other explanation="더 넓은 도움말 메뉴를 설명하지 않고 튜토리얼을 바로 엽니다."}
:::

## 키와 편집기 상태 설명 보기

유용한 도움말 명령은 다음과 같습니다.

- `C-h k KEY`: 키 시퀀스가 실행하는 작업 설명
- `C-h f FUNCTION`: Emacs Lisp 함수 설명
- `C-h v VARIABLE`: Emacs Lisp 변수 설명
- `C-h m`: 현재 주 모드와 부 모드 설명
- `C-h t`: 대화형 튜토리얼 열기

예를 들어 `C-h k C-x C-s`를 입력하면 save-buffer 키 바인딩의 문서를 볼 수 있습니다.

:::single-choice{#emacs-describe-key} `C-x C-s`가 무엇을 하는지 알고 싶습니다. 해당 키 시퀀스 앞에 어떤 도움말 접두사를 입력해야 하나요?

::option[`C-h k`]{#emacs-describe-key-answer .correct explanation="`describe-key`는 키 시퀀스를 기다린 뒤 연결된 명령을 설명합니다."}
::option[`C-h f`]{#emacs-describe-function explanation="키 시퀀스를 읽어 바인딩을 확인하지 않고 함수 이름을 묻습니다."}
::option[`C-h v`]{#emacs-describe-variable explanation="변수 이름을 물으며 키 바인딩을 검사하지 않습니다."}
:::

## 대기 중인 명령 취소하기

요청, 일부만 입력한 키 시퀀스, 증분 검색 또는 취소하려는 다른 명령에 갇혔을 때 `keyboard-quit`에 연결된 `C-g`를 사용합니다.

```text
C-g
```

이미 일어난 버퍼 변경을 실행 취소하거나 Emacs를 종료하지는 않습니다. 현재 상호작용을 멈추고 가능한 경우 일반 편집으로 제어를 돌려줍니다.

:::single-choice{#emacs-cancel-pending-command} 현재 Emacs 요청이나 대기 중인 명령을 일반적으로 취소하는 키는 무엇인가요?

::option[`C-x C-c`]{#emacs-cancel-exit explanation="현재 요청만 취소하지 않고 Emacs 종료 작업 흐름을 시작합니다."}
::option[`C-y`]{#emacs-cancel-yank explanation="킬 링에서 텍스트를 yank하며 명령을 취소하지 않습니다."}
::option[`C-g`]{#emacs-keyboard-quit-answer .correct explanation="`keyboard-quit`는 현재 명령 상호작용을 중단하고 Emacs에 제어를 돌려줍니다."}
:::

## 버퍼 변경 실행 취소하기

일반적인 Emacs 구성에서는 `C-/`, `C-_` 또는 `C-x u`로 실행 취소를 호출합니다.

```text
C-/
```

실행 취소 명령을 반복하면 최근 버퍼 변경을 거슬러 올라갑니다. 커서 이동만으로는 일반적으로 버퍼 변경이 되지 않습니다. Emacs 버전과 구성은 `undo-redo` 및 더 고급 기록 도구를 제공할 수 있으므로 실제 실행 취소 및 다시 실행 바인딩에 `C-h k`를 사용해 로컬 동작을 확인하세요.

:::single-choice{#emacs-undo-change} 최근 Emacs 버퍼 변경을 실행 취소하는 표준 키 바인딩은 무엇인가요?

::option[`C-/`]{#emacs-undo-control-slash .correct explanation="`C-/`는 일반 구성에서 `C-_` 및 `C-x u`와 함께 표준 실행 취소 바인딩입니다."}
::option[`C-x C-s`]{#emacs-undo-save explanation="버퍼의 실행 취소 기록을 이동하지 않고 현재 버퍼를 저장합니다."}
::option[`C-w`]{#emacs-undo-kill explanation="활성 영역을 kill하여 실행 취소 대신 또 다른 변경을 만듭니다."}
:::

`*scratch*`를 열고 일회용 변경을 만든 뒤 실행 취소하고 `C-h k`로 익숙하지 않은 키를 확인하고 `C-g`로 미니버퍼 요청을 취소한 다음 정상적으로 종료해 보세요.

## 요약

이제 저장하지 않은 작업을 무시하지 않고 도움을 얻고 Emacs를 종료할 수 있습니다.

1. `C-x C-c`로 수정 버퍼 검사를 거쳐 종료할 수 있습니다.
2. `C-h C-h`로 help for help를 열 수 있습니다.
3. 키, 함수, 변수 또는 활성 모드의 설명을 볼 수 있습니다.
4. `C-g`로 대기 중인 명령을 취소할 수 있습니다.
5. 확인한 로컬 바인딩으로 최근 버퍼 변경을 실행 취소할 수 있습니다.
