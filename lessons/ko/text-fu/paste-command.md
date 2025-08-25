---
index: 7
lang: "ko"
title: "paste"
meta_title: "paste - 텍스트 처리 기술"
meta_description: "Linux paste 명령어를 사용하여 파일 줄을 병합하는 방법을 배웁니다. 이 필수 Linux 명령어 튜토리얼을 통해 구분 기호를 발견하고 파일을 결합하세요."
meta_keywords: "Linux paste 명령어, paste 명령어 튜토리얼, 파일 줄 병합, Linux 명령어, 초보자 Linux, Linux 가이드"
---

## Lesson Content

`paste` 명령어는 `cat` 명령어와 유사합니다. 파일의 줄을 함께 병합합니다. 다음 내용을 포함하는 새 파일을 만들어 보겠습니다:

```
sample2.txt
The
quick
brown
fox
```

이 모든 줄을 한 줄로 결합해 보겠습니다:

```bash
paste -s sample2.txt
```

`paste`의 기본 구분 기호는 TAB 이므로, 이제 각 단어가 TAB 으로 구분된 한 줄이 됩니다.

이 구분 기호 (`-d`) 를 좀 더 읽기 쉬운 것으로 변경해 보겠습니다:

```bash
paste -d ' ' -s sample2.txt
```

이제 모든 것이 공백으로 구분되어 한 줄에 표시되어야 합니다.

## Exercise

연습하면 완벽해집니다! 다음은 Linux 에서 텍스트 처리 및 데이터 조작에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[간단한 텍스트 처리](https://labex.io/ko/labs/linux-simple-text-processing-18004)** - `tr`, `col`, `join`, `paste`와 같은 강력한 명령어를 사용하여 텍스트 데이터를 효율적으로 조작하고 분석하는 방법을 배웁니다.
2. **[데이터 스트림 리디렉션](https://labex.io/ko/labs/linux-data-stream-redirection-17995)** - Linux 스트림 리디렉션 기술과 표준 입력, 출력 및 오류 스트림을 조작하는 방법을 배웁니다. 이는 `paste`와 같은 명령어가 작동하는 방식을 이해하는 데 필수적입니다.
3. **[시퀀스 제어 및 파이프라인](https://labex.io/ko/labs/linux-sequence-control-and-pipeline-17994)** - 명령어 실행 시퀀스를 제어하고 파이프라인을 활용하는 방법을 배웁니다. 이를 통해 `paste`를 다른 명령어와 결합하여 복잡한 데이터 작업을 수행하는 능력을 향상시킬 수 있습니다.

이러한 랩은 실제 시나리오에 개념을 적용하고 Linux 에서 텍스트 처리 및 데이터 처리 능력을 구축하는 데 도움이 될 것입니다.

## Quiz Question

`paste`와 함께 사용하여 모든 내용을 한 줄로 만드는 데 사용하는 플래그는 무엇입니까?

## Quiz Answer

-s
