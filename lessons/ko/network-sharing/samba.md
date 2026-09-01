---
lesson_id: "samba"
course_id: "network-sharing"
lang: "ko"
order_index: 5
title: "Samba"
description: "기본 Samba 파일 공유를 설정하고 검증하며 접근하고 보호하는 방법을 알아봅니다."
meta_title: "Samba - 네트워크 공유"
meta_description: "리눅스에서 Samba 네트워크 공유를 설정하는 방법을 알아봅니다. Samba 프로토콜, 설치, 설정 및 SMB 리눅스 클라이언트 연결을 설명합니다."
meta_keywords: "Samba, 리눅스 SMB, Samba 네트워크, Samba 프로토콜, 파일 공유, smb.conf, cifs, smbclient"
---

Samba는 유닉스 계열 시스템에 Server Message Block 프로토콜을 구현해 리눅스, Windows, macOS 및 기타 클라이언트가 파일과 프린터를 공유할 수 있게 합니다. 현대 배포에서는 최신 SMB 방언을 사용합니다. 이전 용어인 CIFS가 리눅스 클라이언트 도구에 여전히 보이지만, 이를 오래된 SMB1을 활성화해야 한다는 뜻으로 해석하면 안 됩니다.

## 공유 계획하기

Samba를 설치하거나 변경하기 전에 승인된 클라이언트, 신원, 읽기 및 쓰기 요구 사항, 네트워크 영역, 데이터 소유자, 백업 정책 및 필요한 SMB 방언을 정의합니다. 홈이나 시스템 트리를 실수로 노출하지 말고 전용 디렉터리를 사용하십시오.

접근은 Samba 정책과 하위 파일시스템 권한이 함께 제어합니다. `smb.conf`에서 쓰기를 허용해도 파일시스템 접근 권한이 없는 계정에 권한을 부여할 수는 없습니다.

:::single-choice{#samba-two-permission-layers} 사용자가 Samba 공유를 통해 쓰려면 무엇이 허용해야 합니까?

::option[공유에 표시되는 설명만 허용하면 됩니다.]{#samba-comment-permission explanation="설명은 안내 문구이며 접근 권한을 부여하지 않습니다."}
::option[Samba 규칙과 파일시스템 권한이 모두 허용해야 합니다.]{#samba-policy-and-filesystem .correct explanation="요청은 프로토콜 수준 규칙과 로컬 파일시스템 권한 부여를 모두 통과해야 합니다."}
::option[클라이언트의 바탕 화면 설정만 허용하면 됩니다.]{#samba-wallpaper explanation="클라이언트 모양 설정은 서버 파일을 제어하지 않습니다."}
:::

## 기본 공유 정의하기

주 설정 파일은 일반적으로 `/etc/samba/smb.conf`입니다. 제한적인 예시는 다음과 같습니다.

```ini
[team]
    path = /srv/samba/team
    browseable = yes
    read only = no
    valid users = @teamshare
```

디렉터리를 만들고 유닉스 그룹에 대해 검토한 소유권과 권한을 적용합니다.

```bash
$ sudo install -d -o root -g teamshare -m 2770 /srv/samba/team
```

set-group-ID 비트는 새 항목이 디렉터리 그룹을 상속하는 데 도움이 되지만 공동 접근에는 ACL이나 신중하게 선택한 생성 마스크도 필요할 수 있습니다. 상속만으로 충분하다고 가정하지 말고 실제 파일과 디렉터리 결과를 테스트하십시오.

:::single-choice{#samba-valid-users} `valid users = @teamshare`는 무엇을 나타냅니까?

::option[모든 익명 네트워크 사용자에게 쓰기 권한을 부여합니다.]{#samba-every-anonymous explanation="이 규칙은 게스트 쓰기를 활성화하는 대신 접근을 제한합니다."}
::option[서버가 공유 이름을 teamshare로 변경해야 합니다.]{#samba-rename-share explanation="표시되는 공유 이름은 섹션 이름 [team]으로 유지됩니다."}
::option[지정한 그룹의 구성원만 이 공유 규칙에서 허용됩니다.]{#samba-valid-group .correct explanation="@ 형식은 Samba 사용자 목록 구문에서 그룹을 나타냅니다."}
:::

## 신원 설정하기

독립형 Samba 설정에서 계정에는 일반적으로 대응하는 유닉스 신원과 활성화된 Samba 자격 증명이 필요합니다.

```bash
$ sudo smbpasswd -a alice
```

디렉터리 도메인 배포에서는 다른 신원 설계를 사용합니다. 암호를 셸 기록이나 관련 없는 사용자가 읽을 수 있는 설정에 두지 말고, Samba 암호가 유닉스 계정 암호와 자동으로 같다고 가정하지 마십시오.

:::single-choice{#samba-password-database} 독립형 서버에서 `smbpasswd -a alice`는 일반적으로 무엇을 합니까?

::option[유닉스 사용자의 홈 디렉터리를 삭제합니다.]{#samba-delete-home explanation="이 명령은 Samba 자격 증명을 관리하며 홈 디렉터리를 제거하지 않습니다."}
::option[계정의 Samba 자격 증명을 추가하거나 초기화합니다.]{#samba-add-credential .correct explanation="SMB 인증 데이터베이스는 단순히 유닉스 사용자를 만드는 작업과 별도로 관리됩니다."}
::option[Alice 사용자로 보이는 모든 SMB 공유를 마운트합니다.]{#samba-mount-all explanation="서버 자격 증명 등록과 클라이언트 마운트는 별개입니다."}
:::

## 설정 검증 및 적용하기

서비스를 다시 불러오기 전에 파싱된 설정을 확인합니다.

```bash
$ testparm -s
```

예상하지 못한 기본값과 오류를 검토한 다음 배포판의 서비스 관리자를 통해 Samba 서비스를 다시 불러옵니다. 서비스 이름은 다르며 흔히 `smbd.service` 또는 `smb.service`입니다. 지원된다면 다시 불러오기가 재시작보다 영향이 적지만 상태, 수신 소켓, 방화벽 범위 및 로그도 검증해야 합니다.

명시적인 사용자를 지정해 클라이언트에서 테스트합니다.

```bash
$ smbclient //server.example.net/team -U alice
```

:::single-choice{#samba-testparm-purpose} Samba 변경을 적용하기 전에 `testparm -s`를 실행하는 이유는 무엇입니까?

::option[모든 공유 파일을 백업 서버로 복사합니다.]{#samba-testparm-backup explanation="이 도구는 공유 데이터를 복사하는 대신 설정을 파싱하고 보고합니다."}
::option[실제 적용되는 Samba 설정을 검증하고 표시합니다.]{#samba-testparm-validate .correct explanation="파서 출력은 서비스에 영향을 주기 전에 설정 오류를 포착하고 해석된 설정을 보여 줍니다."}
::option[모든 클라이언트에 관리자 권한을 부여합니다.]{#samba-testparm-admin explanation="검증은 클라이언트 권한 부여를 변경하지 않습니다."}
:::

## 리눅스에서 마운트하기

리눅스 클라이언트는 일반적으로 `cifs` 파일시스템 드라이버와 마운트 도우미를 사용합니다. 명령줄 인수는 기록이나 프로세스 조사로 노출될 수 있으므로 암호를 직접 넣지 마십시오. root만 읽을 수 있는 자격 증명 파일이나 승인된 자격 증명 메커니즘을 사용합니다.

```bash
$ sudo mount -t cifs //server.example.net/team /mnt/team \
    -o credentials=/root/.smb-team,vers=3.1.1
```

자격 증명 파일을 보호하고 양쪽이 지원하는 방언을 확인하며 UID, GID, 권한 및 암호화 요구 사항을 명시적으로 정의합니다. 마운트 후 `findmnt`로 검증하고 승인된 읽기 및 쓰기 테스트를 수행한 다음 활성 사용자를 조율한 뒤 언마운트합니다.

:::single-choice{#samba-command-line-password} 마운트 명령에 `password=...`를 직접 쓰면 안 되는 이유는 무엇입니까?

::option[기록이나 프로세스 인수를 통해 비밀 정보가 노출될 수 있습니다.]{#samba-password-exposure .correct explanation="보호된 자격 증명 소스는 우발적인 공개를 줄이지만 권한도 신중하게 설정해야 합니다."}
::option[SMB는 어떤 암호 인증도 지원하지 않습니다.]{#samba-no-passwords explanation="다른 신원 시스템도 있지만 암호 기반 SMB 인증은 흔히 사용됩니다."}
::option[이 옵션이 공유를 영구적으로 읽기 전용으로 만듭니다.]{#samba-password-readonly explanation="비밀 정보의 위치는 쓰기 정책을 결정하지 않습니다."}
:::

## 요약

이제 프로토콜과 파일시스템 보안을 모두 고려해 Samba 공유를 설정할 수 있습니다.

1. 클라이언트, 신원, 네트워크 범위 및 데이터 정책을 먼저 정의합니다.
2. 공유를 제한하고 하위 파일시스템 권한을 일치시킵니다.
3. 올바른 신원 모델로 Samba 자격 증명을 관리합니다.
4. `testparm`으로 검증하고 종단 간 클라이언트 테스트를 수행합니다.
5. 클라이언트 자격 증명을 보호하고 마운트된 접근을 검증합니다.
