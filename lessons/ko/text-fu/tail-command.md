---
lesson_id: "tail-command"
course_id: "text-fu"
lang: "ko"
order_index: 9
title: "tail"
description: "입력의 끝을 보고 새 내용이 추가될 때 파일을 계속 추적하는 방법을 배웁니다."
meta_title: "tail - Text-Fu"
meta_description: "tail 명령어에 대한 초보자용 리눅스 가이드입니다. 리눅스 tail로 파일 끝을 보고 강력한 tail -f 옵션으로 로그를 실시간 모니터링하는 방법을 배웁니다."
meta_keywords: "tail 명령어, 리눅스 tail, tail -f, 로그 보기, 로그 모니터링, 리눅스 튜토리얼, 초보자 리눅스, 리눅스 가이드, 파일 모니터링"
---

`tail` 명령어는 파일이나 입력 스트림의 끝을 표시합니다. 실행 상태를 유지하면서 파일에 추가되는 데이터를 보여 줄 수도 있어 로그를 관찰할 때 유용합니다.

## 마지막 열 줄 표시하기

개수 옵션 없이 실행하면 `tail`은 지정한 각 파일의 마지막 10줄을 출력합니다.

```bash
$ tail application.log
```

파일이 10줄보다 짧으면 사용 가능한 모든 줄을 출력합니다. 파일 자체는 변경되지 않습니다.

:::single-choice{#tail-default-lines}
기본적으로 `tail application.log`는 무엇을 표시하나요?

::option[파일의 처음 10줄까지 표시합니다.]{#tail-first-ten explanation="파일 시작 부분은 `head`가 선택합니다. `tail`은 끝에서부터 작동합니다."}
::option[명령어가 시작된 뒤 추가되는 모든 줄을 표시합니다.]{#tail-follow-only explanation="계속 추적하려면 `-f`나 관련 옵션이 필요합니다. 일반 `tail`은 현재 상태를 출력하고 종료합니다."}
::option[파일의 마지막 10줄까지 표시합니다.]{#tail-last-ten .correct explanation="개수 옵션이 없으면 `tail`은 마지막 열 줄을 선택하며 더 적은 줄만 있으면 모두 표시합니다."}
:::

## 줄 수나 바이트 수 선택하기

마지막 줄을 다른 수만큼 선택하려면 `-n NUMBER`를 사용합니다.

```bash
$ tail -n 20 application.log
```

마지막 바이트가 필요하면 `-c NUMBER`를 사용합니다.

```bash
$ tail -c 100 payload.bin
```

바이트 모드는 텍스트 줄이나 인코딩된 문자의 중간에서 시작할 수 있으므로 텍스트에는 보통 줄 모드가 더 명확합니다.

:::single-choice{#tail-twenty-lines}
`application.log`의 마지막 20줄을 표시하는 명령어는 무엇인가요?

::option[`tail -n 20 application.log`]{#tail-twenty-end .correct explanation="`-n` 옵션은 줄 수를 선택하고 `tail`은 끝에서 해당 줄들을 가져옵니다."}
::option[`head -n 20 application.log`]{#head-twenty-start explanation="끝이 아니라 시작 부분에서 20줄을 선택합니다."}
::option[`tail -c 20 application.log`]{#tail-twenty-bytes explanation="`-c` 옵션은 마지막 20바이트를 선택하며 이는 20줄과 같지 않습니다."}
:::

## 특정 줄에서 시작하기

개수 앞에 `+`를 붙이면 의미가 달라집니다. `tail -n +N`은 N번째 줄부터 끝까지 출력합니다.

```bash
$ tail -n +5 report.txt
```

처음 네 줄을 건너뛰고 5번째 줄에서 시작합니다. 스트림에서 정해진 수의 헤더 줄을 제거할 때 유용합니다.

:::single-choice{#tail-start-line-five}
`report.txt`를 5번째 줄부터 출력하는 명령어는 무엇인가요?

::option[`tail -n +5 report.txt`]{#tail-from-five .correct explanation="`+5`는 `tail`에 5번째 줄부터 끝까지 계속 출력하라고 지시합니다."}
::option[`tail -n 5 report.txt`]{#tail-final-five explanation="더하기 기호가 없으면 절대 줄 번호와 관계없이 마지막 다섯 줄을 선택합니다."}
::option[`head -n +5 report.txt`]{#head-plus-five explanation="`tail`의 특정 줄부터 시작하는 형식이 아닙니다. 요청한 범위에는 `tail -n +5`를 사용합니다."}
:::

## 추가되는 데이터 추적하기

`-f`를 사용하면 `tail`은 현재 끝부분을 출력한 뒤 실행 상태를 유지하며 추가되는 데이터를 표시합니다.

```bash
$ tail -f application.log
```

`Ctrl+C`를 눌러 `tail`을 중단하고 쉘로 돌아갑니다. 파일 추적은 새 내용만 보여 줄 뿐 로그를 만드는 애플리케이션이 정상인지 또는 모든 관련 이벤트가 그 파일을 사용하는지는 보장하지 않습니다.

:::single-choice{#tail-follow-file}
`application.log`의 현재 끝을 표시한 뒤 추가되는 내용을 계속 기다리는 명령어는 무엇인가요?

::option[`tail -f application.log`]{#tail-follow-app .correct explanation="`-f` 옵션은 `tail`을 계속 실행하고 파일에 추가되는 데이터를 표시합니다."}
::option[`tail -n 0 application.log`]{#tail-zero-lines explanation="처음에 어떤 줄도 출력하지 않으며 추적 옵션이 없으므로 종료됩니다."}
::option[`less application.log`]{#less-log explanation="`less`는 대화형 페이지 탐색을 제공하지만 이 형식은 `tail`처럼 추적 모드로 계속 실행되지 않습니다."}
:::

## 교체되는 로그를 이름으로 추적하기

로그 로테이션은 이전 파일의 이름을 바꾸고 원래 경로에 새 파일을 만들 수 있습니다. GNU `tail -F`는 이름을 기준으로 추적하면서 재시도하므로 교체되거나 잠시 사라진 파일을 다시 열 수 있습니다.

```bash
$ tail -F application.log
```

현재 열린 파일을 계속 추적하려면 `-f`를 사용하고 이름이 지정된 로그가 로테이션될 것으로 예상되면 `-F`를 사용합니다. 이는 GNU 동작이며 다른 구현은 다를 수 있습니다.

:::single-choice{#tail-follow-rotated-name}
GNU/Linux에서 일반적인 이름 변경 후 재생성 방식의 로그 로테이션을 거쳐 `application.log`를 추적하는 데 더 적합한 옵션은 무엇인가요?

::option[`-n`]{#tail-rotation-lines explanation="`-n` 옵션은 표시할 줄 수를 바꾸며 교체된 경로를 다시 시도하지 않습니다."}
::option[`-c`]{#tail-rotation-bytes explanation="`-c` 옵션은 선택 단위를 바이트로 바꾸며 로테이션을 고려한 추적을 제공하지 않습니다."}
::option[`-F`]{#tail-follow-name .correct explanation="GNU `-F`는 이름을 기준으로 추적하고 재시도하므로 교체되거나 잠시 없는 로그를 다시 열 수 있습니다."}
:::

파일을 지정하지 않으면 `tail`은 표준 입력을 읽으므로 명령 출력의 끝을 선택할 수 있습니다. 여러 파일을 지정하면 `head`와 마찬가지로 기본적으로 식별 헤더가 붙습니다.

파일 끝 보기와 추적을 연습하려면 다음 실습을 진행해 보세요.

1. **[리눅스 tail 명령어: 파일 끝 표시](https://labex.io/ko/labs/linux-linux-tail-command-file-end-display-214303)** - 실시간 업데이트를 위한 `-f` 옵션을 포함해 텍스트 파일의 끝을 보고 모니터링하는 방법을 배웁니다.
2. **[리눅스에서 로그 및 구성 파일 보기](https://labex.io/ko/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - `tail`, `cat`, `more`로 로그와 구성 파일을 효율적으로 보고 탐색합니다.
3. **[신속한 위협 탐지](https://labex.io/ko/labs/linux-rapid-threat-detection-387930)** - `tail`로 최근 로그 항목을 빠르게 추출하고 분석합니다.

## 요약

이제 `tail`로 파일 끝을 검사하고 새로 추가되는 내용을 관찰할 수 있습니다.

1. 기본적으로 마지막 열 줄을 표시할 수 있습니다.
2. 줄 수나 바이트 수를 명시적으로 선택할 수 있습니다.
3. `-n +N`으로 번호가 지정된 줄부터 출력을 시작할 수 있습니다.
4. `-f`로 추가 내용을 추적하고 `Ctrl+C`로 중단할 수 있습니다.
5. 이름이 지정된 로그가 로테이션될 수 있을 때 GNU `-F`를 사용할 수 있습니다.
