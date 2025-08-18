---
index: 2
lang: "ko"
title: "root"
meta_title: "root - 사용자 관리"
meta_description: "Linux root 사용자, su 명령, /etc/sudoers 파일에 대해 알아보세요. 이 초보자 가이드를 통해 Linux 의 슈퍼유저 접근 및 권한을 이해하세요."
meta_keywords: "Linux root, su command, sudoers file, Linux permissions, superuser, Linux tutorial, beginner guide"
---

## Lesson Content

`sudo` 명령을 사용하여 슈퍼유저 권한을 얻는 한 가지 방법을 살펴보았습니다. `su` 명령을 사용하여 슈퍼유저로 명령을 실행할 수도 있습니다. 이 명령은 사용자 이름을 지정하지 않으면 "사용자를 대체"하고 root 셸을 엽니다. 암호를 알고 있다면 이 명령을 사용하여 어떤 사용자든 대체할 수 있습니다.

```bash
su
```

이 방법을 사용하는 데는 몇 가지 단점이 있습니다. 모든 것을 root 로 실행하면 치명적인 실수를 저지르기 훨씬 쉽고, 시스템 구성을 변경하는 데 사용한 명령 기록이 남지 않습니다. 기본적으로 슈퍼유저로 명령을 실행해야 한다면 `sudo`를 고수하세요.

이제 슈퍼유저로 실행할 명령을 알았으니, 누가 그 권한을 가지고 있는지 어떻게 알 수 있을까요? 시스템은 모든 사람이 슈퍼유저로 명령을 실행하도록 허용하지 않는데, 어떻게 알 수 있을까요? `/etc/sudoers`라는 파일이 있습니다. 이 파일은 `sudo`를 실행할 수 있는 사용자를 나열합니다. 이 파일은 **visudo** 명령으로 편집할 수 있습니다.

## Exercise

`/etc/sudoers` 파일을 열고 머신의 다른 사용자들이 어떤 슈퍼유저 권한을 가지고 있는지 확인하세요.

## Quiz Question

`sudo`에 접근할 수 있는 사용자를 보여주는 파일은 무엇입니까?

## Quiz Answer

/etc/sudoers
