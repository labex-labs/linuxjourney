---
lesson_id: "kernel-location"
course_id: "kernel"
lang: "ko"
order_index: 5
title: "커널 위치"
description: "배포판이 커널 이미지, initramfs 파일, 설정, 심볼 및 버전별 모듈을 저장하는 위치를 알아봅니다."
meta_title: "커널 위치 - 커널"
meta_description: "리눅스에서 커널이 저장되는 위치를 알아봅니다. /boot 디렉터리의 vmlinuz, initramfs, 설정 파일 및 버전별 모듈 트리를 설명합니다."
meta_keywords: "리눅스 커널 위치, 커널 저장 위치, vmlinuz, /boot 디렉터리, initramfs, 커널 모듈, Unified Kernel Image"
---

리눅스 배포판은 일반적으로 부팅 가능한 커널 결과물을 `/boot` 아래에 저장하지만 UEFI와 부트 로더 사양 레이아웃에서는 EFI 시스템 파티션 또는 확장 부트 파티션의 결과물을 `/boot`, `/boot/efi` 또는 `/efi` 같은 경로에 마운트할 수도 있습니다. 하나의 범용 경로를 가정하지 말고 마운트와 로더 설정을 검사하십시오.

## `/boot` 아래의 버전별 파일

전통적인 배포판 레이아웃에는 다음 파일이 있을 수 있습니다.

- `vmlinuz-KERNEL_RELEASE`: 부팅 가능한 리눅스 커널 이미지
- `initrd.img-KERNEL_RELEASE` 또는 `initramfs-KERNEL_RELEASE.img`: 초기 사용자 공간 이미지
- `config-KERNEL_RELEASE`: 해당 패키지 커널 빌드에 사용된 설정
- `System.map-KERNEL_RELEASE`: 커널 빌드의 심볼 주소 맵

이름은 배포판마다 다릅니다. 최신 배포판의 `initrd` 이름 파일에도 initramfs 아카이브가 들어 있는 경우가 많습니다. `vmlinuz`라는 이름만으로 정확한 내부 압축 방식이나 플랫폼 부팅 형식을 알 수 없으므로 배포판 도구로 검사하십시오.

:::single-choice{#kernel-location-vmlinuz} 버전이 붙은 `vmlinuz-*` 파일에는 일반적으로 무엇이 들어 있습니까?

::option[부팅 가능한 리눅스 커널 이미지입니다.]{#kernel-location-kernel-image .correct explanation="부트 로더나 펌웨어가 이 아키텍처별 커널 결과물을 불러옵니다."}
::option[설치된 모든 커널의 모든 로드 가능 모듈입니다.]{#kernel-location-all-modules explanation="모듈은 릴리스별 모듈 트리에 따로 저장됩니다."}
::option[이전 부팅에서 사용자의 셸 기록입니다.]{#kernel-location-shell-history explanation="부팅 커널 이미지에는 개인 명령 기록이 들어 있지 않습니다."}
:::

## 초기 RAM 파일 시스템과 빌드 메타데이터

initramfs에는 일치하는 커널 및 루트 저장 장치 설계에 필요한 초기 모듈과 도구가 들어 있어야 합니다. 파일 이름이 맞는 것만으로는 충분하지 않습니다. 오래됐거나 생성에 실패한 파일은 부팅 항목을 사용할 수 없게 만들 수 있습니다.

`config-*`는 어떤 기능이 내장되거나 모듈로 빌드되거나 제외되었는지 설명하는 데 도움을 줍니다. `System.map-*`은 심볼화와 디버깅에 도움을 줄 수 있지만 주소 무작위화, 분리된 디버그 정보 및 배포판 도구에 따라 사용 방식이 달라집니다. 이 파일들은 지원 결과물이며 대체 커널이 아닙니다.

:::single-choice{#kernel-location-initramfs-match} initramfs가 특정 커널 릴리스 및 시스템 설정에 연결되는 이유는 무엇입니까?

::option[마운트된 모든 파일 시스템의 영구 내용을 저장하기 때문입니다.]{#kernel-location-all-filesystems explanation="initramfs는 작은 초기 부팅 환경이며 전체 시스템 백업이 아닙니다."}
::option[부팅할 때마다 사용자에게 새 UID를 배정하기 때문입니다.]{#kernel-location-user-ids explanation="계정 식별 정보 관리는 일반적인 initramfs 역할의 범위 밖입니다."}
::option[해당 부팅 경로에 필요한 초기 모듈과 도구를 담기 때문입니다.]{#kernel-location-early-modules .correct explanation="모듈 ABI와 필요한 저장 장치 구성 요소가 선택된 커널과 맞아야 합니다."}
:::

## 버전별 커널 모듈

실행 중인 릴리스의 로드 가능 모듈은 일반적으로 다음 경로 아래에 있습니다.

```bash
$ printf '/lib/modules/%s\n' "$(uname -r)"
```

병합 파일 시스템 레이아웃에서는 `/usr/lib/modules/KERNEL_RELEASE`로 해석될 수 있습니다. 설치된 각 커널에는 호환되는 모듈 트리와 의존성 인덱스가 필요합니다. `modprobe`는 디스크 전체에서 임의의 `.ko` 파일을 찾지 않고 릴리스별 메타데이터를 사용합니다.

:::single-choice{#kernel-location-module-tree} 실행 중인 커널 릴리스의 모듈이 일반적으로 들어 있는 디렉터리는 무엇입니까?

::option[`/home/modules/current/`]{#kernel-location-home-modules explanation="사용자 홈 디렉터리는 표준 시스템 모듈 트리가 아닙니다."}
::option[`/lib/modules/$(uname -r)/`]{#kernel-location-lib-modules .correct explanation="릴리스 구성 요소는 설치된 각 커널의 모듈 ABI와 의존성 데이터를 분리합니다."}
::option[`/proc/modules/files/`]{#kernel-location-proc-files explanation="`/proc/modules`는 로드된 모듈을 보고하며 모듈 바이너리 디렉터리가 아닙니다."}
:::

## 통합 커널 이미지와 펌웨어 경로

통합 커널 이미지(UKI)는 커널, initrd, 명령줄 및 메타데이터를 하나로 묶을 수 있는 서명된 EFI 실행 파일입니다. UKI는 별도의 `vmlinuz`와 initramfs 파일이 아니라 EFI가 접근할 수 있는 부팅 위치에 저장되는 경우가 많습니다.

따라서 전통적인 `/boot` 레이아웃이 비어 보인다고 해서 커널이 설치되지 않았다는 뜻은 아닙니다. `findmnt`, 패키지 데이터베이스, 부트 관리자 도구 및 로더 설정으로 활성 결과물을 매핑하십시오.

:::single-choice{#kernel-location-uki} 통합 커널 이미지가 결합할 수 있는 것은 무엇입니까?

::option[모든 사용자 홈 디렉터리를 GPT 헤더에 결합합니다.]{#kernel-location-uki-homes explanation="UKI는 부팅 실행 파일이며 사용자 데이터 컨테이너나 파티션 테이블이 아닙니다."}
::option[설치된 모든 패키지를 셸 스크립트 하나로 결합합니다.]{#kernel-location-uki-packages explanation="전체 운영체제 저장소가 아니라 부팅 구성 요소를 패키징합니다."}
::option[커널, initrd, 명령줄 및 메타데이터를 EFI 실행 파일로 결합합니다.]{#kernel-location-uki-components .correct explanation="결합된 결과물은 서명된 UEFI 부팅 작업 흐름에 참여할 수 있습니다."}
:::

## 안전하게 공간 관리하기

부트 파일 시스템이 가득 찼다면 먼저 마운트된 부트 경로를 매핑하고 각 결과물을 소유한 패키지를 조회하십시오. 패키지 관리자의 커널 정리 작업 흐름을 사용하고, 실행 중인 커널과 정상 작동이 확인된 대체 커널을 보존하며, 부팅 항목을 다시 생성하거나 검사한 뒤 여유 공간을 검증합니다.

오래됐다는 이유만으로 `vmlinuz`, initramfs, UKI 또는 모듈 트리를 직접 삭제하지 마십시오. 현재 실행 중이지 않더라도 파일 하나가 부팅 가능한 유일한 복구 항목일 수 있습니다.

## 요약

이제 커널 패키지를 부팅 및 모듈 결과물과 연결할 수 있습니다.

1. 실제 `/boot` 및 EFI 관련 마운트를 검사합니다.
2. 커널 이미지, initramfs, 설정 및 심볼 맵을 구분합니다.
3. 모듈 트리를 정확한 커널 릴리스와 일치시킵니다.
4. 통합 커널 이미지와 배포판별 레이아웃을 고려합니다.
5. 검증된 패키지 및 대체 커널 계획을 통해서만 부트 공간을 회수합니다.
