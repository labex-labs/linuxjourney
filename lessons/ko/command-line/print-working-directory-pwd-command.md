---
lesson_id: "print-working-directory-pwd-command"
course_id: "command-line"
lang: "ko"
order_index: 2
title: "pwd (현재 작업 디렉토리 출력)"
description: "pwd를 사용해 리눅스 파일 시스템에서 현재 위치를 확인하는 방법을 배웁니다."
meta_title: "pwd (현재 작업 디렉토리 출력) - 명령어 라인"
meta_description: "Linux의 pwd 명령어, 현재 작업 디렉토리 출력의 의미, 절대 경로가 파일 시스템 내 현재 위치를 어떻게 보여주는지 배워보세요."
meta_keywords: "pwd 명령어, 리눅스 pwd, 현재 작업 디렉토리 출력, 리눅스 현재 디렉토리, 절대 경로, 리눅스 파일 시스템, 디렉토리 트리"
---

Linux에서 파일과 디렉토리는 파일 시스템이라는 계층 구조로 조직되어 있습니다. 자신이 어디에 있는지 알기 전에는 자신 있게 이동할 수 없습니다. `pwd` 명령어는 현재 작업 중인 디렉토리를 출력하여 이 질문에 답해줍니다.

## Linux의 디렉토리 트리

전체 파일 시스템은 루트 디렉토리라고 하는 단일 최상위 디렉토리에서 시작하며, 이는 슬래시(`/`)로 표시됩니다. 루트에서 디렉토리 트리는 하위 디렉토리로 갈라지며, 이 하위 디렉토리들은 파일과 더 많은 하위 디렉토리를 포함할 수 있습니다.

다음은 이 구조가 어떻게 생겼는지 단순화한 예입니다:

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

:::single-choice{#identify-root-subdirectories} 위 디렉터리 트리에서 `home`과 `etc`는 `/`와 어떤 관계인가요?

::option[`/`에서 갈라져 나온 하위 디렉터리입니다.]{#root-subdirectories .correct explanation="두 디렉터리는 트리에서 `/` 바로 아래에 있습니다. 파일 시스템은 루트에서 하위 디렉터리로 갈라집니다."}
::option[`bin` 디렉터리 안에 저장된 파일입니다.]{#files-inside-bin explanation="트리에서 `home`과 `etc`는 `bin` 안이 아니라 그 옆에 있습니다. 이 예에서 둘은 파일이 아닌 디렉터리입니다."}
::option[루트 디렉터리를 가리키는 다른 이름입니다.]{#alternate-root-names explanation="리눅스 파일 시스템의 루트는 `/` 하나입니다. `home`과 `etc`는 그 아래에 있는 디렉터리입니다."}
:::

## 파일 경로 이해하기

파일이나 디렉토리의 위치는 경로로 설명됩니다. 경로는 시작점에서 특정 목적지까지 이어지는 디렉토리들의 연속입니다.

예를 들어, `/home` 안에 `pete`라는 폴더가 있고, `pete` 안에 `Movies` 폴더가 있다면 전체 경로는 다음과 같습니다:

```plaintext
/home/pete/Movies
```

`/`로 시작하는 경로는 루트 디렉토리에서 시작하기 때문에 절대 경로입니다. `Movies`와 같은 경로는 현재 위치에 따라 달라지므로 상대 경로입니다.

:::single-choice{#recognize-absolute-path} `/home/pete/Movies`가 절대 경로인 이유는 무엇인가요?

::option[여러 디렉터리 이름이 `/`로 구분되어 있기 때문입니다.]{#contains-directories explanation="절대 경로와 상대 경로 모두 여러 디렉터리 이름을 포함할 수 있습니다. 이름의 개수가 아니라 시작점이 경로 유형을 결정합니다."}
::option[`Movies`라는 디렉터리에서 끝나기 때문입니다.]{#ends-with-movies explanation="목적지 이름은 절대 경로 여부를 결정하지 않습니다. 절대 경로는 루트에서 시작하는 것으로 구분합니다."}
::option[맨 앞의 `/`가 루트에서 시작함을 나타내기 때문입니다.]{#starts-at-root .correct explanation="절대 경로는 루트 디렉터리에서 시작합니다. 맨 앞의 `/`가 그 시작점을 보여 줍니다."}
:::

## Linux에서 PWD의 전체 의미는 무엇인가요?

`pwd`의 전체 의미는 "print working directory"입니다. 작업 디렉토리는 현재 셸이 위치한 디렉토리입니다. 상대 경로를 사용하는 명령어들은 이 위치에서 시작합니다.

:::single-choice{#expand-pwd-name} `pwd`는 무엇의 약자인가요?

::option[Print working directory]{#print-working-directory .correct explanation="이 이름은 명령어의 동작을 그대로 나타냅니다. 쉘의 현재 작업 디렉터리를 출력합니다."}
::option[Present working directory]{#present-working-directory explanation="일상적인 표현으로 현재 디렉터리라고 할 수는 있지만, 이는 `pwd`의 원래 단어 풀이가 아닙니다."}
::option[Print whole directory]{#print-whole-directory explanation="`pwd`는 현재 디렉터리의 경로를 보여 줄 뿐, 디렉터리의 모든 내용을 출력하지는 않습니다."}
:::

## pwd 명령어 사용법

현재 디렉토리를 찾으려면 `pwd`를 입력하고 Enter 키를 누르세요.

```bash
$ pwd
/home/pete
```

출력은 절대 경로입니다. 이 예에서는 셸이 현재 `pete` 사용자의 홈 디렉토리에 있습니다.

실제 출력은 사용자 이름, 홈 디렉터리, 현재 위치에 따라 시스템마다 다를 수 있습니다. `pwd`는 정보만 출력하고 작업 디렉터리를 바꾸지 않습니다. 반면 `cd`는 쉘이 위치한 디렉터리를 변경합니다.

:::single-choice{#check-location-without-changing-it} 현재 디렉터리를 바꾸지 않고 확인하는 방법은 무엇인가요?

::option[`cd`를 실행하고 이동한 디렉터리를 확인합니다.]{#run-cd explanation="`cd`는 작업 디렉터리를 변경하므로 위치를 바꾸지 않고 확인한다는 조건에 맞지 않습니다."}
::option[`/home/pete`를 입력해 경로 자체를 명령어로 실행합니다.]{#run-path explanation="절대 경로는 위치를 나타내지만, 경로 자체가 현재 디렉터리를 알려 주는 명령어는 아닙니다."}
::option[`pwd`를 실행하고 출력된 절대 경로를 확인합니다.]{#run-pwd .correct explanation="`pwd`는 이동하지 않고 쉘의 현재 위치를 알려 줍니다. 따라서 현재 위치를 확인할 때 안전하게 사용할 수 있습니다."}
:::

## pwd가 유용한 이유

다음과 같은 경우에 `pwd`를 사용하세요:

- 지침을 따르면서 현재 위치를 확인해야 할 때
- 파일 경로가 잘못되어 명령어가 실패했을 때
- 여러 디렉토리를 이동하다가 현재 위치를 잃었을 때
- 현재 디렉토리 경로를 다른 명령어에 복사하고 싶을 때

예를 들어:

```bash
$ pwd
/home/pete/projects
$ ls
app.py  README.md
```

이것은 `app.py`와 `README.md`가 `/home/pete/projects`에 위치함을 알려줍니다.

Linux 파일 시스템 탐색과 현재 위치 확인을 연습하려면 다음 실습을 활용해 보세요.

1. **[Linux pwd 명령어: 디렉토리 표시](https://labex.io/ko/labs/linux-linux-pwd-command-directory-displaying-209734)** - 이 랩은 `pwd` 명령어의 집중적인 개요와 실용적인 사용법을 제공하며, 현재 디렉토리 찾기에 대한 수업 내용을 직접적으로 다룹니다.
2. **[Linux 디렉토리 탐색](https://labex.io/ko/labs/linux-directory-navigation-387844)** - 다양한 디렉토리를 탐색하며 기본 Linux 명령어 라인 기술을 테스트하고, 경로와 파일 시스템 구조에 대한 이해를 확고히 하세요.
3. **[Linux cd 명령어: 디렉토리 변경](https://labex.io/ko/labs/linux-linux-cd-command-directory-changing-209733)** - `cd` 명령어를 사용해 파일 시스템을 효율적으로 탐색하는 방법을 배우고, 디렉토리 변경과 파일 구조 탐색의 다양한 기법을 익히세요.

## 요약

이제 `pwd`로 리눅스 파일 시스템에서 현재 위치를 확인할 수 있습니다.

1. 디렉터리 트리의 루트를 알아볼 수 있습니다.
2. 절대 경로와 상대 경로를 구분할 수 있습니다.
3. `pwd`의 의미와 출력 내용을 설명할 수 있습니다.
4. 작업 디렉터리를 바꾸지 않고 현재 위치를 확인할 수 있습니다.
