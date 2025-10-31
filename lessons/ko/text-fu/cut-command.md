---
index: 6
lang: "ko"
title: "자르기"
meta_title: "cut - 텍스트 도구"
meta_description: "Linux `cut` 명령어를 사용하여 파일에서 특정 텍스트 섹션을 추출하는 방법을 알아보세요. 이 가이드는 문자 및 필드 (`cut f`) 로 자르는 방법을 다루며, 사용자 지정 구분 기호로 f 를 자르는 방법도 포함합니다. Linux 텍스트 처리를 마스터하는 데 적합합니다."
meta_keywords: "cut 명령어, Linux 텍스트 처리, 텍스트 추출, cut f, f 자르는 방법, Linux 튜토리얼, cut 예제, Linux 가이드, 필드 자르기"
---

## Lesson Content

이제 텍스트 처리에 유용한 몇 가지 명령어를 배워보겠습니다. 시작하기 전에, 실습할 파일을 생성해 보겠습니다. 다음 명령어를 복사하여 붙여넣으세요. 붙여넣은 후, "lazy"와 "dog" 사이에 리터럴 TAB 문자를 추가해야 합니다 (종종 Ctrl-v 를 누른 다음 TAB 을 눌러 수행할 수 있습니다).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

우리가 탐구할 첫 번째 명령어는 파일에서 텍스트 부분을 추출하는 `cut`입니다.

### 문자로 자르기 (Cutting by Character)

`-c` 플래그를 사용하여 문자 위치를 기준으로 내용을 추출할 수 있습니다.

```bash
cut -c 5 sample.txt
```

이 명령어는 파일의 각 줄에서 5 번째 문자를 출력합니다. 이 경우 출력은 "q"입니다. 공백도 문자로 계산된다는 점에 유의하세요.

### cut f 를 사용한 필드별 자르기 (Cutting by Field with cut f)

더 강력한 기능은 필드별로 자르는 것입니다. `-f` 플래그를 사용하는 `cut f` 구문은 필드 위치를 기준으로 텍스트를 추출할 수 있게 해줍니다. 기본적으로 `cut`은 TAB 문자를 구분 기호로 사용하므로, TAB 으로 구분된 모든 것이 별도의 필드로 간주됩니다.

필드를 기준으로 f 를 자르는 방법을 살펴보겠습니다.

```bash
cut -f 2 sample.txt
```

"lazy"와 "dog" 사이에 TAB 을 삽입했으므로, 이 명령어는 "dog"를 두 번째 필드로 처리합니다. 출력은 "dog"여야 합니다.

### 사용자 지정 구분 기호 사용 (Using Custom Delimiters)

필드 플래그를 구분 기호 플래그 (`-d`) 와 결합하여 사용자 지정 구분 기호를 지정할 수도 있습니다. 이는 쉼표나 세미콜론과 같은 문자로 데이터를 구분하는 파일을 다룰 때 유용합니다.

```bash
cut -f 1 -d ";" sample.txt
```

이 명령어는 구분 기호를 TAB 에서 세미콜론 (";") 으로 변경합니다. 첫 번째 필드 (`-f 1`) 를 자르고 있으므로 결과는 "The quick brown"이 됩니다.

## Exercise

연습이 완벽을 만듭니다! `cut` 및 기타 관련 명령어를 사용한 텍스트 처리 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[Linux cut 명령어: 텍스트 자르기](https://labex.io/ko/labs/linux-linux-cut-command-text-cutting-219187)** - 이 랩은 `cut` 명령어에 대한 직접적인 실습 소개를 제공하여, 강의에서 논의된 것처럼 텍스트 파일에서 특정 열 또는 필드를 추출하는 연습을 할 수 있게 합니다.
2. **[간단한 텍스트 처리](https://labex.io/ko/labs/linux-simple-text-processing-18004)** - `tr`, `col`, `join`, `paste`와 같은 강력한 명령어를 사용하여 텍스트 데이터를 효율적으로 처리하고 분석함으로써 텍스트 조작 기술을 확장하세요.
3. **[시퀀스 제어 및 파이프라인](https://labex.io/ko/labs/linux-sequence-control-and-pipeline-17994)** - 명령 실행 시퀀스를 제어하고, 파이프라인을 활용하며, `cut`, `grep`, `wc`, `sort`, `uniq`와 같은 강력한 텍스트 처리 도구를 활용하여 명령줄 효율성을 향상시키세요.

이 랩들은 실제 시나리오에서 개념을 적용하고 Linux 텍스트 처리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

파일의 모든 줄에서 첫 번째 문자를 가져오려면 어떤 명령어를 사용해야 합니까?

## Quiz Answer

cut -c 1
