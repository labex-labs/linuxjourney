---
lesson_id: "udev"
course_id: "devices"
lang: "ko"
order_index: 5
title: "udev"
description: "udev가 커널 장치 이벤트를 처리해 정책, 권한 및 영구 링크를 적용하는 방법을 알아봅니다."
meta_title: "udev - 장치"
meta_description: "udev가 리눅스 장치 파일을 동적으로 관리하는 방식과 udevadm 사용법을 알아봅니다. 장치 노드 생성과 udev 규칙을 이해합니다."
meta_keywords: "udev, udevadm, 리눅스 장치 관리, 장치 파일, 리눅스 튜토리얼, udev 규칙, 리눅스 가이드"
---

리눅스 커널은 uevent를 통해 장치 변경을 사용자 공간에 보고합니다. 현재 여러 배포판에서는 `systemd-udevd`가 udev 규칙과 장치 데이터베이스를 사용해 이러한 이벤트를 처리합니다. 커널이 채우는 `devtmpfs`와 함께 작동하여 애플리케이션이 `/dev` 주변에서 보는 소유권, 권한, 속성 및 심볼릭 링크를 만듭니다.

## 커널 이벤트에서 장치 정책으로

장치가 추가, 변경, 이동 또는 제거되면 udev는 다음 작업을 수행할 수 있습니다.

- sysfs의 속성과 이벤트 속성 읽기
- 장치 노드에 소유자, 그룹 및 모드 정책 적용
- `/dev/disk/by-id/...` 같은 안정적인 심볼릭 링크 추가
- 다른 서비스를 위해 장치에 태그 지정
- 범위가 좁게 정의된 보조 처리 실행

실제 장치와 드라이버는 여전히 커널이 담당합니다. `/dev`에서 노드를 삭제해도 하드웨어가 물리적으로 제거되지 않으며, `mknod`로 노드를 직접 만들어도 지원되지 않는 하드웨어가 생기거나 드라이버가 바인딩되지는 않습니다.

:::single-choice{#udev-kernel-event-input}
장치 변경 시 일반적으로 udev 처리를 시작하는 것은 무엇입니까?

::option[APT가 수행하는 패키지 저장소 새로 고침입니다.]{#udev-apt-refresh explanation="패키지 메타데이터 갱신은 실시간 장치 이벤트 처리와 관련이 없습니다."}
::option[사용자가 `/dev` 아래의 모든 파일 이름을 직접 바꾸는 작업입니다.]{#udev-manual-renaming explanation="동적 정책은 대량 수동 이름 변경이 아니라 커널 이벤트와 규칙에 의해 구동됩니다."}
::option[장치 작업을 설명하는 커널 uevent입니다.]{#udev-kernel-uevent .correct explanation="udev는 커널에서 장치 이벤트를 받아 일치하는 사용자 공간 규칙을 적용합니다."}
:::

## 규칙 위치와 우선순위

규칙은 일반적으로 다음 위치에 있습니다.

- `/usr/lib/udev/rules.d/`: 공급업체 또는 패키지가 제공하는 규칙
- `/run/udev/rules.d/`: 휘발성 런타임 규칙
- `/etc/udev/rules.d/`: 로컬 관리자 정책

파일은 파일 이름의 사전식 순서로 처리되며, 설치된 udev 구현의 규칙에 따라 우선순위가 높은 디렉터리의 같은 이름 파일이 낮은 우선순위 버전을 대체합니다. 로컬 규칙에는 의도적으로 정한 파일 이름을 사용하고 열거 이름 대신 안정적인 속성과 일치시키십시오.

규칙 하나가 일치하는 모든 장치에 영향을 줄 수 있으므로 범위를 신중하게 테스트하십시오. 로컬 재정의나 보충 규칙이 적합하다면 패키지에서 제공한 규칙을 직접 편집하지 마십시오.

:::single-choice{#udev-local-rules-directory}
영구적인 로컬 관리자 udev 규칙을 위한 디렉터리는 무엇입니까?

::option[`/proc/udev/rules.d/`]{#udev-proc-rules explanation="procfs는 영구적인 로컬 규칙 디렉터리를 제공하지 않습니다."}
::option[`/etc/udev/rules.d/`]{#udev-etc-rules .correct explanation="로컬 정책은 패키지가 관리하는 공급업체 규칙과 분리하여 `/etc` 아래에 둡니다."}
::option[`/dev/udev/rules.d/`]{#udev-dev-rules explanation="`/dev`에는 영구 규칙 설정이 아니라 런타임 장치 인터페이스 객체가 있습니다."}
:::

## `udevadm`으로 장치 검사하기

기존 노드의 udev 속성을 조회합니다.

```bash
$ udevadm info --query=all --name=/dev/sda
```

현재 시스템에 존재하는 노드를 사용하십시오. `udevadm info --attribute-walk --name=...`는 sysfs 부모 체인의 속성을 표시하여 규칙을 만드는 데 도움을 줄 수 있습니다. `udevadm monitor --kernel --udev --property`는 커널 이벤트와 처리된 이벤트를 관찰합니다. 장치 식별자가 노출될 수 있으므로 캡처한 출력을 적절히 다루십시오.

:::single-choice{#udev-info-purpose}
`udevadm info --query=all --name=/dev/sda`가 요청하는 것은 무엇입니까?

::option[디스크 파티션 테이블의 파괴적인 재작성입니다.]{#udev-info-partition-write explanation="이 조회는 검사 작업이며 저장 장치를 포맷하거나 다시 파티셔닝하지 않습니다."}
::option[인터넷에서 누락된 커널 드라이버를 설치하는 작업입니다.]{#udev-info-install-driver explanation="udevadm 검사는 패키지 다운로드 도구처럼 동작하지 않습니다."}
::option[지정한 장치 노드에 알려진 udev 속성입니다.]{#udev-info-properties .correct explanation="info 명령은 장치 데이터베이스와 관련 sysfs 정보를 조회합니다."}
:::

## 신중하게 규칙 변경 적용하기

규칙 파일을 다시 불러오면 이후 이벤트 처리가 바뀌지만, 기존의 모든 장치 상태가 자동으로 다시 구성되지는 않습니다. 이벤트를 수동으로 트리거하면 여러 장치와 서비스에 영향을 줄 수 있으므로 대상을 좁히고 설치된 `udevadm` 문서를 따르십시오. 테스트 명령은 규칙 평가를 시뮬레이션할 수 있지만 실제 이벤트의 모든 부작용을 재현하지는 못할 수 있습니다.

권한이나 이름을 변경하기 전에 로컬 규칙을 백업하고, 구문을 검증하며, 알려진 테스트 장치 하나를 관찰하고, 복구 경로를 마련하십시오. udev 이벤트 처리 안에서 장시간 실행되는 작업은 피하고 적절한 서비스에 위임하십시오.

:::single-choice{#udev-reload-effect}
udev 규칙을 다시 불러오면 주로 무엇이 바뀝니까?

::option[이후 일치하는 장치 이벤트가 처리되는 방식입니다.]{#udev-future-events .correct explanation="다시 불러오면 메모리 내 규칙이 갱신됩니다. 장치를 다시 평가하려면 여전히 이벤트가 발생하거나 의도적으로 트리거되어야 합니다."}
::option[연결된 모든 장치의 물리 배선입니다.]{#udev-physical-wiring explanation="소프트웨어 규칙을 불러오는 작업으로 하드웨어 연결을 바꿀 수는 없습니다."}
::option[이벤트나 일치 여부와 관계없는 모든 기존 장치 노드입니다.]{#udev-all-existing explanation="다시 불러오기만으로 현재 모든 장치가 즉시 재평가된다고 보장할 수 없습니다."}
:::

[리눅스 하드웨어 장치 살펴보기](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)에서 제어된 환경을 사용해 `udevadm` 속성, sysfs 경로 및 `/dev` 링크를 연결해 보십시오.

## 요약

이제 커널 이벤트와 사용자 공간 장치 정책 사이에서 udev의 위치를 설명할 수 있습니다.

1. uevent와 sysfs 속성을 udev 규칙 일치와 연결합니다.
2. 공급업체, 런타임 및 로컬 규칙 위치를 구분합니다.
3. `udevadm`으로 속성과 이벤트 흐름을 검사합니다.
4. 좁고 테스트된 범위에서만 규칙을 다시 불러오고 트리거합니다.
