---
index: 8
lang: "ko"
title: "스티키 비트"
meta_title: "스티키 비트 - 권한"
meta_description: "Linux 스티키 비트, /tmp 와 같은 공유 디렉토리에서의 목적, 그리고 chmod 를 사용하여 설정하는 방법을 알아보세요. 이 핵심 파일 권한을 이해하세요!"
meta_keywords: "Linux 스티키 비트, chmod +t, /tmp 디렉토리, Linux 권한, 파일 보안, Linux 튜토리얼, Linux 초보자"
---

## Lesson Content

마지막으로 설명하고 싶은 특별한 권한 비트는 스티키 비트입니다.

이 권한 비트는 "파일/디렉토리를 고정"시킵니다. 즉, 소유자 또는 root 사용자만이 파일을 삭제하거나 수정할 수 있습니다. 이는 공유 디렉토리에 매우 유용합니다. 아래 예시를 살펴보세요:

```bash
$ ls -ld /tmp
drwxrwxrwx+t 6 root root 4096 Dec 15 11:45 /tmp
```

여기 끝에 특별한 권한 비트인 **t**가 보일 것입니다. 이는 모든 사람이 `/tmp` 디렉토리에 파일을 추가하고, 파일을 쓰고, 파일을 수정할 수 있지만, root 만이 `/tmp` 디렉토리를 삭제할 수 있음을 의미합니다.

### Modify sticky bit

```bash
sudo chmod +t mydir

sudo chmod 1755 mydir
```

스티키 비트의 숫자 표현은 **1**입니다.

## Exercise

어떤 다른 파일과 디렉토리에 스티키 비트가 활성화되어 있다고 생각하십니까?

## Quiz Question

스티키 비트를 나타내는 기호는 무엇입니까?

## Quiz Answer

t
