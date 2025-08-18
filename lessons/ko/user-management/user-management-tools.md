---
lang: "ko"
title: "사용자 관리 도구"
meta_title: "사용자 관리 도구 - 사용자 관리"
meta_description: "Linux 사용자 관리 배우기: useradd, userdel, passwd 명령으로 사용자 추가, 제거 및 암호 변경. 이 초보자 친화적인 가이드로 시작하세요!"
meta_keywords: "Linux 사용자 관리, adduser, userdel, passwd, Linux 튜토리얼, 초보자 Linux, 사용자 계정, Linux 명령"
---

## Lesson Content

대부분의 기업 환경에서는 사용자, 계정 및 암호를 관리하기 위해 관리 시스템을 사용합니다. 그러나 단일 머신 컴퓨터에서는 사용자를 관리하는 데 유용한 명령이 있습니다.

### Adding Users

`adduser` 또는 `useradd` 명령을 사용할 수 있습니다. `adduser` 명령은 홈 디렉터리 생성과 같은 더 유용한 기능을 포함합니다. 새 사용자를 추가하기 위한 구성 파일은 기본 사용자에게 할당하려는 내용에 따라 사용자 정의할 수 있습니다.

```bash
sudo useradd bob
```

위 명령은 bob 을 위해 `/etc/passwd`에 항목을 생성하고, 기본 그룹을 설정하며, `/etc/shadow` 파일에 항목을 추가하는 것을 볼 수 있습니다.

### Removing Users

사용자를 제거하려면 `userdel` 명령을 사용할 수 있습니다.

```bash
sudo userdel bob
```

이것은 기본적으로 `useradd`에 의해 변경된 파일들을 되돌리기 위해 최선을 다합니다.

### Changing Passwords

```bash
passwd bob
```

이것은 자신 또는 다른 사용자 (루트인 경우) 의 암호를 변경할 수 있도록 합니다.

## Exercise

새 사용자를 생성한 다음 암호를 변경하고 새 사용자로 로그인하십시오.

## Quiz Question

암호를 변경하는 데 사용되는 명령은 무엇입니까?

## Quiz Answer

passwd
