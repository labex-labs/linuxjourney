---
lesson_id: "boot-process-bootloader"
course_id: "boot-system"
lang: "ko"
order_index: 3
title: "부팅 과정: 부트 로더"
description: "부트 로더가 리눅스 부팅 결과물을 선택하고 커널 명령줄을 구성한 뒤 제어권을 넘기는 방법을 알아봅니다."
meta_title: "부팅 과정: 부트 로더 - 시스템 부팅"
meta_description: "리눅스 부트 로더의 역할을 알아봅니다. GRUB이 커널, initramfs 및 root 같은 커널 매개변수를 사용해 시스템을 시작하는 방법을 설명합니다."
meta_keywords: "리눅스 부트 로더, GRUB, 리눅스 부팅, 커널 매개변수, initrd, initramfs, 루트 파일 시스템"
---

부트 로더는 펌웨어 검색과 커널 실행을 연결합니다. 리눅스 PC에서는 GRUB이 흔하지만 systemd-boot, U-Boot, EFI 스텁 커널을 직접 불러오는 펌웨어 및 다른 설계가 이 역할의 서로 다른 부분을 구현합니다.

## 부팅 결과물 선택하기

로더 항목은 다음을 식별할 수 있습니다.

- 리눅스 커널 이미지
- 선택적인 initramfs 또는 레거시 initrd 이미지
- 커널 명령줄
- 플랫폼별 메타데이터 또는 다른 운영체제의 로더

GRUB은 여러 커널과 복구 항목을 표시할 수 있습니다. 대체 커널은 그에 맞는 모듈과 initramfs가 남아 있고 테스트된 경우에만 유용합니다. 로더는 지원되는 저장 장치 및 파일 시스템 모듈을 통해 파일을 읽으며 아직 실행되지 않은 리눅스 VFS에 의존하지 않습니다.

:::single-choice{#bootloader-primary-handoff}
리눅스 부트 로더는 일반적으로 어디로 제어권을 넘깁니까?

::option[모든 서비스가 실행 중인 대화형 사용자 셸입니다.]{#bootloader-user-shell explanation="사용자 공간 셸은 커널과 init 시스템이 시작된 뒤에야 나타납니다."}
::option[필수 부팅 결과물을 불러온 뒤 선택한 커널 이미지입니다.]{#bootloader-selected-kernel .correct explanation="로더는 커널 진입점을 실행하기 전에 커널, 매개변수 및 흔히 initramfs를 준비합니다."}
::option[의존성을 해결하는 파일 시스템 패키지 관리자입니다.]{#bootloader-package-manager explanation="패키지 관리는 부팅에서 다음 프로세서 제어 단계가 아닙니다."}
:::

## 커널 명령줄 매개변수

로더는 커널과 초기 사용자 공간이 해석하는 텍스트 명령줄을 전달합니다. 일반적인 예는 다음과 같습니다.

- `root=...`: 의도한 루트 파일 시스템 또는 초기 사용자 공간 소스 사양을 식별
- `ro` 또는 `rw`: 초기 루트 마운트 모드를 요청
- `quiet`: 커널 콘솔 메시지를 줄임
- `init=...`: 특수 복구를 위해 다른 첫 사용자 공간 프로그램을 요청
- 배포판별 initramfs 도구가 해석하는 `rd.*` 매개변수

`initrd`는 일반적으로 이미지 이름을 지정하는 로더 지시문이며 범용 커널 매개변수가 아닙니다. 일부 GRUB 설정이 만든 명령줄에 `BOOT_IMAGE=`가 나타날 수 있지만 이것이 커널을 불러오는 메커니즘은 아닙니다.

현재 부팅에 사용된 명령줄을 검사합니다.

```bash
$ cat /proc/cmdline
```

:::single-choice{#bootloader-root-parameter}
`root=` 커널 명령줄 매개변수의 목적은 무엇입니까?

::option[부팅 과정이 최종적으로 사용할 루트 파일 시스템을 식별합니다.]{#bootloader-root-filesystem .correct explanation="커널 또는 initramfs는 실제 루트를 찾고 구성하는 과정에서 이 값을 해석합니다."}
::option[root 계정의 로그인 암호를 설정합니다.]{#bootloader-root-password explanation="인증 비밀 정보는 일반 커널 명령줄 텍스트로 전달해서는 안 됩니다."}
::option[PID 1의 이름을 `root`로 바꿉니다.]{#bootloader-root-pid explanation="프로세스 이름은 이 저장 장치 매개변수와 관련이 없습니다."}
:::

:::single-choice{#bootloader-quiet-parameter}
`quiet` 매개변수는 일반적으로 무엇을 요청합니까?

::option[마운트된 모든 파일 시스템에 읽기 전용 접근을 적용합니다.]{#bootloader-quiet-readonly explanation="초기 루트 쓰기 정책에는 `quiet`가 아니라 `ro` 같은 매개변수를 사용합니다."}
::option[부팅 중 출력되는 커널 메시지를 줄입니다.]{#bootloader-quiet-console .correct explanation="여러 정보 메시지를 억제하지만 모든 부팅 구성 요소가 완전히 조용해진다고 보장하지 않습니다."}
::option[모든 하드웨어 냉각 팬을 비활성화합니다.]{#bootloader-quiet-fans explanation="이 매개변수는 하드웨어 소음이 아니라 메시지 출력량과 관련됩니다."}
:::

## 임시 편집과 복구

GRUB은 일반적으로 권한이 있는 콘솔 사용자가 메뉴에 표시된 편집 키 등을 이용해 한 번의 부팅에 사용할 항목을 편집할 수 있게 합니다. `quiet`를 제거하거나, 복구 매개변수를 선택하거나, 잘못된 루트 식별자를 고칠 때 유용합니다. 특히 보안 부팅과 암호로 보호된 GRUB 설정에서는 인터페이스와 권한 부여 방식이 다릅니다.

명령줄 매개변수의 민감한 텍스트는 `/proc/cmdline`, 부팅 로그 및 크래시 보고서에 노출될 수 있습니다. 보안을 약화시키거나 시스템을 부팅 불가 상태로 만들 수도 있습니다. 비밀 정보를 넣지 말고 정상 작동이 확인된 항목과 콘솔 복구 경로를 보존하십시오.

:::single-choice{#bootloader-temporary-edit}
한 번의 부팅을 위해 GRUB 메뉴 항목을 대화형으로 편집할 때의 일반적인 특징은 무엇입니까?

::option[설치된 모든 커널 이미지를 자동으로 다시 씁니다.]{#bootloader-rewrites-kernels explanation="명령 텍스트를 변경해도 커널 바이너리는 수정되지 않습니다."}
::option[모든 디스크에서 펌웨어 검증을 영구 비활성화합니다.]{#bootloader-disables-firmware explanation="펌웨어 정책은 별개이며 항목 하나의 편집으로 보편적으로 바뀌지 않습니다."}
::option[별도로 설정에 저장하지 않으면 해당 부팅에만 변경이 적용됩니다.]{#bootloader-one-boot-change .correct explanation="메뉴 편집은 일반적으로 영구 원본 설정이 아니라 메모리 내 항목을 변경합니다."}
:::

## 영구 GRUB 설정

배포판은 일반적으로 템플릿, 기본값, 스크립트 및 검색된 커널에서 최종 GRUB 설정을 생성합니다. 배포판에서 그 작업 흐름을 명시적으로 문서화하지 않았다면 생성된 `grub.cfg`를 직접 편집하지 마십시오. 다시 생성하면 변경을 덮어쓸 수 있습니다.

범위가 좁은 원본 변경을 수행하고 배포판이 문서화한 재생성 명령을 실행하며 출력을 검사하십시오. 정상 작동이 확인된 이전 항목과 부팅 가능한 복구 미디어를 유지한 상태에서 테스트합니다. 명령과 출력 경로는 데비안, 페도라, UEFI 및 BIOS 설치에 따라 다릅니다.

:::single-choice{#bootloader-generated-config}
생성된 `grub.cfg`를 직접 편집하는 방식이 일반적으로 신뢰하기 어려운 이유는 무엇입니까?

::option[파일에 읽을 수 있는 텍스트가 절대 포함되지 않기 때문입니다.]{#bootloader-config-binary explanation="GRUB 설정은 텍스트이지만 생성되는 파일이라는 소유 관계가 중요합니다."}
::option[GRUB이 각 사용자의 홈 디렉터리 안의 파일만 읽기 때문입니다.]{#bootloader-grub-home explanation="부팅 설정은 시스템 수준이며 사용자 홈 세션보다 먼저 사용할 수 있어야 합니다."}
::option[나중에 재생성하면 수동 변경이 덮어써질 수 있기 때문입니다.]{#bootloader-regeneration-overwrites .correct explanation="영구 설정은 일반적으로 배포판의 설정 원본과 생성 작업 흐름에 둡니다."}
:::

[GRUB2 부팅 메뉴 사용자 지정하기](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)는 복구 가능한 실습 환경에서만 사용하십시오.

## 요약

이제 로더 지시문과 커널 명령줄 매개변수를 구분할 수 있습니다.

1. 커널, initramfs, 명령줄 및 대체 항목을 식별합니다.
2. `root=`, `ro` 및 `quiet`를 실제 역할에 맞게 사용합니다.
3. `/proc/cmdline`에서 실행 중인 부팅의 매개변수를 검사합니다.
4. 대화형 편집을 임시적이고 보안에 민감한 작업으로 취급합니다.
5. 배포판 작업 흐름을 통해 영구 생성 설정을 변경합니다.
