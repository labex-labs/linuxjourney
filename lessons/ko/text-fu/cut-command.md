---
title: "cut"
description: "Linux `cut` 명령어를 사용하여 파일에서 텍스트를 추출하는 방법을 배웁니다. 이 초보자 친화적인 튜토리얼은 문자 및 필드 자르기를 다룹니다. Linux 텍스트 처리 기술을 향상시키세요!"
keywords: "cut 명령어, Linux 텍스트 처리, 텍스트 추출, Linux 튜토리얼, 초보자 Linux, cut 예제, Linux 가이드"
---

## Lesson Content

텍스트를 처리하는 데 사용할 수 있는 몇 가지 유용한 명령어를 배울 것입니다. 시작하기 전에 작업할 파일을 만들어 봅시다. 다음 명령어를 복사하여 붙여넣으세요. 그 후, "lazy"와 "dog" 사이에 TAB을 추가하세요 (Ctrl-v + TAB을 누르세요).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

우리가 배울 첫 번째 명령어는 `cut` 명령어입니다. 이 명령어는 파일에서 텍스트의 일부를 추출합니다.

문자 목록으로 내용을 추출하려면:

```bash
cut -c 5 sample.txt
```

이것은 파일의 각 줄에서 5번째 문자를 출력합니다. 이 경우, "q"입니다. 공백도 문자로 계산된다는 점에 유의하세요.

필드로 내용을 추출하려면 약간의 수정이 필요합니다:

```bash
cut -f 2 sample.txt
```

`-f` 또는 field 플래그는 필드를 기반으로 텍스트를 자릅니다. 기본적으로 TAB을 구분 기호로 사용하므로 TAB으로 구분된 모든 것은 필드로 간주됩니다. 출력으로 "dog"를 볼 수 있을 것입니다.

필드 플래그를 구분 기호 플래그와 결합하여 사용자 지정 구분 기호로 내용을 추출할 수 있습니다:

```bash
cut -f 1 -d ";" sample.txt
```

이것은 TAB 구분 기호를 ";" 구분 기호로 변경하며, 첫 번째 필드를 자르기 때문에 결과는 "The quick brown"이 될 것입니다.

## Exercise

What does the following command do? Why?

```bash
cut -c 5-10 sample.txt
cut -c 5- sample.txt
cut -c -5 sample.txt
```

## Quiz Question

파일의 각 줄에서 첫 번째 문자를 얻으려면 어떤 명령어를 사용하시겠습니까?

## Quiz Answer

cut -c 1
