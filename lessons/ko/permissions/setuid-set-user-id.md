---
index: 5
lang: "ko"
title: "Setuid"
meta_title: "Setuid - 권한"
meta_description: "Linux Setuid (SUID) 권한, 작동 방식 및 수정 방법을 알아보세요. Linux 에서 안전한 파일 접근을 위한 SUID 를 이해하세요."
meta_keywords: "Linux Setuid, SUID, Linux 권한, chmod, passwd 명령어, Linux 보안, 초보자 Linux, Linux 튜토리얼"
---

## Lesson Content

일반 사용자가 작업을 수행하기 위해 권한 상승이 필요한 경우가 많습니다. 시스템 관리자가 사용자가 보호된 파일에 접근해야 할 때마다 루트 암호를 입력할 수는 없으므로, 이러한 동작을 허용하는 특별한 파일 권한 비트가 있습니다. Set User ID (SUID) 는 사용자가 프로그램 파일의 소유자로서 프로그램을 실행할 수 있도록 허용하며, 사용자 자신으로서 실행하는 것이 아닙니다.

예시를 살펴보겠습니다:

비밀번호를 변경하고 싶다고 가정해 봅시다. 간단하죠? `passwd` 명령어를 사용하면 됩니다:

```bash
passwd
```

`passwd` 명령어는 무엇을 할까요? 몇몇 파일을 수정하지만, 가장 중요한 것은 `/etc/shadow` 파일을 수정한다는 것입니다. 잠시 그 파일을 살펴보겠습니다:

```bash
$ ls -l /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

잠깐, 이 파일은 root 가 소유하고 있나요? root 가 소유한 파일을 어떻게 수정할 수 있을까요?

이번에는 우리가 실행한 명령어의 다른 권한 설정을 살펴보겠습니다:

```bash
$ ls -l /usr/bin/passwd

-rwsr-xr-x 1 root root 47032 Dec 1 11:45 /usr/bin/passwd
```

여기서 새로운 권한 비트인 **s**를 발견할 수 있습니다. 이 권한 비트가 SUID 입니다. 파일에 이 권한이 설정되면, 프로그램을 실행한 사용자는 파일 소유자의 권한과 실행 권한을 얻게 됩니다. 이 경우 root 입니다. 따라서 본질적으로 사용자가 `passwd` 명령어를 실행하는 동안에는 root 로 실행되는 것입니다.

이것이 우리가 `passwd` 명령어를 실행할 때 `/etc/shadow`와 같은 보호된 파일에 접근할 수 있는 이유입니다. 만약 이 비트를 제거하면, `/etc/shadow`를 수정할 수 없게 되어 비밀번호를 변경할 수 없게 됩니다.

### SUID 수정하기

일반 권한과 마찬가지로 SUID 권한을 수정하는 두 가지 방법이 있습니다.

_심볼릭 방식:_

```bash
sudo chmod u+s myfile
```

_숫자 방식:_

```bash
sudo chmod 4755 myfile
```

보시다시피, SUID 는 4 로 표시되며 권한 설정 앞에 붙습니다. SUID 가 대문자 **S**로 표시되는 것을 볼 수도 있습니다. 이는 동일한 작업을 수행하지만 실행 권한이 없음을 의미합니다.

## Exercise

연습하면 완벽해집니다! 파일 권한, 사용자 그룹, 그리고 SUID 와 같은 특수 비트가 어떻게 작동하는지 이해하는 것은 Linux 시스템을 관리하고 보호하는 데 매우 중요합니다. 직접 경험하는 것이 지식을 굳건히 할 것입니다.

파일 권한 및 사용자 관리에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 사용자 그룹 및 파일 권한](https://labex.io/ko/labs/linux-linux-user-group-and-file-permissions-18002)** - 사용자 및 그룹 생성 및 관리, 파일 권한 이해, 파일 소유권 조작을 연습합니다. 이 랩은 SUID 가 권한 상승을 위해 이러한 개념을 어떻게 활용하는지 파악하는 데 필요한 기초 지식을 제공합니다.

이 랩은 실제 시나리오에서 개념을 적용하고 Linux 사용자 및 파일 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

SUID 를 나타내는 숫자는 무엇입니까?

## Quiz Answer

4
