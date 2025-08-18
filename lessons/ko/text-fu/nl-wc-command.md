---
index: 15
lang: "ko"
title: "wc 및 nl"
meta_title: "wc 및 nl - Text-Fu"
meta_description: "wc 및 nl Linux 명령어를 배우세요. 단어 수 세기, 줄 번호 매기기, 파일 분석을 이해하세요. 오늘 Linux 명령줄 기술을 향상시키세요!"
meta_keywords: "wc 명령어, nl 명령어, Linux 단어 수, Linux 줄 번호, 파일 분석, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
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

파일의 줄 수를 확인할 때 사용할 수 있는 또 다른 명령어는 `nl` (number lines) 명령어입니다.

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

전체 출력을 검색하지 않고 `nl` 명령어를 사용하여 총 줄 수를 어떻게 얻을 수 있을까요? 힌트: 이 과정에서 배운 다른 명령어들을 사용해 보세요.

## Quiz Question

파일의 총 단어 수와 단어만 얻으려면 어떤 명령어를 사용하시겠습니까?

## Quiz Answer

wc -w
