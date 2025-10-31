---
index: 5
lang: "ko"
title: "/etc/group"
meta_title: "/etc/group - 사용자 관리"
meta_description: "리눅스에서 그룹 관리를 이해하기 위해 /etc/group 파일을 탐색합니다. cat /etc/group으로 그룹 데이터를 보는 방법과 GID 및 사용자 목록을 포함한 구조를 이해합니다. 이 가이드는 etc group linux 파일의 필수 사항을 다룹니다."
meta_keywords: "/etc/group, /etc/group 리눅스, /etc/group 파일 리눅스, cat /etc/group, etc group 리눅스, 그룹 관리, GID, 리눅스 권한, 리눅스 그룹"
---

## Lesson Content

Linux 에서는 여러 사용자에 대한 권한 관리가 그룹 사용을 통해 간소화됩니다. 이를 위한 핵심 파일은 시스템의 그룹과 해당 멤버를 정의하는 `/etc/group`입니다.

### /etc/group 파일이란?

Linux 의 `/etc/group` 파일은 모든 사용자 그룹 목록을 포함하는 일반 텍스트 파일입니다. 각 그룹에는 파일 및 디렉터리에 대한 특정 권한이 할당될 수 있으므로 관리자는 여러 사용자에게 한 번에 효율적으로 액세스 권한을 관리할 수 있습니다. 이 파일을 이해하는 것은 모든 `etc group linux` 환경에서 적절한 사용자 및 권한 관리를 위해 매우 중요합니다.

### 그룹 정보 보기

이 파일의 내용을 검사하려면 간단한 명령을 사용할 수 있습니다. 터미널에서 `cat /etc/group`을 실행하면 시스템의 모든 그룹 정의가 표시됩니다.

```bash
$ cat /etc/group

root:*:0:pete
```

### /etc/group 파일의 구조

`/etc/passwd` 파일과 유사하게, `/etc/group` 파일의 각 줄은 단일 그룹을 나타내며 콜론 (`:`) 으로 구분된 네 개의 필드를 포함합니다.

1. **그룹 이름**: 그룹의 고유 이름입니다.
2. **그룹 암호**: 이 필드는 레거시 기능이며 거의 사용되지 않습니다. 최신 시스템은 그룹 암호 대신 `sudo`와 같은 도구를 사용하여 권한을 높입니다. 일반적으로 별표 (`*`) 또는 'x'와 같은 자리 표시자를 보게 됩니다.
3. **그룹 ID (GID)**: 그룹에 대한 고유한 숫자 식별자입니다. 시스템은 그룹 이름 대신 내부적으로 GID 를 사용하는 경우가 많습니다.
4. **사용자 목록**: 이 그룹의 멤버인 사용자 이름의 쉼표로 구분된 목록입니다.

예시 `root:*:0:pete`에서 그룹 이름은 `root`이고, 암호는 없으며, GID 는 `0`이고, 사용자 `pete`가 멤버입니다.

## Exercise

연습이 완벽함을 만듭니다! Linux 사용자 및 그룹 관리에 대한 이해를 강화하기 위한 몇 가지 실습 랩이 있습니다.

1. **[useradd, usermod 및 userdel 로 Linux 사용자 계정 관리](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성 및 보안부터 수정 및 삭제에 이르기까지 사용자 관리의 전체 수명 주기를 연습합니다.
2. **[groupadd, usermod 및 groupdel 로 Linux 그룹 관리](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - `groupadd`, `usermod`, `groupdel`을 포함하여 그룹 관리를 위한 핵심 명령줄 유틸리티에 대한 실습 경험을 얻습니다.
3. **[새 사용자 및 그룹 추가](https://labex.io/ko/labs/linux-add-new-user-and-group-17987)** - 새 사용자 계정을 생성하고, 사용자 지정 그룹을 설정하고, 그룹 멤버십을 관리하여 서버 환경에 새 팀원을 추가하는 것을 시뮬레이션합니다.

이러한 랩은 실제 시나리오에서 개념을 적용하고 Linux 사용자 및 그룹 관리에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

root 의 GID 는 무엇입니까?

## Quiz Answer

0
