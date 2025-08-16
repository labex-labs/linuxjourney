---
title: "stderr (표준 에러)"
description: "Linux stderr(표준 에러) 리디렉션에 대해 알아보세요. Bash 에서 에러 처리를 위한 2>, 2>&1, &>, 그리고 /dev/null을 이해하세요. Linux 명령줄 기술을 향상시키세요!"
keywords: "Linux stderr, 표준 에러, 2> 리디렉션, 2>&1, &> 리디렉션, /dev/null, Bash 에러 처리, Linux 튜토리얼, Linux 초보자"
---

## Lesson Content

이제 조금 다른 것을 시도해 봅시다. 시스템에 존재하지 않는 디렉터리의 내용을 나열하고 출력을 다시 `peanuts.txt` 파일로 리디렉션해 봅시다.

```bash
ls /fake/directory > peanuts.txt
```

다음과 같은 메시지가 표시되어야 합니다:

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

이제 여러분은 아마도 그 메시지가 파일로 전송되었어야 하는 것 아니냐고 생각할 것입니다. 여기에는 표준 에러 (stderr) 라고 불리는 또 다른 I/O 스트림이 있습니다. 기본적으로 stderr 도 출력을 화면으로 보냅니다. 이는 stdout 과는 완전히 다른 스트림입니다. 따라서 출력을 다른 방식으로 리디렉션해야 합니다.

불행히도 리디렉터는 `<` 또는 `>`를 사용하는 것만큼 편리하지는 않지만, 거의 비슷합니다. 파일 디스크립터를 사용해야 합니다. 파일 디스크립터는 파일 또는 스트림에 접근하는 데 사용되는 음수가 아닌 숫자입니다. 이에 대해서는 나중에 자세히 다루겠지만, 지금은 stdin, stdout, stderr 의 파일 디스크립터가 각각 0, 1, 2 라는 것을 알아두세요.

이제 stderr 를 파일로 리디렉션하려면 다음과 같이 할 수 있습니다:

```bash
ls /fake/directory 2> peanuts.txt
```

`peanuts.txt`에서 stderr 메시지만 표시되어야 합니다.

이제 `peanuts.txt` 파일에서 stderr 와 stdout 을 모두 보고 싶다면 어떻게 해야 할까요? 파일 디스크립터를 사용해서도 가능합니다:

```bash
ls /fake/directory > peanuts.txt 2>&1
```

이것은 `ls /fake/directory`의 결과를 `peanuts.txt` 파일로 보내고, `2>&1`을 통해 stderr 를 stdout 으로 리디렉션합니다. 여기서 작업 순서가 중요합니다. `2>&1`은 stderr 를 stdout 이 가리키는 곳으로 보냅니다. 이 경우 stdout 은 파일을 가리키므로 `2>&1`도 stderr 를 파일로 보냅니다. 따라서 `peanuts.txt` 파일을 열면 stderr 와 stdout 을 모두 볼 수 있습니다. 우리의 경우, 위 명령은 stderr 만 출력합니다.

stdout 과 stderr 를 모두 파일로 리디렉션하는 더 짧은 방법이 있습니다:

```bash
ls /fake/directory &> peanuts.txt
```

이제 그런 불필요한 메시지를 모두 없애고 stderr 메시지를 완전히 제거하고 싶다면 어떻게 해야 할까요? 음, `/dev/null`이라는 특수 파일로 출력을 리디렉션할 수도 있으며, 이는 모든 입력을 버립니다.

```bash
ls /fake/directory 2> /dev/null
```

## Exercise

다음 명령은 무엇을 하는 것입니까?

```bash
ls /fake/directory >> /dev/null 2>&1
```

## Quiz Question

stderr 의 리디렉터는 무엇입니까?

## Quiz Answer

2>
