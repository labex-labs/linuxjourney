---
index: 12
lang: "ko"
title: "sort"
meta_title: "sort - 텍스트 조작"
meta_description: "Linux sort 명령을 사용하여 텍스트 파일을 정렬하는 방법을 배우세요. 역순 및 숫자 정렬과 같은 옵션을 알아보세요. Linux 명령줄 기술을 향상시키세요!"
meta_keywords: "Linux sort command, sort -r, sort -n, Linux tutorial, command line, beginner Linux, sort guide"
---

## Lesson Content

`sort` 명령어는 줄을 정렬하는 데 유용합니다.

```plaintext
file1.txt
dog
cow
cat
elephant
bird

$ sort file1.txt
bird
cat
cow
dog
elephant
```

역순으로 정렬할 수도 있습니다:

```bash
$ sort -r file1.txt
elephant
dog
cow
cat
bird
```

그리고 숫자 값으로도 정렬할 수 있습니다:

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

연습하면 완벽해집니다! 다음은 `sort` 명령과 텍스트 처리에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux sort 명령어: 텍스트 정렬](https://labex.io/ko/labs/linux-linux-sort-command-text-sorting-219196)** - 이 실습은 `sort` 명령에 대한 직접적인 소개를 제공하며, 오름차순 및 내림차순을 포함하여 텍스트 파일의 줄을 다양한 방식으로 정렬하는 연습을 할 수 있습니다.
2. **[단어 개수 세기 및 정렬](https://labex.io/ko/labs/linux-word-count-and-sorting-388125)** - 이 챌린지에서는 정렬 지식과 단어 개수 세기를 함께 적용하여 텍스트 데이터를 분석하고, 자주 나타나는 패턴을 찾고 데이터를 효율적으로 정렬하는 데 도움이 됩니다.

이 실습들은 실제 시나리오에 개념을 적용하고 Linux 에서 텍스트 조작 및 정렬에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

역순 정렬을 수행하려면 어떤 플래그를 사용해야 합니까?

## Quiz Answer

-r
