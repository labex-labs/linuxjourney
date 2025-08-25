---
index: 3
lang: "ko"
title: "stderr(표준 오류)"
meta_title: "stderr(표준 오류) - Text-Fu"
meta_description: "Linux stderr(표준 오류) 리디렉션에 대해 알아보세요. Bash 에서 오류 처리를 위해 2>, 2>&1, &> 및 /dev/null을 이해하세요. Linux 명령줄 기술을 향상시키세요!"
meta_keywords: "Linux stderr, 표준 오류, 2> 리디렉션, 2>&1, &> 리디렉션, /dev/null, Bash 오류 처리, Linux 튜토리얼, 초보자 Linux"
---

## Lesson Content

이제 조금 다른 것을 시도해 봅시다. 시스템에 존재하지 않는 디렉터리의 내용을 나열하고 출력을 다시 `peanuts.txt` 파일로 리디렉션해 봅시다.

```bash
ls /fake/directory > peanuts.txt
```

다음과 같은 내용이 표시되어야 합니다:

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

이제 여러분은 아마도 그 메시지가 파일로 전송되었어야 하는 것 아니냐고 생각할 것입니다. 여기에는 표준 오류 (stderr) 라고 불리는 또 다른 I/O 스트림이 있습니다. 기본적으로 stderr 도 출력을 화면으로 보냅니다. 이것은 stdout 과는 완전히 다른 스트림입니다. 따라서 출력을 다른 방식으로 리디렉션해야 합니다.

안타깝게도 리디렉터는 `<` 또는 `>`를 사용하는 것만큼 좋지는 않지만 상당히 비슷합니다. 파일 디스크립터를 사용해야 합니다. 파일 디스크립터는 파일 또는 스트림에 액세스하는 데 사용되는 음수가 아닌 숫자입니다. 이에 대해서는 나중에 자세히 다루겠지만, 지금은 stdin, stdout, stderr 의 파일 디스크립터가 각각 0, 1, 2 라는 것을 알아두십시오.

이제 stderr 를 파일로 리디렉션하려면 다음과 같이 할 수 있습니다:

```bash
ls /fake/directory 2> peanuts.txt
```

`peanuts.txt` 파일에 stderr 메시지만 표시되어야 합니다.

이제 `peanuts.txt` 파일에 stderr 와 stdout 을 모두 보고 싶다면 어떻게 해야 할까요? 파일 디스크립터를 사용해서도 가능합니다:

```bash
ls /fake/directory > peanuts.txt 2>&1
```

이것은 `ls /fake/directory`의 결과를 `peanuts.txt` 파일로 보내고, `2>&1`을 통해 stderr 를 stdout 으로 리디렉션합니다. 여기서 작업 순서가 중요합니다. `2>&1`은 stderr 를 stdout 이 가리키는 곳으로 보냅니다. 이 경우 stdout 은 파일을 가리키고 있으므로 `2>&1`도 stderr 를 파일로 보냅니다. 따라서 `peanuts.txt` 파일을 열면 stderr 와 stdout 을 모두 볼 수 있습니다. 우리의 경우, 위 명령은 stderr 만 출력합니다.

stdout 과 stderr 를 모두 파일로 리디렉션하는 더 짧은 방법이 있습니다:

```bash
ls /fake/directory &> peanuts.txt
```

이제 그런 잡동사니를 원하지 않고 stderr 메시지를 완전히 없애고 싶다면 어떻게 해야 할까요? 음, `/dev/null`이라는 특수 파일로 출력을 리디렉션할 수도 있으며, 이는 모든 입력을 버립니다.

```bash
ls /fake/directory 2> /dev/null
```

## Exercise

연습이 완벽을 만듭니다! 다음은 입출력 리디렉션에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 에서 입력 및 출력 리디렉션](https://labex.io/ko/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 이 실습에서는 Linux 셸에서 입력 및 출력을 리디렉션하는 방법을 배웁니다. >, >>, 2> 및 tee 명령과 같은 연산자를 사용하여 표준 출력 (stdout), 표준 오류 (stderr) 및 표준 입력 (stdin) 을 조작하여 명령의 데이터 흐름을 제어하는 ​​연습을 합니다.

이 실습은 실제 시나리오에서 I/O 리디렉션 개념을 적용하고 Linux 에서 데이터 스트림을 관리하는 데 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

stderr 의 리디렉터는 무엇입니까?

## Quiz Answer

2>
