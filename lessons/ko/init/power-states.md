---
lesson_id: "power-states"
course_id: "init"
lang: "ko"
order_index: 7
title: "전원 상태"
description: "리눅스 종료 및 재부팅 작업을 예약, 취소 및 안전하게 검증하는 방법을 알아봅니다."
meta_title: "전원 상태 - Init"
meta_description: "리눅스 시스템 전원 상태를 관리하는 방법을 알아봅니다. shutdown, reboot, halt 및 poweroff 명령으로 시스템을 안전하게 끄거나 재시작하는 방법을 설명합니다."
meta_keywords: "리눅스 전원 상태, shutdown 명령어, reboot 명령어, halt 명령어, 리눅스 poweroff, 리눅스 재시작, systemd"
---

종료하거나 재부팅하면 전체 시스템의 가용성이 바뀝니다. 작업 전에 대상 호스트를 확인하고 승인을 받으며 연결된 사용자에게 알리고 중요한 쓰기, 백업 및 유지 관리 작업이 끝날 수 있는지 확인하십시오. 원격 시스템에서는 시스템이 다시 돌아오지 않을 경우를 대비해 독립적인 콘솔 또는 복구 경로를 유지합니다.

## 안전하게 전원 끄기

systemd 기반 배포판에서는 다음 명령으로 질서 있는 전원 끄기를 요청합니다.

```bash
$ sudo systemctl poweroff
```

전통적인 `shutdown` 인터페이스도 널리 사용할 수 있습니다.

```bash
$ sudo shutdown -h now
```

질서 있는 종료는 서비스에 중지를 요청하고 파일 시스템을 마운트 해제한 뒤 시스템의 전원 상태를 바꿉니다. 강제 재부팅이나 물리 전원 스위치를 일반적인 지름길로 사용하지 마십시오. 쓰기를 중단해 데이터나 서비스가 일관되지 않은 상태로 남을 수 있습니다.

:::single-choice{#power-states-orderly-poweroff} 원격 운영 호스트의 전원을 끄기 전에 무엇을 해야 합니까?

::option[명령을 실행하기 전에 관리 콘솔 연결을 끊습니다.]{#power-states-remove-console explanation="관리 콘솔은 유용한 복구 접근이므로 유지해야 합니다."}
::option[서비스가 작업을 지연하지 못하도록 전원을 강제로 끕니다.]{#power-states-force-first explanation="강제 작업은 쓰기를 중단할 수 있으므로 일반적인 방법으로 사용해서는 안 됩니다."}
::option[호스트를 확인하고 복구 접근 경로를 유지합니다.]{#power-states-confirm-and-recover .correct explanation="대상 확인은 잘못된 호스트에서 작업하는 것을 막고 복구 접근은 호스트가 돌아오지 않을 때 도움을 줍니다."}
:::

## 종료 예약 및 취소

작업을 예약하여 사용자와 작업 부하에 준비할 시간을 줍니다. `+m` 형식은 지금부터 몇 분 뒤를 뜻합니다.

```bash
$ sudo shutdown -h +4
```

이 명령은 4분 뒤 정지 또는 전원 끄기를 예약하고 로그인한 사용자에게 경고를 보냅니다. 유지 관리가 연기되면 기한 전에 대기 중인 종료를 취소합니다.

```bash
$ sudo shutdown -c
```

경고를 보냈다고 작업이 안전해졌다고 가정하지 마십시오. 활성 세션과 시스템별 작업 부하를 확인하고 서비스나 클러스터에 문서화된 드레인 절차가 있다면 따르십시오.

:::single-choice{#power-states-four-minute-schedule} 지금부터 4분 뒤 종료를 예약하는 명령은 무엇입니까?

::option[`sudo shutdown -h +4`]{#power-states-relative-four .correct explanation="`-h` 작업과 `+4`를 함께 사용하면 지금부터 4분 뒤 종료를 요청합니다."}
::option[`sudo shutdown -h 4`]{#power-states-absolute-four explanation="더하기 기호가 없으면 시간 인수가 문서화된 상대 분 형식이 아닙니다."}
::option[`sudo shutdown -c +4`]{#power-states-cancel-four explanation="`-c` 옵션은 새 작업을 만들지 않고 대기 중인 종료를 취소합니다."}
:::

## 시스템 재부팅

시스템을 중지한 뒤 다시 시작해야 할 때 질서 있는 재부팅을 사용합니다.

```bash
$ sudo systemctl reboot
```

동등한 호환성 명령은 일반적으로 다음과 같습니다.

```bash
$ sudo shutdown -r now
$ sudo reboot
```

재부팅 전에 암호화 디스크, 부팅 설정, 네트워킹 및 필수 서비스가 현재 대화형 세션 없이 복구될 수 있는지 확인하십시오. 다른 시스템이 호스트에 의존한다면 먼저 장애 조치나 작업 부하 이전을 조정합니다.

:::single-choice{#power-states-reboot-action} `shutdown`을 통해 즉시 질서 있는 재부팅을 요청하는 명령은 무엇입니까?

::option[`sudo shutdown -c now`]{#power-states-cancel-now explanation="`-c` 옵션은 대기 중인 종료를 취소합니다."}
::option[`sudo shutdown -r now`]{#power-states-reboot-now .correct explanation="`-r` 옵션은 재부팅을 선택하고 `now`는 즉시 실행을 예약합니다."}
::option[`sudo shutdown -h now`]{#power-states-halt-now explanation="`-h` 작업은 재부팅하지 않고 정지하거나 전원을 끕니다."}
:::

## 정지와 전원 끄기 구분하기

`halt`, `poweroff` 및 `reboot`는 init 시스템의 호환성 프런트엔드일 수 있지만 요청하는 최종 상태는 다릅니다. halt는 정상 시스템 작동을 멈추며 플랫폼과 구현에 따라 전원이 계속 공급될 수 있습니다. poweroff는 지원되는 하드웨어에 전원 제거도 요청합니다. 의도한 결과를 이름으로 나타내는 명령을 우선 사용하고 호환성 동작은 다를 수 있으므로 로컬 설명서를 확인하십시오.

:::single-choice{#power-states-halt-versus-poweroff} `halt`와 `poweroff`를 구분해야 하는 이유는 무엇입니까?

::option[poweroff는 전원 제거를 요청하지만 halt는 전원이 공급된 상태로 남을 수 있기 때문입니다.]{#power-states-power-distinction .correct explanation="두 작업 모두 정상 작동을 멈추지만 요청하는 최종 하드웨어 상태는 다를 수 있습니다."}
::option[halt가 서비스를 중지한 뒤 항상 재시작하기 때문입니다.]{#power-states-halt-restarts explanation="halt는 서비스를 재시작하는 요청이 아니라 중지 상태입니다."}
::option[poweroff가 현재 터미널 사용자만 로그아웃하기 때문입니다.]{#power-states-power-logout explanation="poweroff는 셸 로그아웃이 아니라 시스템 전체 상태 전환입니다."}
:::

## 결과 검증하기

예약된 작업은 사용자에게 알림이 전달되었고 중요한 작업이 빠져나갔는지 확인하십시오. 재부팅 후에는 예상 커널과 부팅 상태, 실패한 단위, 애플리케이션 상태, 저장 장치 마운트, 네트워크 연결성 및 최근 부팅 로그를 검증합니다. 로그인 성공만으로 전체 서비스가 복구됐다고 증명할 수 없습니다.

```bash
$ uptime
$ systemctl --failed
$ journalctl -b -p warning
```

이는 시작점일 뿐이며 실제 작업 부하에는 애플리케이션 고유 상태 검사를 사용하십시오.

:::single-choice{#power-states-post-reboot-check} 재부팅한 애플리케이션이 준비되었다는 가장 강한 증거는 무엇입니까?

::option[서비스 상태, 로그 및 고유 상태 검사가 모두 성공합니다.]{#power-states-health-evidence .correct explanation="여러 시스템 및 애플리케이션 검사는 단순 호스트 접근이 아니라 작업 부하를 검증합니다."}
::option[섀시 전원 표시등이 켜져 있습니다.]{#power-states-light-on explanation="하드웨어 전원은 애플리케이션 상태를 증명하지 않습니다."}
::option[관리자가 셸에 로그인할 수 있습니다.]{#power-states-shell-open explanation="셸 접근은 시스템 가용성의 일부만 증명합니다."}
:::

## 요약

이제 준비, 명확한 의도 및 검증을 갖춰 리눅스 전원 상태를 변경할 수 있습니다.

1. 대상, 영향, 승인 및 복구 경로를 확인합니다.
2. 일반 작업에는 질서 있는 전원 끄기 또는 재부팅 명령을 사용합니다.
3. 사용자와 작업 부하에 경고가 필요하면 종료를 예약합니다.
4. 유지 관리 계획이 바뀌면 대기 중인 종료를 취소합니다.
5. 시스템이 돌아온 뒤 시스템 및 애플리케이션 상태를 검증합니다.
