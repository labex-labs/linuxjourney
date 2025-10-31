---
index: 14
lang: "ko"
title: "uniq (고유)"
meta_title: "uniq (고유) - Text-Fu"
meta_description: "Linux 에서 uniq 명령어를 사용하여 텍스트에서 인접한 중복 줄을 필터링하고 제거하는 방법을 알아보세요. -c, -u, -d 와 같은 옵션과 함께 uniq 리눅스 도구를 사용하는 방법과 강력한 텍스트 처리를 위해 sort 와 결합하는 방법을 학습합니다."
meta_keywords: "uniq 명령어, 리눅스 uniq, uniq linux, 중복 제거, sort uniq, 텍스트 처리, 데이터 정리, 리눅스 튜토리얼"
---

## Lesson Content

uniq (고유) 명령어는 Linux 텍스트 처리에서 필수적인 도구입니다. 텍스트 파일 내의 중복 줄을 필터링하고 관리하는 데 도움이 되지만, 효과적으로 사용하려면 작동 방식을 이해하는 것이 중요합니다.

### 기본 중복 제거

`uniq` 명령어의 주요 기능은 인접한 중복 줄을 제거하는 것입니다. `reading.txt`라는 파일에 다음과 같은 내용이 있다고 상상해 보세요.

```plaintext
book
book
paper
paper
article
article
magazine
```

반복되는 줄을 제거하려면 `uniq` 명령을 실행할 수 있습니다.

```bash
$ uniq reading.txt
book
paper
article
magazine
```

보시다시피 `uniq`는 인접한 중복 줄이 제거된 파일 버전을 출력합니다.

### 고급 필터링 옵션

`uniq` 명령어는 더 자세한 분석을 위한 몇 가지 옵션도 제공합니다.

각 줄의 발생 횟수를 세려면 `-c` (count) 플래그를 사용합니다.

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

반복되지 않는 줄 (즉, 고유한 줄) 만 표시하려면 `-u` (unique) 플래그를 사용합니다.

```bash
$ uniq -u reading.txt
magazine
```

반대로, 반복되는 줄만 표시하려면 `-d` (duplicated) 플래그를 사용합니다.

```bash
$ uniq -d reading.txt
book
paper
article
```

### 정렬의 중요성

**uniq linux** 명령어에 대한 중요한 세부 사항은 중복된 줄이 서로 인접해 있는 경우에만 중복을 감지한다는 것입니다. 중복이 파일 전체에 흩어져 있으면 `uniq`는 이를 식별하지 못합니다.

중복이 인접하지 않은 `reading.txt`의 버전을 고려해 보세요.

```plaintext
book
paper
book
paper
article
magazine
article
```

이 파일에 `uniq`를 실행하면 놀라운 결과가 나옵니다.

```bash
$ uniq reading.txt
book
paper
book
paper
article
magazine
article
```

서로 바로 옆에 동일한 줄이 없었기 때문에 줄이 제거되지 않았습니다. 이 문제를 해결하려면 먼저 파일 내용을 정렬해야 합니다. `sort`의 출력을 `uniq`로 파이프하면 모든 동일한 줄이 인접하게 되어 `uniq`가 올바르게 작동하도록 보장합니다. 이 조합은 셸 스크립팅에서 강력하고 일반적인 패턴입니다.

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

이 명령어는 먼저 줄을 알파벳순으로 정렬한 다음 `uniq`가 중복을 필터링하여 정리된 고유 항목 목록을 제공합니다.

## Exercise

연습이 완벽을 만듭니다! `uniq` 및 `sort`를 사용한 텍스트 처리에 대한 이해를 강화하기 위한 몇 가지 실습 랩이 있습니다.

1. **[Linux uniq 명령어: 중복 필터링](https://labex.io/ko/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - Linux `uniq` 명령어를 `sort`와 함께 사용하여 텍스트 파일에서 중복 줄을 식별, 필터링 및 분석하는 방법을 알아봅니다.
2. **[Linux sort 명령어: 텍스트 정렬](https://labex.io/ko/labs/linux-linux-sort-command-text-sorting-219196)** - `sort` 명령어를 사용하여 텍스트 파일의 줄을 구성하는 방법을 연습합니다. 이는 `uniq`를 효과적으로 사용하기 위한 중요한 단계입니다.
3. **[단어 수 및 정렬](https://labex.io/ko/labs/linux-word-count-and-sorting-388125)** - 이 실습 과제에서 필수적인 Linux 텍스트 처리 도구인 `wc`(단어 수) 및 `sort`를 배웁니다. 줄, 단어 및 문자를 세고, 빈번한 패턴을 찾고, 다양한 텍스트 분석 작업을 위해 데이터를 효율적으로 정렬하는 방법을 배웁니다.

이러한 랩은 실제 시나리오에서 개념을 적용하고 Linux 에서 텍스트 처리 및 데이터 조작에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

파일에서 인접한 중복 줄을 제거하려면 어떤 명령어를 사용해야 합니까? 답변은 소문자 영어 알파벳으로 된 명령어 이름만 사용하십시오.

## Quiz Answer

uniq
