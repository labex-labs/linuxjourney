---
index: 4
lang: "ko"
title: "ls (디렉토리 목록 보기)"
meta_title: "ls (디렉토리 목록 보기) - 명령줄"
meta_description: "Linux 에서 강력한 ls 명령어를 사용하는 방법을 알아보세요. 이 가이드는 디렉토리 내용을 나열하는 방법, ls -a 로 숨김 파일 보기, ls -l 로 상세 목록 보기, ls -r 명령어로 역순 정렬하는 방법을 다룹니다. cmd ls 를 마스터하기 위한 완벽한 학습 자료입니다."
meta_keywords: "ls 명령어, 디렉토리 목록, cmd ls, ls -r 명령어, 명령어 ls, linux ls -r, 리눅스 명령어 ls, 숨김 파일, 리눅스 명령어, 초보 리눅스"
---

## Lesson Content

이제 파일 시스템을 이동하는 방법을 알았으니, 우리에게 무엇이 있는지 어떻게 확인할 수 있을까요? 올바른 도구 없이는 어둠 속에서 움직이는 것과 같습니다. 다행히도 훌륭한 `command linux ls`가 디렉터리 내용을 나열하여 도와줄 준비가 되어 있습니다.

### ls 명령어의 기본 사용법

기본적으로 `ls` 명령어는 현재 디렉터리의 디렉터리와 파일을 나열합니다. 하지만 다른 디렉터리의 내용을 나열하기 위해 경로를 지정할 수도 있습니다.

```bash
ls
ls /home/pete
```

`command ls`는 보고 있는 파일과 디렉터리에 대한 자세한 정보를 보여줄 수 있는 다용도 도구입니다.

### 숨겨진 파일 보기

모든 파일이 기본적으로 표시되는 것은 아닙니다. Linux 에서는 점 (`.`) 으로 시작하는 파일 이름은 숨겨집니다. "모두"를 의미하는 `-a` 플래그와 함께 `cmd ls`를 사용하여 이 파일들을 볼 수 있습니다.

```bash
ls -a
```

### 자세한 정보 얻기

또 다른 필수 `ls` 플래그는 "long"을 의미하는 `-l`입니다. 이 옵션은 자세한 파일 목록을 긴 형식으로 제공합니다. 왼쪽부터 파일 권한, 링크 수, 소유자 이름, 소유자 그룹, 파일 크기, 마지막 수정 타임스탬프, 파일 또는 디렉터리 이름 순으로 자세한 정보가 표시됩니다.

```bash
ls -l
```

다음은 출력 예시입니다:

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

### 역순 정렬

때로는 정렬 순서를 변경하고 싶을 수 있습니다. `ls -r command`는 파일과 디렉터리를 역순 알파벳 순서로 나열합니다. `linux ls -r` 옵션은 긴 목록의 마지막 항목을 먼저 보고 싶을 때 특히 유용합니다.

```bash
ls -r
```

### 명령어 플래그 결합

명령어에는 추가 기능을 위한 플래그 (인수 또는 옵션이라고도 함) 가 있습니다. `-a`와 `-l`에서 보았듯이, 이들을 `ls -la`와 같은 단일 명령어로 결합할 수 있습니다. 플래그의 순서는 보통 중요하지 않으므로 `ls -al`도 동일하게 작동합니다. 역순 플래그도 추가할 수 있습니다: `ls -lar`.

```bash
ls -la
```

## Exercise

연습이 완벽함을 만듭니다! `ls` 명령어에 대한 이해를 강화하기 위한 실습 랩이 있습니다:

- **[Linux ls 명령어: 콘텐츠 나열](https://labex.io/ko/labs/linux-linux-ls-command-content-listing-219205)** - `ls` 명령어를 사용하여 파일 및 디렉터리 내용을 효율적으로 나열하고 분석하는 방법을 연습합니다. 자세한 목록, 숨겨진 파일 표시, 사람이 읽을 수 있는 크기 및 정렬 기술을 위한 다양한 옵션을 학습하여 명령줄 기술을 향상시킬 것입니다.

이 랩은 실제 시나리오에서 개념을 적용하고 Linux 에서 디렉터리 나열에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

숨겨진 파일을 보려면 어떤 명령어를 사용해야 합니까? 대소문자를 구분하여 영어로 답변해 주십시오.

## Quiz Answer

ls -a
