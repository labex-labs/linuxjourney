---
index: 6
lang: "ko"
title: "Setgid"
meta_title: "Setgid - 권한"
meta_description: "Linux SGID(Set Group ID) 권한, 작동 방식 및 수정 방법을 알아보세요. 이 중요한 Linux 보안 개념을 이해하세요."
meta_keywords: "Linux SGID, Set Group ID, Linux 권한, chmod g+s, Linux 보안, 초보자 Linux, Linux 튜토리얼"
---

## Lesson Content

Set user ID 권한 비트와 유사하게, set group ID (SGID) 권한 비트가 있습니다. 이 비트는 프로그램이 해당 그룹의 구성원인 것처럼 실행되도록 허용합니다.

예시를 살펴보겠습니다:

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

이제 권한 비트가 그룹 권한 세트에 있음을 확인할 수 있습니다.

### SGID 수정하기

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

SGID 의 숫자 표현은 2 입니다.

## Exercise

연습하면 완벽해집니다! 다음은 Linux 사용자, 그룹 및 파일 권한에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 사용자 그룹 및 파일 권한](https://labex.io/ko/labs/linux-linux-user-group-and-file-permissions-18002)** - 사용자 생성 및 관리, 그룹 멤버십 탐색, 파일 권한 이해, 파일 소유권 조작을 포함한 필수 Linux 사용자 및 그룹 관리 개념을 배웁니다.
2. **[새 사용자 및 그룹 추가](https://labex.io/ko/labs/linux-add-new-user-and-group-17987)** - 새로운 사용자 계정 생성, 사용자 지정 그룹 설정, 그룹 멤버십 관리를 연습하여 실제 시스템 관리 작업을 시뮬레이션합니다.

이 랩들은 실제 시나리오에 개념을 적용하고 Linux 권한 및 사용자 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

SGID 를 나타내는 숫자는 무엇입니까?

## Quiz Answer

2
