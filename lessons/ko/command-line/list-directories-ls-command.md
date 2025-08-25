---
index: 4
lang: "ko"
title: "ls (디렉토리 나열)"
meta_title: "ls (디렉토리 나열) - 명령줄"
meta_description: "Linux 에서 'ls' 명령을 사용하여 디렉토리 내용을 나열하고, 숨겨진 파일을 보고, 파일 세부 정보를 이해하는 방법을 배우세요. Linux 명령줄 기술을 향상시키세요!"
meta_keywords: "ls 명령, 디렉토리 나열, Linux 튜토리얼, 숨겨진 파일, Linux 명령, 초보자 Linux, Linux 가이드"
---

## Lesson Content

이제 시스템을 이동하는 방법을 알았으니, 무엇을 사용할 수 있는지 어떻게 알아낼까요? 지금은 마치 어둠 속을 움직이는 것과 같습니다. 음, 우리는 훌륭한 `ls` 명령을 사용하여 디렉토리 내용을 나열할 수 있습니다. `ls` 명령은 기본적으로 현재 디렉토리의 디렉토리와 파일을 나열하지만, 디렉토리를 나열할 경로를 지정할 수 있습니다.

```bash
ls
ls /home/pete
```

`ls`는 매우 유용한 도구입니다. 또한 보고 있는 파일 및 디렉토리에 대한 자세한 정보를 보여줍니다.

또한, 디렉토리의 모든 파일이 보이는 것은 아닙니다. `.`으로 시작하는 파일 이름은 숨겨져 있습니다. 그러나 `ls` 명령과 `-a` 플래그 (`a`는 all 의 약자) 를 사용하여 볼 수 있습니다.

```bash
ls -a
```

또 다른 유용한 `ls` 플래그인 `-l` (long 의 약자) 도 있습니다. 이것은 긴 형식으로 파일의 자세한 목록을 보여줍니다. 이것은 왼쪽부터 파일 권한, 링크 수, 소유자 이름, 소유자 그룹, 파일 크기, 마지막 수정 타임스탬프, 파일/디렉토리 이름과 같은 자세한 정보를 보여줍니다.

```bash
ls -l
```

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

명령에는 더 많은 기능을 추가하기 위한 플래그 (또는 인수 또는 옵션, 원하는 대로 부르세요) 라는 것이 있습니다. `-a`와 `-l`을 어떻게 추가했는지 보세요. `-la`로 둘 다 함께 추가할 수 있습니다. 플래그의 순서는 그것이 들어가는 순서를 결정합니다. 대부분의 경우 이것은 중요하지 않으므로 `ls -al`로 해도 여전히 작동합니다.

```bash
ls -la
```

## Exercise

연습이 완벽을 만듭니다! 다음은 `ls` 명령에 대한 이해를 강화하기 위한 실습 랩입니다:

- **[Linux ls 명령: 내용 나열](https://labex.io/ko/labs/linux-linux-ls-command-content-listing-219205)** - `ls` 명령을 사용하여 파일 및 디렉토리 내용을 효율적으로 나열하고 분석하는 연습을 하세요. 자세한 목록, 숨겨진 파일 표시, 사람이 읽을 수 있는 크기, 정렬 기술을 위한 다양한 옵션을 배워 명령줄 기술을 향상시킬 수 있습니다.

이 랩은 실제 시나리오에서 개념을 적용하고 Linux 에서 디렉토리 목록에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

숨겨진 파일을 보려면 어떤 명령을 사용해야 합니까?

## Quiz Answer

ls -a
