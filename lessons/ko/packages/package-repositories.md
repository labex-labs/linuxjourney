---
index: 2
lang: "ko"
title: "패키지 저장소"
meta_title: "패키지 저장소 - 패키지"
meta_description: "Linux 패키지 저장소와 소프트웨어 관리 방법에 대해 알아보세요. 쉬운 설치를 위해 /etc/apt/sources.list와 같은 패키지 소스를 찾고 추가하는 방법을 알아보세요."
meta_keywords: "Linux 패키지 저장소, apt 소스 목록, /etc/apt/sources.list, Linux 패키지, 초보자 Linux, Linux 튜토리얼, 패키지 관리"
---

## Lesson Content

인터넷에 업로드된 패키지가 어떻게 우리 컴퓨터에 도달할까요? 원하는 각 패키지의 다운로드 페이지로 이동하여 다운로드하고 설치하시나요? 그렇게 할 수도 있지만, 더 나은 해결책이 있습니다: 패키지 저장소 (repository) 입니다. 저장소는 패키지를 위한 중앙 저장 위치입니다. 수많은 패키지를 담고 있는 엄청난 수의 저장소가 있으며, 무엇보다도 이들은 모두 인터넷에서 찾을 수 있습니다. 어리석은 설치 디스크는 필요 없습니다. 명시적으로 알려주지 않으면 컴퓨터는 이러한 저장소를 어디서 찾아야 할지 모릅니다.

예를 들어, 제 컴퓨터에 Docker 소프트웨어를 설치하고 싶다고 가정해 봅시다. Docker 는 컨테이너 패키지를 위한 자체 저장소를 관리합니다. 이 저장소 안에는 `docker-ce` 패키지, `docker-ce-cli` 패키지, `containerd.io` 패키지 등 여러 패키지가 있습니다. Docker 는 이 저장소를 `https://download.docker.com/linux/ubuntu`라는 소스 링크에서 호스팅합니다.

이제 웹사이트에 직접 가서 패키지를 다운로드하는 대신, 컴퓨터에 해당 소스 링크에서 Docker 소프트웨어를 찾도록 지시할 수 있습니다.

배포판에는 이미 패키지를 가져올 수 있는 사전 승인된 소스가 포함되어 있으며, 이것이 시스템에 보이는 모든 기본 패키지를 설치하는 방법입니다. Debian 시스템에서는 이 소스 파일이 `/etc/apt/sources.list` 파일입니다. 컴퓨터는 그곳을 찾아보고 추가한 모든 소스 저장소를 확인할 것입니다.

## Exercise

연습하면 완벽해집니다! 다음은 Linux 패키지 관리 및 저장소에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에 소프트웨어 설치](https://labex.io/ko/labs/linux-software-installation-on-linux-18005)** - `sources.list` 개념과 직접적으로 관련된 apt 사용 및 .deb 파일 처리 등 Ubuntu 시스템에서 소프트웨어를 설치하고 관리하는 다양한 방법을 연습합니다.
2. **[패키지 설치 및 제거](https://labex.io/ko/labs/linux-installing-and-removing-packages-385380)** - Debian 기반 시스템에서 시스템을 업데이트하고 패키지를 설치 및 제거하는 방법을 학습하여 패키지 관리자가 저장소와 상호 작용하는 방식에 대한 이해를 확고히 합니다.
3. **[Linux 에서 YUM 으로 패키지 쿼리 및 업데이트](https://labex.io/ko/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - YUM 을 사용하여 RHEL 기반 Linux 시스템에서 소프트웨어 패키지를 관리하는 방법을 탐색하여 다양한 배포판에 걸친 패키지 관리에 대한 더 넓은 시야를 제공합니다.

이러한 랩은 패키지 저장소 및 소프트웨어 관리 개념을 실제 시나리오에 적용하고 시스템 관리 작업에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

Debian 시스템에서 소스 파일은 어디에 있습니까?

## Quiz Answer

/etc/apt/sources.list
