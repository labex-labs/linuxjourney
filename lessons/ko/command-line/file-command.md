---
lesson_id: "file-command"
course_id: "command-line"
lang: "ko"
order_index: 6
title: "file"
description: "이름이나 확장자에 의존하지 않고 파일의 실제 내용 유형을 추정하는 방법을 배웁니다."
meta_title: "file - 명령어"
meta_description: "텍스트 파일, 이미지, 스크립트, 압축 아카이브, 바이너리, MIME 타입을 식별하는 Linux file 명령어를 예제와 함께 배워보세요."
meta_keywords: "linux file 명령어, file 명령어, 리눅스 파일 타입 식별, mime 타입 리눅스, 텍스트 파일, 바이너리 파일, 아카이브 파일"
---

이전 강의에서는 `touch`로 확장자 없는 파일을 만들었습니다. 리눅스 파일 이름은 내용을 설명하지 않아도 됩니다. `funny.gif`라는 파일이 반드시 GIF 이미지인 것은 아닙니다.

파일을 검사해 예상 유형을 확인하려면 `file` 명령어를 사용합니다.

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

## 파일 확장자만으로는 부족한 이유

리눅스 도구들은 보통 파일 확장자에 의존하지 않고 파일이 무엇인지 판단합니다. 셸 스크립트는 `backup`이라는 이름일 수 있고, 텍스트 파일은 `README`일 수 있으며, 이미지 파일이 잘못된 확장자를 가질 수도 있습니다. `file` 명령어는 파일 시스템 메타데이터와 내용에서 알아볼 수 있는 패턴 같은 속성을 검사합니다.

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

그 결과는 분류일 뿐 보장은 아닙니다. 특이하거나 불완전하거나 손상된 파일은 정확한 유형 대신 `data`처럼 넓은 설명으로 표시될 수 있습니다.

:::single-choice{#identify-misleading-extension}
`report.jpg`라는 파일이 이미지가 아닐 수도 있습니다. 실제 내용의 예상 유형을 확인하는 명령어는 무엇인가요?

::option[`ls report.jpg`]{#list-report explanation="`ls`는 이름이 존재하는지 확인하고 메타데이터를 보여 줄 수 있지만 파일 내용을 분류하지는 않습니다."}
::option[`file report.jpg`]{#inspect-report .correct explanation="`file`은 파일을 검사해 예상 유형을 알려 줍니다. `.jpg` 접미사만 보고 판단하지 않습니다."}
::option[`touch report.jpg`]{#touch-report explanation="`touch`는 타임스탬프를 갱신하거나 없는 파일을 만들며 내용 유형을 식별하지 않습니다."}
:::

## 여러 파일 확인하기

여러 파일을 한 번에 확인할 수 있습니다:

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

쉘 와일드카드도 사용할 수 있습니다. 쉘이 `*`를 일치하는 이름들로 확장한 뒤 `file`이 각 파일을 검사합니다.

```bash
$ file *
```

:::single-choice{#inspect-multiple-files}
현재 디렉터리에서 `*`와 일치하는 숨김 항목 이외의 모든 이름을 `file`로 검사하는 명령어는 무엇인가요?

::option[`file *`]{#file-wildcard .correct explanation="쉘이 `*`를 일치하는 숨김 항목 이외의 이름으로 확장하고 `file`이 각 피연산자를 검사합니다."}
::option[`file .`]{#file-current-directory explanation="점 하나는 현재 디렉터리 자체를 가리키므로 내부의 각 항목이 아니라 그 디렉터리를 분류합니다."}
::option[`file -b`]{#file-brief-no-operand explanation="`-b`는 출력 형식만 바꾸며 이 명령어에는 검사할 파일이 지정되지 않았습니다."}
:::

## MIME 정보 표시하기

`-i` 옵션은 미디어 유형과 가능한 경우 문자 집합을 포함한 MIME 형식 정보를 출력합니다. 다른 프로그램이 `text/html` 같은 값을 요구할 때 유용합니다.

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

:::single-choice{#show-mime-information}
`index.html`의 MIME 형식 정보를 출력하는 명령어는 무엇인가요?

::option[`file -b index.html`]{#brief-index explanation="`-b`는 일반 설명에서 파일 이름을 생략할 뿐 MIME 형식 출력을 요청하지 않습니다."}
::option[`file -i index.html`]{#mime-index .correct explanation="`-i`는 `text/html`과 문자 집합 같은 MIME 형식 출력을 요청합니다."}
::option[`file -L index.html`]{#follow-index explanation="`-L`은 심볼릭 링크 처리 방식을 제어하며 MIME 출력 형식을 선택하지 않습니다."}
:::

## 유용한 file 옵션

- `-i`: MIME 타입 정보를 보여줍니다.
- `-b`: 간략 모드로, 출력에서 파일 이름을 생략합니다.
- `-L`: 심볼릭 링크를 따라갑니다.
- `-z`: 압축된 파일을 검사하려 시도합니다.

예를 들어:

```bash
$ file -b notes.txt
ASCII text
```

:::single-choice{#omit-filename-from-output}
`notes.txt`를 분류하되 출력에서 파일 이름을 생략하는 명령어는 무엇인가요?

::option[`file -i notes.txt`]{#mime-notes explanation="`-i`는 MIME 형식 정보를 요청하며 보통 출력에 파일 이름도 포함됩니다."}
::option[`file -z notes.txt`]{#compressed-notes explanation="`-z`는 가능하면 압축 데이터 내부를 살펴보게 하며 간략 출력을 켜지 않습니다."}
::option[`file -b notes.txt`]{#brief-notes .correct explanation="`-b`로 선택하는 간략 모드는 파일 이름 접두사 없이 분류 결과만 출력합니다."}
:::

## 요약

이제 `file`을 사용해 파일에 어떤 내용이 들어 있을지 조사할 수 있습니다.

1. 확장자를 믿지 않고 파일을 분류할 수 있습니다.
2. 한 명령어로 여러 경로 이름을 검사할 수 있습니다.
3. MIME 형식 정보를 요청할 수 있습니다.
4. 링크, 압축 데이터와 출력 레이블의 처리 방식을 조정할 수 있습니다.
