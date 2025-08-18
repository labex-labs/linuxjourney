---
index: 1
lang: "ko"
title: "stdout (표준 출력)"
meta_title: "stdout (표준 출력) - Text-Fu"
meta_description: "Linux stdout 및 I/O redirection 에 대해 알아보세요. > 및 >> 연산자를 사용하여 명령어 출력을 파일로 리디렉션하는 방법을 이해하세요. 오늘 Linux 여정을 시작하세요!"
meta_keywords: "Linux stdout, I/O redirection, Linux commands, redirect output, Linux tutorial, beginner Linux, Linux guide, shell scripting"
---

## Lesson Content

이제 우리는 많은 명령어와 그 출력에 익숙해졌고, 이것이 다음 주제인 I/O(입력/출력) 스트림으로 이어집니다. 다음 명령어를 실행해보고, 이것이 어떻게 작동하는지 논의해봅시다.

```bash
echo Hello World > peanuts.txt
```

무슨 일이 일어났을까요? 음, 명령어를 실행한 디렉토리를 확인해보세요. 그러면 `peanuts.txt`라는 파일이 보일 것입니다. 그 파일 안을 들여다보면 "Hello World"라는 텍스트가 보일 것입니다. 하나의 명령어로 많은 일이 일어났으니, 이를 분석해봅시다.

먼저, 첫 번째 부분을 분석해봅시다:

```bash
echo Hello World
```

우리는 이것이 화면에 "Hello World"를 출력한다는 것을 알고 있지만, 어떻게 그럴까요? 프로세스는 I/O 스트림을 사용하여 입력을 받고 출력을 반환합니다. 기본적으로 `echo` 명령어는 키보드에서 입력을 (표준 입력 또는 stdin) 받고 화면으로 출력을 (표준 출력 또는 stdout) 반환합니다. 그래서 쉘에서 `echo Hello World`를 입력하면 화면에 "Hello World"가 나타나는 것입니다. 그러나 I/O redirection 을 사용하면 이 기본 동작을 변경하여 파일 유연성을 높일 수 있습니다.

명령어의 다음 부분으로 진행해봅시다:

```bash
>
```

`>`는 표준 출력이 가는 곳을 변경할 수 있게 해주는 redirection operator 입니다. 이것은 `echo Hello World`의 출력을 화면 대신 파일로 보낼 수 있게 해줍니다. 파일이 아직 존재하지 않으면, 우리를 위해 파일을 생성합니다. 그러나 파일이 존재하면, 파일을 덮어씁니다 (사용하는 쉘에 따라 이를 방지하는 쉘 플래그를 추가할 수 있습니다).

그리고 이것이 기본적으로 stdout redirection 이 작동하는 방식입니다!

음, `peanuts.txt`를 덮어쓰고 싶지 않다고 가정해봅시다. 다행히도, 이를 위한 redirection operator 도 있습니다: `>>`.

```bash
echo Hello World >> peanuts.txt
```

이것은 `peanuts.txt` 파일의 끝에 "Hello World"를 추가할 것입니다. 파일이 아직 존재하지 않으면, `>` redirector 처럼 우리를 위해 파일을 생성할 것입니다!

## Exercise

몇 가지 명령어를 시도해보세요:

```bash
ls -l /var/log > myoutput.txt
echo Hello World > rm
> somefile.txt
```

## Quiz Question

파일에 출력을 추가 (append) 하려면 어떤 redirector 를 사용합니까?

## Quiz Answer

> >
