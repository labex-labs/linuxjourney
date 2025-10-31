---
index: 6
lang: "ko"
title: "yum 과 apt"
meta_title: "yum 과 apt - 패키지 관리"
meta_description: "yum 대 apt 논쟁의 주요 차이점을 살펴보세요. 이 가이드는 RPM 및 Debian 기반 Linux 시스템에서 패키지를 설치, 제거 및 업데이트하기 위해 yum 과 apt 를 사용하는 방법을 다룹니다."
meta_keywords: "yum 대 apt, yum apt, 리눅스 패키지 관리, apt, yum, 데비안, 레드햇, 패키지 설치, 패키지 업데이트, 리눅스 명령어"
---

## Lesson Content

패키지 관리자는 소프트웨어 설치, 업데이트 및 제거를 간소화하는 Linux 의 필수 도구입니다. 이들은 종속성을 자동으로 처리하여 필요한 모든 라이브러리와 구성 요소가 올바르게 설치되도록 보장합니다. 가장 두드러진 두 가지 패키지 관리 시스템은 **yum**과 **apt**입니다.

### Yum 대 Apt

이 두 시스템의 주요 차이점은 지원하는 Linux 배포판에 있습니다. `yum`(Yellowdog Updater, Modified) 패키지 관리자는 Red Hat, CentOS, Fedora 와 같은 RPM 기반 배포판에서 사용됩니다. 반면, `apt`(Advanced Package Tool) 는 Ubuntu 를 포함한 Debian 기반 배포판의 표준입니다. `yum`과 `apt` 모두 동일한 목표를 달성하지만, 명령어 구문은 다릅니다.

### 패키지 설치 및 제거

저장소에서 새 소프트웨어를 설치하려면 `install` 명령어를 사용합니다.

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

패키지를 제거할 때 명령어 또한 간단합니다. `apt`는 `remove`를 사용하는 반면, `yum`은 `erase`를 사용합니다.

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### 패키지 업데이트 및 검사

소프트웨어를 설치하거나 업그레이드하기 전에 로컬 패키지 인덱스를 업데이트하는 것이 좋습니다. 이렇게 하면 사용 가능한 최신 버전을 가져올 수 있습니다.

Debian 시스템의 경우, 이는 두 단계로 이루어집니다. `apt update`는 패키지 목록을 새로 고치고, `apt upgrade`는 새 버전을 설치합니다. RPM 시스템의 경우, `yum update`가 단일 명령어로 두 작업을 모두 처리합니다.

```bash
Debian: $ apt update; apt upgrade
RPM: $ yum update
```

특정 패키지에 대한 자세한 정보를 얻어야 하는 경우, 다음 명령어를 사용하여 버전, 크기 및 설명과 같은 정보를 표시할 수 있습니다.

```bash
Debian: $ apt show package_name
RPM: $ yum info package_name
```

## Exercise

연습이 완벽을 만듭니다! Linux 패키지 관리에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1.  **[Linux 에서 YUM 을 사용하여 패키지 쿼리 및 업데이트](https://labex.io/ko/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - YUM 을 사용하여 RHEL 기반 Linux 시스템에서 소프트웨어 패키지를 관리하는 방법을 연습합니다. 여기에는 검사, 업데이트 및 저장소 탐색이 포함됩니다.
2.  **[Linux 에서 소프트웨어 설치](https://labex.io/ko/labs/linux-software-installation-on-linux-18005)** - apt, dpkg 사용 및 .deb 파일 처리 등 Ubuntu 시스템에서 소프트웨어를 설치하고 관리하는 다양한 방법을 배웁니다.
3.  **[패키지 설치 및 제거](https://labex.io/ko/labs/linux-installing-and-removing-packages-385380)** - `apt`를 사용하여 Debian 기반 시스템에서 시스템 업데이트, 패키지 설치 및 제거, 소프트웨어 구성 최적화를 연습합니다.

이 랩들은 실제 시나리오에 개념을 적용하고 Linux 패키지 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

Debian 시스템에서 패키지 정보를 표시하는 데 사용되는 명령어는 무엇입니까? 영어로 대소문자를 구분하여 답변하십시오.

## Quiz Answer

apt show
