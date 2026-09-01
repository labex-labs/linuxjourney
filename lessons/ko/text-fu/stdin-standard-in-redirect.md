---
lesson_id: "stdin-standard-in-redirect"
course_id: "text-fu"
lang: "ko"
order_index: 2
title: "표준 입력 (stdin)"
description: "프로그램이 표준 입력을 읽는 방식과 Bash가 그 스트림을 파일에 연결하는 방법을 배웁니다."
meta_title: "표준 입력 (stdin) - Text-Fu"
meta_description: "stdin(표준 입력) 리디렉션을 학습하여 Linux 명령줄 작업을 마스터하세요. 이 가이드는 stdin 과 stdout 의 관계, '<' 연산자 사용법, 그리고 'cat stdin'과 같은 실용적인 예제를 다루어 데이터 스트림을 효과적으로 관리하는 방법을 설명합니다."
meta_keywords: "stdin, 표준입력, stdin 리디렉션, cat stdin, stdin 과 stdout, 표준 입력, 리눅스 리디렉션, 명령줄, 입력 스트림"
---

**stdin**으로 줄여 쓰는 표준 입력은 프로그램이 들어오는 데이터를 보통 읽는 스트림입니다. 대화형 터미널에서 쉘은 일반적으로 stdin을 터미널 입력에 연결해 프로그램이 사용자가 입력한 내용을 읽게 합니다.

## 표준 입력과 파일 디스크립터 0

관례상 세 표준 스트림은 다음 파일 디스크립터 번호를 사용합니다.

- `0`: 표준 입력(`stdin`)
- `1`: 표준 출력(`stdout`)
- `2`: 표준 오류(`stderr`)

프로그램은 이 스트림을 사용할지와 사용 방식을 선택할 수 있습니다. stdin을 읽도록 만든 명령어는 파일 피연산자나 다른 입력 소스가 없으면 흔히 터미널 입력을 기다립니다.

:::single-choice{#stdin-descriptor-number} 표준 입력을 관례상 나타내는 파일 디스크립터는 무엇인가요?

::option[`0`]{#stdin-fd-zero .correct explanation="표준 입력은 관례상 파일 디스크립터 0입니다."}
::option[`1`]{#stdin-fd-one explanation="파일 디스크립터 1은 정상 결과를 위한 표준 출력을 나타냅니다."}
::option[`2`]{#stdin-fd-two explanation="파일 디스크립터 2는 표준 입력이 아니라 표준 오류를 나타냅니다."}
:::

## 파일을 stdin으로 리디렉션하기

`<` 연산자는 Bash가 파일을 읽기용으로 열어 명령어의 stdin에 연결하게 합니다.

```bash
$ cat < peanuts.txt
Hello World
```

쉘은 `< peanuts.txt`를 처리하고 `cat`은 파일 디스크립터 0을 읽을 뿐입니다. 경로는 일반 파일 피연산자로 `cat`에 전달되지 않습니다.

입력 파일이 없거나 열 수 없으면 쉘이 리디렉션 오류를 내고 해당 입력으로 명령어를 시작하지 않습니다.

:::single-choice{#stdin-from-file} `sort`가 `names.txt`에서 표준 입력을 읽게 하는 명령어는 무엇인가요?

::option[`sort < names.txt`]{#sort-stdin-file .correct explanation="Bash가 `names.txt`를 읽기용으로 열고 파일 디스크립터 0으로 `sort`에 연결합니다."}
::option[`sort > names.txt`]{#stdout-to-names explanation="`>`는 stdout을 파일로 리디렉션해 내용을 잘라낼 수 있으며 파일을 입력으로 제공하지 않습니다."}
::option[`sort names.txt >`]{#incomplete-sort-output explanation="불완전한 출력 리디렉션을 포함하며 요청한 stdin 연결을 나타내지 않습니다."}
:::

## 파일 피연산자와 입력 리디렉션

일부 명령어는 파일 이름 피연산자나 stdin을 모두 받을 수 있지만 결과가 약간 다를 수 있습니다.

```bash
$ wc -l peanuts.txt
1 peanuts.txt
$ wc -l < peanuts.txt
1
```

두 형식은 같은 데이터의 줄을 셉니다. 첫 번째에서는 `wc`가 파일 이름을 인자로 받으므로 이름을 알고, 두 번째에서는 stdin 스트림만 받아 출력할 파일 이름이 없습니다.

:::single-choice{#stdin-not-command-argument} `wc -l < peanuts.txt`가 보통 출력에서 `peanuts.txt`를 생략하는 이유는 무엇인가요?

::option[`wc`가 줄을 센 뒤 파일 이름을 삭제합니다.]{#stdin-delete-name explanation="명령어는 원본 파일의 이름을 바꾸거나 삭제하지 않으며 입력 연결만 달라집니다."}
::option[`<` 연산자가 명령어가 출력하는 모든 단어를 숨깁니다.]{#stdin-hide-words explanation="입력 리디렉션은 stdout을 필터링하지 않으며 `wc`가 파일 이름을 인자로 받지 않아 이름이 없습니다."}
::option[Bash가 파일 이름 인자 대신 stdin으로 파일을 제공합니다.]{#stdin-no-filename .correct explanation="쉘이 리디렉션을 소비해 파일을 디스크립터 0에 연결하므로 `wc`는 경로를 피연산자로 받지 않습니다."}
:::

## 입력과 출력 리디렉션 결합하기

한 명령줄에서 둘 이상의 스트림을 리디렉션할 수 있습니다.

```bash
$ cat < peanuts.txt > banana.txt
```

쉘은 서로 독립적인 두 연결을 수행합니다.

1. `< peanuts.txt`는 `peanuts.txt`를 `cat`의 stdin으로 엽니다.
2. `> banana.txt`는 `banana.txt`를 만들거나 잘라내고 `cat`의 stdout에 연결합니다.

`cat`은 stdin에서 바이트를 읽어 stdout으로 쓰므로 `banana.txt`가 원본 내용을 받습니다. 일반적인 파일 복사에는 `cp peanuts.txt banana.txt`가 의도를 더 직접적으로 전달하며, 이 예제는 스트림 연결을 보여 주기 위한 것입니다.

:::single-choice{#stdin-and-stdout-files} `cat < input.txt > output.txt`에서 stdin을 제공하는 파일과 stdout을 받는 파일은 각각 무엇인가요?

::option[`output.txt`가 stdin을 제공하고 `input.txt`가 stdout을 받습니다.]{#stdin-output-stdout-input explanation="리디렉션 연산자의 의미를 반대로 설명했습니다. 입력 화살표는 명령어 쪽으로, 출력 화살표는 파일 쪽으로 향합니다."}
::option[`input.txt`가 stdin을 제공하고 `output.txt`가 stdout을 받습니다.]{#stdin-input-stdout-output .correct explanation="`<`는 `input.txt`를 디스크립터 0으로 열고 `>`는 `output.txt`를 디스크립터 1로 엽니다."}
::option[두 파일 모두 stdin을 제공하고 stdout은 터미널에 남습니다.]{#both-stdin explanation="두 연산자는 서로 다른 표준 스트림에 작용하며 `>`가 stdout을 터미널 밖으로 리디렉션합니다."}
:::

입출력 리디렉션은 다음 실습에서 연습해 보세요.

1. **[리눅스에서 입력 및 출력 리디렉션](https://labex.io/ko/labs/comptia-redirecting-input-and-output-in-linux-590840)** - >, >>, 2> 및 tee 명령과 같은 연산자를 사용하여 표준 출력 (stdout), 표준 오류 (stderr), 표준 입력 (stdin) 을 조작하여 명령의 데이터 흐름을 제어하는 연습을 합니다.
2. **[데이터 스트림 리디렉션](https://labex.io/ko/labs/linux-data-stream-redirection-17995)** - 리눅스 스트림 리디렉션 기술을 배웁니다. 표준 입력, 출력 및 오류 스트림을 조작하고, 출력을 결합하며, 고급 파일 작업을 위해 /dev/null을 활용합니다.
## 요약

이제 쉘을 통해 명령어의 표준 입력을 파일에 연결할 수 있습니다.

1. stdin이 파일 디스크립터 0임을 알 수 있습니다.
2. `<`로 읽을 수 있는 파일을 리디렉션할 수 있습니다.
3. 파일 이름 피연산자와 리디렉션 입력을 구분할 수 있습니다.
4. stdin과 stdout 리디렉션을 의도적으로 결합할 수 있습니다.
