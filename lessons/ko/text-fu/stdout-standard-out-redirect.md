---
lesson_id: "stdout-standard-out-redirect"
course_id: "text-fu"
lang: "ko"
order_index: 1
title: "표준 출력 (stdout)"
description: "표준 출력이 터미널로 흐르는 방식과 Bash에서 이를 파일로 리디렉션하는 방법을 배웁니다."
meta_title: "표준 출력 (stdout) - Text-Fu"
meta_description: "표준 출력 (stdout) 과 I/O 리디렉션을 마스터하여 리눅스 학습을 시작하세요. 이 강의에서는 > 및 >> 연산자를 사용하여 명령 출력을 파일로 리디렉션하는 방법을 다루며, 이는 모든 리눅스 사용자에게 필수적인 기술입니다."
meta_keywords: "리눅스, 리눅스 학습, stdout, I/O 리디렉션, 표준 출력, 출력 리디렉션, bash, 셸 스크립팅, 리눅스 명령어, 리눅스 튜토리얼"
---

프로그램은 입력/출력 스트림을 통해 통신합니다. **stdout**으로 줄여 쓰는 표준 출력은 프로그램이 보통 정상적인 결과를 내보내는 스트림입니다. 터미널에서 쉘은 처음에 이 스트림을 터미널 화면에 연결합니다.

## 표준 출력에 쓰기

`echo` 명령어는 인자를 stdout에 씁니다.

```bash
$ echo Hello World
Hello World
```

stdout은 파일 디스크립터 `1`이며 여러 스트림을 리디렉션할 때 이 번호가 유용합니다. 프로그램에는 표준 입력(stdin)과 표준 오류(stderr)도 있으며 다음 강의에서 살펴봅니다.

:::single-choice{#stdout-default-destination}
리디렉션이 없을 때 대화형 터미널에서 `echo Hello World`는 정상 출력을 보통 어디로 보내나요?

::option[현재 디렉터리의 `stdout`이라는 파일]{#stdout-file explanation="표준 출력은 자동으로 생성되는 `stdout` 파일이 아니라 스트림이며 파일은 명시적으로 리디렉션할 때만 사용합니다."}
::option[표준 출력을 통해 터미널로 보냅니다.]{#stdout-terminal .correct explanation="쉘은 보통 명령어의 stdout을 터미널에 연결하므로 `echo` 결과가 화면에 표시됩니다."}
::option[명령어의 표준 입력 스트림]{#stdout-to-stdin explanation="표준 입력은 프로그램 안으로 데이터를 전달하고 `echo`의 정상 결과는 stdout으로 나갑니다."}
:::

## >로 파일 교체하기

Bash는 `>`를 출력 리디렉션 연산자로 해석합니다. 목적지 파일을 열고 명령어의 stdout을 그 파일에 연결합니다.

```bash
$ echo Hello World > peanuts.txt
```

이제 stdout이 `peanuts.txt`로 가므로 터미널에 텍스트가 나오지 않습니다. 파일이 없으면 만들고, 있으면 명령어가 쓰기 전에 내용을 잘라내므로 이전 내용이 사라집니다.

결과는 `cat`으로 확인합니다.

```bash
$ cat peanuts.txt
Hello World
```

:::single-choice{#stdout-replace-file}
`notes.txt`에 이미 텍스트가 있습니다. `echo new > notes.txt`를 실행하면 어떻게 되나요?

::option[파일 내용을 `new`로 교체합니다.]{#stdout-replace-existing .correct explanation="쉘은 `>` 목적지의 기존 내용을 잘라낸 뒤 비워진 파일로 `echo` 출력을 보냅니다."}
::option[기존 텍스트 뒤에 `new`를 추가합니다.]{#stdout-add-existing explanation="추가에는 `>>`가 필요하며 `>` 하나는 목적지의 이전 내용을 보존하지 않습니다."}
::option[파일을 바꾸지 않고 `new`를 표시합니다.]{#stdout-display-only explanation="리디렉션이 stdout을 `notes.txt`로 보내므로 정상 출력은 터미널에 남지 않습니다."}
:::

쉘은 명령어를 실행하기 전에 목적지를 열므로 Enter를 누르기 전에 경로를 확인하세요. 철자가 틀렸거나 의도하지 않은 기존 파일은 명령어가 나중에 실패해도 비워질 수 있습니다.

## >>로 파일에 추가하기

파일 내용을 지우지 않고 파일에 내용을 추가하고 싶다면 어떻게 해야 할까요? 이를 위해 `>>` 연산자를 사용합니다.

```bash
$ echo Another line >> peanuts.txt
$ cat peanuts.txt
Hello World
Another line
```

`>`와 마찬가지로 `>>`도 목적지가 없으면 만듭니다. 차이는 기존 파일을 여는 방식으로, `>>`는 잘라내지 않고 뒤에 추가합니다.

:::single-choice{#stdout-append-file}
기존 내용을 지우지 않고 `status.log` 끝에 `Finished`를 추가하는 명령어는 무엇인가요?

::option[`echo Finished > status.log`]{#stdout-truncate-status explanation="`>` 하나는 쓰기 전에 기존 목적지를 잘라내므로 이전 로그 내용이 사라집니다."}
::option[`echo Finished >> status.log`]{#stdout-append-status .correct explanation="`echo`가 텍스트를 만들고 `>>`가 stdout을 목적지 파일 뒤에 추가합니다."}
::option[`cat Finished >> status.log`]{#stdout-cat-filename explanation="`Finished`라는 파일을 읽으라고 `cat`에 요청할 뿐 필요한 텍스트를 stdout으로 만들지 않습니다."}
:::

## 리디렉션은 쉘의 기능

쉘은 `>`와 `>>`를 인식해 프로그램에 전달할 인자에서 제거하고, 파일을 열고, 스트림을 연결합니다. 명령어 자체는 평소처럼 stdout에 쓸 뿐입니다.

따라서 같은 리디렉션 구문을 여러 명령어에 사용할 수 있습니다.

```bash
$ pwd > current-directory.txt
$ ls -la >> directory-list.txt
```

:::single-choice{#stdout-shell-role}
`pwd > current-directory.txt`에서 `>`를 보통 누가 해석하나요?

::option[`>`를 인자로 받은 `pwd` 명령어]{#stdout-pwd-redirection explanation="쉘이 리디렉션 구문을 소비하므로 `pwd`는 보통 `>`나 목적지를 일반 인자로 받지 않습니다."}
::option[`pwd`를 시작하기 전의 Bash 쉘]{#stdout-bash-redirection .correct explanation="Bash는 명령어를 실행하기 전에 목적지를 열고 파일 디스크립터 1을 연결합니다."}
::option[`pwd`가 화면에 경로를 출력한 뒤의 터미널]{#stdout-terminal-redirection explanation="출력이 쓰이기 전에 스트림이 리디렉션되므로 터미널은 해당 stdout을 처음부터 받지 않습니다."}
:::

표준 스트림 리디렉션은 다음 실습에서 연습해 보세요.

1. **[Linux 에서 입력 및 출력 리디렉션](https://labex.io/ko/labs/comptia-redirecting-input-and-output-in-linux-590840)** - `>`, `>>`, `2>`와 같은 연산자와 `tee` 명령어를 사용하여 표준 출력 (stdout), 표준 오류 (stderr), 표준 입력 (stdin) 을 조작하여 명령어 데이터 흐름을 제어하는 연습을 합니다.

## 요약

이제 교체와 추가 동작을 혼동하지 않고 명령어의 표준 출력을 리디렉션할 수 있습니다.

1. stdout이 정상적인 명령 결과를 위한 스트림임을 알 수 있습니다.
2. `>`로 파일 내용을 교체할 수 있습니다.
3. 기존 내용을 보존하며 `>>`로 추가할 수 있습니다.
4. 쉘이 열기 전에 목적지를 확인할 수 있습니다.
