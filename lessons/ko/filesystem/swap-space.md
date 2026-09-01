---
lesson_id: "swap-space"
course_id: "filesystem"
lang: "ko"
order_index: 8
title: "스왑"
description: "리눅스가 스왑 공간을 사용, 초기화, 활성화, 용량 계획 및 안전하게 비활성화하는 방법을 알아봅니다."
meta_title: "스왑 - 파일 시스템"
meta_description: "리눅스 스왑 공간의 작동 방식과 스왑 파티션을 만들고 관리하는 방법을 알아봅니다. 시스템 메모리 사용을 이해하고 조정합니다."
meta_keywords: "리눅스 스왑, mkswap, swapon, swapoff, /etc/fstab, 가상 메모리, 리눅스 튜토리얼"
---

리눅스는 선택된 익명 메모리 페이지를 RAM과 스왑 기반 저장 공간 사이에서 이동할 수 있습니다. 비활성 메모리를 유지하면서 활성 작업 부하와 파일 시스템 캐시를 위한 RAM을 확보할 수 있지만 저장 장치는 RAM보다 훨씬 느립니다. 스왑은 용량 및 메모리 관리 도구이며 충분한 메모리나 애플리케이션 메모리 제한을 대신하지 않습니다.

## 메모리 관리에서 스왑이 수행하는 역할

커널은 작업 부하, 메모리 압력, cgroup 및 swappiness 같은 조정값에 따라 RAM이 완전히 소진되기 전에도 스왑을 사용할 수 있습니다. 파일이 뒷받침하는 깨끗한 페이지는 버린 뒤 파일에서 다시 읽을 수 있는 경우가 많지만, 익명 페이지는 스왑이 필요하거나 RAM에 남아 있어야 합니다.

지속적으로 많은 스왑을 사용하면 심각한 지연이나 스래싱이 생길 수 있습니다. 스왑 영역을 늘리는 것을 보편적인 성능 해결책으로 취급하지 말고 메모리 수요, 작업 집합, 압력 및 애플리케이션 제한을 진단하십시오.

:::single-choice{#swap-space-anonymous-pages} 스왑 저장 공간의 주요 후보가 되는 메모리는 무엇입니까?

::option[`/usr` 아래에 설치된 모든 실행 파일입니다.]{#swap-space-installed-files explanation="설치된 파일은 파일 시스템에 남아 있으며 깨끗하게 매핑된 페이지는 그곳에서 다시 읽을 수 있습니다."}
::option[비활성 익명 메모리 페이지입니다.]{#swap-space-anonymous-memory .correct explanation="익명 페이지에는 단순히 다시 읽을 수 있는 일반 백업 파일이 없습니다."}
::option[디스크의 파티션 테이블 항목입니다.]{#swap-space-partition-table explanation="파티션 메타데이터는 블록 장치에 남으며 RAM에서 스왑되는 프로세스 메모리가 아닙니다."}
:::

## 활성 스왑 검사하기

읽기 전용 명령부터 사용합니다.

```bash
$ swapon --show
$ cat /proc/swaps
$ free -h
```

이 명령들은 설정되어 활성화된 스왑과 전체 메모리 수치를 보여 줍니다. “사용 중” 값이 0보다 크다고 해서 자동으로 문제가 있는 것은 아닙니다. 스왑 입출력 비율, 메모리 압력, 지연 및 작업 부하 동작과 함께 살펴보십시오.

:::single-choice{#swap-space-show-active} 활성 스왑 영역을 구조화된 뷰로 나열하는 명령은 무엇입니까?

::option[`swapon --show`]{#swap-space-swapon-show .correct explanation="show 모드는 활성 스왑 파일이나 장치와 가능한 경우 크기, 사용량 및 우선순위를 보고합니다."}
::option[`mkswap --all`]{#swap-space-mkswap-all explanation="mkswap은 스왑 서명을 초기화하며 읽기 전용 활성 목록 명령이 아닙니다."}
::option[`mkfs -t swap`]{#swap-space-mkfs-swap explanation="표준 초기화 도구는 `mkswap`이며 포맷은 상태 조회가 아닙니다."}
:::

## 스왑 장치 초기화 및 활성화

`mkswap`은 스왑 서명을 기록하고 대상의 이전 사용 가능한 메타데이터를 파괴합니다. 검증된 폐기 가능한 대상에서만 연습하십시오.

```bash
$ sudo mkswap /dev/VERIFIED-SWAP-TARGET
$ sudo swapon /dev/VERIFIED-SWAP-TARGET
```

`mkswap` 전에 `mkfs`와 마찬가지로 모델, 일련번호, 크기, 영구 식별 정보, 기존 서명, 마운트, RAID, LVM, 암호화 및 백업을 검증하십시오. 활성화한 후 `swapon --show`로 정확한 소스를 확인합니다.

영구 적용에는 로컬 정책에 맞는 유형과 옵션과 함께 `/etc/fstab`에 스왑 UUID를 사용합니다.

```text
UUID=VERIFIED-SWAP-UUID none swap sw 0 0
```

:::single-choice{#swap-space-enable-command} 초기화된 스왑 영역을 활성화하는 명령은 무엇입니까?

::option[`swapon`]{#swap-space-command-swapon .correct explanation="swapon은 유효한 스왑 장치나 파일을 커널의 활성 스왑 집합에 추가합니다."}
::option[`mkswap`]{#swap-space-command-mkswap explanation="mkswap은 서명을 초기화하지만 영역을 활성화하지는 않습니다."}
::option[`mount`]{#swap-space-command-mount explanation="스왑은 디렉터리 파일 시스템으로 마운트하지 않고 스왑 하위 시스템을 통해 활성화합니다."}
:::

## 스왑 파일과 기타 백엔드

스왑 파일은 파티션을 다시 나누지 않고 유연한 용량을 제공할 수 있지만 생성 요구 사항은 파일 시스템마다 다릅니다. 파일에는 제한적인 권한, 지원되지 않는 홀이나 쓰기 시 복사 동작이 없는 적절한 할당, 스왑 서명 및 활성화가 필요합니다. 어디에서나 일반적인 `fallocate` 방법을 복사하지 말고 파일 시스템과 배포판 문서를 따르십시오.

zram 같은 압축 RAM 장치는 CPU와 용량의 절충이 다른 또 하나의 스왑 계층을 제공할 수 있습니다. 암호화 스왑은 저장된 페이지를 보호할 수 있고, 최대 절전 모드에는 재개 설정과 충분하고 적합한 저장 공간이 필요합니다. 이러한 목표는 용량과 설계에 영향을 줍니다.

스왑이 항상 RAM의 두 배여야 한다는 보편적인 규칙은 없습니다. 작업 부하 최고점, 원하는 장애 동작, 최대 절전 모드 요구 사항, 저장 장치 지연과 내구성, 크래시 덤프 설계 및 운영 모니터링에 따라 용량을 정하십시오.

:::single-choice{#swap-space-sizing-rule} 스왑 용량을 정하는 가장 좋은 기준은 무엇입니까?

::option[항상 설치된 RAM의 정확히 두 배입니다.]{#swap-space-twice-ram explanation="이 오래된 경험 법칙은 모든 작업 부하나 최신 메모리 크기에 적합하지 않습니다."}
::option[측정된 작업 부하 요구 사항, 최대 절전 모드 목표 및 장애 정책입니다.]{#swap-space-sizing-requirements .correct explanation="고정된 RAM 배수보다 시스템 목적과 관찰된 메모리 동작이 중요합니다."}
::option[SSD가 있으면 항상 0으로 설정합니다.]{#swap-space-zero-ssd explanation="저장 장치 유형만으로 메모리 압력이나 최대 절전 요구 사항이 결정되지는 않습니다."}
:::

## 안전하게 스왑 비활성화하기

검증된 특정 영역을 다음 명령으로 비활성화합니다.

```bash
$ sudo swapoff /dev/VERIFIED-SWAP-TARGET
```

커널은 그 영역에 있는 스왑 페이지를 다른 곳으로 옮겨야 합니다. RAM과 남은 스왑에 페이지를 수용할 공간이 없으면 작업이 실패하거나 위험한 메모리 압력을 만들 수 있습니다. 먼저 작업 부하를 중지하거나 제한하고 메모리를 모니터링하십시오. 올바른 대상을 검증한 뒤에만 영구 fstab 항목을 제거하고, 저장 공간을 다른 용도로 사용하기 전에 `swapon --show`로 비활성화를 확인합니다.

:::single-choice{#swap-space-swapoff-capacity} `swapoff`가 심하게 부하된 시스템에서 실패하거나 위험을 일으킬 수 있는 이유는 무엇입니까?

::option[swapoff가 항상 모든 RAM 모듈을 다시 포맷하기 때문입니다.]{#swap-space-formats-ram explanation="활성 스왑 설정을 변경하며 물리 메모리 하드웨어를 포맷하지 않습니다."}
::option[해당 영역의 페이지를 수용할 RAM이나 다른 스왑 공간이 필요하기 때문입니다.]{#swap-space-pages-need-capacity .correct explanation="비활성화하려면 시스템이 계속 작동하는 동안 살아 있는 스왑 페이지를 다른 곳으로 옮겨야 합니다."}
::option[비활성 스왑 영역을 `/swap`에 계속 마운트해야 하기 때문입니다.]{#swap-space-mounted-path explanation="스왑 영역은 디렉터리에 마운트하는 파일 시스템이 아닙니다."}
:::

제어된 환경에서 [리눅스 스왑 파일 생성 및 활성화하기](https://labex.io/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)를 사용해 파일 권한, 활성화 및 영구 적용을 연습해 보십시오.

## 요약

이제 스왑을 명시적인 메모리 관리 리소스로 취급할 수 있습니다.

1. 스왑을 주로 압력을 받는 익명 메모리와 연결합니다.
2. 용량을 변경하기 전에 활성 스왑과 작업 부하 동작을 검사합니다.
3. 검증된 폐기 가능 대상만 초기화한 뒤 `swapon`으로 활성화합니다.
4. 작업 부하와 최대 절전 요구 사항에 따라 스왑의 용량을 정하고 보호합니다.
5. `swapoff`를 사용하기 전에 페이지를 옮길 공간이 있는지 확인합니다.
