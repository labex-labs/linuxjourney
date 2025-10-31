---
index: 12
lang: "ko"
title: "심볼릭 링크"
meta_title: "심볼릭 링크 - 파일 시스템"
meta_description: "Linux 심볼릭 링크 (symbolic links) 와 하드 링크를 탐색합니다. ln 명령어로 생성하는 방법, ls 로 리눅스에서 링크 수를 확인하는 방법, 그리고 ls 출력 시 심볼릭 링크와 하드 링크의 차이점을 이해하는 방법을 알아보세요."
meta_keywords: "리눅스 심볼릭 링크, 하드 링크, ln 명령어, 심볼릭 링크, ls 심볼릭 링크, 리눅스 링크 수, ls 심볼릭 링크, ls 링크, 리눅스 파일 시스템, 리눅스 튜토리얼"
---

## Lesson Content

파일을 자세히 나열하면 많은 정보를 볼 수 있습니다. `ls -li` 명령에서 나온 이전 inode 정보 예시를 살펴보겠습니다.

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

이전에 우리는 이 출력의 세 번째 필드를 간략하게 다루었습니다. 이 필드는 링크 개수입니다.

### Linux 의 링크 개수

**Linux 의 링크 개수**는 파일이 가진 하드 링크의 총 개수입니다. 이것이 무엇을 의미하는지 이해하려면 먼저 링크가 무엇인지 논의해야 합니다. Linux 에는 심볼릭 링크 (symlinks) 와 하드 링크의 두 가지 유형의 링크가 있습니다.

### 심볼릭 링크 이해하기

Windows 운영 체제에는 다른 파일을 가리키는 별칭인 바로 가기 (shortcuts) 가 있습니다. Linux 에서는 이것에 해당하는 것이 심볼릭 링크 (symbolic link) 이며, 소프트 링크 (soft link) 또는 **심링크 (symlink)**라고도 합니다. 심링크는 이름으로 다른 파일이나 디렉토리를 가리키는 특수한 유형의 파일입니다.

실제 예를 살펴보겠습니다. 몇 개의 파일을 만든 다음 심링크를 만들어 보겠습니다.

```bash
pete@icebox:~/Desktop$ echo 'myfile' > myfile
pete@icebox:~/Desktop$ echo 'myfile2' > myfile2
pete@icebox:~/Desktop$ echo 'myfile3' > myfile3

pete@icebox:~/Desktop$ ln -s myfile myfilelink
pete@icebox:~/Desktop$ ls -li
total 12
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
```

여기서 `myfile`을 가리키는 `myfilelink`라는 심볼릭 링크를 생성했습니다. `ls`를 사용하여 `ls symlink`를 볼 때, 권한 문자열 시작 부분의 `l`과 대상 (target) 을 가리키는 `->` 기호로 명확하게 식별됩니다. 심링크는 고유한 inode 번호 (93403) 를 가진다는 점에 유의하십시오. 심링크는 inode 가 아닌 파일 이름을 가리키기 때문에 다른 파일 시스템에 걸쳐 있을 수 있습니다.

### 하드 링크 이해하기

다른 유형의 링크는 하드 링크입니다. 하드 링크는 원본 파일과 동일한 inode 를 직접 가리키는 또 다른 파일 항목을 생성합니다.

`myfile2`에 대한 하드 링크를 만들어 보겠습니다.

```bash
pete@icebox:~/Desktop$ ln myfile2 myhardlink
pete@icebox:~/Desktop$ ls -li
total 16
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myhardlink
```

`myhardlink`가 `myfile2`와 정확히 동일한 inode 번호 (93401) 를 공유한다는 점에 유의하십시오. 두 파일의 링크 개수도 2 로 증가했습니다. 이는 두 개의 파일 항목이 이제 동일한 inode 를 가리키기 때문입니다. `myfile2`의 내용을 수정하면 `myhardlink`에도 변경 사항이 반영되며 그 반대도 마찬가지입니다. `myfile2`를 삭제하더라도 파일 데이터는 `myhardlink`를 통해 계속 액세스할 수 있습니다. inode 와 그 데이터는 링크 개수가 0 이 될 때까지 디스크에서 제거되지 않습니다. 하드 링크는 단일 파일 시스템 내에서 고유한 inode 를 가리키므로 다른 파일 시스템에 걸쳐 있을 수 없습니다.

### 심링크 및 하드 링크 생성하기

`ln` 명령을 사용하여 두 가지 유형의 링크를 모두 만들 수 있습니다. 구문은 간단합니다.

심볼릭 링크를 만들려면 `-s` 플래그를 사용합니다.

```bash
ln -s /path/to/original /path/to/link
```

하드 링크를 만들려면 `-s` 플래그를 생략합니다.

```bash
ln /path/to/original /path/to/link
```

이러한 다양한 파일 유형을 관리하고 식별하려면 `ls symlinks` 또는 일반적인 `ls links` 명령을 `-l` 옵션과 함께 사용하는 것이 필수적입니다.

## Exercise

연습이 완벽을 만듭니다! 파일 관리, 링크 및 inode 에 대한 이해를 강화하기 위한 몇 가지 실습 랩이 있습니다.

1. **[Linux 에서 파일 및 디렉터리 관리](https://labex.io/ko/labs/comptia-manage-files-and-directories-in-linux-590835)** - 파일 및 디렉터리 생성, 복사, 이동 및 제거를 연습하고, 특히 심볼릭 링크 및 하드 링크에 대해 알아보고 inode 를 분석하는 방법을 배웁니다.
2. **[Linux 파일 시스템 탐색](https://labex.io/ko/labs/comptia-navigate-the-filesystem-in-linux-590971)** - `pwd`, `cd`, `ls`와 같은 필수 명령을 마스터하여 Linux 파일 시스템을 효율적으로 이동하며, 파일과 inode 가 위치한 곳을 이해하기 위한 기본 기술을 익힙니다.

이 랩들은 파일 관리 및 링크 개념을 실제 시나리오에 적용하고 Linux 파일 시스템에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

심링크를 만드는 데 사용되는 명령과 기본 옵션은 무엇입니까? 귀하의 답변은 영어여야 하며 대소문자를 구분합니다. 명령과 옵션 사이에 공백을 포함해야 합니다.

## Quiz Answer

ln -s
