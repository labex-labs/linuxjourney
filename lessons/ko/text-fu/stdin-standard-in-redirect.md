---
index: 2
lang: "ko"
title: "stdin (표준 입력)"
meta_title: "stdin (표준 입력) - Text-Fu"
meta_description: "Linux 에서 stdin(표준 입력) 리디렉션에 대해 알아보세요. '<' 연산자를 파일 및 명령과 함께 사용하는 방법을 이해하세요. 실제 예제를 탐색하고 Linux 명령줄 기술을 향상시키세요."
meta_keywords: "stdin, 표준 입력, Linux 리디렉션, < 연산자, Linux 튜토리얼, 명령줄, 초보자, 가이드"
---

## Lesson Content

이전 레슨에서 우리는 파일이나 화면과 같이 사용할 수 있는 다양한 stdout 스트림이 있다는 것을 배웠습니다. 마찬가지로 사용할 수 있는 다양한 표준 입력 (stdin) 스트림도 있습니다. 키보드와 같은 장치에서 stdin 을 얻는다는 것을 알고 있지만, 파일, 다른 프로세스의 출력, 그리고 터미널도 사용할 수 있습니다. 예를 들어 보겠습니다.

이 예제에서는 이전 레슨의 `peanuts.txt` 파일을 사용하겠습니다. 이 파일에는 "Hello World"라는 텍스트가 들어 있었습니다.

```bash
cat < peanuts.txt > banana.txt
```

stdout 리디렉션에 `>`를 사용했던 것처럼, stdin 리디렉션에는 `<`를 사용할 수 있습니다.

일반적으로 `cat` 명령에서는 파일을 보내면 그 파일이 stdin 이 됩니다. 이 경우, `peanuts.txt`를 stdin 으로 리디렉션했습니다. 그러면 `cat peanuts.txt`의 출력인 "Hello World"가 `banana.txt`라는 다른 파일로 리디렉션됩니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 에서 입출력 리디렉션에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 입력 및 출력 리디렉션](https://labex.io/ko/labs/comptia-redirecting-input-and-output-in-linux-590840)** - >, >>, 2> 및 tee 명령과 같은 연산자를 사용하여 표준 출력 (stdout), 표준 에러 (stderr) 및 표준 입력 (stdin) 을 조작하여 명령의 데이터 흐름을 제어하는 연습을 합니다.
2. **[데이터 스트림 리디렉션](https://labex.io/ko/labs/linux-data-stream-redirection-17995)** - Linux 스트림 리디렉션 기술을 배웁니다. 표준 입력, 출력 및 에러 스트림을 조작하고, 출력을 결합하며, 고급 파일 작업을 위해 /dev/null을 활용합니다.
3. **[시퀀스 제어 및 파이프라인](https://labex.io/ko/labs/linux-sequence-control-and-pipeline-17994)** - 명령 실행 시퀀스를 제어하고, 한 명령의 출력을 다른 명령의 입력으로 전달하는 데 필수적인 파이프라인을 활용하는 방법을 배웁니다.

이러한 랩은 실제 시나리오에서 입출력 리디렉션 개념을 적용하고 셸 스크립팅 및 데이터 조작에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

stdin 을 리디렉션하는 데 사용하는 리디렉터는 무엇입니까?

## Quiz Answer

<
