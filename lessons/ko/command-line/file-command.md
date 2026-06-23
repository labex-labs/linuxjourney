---
index: 6
lang: "ko"
title: "file"
meta_title: "file - 명령어"
meta_description: "텍스트 파일, 이미지, 스크립트, 압축 아카이브, 바이너리, MIME 타입을 식별하는 Linux file 명령어를 예제와 함께 배워보세요."
meta_keywords: "linux file 명령어, file 명령어, 리눅스 파일 타입 식별, mime 타입 리눅스, 텍스트 파일, 바이너리 파일, 아카이브 파일"
---

## Lesson Content

이전 강의에서 `touch`에 대해 배웠습니다. 잠시 다시 살펴보겠습니다. 파일 이름이 Windows 같은 다른 운영체제에서 보던 표준 명명 규칙을 따르지 않는다는 것을 눈치채셨나요? 보통 `banana.jpeg`라는 파일은 JPEG 이미지 파일일 것으로 예상합니다.

리눅스에서는 파일 이름이 파일 내용과 일치할 필요가 없습니다. 실제로 GIF가 아닌 `funny.gif`라는 파일을 만들 수도 있습니다.

파일이 어떤 종류인지 알아내려면 `file` 명령어를 사용할 수 있습니다. 이 명령어는 파일 내용에 대한 설명을 보여줍니다.

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

### 파일 확장자만으로는 부족한 이유

리눅스 도구들은 보통 파일 확장자에 의존하지 않고 파일이 무엇인지 판단합니다. 셸 스크립트는 `backup`이라는 이름일 수 있고, 텍스트 파일은 `README`일 수 있으며, 이미지 파일이 잘못된 확장자를 가질 수도 있습니다. `file` 명령어는 파일 내용과 메타데이터를 검사하여 더 정확한 추측을 합니다.

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

### 여러 파일 확인하기

여러 파일을 한 번에 확인할 수 있습니다:

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

와일드카드도 사용할 수 있습니다:

```bash
$ file *
```

### MIME 타입 표시하기

`-i` 옵션은 MIME 스타일 정보를 출력합니다. 웹 파일이나 스크립트를 다룰 때 유용합니다.

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

### 자주 쓰이는 file 옵션

- `-i`: MIME 타입 정보를 보여줍니다.
- `-b`: 간략 모드로, 출력에서 파일 이름을 생략합니다.
- `-L`: 심볼릭 링크를 따라갑니다.
- `-z`: 압축된 파일을 검사하려 시도합니다.

예를 들어:

```bash
$ file -b notes.txt
ASCII text
```

### 자주 묻는 질문

**file 명령어가 확장자만 의존하나요?** 아니요. 주로 파일 내용과 알려진 서명을 검사합니다.

**file 명령어가 틀릴 수 있나요?** 네. 특히 특이하거나 손상된 파일의 경우 추측을 하기 때문에 틀릴 수 있습니다.

**file 명령어가 "data"라고 표시하는 이유는?** 파일이 더 구체적인 알려진 타입과 일치하지 않거나, 인식 가능한 서명이 없는 바이너리 데이터일 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! 파일 내용과 속성 검사를 이해하는 데 도움이 되는 실습 랩을 소개합니다:

1. **[Linux ls 명령어: 내용 목록](https://labex.io/ko/labs/linux-linux-ls-command-content-listing-219205)** - 파일과 디렉터리 내용을 효율적으로 나열하고 분석하는 Linux `ls` 명령어를 배우세요. 이는 디렉터리 내 내용을 이해하기 위해 `file` 명령어를 사용하기 전후에 자주 사용됩니다.
2. **[Linux cat 명령어: 파일 연결](https://labex.io/ko/labs/linux-linux-cat-command-file-concatenating-210986)** - 파일 유형을 확인한 후 텍스트 파일을 보고 조작하는 일반적인 작업을 연습하세요.
3. **[Linux more 명령어: 파일 스크롤링](https://labex.io/ko/labs/linux-linux-more-command-file-scrolling-214299)** - 큰 텍스트 파일을 탐색하고 살펴보는 명령어 기술을 향상시키세요. 파일 유형을 식별하고 내용을 검사하는 능력을 기반으로 합니다.

이 랩들은 실제 상황에서 파일 검사와 내용 보기 개념을 적용하고 리눅스에서 파일을 관리하는 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

파일의 타입을 확인하려면 어떤 명령어를 사용할 수 있나요?

## Quiz Answer

file
