---
lesson_id: "alias-command"
course_id: "command-line"
lang: "ko"
order_index: 18
title: "alias"
description: "Bash에서 명령어 별칭을 만들고 확인하고 저장하고 우회하고 제거하는 방법을 배웁니다."
meta_title: "alias - 명령어 줄"
meta_description: "임시 alias 생성, .bashrc에 alias 저장, alias 목록 확인, unalias로 제거하는 방법을 예제로 배우는 Linux alias 명령어"
meta_keywords: "linux alias 명령어, alias 명령어, bash alias, .bashrc alias, unalias 명령어, 리눅스 명령어 단축키, 셸 alias"
---

별칭은 대화형 쉘이 명령줄을 실행하기 전에 한 명령어 단어를 다른 문자열로 바꾸게 합니다. 자주 쓰는 명령어를 줄이거나 선호하는 옵션 집합을 제공할 수 있습니다.

## 현재 쉘에 별칭 만들기

Bash에서는 `alias NAME='REPLACEMENT'` 형식으로 별칭을 정의하며 등호 주변에는 공백을 넣지 않습니다.

```bash
$ alias ll='ls -la'
```

이제 `ll`을 명령어로 입력하면 `ls -la`로 확장됩니다. 따옴표는 별칭을 정의하는 동안 치환 문자열을 하나로 묶습니다.

별칭은 간단한 명령어 접두사 치환에 적합합니다. 인자를 더 체계적으로 처리해야 할 때는 쉘 함수를 사용합니다.

:::single-choice{#define-ll-alias}
현재 쉘에서 `ll`을 `ls -la`의 별칭으로 정의하는 Bash 명령어는 무엇인가요?

::option[`alias ll = 'ls -la'`]{#alias-spaces explanation="`=` 주변의 공백이 정의를 별도 쉘 단어로 나누므로 Bash가 유효한 별칭 할당으로 받지 못합니다."}
::option[`alias ll='ls -la'`]{#alias-ll .correct explanation="필수 `NAME=REPLACEMENT` 형식을 사용하고 공백이 든 치환 문자열을 따옴표로 묶었습니다."}
::option[`unalias ll='ls -la'`]{#unalias-definition explanation="`unalias`는 기존 별칭 이름을 제거하며 치환 문자열을 만들지 않습니다."}
:::

## 이후 Bash 세션에 별칭 불러오기

임시 alias는 터미널을 닫거나 시스템을 재부팅하면 사라집니다. `command alias in linux`를 영구적으로 만들려면 셸 설정 파일에 추가해야 합니다. Bash 셸의 경우 일반적으로 `~/.bashrc` 파일입니다.

```bash
alias ll='ls -la'
```

변경 사항을 적용하려면 터미널을 닫았다가 다시 열거나 `source` 명령어로 설정 파일을 다시 불러와야 합니다:

```bash
$ source ~/.bashrc
```

쉘 시작 동작은 쉘, 로그인 모드와 배포판 설정에 따라 달라질 수 있습니다. 예를 들어 Zsh 사용자는 보통 Bash의 `.bashrc` 대신 Zsh 설정을 사용합니다.

:::single-choice{#persist-bash-alias}
이후 대화형 비로그인 Bash 세션이 개인 별칭을 불러오도록 보통 어디에 정의해야 하나요?

::option[사용자의 `~/.bashrc` 파일에 정의합니다.]{#bashrc-alias .correct explanation="대화형 비로그인 Bash는 보통 `~/.bashrc`를 읽으므로 개인 별칭을 두는 관례적인 위치입니다."}
::option[별칭 대상 명령어가 사용하는 실행 파일 안에 정의합니다.]{#edit-executable explanation="설치된 실행 파일 변경은 쉘 별칭 확장과 무관하며 패키지로 관리되는 시스템 파일을 손상할 수 있습니다."}
::option[현재 터미널의 스크롤백 기록에 정의합니다.]{#terminal-scrollback explanation="스크롤백은 표시된 텍스트만 기록하며 Bash는 이를 시작 설정으로 실행하지 않습니다."}
:::

## 별칭과 이름 해석 확인하기

인수 없이 `alias` 명령어를 실행하면 현재 셸의 alias 목록을 볼 수 있습니다.

```bash
$ alias
alias ll='ls -la'
alias grep='grep --color=auto'
```

`type` 명령어를 사용하면 명령어 입력 시 실행되는 내용을 확인할 수 있습니다:

```bash
$ type ll
ll is aliased to 'ls -la'
```

:::single-choice{#inspect-command-alias}
Bash가 현재 `ll`을 별칭, 함수, 내장 명령어 또는 실행 파일 중 무엇으로 해석하는지 보여 주는 명령어는 무엇인가요?

::option[`file ll`]{#file-ll explanation="`file`은 파일 시스템 경로를 분류하지만 별칭은 쉘 상태에 있어 `ll`이라는 파일과 무관할 수 있습니다."}
::option[`type ll`]{#type-ll .correct explanation="`type` 내장 명령어는 현재 Bash 세션이 `ll`이라는 이름을 해석하는 방식을 알려 줍니다."}
::option[`whatis ll`]{#whatis-ll explanation="`whatis`는 매뉴얼 페이지 설명을 조회하며 개인 별칭에는 보통 매뉴얼 데이터베이스 항목이 없습니다."}
:::

## 별칭 우회 및 제거하기

한 번의 명령줄에서 별칭을 우회하려면 명령어 이름 앞에 백슬래시를 붙이거나 Bash의 `command` 내장 명령어 뒤에 둡니다.

```bash
$ \ls
$ command ls
```

기본 명령어의 일반 동작이 필요할 때 유용합니다. 별칭은 짧고 예측 가능하게 유지하고 익숙한 이름 뒤에 의외이거나 파괴적인 동작을 숨기지 마세요.

:::single-choice{#bypass-ls-alias}
현재 Bash 세션에 `ls`라는 별칭이 있습니다. 한 번의 실행에서 이 별칭을 우회하는 명령어는 무엇인가요?

::option[`alias ls`]{#show-ls-alias explanation="`ls` 별칭의 정의를 출력할 뿐 기본 명령어를 실행하지 않습니다."}
::option[`command ls`]{#command-ls .correct explanation="`command`가 명령어 단어이므로 Bash는 뒤의 `ls`를 별칭으로 확장하지 않고 일반적인 명령어 해석을 수행합니다."}
::option[`source ls`]{#source-ls explanation="`source`는 파일을 현재 쉘의 코드로 읽으며 별칭을 우회하는 안전하거나 적절한 방법이 아닙니다."}
:::

현재 쉘에서 별칭을 제거하려면 `unalias`를 사용합니다.

```bash
$ unalias ll
```

정의가 `~/.bashrc`에 남아 있으면 이후 쉘에서 다시 만들어집니다. 영구히 없애려면 해당 설정 줄도 제거하거나 바꿉니다.

:::single-choice{#remove-current-alias}
현재 Bash 세션에서 `ll` 별칭을 제거하는 명령어는 무엇인가요?

::option[`unalias ll`]{#unalias-ll .correct explanation="`unalias`는 현재 쉘의 별칭 테이블에서 지정한 별칭을 삭제합니다."}
::option[`alias ll=''`]{#empty-ll explanation="정의를 제거하는 대신 별칭을 빈 문자열로 치환합니다."}
::option[`command ll`]{#command-ll explanation="해당 줄에서 별칭 확장을 우회할 수 있지만 쉘 상태에서 별칭을 삭제하지는 않습니다."}
:::

## 요약

이제 간단하고 확인 가능한 별칭으로 Bash를 사용자화할 수 있습니다.

1. 올바른 따옴표로 임시 별칭을 정의할 수 있습니다.
2. 이후 세션에서 `~/.bashrc`의 개인 별칭을 불러올 수 있습니다.
3. 별칭과 명령어 해석 방식을 확인할 수 있습니다.
4. 한 번의 실행에서 별칭을 우회할 수 있습니다.
5. 필요할 때 활성 정의와 저장된 정의를 모두 제거할 수 있습니다.
