---
lang: "ko"
title: "yum 과 apt"
description: "Linux 패키지 관리를 위한 yum 과 apt 를 배우세요. 이 초보자 튜토리얼을 통해 Debian/RPM 시스템에서 소프트웨어를 설치, 제거 및 업데이트하세요. 오늘 시작하세요!"
keywords: "yum, apt, Linux 패키지 관리, apt 튜토리얼, yum 튜토리얼, Linux 명령, 초보자 가이드, 패키지 설치"
---

## Lesson Content

아, 패키지 관리의 배트맨들! 이 시스템들은 패키지 종속성 설치를 포함하여 패키지 설치, 제거 및 변경을 더 쉽게 할 수 있는 모든 기능을 제공합니다. 가장 인기 있는 두 가지 관리 시스템은 **yum**과 **apt**입니다. Yum 은 Red Hat 계열에만 해당하며, apt 는 Debian 계열에만 해당합니다.

### Install a package from a repository

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### Remove a package

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### Updating packages for a repository

패키지를 설치하고 업데이트하기 전에 패키지 저장소를 최신 상태로 업데이트하는 것이 항상 가장 좋은 방법입니다.

```bash
Debian: apt update; apt upgrade
RPM: yum update
```

### Get information about an installed package

```bash
Debian: apt show package_name
RPM: yum info package_name
```

## Exercise

각 패키지 명령을 실행하고 받는 출력을 확인하십시오.

## Quiz Question

Debian 시스템에서 패키지 정보를 표시하는 데 사용되는 명령은 무엇입니까?

## Quiz Answer

apt show
