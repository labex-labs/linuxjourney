---
lesson_id: "emacs-text-editor"
course_id: "advanced-text-fu"
lang: "ko"
order_index: 9
title: "Emacs"
description: "Emacs를 시작하고 키 표기법을 해석하며 버퍼, 창, 프레임을 구분하는 방법을 배웁니다."
meta_title: "Emacs - Advanced Text-Fu"
meta_description: "강력하고 확장 가능한 Linux 텍스트 편집기 Emacs를 배웁니다. Emacs 버퍼와 기본 사용법을 이해하고 Emacs 여정을 시작하세요."
meta_keywords: "Emacs, Linux 텍스트 편집기, Emacs 튜토리얼, Emacs 버퍼, Linux 명령어, 초보자, 가이드"
---

GNU Emacs는 Emacs Lisp로 동작을 사용자 지정할 수 있는 확장 가능한 텍스트 편집기입니다. 일반 텍스트 편집, 프로그래밍 모드, 파일 및 버퍼 관리와 여러 선택적 패키지를 지원합니다. 모든 확장을 사용하지 않아도 핵심 편집 명령을 배울 수 있습니다.

## Emacs 확인하고 시작하기

Emacs가 설치되어 있다고 가정하지 마세요. 쉘이 어떻게 해석하는지 확인합니다.

```bash
$ command -v emacs
/usr/bin/emacs
```

일반 표시 선택으로 Emacs를 시작합니다.

```bash
$ emacs
```

그래픽 세션에서는 그래픽 프레임을 만들 수 있습니다. Emacs를 현재 터미널 안에서 실행하려면 no window system의 줄임말인 `-nw`를 사용합니다.

```bash
$ emacs -nw
```

:::single-choice{#emacs-terminal-start}
그래픽 창 시스템 대신 현재 터미널 안에서 Emacs를 시작하는 명령어는 무엇인가요?

::option[`emacs -w`]{#emacs-window-option explanation="여기서 소개한 문서화된 no-window-system 형식이 아닙니다."}
::option[`emacs -nw`]{#emacs-no-window .correct explanation="`-nw` 옵션은 Emacs에 그래픽 창 시스템을 사용하지 않고 터미널에서 실행하라고 지시합니다."}
::option[`command -v emacs`]{#emacs-check-only explanation="명령 해석만 확인하며 편집기를 시작하지 않습니다."}
:::

## 파일 열기

Emacs를 시작할 때 파일을 방문하려면 경로를 전달합니다.

```bash
$ emacs notes.txt
```

파일이 존재하면 Emacs는 버퍼로 읽습니다. 파일이 없으면 해당 경로와 연결된 새 버퍼를 만들며 파일은 성공적으로 저장한 뒤에만 생성됩니다. 파일 시스템 권한은 여전히 쓰기 성공 여부를 결정합니다.

:::single-choice{#emacs-open-file-buffer}
`notes.txt`가 아직 존재하지 않을 때 `emacs notes.txt`는 일반적으로 무엇을 하나요?

::option[해당 경로와 연결된 새 버퍼를 엽니다.]{#emacs-new-file-buffer .correct explanation="버퍼에 `notes.txt`의 새 텍스트를 담을 수 있고 실제 파일은 저장할 때까지 만들어지지 않습니다."}
::option[편집기를 시작하기 전에 디스크에 파일을 만듭니다.]{#emacs-immediate-file explanation="Emacs는 저장에 성공할 때까지 디스크 파일을 만들지 않고 새 버퍼를 경로와 연결할 수 있습니다."}
::option[방문하는 모든 파일이 존재해야 하므로 시작을 거부합니다.]{#emacs-refuse-new-file explanation="Emacs는 없는 경로와 연결된 버퍼에서 새 파일을 작성할 수 있습니다."}
:::

## 버퍼, 창, 프레임 이해하기

Emacs는 서로 관련되어 있지만 구별되는 객체를 사용합니다.

- **버퍼**는 텍스트나 다른 편집기 상태를 보관합니다. 방문한 파일의 내용은 버퍼에 있습니다.
- **창**은 버퍼를 표시하는 Emacs 프레임 안의 영역입니다.
- **프레임**은 그래픽 프레임이나 터미널 프레임 같은 최상위 Emacs 표시입니다.

여러 버퍼가 보이지 않은 채 존재할 수 있고 두 창이 같은 버퍼를 표시할 수도 있습니다. 창을 닫는다고 반드시 버퍼가 종료되거나 파일이 삭제되지는 않습니다.

:::single-choice{#emacs-buffer-definition}
Emacs 버퍼란 무엇인가요?

::option[최상위 그래픽 애플리케이션 프레임입니다.]{#emacs-buffer-frame explanation="프레임은 최상위 표시 객체이며 버퍼는 편집기 내용이나 상태를 보관합니다."}
::option[편집 가능한 텍스트나 다른 편집기 상태를 보관하는 객체입니다.]{#emacs-buffer-content .correct explanation="방문한 파일 내용과 파일이 아닌 여러 보기가 Emacs 버퍼에 존재합니다."}
::option[이전 명령을 담은 쉘 기록 파일입니다.]{#emacs-buffer-history explanation="쉘 기록은 Emacs 버퍼 저장소와 별개입니다."}
:::

## Emacs 키 표기법 읽기

Emacs 문서는 간결한 표기법을 사용합니다.

- `C-x`: Control을 누른 채 `x` 누르기
- `M-x`: Meta를 누른 채 `x` 누르기. 현대 터미널과 데스크톱에서는 Alt가 흔히 Meta 역할을 합니다.
- `C-x C-f`: 키 시퀀스. Control+x를 누른 뒤 Control+f를 누릅니다.

사용하는 터미널이 일부 키를 가로채거나 다시 매핑할 수 있습니다. `Esc` 뒤에 키를 누르는 동작이 Meta 조합을 대신하는 경우가 많습니다.

:::single-choice{#emacs-key-sequence-notation}
`C-x C-f`로 표시된 Emacs 키 시퀀스는 어떻게 입력하나요?

::option[Control을 누른 채 `x`를 누르고, 다음으로 Control을 누른 채 `f`를 누릅니다.]{#emacs-control-x-f .correct explanation="각 `C-` 접두사는 뒤의 키에 적용되며 두 조합을 차례로 입력합니다."}
::option[버퍼에 문자 그대로 `C-x C-f`를 입력합니다.]{#emacs-literal-key-text explanation="표기법은 삽입할 텍스트가 아니라 Control 키 이벤트를 설명합니다."}
::option[Control, `x`, `f`를 하나의 조합으로 동시에 누릅니다.]{#emacs-simultaneous-x-f explanation="표기에는 하나의 세 키 조합이 아니라 연속된 두 조합이 있습니다."}
:::

## 내장 튜토리얼 시작하기

Emacs 안에서 `C-h t`를 입력하면 대화형 튜토리얼이 열립니다. 안전한 연습 버퍼에서 이동, 삽입, 저장, 종료를 가르칩니다. `C-h`는 도움말 접두사이며 `C-h C-h`는 도움말 사용법에 대한 도움말을 표시합니다.

Emacs가 메뉴나 시작 버퍼를 표시하더라도 중요한 파일에서 실험하는 것보다 튜토리얼이 더 체계적인 시작점입니다.

:::single-choice{#emacs-open-tutorial}
Emacs 내장 튜토리얼을 여는 키 시퀀스는 무엇인가요?

::option[`C-x C-s`]{#emacs-save-buffer explanation="현재 버퍼를 저장하며 튜토리얼을 열지 않습니다."}
::option[`C-x C-c`]{#emacs-exit-sequence explanation="레슨을 시작하는 대신 Emacs 종료를 시작합니다."}
::option[`C-h t`]{#emacs-help-tutorial .correct explanation="도움말 접두사 `C-h` 뒤에 `t`를 누르면 Emacs 튜토리얼이 시작됩니다."}
:::

## 요약

이제 Emacs를 시작하고 기초 인터페이스 개념을 해석할 수 있습니다.

1. `emacs` 명령을 사용할 수 있는지 확인할 수 있습니다.
2. `-nw`로 그래픽 또는 터미널 실행을 선택할 수 있습니다.
3. 기존 경로나 새 경로를 버퍼에서 방문할 수 있습니다.
4. 버퍼, 창, 프레임을 구분할 수 있습니다.
5. 키 표기법을 읽고 내장 튜토리얼을 열 수 있습니다.
