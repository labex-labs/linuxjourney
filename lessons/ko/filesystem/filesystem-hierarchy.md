---
lesson_id: "filesystem-hierarchy"
course_id: "filesystem"
lang: "ko"
order_index: 1
title: "파일 시스템 계층"
description: "리눅스의 주요 디렉터리가 맡는 일반적인 역할과 최신 병합 레이아웃의 차이를 알아봅니다."
meta_title: "파일 시스템 계층 - 파일 시스템"
meta_description: "표준 리눅스 파일 시스템 계층(FHS)을 살펴봅니다. /bin, /etc, /home 및 /var 같은 주요 디렉터리의 목적과 리눅스 디렉터리 구조를 설명합니다."
meta_keywords: "리눅스 파일 시스템 계층, 리눅스 파일 계층 구조, 리눅스 디렉터리 구조, FHS, 리눅스 파일 시스템"
---

리눅스는 마운트된 파일 시스템을 `/`에 뿌리를 둔 하나의 디렉터리 트리로 표시합니다. 파일 시스템 계층 표준(FHS)은 여러 디렉터리의 일반적인 역할을 정의하지만 배포판, 컨테이너, 불변 시스템 및 로컬 정책에 따라 달라질 수 있습니다. 경로에 의존하기 전에 실제 호스트를 검사하십시오.

```bash
$ ls -ld /*
```

## 루트와 필수 시스템 경로

- `/`는 보이는 파일 시스템 트리의 루트입니다.
- `/etc`에는 호스트별 시스템 설정이 있습니다. 실행 가능한 보조 또는 시작 스크립트도 포함될 수 있으므로 실행 가능한 내용이 절대 없다고 말하면 정확하지 않습니다.
- `/boot`에는 부트 로더 데이터와, 여러 시스템의 경우 커널 및 초기 RAM 파일 시스템 이미지 같은 부팅 관련 파일이 있습니다.
- `/bin`과 `/sbin`에는 전통적으로 필수 사용자 및 시스템 관리 명령이 있습니다.
- `/lib`와 아키텍처별 변형에는 전통적으로 필수 공유 라이브러리와 로더 구성 요소가 있습니다.

현재 여러 배포판은 `/bin`, `/sbin` 및 `/lib`가 대응하는 `/usr` 디렉터리를 가리키는 심볼릭 링크인 병합된 `/usr` 레이아웃을 사용합니다. 경로가 실제 디렉터리인지 링크인지 가정하지 말고 명령 검색 기능과 패키지 레코드를 사용하십시오.

:::single-choice{#filesystem-hierarchy-configuration-directory} 호스트별 시스템 설정이 일반적으로 들어 있는 디렉터리는 무엇입니까?

::option[`/proc`]{#filesystem-hierarchy-proc-config explanation="procfs는 영구적인 호스트 설정 파일이 아니라 실시간 프로세스와 커널 인터페이스를 제공합니다."}
::option[`/etc`]{#filesystem-hierarchy-etc .correct explanation="시스템과 서비스 설정은 일반적으로 `/etc` 아래에 구성됩니다."}
::option[`/dev`]{#filesystem-hierarchy-dev-config explanation="`/dev`에는 일반 설정 계층이 아니라 런타임 장치 인터페이스 객체가 있습니다."}
:::

## 배포판 및 로컬 소프트웨어

- `/usr`에는 명령, 라이브러리 및 아키텍처 독립 데이터 등 공유 가능하고 대체로 읽기 전용인 운영체제와 애플리케이션의 주 계층이 있습니다.
- `/usr/local`은 배포판의 일반 `/usr` 관리 바깥에서 로컬 관리자가 설치한 소프트웨어와 데이터를 위해 예약됩니다.
- `/opt`에는 자체 완결된 하위 트리 형태의 추가 애플리케이션 패키지를 둘 수 있습니다.

이름과 달리 `/usr`은 일반적으로 개별 사용자의 개인 파일이 있는 곳이 아닙니다. 배포판 패키지 관리자는 대개 이 영역의 많은 부분을 소유하므로 로컬에서 컴파일한 파일을 `/usr/bin`에 복사하면 관리 패키지와 충돌할 수 있습니다.

:::single-choice{#filesystem-hierarchy-local-software} 배포판이 관리하는 `/usr` 콘텐츠 외부에서 로컬로 설치한 소프트웨어를 위해 일반적으로 예약된 접두사는 무엇입니까?

::option[`/usr/local`]{#filesystem-hierarchy-usr-local .correct explanation="로컬 계층은 관리자가 설치한 소프트웨어를 배포판의 기본 `/usr` 트리와 분리합니다."}
::option[`/proc/local`]{#filesystem-hierarchy-proc-local explanation="procfs는 가상 커널 인터페이스이며 영구적인 소프트웨어 접두사가 아닙니다."}
::option[`/dev/local`]{#filesystem-hierarchy-dev-local explanation="장치 노드 저장 위치는 로컬 애플리케이션의 일반적인 위치가 아닙니다."}
:::

## 사용자 및 서비스 데이터

- `/home`에는 일반적으로 root가 아닌 사용자의 홈 디렉터리가 있지만 디렉터리 서비스와 로컬 정책에 따라 다른 위치에 둘 수 있습니다.
- `/root`는 root 계정의 일반적인 홈 디렉터리입니다.
- `/srv`는 이 시스템이 제공하는 사이트별 데이터를 위한 디렉터리입니다.

홈 경로는 단순히 `/home`과 사용자 이름을 합친 값이 아니라 계정 정보에서 가져옵니다. 경로를 하드 코딩하지 말고 `getent passwd USER` 또는 셸이 해석한 홈을 사용하십시오.

:::single-choice{#filesystem-hierarchy-root-home} root 계정의 일반적인 홈 디렉터리는 무엇입니까?

::option[`/home/root`]{#filesystem-hierarchy-home-root explanation="일반 사용자의 홈 디렉터리는 흔히 `/home` 아래에 있지만 root에는 별도의 일반 경로가 있습니다."}
::option[`/root`]{#filesystem-hierarchy-root .correct explanation="특권 계정의 홈은 일반적으로 파일 시스템 루트 바로 아래에 있습니다."}
::option[`/usr/root`]{#filesystem-hierarchy-usr-root explanation="`/usr`은 소프트웨어와 공유 데이터 계층이며 root의 홈이 아닙니다."}
:::

## 가변, 런타임 및 임시 데이터

- `/var`에는 로그, 캐시, 스풀 및 애플리케이션 상태 같은 가변 데이터가 있습니다. 시스템 로그는 일반적으로 `/var/log` 아래에 있지만 일부 시스템은 주로 저널 인터페이스를 사용합니다.
- `/run`에는 소켓, 서비스 상태 및 PID 파일 등 현재 부팅의 휘발성 런타임 상태가 있습니다. 보통 부팅할 때 다시 생성됩니다.
- `/tmp`는 임시 파일을 위한 곳이며 일반적으로 고정 비트 보호와 함께 모든 사용자가 쓸 수 있습니다.
- `/var/tmp`는 `/tmp`의 파일보다 오래 유지되어야 하는 임시 파일을 위한 곳입니다.

`/tmp` 정리 정책은 시스템마다 다릅니다. 파일이 재부팅할 때까지 유지되거나 항상 재부팅 시 삭제된다고 가정하지 마십시오. 애플리케이션은 예측 가능한 이름 대신 안전한 임시 파일 생성 방식을 사용해야 합니다.

:::single-choice{#filesystem-hierarchy-log-path} 시스템 로그 파일을 일반적으로 저장하는 경로는 무엇입니까?

::option[`/etc/log`]{#filesystem-hierarchy-etc-log explanation="`/etc`는 누적되는 일반 로그 데이터가 아니라 설정을 위한 곳입니다."}
::option[`/var/log`]{#filesystem-hierarchy-var-log .correct explanation="로그는 가변 데이터 계층 아래에 구성되는 변경되는 시스템 데이터의 한 종류입니다."}
::option[`/boot/log`]{#filesystem-hierarchy-boot-log explanation="`/boot`는 일반 서비스 로그가 아니라 부팅 관련 결과물을 위해 예약됩니다."}
:::

## 장치, 커널 인터페이스 및 마운트 지점

- `/dev`에는 장치 노드와 관련 런타임 링크가 있습니다.
- `/proc`는 procfs를 통해 프로세스와 커널 인터페이스를 노출합니다.
- `/sys`는 sysfs를 통해 커널 객체, 장치, 드라이버 및 속성을 노출합니다.
- `/media`는 일반적으로 자동 마운트된 이동식 미디어에 사용됩니다.
- `/mnt`는 관리자의 임시 마운트에 쓰이는 일반적인 위치입니다.

이들은 관례이지 권한을 부여하는 규칙이 아닙니다. 비어 있지 않은 디렉터리에 다른 파일 시스템을 마운트하면 마운트 해제할 때까지 그 디렉터리의 기존 내용이 일시적으로 가려집니다.

:::single-choice{#filesystem-hierarchy-sysfs-path} sysfs를 통해 커널 장치 모델을 일반적으로 노출하는 경로는 무엇입니까?

::option[`/srv`]{#filesystem-hierarchy-srv explanation="`/srv`는 시스템이 제공하는 데이터를 위한 곳입니다."}
::option[`/sys`]{#filesystem-hierarchy-sys .correct explanation="sysfs는 일반적으로 `/sys`에 마운트되어 장치, 드라이버, 버스 및 속성을 제공합니다."}
::option[`/opt`]{#filesystem-hierarchy-opt explanation="`/opt`에는 선택적인 추가 애플리케이션 트리가 있습니다."}
:::

[리눅스 파일 시스템 탐색하기](https://labex.io/labs/comptia-navigate-the-filesystem-in-linux-590971)에서 이러한 경로를 검사하고, [리눅스에서 파일과 명령 찾기](https://labex.io/labs/comptia-find-files-and-commands-in-linux-590834)에서 추측한 위치에 의존하지 않는 방법을 연습해 보십시오.

## 요약

이제 실제 시스템의 차이를 고려하면서 주요 리눅스 경로를 그 용도와 연결할 수 있습니다.

1. `/`에 뿌리를 둔 통합 트리에서 시작합니다.
2. 설정, 관리 소프트웨어, 로컬 소프트웨어 및 가변 데이터를 구분합니다.
3. 홈 및 서비스 데이터를 런타임 상태와 구분합니다.
4. `/dev`, `/proc` 및 `/sys`를 특수 런타임 인터페이스로 식별합니다.
5. 레이아웃을 가정하기 전에 심볼릭 링크, 마운트, 계정 데이터 및 배포판 정책을 검사합니다.
