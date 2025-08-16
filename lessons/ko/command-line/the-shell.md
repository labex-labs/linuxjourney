---
lang: "ko"
title: "셸"
description: "Linux 셸, Bash, 그리고 'echo'와 같은 기본 명령에 대해 알아보세요. 셸 프롬프트를 이해하고 이 초보자 친화적인 가이드로 Linux 여정을 시작하세요."
keywords: "Linux 셸, Bash, echo 명령, Linux 튜토리얼, 명령줄, 초보자 Linux, 셸 프롬프트, Linux 가이드"
---

## Lesson Content

세상은 당신의 굴입니다. 아니, 셸이 당신의 굴입니다. 셸이란 무엇일까요? 셸은 기본적으로 키보드에서 명령을 받아 운영 체제로 보내 실행하는 프로그램입니다. GUI 를 사용해 본 적이 있다면 "터미널" 또는 "콘솔"과 같은 프로그램을 보셨을 것입니다. 이것들은 셸을 실행하는 프로그램일 뿐입니다. 이 전체 과정을 통해 우리는 셸의 경이로움에 대해 배울 것입니다.

이 과정에서는 Bash (Bourne Again Shell) 셸 프로그램을 사용할 것입니다. 거의 모든 Linux 배포판은 기본적으로 Bash 셸을 사용합니다. `ksh`, `zsh`, `tsch`와 같은 다른 셸도 있지만, 이 과정에서는 다루지 않을 것입니다.

바로 시작해 봅시다! 배포판에 따라 셸 프롬프트가 달라질 수 있지만, 대부분 다음 형식을 따릅니다:

```plaintext
username@hostname:current_directory
pete@icebox:/home/pete $
```

프롬프트 끝에 있는 `$`가 보이시나요? 셸마다 다른 프롬프트를 가집니다. 우리의 경우, `$`는 Bash, Bourne 또는 Korn 셸을 사용하는 일반 사용자를 위한 것입니다. 명령을 입력할 때 프롬프트 기호를 추가하지 않습니다. 그냥 거기에 있다는 것만 알아두세요.

간단한 명령인 `echo`부터 시작해 봅시다. `echo` 명령은 단순히 텍스트 인수를 화면에 출력합니다.

```bash
echo Hello World
```

## Exercise

다른 Linux 명령들을 시도해보고 어떤 출력을 내는지 확인해보세요:

1. `$ date`
2. `$ whoami`

## Quiz Question

`echo Hello World`를 입력했을 때 화면에 무엇이 출력되어야 할까요?

## Quiz Answer

Hello World
