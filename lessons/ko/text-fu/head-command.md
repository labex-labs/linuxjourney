---
lesson_id: "head-command"
course_id: "text-fu"
lang: "ko"
order_index: 8
title: "head"
description: "입력의 시작 부분에서 지정한 수의 줄이나 바이트를 표시하는 방법을 배웁니다."
meta_title: "head - Text-Fu"
meta_description: "파일 시작 부분을 보는 head 명령어 사용법에 대한 초보자용 리눅스 가이드입니다. 라인 수를 제어하는 head -n 옵션 사용법을 배우세요. 이는 모든 리눅스 튜토리얼에서 필수적인 기술입니다."
meta_keywords: "head 명령어, 리눅스 head, 파일 시작 보기, 리눅스 튜토리얼, 리눅스 명령어, 초보자 리눅스, head -n, 리눅스 가이드, 텍스트 파일, 명령줄"
---

`head` 명령어는 파일이나 입력 스트림의 시작 부분을 표시합니다. 헤더를 확인하거나 구조화된 데이터를 미리 보거나 전체를 출력하지 않고 일부를 살펴볼 때 유용합니다.

## 처음 열 줄 표시하기

개수 옵션 없이 실행하면 `head`는 지정한 각 파일의 처음 10줄을 출력합니다.

```bash
$ head events.log
```

파일은 수정되지 않습니다. 파일이 10줄보다 짧으면 사용 가능한 모든 줄을 출력합니다.

:::single-choice{#head-default-lines}
기본적으로 `head events.log`는 무엇을 출력하나요?

::option[마지막 10줄 또는 파일이 더 짧으면 모든 줄을 출력합니다.]{#head-last-ten explanation="입력의 끝을 표시하는 것은 `tail`의 역할입니다. `head`는 시작 부분을 선택합니다."}
::option[처음 10줄 또는 파일이 더 짧으면 모든 줄을 출력합니다.]{#head-first-ten .correct explanation="개수 옵션이 없으면 `head`는 입력의 처음 열 줄까지 선택합니다."}
::option[파일 길이와 관계없이 첫 줄만 출력합니다.]{#head-first-one explanation="한 줄을 보려면 `-n 1`처럼 개수를 명시해야 하며 기본 개수는 열입니다."}
:::

## 줄 수 선택하기

출력할 줄 수를 고르려면 `-n NUMBER`를 사용합니다.

```bash
$ head -n 15 events.log
```

GNU `head`는 축약형 `-15`도 지원하지만 `-n 15`가 옵션의 의미를 더 분명하게 나타냅니다.

:::single-choice{#head-five-lines}
`report.txt`의 처음 다섯 줄을 표시하는 명령어는 무엇인가요?

::option[`head -c 5 report.txt`]{#head-five-bytes explanation="`-c` 옵션은 줄이 아니라 바이트를 세므로 첫 줄 중간에서 멈출 수 있습니다."}
::option[`head -n 5 report.txt`]{#head-report-five .correct explanation="`-n` 옵션은 줄 수를 선택하며 `5`는 처음 다섯 줄을 요청합니다."}
::option[`tail -n 5 report.txt`]{#tail-five-lines explanation="파일의 시작이 아니라 마지막 다섯 줄을 표시합니다."}
:::

## 바이트 수 선택하기

완전한 줄 대신 바이트가 필요할 때는 `-c NUMBER`를 사용합니다.

```bash
$ head -c 20 archive.bin
```

처음 20바이트를 출력합니다. 텍스트 줄의 중간이나 멀티바이트 텍스트의 인코딩된 문자 중간에서 출력이 끝날 수 있습니다. 일반 텍스트를 미리 볼 때는 줄 모드를 사용하세요.

:::single-choice{#head-first-bytes}
`payload.bin`의 처음 100바이트를 표준 출력에 쓰는 명령어는 무엇인가요?

::option[`head -c 100 payload.bin`]{#head-hundred-bytes .correct explanation="`-c` 옵션은 바이트 수를 선택하므로 사용 가능한 처음 100바이트를 요청합니다."}
::option[`head -n 100 payload.bin`]{#head-hundred-lines explanation="`-n` 옵션은 바이트가 아니라 줄을 셉니다. 100바이트보다 훨씬 많거나 적게 출력할 수 있습니다."}
::option[`cut -c 100 payload.bin`]{#cut-hundredth-character explanation="전체 입력의 처음 100바이트가 아니라 각 줄의 100번째 위치를 선택합니다."}
:::

## 표준 입력과 여러 파일 읽기

파일 피연산자를 지정하지 않으면 `head`는 표준 입력을 읽습니다.

```bash
$ generate-report | head -n 5
```

여러 파일을 지정하면 `head`는 일반적으로 각 파일의 출력을 식별하는 헤더를 추가합니다.

```bash
$ head -n 2 january.txt february.txt
==> january.txt <==
...

==> february.txt <==
...
```

헤더를 숨기려면 `-q`를 사용하고 파일이 하나여도 헤더를 표시하려면 `-v`를 사용합니다.

:::single-choice{#head-pipeline-preview}
`generate-report | head -n 5`에서 `head`는 무엇을 읽나요?

::option[표준 입력을 통해 `generate-report`의 표준 출력을 읽습니다.]{#head-pipe-input .correct explanation="파이프는 생성자의 표준 출력을 `head`의 표준 입력에 연결하며 여기서 처음 다섯 줄을 선택합니다."}
::option[현재 디렉터리의 처음 다섯 파일 이름을 읽습니다.]{#head-directory-names explanation="디렉터리 나열 명령어는 사용되지 않았습니다. `head`는 파이프라인을 통해 스트림을 받습니다."}
::option[이름이 `generate-report`인 파일에서 5바이트를 읽습니다.]{#head-producer-file explanation="왼쪽은 명령어로 실행되며 `-n`은 바이트가 아니라 줄을 셉니다."}
:::

:::single-choice{#head-suppress-filename-headers}
`head`가 여러 파일을 읽을 때 파일 이름 헤더를 숨기는 옵션은 무엇인가요?

::option[`-v`]{#head-verbose explanation="`-v` 옵션은 파일이 하나뿐이어도 헤더를 요청하므로 숨기기와 반대입니다."}
::option[`-c`]{#head-byte-option explanation="`-c` 옵션은 선택 단위를 바이트로 바꾸며 파일 이름 헤더를 제어하지 않습니다."}
::option[`-q`]{#head-quiet .correct explanation="`-q`, 즉 quiet 옵션은 `head`가 파일별 헤더 레이블을 출력하지 않게 합니다."}
:::

파일 시작 부분 미리 보기를 연습하려면 다음 실습을 진행해 보세요.

1. **[리눅스 head 명령어: 파일 시작 표시](https://labex.io/ko/labs/linux-linux-head-command-file-beginning-display-214302)** - `head`로 텍스트 파일의 처음 줄을 표시하고 줄 수를 바꾸는 방법을 연습합니다.
2. **[리눅스에서 로그 및 구성 파일 보기](https://labex.io/ko/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 시스템 로그와 구성 파일을 효율적으로 보고 탐색하는 필수 명령줄 기술을 연습합니다.
3. **[신속한 위협 탐지](https://labex.io/ko/labs/linux-rapid-threat-detection-387930)** - `head`와 `tail`을 활용해 로그 항목을 빠르게 추출하고 분석합니다.

## 요약

이제 `head`로 파일과 명령 출력의 시작 부분을 미리 볼 수 있습니다.

1. 기본값인 처음 열 줄 보기를 사용할 수 있습니다.
2. `-n`으로 줄 수를 선택할 수 있습니다.
3. 적절한 경우 `-c`로 바이트 수를 선택할 수 있습니다.
4. 파이프라인에서 표준 입력을 읽을 수 있습니다.
5. 여러 파일을 표시할 때 헤더를 제어할 수 있습니다.
