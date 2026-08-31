---
lesson_id: "kernel-installation"
course_id: "kernel"
lang: "ko"
order_index: 4
title: "커널 설치"
description: "검증된 대체 커널을 유지하면서 배포판 커널을 설치, 부팅 및 검증하는 방법을 알아봅니다."
meta_title: "커널 설치 - 커널"
meta_description: "리눅스 커널을 설치하고 관리하는 방법을 알아봅니다. uname -r로 실행 중인 버전을 확인하고 배포판 패키지로 안전하게 업데이트하는 절차를 설명합니다."
meta_keywords: "리눅스 커널, 커널 설치, uname -r, 커널 관리, 리눅스 튜토리얼, 커널 업데이트, initramfs"
---

배포판은 커널을 모듈, initramfs 통합, 부트 로더 업데이트, 서명 및 지원 정책과 함께 패키징합니다. 커스텀 커널을 의도적으로 개발하거나 테스트하고 시스템을 복구할 수 있는 경우가 아니라면 이 관리형 작업 흐름을 사용하십시오.

## 실행 중인 커널과 설치된 커널

현재 실행 중인 커널의 릴리스를 표시합니다.

```bash
$ uname -r
6.8.0-00-generic
```

이 명령은 설치된 모든 커널을 나열하지 않으며 새 패키지를 설치한 직후에도 값이 바뀌지 않습니다. `uname -r`에 새 이미지가 표시되려면 시스템이 그 커널로 부팅해야 합니다. 배포판 고유 도구로 설치된 패키지와 부팅 항목을 조회하십시오.

:::single-choice{#kernel-installation-uname-release}
`uname -r`이 표시하는 것은 무엇입니까?

::option[현재 실행 중인 커널의 릴리스 문자열입니다.]{#kernel-installation-running-release .correct explanation="디스크에 저장된 최신 이미지만이 아니라 실시간 커널 상태를 보고합니다."}
::option[모든 저장소에서 사용 가능한 모든 커널 패키지입니다.]{#kernel-installation-all-packages explanation="저장소 목록은 패키지 관리자가 담당합니다."}
::option[연결된 모든 장치의 펌웨어 버전입니다.]{#kernel-installation-device-firmware explanation="커널 릴리스와 장치 펌웨어 목록은 서로 다른 데이터입니다."}
:::

## 배포판 추적 패키지 우선 사용하기

향후 보안 업데이트가 계속 도착하도록 배포판에서 지원하는 커널 추적 또는 메타 패키지를 설치하거나 유지하십시오. 패키지 이름은 릴리스, 아키텍처, 하드웨어 클래스 및 커널 유형에 따라 다릅니다. 예를 들어 우분투는 일반적으로 `linux-generic`을 제공하지만 클라우드, 저지연, HWE, OEM, 실시간 및 아키텍처별 시스템에서는 다른 패키지를 사용합니다.

`uname -r`의 버전 문자열을 그대로 `apt install` 피연산자로 바꾸어 유효하다고 가정하지 마십시오. 설치 전에 현재 배포판 문서를 확인하고 패키지 관리자로 후보를 검사합니다.

:::single-choice{#kernel-installation-meta-package}
지원되는 커널 메타 패키지가 유용한 이유는 무엇입니까?

::option[재부팅이 절대 필요하지 않음을 보장하기 때문입니다.]{#kernel-installation-no-reboot explanation="특수한 라이브 패치 범위를 제외하면 새 커널은 그 커널로 부팅한 뒤에야 활성화됩니다."}
::option[모든 트리 외부 드라이버를 내장 코드로 변환하기 때문입니다.]{#kernel-installation-convert-drivers explanation="외부 모듈에는 여전히 호환되는 빌드와 서명이 필요합니다."}
::option[배포판이 의도한 커널 업데이트 순서를 추적하기 때문입니다.]{#kernel-installation-update-tracking .correct explanation="업데이트가 게시되면 의존성이 시스템을 더 새로운 지원 이미지 및 모듈 패키지로 이동시킵니다."}
:::

## 변경 전 점검

커널 트랜잭션 전에 다음을 수행하십시오.

1. 지원되는 저장소, 패키지 서명, 릴리스 수명 주기 및 의도한 커널 유형을 확인합니다.
2. `/boot` 또는 EFI 시스템 파티션에 충분한 공간이 있는지 확인합니다.
3. 정상 작동이 확인된 설치 커널과 선택 가능한 부팅 항목을 하나 이상 보존합니다.
4. 콘솔, 원격 관리, 복구 미디어, 암호화 복구 및 롤백 접근을 확인합니다.
5. 트리 외부 모듈, 저장 장치 및 네트워크 드라이버, 보안 부팅 서명, 최대 절전 모드 및 가상화 호환성을 검사합니다.

패키지 트랜잭션은 배포판 훅을 통해 일치하는 initramfs를 생성하고 부팅 항목을 갱신해야 합니다. 모든 오류를 읽으십시오. initramfs 또는 로더 생성이 실패했다면 패키지가 설치됨으로 표시되는 것만으로는 충분하지 않습니다.

:::single-choice{#kernel-installation-initramfs-error}
initramfs 생성 오류가 있으면 성공했다고 판단해서는 안 되는 이유는 무엇입니까?

::option[initramfs 생성이 사용자의 셸 암호를 바꾸기 때문입니다.]{#kernel-installation-initramfs-password explanation="부팅 아카이브 작업 흐름은 계정 인증 비밀 정보와 관련이 없습니다."}
::option[새 커널에 루트 저장 장치에 도달할 초기 모듈이나 도구가 없을 수 있기 때문입니다.]{#kernel-installation-missing-early-tools .correct explanation="커널 이미지는 설치됐어도 필요한 초기 사용자 공간 결과물이 없거나 오래되었을 수 있습니다."}
::option[현재 실행 중인 커널이 이미 중지되었다는 뜻이기 때문입니다.]{#kernel-installation-current-stopped explanation="패키지 훅이 실행되는 동안에도 이전 커널은 계속 활성 상태일 수 있습니다."}
:::

## 부팅 및 검증

관계자와 활성 작업 부하를 고려하여 제어된 재부팅을 예약하십시오. 기본 항목이 실패할 때 콘솔에서 이전 항목을 선택할 수 있어야 합니다. 부팅 후 다음을 확인합니다.

```bash
$ uname -r
$ journalctl -k -b
$ systemctl --failed
```

systemd가 아닌 시스템에서는 동등한 도구를 사용하십시오. 저장 장치, 파일 시스템, 네트워킹, 그래픽, 입력, 보안 모듈, 외부 모듈, 컨테이너, 가상 머신 및 애플리케이션 상태를 검증합니다. 로그인 프롬프트만으로는 검증이 완료되지 않습니다.

:::single-choice{#kernel-installation-activation}
새로 설치한 일반 커널 패키지는 언제 실행 중인 커널이 됩니까?

::option[`uname -r`을 입력하는 즉시 활성화됩니다.]{#kernel-installation-uname-activates explanation="uname은 읽기 전용이며 커널을 전환할 수 없습니다."}
::option[시스템이 해당 커널 이미지로 부팅한 뒤입니다.]{#kernel-installation-after-boot .correct explanation="파일을 설치해도 메모리에서 이미 실행 중인 커널은 교체되지 않습니다."}
::option[패키지 아카이브를 다운로드했지만 설치하기 전입니다.]{#kernel-installation-download-activates explanation="다운로드된 아카이브는 실시간 실행에 영향을 주지 않습니다."}
:::

## 이전 커널 제거하기

새 커널이 검증을 통과한 뒤에만 패키지 관리자가 지원하는 정리 작업 흐름을 사용하십시오. 현재 실행 중인 커널, 정상 작동이 확인된 유일한 대체 커널 또는 활성 추적 패키지에 필요한 패키지를 제거하지 마십시오. 정확한 제거 제안과 결과 부팅 항목을 검토합니다.

`/boot`에서 직접 삭제하면 패키지 상태와 로더 상태가 일치하지 않게 됩니다. 이미 공간이 고갈됐다면 임의의 이미지를 삭제하지 말고 파일을 바꾸기 전에 복구 계획을 세우십시오.

:::single-choice{#kernel-installation-old-kernel-removal}
새 커널을 처음 검증하는 동안 어떤 커널을 설치된 상태로 유지해야 합니까?

::option[테스트하지 않은 새 커널만 유지합니다.]{#kernel-installation-only-new explanation="테스트 전에 모든 대체 항목을 제거하면 호환성 문제가 복구 사고로 커집니다."}
::option[부팅 경로 아래의 모든 커널 파일을 제거합니다.]{#kernel-installation-no-kernels explanation="시스템이 리눅스로 부팅하려면 불러올 수 있는 커널 결과물이 필요합니다."}
::option[부트 로더에서 선택할 수 있는 정상 작동이 확인된 대체 커널입니다.]{#kernel-installation-known-good-fallback .correct explanation="새 커널이 하드웨어나 작업 부하에서 실패할 때 대체 항목이 복구 경로를 제공합니다."}
:::

[GRUB2 부팅 메뉴 사용자 지정하기](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) 실습은 여러 부팅 항목을 이해할 수 있는 복구 안전 환경을 제공합니다.

## 요약

이제 커널 업데이트를 부팅 체인 및 호환성 변경으로 취급할 수 있습니다.

1. 실행 중인 릴리스와 설치된 이미지를 구분합니다.
2. 올바른 배포판 패키지를 통해 지원되는 업데이트를 추적합니다.
3. 저장 공간, initramfs, 서명, 모듈 및 복구 접근을 사전 점검합니다.
4. 부팅 후 하드웨어와 애플리케이션 동작을 검증합니다.
5. 새 커널이 입증될 때까지 정상 작동이 확인된 대체 커널을 유지합니다.
