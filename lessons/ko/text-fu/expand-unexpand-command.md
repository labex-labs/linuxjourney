---
index: 10
lang: "ko"
title: "expand 및 unexpand"
meta_title: "expand 및 unexpand - Text-Fu"
meta_description: "`expand` 명령으로 탭을 공백으로, `unexpand` 명령으로 공백을 탭으로 변환하는 방법을 배웁니다. 이 Linux 튜토리얼을 통해 텍스트 파일 서식을 개선하세요."
meta_keywords: "expand command, unexpand command, Linux 탭, Linux 공백, 텍스트 서식, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

`cut` 명령에 대한 수업에서, 우리는 탭을 포함하는 `sample.txt` 파일을 가지고 있었습니다. 일반적으로 탭은 눈에 띄는 차이를 보여주지만, 일부 텍스트 파일은 충분히 잘 보여주지 못합니다. 텍스트 파일에 탭이 있으면 원하는 간격을 제공하지 못할 수 있습니다. 탭을 공백으로 변경하려면 `expand` 명령을 사용하십시오.

```bash
expand sample.txt
```

위 명령은 각 탭이 공백 그룹으로 변환된 출력을 인쇄합니다. 이 출력을 파일에 저장하려면 아래와 같이 출력 리디렉션을 사용하십시오.

```bash
expand sample.txt > result.txt
```

`expand`와 반대로, `unexpand` 명령을 사용하여 각 공백 그룹을 다시 탭으로 변환할 수 있습니다:

```bash
unexpand -a result.txt
```

## Exercise

파일 입력 없이 `expand`만 입력하면 어떻게 될까요?

## Quiz Question

탭을 공백으로 변환하는 데 사용되는 명령은 무엇입니까?

## Quiz Answer

expand
