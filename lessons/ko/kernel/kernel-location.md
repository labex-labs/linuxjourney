---
lang: "ko"
title: "커널 위치"
meta_description: "/boot 디렉토리에서 Linux 커널의 위치를 알아보고, vmlinuz, initrd, System.map 을 이해합니다. 커널 파일을 탐색하고 공간을 효과적으로 관리합니다."
meta_keywords: "Linux 커널, /boot 디렉토리, vmlinuz, initrd, System.map, Linux 초보자, 커널 튜토리얼, Linux 가이드"
---

## Lesson Content

새로운 커널을 설치하면 어떻게 될까요? 실제로는 몇 가지 파일이 시스템에 추가됩니다. 이 파일들은 일반적으로 `/boot` 디렉토리에 추가됩니다.

여러 커널 버전에 대한 다양한 파일을 볼 수 있습니다:

- `vmlinuz` - 실제 Linux 커널입니다.
- `initrd` - 이전에 논의했듯이, `initrd`는 커널을 로드하기 전에 사용되는 임시 파일 시스템으로 사용됩니다.
- `System.map` - 심볼 조회 테이블입니다.
- `config` - 커널 구성 설정입니다. 직접 커널을 컴파일하는 경우, 로드할 수 있는 모듈을 설정할 수 있습니다.

`/boot` 디렉토리의 공간이 부족하면, 항상 이 파일들의 이전 버전을 삭제하거나 패키지 관리자를 사용할 수 있습니다. 하지만 이 디렉토리에서 유지보수를 할 때는 주의해야 하며, 현재 사용 중인 커널을 실수로 삭제하지 않도록 조심해야 합니다.

## Exercise

Go into your boot directory and see what files are in there.

## Quiz Question

`/boot`에 있는 커널 이미지는 무엇이라고 불립니까?

## Quiz Answer

vmlinuz
