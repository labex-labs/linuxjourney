---
lang: "ko"
title: "paste"
meta_title: "paste - Text-Fu"
meta_description: "Linux paste 명령어를 사용하여 파일 줄을 병합하는 방법을 배웁니다. 이 필수 Linux 명령어 튜토리얼을 통해 구분 기호를 알아보고 파일을 결합하세요."
meta_keywords: "Linux paste 명령어, paste 명령어 튜토리얼, 파일 줄 병합, Linux 명령어, 초보자 Linux, Linux 가이드"
---

## Lesson Content

`paste` 명령어는 `cat` 명령어와 유사하게 파일의 줄을 병합합니다. 다음 내용을 가진 새 파일을 만들어 봅시다:

```
sample2.txt
The
quick
brown
fox
```

이 모든 줄을 한 줄로 결합해 봅시다:

```bash
paste -s sample2.txt
```

`paste`의 기본 구분 기호는 TAB 이므로, 이제 각 단어가 TAB 으로 구분된 한 줄이 됩니다.

이 구분 기호 (`-d`) 를 좀 더 읽기 쉬운 것으로 변경해 봅시다:

```bash
paste -d ' ' -s sample2.txt
```

이제 모든 것이 공백으로 구분되어 한 줄에 표시될 것입니다.

## Exercise

여러 파일을 함께 붙여넣어 보세요. 어떤 일이 발생하나요?

## Quiz Question

`paste` 명령어와 함께 어떤 플래그를 사용하여 모든 내용을 한 줄로 만드나요?

## Quiz Answer

-s
