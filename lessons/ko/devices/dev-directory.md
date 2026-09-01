---
lesson_id: "dev-directory"
course_id: "devices"
lang: "ko"
order_index: 1
title: "/dev 디렉터리"
description: "리눅스가 `/dev` 아래의 노드를 통해 장치 인터페이스와 의사 장치를 노출하는 방식을 알아봅니다."
meta_title: "/dev 디렉터리 - 장치"
meta_description: "리눅스 /dev 디렉터리의 목적을 알아봅니다. ls /dev로 살펴보는 방법과 시스템 하드웨어를 위한 장치 파일의 역할을 설명합니다."
meta_keywords: "리눅스 dev, 리눅스 /dev 디렉터리, 리눅스 dev 폴더, ls /dev, 리눅스 장치 파일, 장치 노드, 리눅스 장치"
---

리눅스는 여러 커널 장치 인터페이스를 장치 노드라는 특수 파일 시스템 객체로 노출합니다. 장치 노드는 보통 `/dev` 아래에 유용한 심볼릭 링크 및 통신 엔드포인트와 함께 나타납니다. 장치 노드를 열면 애플리케이션은 일반 파일에 저장된 바이트가 아니라 커널 드라이버에 연결됩니다.

## `/dev` 살펴보기

장치를 역참조하거나 읽지 않고 디렉터리 목록을 표시합니다.

```bash
$ ls -l /dev
```

항목은 물리 저장 장치, 터미널, 입력 인터페이스, 논리 장치 또는 커널이 제공하는 의사 장치를 나타낼 수 있습니다. 모든 하드웨어 구성 요소에 사용자에게 보이는 노드가 필요한 것은 아니며, 장치 하나가 여러 링크나 인터페이스로 표현될 수도 있습니다.

긴 목록의 첫 번째 문자는 파일 시스템 객체 유형을 나타냅니다. 문자 장치 노드와 블록 장치 노드는 각각 `c`와 `b`로 표시됩니다. 이후 수업에서 이러한 유형과 주 번호 및 부 번호를 살펴봅니다.

:::single-choice{#dev-directory-device-node-purpose} 프로그램이 `/dev` 아래의 장치 노드를 열면 어떻게 됩니까?

::option[항상 하드웨어 복사본을 담은 일반 디스크 파일을 읽습니다.]{#dev-directory-ordinary-copy explanation="장치 노드는 특수 객체이며 장치 데이터의 복사본을 일반 파일처럼 저장하지 않습니다."}
::option[커널 드라이버가 구현한 인터페이스에 접근합니다.]{#dev-directory-kernel-interface .correct explanation="장치 노드 작업은 노드의 장치 식별자를 통해 커널 드라이버 동작으로 전달됩니다."}
::option[해당 장치의 드라이버 소스 코드를 다시 컴파일합니다.]{#dev-directory-recompile-driver explanation="인터페이스를 연다고 해서 컴파일러가 호출되거나 커널 모듈이 다시 빌드되지는 않습니다."}
:::

## 의사 장치

일부 노드는 물리 하드웨어에 대응하지 않으면서 커널 서비스를 제공합니다. `/dev/null`은 기록된 데이터를 받아 버립니다.

```bash
$ command > /dev/null
```

그 밖의 익숙한 예로는 0 바이트를 생성하는 `/dev/zero`와 커널 난수 하위 시스템을 통해 난수 바이트를 제공하는 `/dev/urandom`이 있습니다. 각 장치에는 고유한 의미가 있으므로 파일 이름만 보고 동작을 추정하지 마십시오.

:::single-choice{#dev-directory-null-behavior} `/dev/null`은 기록된 데이터를 어떻게 처리합니까?

::option[다음 재부팅 때까지 데이터를 저장합니다.]{#dev-directory-null-temporary-storage explanation="null 장치는 데이터 싱크이며 임시 저장소처럼 동작하지 않습니다."}
::option[로그인한 모든 터미널에 데이터를 전송합니다.]{#dev-directory-null-broadcast explanation="터미널 브로드캐스트는 null 의사 장치와 관련이 없습니다."}
::option[데이터를 버립니다.]{#dev-directory-null-discards .correct explanation="null 장치는 쓰기를 받아들이지만 내용을 보존하지 않습니다."}
:::

## 동적 장치 관리

최신 리눅스 시스템에서는 커널이 지원하는 `devtmpfs`가 장치가 나타날 때 기본 장치 노드를 채울 수 있습니다. `udev` 같은 사용자 공간 장치 관리자는 이벤트를 처리하고, 권한과 소유권을 적용하며, 유용한 심볼릭 링크 또는 정책 기반 이름을 만듭니다. 정확한 역할 분담은 시스템마다 다릅니다.

`/dev/disk/by-id/` 또는 `/dev/disk/by-uuid/` 아래의 항목 같은 안정적인 링크는 하드웨어 구성이나 검색 순서가 바뀌면 달라질 수 있는 `/dev/sda` 같은 감지 순서 기반 이름보다 설정에서 더 안전할 수 있습니다.

:::single-choice{#dev-directory-persistent-link} 관리자가 설정에서 `/dev/sda`보다 `/dev/disk/by-id/...`를 선호할 수 있는 이유는 무엇입니까?

::option[식별자 기반 링크가 장치 검색 순서에 덜 의존하기 때문입니다.]{#dev-directory-stable-identifier .correct explanation="영구 링크는 열거 순서에 따라 배정된 문자가 아니라 장치 속성에서 파생됩니다."}
::option[링크가 장치의 모든 블록을 자동으로 백업하기 때문입니다.]{#dev-directory-link-backup explanation="심볼릭 링크는 같은 장치에 이름을 붙일 뿐 백업 데이터를 만들지 않습니다."}
::option[링크가 대상 장치의 모든 권한을 우회하기 때문입니다.]{#dev-directory-link-permissions explanation="심볼릭 링크를 통해 열어도 대상 장치와 그 접근 제어에 도달합니다."}
:::

## 안전하게 상호 작용하기

표준 도구로 장치 노드를 열 수 있다고 해서 임의의 읽기와 쓰기가 안전한 것은 아닙니다. 읽기는 민감한 입력이나 저장 내용을 노출할 수 있고, 디스크, 터미널 또는 펌웨어 인터페이스에 쓰면 데이터가 손상되거나 사용자가 방해받을 수 있습니다. 이런 이유로 장치 노드 권한, 그룹, ACL, 기능 및 서비스 중개가 접근을 제한합니다.

먼저 읽기 전용 검색 도구를 사용하고, 정확한 노드와 장치 식별자를 확인한 뒤, 장치별 문서를 따르십시오. 중요한 시스템에서 익숙하지 않은 `/dev` 항목으로 데이터를 리디렉션하는 실험은 절대 하지 마십시오.

:::single-choice{#dev-directory-direct-write-risk} 익숙하지 않은 장치 노드에 임의의 데이터를 쓰지 말아야 하는 이유는 무엇입니까?

::option[모든 장치 노드는 무해한 텍스트 파일임이 보장되기 때문입니다.]{#dev-directory-harmless-text explanation="장치 노드는 일반 텍스트 파일과 본질적으로 다릅니다."}
::option[작업이 하드웨어, 저장 장치 또는 다른 커널 인터페이스에 직접 영향을 줄 수 있기 때문입니다.]{#dev-directory-write-impact .correct explanation="장치 쓰기는 드라이버가 정의한 작업을 호출하므로 파괴적이거나 방해가 되는 결과를 일으킬 수 있습니다."}
::option[리눅스가 모든 장치 쓰기를 읽기 전용 목록으로 변환하기 때문입니다.]{#dev-directory-write-listing explanation="쓰기의 의미는 드라이버가 결정하며 커널이 모든 쓰기를 목록으로 변환하지는 않습니다."}
:::

제어된 환경에서 [리눅스 하드웨어 장치 살펴보기](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)를 이용해 읽기 전용 검사를 연습해 보십시오.

## 요약

이제 `/dev`를 커널과 연결되는 실시간 인터페이스의 집합으로 설명할 수 있습니다.

1. 장치 노드와 일반 파일을 구분합니다.
2. `/dev/null` 같은 의사 장치를 식별합니다.
3. 동적 노드 및 영구 링크를 장치 관리와 연결합니다.
4. 직접 장치 접근을 인터페이스별이며 잠재적으로 파괴적인 작업으로 취급합니다.
