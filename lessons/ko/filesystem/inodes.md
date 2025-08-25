---
index: 11
lang: "ko"
title: "Inodes"
meta_title: "Inodes - 파일 시스템"
meta_description: "Linux inode, 구조, 파일 관리 방법을 알아보세요. inode 번호를 이해하고 `df -i` 및 `ls -li`를 사용하여 inode 사용량을 확인하세요. Linux 여정을 시작하세요!"
meta_keywords: "Linux inode, inode 튜토리얼, df -i, ls -li, Linux 파일 시스템, 초보자 Linux, Linux 가이드"
---

## Lesson Content

파일 시스템이 실제 파일과 이 파일을 관리하는 데이터베이스로 구성되어 있다는 것을 기억하시나요? 이 데이터베이스는 inode 테이블로 알려져 있습니다.

### inode 란 무엇인가요?

inode(인덱스 노드) 는 이 테이블의 항목이며, 모든 파일에 대해 하나씩 존재합니다. inode 는 파일에 대한 모든 것을 설명합니다. 예를 들면 다음과 같습니다:

- 파일 유형 - 일반 파일, 디렉토리, 문자 장치 등
- 소유자
- 그룹
- 접근 권한
- 타임스탬프 - mtime (마지막 파일 수정 시간), ctime (마지막 속성 변경 시간), atime (마지막 접근 시간)
- 파일에 대한 하드링크 수
- 파일 크기
- 파일에 할당된 블록 수
- 파일의 데이터 블록에 대한 포인터 - 가장 중요합니다!

기본적으로 inode 는 파일 이름과 파일 자체를 제외한 파일에 대한 모든 것을 저장합니다!

### inode 는 언제 생성되나요?

파일 시스템이 생성될 때 inode 를 위한 공간도 할당됩니다. 알고리즘은 디스크 볼륨 등에 따라 필요한 inode 공간의 양을 결정합니다. 아마도 살면서 디스크 공간 부족 오류를 본 적이 있을 것입니다. inode 에서도 동일한 문제가 발생할 수 있으며 (덜 흔하지만), inode 가 부족하여 더 이상 파일을 생성할 수 없게 될 수 있습니다. 데이터 저장은 데이터와 데이터베이스 (inode) 모두에 달려 있다는 것을 기억하세요.

시스템에 남아 있는 inode 수를 확인하려면 `df -i` 명령을 사용하세요.

### Inode 정보

inode 는 숫자로 식별됩니다. 파일이 생성되면 inode 번호가 할당되며, 이 번호는 순차적으로 할당됩니다. 그러나 새 파일을 생성할 때 다른 파일보다 낮은 inode 번호를 얻는 경우가 있을 수 있습니다. 이는 inode 가 삭제되면 다른 파일에 의해 재사용될 수 있기 때문입니다. inode 번호를 보려면 `ls -li`를 실행하세요:

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

이 명령의 첫 번째 필드는 inode 번호를 나열합니다.

`stat` 명령으로 파일에 대한 자세한 정보를 볼 수도 있습니다. 이 명령은 inode 에 대한 정보도 알려줍니다.

```bash
pete@icebox:~$ stat ~/Desktop/
  File: ‘/home/pete/Desktop/’
  Size: 6               Blocks: 0          IO Block: 4096   directory
Device: 806h/2054d      Inode: 140         Links: 2
Access: (0755/drwxr-xr-x)  Uid: ( 1000/   pete)   Gid: ( 1000/   pete)
Access: 2016-01-20 20:13:50.647435982 -0800
Modify: 2016-01-20 20:13:06.191675843 -0800
Change: 2016-01-20 20:13:06.191675843 -0800
 Birth: -
```

### inode 는 파일을 어떻게 찾나요?

우리의 데이터가 디스크 어딘가에 있다는 것을 알고 있습니다. 불행히도, 데이터는 순차적으로 저장되지 않았을 가능성이 높으므로 inode 를 사용해야 합니다. inode 는 파일의 실제 데이터 블록을 가리킵니다. 일반적인 파일 시스템 (모든 파일 시스템이 동일하게 작동하는 것은 아님) 에서 각 inode 는 15 개의 포인터를 포함합니다. 처음 12 개의 포인터는 데이터 블록을 직접 가리킵니다. 13 번째 포인터는 더 많은 블록에 대한 포인터를 포함하는 블록을 가리키고, 14 번째 포인터는 또 다른 중첩된 포인터 블록을 가리키며, 15 번째 포인터는 또 다시 다른 포인터 블록을 가리킵니다! 혼란스럽다는 것을 압니다! 이렇게 하는 이유는 모든 inode 에 대해 inode 구조를 동일하게 유지하면서도 다양한 크기의 파일을 참조할 수 있도록 하기 위함입니다. 작은 파일이 있다면 처음 12 개의 직접 포인터로 더 빨리 찾을 수 있습니다. 더 큰 파일은 중첩된 포인터로 찾을 수 있습니다. 어떤 경우든 inode 의 구조는 동일합니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 파일 시스템 및 파일 관리에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 파일 및 디렉토리 관리](https://labex.io/ko/labs/comptia-manage-files-and-directories-in-linux-590835)** - 파일 및 디렉토리 생성, 제거, 복사, 이동을 연습하고, inode 를 분석하면서 심볼릭 및 하드 링크 생성을 탐색합니다.
2. **[Linux 에서 파일 시스템 탐색](https://labex.io/ko/labs/comptia-navigate-the-filesystem-in-linux-590971)** - `pwd`, `cd`, `ls`와 같은 필수 셸 명령을 사용하여 Linux 파일 시스템을 탐색하는 기본 기술을 배웁니다.
3. **[Linux 에서 파일 및 명령 찾기](https://labex.io/ko/labs/comptia-find-files-and-commands-in-linux-590834)** - `find`, `locate`, `whereis`, `which`, `type`을 사용하여 Linux 에서 파일 및 명령을 찾는 필수 기술을 마스터합니다.

이 랩은 실제 시나리오에서 개념을 적용하고 Linux 파일 시스템 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

시스템에 남아 있는 inode 수를 어떻게 확인할 수 있나요?

## Quiz Answer

df -i
