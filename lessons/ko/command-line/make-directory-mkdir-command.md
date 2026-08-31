---
lesson_id: "make-directory-mkdir-command"
course_id: "command-line"
lang: "ko"
order_index: 12
title: "mkdir (디렉토리 만들기)"
description: "mkdir 옵션으로 하나 이상의 디렉터리와 중첩된 디렉터리를 만드는 방법을 배웁니다."
meta_title: "mkdir (디렉토리 만들기) - 명령어"
meta_description: "하나의 디렉토리, 여러 디렉토리, 중첩된 상위 디렉토리 생성 및 권한 설정 예제와 함께 Linux mkdir 명령어를 배워보세요."
meta_keywords: "mkdir 명령어, linux mkdir, 디렉토리 생성 linux, 디렉토리 만들기 linux, mkdir -p, mkdir -m, 폴더 생성 linux"
---

make directory의 줄임말인 `mkdir` 명령어는 파일과 다른 디렉터리를 정리할 디렉터리를 만듭니다.

기본 구문은 다음과 같습니다:

```bash
mkdir [OPTIONS] DIRECTORY...
```

## 디렉터리 하나 만들기

`mkdir`의 가장 기본적인 사용법은 단일 새 디렉토리를 만드는 것입니다. 디렉토리가 이미 존재하지 않으면, 이 명령어는 현재 위치에 디렉토리를 생성합니다.

```bash
$ mkdir documents
```

`documents`라는 항목이 이미 있으면 `mkdir`는 이를 교체하지 않고 오류를 표시합니다. `ls -ld documents`로 기존 항목을 확인할 수 있습니다.

:::single-choice{#create-one-directory}
현재 작업 디렉터리에 `documents`라는 디렉터리를 만드는 명령어는 무엇인가요?

::option[`mkdir documents`]{#mkdir-documents .correct explanation="`mkdir`는 상대 경로 `documents`에 요청한 디렉터리를 만듭니다."}
::option[`touch documents`]{#touch-documents explanation="`touch`는 경로가 없을 때 빈 일반 파일을 만들며 디렉터리를 만들지 않습니다."}
::option[`cd documents`]{#cd-documents explanation="`cd`는 기존 디렉터리에 들어가려고 할 뿐 없는 디렉터리를 만들지 않습니다."}
:::

## 여러 디렉터리 만들기

여러 디렉토리를 한 번에 생성할 수도 있습니다. 이름을 공백으로 구분하여 나열하면 됩니다. 이는 여러 폴더를 빠르게 설정하는 효율적인 방법입니다.

```bash
$ mkdir books paintings
```

:::single-choice{#create-separate-directories}
`books`와 `paintings`라는 형제 디렉터리 두 개를 만드는 명령어는 무엇인가요?

::option[`mkdir books/paintings`]{#nested-paintings explanation="이 경로는 형제 디렉터리 둘이 아니라 `books` 안의 `paintings`를 뜻하며 `books`가 없으면 실패합니다."}
::option[`mkdir "books paintings"`]{#spaced-directory explanation="따옴표가 두 단어를 한 경로로 묶어 공백이 든 디렉터리 하나를 요청합니다."}
::option[`mkdir books paintings`]{#two-directories .correct explanation="별도 피연산자를 전달하면 `mkdir`가 `books`와 `paintings`를 각각 만듭니다."}
:::

## 없는 상위 디렉터리 만들기

때로는 디렉토리와 그 상위 디렉토리를 동시에 만들어야 할 때가 있습니다. `-p` 옵션이 이럴 때 적합합니다. 상위 디렉토리가 없으면 오류를 방지해 줍니다.

```bash
$ mkdir -p books/hemingway/favorites
```

이 명령어는 경로에서 없는 부분을 모두 만듭니다. 마지막 디렉터리가 이미 있다는 이유만으로 오류를 내지는 않지만 권한 부족 같은 다른 오류는 여전히 발생할 수 있습니다.

:::single-choice{#create-nested-path}
`projects/app/src` 중 어느 디렉터리도 아직 없습니다. 전체 경로를 만드는 명령어는 무엇인가요?

::option[`mkdir -p projects/app/src`]{#mkdir-parents .correct explanation="`-p`는 마지막 디렉터리를 만들기 전에 없는 각 상위 디렉터리를 만듭니다."}
::option[`mkdir projects/app/src`]{#mkdir-no-parents explanation="`-p`가 없으면 중간 디렉터리가 존재하지 않을 때 `src`를 만들 수 없습니다."}
::option[`mkdir -m projects/app/src`]{#mkdir-mode-missing explanation="`-m`은 모드 인자가 필요하며 없는 상위 디렉터리를 만들도록 요청하지 않습니다."}
:::

## 초기 모드 설정하기

디렉토리를 생성하면서 권한을 설정하려면 `-m` 옵션을 사용하세요.

```bash
$ mkdir -m 755 public
```

권한에 대해서는 나중에 더 배우겠지만, 이 예제는 소유자가 쓰기 가능하고 다른 사용자는 읽기 및 진입할 수 있는 디렉토리를 만듭니다.

`-v`를 더하면 만들어지는 각 디렉터리에 대한 메시지를 출력합니다.

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

:::single-choice{#set-directory-mode}
권한 모드 `755`로 `public`을 만드는 명령어는 무엇인가요?

::option[`mkdir -p 755 public`]{#parents-755 explanation="`-p`는 남은 단어를 디렉터리 경로로 처리하므로 권한 모드 `755`를 설정하지 않습니다."}
::option[`mkdir -v 755 public`]{#verbose-755 explanation="`-v`는 생성 메시지를 출력할 뿐 `755`를 권한 모드로 해석하지 않습니다."}
::option[`mkdir -m 755 public`]{#mode-public .correct explanation="`-m`은 요청한 모드를 인자로 받고 `public`은 만들 디렉터리 경로입니다."}
:::

디렉터리 생성과 구성을 연습하려면 다음 실습을 활용해 보세요.

1. **[Linux mkdir 명령어: 디렉토리 생성하기](https://labex.io/ko/labs/linux-linux-mkdir-command-directory-creating-209739)** - Linux에서 `mkdir` 명령어를 사용해 디렉토리를 만들고 권한을 설정하며 파일 시스템을 조직하는 방법을 배워보세요. 이 랩은 기본 및 고급 사용법, 중첩 디렉토리 생성도 다룹니다.
2. **[새 프로젝트 구조 설정하기](https://labex.io/ko/labs/linux-setting-up-a-new-project-structure-387859)** - 특정 프로젝트 구조를 만들고 `mkdir`, `cd` 같은 필수 명령어로 탐색하는 연습을 통해 Linux 디렉토리 관리 기술을 향상하세요.

## 요약

이제 의도한 이름, 상위 경로, 모드로 디렉터리 구조를 만들 수 있습니다.

1. 한 명령어로 하나 이상의 디렉터리를 만들 수 있습니다.
2. 기존 경로 때문에 발생한 오류를 알아볼 수 있습니다.
3. `-p`로 없는 상위 디렉터리를 만들 수 있습니다.
4. `-m`으로 새 디렉터리의 모드를 지정할 수 있습니다.
