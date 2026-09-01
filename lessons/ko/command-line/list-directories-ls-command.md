---
lesson_id: "list-directories-ls-command"
course_id: "command-line"
lang: "ko"
order_index: 4
title: "ls (디렉토리 목록)"
description: "ls 옵션을 사용해 파일, 숨김 항목, 상세 정보, 크기와 정렬 순서를 확인하는 방법을 배웁니다."
meta_title: "ls (디렉토리 목록) - 커맨드 라인"
meta_description: "파일 목록, 숨김 파일, 긴 형식 출력, 사람이 읽기 쉬운 크기, 정렬 및 옵션 결합 예제를 통해 Linux ls 명령어를 배워보세요."
meta_keywords: "ls 명령어, 리눅스 ls, 리눅스 파일 목록, 디렉토리 목록, ls -a, ls -l, ls -lh, ls -r, 숨김 파일"
---

이제 파일 시스템을 어떻게 이동하는지 알았으니, 어떤 항목들이 있는지 어떻게 확인할 수 있을까요? `ls` 명령어는 파일과 디렉토리를 나열하여 현재 위치나 다른 경로를 검사할 수 있게 해줍니다.

## ls 명령어 기본 사용법

기본적으로 `ls` 명령어는 현재 디렉토리의 디렉토리와 파일을 나열합니다. 하지만 다른 디렉토리의 내용을 나열하려면 경로를 지정할 수도 있습니다.

```bash
$ ls
$ ls /home/pete
```

특정 파일도 나열할 수 있습니다:

```bash
$ ls /etc/hosts
/etc/hosts
```

:::single-choice{#list-another-directory} 해당 디렉터리로 이동하지 않고 `/home/pete`의 내용을 나열하는 명령어는 무엇인가요?

::option[`ls /home/pete`]{#ls-target-path .correct explanation="`ls`에 디렉터리 경로를 전달하면 그 디렉터리의 내용을 나열합니다. 쉘의 현재 작업 디렉터리는 그대로 유지됩니다."}
::option[`cd /home/pete`]{#cd-target-path explanation="`cd`는 쉘의 작업 디렉터리를 변경합니다. 이 명령어만으로는 요청한 목록을 출력하지 않습니다."}
::option[`pwd /home/pete`]{#pwd-target-path explanation="`pwd`는 현재 작업 디렉터리를 알려 주며 나열할 대상 경로를 받지 않습니다. 대신 경로와 함께 `ls`를 사용합니다."}
:::

## 숨김 파일 보기

디렉토리 내 모든 파일이 기본적으로 보이는 것은 아닙니다. Linux에서 파일 이름이 점(`.`)으로 시작하면 숨김 파일입니다. `-a` 옵션을 사용하면 모든 파일을 볼 수 있습니다. `-a`는 all(모두)의 약자입니다.

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

점 파일은 기본적으로 숨겨지며 `.bashrc`처럼 설정을 저장하는 데 자주 사용됩니다.

:::single-choice{#show-hidden-files} 숨김 파일까지 목록에 포함하는 명령어는 무엇인가요?

::option[`ls -l`]{#long-format explanation="`-l`은 상세 열을 추가하지만 이 옵션만으로 숨김 이름까지 포함하지는 않습니다."}
::option[`ls -r`]{#reverse-order explanation="`-r`은 정렬 순서를 뒤집을 뿐, 숨김 파일의 포함 여부는 바꾸지 않습니다."}
::option[`ls -a`]{#all-files .correct explanation="`-a`는 all을 뜻하므로 `ls`가 점으로 시작하는 이름도 포함해 보여 줍니다."}
:::

## 자세한 정보 얻기

또 다른 중요한 `ls` 옵션은 긴 형식인 `-l`입니다. 파일 권한, 링크 수, 소유자, 그룹, 크기, 수정 시간, 이름을 보여줍니다.

```bash
$ ls -l
```

출력 예시는 다음과 같습니다:

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

파일 크기를 더 쉽게 보려면 `-h` 옵션을 추가하여 사람이 읽기 쉬운 형식으로 출력할 수 있습니다:

```bash
$ ls -lh
```

:::single-choice{#show-readable-file-details} 사람이 읽기 쉬운 크기와 긴 형식의 상세 정보를 함께 보여 주는 명령어는 무엇인가요?

::option[`ls -la`]{#long-all explanation="이 명령어는 긴 형식과 숨김 파일 표시를 결합하지만 읽기 쉬운 크기 단위는 요청하지 않습니다."}
::option[`ls -lh`]{#long-human-readable .correct explanation="`-l`은 긴 형식을 선택하고 `-h`는 크기를 읽기 쉽게 표시합니다. 두 플래그는 한 명령어에 결합할 수 있습니다."}
::option[`ls -ltr`]{#long-time-reverse explanation="긴 형식, 수정 시간 정렬, 역순 정렬을 결합하지만 크기를 바꾸는 `-h`는 포함하지 않습니다."}
:::

## 역순 정렬

가끔 정렬 순서를 바꾸고 싶을 때가 있습니다. `-r` 옵션은 파일과 디렉토리를 역순으로 나열합니다.

```bash
$ ls -r
```

수정 시간으로 정렬하려면 `-t`를 사용하고, 그 후 `-r`로 역순 정렬할 수 있습니다:

```bash
$ ls -lt
$ ls -ltr
```

:::single-choice{#show-newest-files-last} 수정 시간으로 정렬한 뒤 가장 최근 항목을 마지막에 배치하는 명령어는 무엇인가요?

::option[`ls -ltr`]{#time-reversed .correct explanation="`-t`는 수정 시간으로 정렬하고 `-r`은 그 순서를 뒤집습니다. 함께 사용하면 오래된 항목이 최신 항목보다 먼저 나옵니다."}
::option[`ls -lt`]{#time-default explanation="수정 시간으로 정렬하지만 기본값인 최신 항목 우선 순서를 유지하므로 최신 항목이 마지막에 오지 않습니다."}
::option[`ls -lr`]{#reverse-name-order explanation="긴 형식으로 이름 정렬의 기본 순서만 뒤집습니다. `-t`가 없으므로 수정 시간이 정렬 기준이 아닙니다."}
:::

## 명령어 옵션 결합

명령어에는 기능을 추가하는 플래그(옵션)가 있습니다. `-a`와 `-l`에서 보았듯이, 이들을 결합해 `ls -la`처럼 한 번에 사용할 수 있습니다. 플래그 순서는 보통 중요하지 않아 `ls -al`도 같은 결과를 냅니다.

```bash
$ ls -la
```

유용한 조합 예시는 다음과 같습니다:

```bash
$ ls -lh
$ ls -la
$ ls -ltr
```

## 자주 사용하는 ls 옵션

- `-a`: 숨김 파일을 포함한 모든 파일을 표시합니다.
- `-l`: 긴 형식을 사용합니다.
- `-h`: `-l`과 함께 사람이 읽기 쉬운 크기를 표시합니다.
- `-r`: 정렬 순서를 역순으로 바꿉니다.
- `-t`: 수정 시간으로 정렬합니다.
- `-S`: 파일 크기로 정렬합니다.
- `-d`: 디렉토리 내용이 아닌 디렉토리 자체를 나열합니다.

:::single-choice{#list-directory-entry-itself} `projects/`의 내용이 아니라 디렉터리 항목 자체를 나열하는 명령어는 무엇인가요?

::option[`ls -d projects/`]{#directory-entry .correct explanation="`-d` 옵션은 디렉터리를 열어 내용 목록을 보여 주는 대신 디렉터리 항목 자체를 표시하게 합니다."}
::option[`ls projects/`]{#directory-contents explanation="`-d` 없이 디렉터리 경로를 전달하면 `ls`는 그 디렉터리 안의 항목을 표시합니다."}
::option[`cd projects/`]{#change-to-directory explanation="`cd`는 작업 디렉터리를 바꾸며 여기서 요청한 디렉터리 항목을 나열하지 않습니다."}
:::

일부 시스템은 파일 유형에 따라 `ls` 출력을 다른 색으로 표시합니다. 이 동작은 보통 별칭이나 환경 설정에서 오므로 시스템마다 색상이 다를 수 있습니다.

`ls` 명령어를 연습하려면 다음 실습을 활용해 보세요.

- **[Linux ls 명령어: 내용 목록](https://labex.io/ko/labs/linux-linux-ls-command-content-listing-219205)** - `ls` 명령어를 사용하여 파일과 디렉토리 내용을 효율적으로 나열하고 분석하는 연습을 하세요. 자세한 목록, 숨김 파일 표시, 사람이 읽기 쉬운 크기, 정렬 기법 등 다양한 옵션을 배우며 커맨드 라인 실력을 향상시킬 수 있습니다.

이 실습은 실제 상황에 개념을 적용하고 Linux 디렉터리 목록 작업에 익숙해지는 데 도움이 됩니다.

## 요약

이제 `ls`로 디렉터리 내용을 살펴보고 항목 표시 방식을 제어할 수 있습니다.

1. 현재 디렉터리나 다른 경로의 내용을 나열할 수 있습니다.
2. 숨김 파일을 목록에 포함할 수 있습니다.
3. 읽기 쉬운 크기와 상세 정보를 표시할 수 있습니다.
4. 수정 시간의 역순으로 항목을 정렬할 수 있습니다.
5. 내용 대신 디렉터리 항목 자체를 나열할 수 있습니다.
