---
index: 12
lang: "ko"
title: "sort"
meta_title: "sort - Text-Fu"
meta_description: "텍스트 파일을 정렬하기 위해 Linux sort 명령을 사용하는 방법을 배우십시오. 역순 및 숫자 정렬과 같은 옵션을 알아보십시오. Linux 명령줄 기술을 향상시키십시오!"
meta_keywords: "Linux sort 명령어, sort -r, sort -n, Linux 튜토리얼, 명령줄, 초보자 Linux, sort 가이드"
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

또한 숫자 값으로 정렬할 수도 있습니다:

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

`sort`의 진정한 힘은 다른 명령과 결합할 수 있는 능력에서 나옵니다. 다음 명령을 시도하고 어떤 일이 발생하는지 확인하십시오:

```bash
ls /etc | sort -rn
```

## Quiz Question

역순 정렬을 수행하기 위해 어떤 플래그를 사용합니까?

## Quiz Answer

-r
