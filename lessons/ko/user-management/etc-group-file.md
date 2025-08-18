---
index: 5
lang: "ko"
title: "/etc/group"
meta_title: "/etc/group - 사용자 관리"
meta_description: "Linux 의 /etc/group 파일에 대해 알아보고, 그룹 관리, GID, 사용자 권한을 이해합니다. 초보자를 위한 필수 Linux 그룹 파일 튜토리얼입니다."
meta_keywords: "/etc/group, Linux 그룹, 그룹 관리, GID, Linux 권한, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

사용자 관리에 사용되는 또 다른 파일은 `/etc/group` 파일입니다. 이 파일을 통해 다양한 권한을 가진 여러 그룹을 만들 수 있습니다.

```bash
$ cat /etc/group

root:*:0:pete
```

`/etc/passwd` 파일과 매우 유사하게, `/etc/group` 필드는 다음과 같습니다:

1. 그룹 이름
2. 그룹 비밀번호 - 그룹 비밀번호를 설정할 필요는 없으며, `sudo`와 같은 상승된 권한을 사용하는 것이 일반적입니다. 기본값으로 별표 (`*`) 가 표시됩니다.
3. 그룹 ID (GID)
4. 사용자 목록 - 특정 그룹에 포함시키려는 사용자를 수동으로 지정할 수 있습니다.

## Exercise

`groups` 명령을 실행해 보세요. 무엇이 보이나요?

## Quiz Question

root 의 GID 는 무엇인가요?

## Quiz Answer

0
