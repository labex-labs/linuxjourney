---
lesson_id: "sysv-overview"
course_id: "init"
lang: "ko"
order_index: 1
title: "System V 개요"
description: "전통적인 System V init이 런레벨과 순서가 지정된 서비스 스크립트 링크를 사용하는 방법을 알아봅니다."
meta_title: "System V 개요 - Init"
meta_description: "전통적인 System V init 시스템을 살펴봅니다. sysvinit이 프로세스, 순차적 시작 및 리눅스 런레벨을 관리하는 방식을 설명합니다."
meta_keywords: "System V, sysvinit, SysV init, 리눅스 런레벨, init 시스템, 프로세스 관리, 리눅스 튜토리얼"
---

일반적으로 SysV init 또는 sysvinit이라고 부르는 System V init은 전통적인 PID 1 및 서비스 시작 설계입니다. 레거시 시스템과 호환성 스크립트에서 여전히 중요하지만 SysV 방식 파일이 설치되어 있다고 해서 sysvinit이 실행 중인 PID 1이라는 증거는 아닙니다.

## 활성 Init 시스템 식별하기

실행 중인 PID 1을 검사합니다.

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

`/etc/inittab` 파일이나 `/etc/init.d/` 디렉터리는 보조 증거일 뿐입니다. systemd와 다른 init 시스템도 호환성을 위해 이 파일을 유지할 수 있고 컨테이너에서는 호스트와 다른 PID 네임스페이스가 보일 수 있습니다.

:::single-choice{#sysv-overview-detection} sysvinit이 활성 상태라는 가장 강한 증거는 무엇입니까?

::option[실행 중인 PID 1 실행 파일이 sysvinit 또는 해당 init 프로그램입니다.]{#sysv-overview-live-pid-one .correct explanation="실행 중인 첫 프로세스를 검사하는 편이 호환성 파일에서 추론하는 것보다 직접적입니다."}
::option[`/etc/init.d/` 디렉터리가 존재합니다.]{#sysv-overview-init-d-only explanation="다른 init 시스템도 SysV 스크립트나 래퍼를 흔히 보존합니다."}
::option[패키지 설명에 service라는 단어가 들어 있습니다.]{#sysv-overview-package-word explanation="패키지 텍스트는 현재 PID 1 역할을 하는 프로세스를 식별하지 않습니다."}
:::

## 런레벨

런레벨은 숫자로 이름을 붙인 운영 모드입니다. SysV 설정은 전통적으로 `0`부터 `6`까지의 레벨과 특수 레벨을 사용하지만 그 의미는 보편적인 법칙이 아니라 배포판 정책입니다. 일반적인 관례는 다음과 같습니다.

- `0`: 정지 또는 전원 끄기 전환
- `1` 또는 `S`: 단일 사용자 또는 복구 모드
- `2`부터 `5`: 배포판에서 정의한 다중 사용자 모드
- `6`: 재부팅 전환

데비안 계열 시스템은 역사적으로 레벨 2~5를 비슷하게 취급했지만 레드햇 계열 관례는 텍스트 모드와 그래픽 모드를 구분합니다. 실제 호스트의 `/etc/inittab`, init 문서 및 런레벨 디렉터리를 검사하십시오.

:::single-choice{#sysv-overview-shutdown-runlevel} 여러 SysV 시스템에서 정지 또는 전원 끄기를 일반적으로 요청하는 런레벨은 무엇입니까?

::option[`3`]{#sysv-overview-runlevel-three explanation="일반적으로 종료가 아니라 다중 사용자 운영 모드입니다."}
::option[`0`]{#sysv-overview-runlevel-zero .correct explanation="로컬 init 정책이 우선하지만 레벨 0은 일반적으로 종료 전환입니다."}
::option[`6`]{#sysv-overview-runlevel-six explanation="레벨 6은 일반적으로 재부팅을 요청합니다."}
:::

## Init 스크립트와 런레벨 링크

서비스 스크립트는 일반적으로 `/etc/init.d/` 아래에 있습니다. `/etc/rc2.d/` 또는 `/etc/rc.d/rc2.d/` 같은 런레벨 디렉터리에는 전환 작업과 순서를 이름에 인코딩한 링크가 있습니다.

- `SNNname` 링크는 시작 작업을 요청합니다.
- `KNNname` 링크는 중지 작업을 요청합니다.
- `NN`은 해당 전환에서 링크 사이의 사전식 순서를 제공합니다.

정확한 알고리즘과 디렉터리는 서로 다릅니다. 의존성을 스크립트 헤더로 표현하고 배포판 도구로 처리할 수도 있으며 일부 구현은 작업을 병렬화합니다. SysV를 모든 서비스가 반드시 하나씩 엄격히 시작된다는 보장으로 단순화해서는 안 됩니다.

:::single-choice{#sysv-overview-start-link} 런레벨에 진입할 때 `S20networking` 링크는 일반적으로 무엇을 요청합니까?

::option[모든 네트워크 프로세스에 신호 20을 직접 보냅니다.]{#sysv-overview-signal-twenty explanation="숫자는 신호 번호가 아니라 순서 메타데이터입니다."}
::option[네트워크 설정 백업을 20개 저장합니다.]{#sysv-overview-twenty-backups explanation="런레벨 링크는 백업 보존 기능을 제공하지 않습니다."}
::option[연결된 서비스 스크립트를 `S` 순서의 시작 작업으로 실행합니다.]{#sysv-overview-start-action .correct explanation="접두사는 시작 링크를 구분하고 숫자는 순서에 기여합니다."}
:::

## 런레벨 사이 전환

init이 런레벨을 변경하면 배포판의 rc 메커니즘이 새 모드에 필요 없는 서비스를 중지하고 필요한 서비스를 시작합니다. 스크립트는 반복되는 상태 또는 전환 작업을 처리할 수 있을 만큼 멱등성을 갖추고 의미 있는 상태를 반환해야 합니다.

런레벨 0 또는 6 요청은 시스템 전체 가용성에 영향을 주는 파괴적 작업입니다. 원시 init 전환을 가볍게 호출하지 말고 시스템 종료 인터페이스를 사용하고, 사용자에게 알리고, 활성 작업을 보존하며, 원격 콘솔 접근을 확인하십시오.

:::single-choice{#sysv-overview-runlevel-six-meaning} 런레벨 `6`은 일반적으로 무엇을 요청합니까?

::option[사용자 계정 여섯 개를 추가로 만듭니다.]{#sysv-overview-six-users explanation="런레벨은 계정 수가 아니라 운영 모드를 설명합니다."}
::option[시스템 재부팅 전환입니다.]{#sysv-overview-reboot .correct explanation="전통적인 SysV 정책은 서비스 중지와 시스템 재시작에 레벨 6을 사용합니다."}
::option[모든 파일 시스템을 영구적으로 읽기 전용 마운트합니다.]{#sysv-overview-six-readonly explanation="일반적인 런레벨 6의 목적이 아닙니다."}
:::

## 호환성의 한계

systemd 호스트에서 SysV 스크립트는 생성된 단위로 감싸질 수 있지만 systemd 의존성, 시간 제한, 로깅 및 상태 의미 체계가 계속 적용됩니다. 레거시 스크립트를 직접 실행하면 서비스 관리자의 추적을 우회할 수 있습니다. 활성 관리자를 식별하고 가능하면 고유 인터페이스를 사용하십시오.

:::single-choice{#sysv-overview-compatibility-script} systemd 호스트의 SysV 방식 스크립트를 일반적으로 서비스 관리자를 통해 호출해야 하는 이유는 무엇입니까?

::option[직접 실행하면 의존성과 상태 추적을 우회할 수 있기 때문입니다.]{#sysv-overview-manager-tracking .correct explanation="관리자는 프로세스 소유권, 순서, 시간 제한 및 상태를 조정해야 합니다."}
::option[systemd 시스템에서는 셸 스크립트를 실행할 수 없기 때문입니다.]{#sysv-overview-scripts-impossible explanation="실행할 수 있지만 감독을 우회하면 상태가 일치하지 않을 수 있습니다."}
::option[systemd가 모든 서비스 스크립트를 커널 모듈로 변환하기 때문입니다.]{#sysv-overview-script-module explanation="호환성 단위는 사용자 공간 서비스 관리로 남습니다."}
:::

## 요약

이제 전통적인 SysV 레이아웃이 활성 상태라고 가정하지 않고 해석할 수 있습니다.

1. init 명령을 선택하기 전에 실행 중인 PID 1을 식별합니다.
2. 런레벨 의미를 배포판이 정의한 관례로 취급합니다.
3. 런레벨 링크의 `S`, `K` 및 숫자 순서를 읽습니다.
4. 레벨 0과 6에는 제어된 종료 절차를 사용합니다.
5. 호환성 스크립트가 있을 때 활성 관리자를 존중합니다.
