---
lesson_id: "stderr-standard-error-redirect"
course_id: "text-fu"
lang: "ko"
order_index: 3
title: "stderr (표준 오류)"
description: "Bash에서 표준 오류를 별도로 리디렉션하거나 표준 출력과 결합하는 방법을 배웁니다."
meta_title: "stderr (표준 오류) - Text-Fu"
meta_description: "Linux 에서 표준 오류를 관리하는 방법을 알아보세요. 이 가이드는 stderr 리디렉션, stderr 파일 디스크립터 (2), 그리고 2>, 2>&1, &>를 사용하여 stderr 를 파일이나 /dev/null로 리디렉션하는 방법을 다룹니다."
meta_keywords: "stderr, 표준 오류 리눅스, stderr 파일 디스크립터, stderr 파일, 리눅스 표준 오류, stderr 리디렉션, 2>, 2>&1, &>, /dev/null, bash 오류 처리"
---

프로그램은 보통 정상 결과를 표준 출력에, 진단 메시지를 **stderr**로 줄여 쓰는 표준 오류라는 별도 스트림에 씁니다. 스트림을 분리하면 오류 메시지를 섞지 않고 유용한 데이터를 저장할 수 있습니다.

## 정상 출력과 오류 분리하기

존재하지 않는 경로를 지정한 명령어를 살펴보겠습니다.

```bash
$ ls /fake/directory > peanuts.txt
ls: cannot access '/fake/directory': No such file or directory
```

`>`는 stdout만 리디렉션합니다. 진단은 여전히 터미널에 연결된 stderr로 나갑니다. 한편 쉘은 `ls`에 정상 결과가 없어도 stdout용 `peanuts.txt`를 만들거나 잘라냅니다.

표준 스트림은 관례상 다음 파일 디스크립터를 사용합니다.

- `0`: stdin (표준 입력)
- `1`: stdout (표준 출력)
- `2`: stderr (표준 오류)

:::single-choice{#stderr-not-in-stdout-file} `ls /missing > results.txt`의 오류가 보통 터미널에 남는 이유는 무엇인가요?

::option[`>`는 stdout을 리디렉션하고 진단 메시지는 stderr에 쓰기 때문입니다.]{#stderr-separate-stream .correct explanation="일반 `>`는 파일 디스크립터 1만 바꾸므로 디스크립터 2는 기존 터미널 목적지를 유지합니다."}
::option[`ls`가 파일이 닫힐 때까지 기다린 뒤 오류를 출력하기 때문입니다.]{#stderr-waits-for-close explanation="출력 시점의 문제가 아니라 정상 메시지와 진단 메시지가 서로 다른 스트림을 사용하기 때문입니다."}
::option[`results.txt`는 정상 텍스트만 저장하고 진단 메시지는 저장할 수 없기 때문입니다.]{#stderr-file-capability explanation="일반 파일은 어느 스트림이든 저장할 수 있으며 명령줄이 stderr를 그 파일로 리디렉션하지 않았을 뿐입니다."}
:::

## 2>로 stderr 리디렉션하기

`stderr`를 파일로 리디렉션하려면 파일 디스크립터 `2` 뒤에 `>` 연산자를 사용합니다. 이 명령은 모든 오류 메시지를 지정된 `stderr 파일`로 보냅니다.

```bash
$ ls /fake/directory 2> errors.txt
```

쉘은 `errors.txt`를 만들거나 잘라내고 디스크립터 2에 연결합니다. stdout은 기존 목적지를 유지합니다. 오류 출력을 추가하려면 `2>> errors.txt`를 사용합니다.

:::single-choice{#stderr-to-error-file} stdout은 기존 목적지에 둔 채 `find /restricted`의 진단으로 `errors.log`를 교체하는 명령어는 무엇인가요?

::option[`find /restricted > errors.log`]{#stdout-errors-log explanation="일반 `>`는 디스크립터 1을 리디렉션하므로 진단이 아니라 정상 결과를 캡처합니다."}
::option[`find /restricted < errors.log`]{#stdin-errors-log explanation="`<`는 파일을 stdin으로 제공하며 어느 출력 스트림도 캡처하지 않습니다."}
::option[`find /restricted 2> errors.log`]{#stderr-errors-log .correct explanation="앞의 `2`가 stderr를 선택하고 `>`는 해당 스트림의 목적지를 만들거나 잘라냅니다."}
:::

## stdout과 stderr 결합하기

정상 출력과 오류 메시지를 모두 동일한 파일에 캡처하고 싶다면 어떻게 해야 할까요? 두 스트림을 모두 리디렉션하여 이를 수행할 수 있습니다.

```bash
$ ls /fake/directory /etc/passwd > combined.txt 2>&1
```

이것을 분석해 보겠습니다.

1. `> combined.txt`는 stdout을 파일에 연결합니다.
2. `2>&1`은 `stderr`(파일 디스크립터 2) 를 `stdout`(파일 디스크립터 1) 이 현재 가리키고 있는 위치로 리디렉션합니다.

리디렉션은 왼쪽에서 오른쪽으로 처리되므로 순서가 중요합니다. 순서를 뒤집으면 결과도 달라집니다.

```bash
$ ls /fake/directory /etc/passwd 2>&1 > regular.txt
```

여기서는 stderr가 먼저 stdout의 원래 터미널 목적지를 복제하고, 그 뒤 stdout만 `regular.txt`로 이동하므로 두 스트림이 다른 곳으로 갑니다.

:::single-choice{#stderr-combine-order} `command`의 stdout과 stderr를 모두 `all.log`로 보내는 Bash 리디렉션은 무엇인가요?

::option[`command 2>&1 > all.log`]{#stderr-before-stdout explanation="먼저 stderr를 stdout의 이전 목적지에 연결한 뒤 stdout만 파일로 보내므로 두 스트림이 분리됩니다."}
::option[`command 2> all.log > /dev/null`]{#stderr-file-stdout-null explanation="stderr는 `all.log`로 보내지만 stdout은 버리므로 두 스트림을 파일에 결합하지 않습니다."}
::option[`command > all.log 2>&1`]{#stdout-then-stderr .correct explanation="stdout을 먼저 파일로 보내고 stderr가 그 시점의 stdout 목적지를 복제합니다."}
:::

`stdout`과 `stderr`를 모두 리디렉션하는 더 현대적이고 짧은 방법은 `&>`를 사용하는 것입니다.

```bash
$ ls /fake/directory /etc/passwd &> combined.txt
```

Bash에서 두 스트림을 추가하려면 `&>>`를 사용합니다. 명시적인 `> file 2>&1` 형식도 쉘 스크립트와 문서에 자주 나오므로 알아둘 가치가 있습니다.

:::single-choice{#stderr-bash-short-form} `build`의 stdout과 stderr를 모두 `build.log`에 추가하는 Bash 명령어는 무엇인가요?

::option[`build &> build.log`]{#replace-both-build explanation="Bash의 `&>`는 두 스트림을 리디렉션하지만 기존 파일에 추가하지 않고 교체합니다."}
::option[`build 2>> build.log`]{#append-errors-build explanation="stderr만 추가하며 stdout은 기존 목적지를 유지합니다."}
::option[`build &>> build.log`]{#append-both-build .correct explanation="Bash에서 `&>>`는 파일 디스크립터 1과 2를 같은 목적지 뒤에 추가합니다."}
:::

## 의도적으로 스트림 버리기

때로는 명령을 실행하고 잠재적인 오류 메시지를 완전히 무시하고 싶을 수 있습니다. 이 작업을 수행하려면 `stderr`를 `/dev/null`이라는 특수 파일로 리디렉션할 수 있으며, 이 파일은 기록되는 모든 데이터를 폐기합니다.

```bash
$ ls /fake/directory 2> /dev/null
```

이는 명령어를 성공하게 만들거나 종료 상태를 바꾸지 않고 진단 스트림만 숨깁니다. 문제 해결 중에는 필요한 정보를 버리지 말고 stderr를 보존하거나 표시하세요.

:::single-choice{#stderr-dev-null-effect} `check-data 2> /dev/null`은 무엇을 바꾸나요?

::option[stdout을 버리고 모든 오류를 성공으로 바꿉니다.]{#discard-stdout-success explanation="디스크립터 2는 stdout이 아니라 stderr이며 리디렉션은 프로그램 종료 상태를 다시 쓰지 않습니다."}
::option[stderr를 버리지만 성공 종료 상태를 강제하지는 않습니다.]{#discard-stderr-only .correct explanation="리디렉션은 진단 메시지가 갈 곳만 바꾸고 성공 또는 실패 상태는 프로그램이 결정합니다."}
::option[stderr를 `/dev/null`이라는 숨김 파일에 저장합니다.]{#save-dev-null explanation="`/dev/null`은 기록된 데이터를 버리며 나중에 복구할 저장 파일이 아닙니다."}
:::

세 표준 스트림 관리는 다음 실습에서 연습해 보세요.

1. **[Linux 에서 입력 및 출력 리디렉션](https://labex.io/ko/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 이 랩에서는 Linux 셸에서 입력 및 출력을 리디렉션하는 방법을 배웁니다. 표준 출력 (stdout), 표준 오류 (stderr) 및 표준 입력 (stdin) 을 제어하고 >, >>, 2> 및 tee 명령과 같은 연산자를 사용하여 데이터 흐름을 조작하는 방법을 연습합니다.

## 요약

이제 진단 메시지를 정상 출력과 분리하거나 함께 결합할 수 있습니다.

1. stderr가 파일 디스크립터 2임을 알 수 있습니다.
2. `2>` 또는 `2>>`로 오류 로그를 교체하거나 추가할 수 있습니다.
3. 여러 리디렉션을 왼쪽에서 오른쪽으로 적용할 수 있습니다.
4. 두 출력 스트림을 의도한 구문으로 결합할 수 있습니다.
5. 진단 손실을 감수할 수 있을 때만 버릴 수 있습니다.
