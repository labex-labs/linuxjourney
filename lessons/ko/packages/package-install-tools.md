---
index: 5
lang: "ko"
title: "rpm 및 dpkg"
meta_title: "rpm 및 dpkg - 패키지"
meta_description: "rpm 및 dpkg 명령을 사용하여 패키지를 설치, 제거 및 나열하는 방법을 배웁니다. .deb 및 .rpm 파일에 대한 직접 패키지 관리를 이해합니다. Linux 여정을 시작하세요!"
meta_keywords: "rpm, dpkg, Linux 패키지 관리, .deb, .rpm, Linux 튜토리얼, 초보자 가이드, 패키지 설치"
---

## Lesson Content

이 과정의 대부분은 패키지 관리 시스템 (패키지 관리의 배트맨) 에 관한 것이지만, 로빈들을 잊어서는 안 됩니다. 매우 유용하고 신뢰할 수 있지만, 멋진 배트모빌과 유틸리티 벨트는 함께 제공되지 않습니다.

`.exe`가 단일 실행 파일인 것처럼, `.deb`와 `.rpm`도 마찬가지입니다. 일반적으로 패키지 저장소를 사용한다면 이들을 볼 일이 없겠지만, 패키지를 직접 다운로드한다면 이 인기 있는 형식으로 얻게 될 가능성이 높습니다. 분명히, 이들은 각 배포판에만 해당됩니다: Debian 기반은 `.deb`, Red Hat 기반은 `.rpm`입니다.

이러한 직접 패키지를 설치하려면 `rpm` 및 `dpkg`와 같은 패키지 관리 명령을 사용할 수 있습니다. 이 도구들은 패키지 파일을 설치하는 데 사용되지만, 패키지 종속성은 설치하지 않습니다. 따라서 패키지에 10 개의 종속성이 있다면, 해당 패키지들을 별도로 설치하고, 그 다음 그들의 종속성을 설치하는 식으로 계속해야 합니다. 보시다시피, 이것이 나중에 논의할 완전한 관리 시스템이 등장하게 된 이유 중 하나였습니다.

이러한 도구 중 하나로 패키지를 설치, 쿼리 또는 확인해야 할 경우가 셀 수 없이 많을 것이므로, 이 명령들을 기억하십시오.

### Install a package

```bash
Debian: $ dpkg -i some_deb_package.deb
RPM: $ rpm -i some_rpm_package.rpm
```

`i`는 install 을 의미합니다. 더 긴 형식인 `--install`을 사용할 수도 있습니다.

### Remove a package

```bash
Debian: $ dpkg -r some_deb_package.deb
RPM: $ rpm -e some_rpm_package.rpm
```

Debian: `r` for remove
RPM: `e` for erase

### List installed packages

```bash
Debian: $ dpkg -l
RPM: $ rpm -qa
```

Debian: `l` for list
RPM: `q` for query and `a` for all

## Exercise

Google Chrome 과 같이 시스템에 설치하고 싶은 프로그램을 찾아 이 명령 중 하나를 사용하여 설치하십시오.

## Quiz Question

`.deb` 파일용 패키지 관리 도구는 무엇입니까?

## Quiz Answer

dpkg
