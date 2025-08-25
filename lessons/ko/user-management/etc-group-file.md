---
index: 5
lang: "ko"
title: "/etc/group"
meta_title: "/etc/group - 사용자 관리"
meta_description: "Linux 의 /etc/group 파일에 대해 알아보고, 그룹 관리, GID 및 사용자 권한을 이해합니다. 초보자를 위한 필수 Linux 그룹 파일 튜토리얼입니다."
meta_keywords: "/etc/group, Linux 그룹, 그룹 관리, GID, Linux 권한, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

사용자 관리에 사용되는 또 다른 파일은 `/etc/group` 파일입니다. 이 파일은 서로 다른 권한을 가진 다양한 그룹을 허용합니다.

```bash
$ cat /etc/group

root:*:0:pete
```

`/etc/passwd` 파일과 매우 유사하게, `/etc/group` 필드는 다음과 같습니다:

1. 그룹 이름
2. 그룹 암호 - 그룹 암호를 설정할 필요는 없으며, `sudo`와 같은 상승된 권한을 사용하는 것이 일반적입니다. 기본값으로 별표 (`*`) 가 표시됩니다.
3. 그룹 ID (GID)
4. 사용자 목록 - 특정 그룹에 포함시키려는 사용자를 수동으로 지정할 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 사용자 및 그룹 관리에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[useradd, usermod, userdel 을 사용하여 Linux 사용자 계정 관리](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성 및 보안 설정부터 수정 및 삭제에 이르기까지 사용자 관리의 전체 수명 주기를 연습합니다.
2. **[groupadd, usermod, groupdel 을 사용하여 Linux 그룹 관리](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - `groupadd`, `usermod`, `groupdel`을 포함한 그룹 관리를 위한 핵심 명령줄 유틸리티를 직접 경험해 보세요.
3. **[새 사용자 및 그룹 추가](https://labex.io/ko/labs/linux-add-new-user-and-group-17987)** - 새 사용자 계정을 생성하고, 사용자 지정 그룹을 설정하고, 그룹 멤버십을 관리하여 서버 환경에 새 팀원을 추가하는 것을 시뮬레이션합니다.

이러한 랩은 실제 시나리오에 개념을 적용하고 Linux 사용자 및 그룹 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

root 의 GID 는 무엇입니까?

## Quiz Answer

0
