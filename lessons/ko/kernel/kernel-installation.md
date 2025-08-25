---
index: 4
lang: "ko"
title: "커널 설치"
meta_title: "커널 설치 - 커널"
meta_description: "Linux 커널을 설치하고 관리하는 방법을 배우십시오. 커널 버전, `uname -r` 및 apt 명령을 알아보십시오. Linux 커널 여정을 시작하십시오!"
meta_keywords: "Linux 커널, 커널 설치, uname -r, apt dist-upgrade, 커널 관리, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

자, 이제 지루한 것들은 다 치웠으니, 실제로 커널을 설치하고 수정하는 방법에 대해 이야기해 봅시다. 시스템에 여러 커널을 설치할 수 있습니다. 부팅 프로세스에 대한 수업에서 기억하시나요? GRUB 메뉴에서 부팅할 커널을 선택할 수 있습니다.

시스템에 설치된 커널 버전을 확인하려면 다음 명령을 사용하십시오:

```bash
$ uname -r
3.19.0-43-generic
```

`uname` 명령은 시스템 정보를 출력합니다. `-r` 옵션은 커널 릴리스 버전을 출력합니다.

Linux 커널은 다양한 방법으로 설치할 수 있습니다: 소스 패키지를 다운로드하여 소스에서 컴파일하거나, 패키지 관리 도구를 사용하여 설치할 수 있습니다.

```bash
sudo apt install linux-generic-lts-vivid
```

그리고 설치한 커널로 재부팅하기만 하면 됩니다. 간단하죠? 어느 정도는요. `linux-headers`, `linux-image-generic` 등 다른 Linux 패키지도 설치해야 합니다. 버전 번호를 지정할 수도 있으므로 위 명령은 다음과 같이 보일 수 있습니다: **`sudo apt install 3.19.0-43-generic`**

또는 업데이트된 커널 버전만 원한다면 `dist-upgrade`를 사용하십시오. 이 명령은 시스템의 모든 패키지를 업그레이드합니다:

```bash
sudo apt dist-upgrade
```

다양한 커널 버전이 있습니다. 일부는 LTS(Long Term Support) 로 사용되고, 일부는 최신 버전입니다. 커널 버전 간의 호환성은 매우 다를 수 있으므로 다른 커널을 시도해 볼 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 커널 관리 및 관련 시스템 관리 작업에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 GRUB2 부팅 메뉴 사용자 정의](https://labex.io/ko/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - 여러 커널 버전을 관리하고 부팅할 커널을 선택할 때 필수적인 GRUB2 부팅 메뉴 수정 연습.
2. **[Linux 에서 커널 모듈 관리](https://labex.io/ko/labs/comptia-manage-kernel-modules-in-linux-590865)** - 커널 관리의 기본이자 하드웨어가 시스템과 상호 작용하는 방식을 이해하는 데 중요한 커널 모듈을 나열, 검사, 로드 및 언로드하는 방법을 배웁니다.
3. **[Linux 에 소프트웨어 설치](https://labex.io/ko/labs/linux-software-installation-on-linux-18005)** - 패키지 관리자를 포함하여 소프트웨어를 설치하고 관리하는 다양한 방법에 대한 실질적인 경험을 얻습니다. 이는 커널을 설치하고 업데이트하는 일반적인 방법입니다.

이러한 랩은 커널 관리, 부팅 프로세스 및 패키지 관리 개념을 실제 시나리오에 적용하여 시스템 관리 능력을 향상시키는 데 도움이 될 것입니다.

## Quiz Question

시스템의 커널 버전을 어떻게 확인합니까?

## Quiz Answer

uname -r
