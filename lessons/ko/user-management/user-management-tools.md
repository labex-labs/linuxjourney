---
index: 6
lang: "ko"
title: "사용자 관리 도구"
meta_title: "사용자 관리 도구 - 사용자 관리"
meta_description: "필수 명령줄 도구로 Linux 사용자 관리를 마스터하세요. 이 가이드는 Linux 에서 계정 관리를 위한 useradd, userdel, passwd 사용법을 다루며 초보자에게 적합합니다."
meta_keywords: "리눅스 사용자 관리, 리눅스 계정 관리 명령줄 도구, useradd, userdel, passwd, 리눅스 계정, 리눅스 사용자 관리"
---

## Lesson Content

많은 엔터프라이즈 환경에서 전용 시스템에 의존하지만, 단일 머신에서 **Linux 사용자 관리**의 기본 사항을 이해하는 것은 중요한 기술입니다. 여러 유틸리티가 **Linux 에서 계정을 관리하기 위한 명령줄 도구** 역할을 하며 터미널에서 효율적인 관리를 가능하게 합니다.

### 사용자 추가

새 사용자를 생성하려면 `useradd` 명령을 사용할 수 있습니다. 이는 `/etc/default/useradd`에 있는 기본값을 기반으로 새 사용자 계정을 생성하는 저수준 유틸리티입니다. 일부 시스템에서는 보다 대화식이고 사용자 친화적인 스크립트인 `adduser`도 제공하지만, `useradd`가 보편적인 표준입니다.

```bash
sudo useradd bob
```

이 명령을 실행하면 사용자 "bob"에 대한 항목이 `/etc/passwd` 파일에 추가되고, 기본 그룹 멤버십이 설정되며, 암호 정보를 안전하게 저장하기 위해 `/etc/shadow` 파일에 해당 항목이 생성됩니다.

### 사용자 제거

사용자 계정을 제거하려면 `userdel` 명령을 사용할 수 있습니다. 이 명령은 `useradd`로 만든 변경 사항을 사용자 계정 파일에서 사용자를 제거하여 효과적으로 되돌립니다.

```bash
sudo userdel bob
```

기본적으로 이 명령은 사용자의 홈 디렉터리를 제거하지 않을 수 있습니다. 홈 디렉터리와 메일 스풀도 삭제되도록 하려면 `-r` 플래그 (`userdel -r bob`) 를 사용할 수 있습니다.

### 암호 변경

`passwd` 명령은 사용자의 암호를 설정하거나 변경하는 데 사용됩니다. 일반 사용자는 이 명령을 실행하여 자신의 암호를 변경할 수 있습니다. 루트 사용자는 이 명령을 실행하여 모든 사용자의 암호를 변경할 수 있습니다.

```bash
passwd bob
```

관리자가 실행하면 시스템은 이전 암호를 묻지 않고 지정된 사용자에 대한 새 암호를 요청합니다. 이는 **Linux 사용자 관리**의 기본 작업입니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 에서 사용자 및 계정 관리에 대한 이해를 강화하기 위한 실습 랩입니다.

1. **[useradd, usermod 및 userdel 을 사용하여 Linux 사용자 계정 관리](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성 및 보안부터 수정 및 삭제에 이르기까지 사용자 관리의 전체 수명 주기를 연습합니다.
2. **[groupadd, usermod 및 groupdel 을 사용하여 Linux 그룹 관리](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 그룹 추가, 수정 및 삭제를 포함하여 그룹 관리를 위한 핵심 명령줄 유틸리티에 대한 실습 경험을 얻습니다.
3. **[Linux 에서 사용자 계정 및 Sudo 권한 구성](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Linux 시스템 보안 강화를 위한 사용자 계정 및 sudo 권한 관리의 필수 기술을 배웁니다.

이 랩들은 실제 시나리오에서 개념을 적용하고 Linux 사용자 및 그룹 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

암호를 변경하는 데 사용되는 명령은 무엇입니까? 소문자로 된 영어 명령 이름만으로 답하십시오.

## Quiz Answer

passwd
