---
index: 14
lang: "ko"
title: "uniq (고유)"
meta_title: "uniq (고유) - 텍스트 처리"
meta_description: "Linux `uniq` 명령어를 사용하여 텍스트 파일에서 중복 줄을 제거하는 방법을 배웁니다. -c, -u, -d 와 같은 옵션을 알아보고 `sort`와 결합하여 효과적인 데이터 정리를 수행합니다."
meta_keywords: "uniq 명령어, Linux uniq, 중복 제거, sort uniq, Linux 튜토리얼, 텍스트 처리, 초보자 Linux, Linux 가이드"
---

## Lesson Content

`uniq` (unique) 명령어는 텍스트를 구문 분석하는 데 유용한 또 다른 도구입니다.

중복이 많은 파일이 있다고 가정해 봅시다:

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

그리고 중복을 제거하고 싶다면 `uniq` 명령어를 사용할 수 있습니다:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

줄의 발생 횟수를 세어 봅시다:

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

중복 값만 가져와 봅시다:

```bash
$ uniq -d reading.txt
book
paper
article
```

**참고**: `uniq`는 인접한 줄이 아니면 중복을 감지하지 못합니다. 예를 들어:

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

`uniq`가 반환하는 결과는 첫 번째 예제와 달리 모든 항목을 포함합니다.

`uniq`의 이러한 한계를 극복하기 위해 `sort`와 `uniq`를 함께 사용할 수 있습니다:

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

## Exercise

연습하면 완벽해집니다! 다음은 `uniq` 및 `sort`를 사용한 텍스트 처리 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux uniq Command: Duplicate Filtering](https://labex.io/ko/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - 텍스트 파일에서 중복 줄을 식별, 필터링 및 분석하기 위해 Linux `uniq` 명령어를 `sort`와 함께 사용하는 방법을 배웁니다.
2. **[Linux sort Command: Text Sorting](https://labex.io/ko/labs/linux-linux-sort-command-text-sorting-219196)** - `uniq`를 효과적으로 사용하기 전에 중요한 단계인 텍스트 파일의 줄을 정렬하기 위해 `sort` 명령어를 사용하는 연습을 합니다.
3. **[Word Count and Sorting](https://labex.io/ko/labs/linux-word-count-and-sorting-388125)** - 이 실습 챌린지에서 필수적인 Linux 텍스트 처리 도구인 `wc` (단어 수) 와 `sort`를 배웁니다. 다양한 텍스트 분석 작업을 위해 줄, 단어, 문자를 세고, 빈번한 패턴을 찾고, 데이터를 효율적으로 정렬하는 방법을 배웁니다.

이 랩들은 실제 시나리오에 개념을 적용하고 Linux 에서 텍스트 처리 및 데이터 조작에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

파일에서 중복을 제거하려면 어떤 명령을 사용하시겠습니까?

## Quiz Answer

uniq
