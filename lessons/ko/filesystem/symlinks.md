---
index: 12
lang: "ko"
title: "심링크"
meta_title: "심링크 - 파일 시스템"
meta_description: "Linux 심링크와 하드 링크에 대해 배우고, 생성 및 관리 방법을 익힙니다. 이 초보자 친화적인 가이드를 통해 차이점과 사용 사례를 이해하세요."
meta_keywords: "Linux 심링크, 하드 링크, ln 명령어, 심볼릭 링크, Linux 파일 시스템, Linux 튜토리얼, 초보자 Linux"
---

## Lesson Content

이전 inode 정보 예시를 사용해 봅시다:

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

`ls` 명령어의 세 번째 필드를 우리가 간과하고 있었다는 것을 눈치챘을 수도 있습니다. 이 필드는 링크 카운트입니다. 링크 카운트는 파일이 가진 하드 링크의 총 개수입니다. 현재로서는 이것이 아무 의미가 없을 테니, 먼저 링크에 대해 논의해 봅시다.

### Symlinks

Windows 운영 체제에는 바로 가기 (shortcuts) 라는 것이 있습니다. 바로 가기는 다른 파일에 대한 별칭일 뿐입니다. 원본 파일에 어떤 작업을 수행하면 바로 가기가 손상될 수 있습니다. Linux 에서 바로 가기에 해당하는 것은 심볼릭 링크 (symbolic links, 또는 소프트 링크 soft links, 또는 심링크 symlinks) 입니다. 심링크를 사용하면 파일 이름으로 다른 파일에 링크할 수 있습니다. Linux 에서 찾을 수 있는 또 다른 유형의 링크는 하드 링크 (hard links) 입니다. 이것들은 실제로 inode 에 대한 링크를 가진 또 다른 파일입니다. 심링크부터 시작하여 실제로 어떤 의미인지 살펴보겠습니다.

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

`myfile`을 가리키는 `myfilelink`라는 심볼릭 링크를 만들었습니다. 심볼릭 링크는 `->`로 표시됩니다. 하지만 새로운 inode 번호를 얻었다는 점에 주목하십시오. 심링크는 파일 이름을 가리키는 파일일 뿐입니다. 심링크를 수정하면 파일도 수정됩니다. Inode 번호는 파일 시스템에 고유합니다. 단일 파일 시스템 내에서 동일한 inode 번호를 두 개 가질 수 없으며, 이는 다른 파일 시스템의 파일을 inode 번호로 참조할 수 없다는 의미입니다. 그러나 심링크를 사용하면 inode 번호를 사용하지 않고 파일 이름을 사용하므로 다른 파일 시스템 간에도 참조할 수 있습니다.

### Hardlinks

하드 링크의 예시를 살펴보겠습니다:

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

하드 링크는 동일한 inode 에 대한 링크를 가진 또 다른 파일을 생성할 뿐입니다. 따라서 `myfile2` 또는 `myhardlink`의 내용을 수정하면 두 곳 모두에서 변경 사항이 반영됩니다. 하지만 `myfile2`를 삭제하더라도 `myhardlink`를 통해 파일에 계속 접근할 수 있습니다. 여기서 `ls` 명령어의 링크 카운트가 중요해집니다. 링크 카운트는 inode 가 가진 하드 링크의 수입니다. 파일을 제거하면 링크 카운트가 감소합니다. Inode 는 inode 에 대한 모든 하드 링크가 삭제될 때만 삭제됩니다. 파일을 생성하면 해당 inode 를 가리키는 유일한 파일이므로 링크 카운트는 1 이 됩니다. 심링크와 달리 하드 링크는 inode 가 파일 시스템에 고유하므로 파일 시스템을 넘나들 수 없습니다.

### Creating a symlink

```bash
ln -s myfile mylink
```

심볼릭 링크를 생성하려면 `ln` 명령어를 사용하고 심볼릭을 의미하는 `-s` 옵션을 사용하며, 대상 파일과 링크 이름을 지정합니다.

### Creating a hardlink

```bash
ln somefile somelink
```

심링크 생성과 유사하지만, 이번에는 `-s`를 생략합니다.

## Exercise

심링크와 하드 링크를 만들고 가지고 놀아보세요. 몇 개를 삭제하고 어떤 일이 일어나는지 확인해보세요.

## Quiz Question

심링크를 만드는 데 사용되는 명령어는 무엇입니까?

## Quiz Answer

ln -s
