---
index: 1
lang: "ko"
title: "stdout (표준 출력)"
meta_title: "stdout (표준 출력) - Text-Fu"
meta_description: "Linux stdout 및 I/O 리디렉션에 대해 알아보세요. > 및 >> 연산자를 사용하여 명령어 출력을 파일로 리디렉션하는 방법을 이해하세요. 오늘 Linux 여정을 시작하세요!"
meta_keywords: "Linux stdout, I/O 리디렉션, Linux 명령어, 출력 리디렉션, Linux 튜토리얼, 초보자 Linux, Linux 가이드, 셸 스크립팅"
---

## Lesson Content

이제 우리는 많은 명령어와 그 출력에 익숙해졌으며, 이것이 다음 주제인 I/O(입력/출력) 스트림으로 이어집니다. 다음 명령어를 실행하고 이것이 어떻게 작동하는지 논의해 봅시다.

```bash
echo Hello World > peanuts.txt
```

무슨 일이 일어났을까요? 음, 명령어를 실행한 디렉토리를 확인해 보면 `peanuts.txt`라는 파일이 보일 것입니다. 그 파일 안을 들여다보면 "Hello World"라는 텍스트가 보일 것입니다. 하나의 명령어로 많은 일이 일어났으니, 하나씩 분석해 봅시다.

먼저, 첫 번째 부분을 분석해 봅시다:

```bash
echo Hello World
```

이것이 화면에 "Hello World"를 출력한다는 것을 알고 있지만, 어떻게 그럴까요? 프로세스는 I/O 스트림을 사용하여 입력을 받고 출력을 반환합니다. 기본적으로 `echo` 명령어는 키보드에서 입력 (표준 입력 또는 stdin) 을 받고 화면으로 출력 (표준 출력 또는 stdout) 을 반환합니다. 그래서 셸에서 `echo Hello World`를 입력하면 화면에 "Hello World"가 나타나는 것입니다. 하지만 I/O 리디렉션을 사용하면 이 기본 동작을 변경하여 파일 유연성을 높일 수 있습니다.

명령어의 다음 부분으로 진행해 봅시다:

```bash
>
```

`>`는 표준 출력이 어디로 갈지 변경할 수 있게 해주는 리디렉션 연산자입니다. 이것은 `echo Hello World`의 출력을 화면 대신 파일로 보낼 수 있게 해줍니다. 파일이 아직 존재하지 않으면 파일을 생성해 줍니다. 하지만 파일이 이미 존재하면 덮어씁니다 (사용하는 셸에 따라 이를 방지하기 위한 셸 플래그를 추가할 수 있습니다).

그리고 이것이 기본적으로 stdout 리디렉션이 작동하는 방식입니다!

음, `peanuts.txt`를 덮어쓰고 싶지 않다고 가정해 봅시다. 다행히도 이를 위한 리디렉션 연산자도 있습니다: `>>`.

```bash
echo Hello World >> peanuts.txt
```

이것은 `peanuts.txt` 파일의 끝에 "Hello World"를 추가할 것입니다. 파일이 아직 존재하지 않으면 `>` 리디렉터처럼 파일을 생성해 줍니다!

## Exercise

연습이 완벽을 만듭니다! 다음은 I/O 리디렉션에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 에서 입력 및 출력 리디렉션](https://labex.io/ko/labs/comptia-redirecting-input-and-output-in-linux-590840)** - `>`, `>>`, `2>` 및 `tee` 명령어와 같은 연산자를 사용하여 표준 출력 (stdout), 표준 오류 (stderr) 및 표준 입력 (stdin) 을 조작하여 명령어에서 데이터 흐름을 제어하는 ​​연습을 하세요.

이 실습은 실제 시나리오에서 개념을 적용하고 I/O 리디렉션에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

출력을 파일에 추가하는 데 사용하는 리디렉터는 무엇입요?

## Quiz Answer

> >