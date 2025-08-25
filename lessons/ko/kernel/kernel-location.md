---
index: 5
lang: "ko"
title: "커널 위치"
meta_title: "커널 위치 - 커널"
meta_description: "`/boot` 디렉토리의 Linux 커널 위치에 대해 알아보고, vmlinuz, initrd, System.map 을 이해합니다. 커널 파일을 탐색하고 공간을 효과적으로 관리합니다."
meta_keywords: "Linux 커널, /boot 디렉토리, vmlinuz, initrd, System.map, Linux 초보자, 커널 튜토리얼, Linux 가이드"
---

## Lesson Content

새로운 커널을 설치하면 어떻게 될까요? 시스템에 몇 개의 파일이 추가됩니다. 이 파일들은 일반적으로 `/boot` 디렉토리에 추가됩니다.

다른 커널 버전에 대한 여러 파일을 볼 수 있습니다:

- `vmlinuz` - 실제 Linux 커널입니다.
- `initrd` - 이전에 논의했듯이, `initrd`는 커널을 로드하기 전에 사용되는 임시 파일 시스템으로 사용됩니다.
- `System.map` - 심볼릭 조회 테이블입니다.
- `config` - 커널 구성 설정입니다. 자체 커널을 컴파일하는 경우 로드할 수 있는 모듈을 설정할 수 있습니다.

`/boot` 디렉토리의 공간이 부족하면 언제든지 이러한 파일의 이전 버전을 삭제하거나 패키지 관리자를 사용할 수 있습니다. 하지만 이 디렉토리에서 유지보수를 할 때는 주의해야 하며, 현재 사용 중인 커널을 실수로 삭제하지 않도록 조심해야 합니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 부팅 프로세스 및 커널 관리에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 에서 GRUB2 부팅 메뉴 사용자 지정](https://labex.io/ko/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Linux 시스템이 부팅되고 커널 버전을 선택하는 방식에 직접적인 영향을 미치는 GRUB2 구성을 수정하는 연습을 합니다. 이 실습은 `/boot` 디렉토리에서 논의된 파일의 실제적인 의미를 이해하는 데 도움이 될 것입니다.

이 실습은 실제 시나리오에 개념을 적용하고 Linux 커널 및 부팅 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

`/boot`에 있는 커널 이미지는 무엇이라고 불립니까?

## Quiz Answer

vmlinuz
