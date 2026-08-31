---
lesson_id: "tracking-processes-lsof-fuser"
course_id: "process-utilization"
lang: "ko"
order_index: 2
title: "lsof와 fuser"
description: "파일, 디렉터리, 마운트 지점 및 네트워크 소켓을 사용하는 프로세스를 식별하는 방법을 알아봅니다."
meta_title: "lsof와 fuser - 프로세스 사용량"
meta_description: "리눅스의 lsof와 fuser 명령으로 특정 파일을 사용하는 프로세스를 식별하는 방법을 알아봅니다. 장치 사용 중 오류, 두 도구의 차이 및 안전한 대응을 설명합니다."
meta_keywords: "lsof, fuser, fuser 명령어, 리눅스 fuser, lsof와 fuser 비교, 열린 파일, 프로세스 관리, 장치 사용 중"
---

프로세스가 파일을 열고 있거나 메모리에 매핑하거나 디렉터리를 현재 작업 디렉터리로 사용하면 파일 시스템이 사용 중 상태로 남을 수 있습니다. `lsof`와 `fuser`는 이러한 관계를 식별하는 데 도움을 줍니다. 먼저 검사하십시오. 프로세스 중지는 운영상 결과가 있는 별도의 결정입니다.

## lsof로 열린 파일 나열하기

`lsof`는 “열린 파일 나열”을 뜻합니다. 경로를 조회하여 일치하는 열린 파일 레코드를 확인합니다.

```bash
$ sudo lsof -- /mnt/usb
```

같은 파일 시스템의 전체 디렉터리 트리에는 구현에서 일반적으로 `+D`를 지원하지만 재귀 검사는 비용이 클 수 있습니다.

```bash
$ sudo lsof +D /mnt/usb
```

유용한 열에는 `COMMAND`, `PID`, `USER`, 파일 디스크립터(`FD`), 유형, 장치 및 `NAME`이 있습니다. `FD`가 `cwd`인 레코드는 프로세스가 해당 디렉터리를 현재 작업 디렉터리로 사용함을 나타냅니다. 비특권 출력은 다른 사용자가 소유한 프로세스에 대해 불완전할 수 있습니다.

:::single-choice{#lsof-cwd-record}
`FD` 열의 `cwd`는 무엇을 나타냅니까?

::option[프로세스가 해당 디렉터리를 현재 작업 디렉터리로 사용합니다.]{#lsof-current-directory .correct explanation="프로세스의 현재 디렉터리는 마운트된 파일 시스템을 사용 중 상태로 유지할 수 있습니다."}
::option[쓰는 도중 파일이 닫혔습니다.]{#lsof-closed-write explanation="이 표시는 닫기 이벤트가 아니라 디렉터리 관계를 설명합니다."}
::option[프로세스가 파일 시스템 장치를 소유합니다.]{#lsof-device-owner explanation="파일 시스템 소유권은 `cwd` 디스크립터 레이블로 표현되지 않습니다."}
:::

## fuser로 사용자 식별하기

`fuser`는 지정된 파일이나 파일 시스템을 사용하는 프로세스 ID를 보고합니다. 상세 출력은 사용자, 접근 유형 및 명령 이름을 추가합니다.

```bash
$ sudo fuser -v /mnt/usb
```

인수를 마운트된 파일 시스템으로 취급하고 그 안의 파일에 접근하는 프로세스를 찾으려면 procps `fuser`가 지원하는 마운트 옵션을 사용합니다.

```bash
$ sudo fuser -vm /mnt/usb
```

`findmnt --target /mnt/usb` 같은 도구로 경로가 의도한 마운트 지점인지 검증하십시오. 바인드 마운트, 네임스페이스, 권한 및 경쟁 상태 때문에 한 번의 조회 결과가 불완전할 수 있습니다.

:::single-choice{#fuser-verbose-purpose}
조사 중에 일반 `fuser` 대신 `fuser -v`를 사용하는 이유는 무엇입니까?

::option[선택한 파일 시스템을 자동으로 마운트 해제합니다.]{#fuser-verbose-unmount explanation="상세 모드는 정보를 보고할 뿐 마운트 해제를 요청하지 않습니다."}
::option[사용자, 접근 유형 및 명령 같은 맥락을 추가합니다.]{#fuser-verbose-details .correct explanation="추가 열은 어떤 프로세스를 조정하거나 중지해도 안전한지 판단하는 데 도움을 줍니다."}
::option[프로세스가 파일을 다시 여는 것을 영구적으로 막습니다.]{#fuser-verbose-prevent explanation="보고 작업은 접근 제어 규칙을 만들지 않습니다."}
:::

## 사용 중인 파일 시스템 처리하기

일치하는 모든 PID를 즉시 종료하지 말고 의도적인 순서를 따르십시오.

1. 호스트, 경로, 마운트 소스 및 의도한 유지 관리를 확인합니다.
2. 가능하면 두 도구로 프로세스를 식별합니다.
3. 각 프로세스를 중지하거나 디렉터리 밖으로 이동하거나 끝날 때까지 기다릴 수 있는지 판단합니다.
4. 가능한 경우 서비스 관리자 또는 애플리케이션 인터페이스를 통해 중지합니다.
5. 다시 조회한 뒤 마운트 해제하고 결과를 검증합니다.

`fuser -k`는 일치하는 프로세스에 신호를 보냅니다. 일반적인 procps 구현의 기본 신호는 `SIGKILL`이므로 질서 있는 종료를 제공하지 않습니다. 명시적으로 승인된 종료가 필요하다면 적절한 신호를 선택하고 PID와 소유자를 검증하며, 검사와 작업 사이에 프로세스 집합이 바뀔 수 있음을 이해하십시오.

:::single-choice{#fuser-k-risk}
`fuser -k /mnt/usb`가 좋지 않은 첫 문제 해결 단계인 이유는 무엇입니까?

::option[파일 시스템 여유 공간만 출력하기 때문입니다.]{#fuser-k-space explanation="이 옵션은 용량을 보고하는 대신 프로세스를 대상으로 합니다."}
::option[질서 있는 정리 없이 일치하는 여러 프로세스를 종료할 수 있기 때문입니다.]{#fuser-k-kills .correct explanation="광범위한 신호 작업은 쓰기나 서비스를 중단할 수 있으므로 먼저 조사하고 조정해야 합니다."}
::option[일치하는 모든 프로세스의 작업 디렉터리를 바꾸기 때문입니다.]{#fuser-k-chdir explanation="신호를 보낼 뿐 프로세스 디렉터리를 이동하지 않습니다."}
:::

## 도구 선택하기

상세한 열린 파일 레코드, 디스크립터 또는 소켓 정보가 필요하면 `lsof`를 사용합니다. 경로 중심의 일치 PID와 접근 유형 뷰에는 `fuser`를 사용합니다. 어느 결과도 그 자체로 프로세스를 종료해도 안전한지 알려 주지는 않습니다.

네트워크 소켓에는 `fuser`의 명시적인 프로토콜 네임스페이스나 `ss` 같은 소켓 중심 도구를 사용합니다.

```bash
$ sudo fuser -v 22/tcp
$ sudo ss -lntp
```

:::single-choice{#lsof-fuser-tool-choice}
열린 파일 디스크립터와 소유 프로세스의 상세 목록에 적합한 도구는 무엇입니까?

::option[`lsof`]{#lsof-detailed-records .correct explanation="출력은 열린 파일 레코드와 해당 프로세스 메타데이터를 중심으로 구성됩니다."}
::option[`uptime`]{#lsof-uptime explanation="uptime은 열린 디스크립터가 아니라 가동 시간과 부하 평균을 보고합니다."}
::option[`free`]{#lsof-free explanation="free는 파일 사용이 아니라 메모리를 요약합니다."}
:::

## 요약

이제 종료를 기본 대응으로 취급하지 않고 파일 및 파일 시스템 사용을 조사할 수 있습니다.

1. 상세한 열린 파일 레코드에는 `lsof`를 사용합니다.
2. 경로 중심 PID와 접근 정보에는 `fuser`를 사용합니다.
3. 마운트를 확인하고 권한과 경쟁 상태를 고려합니다.
4. 신호를 고려하기 전에 질서 있는 중지를 조정합니다.
5. 다시 조회하고 마운트 해제 또는 서비스 결과를 검증합니다.
