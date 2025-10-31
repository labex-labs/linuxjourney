---
index: 12
lang: "ko"
title: "mkdir (디렉토리 생성)"
meta_title: "mkdir (디렉토리 생성) - 명령줄"
meta_description: "Linux 에서 mkdir 명령어를 사용하여 새 디렉토리를 만드는 방법을 알아보세요. 이 가이드는 명령 프롬프트에서 여러 디렉토리 및 상위 디렉토리를 만드는 방법을 포함하여 Linux 폴더 생성 명령어를 다룹니다."
meta_keywords: "리눅스 디렉토리 생성, 리눅스 mkdir 명령어, 리눅스 디렉토리 만들기, 명령 프롬프트 디렉토리 생성, 리눅스 폴더 생성 명령어, mkdir, 디렉토리 만들기, 리눅스"
---

## Lesson Content

파일을 다루다 보면 파일을 디렉터리 (폴더) 로 정리해야 할 필요가 있습니다. 이 작업을 위한 주요 도구는 "디렉터리 만들기 (Make Directory)"를 의미하는 `mkdir` 명령어입니다. 이 명령어를 사용하면 터미널이나 **명령 프롬프트**에서 바로 **Linux 에서 디렉터리를 생성**할 수 있습니다.

### 단일 디렉터리 생성

**Linux 의 mkdir 명령어**의 가장 기본적인 용도는 단일 새 디렉터리를 만드는 것입니다. 해당 디렉터리가 아직 존재하지 않는다면, 이 명령어는 현재 위치에 디렉터리를 생성합니다. 예를 들어, `documents`라는 디렉터리를 만들려면 다음과 같이 입력합니다.

```bash
mkdir documents
```

### 여러 디렉터리 생성

여러 디렉터리 이름을 공백으로 구분하여 한 번에 여러 디렉터리를 만들 수도 있습니다. 이는 여러 폴더를 빠르게 설정하는 효율적인 방법입니다.

```bash
mkdir books paintings
```

### 중첩된 디렉터리 생성

때로는 디렉터리와 그 부모 디렉터리를 동시에 만들어야 할 때가 있습니다. 이때 `-p` (parent) 옵션이 완벽하게 유용합니다. **Linux 폴더 생성 명령어**의 이 강력한 기능은 부모 디렉터리가 존재하지 않아도 오류를 방지합니다. 예를 들어, `books` 안에 `hemmingway`가 있고 그 안에 `favorites` 디렉터리를 만들려면 다음과 같이 입력합니다.

```bash
mkdir -p books/hemmingway/favorites
```

이 단일 명령은 `books`, `hemmingway`, `favorites`가 아직 존재하지 않는다면 모두 생성하여, **Linux 에서 디렉터리를 생성**해야 할 때의 핵심 기능을 보여줍니다.

## Exercise

연습이 완벽함을 만듭니다! 디렉터리 생성 및 관리에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[Linux mkdir 명령어: 디렉터리 생성](https://labex.io/ko/labs/linux-linux-mkdir-command-directory-creating-209739)** - Linux 에서 `mkdir` 명령어를 사용하여 디렉터리를 만들고, 권한을 설정하며, 파일 시스템을 구성하는 방법을 배웁니다. 이 랩은 중첩된 디렉터리 생성과 같은 기본 및 고급 사용법을 다룹니다.
2. **[새 프로젝트 구조 설정](https://labex.io/ko/labs/linux-setting-up-a-new-project-structure-387859)** - `mkdir` 및 `cd`와 같은 필수 명령어를 사용하여 특정 프로젝트 구조를 만들고 그 안을 탐색하면서 Linux 디렉터리 관리 기술을 연습합니다.

이 랩들은 실제 시나리오에 개념을 적용하고 Linux 에서 디렉터리를 생성하고 구성하는 데 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

디렉터리를 만드는 데 사용되는 명령어는 무엇입니까? 소문자 영어 명령어를 사용하여 답변하십시오.

## Quiz Answer

mkdir
