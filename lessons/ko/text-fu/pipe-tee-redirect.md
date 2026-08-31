---
lesson_id: "pipe-tee-redirect"
course_id: "text-fu"
lang: "ko"
order_index: 4
title: "파이프 및 티"
description: "파이프라인이 명령어를 연결하는 방식과 tee가 스트림을 저장하면서 다음 단계로 보내는 방법을 배웁니다."
meta_title: "파이프 및 티 - Text-Fu"
meta_description: "Linux 에서 강력한 파이프 및 티 명령어를 살펴보세요. Linux 파이프 티 조합으로 명령어를 연결하고 출력을 화면과 파일 모두로 리디렉션하는 방법을 알아보세요. 이 가이드는 고급 명령줄 데이터 흐름을 위해 티로 파이프하는 방법을 다룹니다."
meta_keywords: "리눅스 파이프 및 티 명령어, 리눅스 파이프 티, 티로 파이프, 리눅스 파이프, 티 명령어, stdout, stdin, 명령줄 리디렉션, 리눅스 튜토리얼"
---

파이프라인은 작은 명령어들을 연결해 중간 파일 없이 데이터가 흐르게 합니다. `tee` 명령어는 이 흐름의 일부를 파일에 복사하면서 계속 다음 단계로 보낼 수 있습니다.

## |로 명령어 연결하기

많은 출력을 생성하는 명령어로 시작해 보겠습니다.

```bash
$ ls -la /etc
```

항목 목록이 화면에 다 들어오지 않아 읽기 어려울 수 있습니다. 이 출력을 파일로 리디렉션할 수도 있지만, 더 효율적인 방법은 `less`와 같은 다른 명령어로 직접 보내 쉽게 보는 것입니다.

```bash
$ ls -la /etc | less
```

파이프 연산자 `|`는 왼쪽 명령어의 stdout을 오른쪽 명령어의 stdin에 연결합니다. 쉘은 파이프라인 명령어들을 시작하고 스트림 연결을 구성합니다. 명령어는 동시에 작동할 수 있어 `ls`가 전체 목록을 만들기 전에 `less`가 읽기 시작할 수 있습니다.

:::single-choice{#pipe-stream-connection}
`ls -la /etc | less`에서 `|`는 기본적으로 어떤 스트림을 연결하나요?

::option[`ls`의 stdin을 `less`의 stdout에 연결합니다.]{#pipe-reversed-streams explanation="생산자와 소비자를 모두 반대로 설명했습니다. 데이터는 왼쪽 명령어의 출력에서 오른쪽 명령어의 입력으로 흐릅니다."}
::option[`ls`의 stderr를 `less`의 두 스트림에 연결합니다.]{#pipe-stderr-both explanation="일반 파이프는 왼쪽 명령어의 stderr를 연결하지 않고 오른쪽 명령어의 두 스트림을 대상으로 하지도 않습니다."}
::option[`ls`의 stdout을 `less`의 stdin에 연결합니다.]{#pipe-stdout-stdin .correct explanation="표준 파이프라인은 왼쪽 명령어의 파일 디스크립터 1을 오른쪽 명령어의 파일 디스크립터 0에 연결합니다."}
:::

## stderr를 분리해 두기

일반 `|`는 stdout만 전달합니다. 왼쪽 명령어의 stderr는 흔히 터미널인 기존 목적지를 유지합니다.

```bash
$ find /etc -name "*.conf" | less
```

일치 경로는 파이프로 가지만 권한 진단은 터미널에 직접 나타날 수 있습니다. 다르게 처리하려면 stderr를 별도로 리디렉션합니다.

```bash
$ find /etc -name "*.conf" 2> find-errors.log | less
```

:::single-choice{#pipe-left-stderr}
`find /etc -name "*.conf" | less`에서 별도 리디렉션이 없을 때 `find`의 stderr는 보통 어디로 가나요?

::option[stdout과 같은 파이프를 통해 `less`로 갑니다.]{#pipe-errors-to-less explanation="일반 파이프는 stdout만 연결하고 stderr를 자동으로 결합하지 않습니다."}
::option[현재 디렉터리의 `stderr`라는 파일로 갑니다.]{#pipe-errors-to-file explanation="오류 파일 리디렉션이 없으므로 쉘은 그런 파일을 만들지 않습니다."}
::option[기존 목적지인 터미널로 갑니다.]{#pipe-errors-terminal .correct explanation="디스크립터 2가 바뀌지 않았으므로 진단 메시지는 보통 터미널에 연결된 채로 남습니다."}
:::

## tee로 스트림 복사하기

출력을 화면에 표시하는 동시에 파일에 저장하고 싶다면 어떨까요? 이때 `tee` 명령어가 사용됩니다. `linux에서 pipe와 tee 명령어`는 로깅 및 모니터링을 위한 고전적인 조합입니다.

```bash
$ ls | tee listing.txt
```

`listing.txt`가 목록을 받고 `tee`의 stdout은 터미널에 연결된 채로 남습니다. 기본적으로 `tee`는 `>`처럼 지정한 파일을 만들거나 잘라냅니다.

:::single-choice{#tee-display-and-save}
`generate-report` 출력을 표시하면서 같은 출력으로 `report.txt`를 교체하는 명령어는 무엇인가요?

::option[`generate-report > report.txt`]{#redirect-report-only explanation="일반 출력 리디렉션은 파일에 쓰지만 터미널로 계속 흐르는 복사본을 남기지 않습니다."}
::option[`generate-report | tee report.txt`]{#tee-report .correct explanation="`tee`는 stdin을 `report.txt`와 stdout에 복사하며 이 파이프라인에서 stdout은 터미널입니다."}
::option[`tee generate-report | report.txt`]{#tee-operands-reversed explanation="`generate-report`를 목적지 파일로 처리하고 `report.txt`를 명령어로 실행하려 합니다. 생산자는 왼쪽에 와야 합니다."}
:::

파일을 교체하지 않고 추가하려면 `-a`를 사용합니다.

```bash
$ date | tee -a activity.log
```

:::single-choice{#tee-append-log}
현재 날짜를 표시하면서 `activity.log`에 추가하는 명령어는 무엇인가요?

::option[`date | tee -a activity.log`]{#tee-append-activity .correct explanation="`-a`는 `tee`가 파일에 추가하면서 입력을 stdout으로도 계속 복사하게 합니다."}
::option[`date | tee activity.log`]{#tee-replace-activity explanation="`-a`가 없으면 기존 내용을 보존하지 않고 파일을 교체합니다."}
::option[`date > activity.log`]{#redirect-replace-activity explanation="파일을 교체하며 터미널에 복사본을 보내지 않아 추가와 표시 조건을 모두 충족하지 않습니다."}
:::

## 중간 결과 저장하기

`tee`를 파이프라인 중간에 두면 중간 스트림을 저장하면서 처리를 계속할 수 있습니다.

```bash
$ ls -la /etc | tee etc-listing.txt | grep "conf"
```

이 명령어는 세 가지 작업을 수행합니다.

1. `/etc` 디렉토리의 내용을 나열합니다.
2. 해당 출력을 `tee`로 파이프하여 `etc_listing.txt`에 복사본을 저장하고 동시에 전달합니다.
3. `tee`에서 나온 출력은 `grep`으로 파이프되어 "conf"를 포함하는 줄을 필터링합니다.

파일에는 `grep`이 필터링하기 전 데이터가 들어갑니다. 일치하는 줄만 저장하려면 `tee`를 `grep` 뒤에 둡니다.

:::single-choice{#tee-before-filter-result}
`produce | tee all.txt | grep error`가 성공적으로 끝나면 `all.txt`에는 무엇이 들어 있나요?

::option[`grep`과 일치한 줄만 들어 있습니다.]{#tee-filtered-only explanation="`tee`가 `grep` 앞에서 실행되므로 아래 단계의 일치 집합이 아니라 필터링 전 입력을 씁니다."}
::option[`produce`의 stderr만 들어 있습니다.]{#tee-producer-stderr explanation="일반 파이프는 `produce`의 stdout을 전달하며 stderr는 `tee` 입력이 아닙니다."}
::option[필터링 전 만들어진 모든 stdout이 들어 있습니다.]{#tee-complete-intermediate .correct explanation="`tee`는 받은 모든 바이트를 저장한 뒤 같은 스트림을 `grep`에 전달해 필터링합니다."}
:::

파이프라인과 스트림 복사는 다음 실습에서 연습해 보세요.

1. **[Linux 에서 입력 및 출력 리디렉션](https://labex.io/ko/labs/comptia-redirecting-input-and-output-in-linux-590840)** - 연산자 (예: `>`, `>>`, `2>`, 및 `tee` 명령어) 를 조작하여 명령어의 표준 출력 (stdout), 표준 오류 (stderr), 표준 입력 (stdin) 을 제어하여 데이터 흐름을 연습합니다.
2. **[시퀀스 제어 및 파이프라인](https://labex.io/ko/labs/linux-sequence-control-and-pipeline-17994)** - 명령어 실행 시퀀스를 제어하고, 파이프라인을 활용하며, `cut`, `grep`, `wc`, `sort`, `uniq`와 같은 강력한 텍스트 처리 도구를 활용하는 방법을 배웁니다.
3. **[데이터 스트림 리디렉션](https://labex.io/ko/labs/linux-data-stream-redirection-17995)** - 표준 입력, 출력 및 오류 스트림 조작, 출력 결합, `/dev/null` 활용을 포함하여 Linux 스트림 리디렉션 기술을 배웁니다.

## 요약

이제 명령어를 연결하고 데이터 스트림의 원하는 지점을 보존할 수 있습니다.

1. 한 명령어의 stdout을 다른 명령어의 stdin으로 파이프할 수 있습니다.
2. 필요할 때 stderr를 별도로 리디렉션할 수 있습니다.
3. `tee`로 입력을 파일과 stdout에 함께 복사할 수 있습니다.
4. 파일을 교체하지 않고 `tee -a`로 추가할 수 있습니다.
5. 필터 앞이나 뒤에 `tee`를 의도적으로 배치할 수 있습니다.
