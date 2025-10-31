---
index: 5
lang: "ko"
title: "터치"
meta_title: "touch - 리눅스 명령어"
meta_description: "리눅스 touch 명령어를 사용하여 파일을 생성하고 타임스탬프를 관리하는 방법을 알아보세요. 이 가이드는 linux touch -r 및 touch -d 와 같은 옵션을 포함하여 리눅스 touch 명령어를 다룹니다."
meta_keywords: "리눅스 touch, 리눅스 touch 명령어, bash touch, touch -d 리눅스, 리눅스 touch -r, 파일 생성, 타임스탬프 업데이트, 파일 관리, 리눅스 명령어"
---

## Lesson Content

touch 명령어는 Unix 계열 운영 체제에서 표준 유틸리티입니다. 주된 목적은 파일 타임스탬프를 변경하는 것이지만, 새롭고 빈 파일을 만드는 데에도 일반적으로 사용됩니다. linux touch 명령어가 어떻게 작동하는지 살펴보겠습니다.

### 새 파일 만들기

빈 파일을 만드는 가장 간단한 방법은 touch 명령어 뒤에 파일 이름을 사용하는 것입니다. 파일이 존재하지 않으면 touch 가 파일을 생성합니다. 이는 스크립팅 및 일상 작업에서 기본적인 bash touch 작업입니다.

```bash
touch mysuperduperfile
```

이 명령어를 실행한 후, 현재 디렉토리에 `mysuperduperfile`이라는 새 빈 파일이 나타납니다. 파일 이름을 나열하여 한 번에 여러 파일을 만들 수 있습니다.

```bash
touch file1.txt file2.txt file3.log
```

### 파일 타임스탬프 업데이트

linux touch 명령어의 원래 기능은 파일 또는 디렉터리의 액세스 및 수정 타임스탬프를 업데이트하는 것입니다. 기존 파일에 touch 를 사용하면 타임스탬프가 현재 시간으로 업데이트됩니다.

`ls -l`을 사용하여 파일의 타임스탬프를 확인하고, touch 를 실행한 다음 다시 확인하여 이를 확인할 수 있습니다.

```bash
# 원래 타임스탬프 확인
ls -l mysuperduperfile

# 타임스탬프 업데이트
touch mysuperduperfile

# 새 타임스탬프 확인
ls -l mysuperduperfile
```

### 고급 타임스탬프 제어

linux touch 명령어는 보다 정밀한 타임스탬프 조작을 위한 옵션도 제공합니다.

#### 참조 파일 사용

linux touch -r 옵션을 사용하면 한 파일의 타임스탬프를 다른 파일 (참조 파일) 의 타임스탬프와 일치하도록 설정할 수 있습니다. 이는 관련 파일 간의 타임스탬프 동기화에 유용합니다.

```bash
# file2.txt의 타임스탬프를 file1.txt의 타임스탬프와 일치하도록 설정
touch -r file1.txt file2.txt
```

#### 특정 날짜 설정

touch -d 옵션을 사용하면 파일의 타임스탬프를 특정 날짜와 시간으로 설정할 수 있습니다. touch -d linux 기능은 날짜에 대해 다양한 문자열 형식을 허용합니다.

```bash
# 타임스탬프를 특정 날짜와 시간으로 설정
touch -d "2023-01-01 12:30:00" mysuperduperfile
```

touch 를 마스터하는 것은 명령줄에서 파일 시스템을 효율적으로 관리하는 방법을 배우는 훌륭한 단계입니다.

## Exercise

연습이 완벽을 만듭니다! 파일 시스템 객체 생성 및 관리에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[Linux mkdir 명령어: 디렉터리 생성](https://labex.io/ko/labs/linux-linux-mkdir-command-directory-creating-209739)** - Linux 에서 `mkdir` 명령어를 사용하여 디렉터리를 생성하고, 권한을 설정하며, 파일 시스템을 구성하는 방법을 배웁니다. 이는 파일 시스템에서 새 항목을 생성하는 더 넓은 개념을 이해하는 데 도움이 될 것입니다.
2. **[새 프로젝트 구조 설정](https://labex.io/ko/labs/linux-setting-up-a-new-project-structure-387859)** - `mkdir` 및 `cd`와 같은 필수 명령어를 사용하여 특정 프로젝트 구조를 만들고 그 안을 탐색하면서 Linux 디렉터리 관리 기술을 연습합니다.

이 랩들은 실제 시나리오에서 파일 시스템 생성 및 구성 개념을 적용하고 Linux 명령어에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

`myfile`이라는 파일을 어떻게 만드나요? 대소문자를 구분하여 영어 명령어로만 답변해 주세요.

## Quiz Answer

touch myfile
