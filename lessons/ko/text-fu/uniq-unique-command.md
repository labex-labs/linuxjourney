---
lang: "ko"
title: "uniq (고유)"
description: "Linux `uniq` 명령어를 사용하여 텍스트 파일에서 중복된 줄을 제거하는 방법을 배웁니다. -c, -u, -d 와 같은 옵션을 알아보고, `sort`와 결합하여 효과적인 데이터 정리를 수행하는 방법을 알아봅니다."
keywords: "uniq 명령어, Linux uniq, 중복 제거, sort uniq, Linux 튜토리얼, 텍스트 처리, 초보자 Linux, Linux 가이드"
---

## Lesson Content

`uniq` (unique) 명령어는 텍스트를 파싱하는 데 유용한 또 다른 도구입니다.

중복된 내용이 많은 파일이 있다고 가정해 봅시다:

```plaintext
reading.txt
book
book
paper
paper
article
article
magazine
```

그리고 중복을 제거하고 싶다면, `uniq` 명령어를 사용할 수 있습니다:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

각 줄의 발생 횟수를 세어 봅시다:

```bash
$ uniq -c reading.txt
2 book
2 paper
2 article
1 magazine
```

고유한 값만 가져와 봅시다:

```bash
$ uniq -u reading.txt
magazine
```

중복된 값만 가져와 봅시다:

```bash
$ uniq -d reading.txt
book
paper
article
```

**참고**: `uniq`는 인접한 줄이 아니면 중복을 감지하지 않습니다. 예를 들어:

인접하지 않은 중복이 있는 파일이 있다고 가정해 봅시다:

```plaintext
reading.txt
book
paper
book
paper
article
magazine
article
```

```bash
$ uniq reading.txt
reading.txt
book
paper
book
paper
article
magazine
article
```

`uniq`가 반환하는 결과는 첫 번째 예시와 달리 모든 항목을 포함할 것입니다.

`uniq`의 이러한 한계를 극복하기 위해 `sort`와 `uniq`를 함께 사용할 수 있습니다:

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

## Exercise

`uniq -uc`를 시도하면 어떤 결과를 얻을 수 있을까요?

## Quiz Question

파일에서 중복을 제거하려면 어떤 명령어를 사용해야 할까요?

## Quiz Answer

uniq
