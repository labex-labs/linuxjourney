---
lesson_id: "sysfs"
course_id: "devices"
lang: "ko"
order_index: 4
title: "sysfs"
description: "sysfs가 `/sys` 아래에 리눅스 커널의 실시간 장치, 드라이버, 버스 및 클래스 모델을 노출하는 방법을 알아봅니다."
meta_title: "sysfs - 장치"
meta_description: "sysfs와 리눅스 시스템에서의 역할을 살펴봅니다. 장치 정보를 제공하는 가상 파일 시스템인 /sys 디렉터리를 설명하고 /dev와 비교합니다."
meta_keywords: "sysfs, sysfs란, /sys, 리눅스 /sys, 리눅스 시스템, 가상 파일 시스템, 리눅스 장치, /dev"
---

`sysfs`는 일반적으로 `/sys`에 마운트되는 가상 파일 시스템입니다. 디렉터리, 심볼릭 링크 및 작은 속성 파일을 통해 커널 객체와 그 관계를 나타냅니다. 장치 검색 도구와 관리자는 이를 이용해 커널의 현재 장치 모델을 파악합니다.

## 장치 모델 탐색하기

중요한 최상위 뷰는 다음과 같습니다.

- `/sys/devices/`: 물리 및 논리 장치 계층
- `/sys/class/`: 블록이나 네트워크 같은 기능 클래스별로 묶은 장치
- `/sys/bus/`: 버스와 그 장치 및 드라이버
- `/sys/block/`: 블록 장치를 편리하게 보여 주는 뷰
- `/sys/dev/`: 문자 또는 블록 장치의 주 번호와 부 번호로 색인한 링크

`/sys/devices` 외부의 여러 항목은 표준 계층을 가리키는 심볼릭 링크입니다. 실제 부모 경로가 필요하면 `readlink -f`로 링크를 해석합니다.

```bash
$ readlink -f /sys/class/block/sda
```

다른 저장 인터페이스를 사용하는 시스템에는 예시의 이름이 없을 수 있습니다.

:::single-choice{#sysfs-canonical-device-tree}
커널의 기본 장치 계층이 들어 있는 sysfs 하위 트리는 무엇입니까?

::option[`/sys/passwords/`]{#sysfs-passwords-tree explanation="sysfs는 사용자 인증 비밀 정보를 저장하는 곳이 아닙니다."}
::option[`/sys/devices/`]{#sysfs-devices-tree .correct explanation="devices 하위 트리는 장치의 부모-자식 토폴로지를 나타내며 클래스 및 버스 뷰가 이곳을 가리킵니다."}
::option[`/sys/packages/`]{#sysfs-packages-tree explanation="설치된 패키지 상태는 이 sysfs 경로가 아니라 배포판 패키지 도구가 관리합니다."}
:::

## 속성 읽기

속성 파일은 개별 값이나 제어 항목을 노출합니다. 블록 장치의 예는 다음과 같습니다.

```bash
$ cat /sys/class/block/sda/dev
8:0
$ cat /sys/class/block/sda/ro
0
$ cat /sys/class/block/sda/size
1953525168
```

`dev`는 장치의 주 번호와 부 번호를 보고합니다. `ro`는 블록 장치의 읽기 전용 플래그를 보고합니다. 리눅스 블록 장치에서 `size`는 장치의 물리 섹터 크기와 관계없이 관례상 512바이트 섹터 단위로 표시됩니다. 특정 속성의 단위와 의미는 항상 커널 ABI 문서를 확인하십시오.

:::single-choice{#sysfs-dev-attribute}
블록 장치의 sysfs `dev` 속성에는 일반적으로 무엇이 들어 있습니까?

::option[현재 장치에 저장된 모든 파일입니다.]{#sysfs-file-list explanation="파일 시스템 디렉터리 트리는 이 작은 장치 속성에 포함되지 않습니다."}
::option[하드웨어를 설치한 패키지 이름입니다.]{#sysfs-package-name explanation="하드웨어는 `dev` 속성으로 식별되는 패키지로 설치되지 않습니다."}
::option[장치의 주 번호와 부 번호입니다.]{#sysfs-major-minor .correct explanation="이 속성은 sysfs 객체를 해당 블록 장치 식별자와 연결합니다."}
:::

## `/sys`와 `/dev` 연결하기

`/dev`에는 애플리케이션이 장치 입출력을 위해 여는 노드가 있습니다. `/sys`는 객체 관계, 속성, 상태 및 일부 제어 항목을 노출합니다. `/dev/sda` 같은 블록 노드는 `/sys/dev/block/8:0`과 일치시킬 수 있으며, 이 링크는 관련 sysfs 객체로 해석됩니다.

두 인터페이스는 서로 보완합니다. 어느 쪽도 모든 하드웨어 사실을 완전하게 담은 독립형 목록은 아니며, 검사하는 동안 장치가 사라질 수도 있습니다.

:::single-choice{#sysfs-versus-dev}
`/sys`와 `/dev`의 차이를 올바르게 설명한 것은 무엇입니까?

::option[`/sys`는 사용자 문서를 저장하고 `/dev`는 패키지 아카이브를 저장합니다.]{#sysfs-dev-user-files explanation="두 디렉터리 모두 그러한 일반 데이터 저장 역할을 하지 않습니다."}
::option[`/sys`는 커널 객체 속성을 노출하고 `/dev`는 입출력을 위한 장치 노드를 제공합니다.]{#sysfs-dev-distinction .correct explanation="sysfs는 객체와 제어 항목을 모델링하고 장치 노드는 작업을 문자 또는 블록 드라이버로 전달합니다."}
::option[두 디렉터리는 설치 중 한 번만 만들어지는 정적 목록입니다.]{#sysfs-dev-static explanation="장치와 커널 객체가 나타나거나 사라지면 보이는 상태도 바뀝니다."}
:::

## 안전하게 속성 쓰기

일부 sysfs 속성은 쓸 수 있으며 전원 상태, 드라이버 바인딩, 큐 동작, 장치 인증, LED 또는 다른 실시간 제어 항목을 변경할 수 있습니다. 텍스트 쓰기가 성공하면 하드웨어나 서비스에 즉시 영향을 줄 수 있으며, 이는 영구 설정 파일을 편집하는 것과 같지 않습니다.

문서화된 ABI와 현재 값을 읽고, 설정을 영구 적용하는 방법을 파악하며, 권한이 있는 시스템에서만 테스트하십시오. `/sys` 전체의 권한을 재귀적으로 편집하거나 추측한 값을 쓰지 마십시오.

:::single-choice{#sysfs-write-risk}
sysfs 속성에 쓰는 작업이 운영상 중요한 이유는 무엇입니까?

::option[모든 쓰기가 디스크에 일반 백업 사본을 만들기 때문입니다.]{#sysfs-backup-copy explanation="sysfs는 가상 파일 시스템이며 제어 변경을 자동으로 백업하지 않습니다."}
::option[속성이 쓰기 가능해도 sysfs가 모든 쓰기를 무시하기 때문입니다.]{#sysfs-ignore-writes explanation="쓰기 가능한 속성은 지원되는 제어 값을 받아들이기 위해 존재합니다."}
::option[쓰기가 실시간 커널 또는 드라이버 제어를 호출할 수 있기 때문입니다.]{#sysfs-live-control .correct explanation="쓰기 가능한 속성은 활성 인터페이스이며 장치 동작을 즉시 바꿀 수 있습니다."}
:::

[리눅스 하드웨어 장치 살펴보기](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)에서 sysfs를 읽기 전용으로 탐색하고 장치 노드와 연결해 보십시오.

## 요약

이제 sysfs를 실시간 커널 객체의 구조화된 뷰로 사용할 수 있습니다.

1. 장치, 클래스, 버스, 블록 및 장치 번호 뷰를 탐색합니다.
2. 문서화된 속성을 올바른 단위로 하나씩 읽습니다.
3. sysfs 객체를 `/dev` 노드와 연결합니다.
4. 쓰기 가능한 속성을 실시간 제어 인터페이스로 취급합니다.
