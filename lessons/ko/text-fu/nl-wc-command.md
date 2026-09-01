---
lesson_id: "nl-wc-command"
course_id: "text-fu"
lang: "ko"
order_index: 15
title: "wc와 nl"
description: "wc로 줄, 단어, 바이트, 문자를 세고 nl로 줄 번호를 붙이는 방법을 배웁니다."
meta_title: "wc와 nl - Text-Fu"
meta_description: "이 Linux 튜토리얼에서 wc와 nl 명령어를 익혀 보세요. Linux 단어 수를 세고 파일에 줄 번호를 추가하며 기본적인 파일 분석을 수행하는 방법을 배웁니다."
meta_keywords: "wc 명령어, nl 명령어, Linux 단어 수, Linux 파일 단어 세기, Linux 줄 번호, nl 명령어 Linux, 파일 분석, Linux 텍스트 처리, Linux 명령줄, 초보자 Linux 튜토리얼"
---

`wc` 명령어는 텍스트 스트림의 여러 속성을 세고 `nl`은 입력에 생성한 줄 번호를 붙여 씁니다. 둘 다 파일이나 표준 입력을 읽고 결과를 표준 출력으로 보냅니다.

## wc 기본 출력 읽기

개수 옵션이 없으면 `wc`는 줄 바꿈 문자 수, 단어 수, 바이트 수를 출력하고 파일을 지정했을 때는 파일 이름을 뒤에 붙입니다.

```bash
$ printf 'red blue\ngreen\n' > colors.txt
$ wc colors.txt
 2  3 15 colors.txt
```

왼쪽부터 다음을 뜻합니다.

1. 줄 수로 보고되는 줄 바꿈 문자 `2`개
2. 공백으로 구분된 단어 `3`개
3. 이 ASCII 예제의 바이트 `15`개

끝에 줄 바꿈이 없는 마지막 텍스트 줄은 `wc -l`에서 세지 않습니다. 이 옵션은 눈으로 보이는 줄이 아니라 줄 바꿈 문자를 세기 때문입니다.

:::single-choice{#wc-default-columns} `wc file.txt`의 기본 출력에서 처음 세 숫자는 무엇을 나타내나요?

::option[차례대로 줄, 단어, 바이트입니다.]{#wc-lines-words-bytes .correct explanation="기본 `wc` 출력은 파일 이름 앞에 줄 바꿈 수, 단어 수, 바이트 수를 보고합니다."}
::option[차례대로 바이트, 단어, 줄입니다.]{#wc-bytes-words-lines explanation="같은 측정값이지만 순서가 잘못되었습니다. 줄 수가 먼저 나옵니다."}
::option[차례대로 파일, 문자, 문단입니다.]{#wc-files-characters-paragraphs explanation="기본 열은 파일이나 문단을 세지 않으며 세 번째 기본 측정값은 바이트입니다."}
:::

## 한 가지 개수 요청하기

필요한 측정값만 선택할 수 있습니다.

- `-l`: 줄 바꿈 문자 수
- `-w`: 단어 수
- `-c`: 바이트 수
- `-m`: 현재 로캘에 따른 문자 수

예를 들면 다음과 같습니다.

```bash
$ wc -w colors.txt
3 colors.txt
```

ASCII 텍스트에서는 바이트 수와 문자 수가 같지만 UTF-8 같은 멀티바이트 인코딩에서는 다를 수 있습니다. 파일 이름 피연산자 없이 표준 입력을 사용하면 `wc`는 일반적으로 파일 이름 레이블을 생략합니다.

```bash
$ printf 'one two\n' | wc -w
2
```

:::single-choice{#wc-word-count-only} `essay.txt`의 단어 수만 보고하는 명령어는 무엇인가요?

::option[`wc -l essay.txt`]{#wc-lines-essay explanation="`-l` 옵션은 단어가 아니라 줄 바꿈 문자를 보고합니다."}
::option[`wc -w essay.txt`]{#wc-words-essay .correct explanation="`-w` 옵션은 단어 수 측정값을 선택합니다."}
::option[`wc -c essay.txt`]{#wc-bytes-essay explanation="`-c` 옵션은 공백으로 구분된 단어가 아니라 바이트를 보고합니다."}
:::

:::single-choice{#wc-characters-not-bytes} 현재 로캘에서 바이트가 아니라 문자를 세도록 `wc`에 요청하는 옵션은 무엇인가요?

::option[`-m`]{#wc-character-option .correct explanation="`-m` 옵션은 문자를 보고하며 멀티바이트 텍스트에서는 바이트 수와 다를 수 있습니다."}
::option[`-c`]{#wc-byte-option explanation="`-c` 옵션은 바이트를 보고합니다. UTF-8 같은 인코딩에서는 문자 하나가 여러 바이트를 차지할 수 있습니다."}
::option[`-w`]{#wc-word-option explanation="`-w` 옵션은 문자나 바이트가 아니라 단어를 셉니다."}
:::

여러 파일을 지정하면 `wc`는 파일마다 결과 하나를 출력하고 `total` 줄을 추가합니다. GNU `wc -L`은 입력 줄의 최대 표시 너비를 보고합니다.

## nl로 비어 있지 않은 줄에 번호 붙이기

기본적으로 `nl`은 입력의 논리적 본문에서 비어 있지 않은 줄에 번호를 붙입니다. `notes.txt`의 두 번째 줄이 비어 있다고 가정합니다.

```text
alpha

beta
```

빈 줄은 유지되지만 번호를 받지 않습니다.

```bash
$ nl notes.txt
	 1	alpha

	 2	beta
```

`nl`은 번호가 붙은 출력을 쓰며 `notes.txt`를 수정하지 않습니다.

:::single-choice{#nl-default-blank-lines} 기본적으로 `nl notes.txt`는 빈 본문 줄을 어떻게 처리하나요?

::option[각 빈 줄을 출력에서 완전히 생략합니다.]{#nl-omit-blank explanation="빈 줄은 출력에 남지만 기본적으로 번호를 받지 않습니다."}
::option[번호 없이 그대로 유지합니다.]{#nl-preserve-unnumbered .correct explanation="기본 본문 스타일은 비어 있지 않은 줄에 번호를 붙이고 빈 줄은 번호 없이 통과시킵니다."}
::option[비어 있지 않은 줄과 같은 순서로 번호를 붙입니다.]{#nl-number-blank-default explanation="모든 본문 줄에 번호를 붙이려면 `-ba` 같은 다른 스타일이 필요합니다."}
:::

## 모든 줄에 번호 붙이기

모든 줄에 번호를 붙이는 본문 번호 스타일 `a`를 선택하려면 `-ba`를 사용합니다.

```bash
$ nl -ba notes.txt
	 1	alpha
	 2
	 3	beta
```

다른 옵션으로 서식을 제어할 수 있습니다. 예를 들어 `-w 3`은 번호 필드 너비를 정하고 `-s ': '`는 번호 뒤의 구분 기호를 바꿉니다.

:::single-choice{#nl-number-all-lines} 빈 줄을 포함해 `notes.txt`의 모든 본문 줄에 번호를 붙이는 명령어는 무엇인가요?

::option[`nl -w 3 notes.txt`]{#nl-width-three explanation="번호 필드 너비를 바꾸지만 기본적인 비어 있지 않은 줄 번호 규칙은 유지합니다."}
::option[`nl -ba notes.txt`]{#nl-body-all .correct explanation="`-b` 옵션은 본문 스타일을 선택하고 스타일 `a`는 모든 본문 줄에 번호를 붙입니다."}
::option[`wc -l notes.txt`]{#wc-lines-notes explanation="줄 바꿈 문자 수를 출력하며 파일을 줄 번호와 함께 다시 출력하지 않습니다."}
:::

텍스트 계산과 줄 번호 붙이기를 연습하려면 다음 실습을 진행해 보세요.

1. **[Linux wc 명령어: 텍스트 계산](https://labex.io/ko/labs/linux-linux-wc-command-text-counting-219200)** - `wc`로 텍스트 파일의 단어, 줄, 문자를 세는 방법을 연습합니다.
2. **[Linux nl 명령어: 줄 번호 붙이기](https://labex.io/ko/labs/linux-linux-nl-command-line-numbering-210988)** - `nl`로 텍스트 파일의 줄에 번호를 붙이는 방법을 배웁니다.
3. **[단어 수 세기와 정렬](https://labex.io/ko/labs/linux-word-count-and-sorting-388125)** - `wc`로 줄, 단어, 문자를 세고 정렬과 결합해 텍스트를 분석합니다.

## 요약

이제 원본을 편집하지 않고 텍스트 스트림을 측정하고 눈에 보이는 줄 번호를 추가할 수 있습니다.

1. `wc`의 기본 줄, 단어, 바이트 열을 해석할 수 있습니다.
2. `-l`, `-w`, `-c`, `-m`으로 한 가지 개수를 선택할 수 있습니다.
3. 바이트 수와 문자 수를 구분할 수 있습니다.
4. 기본 `nl` 동작으로 비어 있지 않은 줄에 번호를 붙일 수 있습니다.
5. `nl -ba`로 빈 줄에도 번호를 붙일 수 있습니다.
