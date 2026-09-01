---
lesson_id: "package-install-tools"
course_id: "packages"
lang: "ko"
order_index: 5
title: "rpm과 dpkg"
description: "`dpkg`와 `rpm`이 각각의 네이티브 패키지 데이터베이스 및 로컬 아카이브를 검사하고 변경하는 방법을 알아봅니다."
meta_title: "rpm과 dpkg - 패키지"
meta_description: "rpm과 dpkg 명령으로 패키지를 설치, 제거 및 나열하는 방법을 알아봅니다. .deb 및 .rpm 파일을 직접 관리하는 방식을 이해합니다."
meta_keywords: "rpm, dpkg, 리눅스 패키지 관리, .deb, .rpm, 리눅스 튜토리얼, 리눅스 입문, 패키지 설치"
---

`dpkg`는 데비안 계열 시스템의 저수준 패키지 도구이고, `rpm`은 RPM 계열 시스템에서 비슷한 역할을 합니다. 이 도구들은 네이티브 아카이브를 풀고, 패키지 수명 주기 작업을 실행하며, 설치된 패키지 데이터베이스를 갱신합니다. APT와 DNF 같은 저장소 인식 도구는 이러한 저수준 메커니즘을 기반으로 동작합니다.

## 설치 전에 아카이브 검사하기

패키지 아카이브는 실행 파일 하나와 같지 않습니다. 여러 페이로드 파일, 메타데이터, 설정 처리 및 권한 있는 수명 주기 스크립트를 포함할 수 있습니다. 설치하기 전에 출처, 서명 또는 인증된 다운로드 경로, 메타데이터 및 내용을 검사하십시오.

```bash
Debian: $ dpkg-deb --info ./some-package.deb
Debian: $ dpkg-deb --contents ./some-package.deb
RPM:    $ rpm -qip ./some-package.rpm
RPM:    $ rpm -qlp ./some-package.rpm
```

위 RPM 조회 형식에서 `p`는 설치된 데이터베이스가 아니라 “패키지 파일을 조회”한다는 뜻입니다. 조회 출력은 패키지 검토에 도움이 되지만 스크립트나 프로그램이 안전하다는 사실을 증명하지는 못합니다.

:::single-choice{#package-install-tools-native-format} 데비안 `.deb` 패키지와 설치 데이터베이스를 관리하는 저수준 도구는 무엇입니까?

::option[`rpm`]{#package-install-tools-rpm-debian explanation="RPM은 RPM 계열 시스템에서 자체 네이티브 형식과 데이터베이스를 관리합니다."}
::option[`tar`]{#package-install-tools-tar-debian explanation="tar는 아카이브를 읽을 수 있지만 데비안의 설치 패키지 수명 주기를 구현하지는 않습니다."}
::option[`dpkg`]{#package-install-tools-dpkg-debian .correct explanation="데비안 계열 시스템은 저수준 `.deb` 아카이브 및 패키지 데이터베이스 작업에 `dpkg`를 사용합니다."}
:::

## 로컬 아카이브 설치하기

다음과 같이 저수준 도구로 직접 설치할 수 있습니다.

```bash
Debian: $ sudo dpkg -i ./some-package.deb
RPM:    $ sudo rpm -U ./some-package.rpm
```

`dpkg -i`는 요청한 아카이브를 풀고 설정할 수 있지만 누락된 저장소 의존성을 가져오지는 않습니다. 원시 `rpm` 명령도 일반적인 저장소 해결기 작업 흐름을 제공하지 않습니다. 설정된 소스에서 의존성을 해결할 수 있으므로 로컬 아카이브에는 대체로 다음 고수준 명령이 더 적합합니다.

```bash
Debian: $ sudo apt install ./some-package.deb
RPM:    $ sudo dnf install ./some-package.rpm
```

확정하기 전에 트랜잭션을 검토하십시오. APT에서는 앞의 `./`가 로컬 데비안 아카이브 경로를 저장소 패키지 이름과 구분합니다.

:::single-choice{#package-install-tools-local-dependencies} 사용 가능한 저장소 의존성을 해결하면서 로컬 `.deb` 파일을 설치할 수 있는 명령은 무엇입니까?

::option[`dpkg -l ./some-package.deb`]{#package-install-tools-dpkg-list-file explanation="`dpkg -l`은 설치 패키지 선택 항목을 나열하며 로컬 의존성을 해결하는 설치 작업 흐름이 아닙니다."}
::option[`rpm -qa ./some-package.deb`]{#package-install-tools-rpm-query-deb explanation="RPM 조회 구문은 데비안 아카이브를 설치하지 않습니다."}
::option[`apt install ./some-package.deb`]{#package-install-tools-apt-local .correct explanation="APT는 명시적인 로컬 경로를 인식하고 설정된 저장소를 이용해 선언된 의존성을 충족할 수 있습니다."}
:::

## 설치된 패키지 제거하기

제거할 때는 이전에 사용한 아카이브 파일 이름이 아니라 설치된 패키지 이름을 지정합니다.

```bash
Debian: $ sudo dpkg --remove package-name
RPM:    $ sudo rpm --erase package-name
```

데비안의 `--remove`는 보통 conffile로 분류된 설정 파일을 유지합니다. `--purge`는 패키지 스크립트와 관리되지 않는 데이터의 영향을 받지만 이러한 설정 파일도 제거하도록 요청합니다. 어느 명령도 사용자가 만든 데이터의 삭제를 보장하지 않습니다. 관련 패키지를 평가하고 전체 트랜잭션을 보여 줄 수 있으므로 일반적으로 고수준 `apt remove` 또는 `dnf remove`가 더 좋습니다.

:::single-choice{#package-install-tools-remove-operand} `dpkg --remove`는 설치된 패키지를 제거할 때 어떤 피연산자를 요구합니까?

::option[저장소 인덱스의 URL입니다.]{#package-install-tools-remove-url explanation="저장소 위치는 저수준 제거 명령에 전달하는 패키지 식별자가 아닙니다."}
::option[설치된 패키지 이름입니다.]{#package-install-tools-remove-name .correct explanation="제거는 이전 `.deb` 경로가 아니라 `example` 같은 패키지 레코드를 대상으로 합니다."}
::option[패키지가 시작한 프로세스의 PID입니다.]{#package-install-tools-remove-pid explanation="프로세스 ID는 설치 패키지 데이터베이스 키와 관련이 없습니다."}
:::

## 설치 상태 조회하기

다음 명령으로 설치되었거나 알려진 패키지 레코드를 나열합니다.

```bash
Debian: $ dpkg-query -l
RPM:    $ rpm -qa
```

대상을 좁혀 검사할 때는 특정 패키지 이름을 사용하고, 스크립트의 안정성이 중요하다면 기계 판독 형식을 사용하십시오. 패키지 데이터베이스는 관리되는 상태를 설명하지만 로컬 관리자나 애플리케이션이 나중에 파일을 변경할 수도 있습니다. 설치 파일을 기록된 메타데이터와 비교해야 한다면 검증 기능을 사용하십시오.

:::single-choice{#package-install-tools-rpm-list-installed} RPM 데이터베이스에 설치된 것으로 기록된 모든 패키지를 조회하는 명령은 무엇입니까?

::option[`rpm -qa`]{#package-install-tools-rpm-query-all .correct explanation="`-q`는 조회 모드를 선택하고 `-a`는 모든 설치 패키지 레코드로 범위를 넓힙니다."}
::option[`rpm -e`]{#package-install-tools-rpm-erase explanation="`-e`는 읽기 전용 목록이 아니라 패키지 제거를 요청합니다."}
::option[`dpkg-deb --contents`]{#package-install-tools-deb-contents explanation="이 명령은 데비안 아카이브 파일의 페이로드를 검사하며 RPM 설치 데이터베이스를 조회하지 않습니다."}
:::

[RPM으로 패키지 관리하기](https://labex.io/labs/rhel-managing-packages-with-rpm-in-linux-590868)에서 격리된 시스템을 사용해 아카이브 조회와 무결성 검사를 연습해 보십시오.

## 요약

이제 저수준 패키지 작업과 저장소 트랜잭션을 구분할 수 있습니다.

1. 설치하기 전에 로컬 아카이브의 메타데이터와 내용을 검사합니다.
2. `.deb` 저수준 작업에는 `dpkg`를, `.rpm` 작업에는 `rpm`을 사용합니다.
3. 의존성을 해결해야 할 때는 APT 또는 DNF를 우선 사용합니다.
4. 설치된 패키지 이름으로 제거하고 관리 상태는 별도로 검증합니다.
