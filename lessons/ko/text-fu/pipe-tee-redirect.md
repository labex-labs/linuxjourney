---
index: 4
lang: "ko"
title: "파이프 및 tee"
meta_title: "파이프 및 tee - Text-Fu"
meta_description: "효율적인 명령줄 데이터 흐름을 위해 Linux 파이프 및 tee 명령을 배우세요. stdout, stdin 및 파일 출력을 이해하세요. Linux 기술을 향상시키세요!"
meta_keywords: "Linux 파이프, tee 명령, Linux 튜토리얼, stdout, stdin, 초보자 Linux, 명령줄, Linux 가이드"
---

## Lesson Content

이제 배관 작업을 좀 해볼까요? 실제 배관은 아니지만, 그런 종류의 작업입니다. 다음 명령을 시도해 봅시다:

```bash
ls -la /etc
```

매우 긴 항목 목록이 보일 것입니다. 사실 읽기가 좀 어렵습니다. 이 출력을 파일로 리디렉션하는 대신, `less`와 같은 다른 명령에서 출력을 볼 수 있다면 좋지 않을까요? 물론 가능합니다!

```bash
ls -la /etc | less
```

수직 막대로 표시되는 파이프 연산자 `|`는 한 명령의 `stdout`을 가져와서 다른 프로세스의 `stdin`으로 만들 수 있게 해줍니다. 이 경우, `ls -la /etc`의 `stdout`을 가져와서 `less` 명령으로 _파이프_했습니다. 파이프 명령은 매우 유용하며, 우리는 영원히 계속 사용할 것입니다.

그렇다면 명령의 출력을 두 개의 다른 스트림에 쓰고 싶다면 어떻게 해야 할까요? `tee` 명령으로 가능합니다:

```bash
ls | tee peanuts.txt
```

화면에 `ls`의 출력이 보일 것이고, `peanuts.txt` 파일을 열어보면 같은 정보가 보일 것입니다!

## Exercise

연습하면 완벽해집니다! 다음은 입출력 리디렉션 및 파이프라인에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 에서 입력 및 출력 리디렉션](https://labex.io/ko/labs/comptia-redirecting-input-and-output-in-linux-590840)** - `>`, `>>`, `2>`, 그리고 `tee` 명령과 같은 연산자를 사용하여 표준 출력 (stdout), 표준 오류 (stderr), 표준 입력 (stdin) 을 조작함으로써 명령의 데이터 흐름을 제어하는 ​​연습을 합니다.
2. **[시퀀스 제어 및 파이프라인](https://labex.io/ko/labs/linux-sequence-control-and-pipeline-17994)** - 명령 실행 시퀀스를 제어하고, 파이프라인을 활용하며, `cut`, `grep`, `wc`, `sort`, `uniq`와 같은 강력한 텍스트 처리 도구를 사용하는 방법을 배웁니다.
3. **[데이터 스트림 리디렉션](https://labex.io/ko/labs/linux-data-stream-redirection-17995)** - 표준 입력, 출력, 오류 스트림 조작, 출력 결합, `/dev/null` 활용을 포함한 Linux 스트림 리디렉션 기술을 배웁니다.

이 실습들은 파이핑 및 리디렉션 개념을 실제 시나리오에 적용하고 명령줄 데이터 조작에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

파이프 연산자를 나타내는 키는 무엇입니까?

## Quiz Answer

|
