---
index: 3
lang: "ko"
title: "stderr (표준 오류)"
meta_title: "stderr (표준 오류) - Text-Fu"
meta_description: "Linux 에서 표준 오류를 관리하는 방법을 알아보세요. 이 가이드는 stderr 리디렉션, stderr 파일 디스크립터 (2), 그리고 2>, 2>&1, &>를 사용하여 stderr 를 파일이나 /dev/null로 리디렉션하는 방법을 다룹니다."
meta_keywords: "stderr, 표준 오류 리눅스, stderr 파일 디스크립터, stderr 파일, 리눅스 표준 오류, stderr 리디렉션, 2>, 2>&1, &>, /dev/null, bash 오류 처리"
---

## Lesson Content

명령이 오류를 생성할 때 어떤 일이 발생하는지 살펴보겠습니다. 존재하지 않는 디렉터리의 내용을 나열하고 출력을 `peanuts.txt`라는 파일로 리디렉션해 보세요.

```bash
ls /fake/directory > peanuts.txt
```

깔끔한 프롬프트 대신 화면에 오류 메시지가 표시됩니다.

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

이 메시지가 파일로 전송되지 않은 이유가 궁금할 수 있습니다. 이는 **표준 오류 (standard error)**, 즉 **stderr**라는 또 다른 I/O 스트림이 작용하기 때문입니다.

### Linux 에서 표준 오류 (Standard Error) 란 무엇인가요?

Linux 에서 `stderr`는 프로그램이 오류 메시지와 진단 정보를 보내는 데 사용하는 기본 출력 스트림입니다. 이는 일반적인 프로그램 출력을 위해 사용되는 표준 출력 (`stdout`) 스트림과는 완전히 분리되어 있습니다. 기본적으로 `stdout`과 `stderr` 모두 출력을 터미널 화면으로 보내므로 오류 메시지가 직접 표시되는 것입니다.

`stderr`를 제어하려면 다른 리디렉션 방법이 필요합니다.

### 파일 디스크립터 이해하기

`stdin`, `stdout`, `stderr`와 같은 I/O 스트림을 관리하기 위해 시스템은 파일 디스크립터를 사용합니다. **파일 디스크립터**는 커널이 열린 파일이나 스트림을 식별하는 데 사용하는 음이 아닌 정수입니다. 기본 파일 디스크립터는 다음과 같습니다.

- `0`: stdin (표준 입력)
- `1`: stdout (표준 출력)
- `2`: stderr (표준 오류)

숫자 `2`는 전용 **stderr 파일 디스크립터**이며, 이를 사용하여 오류 메시지가 어디로 가는지 제어할 수 있습니다.

### stderr 를 파일로 리디렉션하기

`stderr`를 파일로 리디렉션하려면 파일 디스크립터 `2` 뒤에 `>` 연산자를 사용합니다. 이 명령은 모든 오류 메시지를 지정된 `stderr 파일`로 보냅니다.

```bash
ls /fake/directory 2> peanuts.txt
```

이제 터미널은 조용해지고 오류 메시지는 `peanuts.txt` 파일 안에 있게 됩니다.

### stdout 및 stderr 결합하기

정상 출력과 오류 메시지를 모두 동일한 파일에 캡처하고 싶다면 어떻게 해야 할까요? 두 스트림을 모두 리디렉션하여 이를 수행할 수 있습니다.

```bash
ls /fake/directory /etc/passwd > peanuts.txt 2>&1
```

이것을 분석해 보겠습니다.

1. `> peanuts.txt`는 `stdout`(파일 디스크립터 1) 을 `peanuts.txt` 파일로 리디렉션합니다.
2. `2>&1`은 `stderr`(파일 디스크립터 2) 를 `stdout`(파일 디스크립터 1) 이 현재 가리키고 있는 위치로 리디렉션합니다.

순서가 중요합니다. `2>&1`은 `stderr`를 `stdout`의 현재 대상으로 보냅니다. 이 경우 `stdout`은 파일로 연결되어 있으므로 `stderr`도 해당 파일로 전송됩니다.

`stdout`과 `stderr`를 모두 리디렉션하는 더 현대적이고 짧은 방법은 `&>`를 사용하는 것입니다.

```bash
ls /fake/directory /etc/passwd &> peanuts.txt
```

### 오류 메시지 폐기하기

때로는 명령을 실행하고 잠재적인 오류 메시지를 완전히 무시하고 싶을 수 있습니다. 이 작업을 수행하려면 `stderr`를 `/dev/null`이라는 특수 파일로 리디렉션할 수 있으며, 이 파일은 기록되는 모든 데이터를 폐기합니다.

```bash
ls /fake/directory 2> /dev/null
```

이 명령은 실행되며 `stderr`의 모든 오류 출력은 `/dev/null`로 전송되어 폐기되므로 화면이 깨끗하게 유지됩니다.

## Exercise

연습이 완벽하게 만듭니다! 입력/출력 리디렉션에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[Linux 에서 입력 및 출력 리디렉션](https://labex.io/ko/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 이 랩에서는 Linux 셸에서 입력 및 출력을 리디렉션하는 방법을 배웁니다. 표준 출력 (stdout), 표준 오류 (stderr) 및 표준 입력 (stdin) 을 제어하고 >, >>, 2> 및 tee 명령과 같은 연산자를 사용하여 데이터 흐름을 조작하는 방법을 연습합니다.

이 랩은 실제 시나리오에서 I/O 리디렉션 개념을 적용하고 Linux 에서 데이터 스트림을 관리하는 데 자신감을 갖도록 도와줄 것입니다.

## Quiz Question

`stderr` 스트림을 리디렉션하는 데 사용되는 연산자는 무엇입니까? 답변에 정확한 연산자를 제공해 주세요.

## Quiz Answer

2>
