---
index: 18
lang: "ko"
title: "alias"
meta_title: "alias - 명령어 줄"
meta_description: "임시 alias 생성, .bashrc에 alias 저장, alias 목록 확인, unalias로 제거하는 방법을 예제로 배우는 Linux alias 명령어"
meta_keywords: "linux alias 명령어, alias 명령어, bash alias, .bashrc alias, unalias 명령어, 리눅스 명령어 단축키, 셸 alias"
---

## Lesson Content

길거나 반복적인 명령어를 입력하는 것은 지루할 수 있습니다. alias는 명령어나 명령어 시퀀스에 대해 사용자 정의 이름을 지정할 수 있는 셸 단축키입니다.

### 임시 Alias 만들기

현재 터미널 세션 동안만 지속되는 임시 alias를 만들려면 이름을 지정하고 명령어 문자열과 같게 설정하면 됩니다.

예를 들어, `ls -la`에 대해 `ll`이라는 alias를 만듭니다:

```bash
$ alias ll='ls -la'
```

이제 `ls -la` 대신 `ll`만 입력하면 동일한 명령어가 실행됩니다. 이는 셸을 간단하지만 강력하게 사용자화하는 방법입니다.

### Alias를 영구적으로 만들기

임시 alias는 터미널을 닫거나 시스템을 재부팅하면 사라집니다. `command alias in linux`를 영구적으로 만들려면 셸 설정 파일에 추가해야 합니다. Bash 셸의 경우 일반적으로 `~/.bashrc` 파일입니다.

1. 텍스트 편집기로 파일을 엽니다: `nano ~/.bashrc`
2. 명령줄에서 입력한 것처럼 alias 정의를 파일에 추가합니다:

```bash
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade'
```

3. 파일을 저장하고 편집기를 종료합니다.

변경 사항을 적용하려면 터미널을 닫았다가 다시 열거나 `source` 명령어로 설정 파일을 다시 불러와야 합니다:

```bash
$ source ~/.bashrc
```

이제 새 Bash 세션을 시작할 때마다 alias를 사용할 수 있습니다.

### Alias 제거하기

더 이상 alias가 필요 없으면 `unalias` 명령어로 현재 세션에서 제거할 수 있습니다.

```bash
$ unalias ll
```

영구 alias를 제거하려면 `~/.bashrc` 파일에서 해당 정의도 삭제해야 합니다.

### 기존 Alias 목록 보기

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

### 유용한 Alias 예제

```bash
$ alias la='ls -la'
$ alias ..='cd ..'
$ alias grep='grep --color=auto'
```

alias는 짧고 예측 가능하게 유지하세요. 파괴적인 명령어를 예상치 못한 동작으로 대체하는 것은 매우 확신이 있을 때만 피하세요.

### 자주 묻는 질문

**스크립트에서 alias가 작동하나요?** 보통 기본적으로는 아닙니다. 스크립트는 전체 명령어나 함수를 사용해야 합니다.

**Bash alias는 어디에 두어야 하나요?** 대화형 Bash 세션에서는 `~/.bashrc`에 두세요.

**alias가 실제 명령어와 충돌하면 어떻게 되나요?** 대화형 셸에서는 보통 alias가 우선합니다. alias를 우회하려면 `command name` 또는 `\name`을 사용하세요.

## Exercise

이 주제에 대한 특정 실습은 없지만, 관련 Linux 기술과 개념을 연습하기 위해 포괄적인 [Linux 학습 경로](https://labex.io/ko/learn/linux)를 탐색하는 것을 권장합니다.

## Quiz Question

alias를 생성하는 데 사용되는 명령어는 무엇인가요? 영어 소문자로 답해주세요.

## Quiz Answer

alias
