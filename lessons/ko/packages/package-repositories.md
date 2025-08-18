---
lang: "ko"
title: "패키지 저장소"
meta_description: "Linux 패키지 저장소와 소프트웨어 관리 방법에 대해 알아보세요. /etc/apt/sources.list와 같은 패키지 소스를 찾고 추가하여 쉽게 설치하는 방법을 알아보세요."
meta_keywords: "Linux 패키지 저장소, apt sources list, /etc/apt/sources.list, Linux 패키지, Linux 초보자, Linux 튜토리얼, 패키지 관리"
---

## Lesson Content

인터넷에 업로드된 패키지가 어떻게 우리 컴퓨터에 들어오게 될까요? 원하는 각 패키지의 다운로드 페이지로 이동하여 다운로드하고 설치하시나요? 그렇게 할 수도 있지만, 더 나은 해결책이 있습니다: 패키지 저장소 (repository) 입니다. 저장소는 패키지를 위한 중앙 저장 위치입니다. 수많은 패키지를 담고 있는 수많은 저장소가 있으며, 가장 좋은 점은 이 모든 것이 인터넷에서 발견된다는 것입니다. 번거로운 설치 디스크는 필요 없습니다. 명시적으로 어디를 찾아야 할지 알려주지 않으면, 여러분의 기기는 이 저장소들을 어디서 찾아야 할지 모릅니다.

예를 들어, 제 기기에 WackyWidgets 소프트웨어를 설치하고 싶다고 가정해 봅시다. WackyWidgets 는 위젯 패키지를 위한 자체 저장소를 관리합니다. 이 저장소 안에는 CoolWidget 패키지, SuperWidget 패키지 등 10 개의 패키지가 있습니다. WackyWidgets 는 이 저장소를 <http://download.widgets/linux/deb/>라는 소스 링크에서 호스팅합니다.

이제, 웹사이트에 직접 방문하여 패키지를 다운로드하는 대신, 여러분의 기기에 해당 소스 링크에서 WackyWidgets 소프트웨어를 찾도록 지시할 수 있습니다.

여러분의 배포판은 이미 패키지를 가져올 수 있는 사전 승인된 소스와 함께 제공되며, 이것이 시스템에 보이는 모든 기본 패키지를 설치하는 방식입니다. Debian 시스템에서 이 소스 파일은 `/etc/apt/sources.list` 파일입니다. 여러분의 기기는 그곳을 찾아보고 추가한 모든 소스 저장소를 확인할 것입니다.

## Exercise

No exercises for this lesson.

## Quiz Question

Debian 시스템에서 소스 파일은 어디에 있습니까?

## Quiz Answer

/etc/apt/sources.list
