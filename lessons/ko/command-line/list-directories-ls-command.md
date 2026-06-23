---
index: 4
lang: "ko"
title: "ls (디렉토리 목록)"
meta_title: "ls (디렉토리 목록) - 커맨드 라인"
meta_description: "파일 목록, 숨김 파일, 긴 형식 출력, 사람이 읽기 쉬운 크기, 정렬 및 옵션 결합 예제를 통해 Linux ls 명령어를 배워보세요."
meta_keywords: "ls 명령어, 리눅스 ls, 리눅스 파일 목록, 디렉토리 목록, ls -a, ls -l, ls -lh, ls -r, 숨김 파일"
---

## Lesson Content

이제 파일 시스템을 어떻게 이동하는지 알았으니, 어떤 항목들이 있는지 어떻게 확인할 수 있을까요? `ls` 명령어는 파일과 디렉토리를 나열하여 현재 위치나 다른 경로를 검사할 수 있게 해줍니다.

### ls 명령어 기본 사용법

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

### 숨김 파일 보기

디렉토리 내 모든 파일이 기본적으로 보이는 것은 아닙니다. Linux에서 파일 이름이 점(`.`)으로 시작하면 숨김 파일입니다. `-a` 옵션을 사용하면 모든 파일을 볼 수 있습니다. `-a`는 all(모두)의 약자입니다.

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

### 자세한 정보 얻기

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

### 역순 정렬

가끔 정렬 순서를 바꾸고 싶을 때가 있습니다. `-r` 옵션은 파일과 디렉토리를 역순으로 나열합니다.

```bash
$ ls -r
```

수정 시간으로 정렬하려면 `-t`를 사용하고, 그 후 `-r`로 역순 정렬할 수 있습니다:

```bash
$ ls -lt
$ ls -ltr
```

### 명령어 옵션 결합

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

### 자주 사용하는 ls 옵션

- `-a`: 숨김 파일을 포함한 모든 파일을 표시합니다.
- `-l`: 긴 형식을 사용합니다.
- `-h`: `-l`과 함께 사람이 읽기 쉬운 크기를 표시합니다.
- `-r`: 정렬 순서를 역순으로 바꿉니다.
- `-t`: 수정 시간으로 정렬합니다.
- `-S`: 파일 크기로 정렬합니다.
- `-d`: 디렉토리 내용이 아닌 디렉토리 자체를 나열합니다.

### 자주 묻는 질문

**왜 일부 파일 이름이 점으로 시작하나요?** 점으로 시작하는 파일은 기본적으로 숨김 처리되며, `.bashrc`와 같은 설정 파일을 저장하는 데 자주 사용됩니다.

**디렉토리 자체만 나열하려면 어떻게 하나요?** `ls -d directory/`를 사용하세요.

**가장 최근 파일을 마지막에 보려면 어떻게 하나요?** `ls -ltr`을 사용하세요.

**왜 ls가 색상을 보여주나요?** 많은 시스템에서 별칭(alias)이나 환경 설정을 통해 파일 유형별로 색상을 표시하도록 `ls`를 설정합니다.

## Exercise

연습이 완벽을 만듭니다! `ls` 명령어에 대한 이해를 강화할 수 있는 실습 랩입니다:

- **[Linux ls 명령어: 내용 목록](https://labex.io/ko/labs/linux-linux-ls-command-content-listing-219205)** - `ls` 명령어를 사용하여 파일과 디렉토리 내용을 효율적으로 나열하고 분석하는 연습을 하세요. 자세한 목록, 숨김 파일 표시, 사람이 읽기 쉬운 크기, 정렬 기법 등 다양한 옵션을 배우며 커맨드 라인 실력을 향상시킬 수 있습니다.

이 랩은 실제 상황에서 개념을 적용하고 Linux에서 디렉토리 목록 작업에 자신감을 쌓는 데 도움이 될 것입니다.

## Quiz Question

숨김 파일을 보려면 어떤 명령어를 사용하나요? 대소문자 구분에 주의하여 영어로 답해주세요.

## Quiz Answer

ls -a
