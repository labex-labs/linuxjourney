---
lesson_id: "systemd-goals"
course_id: "init"
lang: "ko"
order_index: 6
title: "Systemd 목표"
description: "systemd 서비스 단위를 검사, 재정의, 검증, 시작, 활성화 및 문제 해결하는 방법을 알아봅니다."
meta_title: "Systemd 목표 - Init"
meta_description: "필수 systemctl 명령으로 리눅스 서비스를 관리하는 방법을 알아봅니다. systemd 단위 파일의 기초, 서비스 시작·중지·활성화 및 상태 확인을 설명합니다."
meta_keywords: "systemd, systemctl, 리눅스 서비스, 단위 파일, systemd 목표, 서비스 관리, systemd 단위"
---

`systemctl`은 systemd 관리자에 요청을 보냅니다. 이 수업은 시스템 서비스 단위에 초점을 맞춥니다. 상태를 변경하기 전에 정확한 단위 이름, 관리자 범위, 의존성 및 운영 영향을 확인하십시오.

## 서비스 단위 읽기

최소한의 예시 단위는 다음과 같습니다.

```ini
[Unit]
Description=Example worker
Wants=network-online.target
After=network-online.target

[Service]
Type=exec
ExecStart=/usr/local/bin/example-worker
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

- `[Unit]`에는 설명과 의존 관계가 있습니다.
- `[Service]`는 프로세스 수명 주기와 서비스별 동작을 정의합니다.
- `[Install]`은 활성화 명령이 만들 별칭이나 의존성 링크를 알려 주며 자동으로 활성 런타임 의존성이 되지는 않습니다.

`ExecStart=`는 기본적으로 셸을 통해 전달되지 않습니다. 명시적으로 셸을 호출하지 않는 한 셸 파이프라인, 리디렉션, 변수 및 인용은 대화형 명령줄처럼 동작하지 않습니다.

:::single-choice{#systemd-goals-install-section} `WantedBy=` 같은 `[Install]` 지시문의 주된 목적은 무엇입니까?

::option[서비스 프로세스가 이미 실행 중임을 보장합니다.]{#systemd-goals-install-running explanation="런타임 활성화에는 start 또는 다른 트리거 의존성이 필요합니다."}
::option[단위를 활성화할 때 만들어지는 링크나 관계를 설명합니다.]{#systemd-goals-enable-links .correct explanation="설치 메타데이터는 활성화 작업이 해석하며 현재 프로세스 상태와 별개입니다."}
::option[모든 명령을 사용자의 대화형 셸로 실행합니다.]{#systemd-goals-install-shell explanation="단위 명령 구문 분석은 기본적으로 대화형 셸을 사용하지 않습니다."}
:::

## 유효 설정 검사하기

로드된 단위를 나열합니다.

```bash
$ systemctl list-units --type=service
```

설치된 단위 파일과 활성화 상태를 나열합니다.

```bash
$ systemctl list-unit-files --type=service
```

두 명령은 서로 다른 뷰입니다. 단위 파일은 활성화되었지만 비활성 상태, 활성 상태이지만 비활성화된 상태, 정적, 생성됨, 임시, 마스크됨일 수 있으며 목록 하나에는 나타나지 않을 수도 있습니다. 병합된 공급업체 및 드롭인 내용을 검사합니다.

```bash
$ systemctl cat UNIT.service
$ systemctl show UNIT.service
```

:::single-choice{#systemd-goals-list-units-versus-files} `list-unit-files`가 주로 보여 주고 `list-units`는 주로 보여 주지 않는 것은 무엇입니까?

::option[CPU를 가장 많이 사용하는 프로세스만 보여 줍니다.]{#systemd-goals-cpu-processes explanation="프로세스 리소스 순위는 이 단위 목록 명령의 범위 밖입니다."}
::option[설치된 단위 파일의 활성화 상태입니다.]{#systemd-goals-unit-file-state .correct explanation="단위 파일이 enabled, disabled, static, masked인지와 관련 설치 상태를 보고합니다."}
::option[저널에 기록된 모든 줄입니다.]{#systemd-goals-all-journal explanation="저널 조회에는 `journalctl`을 사용합니다."}
:::

## 로컬 재정의 만들기

패키지 단위를 편집하지 말고 드롭인을 사용합니다.

```bash
$ sudo systemctl edit UNIT.service
```

현재 구현에서는 저장 후 이 편집 작업 흐름의 일부로 systemctl이 일반적으로 관리자에 다시 불러오기를 요청합니다. 다른 방식으로 파일을 변경했다면 다음 명령을 실행합니다.

```bash
$ sudo systemctl daemon-reload
```

`daemon-reload`는 단위 정의를 다시 읽고 의존성을 재구성합니다. 애플리케이션 설정을 다시 불러오거나 실행 중인 서비스를 재시작하지는 않습니다. 적절한 경우 `systemd-analyze verify`로 단위 구문과 의존성을 검증한 다음 병합된 유효 단위를 검토하십시오.

:::single-choice{#systemd-goals-daemon-reload} `systemctl daemon-reload`는 무엇을 합니까?

::option[모든 데몬이 애플리케이션 설정을 다시 읽도록 강제합니다.]{#systemd-goals-reload-all-apps explanation="애플리케이션 다시 불러오기는 서비스별 작업이며 관리자 설정과 별개입니다."}
::option[새 릴리스의 커널로 재부팅합니다.]{#systemd-goals-reload-kernel explanation="커널 활성화에는 단위 정의 다시 불러오기가 아니라 부팅이 필요합니다."}
::option[systemd 단위 정의와 의존성 정보를 다시 불러옵니다.]{#systemd-goals-reload-manager .correct explanation="서비스를 본질적으로 재시작하지 않고 관리자의 설정 뷰를 갱신합니다."}
:::

## 런타임 서비스 상태

서비스 설정을 검증하고 복구 접근을 보존한 뒤 다음 명령을 사용합니다.

```bash
$ sudo systemctl start peanut.service
$ sudo systemctl stop peanut.service
$ sudo systemctl restart peanut.service
$ sudo systemctl reload peanut.service
```

`reload`는 단위가 다시 불러오기 작업을 정의하거나 지원할 때만 성공합니다. `restart`는 프로세스를 중단하며 서비스를 복원하지 못할 수 있습니다. 원격 접근, 네트워킹, 저장 장치 또는 인증에는 별도 콘솔 경로를 유지하고 작업 전에 설정을 검증하십시오.

상태와 로그를 확인합니다.

```bash
$ systemctl status peanut.service
$ systemctl is-active peanut.service
$ journalctl -u peanut.service -b
```

“활성”은 관리자 상태이며 모든 애플리케이션 엔드포인트가 정상이라는 증거는 아닙니다.

:::single-choice{#systemd-goals-start-peanut} 향후 활성화 상태를 바꾸지 않고 지금 `peanut.service`를 시작하는 명령은 무엇입니까?

::option[`sudo systemctl enable peanut.service`]{#systemd-goals-enable-only explanation="enable은 설치 링크를 변경하지만 `--now`와 결합하지 않으면 서비스를 시작하지 않습니다."}
::option[`sudo systemctl start peanut.service`]{#systemd-goals-start-command .correct explanation="start는 현재 런타임 활성화를 요청하며 활성화와 별개입니다."}
::option[`sudo systemctl daemon-reload peanut.service`]{#systemd-goals-daemon-reload-unit explanation="daemon-reload는 단위 활성화 피연산자를 받지 않으며 이 서비스를 시작하지 않습니다."}
:::

## 활성화, 비활성화 및 마스킹

향후 의존성 링크를 관리합니다.

```bash
$ sudo systemctl enable peanut.service
$ sudo systemctl disable peanut.service
```

enable은 `--now`를 추가하지 않으면 단위를 시작하지 않습니다. disable은 `--now`를 추가하지 않으면 실행 중인 단위를 중지하지 않습니다. 정적 단위는 설치 메타데이터가 없어도 다른 단위의 의존성으로 활성화될 수 있습니다.

마스킹은 단위를 `/dev/null`에 연결하고 마스크를 해제할 때까지 의존성 활성화를 포함한 일반 활성화를 차단합니다. disable보다 강하며 의존 항목을 손상시킬 수 있으므로 사용 전에 역방향 의존성을 검사하십시오.

:::single-choice{#systemd-goals-disable-runtime} `--now` 없이 `systemctl disable UNIT`을 실행하면 이미 실행 중인 서비스는 어떻게 됩니까?

::option[즉시 `SIGKILL`로 종료됩니다.]{#systemd-goals-disable-kills explanation="disable만으로는 현재 중지를 요청하지 않습니다."}
::option[실행 파일이 파일 시스템에서 삭제됩니다.]{#systemd-goals-disable-deletes explanation="활성화 작업은 프로그램 패키지 파일이 아니라 링크를 관리합니다."}
::option[향후 활성화 링크가 제거되지만 일반적으로 계속 실행됩니다.]{#systemd-goals-disable-keeps-running .correct explanation="런타임 상태와 설치 상태는 서로 다른 차원입니다."}
:::

## 서비스 결과 검증하기

변경 후 프로세스 상태, 최근 로그, 수신 엔드포인트, 의존 단위, 애플리케이션 상태 및 부팅 활성화가 바뀌었다면 제어된 재부팅 후 동작을 검증하십시오. 적절한 경우 `systemctl is-failed`, `systemctl list-dependencies` 및 애플리케이션 고유 검사를 사용합니다.

## 요약

이제 설정, 런타임 및 활성화를 혼동하지 않고 systemd 서비스를 관리할 수 있습니다.

1. `[Unit]`, `[Service]` 및 `[Install]`의 서로 다른 역할을 읽습니다.
2. 로드된 단위 상태와 설치된 단위 파일 상태를 비교합니다.
3. 드롭인을 사용하고 외부 파일 변경 후 관리자를 다시 불러옵니다.
4. 영향을 검토한 뒤에만 시작, 중지, 다시 불러오기 또는 재시작합니다.
5. enable, disable 및 mask를 서로 다른 영구 제어로 취급합니다.
