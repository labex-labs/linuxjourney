---
lesson_id: "compile-source-code"
course_id: "packages"
lang: "ko"
order_index: 7
title: "소스 코드 컴파일"
description: "소스에서 컴파일한 소프트웨어를 검증, 설정, 빌드, 테스트, 스테이징 및 추적하는 방법을 알아봅니다."
meta_title: "소스 코드 컴파일 - 패키지"
meta_description: "리눅스에서 소스 코드를 컴파일하는 방법을 알아봅니다. configure, make, DESTDIR 및 패키지 추적을 이용한 안전한 소스 빌드 절차를 설명합니다."
meta_keywords: "소스 코드 컴파일 방법, 소스 코드 빌드, 소스 코드 컴파일, make install, checkinstall, 리눅스 컴파일, build-essential, configure 스크립트, Makefile, 리눅스 튜토리얼"
---

소스에서 빌드하면 설정된 저장소에 없는 버전이나 기능을 사용할 수 있지만, 통합, 업데이트 및 신뢰 관리 책임이 배포판에서 사용자에게 넘어옵니다. 요구 사항을 충족하는 지원 배포판 패키지가 있다면 그것을 우선 사용하십시오.

## 빌드 전에 검증하고 읽기

인증된 업스트림 릴리스 경로에서 소스를 구하십시오. 신뢰할 수 있는 경로를 통해 서명 또는 체크섬을 검증하고, 아카이브를 검사한 뒤 비특권 스테이징 디렉터리에 추출하십시오. `README`, `INSTALL`, `SECURITY` 및 프로젝트 빌드 문서 같은 파일을 읽으십시오.

빌드 지침은 실행 가능한 코드입니다. `configure` 스크립트, 빌드 정의, 테스트 또는 컴파일러 플러그인은 사용자 권한으로 임의 명령을 실행할 수 있습니다. 신뢰할 수 없는 소스는 빌드하지 말고, 빌드 자체를 `sudo`로 실행하지 마십시오.

:::single-choice{#compile-source-code-build-privilege} 일반적으로 `sudo` 없이 컴파일 단계를 실행해야 하는 이유는 무엇입니까?

::option[컴파일러는 root 사용자의 머신 코드를 만들 수 없기 때문입니다.]{#compile-source-code-root-compiler explanation="컴파일러는 root로도 실행되지만 그렇게 하면 불필요하게 위험이 커집니다."}
::option[`sudo`가 생성된 모든 오브젝트 파일을 자동으로 삭제하기 때문입니다.]{#compile-source-code-sudo-delete explanation="권한 상승이 본질적으로 빌드 결과물을 제거하지는 않습니다."}
::option[빌드 로직은 임의 명령을 실행할 수 있으며 보통 시스템 권한이 필요하지 않기 때문입니다.]{#compile-source-code-unprivileged-build .correct explanation="비특권으로 빌드하면 실수나 악의적인 빌드 지침이 일으킬 수 있는 피해를 제한합니다."}
:::

## 빌드 요구 사항 설치하기

데비안 계열 개발 시스템에서는 다음 명령을 흔히 시작점으로 사용합니다.

```bash
$ sudo apt install build-essential
```

이 명령은 기본적인 컴파일러와 빌드 도구를 설치하지만 모든 프로젝트에 필요한 모든 의존성을 제공하지는 않습니다. 프로젝트에는 언어 런타임, 생성기, 빌드 시스템 도구, 개발 헤더 또는 정확한 라이브러리 버전이 추가로 필요할 수 있습니다. 신뢰할 수 있는 저장소에서 요구 사항을 설치하고 빌드 의존성과 런타임 의존성을 구분하십시오.

:::single-choice{#compile-source-code-build-essential-scope} 데비안 계열 시스템에서 `build-essential`이 제공하는 것은 무엇입니까?

::option[일반적인 컴파일 및 빌드 도구의 기본 집합입니다.]{#compile-source-code-baseline-tools .correct explanation="기초 도구를 제공하지만 프로젝트별 라이브러리나 생성기를 모두 예측할 수는 없습니다."}
::option[모든 소스 프로젝트의 모든 의존성입니다.]{#compile-source-code-all-dependencies explanation="개별 프로젝트에는 추가 요구 사항과 특정 버전 요구 사항이 선언됩니다."}
::option[다운로드한 소스를 신뢰할 수 있다는 보장입니다.]{#compile-source-code-trust-guarantee explanation="빌드 도구 설치는 별도로 받은 소스 릴리스를 인증하지 않습니다."}
:::

## 설정 및 빌드

전통적인 Autoconf 방식 프로젝트에서는 다음 명령을 사용합니다.

```bash
$ ./configure --prefix=/usr/local
$ make
```

`configure`는 환경을 확인하고 선택한 옵션에 따라 빌드 파일을 생성합니다. `make`는 일반적으로 `Makefile`에 있는 의존성과 명령 규칙을 읽고 요청된 대상을 만듭니다.

이 순서가 모든 프로젝트에 적용되는 것은 아닙니다. 프로젝트는 CMake, Meson, Ninja, 언어별 도구 또는 사용자 정의 스크립트를 사용할 수 있습니다. 익숙하다는 이유만으로 `./configure`를 실행하지 말고 정확한 릴리스의 문서를 따르십시오. 빌드 시스템이 지원한다면 트리 외부 빌드 디렉터리를 사용해 생성 파일을 분리할 수 있습니다.

:::single-choice{#compile-source-code-make-role} 전통적인 작업 흐름에서 `make`는 무엇을 합니까?

::option[모든 결과물을 배포판 패키지 데이터베이스에 등록합니다.]{#compile-source-code-make-package-db explanation="컴파일만으로는 네이티브 패키지 소유권 레코드가 만들어지지 않습니다."}
::option[인증된 소스 릴리스를 자동으로 다운로드합니다.]{#compile-source-code-make-download explanation="프로젝트가 명시적으로 다르게 정의하지 않는 한 로컬 빌드 전에 소스를 구하고 검증합니다."}
::option[빌드 설명에서 적용 가능한 규칙을 실행합니다.]{#compile-source-code-make-rules .correct explanation="make는 의존성을 평가하고 선택한 대상을 최신 상태로 만드는 데 필요한 명령을 실행합니다."}
:::

## 설치 전에 테스트하기

다음과 같이 프로젝트 문서에 지정된 테스트 대상을 실행합니다.

```bash
$ make check
```

실제 대상은 `test`, `check` 또는 별도의 명령일 수 있습니다. 테스트하지 않은 결과물을 설치하지 말고 실패 원인을 조사하십시오. 테스트에는 네트워크 접근, 서비스, 특수 하드웨어 또는 격리가 필요할 수 있습니다. 다른 빌드 코드와 마찬가지로 실행 전에 내용을 검토하십시오.

:::single-choice{#compile-source-code-test-failure} 문서에 명시된 테스트 모음이 실패하면 어떻게 해야 합니까?

::option[같은 설치를 즉시 root로 실행합니다.]{#compile-source-code-install-after-failure explanation="권한을 높여도 알 수 없는 정확성 문제가 해결되지 않으며 결과만 더 심각해집니다."}
::option[충돌을 피하려고 패키지 관리자 데이터베이스를 삭제합니다.]{#compile-source-code-delete-database explanation="네이티브 데이터베이스는 소스 테스트 실패 해결과 관련이 없으며 삭제해서는 안 됩니다."}
::option[빌드를 설치하기 전에 실패 원인을 조사합니다.]{#compile-source-code-investigate-tests .correct explanation="실패한 테스트는 호환되지 않는 의존성, 빌드 결함 또는 환경에 대한 가정을 드러낼 수 있습니다."}
:::

## 설치 스테이징 및 추적

`sudo make install`은 네이티브 패키지 데이터베이스에 기록하지 않고 파일을 시스템 접두사에 직접 복사할 수 있습니다. 제거 대상은 선택 사항이며 불완전할 수 있고, 나중의 업그레이드가 파일을 덮어쓰거나 고아 파일로 남길 수도 있습니다.

다음과 같은 제어 가능한 방법을 우선 사용하십시오.

- 배포판 패키징 도구로 공식 네이티브 패키지 빌드
- 정책이 허용한다면 `/usr/local`처럼 명확히 분리된 접두사에 설치
- `DESTDIR` 같은 지원 메커니즘으로 임시 패키징 루트에 파일 스테이징
- 적절한 경우 비특권 사용자 접두사, 격리 환경 또는 컨테이너 사용

`checkinstall`은 일부 `make install` 작업 흐름에서 단순 패키지를 만들 수 있지만 범용 도구가 아니며, 검토된 배포판 수준의 패키지 제작법을 대신하지도 않습니다. 이를 “항상” 적용하는 규칙으로 취급하지 마십시오. 권한 있는 복사를 수행하기 전에 스테이징된 파일 목록, 소유권, 권한, 경로 및 제거 또는 업그레이드 계획을 검사하십시오.

:::single-choice{#compile-source-code-destdir-purpose} 지원되는 `DESTDIR` 스테이징 설치의 목적은 무엇입니까?

::option[설치할 파일을 검사 또는 패키징을 위한 임시 루트 아래에 배치합니다.]{#compile-source-code-stage-root .correct explanation="스테이징은 파일 수집을 실제 시스템 접두사에 즉시 기록하는 작업과 분리합니다."}
::option[컴파일러를 원격 패키지 저장소로 바꿉니다.]{#compile-source-code-destdir-repository explanation="이 변수는 설치 경로를 재지정하며 저장소 메타데이터를 게시하지 않습니다."}
::option[컴파일을 건너뛰고 출처를 알 수 없는 바이너리를 대신 다운로드합니다.]{#compile-source-code-destdir-download explanation="스테이징은 빌드 후에 적용되며 외부 바이너리 다운로드를 대신하지 않습니다."}
:::

폐기 가능한 환경에서 [리눅스 소스 코드로 소프트웨어 빌드하기](https://labex.io/labs/comptia-build-software-from-source-code-in-linux-590853)를 실습해, 실험용 파일을 운영 시스템에 섞지 않고 작업 흐름을 익혀 보십시오.

## 요약

이제 소스 빌드를 제어 가능한 소프트웨어 공급 작업 흐름으로 다룰 수 있습니다.

1. 소스를 인증하고 그 지침을 실행 가능한 코드로 간주해 검토합니다.
2. 신뢰하는 저장소에서 명시된 빌드 요구 사항을 설치합니다.
3. 불필요한 권한 없이 설정, 빌드 및 테스트합니다.
4. 시스템에 설치하기 전에 결과물을 스테이징하고 검사합니다.
5. 네이티브 패키징 또는 의도적으로 격리한 접두사로 설치 파일을 추적합니다.
