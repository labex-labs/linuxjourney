---
index: 5
lang: "ko"
title: "touch"
meta_title: "touch - 명령어 사용법"
meta_description: "빈 파일 생성, 타임스탬프 업데이트, 날짜 설정, 참조 파일 사용, 덮어쓰기 방지 등 Linux touch 명령어 예제와 함께 배우기."
meta_keywords: "linux touch 명령어, touch 명령어, 파일 생성 linux, 타임스탬프 업데이트 linux, touch -d, touch -r, touch -c"
---

## Lesson Content

`touch` 명령어는 유닉스 계열 운영체제에서 표준으로 제공되는 유틸리티입니다. 주된 목적은 파일의 타임스탬프를 변경하는 것이지만, 새 빈 파일을 생성하는 데에도 자주 사용됩니다.

기본 구문은 다음과 같습니다:

```bash
touch [OPTIONS] FILE...
```

### 새 파일 생성하기

빈 파일을 생성하는 가장 간단한 방법은 `touch` 뒤에 파일 이름을 적는 것입니다. 파일이 존재하지 않으면 `touch`가 새로 만듭니다.

```bash
$ touch mysuperduperfile
```

이 명령어를 실행하면 현재 디렉터리에 `mysuperduperfile`이라는 새 빈 파일이 생성됩니다. 여러 파일을 한 번에 생성하려면 파일 이름을 나열하면 됩니다.

```bash
$ touch file1.txt file2.txt file3.log
```

이는 프로젝트 구조를 설정하거나 내용을 추가하기 전에 자리 표시자 파일을 만들 때 유용합니다.

### 파일 타임스탬프 업데이트

`touch`의 원래 기능은 파일이나 디렉터리의 접근 및 수정 타임스탬프를 갱신하는 것입니다. 기존 파일에 `touch`를 사용하면 현재 시간으로 타임스탬프가 업데이트됩니다.

`ls -l`로 파일의 타임스탬프를 확인하고, `touch`를 실행한 후 다시 확인해보면 알 수 있습니다.

```bash
# Check the original timestamp
$ ls -l mysuperduperfile

# Update the timestamp
$ touch mysuperduperfile

# Check the new timestamp
$ ls -l mysuperduperfile
```

### 고급 타임스탬프 조작

`touch` 명령어는 더 정밀한 타임스탬프 조작을 위한 옵션도 제공합니다.

`-r` 옵션으로 참조 파일의 타임스탬프를 복사할 수 있습니다.

```bash
$ touch -r file1.txt file2.txt
```

`-d` 옵션으로 특정 날짜와 시간을 설정할 수 있습니다:

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

`-c` 옵션은 파일이 이미 존재할 때만 업데이트하며, 없으면 새로 만들지 않습니다.

```bash
$ touch -c existing-file.txt
```

### 자주 쓰이는 touch 옵션

- `-a`: 접근 시간만 변경합니다.
- `-m`: 수정 시간만 변경합니다.
- `-c`: 파일이 없으면 생성하지 않습니다.
- `-d "DATE"`: 특정 날짜 문자열을 사용합니다.
- `-r FILE`: 다른 파일의 타임스탬프를 참조합니다.
- `-t STAMP`: 간결한 숫자 형식의 타임스탬프를 사용합니다.

예를 들어, 수정 시간만 변경하려면 다음과 같이 합니다:

```bash
$ touch -m notes.txt
```

### 자주 묻는 질문

**touch가 파일에 텍스트를 추가하나요?** 아니요. `touch`는 빈 파일을 생성하거나 타임스탬프를 업데이트합니다. 텍스트를 추가하려면 편집기, `echo`, `cat` 등을 사용하세요.

**touch가 기존 파일을 덮어쓰나요?** 아니요. 타임스탬프만 업데이트하며 파일 내용을 변경하지 않습니다.

**스크립트에서 touch를 왜 사용하나요?** 파일이 존재하는지 빠르게 확인하거나 특정 작업이 언제 발생했는지 표시하는 간단한 방법입니다.

## Exercise

연습이 완벽을 만듭니다! 파일 시스템 객체 생성 및 관리에 대한 이해를 강화할 수 있는 실습 랩을 소개합니다:

1. **[Linux mkdir 명령어: 디렉터리 생성하기](https://labex.io/ko/labs/linux-linux-mkdir-command-directory-creating-209739)** - Linux에서 `mkdir` 명령어를 사용해 디렉터리를 생성하고 권한을 설정하며 파일 시스템을 조직하는 방법을 배워보세요. 파일 시스템 내 새 항목 생성의 기본 개념을 이해하는 데 도움이 됩니다.
2. **[새 프로젝트 구조 설정하기](https://labex.io/ko/labs/linux-setting-up-a-new-project-structure-387859)** - `mkdir`와 `cd` 같은 필수 명령어를 사용해 특정 프로젝트 구조를 만들고 탐색하는 연습을 통해 Linux 디렉터리 관리 능력을 향상시키세요.

이 랩들은 실제 상황에서 파일 시스템 생성 및 조직 개념을 적용하고 Linux 명령어 사용에 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

`myfile`이라는 파일을 어떻게 만드나요? 대소문자 구분에 주의하여 영어 명령어만으로 답해주세요.

## Quiz Answer

touch myfile
