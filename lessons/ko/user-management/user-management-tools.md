---
index: 6
lang: "ko"
title: "사용자 관리 도구"
meta_title: "사용자 관리 도구 - 사용자 관리"
meta_description: "useradd, userdel, passwd 명령을 사용하여 Linux 사용자 관리: 추가, 제거 및 암호 변경을 배웁니다. 이 초보자 친화적인 가이드로 시작하세요!"
meta_keywords: "Linux 사용자 관리, adduser, userdel, passwd, Linux 튜토리얼, 초보자 Linux, 사용자 계정, Linux 명령"
---

## Lesson Content

대부분의 기업 환경에서는 사용자, 계정 및 암호를 관리하기 위해 관리 시스템을 사용합니다. 그러나 단일 머신 컴퓨터에서는 사용자를 관리하는 데 유용한 명령이 있습니다.

### 사용자 추가

`adduser` 또는 `useradd` 명령을 사용할 수 있습니다. `adduser` 명령은 홈 디렉터리를 만들고 더 많은 유용한 기능을 포함합니다. 기본 사용자에게 할당하려는 내용에 따라 사용자 정의할 수 있는 새 사용자 추가를 위한 구성 파일이 있습니다.

```bash
sudo useradd bob
```

위 명령은 bob 에 대한 `/etc/passwd`에 항목을 생성하고, 기본 그룹을 설정하며, `/etc/shadow` 파일에 항목을 추가합니다.

### 사용자 제거

사용자를 제거하려면 `userdel` 명령을 사용할 수 있습니다.

```bash
sudo userdel bob
```

이것은 기본적으로 `useradd`에 의해 변경된 파일을 되돌리기 위해 최선을 다합니다.

### 암호 변경

```bash
passwd bob
```

이것은 자신 또는 다른 사용자 (루트인 경우) 의 암호를 변경할 수 있도록 합니다.

## Exercise

연습은 완벽을 만듭니다! 다음은 Linux 에서 사용자 및 계정 관리에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[useradd, usermod 및 userdel 을 사용하여 Linux 사용자 계정 관리](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성 및 보안 설정부터 수정 및 삭제에 이르기까지 사용자 관리의 전체 수명 주기를 연습합니다.
2. **[groupadd, usermod 및 groupdel 을 사용하여 Linux 그룹 관리](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 그룹 추가, 수정 및 삭제를 포함하여 그룹 관리를 위한 핵심 명령줄 유틸리티에 대한 실습 경험을 얻습니다.
3. **[Linux 에서 사용자 계정 및 Sudo 권한 구성](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Linux 시스템의 보안을 강화하기 위한 사용자 계정 및 sudo 권한 관리에 대한 필수 기술을 배웁니다.

이러한 랩은 실제 시나리오에 개념을 적용하고 Linux 사용자 및 그룹 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

암호를 변경하는 데 사용되는 명령은 무엇입니까?

## Quiz Answer

passwd
