---
lesson_id: "software-distribution"
course_id: "packages"
lang: "ko"
order_index: 1
title: "소프트웨어 배포"
description: "업스트림 프로젝트, 배포판 유지 관리자, 패키지, 패키지 형식이 어떻게 리눅스 소프트웨어 공급망을 이루는지 알아봅니다."
meta_title: "소프트웨어 배포 - 패키지"
meta_description: "소프트웨어 배포, 패키지 관리자, .deb 및 .rpm 같은 패키지 형식을 이해하며 리눅스를 체계적으로 학습하는 방법을 알아봅니다."
meta_keywords: "리눅스 소프트웨어 배포, 패키지 관리자, .deb, .rpm, 리눅스 학습, 패키지 형식, 소프트웨어 설치, 리눅스 패키지"
---

리눅스 소프트웨어는 일반적으로 배포판별 도구가 관리하는 패키지 형태로 제공됩니다. 패키지는 설치 가능한 파일과 메타데이터를 하나로 묶어, 시스템이 버전, 의존성, 소유권, 체크섬 및 수명 주기 작업을 추적할 수 있게 합니다.

## 패키지에 포함되는 항목

바이너리 패키지에는 실행 파일, 라이브러리, 문서, 기본 설정, 서비스 정의 및 기타 리소스가 포함될 수 있습니다. 또한 다음과 같은 메타데이터도 담습니다.

- 패키지 이름과 버전
- 대상 아키텍처와 배포판 환경
- 선언된 의존성과 충돌 관계
- 파일 목록과 무결성 정보
- 수명 주기 작업에 사용되는 선택적 스크립트 또는 트리거

모든 패키지가 대화형 애플리케이션인 것은 아닙니다. 패키지는 라이브러리, 커널 구성 요소, 언어 데이터, 글꼴, 디버그 심볼 또는 여러 다른 패키지 모음에 의존하는 메타데이터를 제공할 수도 있습니다.

:::single-choice{#software-distribution-package-metadata} 다음 중 애플리케이션 실행 파일이 아니라 일반적으로 패키지 메타데이터에 해당하는 정보는 무엇입니까?

::option[애플리케이션을 구현하는 CPU 명령어입니다.]{#software-distribution-executable-code explanation="컴파일된 명령어는 의존성 메타데이터가 아니라 패키지 페이로드의 내용입니다."}
::option[선언된 의존 관계입니다.]{#software-distribution-dependencies .correct explanation="패키지는 필수 또는 충돌 패키지를 기술하므로 관리 도구가 설치 과정을 판단할 수 있습니다."}
::option[현재 메모리에 열려 있는 사용자의 저장되지 않은 문서입니다.]{#software-distribution-user-document explanation="실행 중에 생성된 사용자 데이터는 배포 패키지의 메타데이터가 아닙니다."}
:::

## 업스트림과 배포판의 역할

업스트림 프로젝트는 원본 소스 코드를 개발하고 릴리스합니다. 그런 다음 리눅스 배포판 유지 관리자는 선택한 릴리스를 해당 배포판에 맞게 조정합니다. 이 작업에는 라이선스 검토, 통합 또는 보안 패치 적용, 빌드 지침 정의, 결과물의 패키지 분할, 의존성 선언, 테스트 실행 및 업데이트 유지 관리가 포함될 수 있습니다.

배포판의 빌드 인프라는 지원되는 릴리스와 아키텍처를 위한 패키지를 만듭니다. 저장소 도구는 클라이언트가 검증할 수 있는 메타데이터와 서명을 게시합니다. 정확한 역할 분담은 경우마다 다릅니다. 일부 업스트림 프로젝트는 자체 패키지를 배포하며, 배포판은 소스에서 독립적으로 빌드할 수도 있습니다.

:::single-choice{#software-distribution-maintainer-role} 다음 중 일반적으로 배포판 패키지 유지 관리자가 담당하는 작업은 무엇입니까?

::option[업스트림 소스를 배포판의 빌드 및 의존성 규칙에 맞게 조정합니다.]{#software-distribution-maintainer-integrates .correct explanation="유지 관리자는 소프트웨어를 배포판 정책, 빌드, 의존성 및 지원 환경에 맞게 조정합니다."}
::option[모든 사용자의 로컬 계정 암호를 선택합니다.]{#software-distribution-maintainer-passwords explanation="로컬 인증 데이터는 패키지 유지 관리와 관련이 없습니다."}
::option[설치된 각 프로세스를 CPU에 스케줄링합니다.]{#software-distribution-maintainer-scheduler explanation="설치 후 CPU 실행은 동작 중인 커널 스케줄러가 처리합니다."}
:::

## 일반적인 네이티브 패키지 형식

널리 사용되는 네이티브 형식 두 가지는 다음과 같습니다.

- `.deb`: 데비안과 우분투, 리눅스 민트 등 데비안에서 파생된 배포판에서 사용
- `.rpm`: 페도라, 레드햇 엔터프라이즈 리눅스 및 여러 관련 배포판에서 사용

그 밖에도 다양한 네이티브 형식과 배포판 공통 형식이 있습니다. 파일 이름의 확장자가 맞는다는 사실만으로 호환성이 보장되지는 않습니다. 패키지 아키텍처, 배포판 릴리스, 라이브러리 버전, 정책, 서명 및 의존성도 서로 맞아야 합니다.

:::single-choice{#software-distribution-debian-format} 데비안과 우분투에서 사용하는 네이티브 패키지 형식은 무엇입니까?

::option[`.deb`]{#software-distribution-format-deb .correct explanation="데비안 계열 패키지 도구는 `.deb` 아카이브 형식을 사용합니다."}
::option[`.rpm`]{#software-distribution-format-rpm explanation="RPM은 페도라, RHEL 및 관련 배포판 계열의 네이티브 형식입니다."}
::option[`.tar`]{#software-distribution-format-tar explanation="tar 아카이브는 범용 컨테이너이며, 그 자체로 데비안 패키지의 메타데이터와 수명 주기 의미 체계를 제공하지는 않습니다."}
:::

## 관리형 배포가 중요한 이유

패키지 관리자는 설치 상태를 기록하고 여러 패키지에 걸친 변경을 조정합니다. 신뢰할 수 있는 배포판 저장소에서 설치하면 일반적으로 일관된 의존성 해결, 서명 검증, 보안 업데이트 및 깔끔한 제거 기능을 이용할 수 있습니다. 바이너리를 직접 복사하거나 소스에서 설치하는 방식도 적절할 수 있지만, 그러한 소프트웨어가 자동으로 관리형 수명 주기에 포함되지는 않습니다.

신뢰 여부는 여전히 저장소 설정과 서명 키에 달려 있습니다. 암호학적으로 유효한 패키지는 신뢰하는 키와 연결되어 있음을 증명할 뿐, 임의의 서드파티 소프트웨어가 안전하거나 적합하다는 뜻은 아닙니다. 가능하면 배포판 저장소를 우선 사용하고, 외부 소스에 설치 권한을 부여하기 전에 그 출처를 평가하십시오.

:::single-choice{#software-distribution-package-manager-benefit} 신뢰할 수 있는 패키지 저장소를 통해 설치할 때 얻는 이점은 무엇입니까?

::option[관리자가 버전을 추적하고 선언된 의존성을 해결할 수 있습니다.]{#software-distribution-managed-lifecycle .correct explanation="저장소 메타데이터와 설치 상태 기록을 통해 설치, 업데이트 및 제거를 체계적으로 관리할 수 있습니다."}
::option[설치된 모든 프로그램이 보안 결함에 영향을 받지 않게 됩니다.]{#software-distribution-no-vulnerabilities explanation="패키지 관리는 업데이트를 지원하지만 결함 없는 소프트웨어를 보장하지는 않습니다."}
::option[모든 배포판의 패키지를 서로 바꾸어 사용할 수 있게 됩니다.]{#software-distribution-universal-compatibility explanation="네이티브 패키지는 여전히 형식, 릴리스, 아키텍처 및 의존성 환경에 종속됩니다."}
:::

[RPM으로 패키지 관리하기](https://labex.io/labs/rhel-managing-packages-with-rpm-in-linux-590868) 실습에서 패키지 메타데이터와 무결성을 살펴보거나, [소스 코드에서 소프트웨어 빌드하기](https://labex.io/labs/comptia-build-software-from-source-code-in-linux-590853) 실습에서 소스 기반 작업 흐름과 관리형 패키지를 비교해 보십시오.

## 요약

이제 리눅스 소프트웨어 배포의 주요 구성 요소를 구분할 수 있습니다.

1. 패키지 페이로드 파일과 패키지 메타데이터를 구분합니다.
2. 업스트림 개발과 배포판 통합의 차이를 이해합니다.
3. `.deb`와 `.rpm`을 각각 사용하는 배포판 계열과 연결합니다.
4. 파일 이름 확장자만이 아니라 호환성과 신뢰 요소를 함께 평가합니다.
