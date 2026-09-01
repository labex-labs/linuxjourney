---
lesson_id: "text-editors-vim-or-emacs"
course_id: "advanced-text-fu"
lang: "ko"
order_index: 2
title: "텍스트 편집기"
description: "Linux 관리와 개발을 위한 터미널 텍스트 편집기를 선택하고 구성하는 방법을 배웁니다."
meta_title: "텍스트 편집기 - Advanced Text-Fu"
meta_description: "Vim과 Emacs 같은 Linux 텍스트 편집기를 알아봅니다. 시스템 탐색에서 편집기의 용도와 중요성을 배우고 Linux 텍스트 편집기 여정을 시작하세요."
meta_keywords: "Linux 텍스트 편집기, Vim, Emacs, Linux 명령어, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

Linux 구성, 스크립트, 소스 코드, 로그는 일반 텍스트로 저장되는 경우가 많습니다. 터미널 편집기를 사용하면 로컬 터미널, 원격 SSH 세션 또는 그래픽 데스크톱이 없는 환경에서 이러한 파일을 다룰 수 있습니다.

## 환경에 맞는 편집기 선택하기

모든 사람이나 작업에 가장 좋은 편집기 하나는 없습니다. 그래픽 편집기, 터미널 편집기, 통합 개발 환경 모두 상황에 따라 적합할 수 있습니다. 명령줄 작업에는 설치되어 있고 안전하게 종료할 수 있으며 기본 편집 방식을 이해하는 편집기를 선택하세요.

Vim이나 Emacs가 설치되어 있다고 가정하지 마세요. 현재 쉘에서 명령 해석을 확인합니다.

```bash
$ command -v vim
/usr/bin/vim
$ command -v emacs
/usr/bin/emacs
```

결과가 비어 있고 종료 상태가 0이 아니면 현재 명령 검색을 통해 그 이름을 찾지 못했다는 뜻입니다. 최소 시스템에는 `vi`만 있을 수 있고 다른 시스템에는 Nano가 포함되거나 대화형 편집기가 전혀 없을 수도 있습니다.

:::single-choice{#editors-check-availability} 현재 쉘이 `vim`이라는 실행 파일을 해석할 수 있는지 확인하는 명령어는 무엇인가요?

::option[`vim --install`]{#editors-vim-install explanation="Vim은 이 명령을 이식 가능한 설치 확인으로 사용하지 않으며 패키지 설치 방식은 배포판마다 다릅니다."}
::option[`file ~/.vimrc`]{#editors-file-vimrc explanation="존재한다면 구성 경로 하나를 분류할 뿐 `vim`을 해석할 수 있는지는 확인하지 않습니다."}
::option[`command -v vim`]{#editors-command-v-vim .correct explanation="쉘 내장 명령이 명령 해석을 확인하고 사용할 수 있으면 해석된 형태를 출력합니다."}
:::

## Vim의 모델 이해하기

Vim은 모달 편집기입니다. 현재 모드에 따라 같은 키가 다른 의미를 가질 수 있습니다.

- 일반 모드는 키를 탐색 및 편집 명령으로 해석합니다.
- 입력 모드는 입력한 텍스트를 삽입합니다.
- 명령줄 모드는 저장이나 종료 같은 명령을 받습니다.

연습하면 반복적인 키보드 편집을 효율적으로 할 수 있지만 초보자는 활성 모드를 계속 파악해야 합니다. 뒤의 레슨에서 Vim 작업을 하나씩 소개합니다.

:::single-choice{#editors-vim-modal-meaning} Vim이 모달이라는 것은 무엇을 의미하나요?

::option[모든 파일이 별도의 그래픽 창에서 열립니다.]{#editors-vim-windows explanation="창과 버퍼는 별도의 개념입니다. 모달은 편집기 상태에 따라 키 동작이 바뀌는 방식을 뜻합니다."}
::option[Vim은 한 번에 한 종류의 텍스트 파일만 편집할 수 있습니다.]{#editors-vim-file-type explanation="Vim은 다양한 파일 형식을 지원합니다. 모달은 파일 제한이 아니라 상호작용 모델을 설명합니다."}
::option[활성 모드에 따라 키가 다른 동작을 수행합니다.]{#editors-vim-modes .correct explanation="예를 들어 같은 키가 일반 모드에서는 명령을 실행하지만 입력 모드에서는 텍스트를 삽입할 수 있습니다."}
:::

## Emacs의 모델 이해하기

Emacs는 확장 가능한 환경 안에서 주로 키 조합과 이름이 지정된 명령을 사용합니다. 파일은 버퍼에서 방문하며 주 모드와 부 모드가 서로 다른 내용과 작업에 맞춰 동작을 구성합니다. Emacs는 터미널이나 그래픽 프레임에서 실행할 수 있습니다.

Vim과 Emacs 모두 구성과 확장을 통해 기본 편집보다 훨씬 많은 기능을 지원합니다. 사용자 지정을 추가하기 전에 일반 텍스트 파일을 열고 수정하고 저장하고 닫는 것부터 시작하세요.

:::single-choice{#editors-emacs-buffer} Emacs 용어에서 방문한 파일의 편집 가능한 텍스트는 일반적으로 어디에 보관되나요?

::option[버퍼에 보관됩니다.]{#editors-emacs-buffer-answer .correct explanation="Emacs는 파일을 버퍼에서 방문하며 버퍼가 보고 편집하는 텍스트를 담습니다."}
::option[쉘의 별칭 테이블에 보관됩니다.]{#editors-emacs-alias-table explanation="별칭은 쉘 명령 해석에 속하며 편집기 텍스트를 저장하지 않습니다."}
::option[터미널 스크롤백에만 보관됩니다.]{#editors-emacs-scrollback explanation="터미널 스크롤백은 표시된 출력을 기록하지만 Emacs는 편집 가능한 텍스트를 버퍼에서 관리합니다."}
:::

## 선호 편집기 설정하기

많은 명령줄 프로그램은 편집기를 시작해야 할 때 `VISUAL`이나 `EDITOR`를 확인합니다. 예를 들어 현재 Bash 세션과 그 자식에서 실행하는 명령에 Vim을 선택합니다.

```bash
$ export VISUAL=vim
$ export EDITOR="$VISUAL"
```

이 변수들은 선호를 표현할 뿐 프로그램을 설치하지 않습니다. 실제로 존재하는 명령을 사용하고 테스트한 뒤에만 알맞은 쉘 시작 파일에 export 줄을 넣으세요.

:::single-choice{#editors-editor-variable} `export EDITOR=vim`은 무엇을 하나요?

::option[이후 자식 프로세스에 `vim`이 선호 편집기 값이라고 알립니다.]{#editors-export-preference .correct explanation="export는 현재 쉘에서 시작한 명령이 상속하는 환경에 선호 값을 넣습니다."}
::option[시스템의 모든 사용자를 위해 Vim을 설치합니다.]{#editors-install-vim explanation="환경 변수 할당은 패키지를 설치하거나 다른 사용자의 시스템을 바꾸지 않습니다."}
::option[모든 프로그램이 Vim 키 바인딩을 따르게 합니다.]{#editors-global-bindings explanation="프로그램이 변수를 확인해 편집기를 시작할 수는 있지만 자체 상호작용 모델을 대체하지는 않습니다."}
:::

## 중요한 파일을 위험에 빠뜨리지 않고 연습하기

자신이 소유한 디렉터리의 일회용 파일로 연습합니다.

```bash
$ printf 'first line\nsecond line\n' > editor-practice.txt
$ vim editor-practice.txt
```

시스템 구성이나 다른 사용자의 데이터로 시작하지 마세요. 중요한 파일을 바꾸기 전에 백업을 만들고 저장 및 종료 방법을 이해한 뒤 `cat`이나 `diff` 같은 읽기 전용 명령으로 결과를 검토하세요.

:::single-choice{#editors-first-practice-file} 익숙하지 않은 편집기를 처음 연습할 때 가장 안전한 파일은 무엇인가요?

::option[root 권한으로 연 중요한 부팅 구성 파일입니다.]{#editors-boot-file explanation="실수로 바꾸면 정상 시작을 막을 수 있고 높은 권한은 실수의 영향을 키웁니다."}
::option[자신이 소유한 디렉터리의 일회용 텍스트 파일입니다.]{#editors-disposable-file .correct explanation="연습 파일은 탐색, 저장, 종료를 배우는 동안 실수로 편집해도 결과를 제한합니다."}
::option[백업이 없는 공유 운영 파일입니다.]{#editors-production-file explanation="공유 데이터를 검토 없이 연습용으로 사용하면 다른 사람의 작업을 방해하고 간단한 복구 방법도 없습니다."}
:::

터미널 텍스트 파일 열기, 편집, 저장을 연습하려면 다음 실습을 진행해 보세요.

1. **[Vim과 Nano로 Linux 텍스트 파일 편집하기](https://labex.io/ko/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - vi/vim과 nano로 파일 생성, 텍스트 편집, 파일 저장, 탐색을 연습합니다.

## 요약

이제 터미널 편집기를 선택하고 안전한 연습 작업 흐름을 준비할 수 있습니다.

1. 편집기 명령을 사용할 수 있는지 확인할 수 있습니다.
2. Vim의 모달 상호작용 모델을 이해할 수 있습니다.
3. Emacs의 버퍼와 확장 가능한 모드를 이해할 수 있습니다.
4. 설치와 혼동하지 않고 편집기 선호를 설정할 수 있습니다.
5. 중요한 파일을 편집하기 전에 일회용 텍스트로 연습할 수 있습니다.
