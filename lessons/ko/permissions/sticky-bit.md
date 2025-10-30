---
index: 8
lang: "ko"
title: "스티키 비트"
meta_title: "스티키 비트 - 권한"
meta_description: "Linux 스티키 비트, /tmp 와 같은 공유 디렉토리에서의 목적, chmod 를 사용하여 설정하는 방법을 알아보세요. 이 중요한 파일 권한을 이해하세요!"
meta_keywords: "Linux 스티키 비트, chmod +t, /tmp 디렉토리, Linux 권한, 파일 보안, Linux 튜토리얼, 초보자 Linux"
---

## Lesson Content

제가 이야기하고 싶은 마지막 특별 권한 비트는 스티키 비트입니다.

이 권한 비트는 "파일/디렉토리를 고정"시키는데, 이는 소유자 또는 root 사용자만이 파일을 삭제하거나 수정할 수 있음을 의미합니다. 이는 공유 디렉토리에 매우 유용합니다. 아래 예시를 살펴보세요:

```bash
$ ls -ld /tmp
drwxrwxrwx+t 6 root root 4096 Dec 15 11:45 /tmp
```

여기 끝에 특별한 권한 비트 **t**가 보일 것입니다. 이는 모든 사람이 `/tmp` 디렉토리에 파일을 추가하고, 파일을 쓰고, 파일을 수정할 수 있지만, root 만이 `/tmp` 디렉토리를 삭제할 수 있음을 의미합니다.

### 스티키 비트 수정

```bash
sudo chmod +t mydir

sudo chmod 1755 mydir
```

스티키 비트의 숫자 표현은 **1**입니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 파일 권한과 파일 및 디렉토리 관리에 미치는 영향을 이해하는 데 도움이 되는 실습 랩입니다:

1. **[Linux 사용자 그룹 및 파일 권한](https://labex.io/ko/labs/linux-linux-user-group-and-file-permissions-18002)** - 사용자 및 그룹 생성 및 관리, 파일 권한 이해, 파일 소유권 조작을 연습합니다. 이 랩은 스티키 비트와 같은 특별 권한이 어떻게 작동하는지 이해하기 위한 기초 지식을 제공합니다.
2. **[파일 삭제 및 이동](https://labex.io/ko/labs/linux-delete-and-move-files-7777)** - Linux 시스템에서 파일을 삭제하고 이동하는 방법을 배웁니다. 이 랩은 권한이 이러한 작업을 어떻게 제한할 수 있는지 포함하여 권한의 실제적인 의미를 이해하는 데 도움이 될 것입니다.
3. **[파일 찾기](https://labex.io/ko/labs/linux-find-a-file-17993)** - 파일을 찾고 접근 권한을 설정하는 것을 연습합니다. 이 랩은 파일 권한의 중요성과 파일 권한이 접근 및 수정을 제어하는 방법을 강화합니다.

이 랩들은 실제 시나리오에서 파일 권한 개념을 적용하고 Linux 에서 파일 접근을 관리하는 데 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

스티키 비트를 나타내는 기호는 무엇입니까?

## Quiz Answer

t
