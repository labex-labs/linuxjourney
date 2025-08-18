---
index: 2
lang: "ko"
title: "stdin (표준 입력)"
meta_title: "stdin (표준 입력) - Text-Fu"
meta_description: "Linux 에서 stdin(표준 입력) 리디렉션에 대해 알아보세요. '<' 연산자를 파일 및 명령과 함께 사용하는 방법을 이해합니다. 실제 예제를 탐색하고 Linux 명령줄 기술을 향상시키세요."
meta_keywords: "stdin, 표준 입력, Linux 리디렉션, < 연산자, Linux 튜토리얼, 명령줄, 초보자, 가이드"
---

## Lesson Content

이전 강의에서 우리는 파일이나 화면과 같은 다양한 stdout 스트림을 사용할 수 있다는 것을 배웠습니다. 마찬가지로 다양한 표준 입력 (stdin) 스트림도 사용할 수 있습니다. 키보드와 같은 장치에서 stdin 을 사용한다는 것을 알고 있지만, 파일, 다른 프로세스의 출력, 터미널도 사용할 수 있습니다. 예를 들어 보겠습니다.

이 예제에서는 이전 강의의 `peanuts.txt` 파일을 사용해 보겠습니다. 이 파일에는 "Hello World"라는 텍스트가 들어 있었습니다.

```bash
cat < peanuts.txt > banana.txt
```

stdout 리디렉션에 `>`를 사용했던 것처럼, stdin 리디렉션에는 `<`를 사용할 수 있습니다.

일반적으로 `cat` 명령에서는 파일을 보내면 그 파일이 stdin 이 됩니다. 이 경우 `peanuts.txt`를 stdin 으로 리디렉션했습니다. 그러면 `cat peanuts.txt`의 출력인 "Hello World"가 `banana.txt`라는 다른 파일로 리디렉션됩니다.

## Exercise

몇 가지 명령을 시도해 보세요:

```bash
echo < peanuts.txt > banana.txt
ls < peanuts.txt > banana.txt
pwd < peanuts.txt > banana.txt
```

## Quiz Question

stdin 을 리디렉션하는 데 사용하는 리디렉터는 무엇입데까?

## Quiz Answer

<
