---
lesson_id: "the-shell"
course_id: "command-line"
lang: "ko"
order_index: 1
title: "쉘"
description: "리눅스 쉘의 역할과 명령어가 실행되는 방식을 배웁니다."
meta_title: "쉘 - 커맨드 라인"
meta_description: "리눅스 쉘이 무엇인지, Bash 프롬프트가 어떻게 작동하는지, 그리고 초보자 친화적인 커맨드 라인 예제로 첫 명령어를 실행하는 방법을 배워보세요."
meta_keywords: "리눅스 쉘, bash 쉘, 커맨드 라인, 리눅스 터미널, 쉘 프롬프트, echo 명령어, 기본 리눅스 명령어"
---

## 리눅스 쉘이란 무엇인가

리눅스 여정에 오신 것을 환영합니다! 첫 단계는 리눅스 쉘을 이해하는 것입니다. 쉘은 사용자가 입력한 명령어를 받아 운영체제에 실행을 요청한 뒤, 그 결과를 터미널에 출력하는 프로그램입니다.

그래픽 사용자 인터페이스를 사용해 봤다면 창, 메뉴, 버튼을 클릭하는 데 익숙할 것입니다. 커맨드 라인에서는 그 대신 정확한 명령어를 입력합니다. 보통 "Terminal", "Console", "Konsole"이라는 이름의 애플리케이션이 쉘 세션을 열어 줍니다.

터미널은 명령어를 입력하는 창이나 앱이고, 쉘은 그 안에서 실행되는 프로그램입니다.

쉘은 빠르고 스크립트로 자동화할 수 있으며 거의 모든 리눅스 시스템에서 사용할 수 있습니다. 명령어를 더 배우면 이를 조합해 파일을 살펴보고, 디렉터리를 관리하고, 텍스트를 검색하고, 소프트웨어를 설치하고, 반복 작업을 자동화할 수 있습니다.

:::single-choice{#distinguish-shell-and-terminal} 터미널과 쉘의 관계를 올바르게 설명한 것은 무엇인가요?

::option[터미널은 창을 제공하고 쉘은 그 안에서 실행됩니다.]{#shell-runs-in-terminal .correct explanation="터미널은 사용자가 다루는 인터페이스이고, 쉘은 그 안에서 명령어를 처리하는 프로그램입니다."}
::option[터미널은 명령어를 받고 쉘은 결과만 표시합니다.]{#terminal-accepts-commands explanation="두 역할을 반대로 설명했습니다. 터미널은 인터페이스를 제공하고 쉘이 명령어를 받아 실행합니다."}
::option[터미널과 쉘은 같은 프로그램을 가리키는 두 이름입니다.]{#terminal-equals-shell explanation="둘은 함께 작동하지만 같은 프로그램은 아닙니다. 터미널이 세션을 열면 그 안에서 쉘이 실행됩니다."}
:::

## Bash 쉘과 상호작용하기

이 과정에서는 Bourne Again Shell의 줄임말인 Bash를 중심으로 배웁니다. Bash는 가장 널리 쓰이는 리눅스 쉘 중 하나이며, 나중에 `zsh`, `fish` 또는 다른 쉘을 사용하더라도 탄탄한 기초가 됩니다.

터미널을 열면 쉘 프롬프트가 나타납니다. 모양은 시스템마다 다르지만 보통 사용자 이름, 호스트 이름, 현재 디렉터리를 보여 줍니다.

```plaintext
pete@icebox:/home/pete $
```

`$` 기호는 쉘이 일반 사용자의 입력을 받을 준비가 되었음을 뜻합니다. 명령어를 입력할 때 이 기호까지 입력하지는 않습니다. `#`가 보인다면 대개 더 큰 권한과 위험을 지닌 root 사용자로 작업하고 있다는 뜻입니다.

:::single-choice{#interpret-dollar-prompt} 예시 프롬프트 끝의 `$`는 무엇을 나타내나요?

::option[쉘이 root 사용자 권한으로 실행 중입니다.]{#root-user-ready explanation="root 프롬프트는 보통 `$`가 아니라 `#`로 끝납니다. root 권한에는 더 큰 힘과 위험이 따릅니다."}
::option[쉘이 일반 사용자의 입력을 기다리고 있습니다.]{#normal-user-ready .correct explanation="`$`는 일반 사용자 프롬프트이며 쉘이 명령어를 받을 준비가 되었음을 나타냅니다."}
::option[다음 명령어는 달러 기호로 시작해야 합니다.]{#type-dollar-first explanation="`$`는 프롬프트의 일부입니다. 이 기호를 복사하지 말고 그 뒤에 명령어만 입력합니다."}
:::

명령어는 흔히 다음 형태를 따릅니다.

```bash
command options arguments
```

예를 들어 `echo Hello World`에서 `echo`는 명령어이고 `Hello World`는 명령어에 전달되는 텍스트입니다.

:::single-choice{#identify-command-name} `echo Hello World`에서 명령어 이름은 어느 부분인가요?

::option[`Hello`]{#hello-command explanation="`Hello`는 명령어 이름 뒤에 있으므로 `echo`에 전달되는 텍스트의 일부입니다."}
::option[`World`]{#world-command explanation="`World` 역시 `echo`에 전달되는 텍스트이며 실행할 명령어의 이름이 아닙니다."}
::option[`echo`]{#echo-command .correct explanation="`echo`는 쉘이 실행할 프로그램의 이름입니다. 그 뒤의 단어는 해당 프로그램에 인자로 전달됩니다."}
:::

## 첫 번째 리눅스 명령어

초보자가 익힐 가장 기본적인 리눅스 명령어 중 하나인 `echo`부터 시작해 봅시다. 이 명령어는 사용자가 건넨 텍스트를 터미널에 출력합니다.

```bash
$ echo Hello World
Hello World
```

몇 가지 예제를 더 실행해 보세요.

```bash
$ echo Linux is fun
Linux is fun
$ echo "Hello from Bash"
Hello from Bash
```

쉘이 여러 단어를 하나의 텍스트 덩어리로 다루게 하려면 따옴표가 유용합니다.

:::single-choice{#group-words-with-quotes} 쉘이 `Hello from Bash`를 따옴표로 묶인 하나의 텍스트 덩어리로 처리하게 하는 명령어는 무엇인가요?

::option[`echo "Hello from Bash"`]{#quoted-words .correct explanation="따옴표가 세 단어를 하나의 인자로 묶어 `echo`에 전달합니다."}
::option[`echo Hello from Bash`]{#unquoted-words explanation="화면에는 같은 단어가 출력되지만, 따옴표가 없으므로 쉘은 각 단어를 별도의 인자로 처리합니다."}
::option[`"echo Hello from Bash"`]{#quoted-command explanation="전체 줄을 따옴표로 묶으면 쉘은 `echo`를 실행하는 대신 그 전체 문자열을 명령어 이름으로 찾습니다."}
:::

이 기술을 연습하려면 종합적인 [![Shell Learning Path](https://labex.io/cdn-cgi/image/width=200,height=200,quality=80,format=auto,onerror=redirect/https://file.labex.io/path/FaVTnI4iqZP0.png)Shell Learning Path](https://labex.io/ko/learn/shell)를 살펴보세요.

## 초보자를 위한 일반 팁

- 명령어를 실행하려면 `Enter` 키를 누릅니다.
- 이전 명령어를 불러오려면 `위쪽 화살표` 키를 누릅니다.
- 리눅스의 명령어와 파일 이름은 대소문자를 구분합니다.
- 공백은 중요합니다. `echo hello`와 `echohello`는 서로 다릅니다.
- 명령어가 멈춘 것 같다면 `Ctrl-C`로 취소할 수 있습니다.

## 요약

이제 쉘의 역할을 설명하고 기본 쉘 프롬프트를 사용할 수 있습니다.

1. 터미널과 쉘을 구분할 수 있습니다.
2. 명령 프롬프트를 알아볼 수 있습니다.
3. `echo`로 간단한 명령어를 실행할 수 있습니다.
