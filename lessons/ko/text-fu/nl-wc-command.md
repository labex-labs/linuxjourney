---
index: 15
lang: "ko"
title: "wc 및 nl"
meta_title: "wc 및 nl - 텍스트 처리"
meta_description: "wc 및 nl Linux 명령어를 배우세요. 단어 수 세기, 줄 번호 매기기, 파일 분석을 이해하세요. 오늘 Linux 명령줄 기술을 향상시키세요!"
meta_keywords: "wc 명령어, nl 명령어, Linux 단어 수 세기, Linux 줄 번호, 파일 분석, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

`wc` (word count) 명령어는 파일의 총 단어 수를 보여줍니다.

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

이 명령어는 각각 줄 수, 단어 수, 바이트 수를 표시합니다.

특정 필드의 개수만 보려면 각각 `-l`, `-w`, 또는 `-c` 옵션을 사용합니다.

```bash
$ wc -l /etc/passwd
96
```

파일의 줄 수를 확인하는 데 사용할 수 있는 또 다른 명령어는 `nl` (number lines) 명령어입니다.

```plaintext
file1.txt
i
like
turtles
```

```bash
$ nl file1.txt
1. i
2. like
3. turtles
```

## Exercise

연습은 완벽을 만듭니다! 다음은 Linux 에서 텍스트 개수 세기 및 줄 번호 매기기에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux wc 명령어: 텍스트 개수 세기](https://labex.io/ko/labs/linux-linux-wc-command-text-counting-219200)** - `wc` 명령어를 사용하여 텍스트 파일의 단어, 줄, 문자 수를 세는 연습을 합니다.
2. **[Linux nl 명령어: 줄 번호 매기기](https://labex.io/ko/labs/linux-linux-nl-command-line-numbering-210988)** - `nl` 명령어를 사용하여 텍스트 파일에 줄 번호를 매기는 방법을 배웁니다.
3. **[단어 개수 세기 및 정렬](https://labex.io/ko/labs/linux-word-count-and-sorting-388125)** - `wc` 지식을 적용하여 줄, 단어, 문자 수를 세고, 실용적인 텍스트 분석 작업을 위해 정렬과 결합합니다.

이 랩들은 실제 시나리오에 개념을 적용하고 Linux 에서 텍스트 처리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

파일의 총 단어 수와 단어만 얻으려면 어떤 명령어를 사용하시겠습니까?

## Quiz Answer

wc -w
