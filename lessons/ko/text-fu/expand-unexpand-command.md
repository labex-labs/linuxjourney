---
index: 10
lang: "ko"
title: "expand 및 unexpand"
meta_title: "expand 및 unexpand - 텍스트 조작"
meta_description: "`expand` 명령으로 탭을 공백으로 변환하고 `unexpand` 명령으로 공백을 탭으로 변환하는 방법을 배우십시오. 이 Linux 튜토리얼로 텍스트 파일 서식을 개선하십시오."
meta_keywords: "expand command, unexpand command, Linux 탭, Linux 공백, 텍스트 서식, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

`cut` 명령에 대한 수업에서 탭을 포함하는 `sample.txt` 파일이 있었습니다. 일반적으로 탭은 눈에 띄는 차이를 보이지만, 일부 텍스트 파일은 충분히 잘 표시되지 않습니다. 텍스트 파일에 탭이 있으면 원하는 간격을 제공하지 못할 수 있습니다. 탭을 공백으로 변경하려면 `expand` 명령을 사용하십시오.

```bash
expand sample.txt
```

위 명령은 각 탭이 공백 그룹으로 변환된 출력을 인쇄합니다. 이 출력을 파일에 저장하려면 아래와 같이 출력 리디렉션을 사용하십시오.

```bash
expand sample.txt > result.txt
```

`expand`와 반대로, `unexpand` 명령을 사용하여 각 공백 그룹을 탭으로 다시 변환할 수 있습니다:

```bash
unexpand -a result.txt
```

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 에서 텍스트 조작 및 리디렉션에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 입력 및 출력 리디렉션](https://labex.io/ko/labs/comptia-redirecting-input-and-output-in-linux-590840)** - `>` 및 `>>`와 같은 연산자를 사용하여 표준 출력 (stdout), 표준 오류 (stderr) 및 표준 입력 (stdin) 을 조작하여 명령의 데이터 흐름을 제어하는 연습을 하십시오.
2. **[간단한 텍스트 처리](https://labex.io/ko/labs/linux-simple-text-processing-18004)** - `tr`, `col`, `join`, `paste`와 같은 강력한 명령을 사용하여 텍스트 데이터를 효율적으로 조작하고 분석하는 방법을 배우고, 데이터 처리를 위한 명령줄 기술을 향상시키십시오.
3. **[텍스트 처리 및 정규 표현식](https://labex.io/ko/labs/linux-text-processing-and-regular-expressions-18003)** - 강력한 텍스트 처리 도구인 `grep`, `sed`, `awk`를 배우고, Linux 에서 효율적인 텍스트 조작 및 패턴 일치를 위해 정규 표현식을 사용하십시오.

이러한 랩은 실제 시나리오에서 텍스트 변환 및 파일 조작 개념을 적용하고 Linux 명령줄 도구에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

탭을 공백으로 변환하는 데 사용되는 명령은 무엇입니까?

## Quiz Answer

expand
