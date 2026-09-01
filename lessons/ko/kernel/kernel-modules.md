---
lesson_id: "kernel-modules"
course_id: "kernel"
lang: "ko"
order_index: 6
title: "커널 모듈"
description: "릴리스별 리눅스 커널 모듈을 검사하고 불러오며 설정하고 안전하게 제거하는 방법을 알아봅니다."
meta_title: "커널 모듈 - 커널"
meta_description: "리눅스 커널 모듈과 커널 기능을 확장하는 방식을 알아봅니다. lsmod와 modprobe로 모듈을 나열하고 불러오며 제거하는 방법을 설명합니다."
meta_keywords: "리눅스 커널 모듈, modprobe, lsmod, modinfo, 커널 관리, 모듈 로드, 모듈 제거"
---

로드 가능 커널 모듈은 실행 중인 커널에 드라이버, 파일 시스템, 네트워크 기능 또는 다른 하위 시스템을 추가할 수 있는 특권 코드입니다. 모든 선택 기능을 하나의 커널 이미지에 내장하지 않아도 되지만 모듈 하나를 불러오면 신뢰해야 하는 커널 공격 표면이 넓어집니다.

## 모듈 나열 및 검사

현재 로드된 모듈을 나열합니다.

```bash
$ lsmod
```

출력은 `/proc/modules` 같은 커널 상태에서 파생되며 모듈 이름, 크기 및 사용 수 또는 의존성을 포함합니다. 사용 수가 0처럼 보여도 안전하게 제거할 수 있다는 완전한 증거는 아닙니다. 드라이버가 활성 장치를 소유하거나 하위 시스템 상태에 참여할 수 있습니다.

실행 중인 커널에서 사용할 수 있는 모듈을 검사합니다.

```bash
$ modinfo MODULE_NAME
```

`modinfo`는 파일 이름, 별칭, 매개변수, 라이선스, 설명 및 서명 정보를 보여 줄 수 있습니다. 메타데이터는 설명일 뿐 모듈이 신뢰할 수 있거나 작업 부하와 호환된다는 증거로 취급하지 마십시오.

:::single-choice{#kernel-modules-lsmod-purpose} `lsmod`가 표시하는 것은 무엇입니까?

::option[원격 저장소에서 사용 가능한 모든 모듈 패키지입니다.]{#kernel-modules-repository-list explanation="저장소 목록에는 패키지 관리자 조회가 필요합니다."}
::option[커널 이미지에 직접 컴파일된 드라이버만 표시합니다.]{#kernel-modules-builtins explanation="내장 기능은 로드 가능 모듈이 아니며 일반적으로 lsmod에 나타나지 않습니다."}
::option[현재 실행 중인 커널에 로드된 모듈입니다.]{#kernel-modules-loaded-list .correct explanation="목록은 실시간 모듈 상태와 의존성 또는 사용 정보를 반영합니다."}
:::

## `modprobe`로 불러오기

이름으로 모듈을 불러옵니다.

```bash
$ sudo modprobe MODULE_NAME
```

`modprobe`는 `/lib/modules/$(uname -r)/` 아래에서 실행 중인 커널의 의존성 인덱스, 별칭 및 설정을 참조합니다. 필요한 의존성을 불러오고 설정된 매개변수를 전달합니다. 반면 `insmod`는 지정한 모듈 파일 하나를 직접 삽입하며 같은 의존성 해결 작업 흐름을 제공하지 않습니다.

불러오기 전에 모듈 출처, 서명 정책, 커널 릴리스 호환성, 매개변수, 예상 하드웨어 바인딩 및 롤백 방법을 확인하십시오. 보안 부팅이나 커널 잠금은 서명되지 않은 모듈을 거부할 수 있습니다. 호환되지 않는 코드를 강제로 불러오면 충돌이나 시스템 손상이 발생할 수 있습니다.

:::single-choice{#kernel-modules-modprobe-dependencies} 직접 `insmod`를 사용하는 것보다 일반적으로 `modprobe`가 선호되는 이유는 무엇입니까?

::option[모듈을 완전히 비특권 사용자 공간에서 실행하기 때문입니다.]{#kernel-modules-modprobe-userspace explanation="삽입된 모듈은 특권 커널 코드로 실행됩니다."}
::option[모든 서드파티 모듈이 서명되고 안전함을 보장하기 때문입니다.]{#kernel-modules-modprobe-guarantee explanation="적용 여부는 정책에 따라 달라지고 유효한 서명이 결함 없음을 증명하지 않습니다."}
::option[모듈 별칭, 의존성 및 설정을 해결하기 때문입니다.]{#kernel-modules-modprobe-resolves .correct explanation="modprobe는 정확한 실행 릴리스의 색인된 모듈 트리를 사용합니다."}
:::

## 모듈 매개변수와 부팅 시 로드

영구적인 매개변수와 별칭 정책은 `/etc/modprobe.d/` 아래의 `.conf` 파일에 둡니다.

```text
options example_module mode=careful
```

이 줄은 modprobe가 모듈을 불러오는 방식에 영향을 주지만 그 자체로 부팅 시 로드를 요청하지는 않습니다. 단순한 부팅 시 로드 목록은 일반적으로 `/etc/modules-load.d/` 아래에 둡니다.

```text
example_module
```

하드웨어 별칭은 명시적인 목록 없이 자동 로드를 트리거하는 경우가 많습니다. 초기 부팅 안에서 필요한 모듈은 설정 변경 후 배포판이 문서화한 절차로 initramfs를 갱신하십시오.

:::single-choice{#kernel-modules-options-versus-load} `/etc/modprobe.d/`의 `options` 줄은 무엇을 합니까?

::option[그 줄만으로 모듈이 부팅할 때마다 로드됨을 보장합니다.]{#kernel-modules-options-autoload explanation="부팅 시 로드 요청에는 modules-load 설정이나 장치 별칭 같은 다른 메커니즘을 사용합니다."}
::option[지정한 모듈이 로드될 때 사용할 매개변수를 설정합니다.]{#kernel-modules-options-parameters .correct explanation="modprobe는 삽입 중 설정된 키-값 인수를 적용합니다."}
::option[설치된 모든 커널 릴리스용 모듈을 컴파일합니다.]{#kernel-modules-options-compiles explanation="설정은 바이너리 모듈을 빌드하지 않습니다."}
:::

## 블랙리스트와 한계

modprobe 설정에는 다음 줄을 넣을 수 있습니다.

```text
blacklist example_module
```

블랙리스트는 일반적으로 모듈 별칭을 통한 자동 로드를 억제합니다. 이미 로드된 모듈을 내리거나 initramfs에서 제거하지 않으며, 정확한 이름을 통한 명시적 로드나 의존성으로서의 로드를 반드시 막는 것도 아닙니다. 보안 강화에는 위협별 모듈 가용성, 서명 적용, initramfs 내용, 부팅 매개변수 및 정책의 조합이 필요합니다.

:::single-choice{#kernel-modules-blacklist-effect} 기본 modprobe `blacklist` 줄이 주로 억제하는 것은 무엇입니까?

::option[모듈 별칭을 통한 자동 로드입니다.]{#kernel-modules-blacklist-aliases .correct explanation="이 지시문은 코드가 이미 로드되었거나 로드될 수 있는 모든 경로를 보편적으로 금지하지 않습니다."}
::option[이름이 비슷한 모든 사용자 공간 프로그램의 실행입니다.]{#kernel-modules-blacklist-user-programs explanation="modprobe 설정은 커널 모듈 해석에 적용됩니다."}
::option[커널 이미지에 컴파일된 모든 코드입니다.]{#kernel-modules-blacklist-builtins explanation="내장 기능은 모듈처럼 내리거나 차단할 수 없습니다."}
:::

## 안전하게 모듈 제거하기

다음 명령으로 제거를 요청합니다.

```bash
$ sudo modprobe -r MODULE_NAME
```

modprobe는 적절한 경우 더 이상 사용되지 않는 의존성도 제거할 수 있습니다. 일반 참조 추적에서 모듈이 사용 중이면 커널이 제거를 거부하지만 이를 유일한 안전 검사로 의존하지 마십시오. 활성 하드웨어를 지원하는 코드를 제거하기 전에 서비스를 중지하고, 파일 시스템을 마운트 해제하고, 장치를 분리하고, 네트워크 작업을 정지하며, 다른 드라이버나 복구 경로를 확인합니다.

보존해야 하는 시스템에서 모듈을 강제로 내리지 마십시오. 제거 버그나 남은 활동 때문에 커널이 충돌하거나 데이터가 손상될 수 있습니다.

:::single-choice{#kernel-modules-remove-command} 이름으로 모듈의 의존성을 고려한 제거를 요청하는 명령은 무엇입니까?

::option[`lsmod -r MODULE_NAME`]{#kernel-modules-lsmod-remove explanation="lsmod는 읽기 전용 목록 도구이며 제거 역할이 없습니다."}
::option[`uname -r MODULE_NAME`]{#kernel-modules-uname-remove explanation="uname은 커널 정보를 보고하며 모듈을 관리하지 않습니다."}
::option[`modprobe -r MODULE_NAME`]{#kernel-modules-modprobe-remove .correct explanation="제거 모드는 요청한 모듈 주변의 색인된 의존성 관계를 고려합니다."}
:::

[리눅스 커널 모듈 관리하기](https://labex.io/labs/comptia-manage-kernel-modules-in-linux-590865)에서 실습이 안전하다고 지정한 모듈로 연습하십시오.

## 요약

이제 커널 수준의 위험을 고려하면서 모듈을 관리할 수 있습니다.

1. 실시간 상태에는 `lsmod`를, 사용 가능한 메타데이터에는 `modinfo`를 사용합니다.
2. 별칭 및 의존성을 고려한 로드에는 `modprobe`를 사용합니다.
3. modprobe 매개변수와 부팅 시 로드 요청을 구분합니다.
4. 블랙리스트를 절대적 차단이 아니라 제한적인 정책으로 취급합니다.
5. `modprobe -r` 전에 모든 사용자를 정지합니다.
