---
lang: "ko"
title: "Inode"
meta_title: "Inode - 파일 시스템"
meta_description: "Linux inode, 그 구조, 그리고 파일 관리 방법을 배우세요. inode 번호를 이해하고 `df -i` 및 `ls -li`를 사용하여 inode 사용량을 확인하세요. Linux 여정을 시작하세요!"
meta_keywords: "Linux inode, inode 튜토리얼, df -i, ls -li, Linux 파일 시스템, Linux 초보자, Linux 가이드"
---

## Lesson Content

우리의 파일 시스템이 실제 파일과 이 파일들을 관리하는 데이터베이스로 구성되어 있다는 것을 기억하시나요? 이 데이터베이스는 inode 테이블이라고 알려져 있습니다.

### Inode 란 무엇인가요?

inode (index node) 는 이 테이블의 항목이며, 모든 파일에 대해 하나씩 존재합니다. inode 는 파일에 대한 모든 것을 설명합니다. 예를 들면:

- 파일 유형 - regular file, directory, character device 등
- Owner
- Group
- Access permissions
- Timestamps - mtime (마지막 파일 수정 시간), ctime (마지막 속성 변경 시간), atime (마지막 접근 시간)
- 파일에 대한 hardlinks 수
- 파일의 Size
- 파일에 할당된 blocks 수
- 파일의 data blocks 에 대한 Pointers - 가장 중요합니다!

기본적으로 inode 는 파일 이름과 파일 자체를 제외한 파일에 대한 모든 것을 저장합니다!

### Inode 는 언제 생성되나요?

파일 시스템이 생성될 때, inode 를 위한 공간도 함께 할당됩니다. 알고리즘은 디스크의 볼륨 등에 따라 필요한 inode 공간의 양을 결정합니다. 아마도 인생의 어느 시점에서 디스크 공간 부족 오류를 본 적이 있을 것입니다. inode 에서도 동일한 상황이 발생할 수 있습니다 (덜 흔하지만). inode 가 부족하여 더 이상 파일을 생성할 수 없는 경우가 발생할 수 있습니다. 데이터 저장은 데이터와 데이터베이스 (inodes) 모두에 달려 있다는 것을 기억하세요.

시스템에 남아있는 inode 수를 확인하려면 `df -i` 명령어를 사용하세요.

### Inode 정보

inode 는 숫자로 식별됩니다. 파일이 생성될 때 inode 번호가 할당되며, 이 번호는 순차적으로 할당됩니다. 그러나 새 파일을 생성할 때 다른 파일보다 낮은 inode 번호를 얻는 것을 가끔 발견할 수 있습니다. 이는 inode 가 삭제되면 다른 파일에 의해 재사용될 수 있기 때문입니다. inode 번호를 보려면 `ls -li`를 실행하세요:

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

이 명령어의 첫 번째 필드는 inode 번호를 나열합니다.

`stat` 명령어로 파일에 대한 자세한 정보를 볼 수도 있습니다. 이 명령어는 inode 에 대한 정보도 알려줍니다.

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

### Inode 는 어떻게 파일을 찾나요?

우리의 데이터는 디스크 어딘가에 있다는 것을 알고 있습니다. 불행히도, 데이터는 순차적으로 저장되지 않았을 가능성이 높으므로 inode 를 사용해야 합니다. inode 는 파일의 실제 data blocks 을 가리킵니다. 일반적인 파일 시스템 (모든 파일 시스템이 동일하게 작동하는 것은 아님) 에서 각 inode 는 15 개의 포인터를 포함합니다. 처음 12 개의 포인터는 data blocks 을 직접 가리킵니다. 13 번째 포인터는 더 많은 블록을 가리키는 포인터를 포함하는 블록을 가리키고, 14 번째 포인터는 또 다른 중첩된 포인터 블록을 가리키며, 15 번째 포인터는 또 다시 다른 포인터 블록을 가리킵니다! 혼란스럽다는 것을 압니다! 이렇게 하는 이유는 모든 inode 에 대해 inode 구조를 동일하게 유지하면서도 다른 크기의 파일을 참조할 수 있도록 하기 위함입니다. 작은 파일이 있다면 처음 12 개의 직접 포인터로 더 빨리 찾을 수 있습니다. 더 큰 파일은 포인터의 중첩을 통해 찾을 수 있습니다. 어떤 경우든 inode 의 구조는 동일합니다.

## Exercise

다양한 파일의 inode 번호를 관찰해 보세요. 어떤 파일이 일반적으로 먼저 생성될까요?

## Quiz Question

시스템에 남아있는 inode 수를 어떻게 확인할 수 있나요?

## Quiz Answer

df -i
