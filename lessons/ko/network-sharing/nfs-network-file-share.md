---
lesson_id: "nfs-network-file-share"
course_id: "network-sharing"
lang: "ko"
order_index: 4
title: "NFS"
description: "NFS 클라이언트 마운트를 찾고, 마운트하고, 검증하며, 안전하게 자동화하는 방법을 알아봅니다."
meta_title: "NFS - 네트워크 공유"
meta_description: "리눅스에서 NFS를 사용하는 방법을 알아봅니다. NFS 클라이언트 설정, mount 명령 및 네트워크 공유 자동 마운트를 설명합니다."
meta_keywords: "NFS, NFS 클라이언트, 자동 마운트, 네트워크 파일 시스템, 리눅스 네트워킹, mount 명령"
---

네트워크 파일 시스템(NFS)을 사용하면 클라이언트가 로컬 파일시스템 네임스페이스를 통해 서버 내보내기에 접근할 수 있습니다. 서버는 내보내기와 접근 정책 대부분을 제어하고, 클라이언트는 승인된 내보내기를 어디에 언제 마운트할지 제어합니다.

## 클라이언트 준비하기

배포판의 NFS 클라이언트 유틸리티를 설치합니다. Debian 계열에서는 보통 `nfs-common`, Red Hat 계열에서는 `nfs-utils` 패키지입니다. DNS 또는 주소 연결, 허용된 NFS 버전, 방화벽 정책 및 정확한 내보내기 경로를 서버 관리자와 확인하십시오.

`showmount -e SERVER`는 이전 마운트 프로토콜을 통해 제공되는 내보내기를 나열할 수 있지만 모든 NFSv4 전용 서버에 대해 권위 있는 결과를 제공하지는 않습니다. 목록 조회 실패가 승인된 NFSv4 내보내기가 없음을 입증하지는 않습니다.

:::single-choice{#nfs-showmount-limit}
`showmount -e`가 NFSv4 서버에서 불완전할 수 있는 이유는 무엇입니까?

::option[공개되지 않을 수 있는 이전 내보내기 목록 프로토콜을 조회하기 때문입니다.]{#nfs-showmount-protocol .correct explanation="NFSv4는 별도의 목록 서비스를 제공하지 않고도 작동할 수 있습니다."}
::option[로컬 CPU 온도만 표시하기 때문입니다.]{#nfs-showmount-temperature explanation="이 명령은 NFS 서버의 내보내기 정보와 관련됩니다."}
::option[나열한 모든 내보내기를 영구적으로 비활성화하기 때문입니다.]{#nfs-showmount-disables explanation="목록 조회는 읽기 전용 탐색 요청입니다."}
:::

## 내보내기 마운트하기

비어 있는 전용 마운트 지점을 만들고 승인된 내보내기를 마운트합니다.

```bash
$ sudo mkdir -p /mnt/team
$ sudo mount -t nfs server.example.net:/srv/team /mnt/team
```

정책이나 호환성 때문에 필요할 때만 `-o vers=4.2`처럼 버전을 지정합니다. 성능이나 보안 옵션을 추측해서 설정하지 마십시오. 결과 소스, 유형 및 옵션을 확인합니다.

```bash
$ findmnt --target /mnt/team
```

:::single-choice{#nfs-mount-operands}
mount 명령에서 `server.example.net:/srv/team`은 무엇입니까?

::option[원격 내보내기를 가리는 로컬 디렉터리입니다.]{#nfs-local-mountpoint explanation="예제의 로컬 마운트 지점은 /mnt/team입니다."}
::option[설치할 클라이언트 패키지 이름입니다.]{#nfs-package-name explanation="패키지 이름은 배포판에 따라 다르며 마운트 소스 피연산자가 아닙니다."}
::option[서버와 내보낸 원격 경로입니다.]{#nfs-remote-export .correct explanation="호스트와 콜론 뒤의 경로가 NFS 소스를 식별합니다."}
:::

## 신원과 권한 이해하기

NFS 접근에는 서버 내보내기 규칙, 프로토콜 보안, 숫자 신원 또는 디렉터리 서비스 및 파일시스템 권한이 함께 작용합니다. 두 호스트에서 표시되는 사용자 이름이 같아도 숫자 ID가 일치한다고 보장할 수 없습니다. 전통적인 `AUTH_SYS`는 클라이언트가 제공한 숫자 신원을 보내며 신뢰할 수 있는 클라이언트와 네트워크 제어에 크게 의존합니다. 더 강한 보안이 필요한 환경에서는 종단 간 설정된 Kerberos 보안 모드를 사용할 수 있습니다.

서버는 일반적으로 root 스쿼싱을 통해 원격 root를 권한 없는 신원에 매핑합니다. 권한 오류를 해결하려고 이 보호를 무작정 비활성화하지 말고 ID, 디렉터리 소유권, 내보내기 정책 및 의도한 보안 모델을 조사하십시오.

:::single-choice{#nfs-name-versus-id}
표시되는 이름이 같은 두 사용자가 서로 다른 NFS 권한을 받을 수 있는 이유는 무엇입니까?

::option[NFS 권한이 숫자 신원 매핑에 따라 달라질 수 있기 때문입니다.]{#nfs-numeric-mapping .correct explanation="이름만 같다고 클라이언트와 서버가 같은 UID와 그룹으로 해석한다는 보장은 없습니다."}
::option[NFS가 모든 파일시스템 권한을 무시하기 때문입니다.]{#nfs-ignores-permissions explanation="파일시스템 및 내보내기 권한도 여전히 권한 부여의 일부입니다."}
::option[모든 마운트가 서버의 계정 데이터베이스를 자동으로 변경하기 때문입니다.]{#nfs-changes-accounts explanation="클라이언트 마운트는 서버의 신원을 다시 쓰지 않습니다."}
:::

## 네트워크 마운트 자동화하기

일반적인 부팅 시점의 `/etc/fstab` 마운트는 네트워크나 서버를 사용할 수 없을 때 시작을 지연할 수 있습니다. 호스트에 따라 `autofs`의 주문형 맵이나 `_netdev,nofail,x-systemd.automount` 같은 systemd 마운트 옵션을 사용하되 정확한 의미를 테스트하십시오.

```fstab
server.example.net:/srv/team /mnt/team nfs4 rw,_netdev,nofail,x-systemd.automount 0 0
```

fstab을 편집하기 전에 복구 접근 경로를 보존하고 비파괴적 파서나 통제된 마운트 테스트로 검증합니다. 자동 마운트는 가용성 동작을 개선하지만 권한 부여, DNS 또는 서버 장애를 해결하지는 않습니다.

:::single-choice{#nfs-automount-benefit}
NFS 공유를 주문형으로 자동 마운트할 때의 주요 이점은 무엇입니까?

::option[모든 클라이언트에 내보내기의 root 접근 권한을 부여합니다.]{#nfs-automount-root explanation="마운트 시점은 서버 권한 부여를 우회하지 않습니다."}
::option[초기 부팅 중 서버가 반드시 사용 가능하지 않아도 됩니다.]{#nfs-automount-boot .correct explanation="초기 시작을 막는 대신 접근할 때 연결이 시작됩니다."}
::option[서버 파일시스템 전체를 로컬 디스크에 복사합니다.]{#nfs-automount-copy explanation="마운트는 원격 접근을 제공하며 완전한 로컬 복사가 아닙니다."}
:::

## 언마운트 및 검증

언마운트 전에 공유를 사용하는 프로세스를 중지하거나 조율하고 애플리케이션 작업이 모두 기록되게 합니다. 그런 다음 마운트 지점을 언마운트하고 사라졌는지 확인합니다.

```bash
$ sudo umount /mnt/team
$ findmnt --target /mnt/team
```

강제 또는 지연 언마운트는 활성 참조를 숨기고 애플리케이션 오류를 일으킬 수 있습니다. 원인을 진단한 장애에 명시적인 복구 계획이 있을 때만 사용하십시오.

:::single-choice{#nfs-safe-unmount}
일반적인 NFS 언마운트 전에 무엇을 해야 합니까?

::option[공유를 사용하는 프로세스를 조율하고 중요한 쓰기를 완료합니다.]{#nfs-coordinate-writers .correct explanation="사용 중인 파일시스템을 애플리케이션에서 제거하면 I/O가 중단되거나 작업이 미완료 상태로 남을 수 있습니다."}
::option[서버의 내보내기 디렉터리를 삭제합니다.]{#nfs-delete-export explanation="클라이언트 언마운트에 서버 데이터 삭제는 필요하지 않습니다."}
::option[모든 클라이언트 네트워크 인터페이스를 비활성화합니다.]{#nfs-disable-network explanation="정상적인 완료를 더 어렵게 만들 수 있으며 일반적인 순서가 아닙니다."}
:::

## 요약

이제 신원과 가용성 가정을 명시한 NFS 클라이언트 마운트를 운영할 수 있습니다.

1. 클라이언트 도구, 내보내기 경로, 프로토콜 및 네트워크 정책을 확인합니다.
2. 전용 경로에 마운트하고 실제 소스와 옵션을 검증합니다.
3. 신원 및 내보내기 정책을 통해 권한 문제를 진단합니다.
4. 부팅 가용성이 중요할 때 테스트한 주문형 마운트를 사용합니다.
5. 사용자를 조율하고 정상적으로 언마운트한 뒤 제거 여부를 확인합니다.
