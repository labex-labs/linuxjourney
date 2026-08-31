---
lesson_id: "network-file-sharing"
course_id: "network-sharing"
lang: "ko"
order_index: 1
title: "파일 공유 개요"
description: "SSH 기반 파일 전송 방식을 선택하고 scp로 안전하게 복사하는 방법을 알아봅니다."
meta_title: "파일 공유 개요 - 네트워크 공유"
meta_description: "리눅스 파일 공유와 scp 명령을 사용한 안전한 네트워크 파일 전송 방법을 알아봅니다."
meta_keywords: "리눅스 파일 공유, scp 명령, 보안 복사, 리눅스 명령어, 네트워크 파일 전송"
---

네트워크 파일 이동은 일회성 복사부터 계속 마운트되는 공유와 동기화된 디렉터리 트리까지 다양합니다. 방향, 데이터 크기, 갱신 빈도, 신원 모델, 네트워크 신뢰도, 메타데이터 요구 사항 및 클라이언트에 실시간 공유 접근이 필요한지를 기준으로 방식을 선택하십시오.

## 전송 방식 선택하기

- `scp` 또는 SFTP는 SSH로 인증된 복사나 대화형 전송을 제공합니다.
- `rsync`는 로컬 또는 SSH 같은 전송 수단을 통해 디렉터리 트리를 효율적으로 동기화합니다.
- NFS는 서버 내보내기를 마운트된 파일시스템으로 제공하며 유닉스 계열 호스트 사이에서 흔히 사용됩니다.
- 리눅스에서 Samba로 구현되는 SMB는 여러 운영체제에 걸친 공유 접근을 지원합니다.
- HTTP는 간단한 다운로드를 제공할 수 있지만 일반적인 마운트 파일시스템은 아닙니다.

복사본이 자동으로 백업이 되는 것은 아닙니다. 백업 설계에는 독립적인 보존, 복원 테스트, 무결성 검사 및 같은 삭제나 침해로부터의 보호도 필요합니다.

:::single-choice{#file-sharing-one-time-ssh-copy}
SSH를 통한 일회성 파일 복사에 적합한 도구는 무엇입니까?

::option[`scp`]{#file-sharing-scp .correct explanation="SCP는 파일 복사에 SSH 인증과 전송을 사용합니다."}
::option[`uptime`]{#file-sharing-uptime explanation="uptime은 파일을 전송하는 대신 호스트 가동 시간과 부하를 보고합니다."}
::option[`logrotate`]{#file-sharing-logrotate explanation="logrotate는 호스트의 파일 로그 세대를 관리합니다."}
:::

## scp 경로 이해하기

일반적인 형식은 `scp SOURCE DESTINATION`입니다. 원격 피연산자는 보통 `user@host:path` 형식을 사용합니다.

```bash
$ scp -- report.txt alice@example.net:/srv/incoming/
$ scp -- alice@example.net:/srv/outgoing/result.txt ./result.txt
```

첫째 명령은 로컬 파일을 원격으로 보내고, 둘째 명령은 원격 파일을 로컬로 가져옵니다. 콜론은 원격 호스트와 그 경로를 구분합니다. 셸에 특별한 의미가 있는 문자를 포함한 경로는 따옴표로 감싸고 신뢰할 수 없는 모호한 파일 이름을 피하십시오.

:::single-choice{#file-sharing-scp-pull-source}
`scp`로 파일을 가져올 때 원격 명세는 어디에 나타납니까?

::option[로컬 대상 앞의 소스로 나타납니다.]{#file-sharing-pull-source .correct explanation="복사 방향은 소스에서 대상으로 이어지는 피연산자 순서를 따릅니다."}
::option[모든 옵션 뒤의 로컬 대상으로 나타납니다.]{#file-sharing-pull-destination explanation="가져올 원격 객체는 소스 피연산자입니다."}
::option[사용자의 SSH 설정 파일 안에만 나타납니다.]{#file-sharing-pull-config explanation="SSH 설정에서 기본값을 제공할 수 있지만 복사할 원격 경로는 여전히 피연산자입니다."}
:::

## 디렉터리 복사하기

디렉터리 트리에는 재귀 모드를 사용합니다.

```bash
$ scp -r -- project/ alice@example.net:/srv/incoming/
```

복사 전에 데이터 크기, 심볼릭 링크, 권한, 소유권 요구 사항, 여유 공간 및 대상 이름을 조사합니다. SCP는 동기화 정책이 아닙니다. 디렉터리를 반복해서 복사하면 소스에서 사라진 파일이 대상에 남을 수 있습니다.

:::single-choice{#file-sharing-scp-recursive}
`scp -r`은 무엇을 요청합니까?

::option[복사 전에 원격 대상을 제거합니다.]{#file-sharing-scp-remove explanation="재귀 모드는 디렉터리를 순회하며 정리 정책을 정의하지 않습니다."}
::option[디렉터리 트리를 재귀적으로 복사합니다.]{#file-sharing-scp-tree .correct explanation="선택한 소스가 디렉터리일 때 필요한 플래그입니다."}
::option[SSH 설정에 읽기 전용으로 접근합니다.]{#file-sharing-scp-readonly explanation="이 옵션은 설정 접근이 아니라 디렉터리 순회와 관련됩니다."}
:::

## 신원과 결과 검증하기

SSH 호스트 키 검증은 잘못된 서버에 연결하는 일을 막아 줍니다. 호스트 키가 변경됐다는 경고를 우회하지 말고 신뢰할 수 있는 경로로 확인해야 할 사건으로 다루십시오. 최소 권한 계정과 환경에 맞는 키 관리 방식을 사용합니다.

전송 후에는 종료 상태, 예상 파일, 크기, 메타데이터를 확인하고 무결성 요구 사항이 있다면 양쪽에서 독립적으로 계산한 해시를 비교합니다. 대상 애플리케이션이 실제로 데이터를 읽을 수 있는지도 확인하십시오.

:::single-choice{#file-sharing-host-key-change}
SSH가 예상치 못한 호스트 키 변경을 보고하면 어떻게 해야 합니까?

::option[앞으로 모든 전송에서 호스트 키 검사를 비활성화합니다.]{#file-sharing-disable-checking explanation="중요한 서버 신원 제어를 제거하는 행동입니다."}
::option[계속하기 전에 신뢰할 수 있는 소스를 통해 새 키를 검증합니다.]{#file-sharing-verify-key .correct explanation="경고는 호스트 재구축, 잘못된 대상 또는 가로채기를 나타낼 수 있으므로 조사해야 합니다."}
::option[명령 출력에 개인 인증 키를 공개합니다.]{#file-sharing-publish-key explanation="개인 자격 증명은 노출하면 안 됩니다."}
:::

## 요약

이제 안전한 일회성 네트워크 파일 복사를 선택하고 검증할 수 있습니다.

1. 접근 및 보존 요구 사항에 맞는 공유 방식을 선택합니다.
2. 로컬 및 원격 `scp` 피연산자를 소스와 대상으로 구분합니다.
3. 디렉터리 트리에는 재귀 모드를 신중하게 사용합니다.
4. 서버 신원, 전송 결과 및 대상에서의 사용 가능성을 검증합니다.
