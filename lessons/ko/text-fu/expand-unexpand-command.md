---
index: 10
lang: "ko"
title: "확장 및 축소"
meta_title: "확장 및 축소 - Text-Fu"
meta_description: "expand 및 unexpand 명령 가이드를 통해 Linux 텍스트 서식을 마스터하세요. 일관된 파일 레이아웃을 위해 탭을 공백으로, 공백을 다시 탭으로 변환하는 방법을 배웁니다."
meta_keywords: "expand 명령어, unexpand 명령어, 리눅스 탭, 리눅스 공백, 텍스트 서식, 리눅스 튜토리얼, 초보 리눅스, 리눅스 가이드"
---

## Lesson Content

일관성 없는 공백은 텍스트 파일을 읽기 어렵게 만들 수 있습니다. 탭은 균일한 들여쓰기를 위해 고안되었지만, 편집기나 시스템에 따라 표시 너비가 다를 수 있습니다. 이는 텍스트 서식 및 정렬을 방해할 수 있습니다. 다행히 Linux 는 탭과 공백 간의 변환을 통해 이를 관리할 수 있는 간단한 도구를 제공합니다. 이 초보자용 Linux 가이드에서는 그 과정을 안내합니다.

### expand 명령을 사용하여 탭을 공백으로 변환하기

일관된 공백이 필요할 때, `expand` 명령을 사용하여 탭을 표준 개수의 공백으로 변환할 수 있습니다. 이 명령은 파일을 읽고 각 탭 문자를 일련의 공백 문자로 대체하여 결과를 표준 출력으로 인쇄합니다.

```bash
expand sample.txt
```

기본적으로 `expand command`는 각 탭을 8 개의 공백으로 변환합니다. 이 간단한 유틸리티는 텍스트 서식을 개선하는 강력한 도구입니다.

### 변환된 출력 저장하기

`expand` 명령은 변환된 텍스트를 터미널에만 인쇄합니다. 변경 사항을 저장하려면 출력을 새 파일로 리디렉션해야 합니다.

```bash
expand sample.txt > result.txt
```

이 명령은 `expand sample.txt`의 출력을 `result.txt`에 기록하여 탭 대신 공백이 포함된 새 파일을 제공합니다.

### unexpand 명령을 사용하여 공백을 탭으로 변환하기

반대 작업, 즉 공백을 다시 탭으로 변환하는 작업은 `unexpand` 명령으로 처리됩니다. 이는 파일 크기를 줄이거나 탭을 요구하는 코딩 표준을 준수해야 할 때 유용할 수 있습니다.

```bash
unexpand -a result.txt
```

기본적으로 `unexpand`는 각 줄의 선행 공백만 변환합니다. `-a` 옵션은 `unexpand command`에게 줄 시작 부분에 있는 공백뿐만 아니라 8 개의 공백이 일치하는 모든 인스턴스를 탭으로 변환하도록 지시하여 Linux 공백 및 탭에 대한 보다 포괄적인 제어 기능을 제공합니다.

## Exercise

Linux 에서 텍스트 조작 및 리디렉션을 마스터하려면 연습이 중요합니다. 다음 실습 랩은 이해도를 높이는 데 도움이 될 것입니다.

1.  **[Linux 에서 입력 및 출력 리디렉션](https://labex.io/ko/labs/comptia-redirecting-input-and-output-in-linux-590840)** - `>` 및 `>>`와 같은 연산자를 사용하여 표준 출력 (stdout), 표준 오류 (stderr), 표준 입력 (stdin) 을 조작하여 명령의 데이터 흐름을 제어하는 연습을 합니다.
2.  **[간단한 텍스트 처리](https://labex.io/ko/labs/linux-simple-text-processing-18004)** - 데이터 처리를 위한 명령줄 기술을 향상시키기 위해 `tr`, `col`, `join`, `paste`와 같은 강력한 명령을 사용하여 텍스트 데이터를 효율적으로 조작하고 분석하는 방법을 배웁니다.
3.  **[텍스트 처리 및 정규 표현식](https://labex.io/ko/labs/linux-text-processing-and-regular-expressions-18003)** - Linux 에서 효율적인 텍스트 조작 및 패턴 일치를 위해 강력한 텍스트 처리 도구인 `grep`, `sed`, `awk`를 배우고 정규 표현식을 사용합니다.

이러한 랩을 완료하면 텍스트 변환 및 파일 조작 개념을 실제 시나리오에 적용하는 데 도움이 되며, 필수적인 Linux 명령줄 도구에 대한 자신감을 쌓을 수 있습니다.

## Quiz Question

탭을 공백으로 변환하는 데 사용되는 명령은 무엇입니까? (소문자 영어 명령 이름을 사용하여 답변하십시오.)

## Quiz Answer

expand
