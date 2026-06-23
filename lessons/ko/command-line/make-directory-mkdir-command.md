---
index: 12
lang: "ko"
title: "mkdir (디렉토리 만들기)"
meta_title: "mkdir (디렉토리 만들기) - 명령어"
meta_description: "하나의 디렉토리, 여러 디렉토리, 중첩된 상위 디렉토리 생성 및 권한 설정 예제와 함께 Linux mkdir 명령어를 배워보세요."
meta_keywords: "mkdir 명령어, linux mkdir, 디렉토리 생성 linux, 디렉토리 만들기 linux, mkdir -p, mkdir -m, 폴더 생성 linux"
---

## Lesson Content

파일을 다루다 보면 파일을 디렉토리로 정리해야 할 필요가 있습니다. 이 작업의 기본 도구는 `mkdir` 명령어로, 디렉토리를 만든다는 뜻입니다.

기본 구문은 다음과 같습니다:

```bash
mkdir [OPTIONS] DIRECTORY...
```

### 단일 디렉토리 생성하기

`mkdir`의 가장 기본적인 사용법은 단일 새 디렉토리를 만드는 것입니다. 디렉토리가 이미 존재하지 않으면, 이 명령어는 현재 위치에 디렉토리를 생성합니다.

```bash
$ mkdir documents
```

### 여러 디렉토리 생성하기

여러 디렉토리를 한 번에 생성할 수도 있습니다. 이름을 공백으로 구분하여 나열하면 됩니다. 이는 여러 폴더를 빠르게 설정하는 효율적인 방법입니다.

```bash
$ mkdir books paintings
```

### 중첩된 디렉토리 생성하기

때로는 디렉토리와 그 상위 디렉토리를 동시에 만들어야 할 때가 있습니다. `-p` 옵션이 이럴 때 적합합니다. 상위 디렉토리가 없으면 오류를 방지해 줍니다.

```bash
$ mkdir -p books/hemingway/favorites
```

이 단일 명령어는 `books`, `hemingway`, `favorites`가 이미 존재하지 않는 경우 생성합니다.

### 디렉토리 권한 설정하기

디렉토리를 생성하면서 권한을 설정하려면 `-m` 옵션을 사용하세요.

```bash
$ mkdir -m 755 public
```

권한에 대해서는 나중에 더 배우겠지만, 이 예제는 소유자가 쓰기 가능하고 다른 사용자는 읽기 및 진입할 수 있는 디렉토리를 만듭니다.

### 자주 사용하는 mkdir 옵션

- `-p`: 필요한 경우 상위 디렉토리도 생성합니다.
- `-m MODE`: 새 디렉토리의 권한을 설정합니다.
- `-v`: 생성된 각 디렉토리에 대해 메시지를 출력합니다.

예시:

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

### 자주 묻는 질문

**mkdir가 "File exists"라고 하는 이유는?** 해당 이름의 파일이나 디렉토리가 이미 존재하기 때문입니다. `ls` 명령어로 확인해 보세요.

**중첩된 디렉토리는 어떻게 만드나요?** `mkdir -p parent/child/grandchild`를 사용하세요.

**mkdir로 파일도 만들 수 있나요?** 아닙니다. 빈 파일을 만들려면 `touch`를 사용하세요.

## Exercise

연습이 완벽을 만듭니다! 디렉토리 생성과 관리에 대한 이해를 강화할 수 있는 실습 랩을 소개합니다:

1. **[Linux mkdir 명령어: 디렉토리 생성하기](https://labex.io/ko/labs/linux-linux-mkdir-command-directory-creating-209739)** - Linux에서 `mkdir` 명령어를 사용해 디렉토리를 만들고 권한을 설정하며 파일 시스템을 조직하는 방법을 배워보세요. 이 랩은 기본 및 고급 사용법, 중첩 디렉토리 생성도 다룹니다.
2. **[새 프로젝트 구조 설정하기](https://labex.io/ko/labs/linux-setting-up-a-new-project-structure-387859)** - 특정 프로젝트 구조를 만들고 `mkdir`, `cd` 같은 필수 명령어로 탐색하는 연습을 통해 Linux 디렉토리 관리 기술을 향상하세요.

이 랩들은 실제 상황에서 개념을 적용하고 Linux에서 디렉토리를 만들고 조직하는 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

디렉토리를 만들 때 사용하는 명령어는 무엇인가요? 영어 소문자 명령어만 사용해 답해주세요.

## Quiz Answer

mkdir
