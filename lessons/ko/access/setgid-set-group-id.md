---
lang: "ko"
title: "Setgid"
meta_description: "Linux SGID (Set Group ID) 권한, 작동 방식 및 수정 방법을 알아보세요. 이 중요한 Linux 보안 개념을 이해합니다."
meta_keywords: "Linux SGID, Set Group ID, Linux permissions, chmod g+s, Linux security, beginner Linux, Linux tutorial"
---

## Lesson Content

Set user ID 권한 비트와 유사하게, set group ID (SGID) 권한 비트가 있습니다. 이 비트는 프로그램이 해당 그룹의 구성원인 것처럼 실행되도록 허용합니다.

다음 예시를 살펴보겠습니다:

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

이제 권한 비트가 그룹 권한 세트에 있음을 확인할 수 있습니다.

### Modifying SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

SGID 의 숫자 표현은 2 입니다.

## Exercise

No exercises for this lesson.

## Quiz Question

SGID 를 나타내는 숫자는 무엇입니까?

## Quiz Answer

2
