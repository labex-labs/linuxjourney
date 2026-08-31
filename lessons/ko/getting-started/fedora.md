---
lesson_id: "fedora"
course_id: "getting-started"
lang: "ko"
order_index: 6
title: "페도라"
description: "Fedora가 Red Hat과 연결된 커뮤니티 프로젝트로 최신 리눅스 기술을 제공하는 방식을 배웁니다."
meta_title: "페도라 리눅스 배포판"
meta_description: "페도라 리눅스 배포판의 정의, 레드햇과의 관계, DNF 패키지 관리 방식, 그리고 개발자와 데스크톱 사용자에게 인기 있는 이유를 알아보세요."
meta_keywords: "페도라 리눅스, 페도라 리눅스 배포판, 페도라란, 페도라 레드햇, 페도라 릴리스, DNF 패키지 관리, 리눅스 배포판"
---

## Fedora란 무엇인가?

Fedora 는 Red Hat 이 후원하는 커뮤니티 주도형 리눅스 배포판입니다. 최신 기술을 도입하고 세련된 데스크톱 환경을 제공하며, 개발자와 기술 사용자에게 강력한 지원을 제공하는 것으로 유명합니다.

Fedora 는 보수적인 배포판보다 빠르게 발전하면서도 품질과 사용성을 유지하는 것으로 정평이 나 있습니다. 이러한 균형 덕분에 모든 것을 처음부터 구축하지 않고도 현대적인 리눅스 시스템을 원하는 사용자들에게 매력적입니다.

:::single-choice{#identify-fedora-project-model}
Fedora 프로젝트를 올바르게 설명한 것은 무엇인가요?

::option[지원이 중단된 Red Hat Enterprise Linux 버전입니다.]{#discontinued-rhel explanation="Fedora는 자체 릴리스를 제공하는 활성 배포판이며 오래된 RHEL 버전이 아니라 RHEL의 업스트림입니다."}
::option[한 하드웨어 제조사가 유지하는 배포판입니다.]{#hardware-maintained explanation="Fedora가 하드웨어 업체와 협력하기는 하지만 개발은 커뮤니티가 주도하고 Red Hat이 후원합니다."}
::option[Red Hat이 후원하는 커뮤니티 프로젝트입니다.]{#community-sponsored .correct explanation="Fedora는 Red Hat의 후원과 지원을 받는 커뮤니티가 만들며 독립적인 커뮤니티 배포판입니다."}
:::

## Fedora가 돋보이는 이유

Fedora 는 기업용 배포판보다 새로운 리눅스 기능을 더 빨리 도입하기 때문에 돋보입니다. 이로 인해 개발자, 오픈 소스 기여자, 그리고 강력한 업스트림 연결을 갖춘 최신 시스템을 원하는 데스크톱 사용자들에게 인기가 많습니다.

또한 깔끔한 기본 환경을 제공하는 것으로도 잘 알려져 있습니다. Fedora Workstation 은 현대적인 데스크톱, 최신 도구, 컨테이너, 가상화 및 기타 개발 워크플로우에 대한 우수한 지원을 원하는 개발자들 사이에서 특히 인기가 높습니다.

:::single-choice{#match-fedora-user}
Fedora Workstation과 가장 잘 맞는 사용자 목표는 무엇인가요?

::option[하나의 기업용 릴리스를 수년 동안 바꾸지 않고 유지합니다.]{#long-enterprise-lifecycle explanation="길고 보수적인 기업 수명 주기는 RHEL의 역할에 더 가깝고 Fedora는 더 빠른 릴리스와 업그레이드 일정을 따릅니다."}
::option[세련된 데스크톱 시스템에서 최신 개발 도구를 사용합니다.]{#current-developer-desktop .correct explanation="Fedora Workstation은 잘 구성된 데스크톱과 최신 개발, 컨테이너, 가상화 도구를 결합하므로 이 목표와 직접 맞습니다."}
::option[모든 시스템 구성 요소를 소스에서 직접 빌드합니다.]{#fedora-manual-source explanation="Fedora는 완성된 패키지 시스템을 제공해 사용자가 모든 구성 요소를 빌드할 필요가 없으며 이는 더 특수한 작업 흐름입니다."}
:::

## Fedora와 Red Hat

Fedora 는 Red Hat 생태계에서 중요한 역할을 합니다. 새로운 기술과 변경 사항은 종종 Fedora 에 먼저 적용되며, 그중 일부는 나중에 Red Hat Enterprise Linux(RHEL) 에 영향을 미칩니다. 이러한 관계는 RHEL 이 더 보수적이고 기업 중심적인 반면, Fedora 가 왜 더 최신 상태를 유지하는지를 설명해 줍니다.

Fedora 를 기업용 옵션과 비교하고 싶다면 [Red Hat Enterprise Linux](https://labex.io/ko/lesson/red-hat-enterprise-linux)를 참조하세요. 배포판 계열을 비교 중이라면 [리눅스 배포판 선택하기](https://labex.io/ko/lesson/choosing-a-linux-distribution)에서 더 넓은 개요를 확인할 수 있습니다.

:::single-choice{#explain-fedora-upstream-role}
Fedora와 RHEL의 업스트림 관계는 무엇을 뜻하나요?

::option[RHEL 릴리스를 나중에 Fedora로 그대로 복사합니다.]{#rhel-copied-to-fedora explanation="관계를 반대로 설명했습니다. Fedora는 더 빠르게 움직이며 RHEL의 나중 복사본이 아니라 업스트림 역할을 합니다."}
::option[Fedora와 RHEL은 항상 같은 소프트웨어 버전을 제공합니다.]{#identical-software-versions explanation="두 배포판은 릴리스 목표와 일정이 다르며 RHEL은 Fedora의 모든 버전을 맞추는 대신 기술을 선택해 안정화합니다."}
::option[Fedora에서 개발된 작업이 나중에 RHEL에 영향을 줄 수 있습니다.]{#fedora-influences-rhel .correct explanation="Fedora는 새로운 기술을 더 일찍 통합하며 그중 일부가 나중에 Red Hat의 기업 플랫폼에 기여합니다."}
:::

## Fedora 릴리스

Fedora 는 정기적인 릴리스 주기를 따르며, 대부분의 해에 두 번의 주요 릴리스가 있고 각 릴리스는 약 13 개월 동안 지원됩니다. 더 보수적인 배포판과 비교하여 Fedora 는 더 빠른 일정으로 최신 커널, 데스크톱 환경 및 개발자 도구를 제공하는 경향이 있습니다.

이로 인해 Fedora 는 최신 소프트웨어를 원하면서도 수동적인 롤링 릴리스 시스템보다는 체계적이고 주류인 리눅스 배포판을 선호하는 사용자에게 적합합니다.

:::single-choice{#plan-fedora-upgrades}
Fedora 사용자는 릴리스 모델에 따라 어떤 유지 관리를 예상해야 하나요?

::option[컴퓨터 수명 동안 버전 업그레이드가 필요 없습니다.]{#no-version-upgrades explanation="Fedora 버전의 지원 기간은 제한되어 있으므로 계속 지원받으려면 시간이 지나면서 새 릴리스로 이동해야 합니다."}
::option[지원되는 릴리스를 유지하기 위한 정기 업그레이드]{#regular-release-upgrades .correct explanation="Fedora는 비교적 빠른 주기로 릴리스되고 약 13개월 동안 업데이트되므로 정기적인 버전 업그레이드를 계획해야 합니다."}
::option[구분된 시스템 릴리스 없이 계속되는 패키지 변경]{#no-distinct-releases explanation="Fedora는 일반적인 롤링 릴리스가 아니라 구분된 주요 릴리스를 내며 패키지가 최신이어도 릴리스 구분은 중요합니다."}
:::

## 패키지 관리

Fedora 는 소프트웨어를 설치, 업데이트 및 제거하기 위해 RPM 패키지 형식과 DNF 패키지 관리자를 사용합니다. DNF 는 Fedora 환경의 핵심이며 사용자가 시스템을 최신 상태로 유지하기 위해 의존하는 주요 도구 중 하나입니다.

Fedora 의 패키지 관리는 직관적이며, 더 넓은 Red Hat 계열 시스템과 자연스럽게 호환됩니다.

:::single-choice{#identify-fedora-package-tool}
Fedora가 상위 수준의 패키지 관리에 사용하는 도구는 무엇인가요?

::option[APT]{#fedora-apt-tool explanation="APT는 데비안 기반 배포판과 관련된 도구이며 Fedora는 RPM 패키지 계열에 속해 DNF를 사용합니다."}
::option[DNF]{#fedora-dnf-tool .correct explanation="DNF는 Fedora 저장소의 패키지를 설치, 업데이트, 제거하며 그 아래에서 RPM 형식을 사용합니다."}
::option[Pacman]{#fedora-pacman-tool explanation="Pacman은 Arch Linux의 패키지 관리자이며 Fedora의 상위 패키지 도구는 DNF입니다."}
:::

## 일반적인 용도

Fedora 는 일반적으로 개발자 워크스테이션, 기술 데스크톱 및 노트북에서 사용됩니다. 코딩, 컨테이너, 가상 머신 및 일반적인 데스크톱 작업을 위한 현대적인 리눅스 환경을 원하는 사용자에게 특히 매력적입니다.

Fedora 는 서버에서도 사용할 수 있지만, 가장 강력한 정체성은 최신 개발자 친화적인 리눅스 배포판입니다.

## Fedora는 초보자에게 친숙한가?

Fedora 는 초보자에게 친숙할 수 있지만, 일반적으로 다소 빠르게 변화하는 시스템에 익숙한 사용자에게 더 적합합니다. 수동 설정이 많은 배포판보다는 접근하기 쉽지만, Debian 보다 덜 보수적이거나 Ubuntu 또는 Linux Mint 보다 초보자 중심적이지 않게 느껴질 수 있습니다.

현대적인 리눅스 배포판을 원하고 배우는 과정을 즐기는 사용자에게 Fedora 는 강력한 선택지입니다.

## 추가 읽기 자료

- [Fedora Workstation](https://fedoraproject.org/workstation/)
- [Fedora 문서](https://docs.fedoraproject.org/)
- [Fedora 릴리스 수명 주기](https://docs.fedoraproject.org/en-US/releases/lifecycle/)
- [Fedora Workstation 워킹 그룹](https://docs.fedoraproject.org/en-US/workstation-working-group/)

Fedora 에 대해 학습한 후 실질적인 리눅스 기술을 쌓기 위해 다음 LabEx 과정을 추천합니다:

1. **[리눅스 퀵 스타트](https://labex.io/ko/courses/quick-start-with-linux)** - 여러 배포판에 공통으로 적용되는 Linux 기초를 다룹니다.
2. **[리눅스 명령어 온라인 실습](https://labex.io/ko/courses/linux-basic-commands-practice-online)** - 일상적인 Linux 작업에 중요한 명령줄 습관을 강화합니다.
3. **[RPM 및 DNF 패키지 관리](https://labex.io/ko/courses/rpm-and-dnf-package-management)** - RPM 및 DNF 관련 패키지 관리 개념을 연습합니다.

## 요약

이제 Fedora가 Red Hat 생태계에서 최신 기술을 제공하는 커뮤니티 배포판인 이유를 설명할 수 있습니다.

1. Fedora의 커뮤니티 및 후원 모델을 설명할 수 있습니다.
2. Fedora Workstation이 지원하는 사용자와 작업 흐름을 알아볼 수 있습니다.
3. Fedora와 RHEL의 업스트림 관계를 설명할 수 있습니다.
4. Fedora의 정기 릴리스 업그레이드를 계획할 수 있습니다.
5. DNF가 Fedora의 패키지 관리 도구임을 알 수 있습니다.
