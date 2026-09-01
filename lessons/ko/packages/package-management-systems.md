---
lesson_id: "package-management-systems"
course_id: "packages"
lang: "ko"
order_index: 6
title: "yum과 apt"
description: "저장소를 인식하는 APT와 DNF를 사용해 패키지를 검사, 설치, 제거 및 업그레이드하는 작업 흐름을 알아봅니다."
meta_title: "yum과 apt - 패키지"
meta_description: "yum과 apt의 주요 차이를 살펴봅니다. RPM 및 데비안 기반 리눅스 시스템에서 yum과 apt로 패키지를 설치, 제거 및 업데이트하는 방법을 알아봅니다."
meta_keywords: "yum과 apt, yum apt, 리눅스 패키지 관리, apt, yum, 데비안, 레드햇, 패키지 설치, 패키지 업데이트, 리눅스 명령어"
---

저장소를 인식하는 패키지 관리자는 메타데이터를 가져오고, 의존성을 해결하며, 인증된 콘텐츠를 검증하고, 트랜잭션을 조정합니다. 데비안 계열 시스템은 일반적으로 APT를 사용합니다. 현재 페도라와 레드햇 엔터프라이즈 리눅스 릴리스는 DNF를 사용합니다. 최신 RHEL에서 `yum` 명령은 DNF의 호환성 별칭으로 남아 있지만, 구형 시스템은 원래 YUM 구현을 사용했습니다.

명령 집합 하나가 어디에서나 통한다고 가정하지 말고, 설치된 배포판과 릴리스의 문서를 따르십시오.

## 메타데이터 새로 고침 및 검사

APT는 메타데이터 새로 고침과 패키지 업그레이드를 분리합니다.

```bash
Debian family: $ sudo apt update
```

설치하기 전에 다음과 같이 검색하고 검사합니다.

```bash
Debian family: $ apt search package-name
Debian family: $ apt show package-name
RPM family:    $ dnf search package-name
RPM family:    $ dnf info package-name
```

이 명령으로 찾을 수 있는 항목은 저장소 설정에 따라 달라집니다. 소스 이름, 아키텍처, 버전 및 서명 오류를 주의 깊게 읽으십시오.

:::single-choice{#package-management-systems-apt-show} `package-name`에 대한 APT 패키지 상세 정보를 표시하는 명령은 무엇입니까?

::option[`apt remove package-name`]{#package-management-systems-apt-remove-command explanation="`remove` 하위 명령은 패키지 제거를 제안합니다."}
::option[`dnf search package-name`]{#package-management-systems-dnf-search-command explanation="이 명령은 RPM 계열 저장소를 검색하며 APT 상세 정보 명령이 아닙니다."}
::option[`apt show package-name`]{#package-management-systems-apt-show-command .correct explanation="`show` 하위 명령은 지정한 바이너리 패키지의 메타데이터를 표시합니다."}
:::

## 패키지 설치하기

다음과 같이 저장소 패키지 이름으로 설치합니다.

```bash
Debian family: $ sudo apt install package-name
RPM family:    $ sudo dnf install package-name
```

관리자는 의존성과 충돌 또는 대체 항목을 제안합니다. 패키지 출처, 버전, 아키텍처, 다운로드 크기, 디스크 변경량, 제거 항목 및 새로 설치되는 의존성을 검토하기 전에는 자동으로 확정하지 마십시오.

:::single-choice{#package-management-systems-dnf-install} 설정된 RPM 계열 저장소에서 `package-name`을 설치하는 현재 명령은 무엇입니까?

::option[`rpm -qa package-name`]{#package-management-systems-rpm-query-command explanation="이것은 RPM 설치 데이터베이스 조회이며 저장소 설치 요청이 아닙니다."}
::option[`dnf install package-name`]{#package-management-systems-dnf-install-command .correct explanation="DNF는 페도라와 최신 RHEL 릴리스에서 사용하는 현재의 저장소 인식 관리자입니다."}
::option[`apt update package-name`]{#package-management-systems-apt-update-package explanation="APT update는 인덱스를 갱신하며 지정된 RPM 계열 패키지를 설치하지 않습니다."}
:::

## 패키지 제거하기

다음 명령으로 제거를 요청합니다.

```bash
Debian family: $ sudo apt remove package-name
RPM family:    $ sudo dnf remove package-name
```

제거는 의존하는 패키지에 영향을 주거나, 이제 사용되지 않는 의존성과 설정을 남길 수 있습니다. 제안된 트랜잭션을 검토하고, 데비안 계열 시스템에서 remove와 purge의 의미를 구분하며, 애플리케이션별 백업 및 보존 절차에 따라 데이터를 보존하십시오. 패키지를 제거해도 사용자가 만든 데이터까지 삭제된다고 보장할 수 없습니다.

:::single-choice{#package-management-systems-remove-review} 제거 트랜잭션을 확정하기 전에 검토해야 하는 이유는 무엇입니까?

::option[제거하면 항상 패키지가 있는 파일 시스템을 다시 포맷하기 때문입니다.]{#package-management-systems-removal-format explanation="패키지 관리자는 관리 파일과 상태를 제거하며 일반적으로 파일 시스템을 포맷하지 않습니다."}
::option[패키지 관리자가 제안된 변경 집합을 표시할 수 없기 때문입니다.]{#package-management-systems-no-proposal explanation="대화형 관리자는 검토할 수 있도록 보통 예정된 트랜잭션을 보여 줍니다."}
::option[다른 패키지가 선택한 패키지에 의존해 함께 영향을 받을 수 있기 때문입니다.]{#package-management-systems-dependent-removal .correct explanation="의존성 제약 때문에 요청 범위가 처음 입력한 패키지 이름 하나보다 넓어질 수 있습니다."}
:::

## 업데이트 적용하기

APT 시스템에서는 메타데이터를 새로 고친 다음, 별도의 성공한 단계로 업그레이드를 검토합니다.

```bash
$ sudo apt update
$ apt list --upgradable
$ sudo apt upgrade
```

DNF 시스템에서는 로컬 문서에 따른 작업 흐름으로 사용 가능한 업데이트를 검사하고 적용합니다.

```bash
$ dnf check-update
$ sudo dnf upgrade
```

업데이트 명령은 핵심 라이브러리, 서비스, 커널 및 의존성을 변경할 수 있습니다. 시스템에 맞는 백업, 유지 관리 정책, 릴리스 정보 및 재시작 또는 재부팅 계획을 사용하십시오. 명령 종료 상태의 의미도 확인해야 합니다. 예를 들어 일부 “업데이트 확인” 작업은 실행 실패가 아니라 업데이트가 있음을 알리기 위해 0이 아닌 상태를 사용합니다.

:::single-choice{#package-management-systems-apt-update-upgrade} `apt update`와 `apt upgrade`는 어떤 관계입니까?

::option[`update`는 패키지를 제거하고 `upgrade`는 설정 파일을 복원합니다.]{#package-management-systems-apt-remove-restore explanation="두 명령 사이에는 그러한 제거 및 복원 관계가 없습니다."}
::option[`update`는 메타데이터를 새로 고치고 `upgrade`는 승인한 패키지 업그레이드 계획을 적용합니다.]{#package-management-systems-apt-two-steps .correct explanation="APT는 카탈로그 갱신과 새 패키지 버전 설치를 분리합니다."}
::option[두 이름은 동일한 작업을 가리킵니다.]{#package-management-systems-apt-identical explanation="두 명령은 서로 다른 단계를 수행하므로 각각 확인해야 합니다."}
:::

## `dnf`와 `yum` 선택하기

현재 페도라와 RHEL 문서에서는 `dnf`를 사용하십시오. 최신 RHEL 시스템의 `yum` 명령은 DNF 호환 동작을 호출할 수 있지만, 스크립트에서 실행 파일 이름만 보고 구현을 추정해서는 안 됩니다. 레거시 호스트에서는 지침을 옮기기 전에 설치된 버전과 지원 구문을 확인하십시오.

:::single-choice{#package-management-systems-yum-current-rhel} 현재 RHEL 시스템에서 `yum`은 일반적으로 무엇을 나타냅니까?

::option[DNF가 뒷받침하는 호환성 명령입니다.]{#package-management-systems-yum-dnf-alias .correct explanation="최신 RHEL 릴리스는 DNF를 사용하면서 호환성을 위해 yum 명령 이름을 유지합니다."}
::option[데비안의 저수준 `.deb` 아카이브 도구입니다.]{#package-management-systems-yum-dpkg explanation="데비안 시스템은 네이티브 패키지 관리에 YUM이 아니라 APT와 dpkg 같은 도구를 사용합니다."}
::option[저장소 메타데이터 전용 압축 도구입니다.]{#package-management-systems-yum-compressor explanation="YUM과 DNF는 패키지 관리 인터페이스이며 독립형 압축 형식이 아닙니다."}
:::

[패키지 설치 및 제거하기](https://labex.io/labs/linux-installing-and-removing-packages-385380)에서 APT를 연습하고, [YUM으로 패키지 조회 및 업데이트하기](https://labex.io/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)에서 DNF/YUM 계열 개념을 익혀 보십시오.

## 요약

이제 일반적인 저장소 패키지 작업을 선택하고 검토할 수 있습니다.

1. 데비안 계열 시스템에서는 APT를, 현재 RPM 계열 시스템에서는 DNF를 사용합니다.
2. 설치 전에 메타데이터와 제안된 의존성 변경을 검사합니다.
3. 제거를 단일 파일 삭제가 아니라 의존성을 고려하는 트랜잭션으로 취급합니다.
4. 도구가 구분하는 경우 메타데이터 갱신과 업그레이드 적용을 분리합니다.
5. `yum`이 레거시 YUM인지 DNF 호환성 명령인지 확인합니다.
