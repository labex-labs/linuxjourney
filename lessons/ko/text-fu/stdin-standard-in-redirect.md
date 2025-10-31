---
index: 2
lang: "ko"
title: "표준 입력 (stdin)"
meta_title: "표준 입력 (stdin) - Text-Fu"
meta_description: "stdin(표준 입력) 리디렉션을 학습하여 Linux 명령줄 작업을 마스터하세요. 이 가이드는 stdin 과 stdout 의 관계, '<' 연산자 사용법, 그리고 'cat stdin'과 같은 실용적인 예제를 다루어 데이터 스트림을 효과적으로 관리하는 방법을 설명합니다."
meta_keywords: "stdin, 표준입력, stdin 리디렉션, cat stdin, stdin 과 stdout, 표준 입력, 리눅스 리디렉션, 명령줄, 입력 스트림"
---

## Lesson Content

이전 단원에서는 표준 출력 (stdout) 스트림 리디렉션에 대해 배웠습니다. 마찬가지로 표준 입력 (`stdin`) 스트림도 관리할 수 있습니다. 기본적으로 프로그램은 키보드로부터 `stdin`을 받지만, 파일이나 다른 프로세스의 출력을 입력 소스로 사용할 수도 있습니다.

### stdin 과 stdout 이해하기

리눅스의 모든 명령줄 프로세스는 최소한 두 가지 기본 데이터 스트림, 즉 표준 입력 (`stdin`) 과 표준 출력 (`stdout`) 을 가지고 작동합니다. 프로그램은 `stdin`에서 데이터를 읽고 결과를 `stdout`에 씁니다. 효과적인 명령줄 작업을 위해서는 `stdin과 stdout` 모두를 제어하는 방법을 이해하는 것이 중요합니다.

### stdin 리디렉션 방법

stdout 리디렉션을 위해 `>`를 사용하는 것처럼, `stdin`을 `리디렉션`하기 위해 `<` 연산자를 사용합니다. 이 강력한 기능을 사용하면 명령이 키보드 입력을 기다리는 대신 파일에서 입력을 읽도록 지시할 수 있습니다. 이것이 바로 입력 리디렉션의 핵심 개념입니다.

### cat stdin 을 사용한 실제 예제

이전 단원에서 "Hello World" 텍스트가 포함된 `peanuts.txt` 파일을 다시 살펴보겠습니다. 다음 명령을 고려해 보세요.

```bash
cat < peanuts.txt > banana.txt
```

여기서 일어나는 일에 대한 분석입니다.

1. `< peanuts.txt` 부분은 셸에게 `cat` 명령의 `stdin`을 `리디렉션`하여 키보드 대신 `peanuts.txt`에서 읽도록 지시합니다.
2. `cat` 명령은 입력을 처리합니다. 이 경우, `cat stdin`을 사용한다는 것은 `peanuts.txt`의 내용을 읽는다는 의미입니다.
3. `> banana.txt` 부분은 `cat`의 표준 출력을 `banana.txt`라는 새 파일로 리디렉션합니다.

결과적으로 `peanuts.txt`의 내용이 `banana.txt`로 복사됩니다. 이 예제는 단일하고 효율적인 명령으로 `stdin과 stdout`을 모두 관리하는 방법을 효과적으로 보여줍니다.

## Exercise

입력 및 출력 리디렉션에 대한 이해를 공고히 하기 위해 리눅스에서 표준 입력 및 출력 리디렉션에 중점을 둔 다음 실습을 시도해 보세요.

1. **[리눅스에서 입력 및 출력 리디렉션](https://labex.io/ko/labs/comptia-redirecting-input-and-output-in-linux-590840)** - >, >>, 2> 및 tee 명령과 같은 연산자를 사용하여 표준 출력 (stdout), 표준 오류 (stderr), 표준 입력 (stdin) 을 조작하여 명령의 데이터 흐름을 제어하는 연습을 합니다.
2. **[데이터 스트림 리디렉션](https://labex.io/ko/labs/linux-data-stream-redirection-17995)** - 리눅스 스트림 리디렉션 기술을 배웁니다. 표준 입력, 출력 및 오류 스트림을 조작하고, 출력을 결합하며, 고급 파일 작업을 위해 /dev/null을 활용합니다.
3. **[순서 제어 및 파이프라인](https://labex.io/ko/labs/linux-sequence-control-and-pipeline-17994)** - 명령 실행 순서를 제어하고 파이프라인을 활용하는 방법을 배웁니다. 파이프라인은 한 명령의 출력을 다른 명령의 입력으로 전달하는 데 기본이 됩니다.

이러한 실습은 실제 시나리오에서 입력 및 출력 리디렉션 개념을 적용하고 셸 스크립팅 및 데이터 조작에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

stdin 을 리디렉션하는 데 사용되는 연산자는 무엇입니까? 필요한 기호만으로 답하십시오.

## Quiz Answer

<
