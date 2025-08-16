---
lang: "ko"
title: "pipe 및 tee"
description: "효율적인 명령줄 데이터 흐름을 위해 Linux 파이프 및 tee 명령을 배우세요. stdout, stdin 및 파일 출력을 이해하세요. Linux 기술을 향상시키세요!"
keywords: "Linux pipe, tee command, Linux tutorial, stdout, stdin, beginner Linux, command line, Linux guide"
---

## Lesson Content

이제 배관 작업에 들어가 보겠습니다. 실제 배관은 아니지만, 그런 종류입니다. 다음 명령을 시도해 봅시다:

```bash
ls -la /etc
```

매우 긴 항목 목록이 보일 것입니다. 사실 읽기가 좀 어렵습니다. 이 출력을 파일로 리디렉션하는 대신, `less`와 같은 다른 명령에서 출력을 볼 수 있다면 좋지 않을까요? 네, 가능합니다!

```bash
ls -la /etc | less
```

수직 막대로 표시되는 파이프 연산자 `|`는 명령의 `stdout`을 가져와서 다른 프로세스의 `stdin`으로 만들 수 있게 해줍니다. 이 경우, `ls -la /etc`의 `stdout`을 가져와서 `less` 명령으로 *파이프*했습니다. 파이프 명령은 매우 유용하며, 우리는 영원히 계속 사용할 것입니다.

그렇다면 명령의 출력을 두 개의 다른 스트림에 쓰고 싶다면 어떻게 할까요? `tee` 명령으로 가능합니다:

```bash
ls | tee peanuts.txt
```

화면에 `ls`의 출력이 보일 것이고, `peanuts.txt` 파일을 열어보면 동일한 정보가 보일 것입니다!

## Exercise

다음 명령을 시도해 보세요:

```bash
ls | tee peanuts.txt banan.txt
```

## Quiz Question

파이프 연산자를 나타내는 키는 무엇입니까?

## Quiz Answer

|
