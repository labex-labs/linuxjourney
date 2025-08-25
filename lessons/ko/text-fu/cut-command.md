---
index: 6
lang: "ko"
title: "cut"
meta_title: "cut - 텍스트 처리"
meta_description: "Linux `cut` 명령어를 사용하여 파일에서 텍스트를 추출하는 방법을 배우세요. 이 초보자 친화적인 튜토리얼은 문자 및 필드 자르기를 다룹니다. Linux 텍스트 처리 기술을 향상시키세요!"
meta_keywords: "cut 명령어, Linux 텍스트 처리, 텍스트 추출, Linux 튜토리얼, 초보자 Linux, cut 예제, Linux 가이드"
---

## Lesson Content

텍스트를 처리하는 데 사용할 수 있는 몇 가지 유용한 명령어를 배울 것입니다. 시작하기 전에 작업할 파일을 만들어 봅시다. 다음 명령어를 복사하여 붙여넣으세요. 그런 다음 "lazy"와 "dog" 사이에 TAB 을 추가하세요 (Ctrl-v + TAB 을 누르세요).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

우리가 배울 첫 번째 명령어는 `cut` 명령어입니다. 이 명령어는 파일에서 텍스트의 일부를 추출합니다.

문자 목록으로 내용을 추출하려면:

```bash
cut -c 5 sample.txt
```

이것은 파일의 각 줄에서 5 번째 문자를 출력합니다. 이 경우 "q"입니다. 공백도 문자로 계산된다는 점에 유의하세요.

필드로 내용을 추출하려면 약간의 수정이 필요합니다:

```bash
cut -f 2 sample.txt
```

`-f` 또는 필드 플래그는 필드를 기반으로 텍스트를 자릅니다. 기본적으로 TAB 을 구분 기호로 사용하므로 TAB 으로 구분된 모든 것이 필드로 간주됩니다. 출력으로 "dog"가 표시되어야 합니다.

필드 플래그를 구분 기호 플래그와 결합하여 사용자 지정 구분 기호로 내용을 추출할 수 있습니다:

```bash
cut -f 1 -d ";" sample.txt
```

이렇게 하면 TAB 구분 기호가 ";" 구분 기호로 변경되고, 첫 번째 필드를 자르기 때문에 결과는 "The quick brown"이 됩니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 `cut` 및 기타 관련 명령어를 사용하여 텍스트 처리에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux cut 명령어: 텍스트 자르기](https://labex.io/ko/labs/linux-linux-cut-command-text-cutting-219187)** - 이 랩은 `cut` 명령어에 대한 직접적이고 실용적인 소개를 제공하여, 수업에서 논의된 대로 텍스트 파일에서 특정 열 또는 필드를 추출하는 연습을 할 수 있도록 합니다.
2. **[간단한 텍스트 처리](https://labex.io/ko/labs/linux-simple-text-processing-18004)** - `tr`, `col`, `join`, `paste`와 같은 강력한 명령어를 사용하여 텍스트 데이터를 효율적으로 처리하고 분석함으로써 텍스트 조작 기술을 확장하세요.
3. **[시퀀스 제어 및 파이프라인](https://labex.io/ko/labs/linux-sequence-control-and-pipeline-17994)** - 명령어 실행 시퀀스를 제어하고, 파이프라인을 활용하며, `cut`, `grep`, `wc`, `sort`, `uniq`와 같은 강력한 텍스트 처리 도구를 활용하는 방법을 학습하여 명령줄 효율성을 향상시키세요.

이 랩들은 실제 시나리오에 개념을 적용하고 Linux 에서 텍스트 처리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

파일의 각 줄에서 첫 번째 문자를 얻으려면 어떤 명령어를 사용해야 합니까?

## Quiz Answer

cut -c 1
