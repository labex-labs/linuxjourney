---
lesson_id: "package-repositories"
course_id: "packages"
lang: "ko"
order_index: 2
title: "패키지 저장소"
description: "저장소가 서명된 패키지 인덱스를 게시하는 방식과 APT가 설정된 데비안 계열 소스를 찾는 방식을 알아봅니다."
meta_title: "패키지 저장소 - 패키지"
meta_description: "리눅스 패키지 저장소와 패키지 관리에서의 역할을 살펴보고, 시스템이 /etc/apt/sources.list 같은 소스를 이용해 패키지를 찾고 설치하는 방법을 알아봅니다."
meta_keywords: "리눅스 패키지 저장소, APT 소스 목록, /etc/apt/sources.list, 리눅스 패키지, 리눅스 입문, 리눅스 튜토리얼, 패키지 관리"
---

패키지 저장소는 패키지와 함께 인덱스 및 릴리스 메타데이터를 게시합니다. 패키지 관리자는 이 인덱스를 내려받아 설정된 배포판과 아키텍처에 맞는 버전을 선택하고, 저장소 인증을 확인한 뒤 필요한 패키지 파일을 가져옵니다.

## 저장소 메타데이터와 로컬 카탈로그

저장소는 단순한 아카이브 디렉터리가 아닙니다. 저장소 메타데이터에는 사용 가능한 패키지 이름, 버전, 아키텍처, 체크섬, 의존성 및 저장소 섹션이 기술됩니다. 클라이언트는 모든 아카이브를 먼저 내려받지 않고도 패키지를 검색하고 의존성을 해결할 수 있도록 로컬 카탈로그를 캐시합니다.

데비안 계열 시스템에서는 다음 명령으로 설정된 메타데이터를 새로 고칩니다.

```bash
$ sudo apt update
```

이 명령은 로컬 패키지 인덱스를 갱신할 뿐, 사용 가능한 업그레이드를 모두 설치하지는 않습니다. 실패한 항목을 무시하지 말고 보고된 소스와 인증 오류를 검토하십시오.

:::single-choice{#package-repositories-apt-update} `apt update`가 주로 새로 고치는 것은 무엇입니까?

::option[확인 없이 설치된 모든 패키지 바이너리입니다.]{#package-repositories-all-binaries explanation="업그레이드 설치는 메타데이터 갱신과 별개의 작업입니다."}
::option[패키지 설치 권한이 있는 사용자의 암호입니다.]{#package-repositories-user-passwords explanation="저장소 인덱스 갱신은 로컬 인증 자격 증명을 변경하지 않습니다."}
::option[설정된 소스에서 사용 가능한 패키지를 설명하는 로컬 인덱스입니다.]{#package-repositories-local-indexes .correct explanation="APT는 최신 저장소 메타데이터를 내려받아 이후 검색과 의존성 해결에 갱신된 카탈로그를 사용합니다."}
:::

## APT 소스 설정

APT는 다음 두 위치에서 설정된 소스를 읽습니다.

- `/etc/apt/sources.list`
- `/etc/apt/sources.list.d/` 아래에서 `.list` 또는 `.sources`로 끝나는 파일

`.list` 확장자는 전통적인 한 줄 형식을 사용합니다. `.sources` 확장자는 deb822 방식의 스탠자를 사용하며, 현재 APT 문서에서는 새 설정에 이 형식을 권장합니다. 배포판은 기본 소스를 어느 위치에나 둘 수 있으므로, `/etc/apt/sources.list`에 전체 설정 또는 주 설정이 반드시 들어 있는 것은 아닙니다.

deb822 방식 소스는 다음과 같은 형태입니다.

```text
Types: deb
URIs: https://deb.example.invalid/repository
Suites: stable
Components: main
Signed-By: /etc/apt/keyrings/example.gpg
```

이는 구문을 보여 주기 위한 예시일 뿐이며, 예약된 `.invalid` 도메인은 실제 저장소로 사용할 수 없습니다.

:::single-choice{#package-repositories-apt-locations} APT는 어디에서 활성 저장소 정의를 읽을 수 있습니까?

::option[`/etc/apt/sources.list`에서만 읽습니다.]{#package-repositories-only-main-list explanation="APT는 `/etc/apt/sources.list.d/`에 있는 지원되는 소스 파일도 읽습니다."}
::option[각 사용자의 홈 디렉터리 안에 있는 파일에서만 읽습니다.]{#package-repositories-only-home explanation="시스템 APT 소스 설정은 일반적으로 `/etc/apt` 아래에 있습니다."}
::option[`/etc/apt/sources.list`와 `/etc/apt/sources.list.d/`의 지원되는 파일에서 읽습니다.]{#package-repositories-both-locations .correct explanation="APT는 기본 파일과 소스 목록 디렉터리의 `.list` 및 `.sources` 정의를 결합합니다."}
:::

## 저장소 인증

APT는 서명된 저장소 릴리스 메타데이터를 검증한 다음, 내려받은 패키지 파일을 인증된 메타데이터의 체크섬과 대조합니다. `Signed-By`를 사용하면 해당 저장소에서 전역으로 설정된 모든 키를 신뢰하는 대신 특정 키링으로 소스의 신뢰 범위를 제한할 수 있습니다.

유효한 서명은 메타데이터가 허용된 서명 키의 소유자에게서 왔으며 탐지되지 않은 채 변조되지 않았음을 보여 줍니다. 하지만 게시자의 소프트웨어에 결함이 없거나, 악의적이지 않거나, 해당 시스템에 적합하다는 사실까지 증명하지는 않습니다. 독립적으로 신뢰할 수 있는 경로를 통해 키 지문과 소스 설정 지침을 확인하십시오.

:::single-choice{#package-repositories-signed-by} APT 소스 정의에서 `Signed-By`의 보안 목적은 무엇입니까?

::option[root도 읽을 수 없도록 설치된 모든 패키지를 암호화합니다.]{#package-repositories-package-encryption explanation="저장소 서명은 출처와 무결성을 확인하며, 로컬 관리자에게 내용을 숨기는 기능은 아닙니다."}
::option[해당 소스에서 선택된 서명 키만 사용하도록 제한합니다.]{#package-repositories-key-scope .correct explanation="이 필드는 제한 없는 전역 키 집합 대신 선택된 키링 자료에 저장소 검증을 연결합니다."}
::option[저장소에 취약한 소프트웨어가 없음을 보장합니다.]{#package-repositories-no-vulnerabilities explanation="암호학적 진위 확인은 소프트웨어 품질이나 보안 결함을 평가하지 않습니다."}
:::

## 신중하게 서드파티 소스 추가하기

저장소는 시스템 권한으로 패키지와 수명 주기 스크립트를 설치할 수 있으므로, 저장소를 추가하면 시스템의 소프트웨어 신뢰 경계가 확장됩니다. 추가하기 전에는 다음 사항을 확인하십시오.

1. 요구 사항을 충족한다면 배포판 저장소를 우선 사용합니다.
2. 게시자, 지원 릴리스, 아키텍처 및 서명 키 지문을 확인합니다.
3. 전용 소스 파일과 범위가 제한된 키링을 사용합니다.
4. 설치 전에 패키지 이름과 의존성 변경 사항을 살펴봅니다.
5. 소스를 비활성화하고 그 패키지를 마이그레이션하거나 제거하는 방법을 문서화합니다.

서명 검사를 끄거나 검토하지 않은 원격 스크립트를 권한 있는 셸로 전달하는 오래된 지침을 그대로 따라 하지 마십시오.

:::single-choice{#package-repositories-third-party-risk} 서드파티 저장소를 추가하면 시스템의 신뢰 경계가 확장되는 이유는 무엇입니까?

::option[인증된 패키지와 스크립트가 시스템 권한으로 설치될 수 있기 때문입니다.]{#package-repositories-privileged-install .correct explanation="서명 소스를 신뢰하면 운영체제에 영향을 주는 코드와 수명 주기 작업이 허용될 수 있습니다."}
::option[리눅스 커널이 파일 권한 적용을 중단하기 때문입니다.]{#package-repositories-disable-permissions explanation="저장소 설정은 커널의 일반적인 접근 제어 메커니즘을 비활성화하지 않습니다."}
::option[모든 네이티브 패키지를 소스 아카이브로 변환하기 때문입니다.]{#package-repositories-convert-source explanation="저장소를 추가하면 사용 가능한 패키지 소스가 바뀔 뿐, 기존 패키지의 기본 형식은 바뀌지 않습니다."}
:::

[리눅스에서 소프트웨어 설치하기](https://labex.io/labs/linux-software-installation-on-linux-18005)에서 저장소를 이용한 설치를 연습하거나, [YUM으로 패키지 조회 및 업데이트하기](https://labex.io/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)에서 레드햇 계열 작업 흐름과 비교해 보십시오. 정확한 APT 구문은 로컬 `sources.list(5)` 설명서를 참고하십시오.

## 요약

이제 설정된 저장소가 어떻게 신뢰할 수 있는 패키지 메타데이터로 이어지는지 설명할 수 있습니다.

1. 저장소 인덱스와 패키지 아카이브를 구분합니다.
2. `apt update`로 로컬 카탈로그를 새로 고칩니다.
3. 한 줄 형식과 deb822 방식의 APT 소스 정의 위치를 모두 찾습니다.
4. 서명 키의 범위를 제한하고 서드파티 신뢰를 신중하게 검토합니다.
