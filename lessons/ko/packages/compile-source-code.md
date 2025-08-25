---
index: 7
lang: "ko"
title: "소스 코드 컴파일"
meta_title: "소스 코드 컴파일 - 패키지"
meta_description: "make, configure, checkinstall 을 사용하여 Linux 에서 소스 코드를 컴파일하는 방법을 배웁니다. 초보자 및 중급 사용자를 위한 빌드 프로세스를 이해합니다."
meta_keywords: "소스 코드 컴파일, make install, checkinstall, Linux 컴파일, build-essential, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

종종 순수한 소스 코드 형태로만 제공되는 잘 알려지지 않은 패키지를 접하게 될 것입니다. 해당 소스 코드 패키지를 컴파일하여 시스템에 설치하려면 몇 가지 명령어를 사용해야 합니다.

가장 먼저, 소스 코드를 컴파일할 수 있는 도구를 설치할 소프트웨어가 필요합니다.

```bash
sudo apt install build-essential
```

설치한 후에는 패키지 파일, 대부분 `.tar.gz` 파일의 내용을 압축 해제합니다.

```bash
tar -xzvf package.tar.gz
```

무엇을 하기 전에 패키지 안에 있는 `README` 또는 `INSTALL` 파일을 살펴보세요. 때로는 특정 설치 지침이 있을 수 있습니다.

개발자가 사용한 컴파일 방법에 따라 `cmake` 또는 다른 명령어를 사용해야 할 수 있습니다.

하지만 가장 일반적으로는 기본적인 `make` 컴파일을 보게 될 것이므로, 이에 대해 논의하겠습니다:

패키지 내용 안에는 `configure` 스크립트가 있습니다. 이 스크립트는 시스템의 종속성을 확인하며, 누락된 것이 있으면 오류가 표시되고 해당 종속성을 해결해야 합니다.

```bash
./configure
```

`./`는 현재 디렉토리에서 스크립트를 실행할 수 있도록 합니다.

```bash
make
```

패키지 내용 안에는 소프트웨어 빌드 규칙을 포함하는 `Makefile`이라는 파일이 있습니다. `make` 명령을 실행하면 이 파일을 참조하여 소프트웨어를 빌드합니다.

```bash
sudo make install
```

이 명령어는 실제로 패키지를 설치합니다. 올바른 파일을 컴퓨터의 올바른 위치에 복사합니다.

패키지를 제거하려면 다음을 사용합니다:

```bash
sudo make uninstall
```

`make install`을 사용할 때는 주의해야 합니다. 백그라운드에서 얼마나 많은 일이 일어나는지 깨닫지 못할 수 있습니다. 이 패키지를 제거하기로 결정하더라도, 시스템에 추가된 내용을 알지 못했기 때문에 모든 것을 실제로 제거하지 못할 수도 있습니다. 대신, 방금 설명한 `make install`에 대한 모든 것을 잊고 **checkinstall** 명령을 사용하십시오. 이 명령은 쉽게 설치하고 제거할 수 있는 `.deb` 파일을 만들어 줄 것입니다.

```bash
sudo checkinstall
```

이 명령어는 본질적으로 "make install"을 수행하고 `.deb` 패키지를 빌드하여 설치합니다. 이렇게 하면 나중에 패키지를 더 쉽게 제거할 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 소스에서 소프트웨어를 빌드하는 이해를 강화하기 위한 실습입니다:

1. **[Linux 에서 소스 코드로부터 소프트웨어 빌드하기](https://labex.io/ko/labs/comptia-build-software-from-source-code-in-linux-590853)** - `configure`, `make`, `make install`을 포함하여 소스 코드로부터 소프트웨어를 빌드하고 설치하는 기본적인 과정을 연습합니다.

이 실습은 실제 시나리오에서 개념을 적용하고 소프트웨어 컴파일에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

`make install` 대신 항상 무엇을 사용해야 할까요?

## Quiz Answer

checkinstall
