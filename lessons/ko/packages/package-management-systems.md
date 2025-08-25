---
index: 6
lang: "ko"
title: "yum 과 apt"
meta_title: "yum 과 apt - 패키지"
meta_description: "Linux 패키지 관리를 위한 yum 과 apt 를 배우세요. 이 초보자 튜토리얼을 통해 Debian/RPM 시스템에서 소프트웨어를 설치, 제거 및 업데이트하세요. 오늘 시작하세요!"
meta_keywords: "yum, apt, Linux 패키지 관리, apt 튜토리얼, yum 튜토리얼, Linux 명령어, 초보자 가이드, 패키지 설치"
---

## Lesson Content

아, 패키지 관리의 배트맨들! 이 시스템들은 패키지 종속성 설치를 포함하여 패키지 설치, 제거 및 변경을 더 쉽게 하기 위한 모든 기능을 제공합니다. 가장 인기 있는 두 가지 관리 시스템은 **yum**과 **apt**입니다. Yum 은 Red Hat 계열에만 해당하며, apt 는 Debian 계열에만 해당합니다.

### 저장소에서 패키지 설치

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### 패키지 제거

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### 저장소 패키지 업데이트

패키지를 설치하고 업데이트하기 전에 패키지 저장소를 최신 상태로 업데이트하는 것이 항상 가장 좋은 방법입니다.

```bash
Debian: apt update; apt upgrade
RPM: yum update
```

### 설치된 패키지 정보 확인

```bash
Debian: apt show package_name
RPM: yum info package_name
```

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 패키지 관리에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 에서 YUM 으로 패키지 쿼리 및 업데이트](https://labex.io/ko/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - YUM 을 사용하여 RHEL 기반 Linux 시스템에서 소프트웨어 패키지를 관리하는 방법을 연습합니다. 여기에는 저장소 검사, 업데이트 및 탐색이 포함됩니다.
2. **[Linux 소프트웨어 설치](https://labex.io/ko/labs/linux-software-installation-on-linux-18005)** - apt, dpkg 사용 및 .deb 파일 처리 등 Ubuntu 시스템에서 소프트웨어를 설치하고 관리하는 다양한 방법을 배웁니다.
3. **[패키지 설치 및 제거](https://labex.io/ko/labs/linux-installing-and-removing-packages-385380)** - `apt`를 사용하여 Debian 기반 시스템에서 시스템 업데이트, 패키지 설치 및 제거, 소프트웨어 구성 최적화를 연습합니다.

이 실습들은 실제 시나리오에 개념을 적용하고 Linux 패키지 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

Debian 시스템에서 패키지 정보를 표시하는 데 사용되는 명령어는 무엇입니까?

## Quiz Answer

apt show
