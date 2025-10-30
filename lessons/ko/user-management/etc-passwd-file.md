---
index: 3
lang: "ko"
title: "/etc/passwd"
meta_title: "/etc/passwd - 사용자 관리"
meta_description: "리눅스 /etc/passwd 파일에 대한 종합 가이드. 사용자 데이터 필드 해석 방법, UID 이해, root:x:0:0:root:/root:/bin/bash 와 같은 예시를 학습합니다."
meta_keywords: "/etc/passwd, 리눅스 /etc/passwd, root:x:0:0:root:/root:/bin/bash, 사용자 ID, UID, 사용자 관리, 리눅스 튜토리얼"
---

## Lesson Content

Linux 에서는 사용자 이름이 사람이 읽을 수 있는 레이블이지만, 시스템은 고유한 사용자 ID(UID) 로 사용자를 식별합니다. 사용자 이름과 UID 간의 매핑은 사용자 관리에 중요한 구성 요소인 `/etc/passwd` 파일에 저장됩니다.

내용을 보려면 간단한 명령어를 사용할 수 있습니다:

```bash
cat /etc/passwd
```

이 파일은 모든 시스템 사용자와 그들에 대한 자세한 정보를 표시합니다. 각 줄은 단일 사용자 계정을 나타냅니다.

### /etc/passwd 필드 분석

이 파일의 일반적인 한 줄, 종종 첫 번째 줄은 다음과 같이 보입니다:

```plaintext
root:x:0:0:root:/root:/bin/bash
```

`root` 사용자에 대한 이 항목은 콜론 (`:`) 으로 구분된 일곱 개의 필드를 포함합니다. Linux 에서 `/etc/passwd`의 구조를 이해하는 것이 사용자 관리의 핵심입니다. 각 필드를 분석해 보겠습니다:

1.  **사용자 이름 (Username)**: 사용자의 로그인 이름 (예: `root`).
2.  **암호 (Password)**: 사용자의 암호화된 암호를 위한 자리 표시자입니다. 보안상의 이유로 실제 암호는 여기에 저장되지 않습니다.
    - `x`는 암호화된 암호가 `/etc/shadow` 파일에 있음을 나타냅니다.
    - `*`(별표) 는 계정이 잠겨서 로그인에 사용할 수 없음을 의미합니다.
    - 빈 필드는 사용자가 암호가 없음을 의미합니다.
3.  **사용자 ID (UID)**: 사용자의 고유한 숫자 식별자입니다. `root` 사용자는 항상 UID 가 `0`입니다.
4.  **그룹 ID (GID)**: 사용자의 기본 그룹에 대한 숫자 식별자입니다.
5.  **GECOS 필드**: 전통적으로 사용자의 전체 이름, 전화번호 또는 사무실 위치와 같은 추가 정보를 담는 주석 필드입니다. 쉼표로 구분됩니다.
6.  **홈 디렉토리 (Home Directory)**: 사용자의 홈 디렉토리에 대한 절대 경로입니다 (예: `/root`).
7.  **기본 셸 (Default Shell)**: 사용자의 기본 명령줄 인터프리터로, 로그인 시 실행됩니다 (예: `/bin/bash`).

### 시스템 사용자 및 특수 계정

`/etc/passwd` 파일을 검사하면 인간 사용자가 아닌 많은 계정을 발견할 수 있습니다. 이들은 시스템 보안을 강화하기 위해 제한된 권한으로 특정 서비스나 프로세스를 실행하는 데 사용되는 시스템 계정입니다. 예를 들어, `daemon` 사용자는 백그라운드 데몬 프로세스를 실행하는 데 사용됩니다.

### /etc/passwd 파일 편집

기술적으로 텍스트 편집기나 `vipw` 명령어를 사용하여 `/etc/passwd` 파일을 직접 편집할 수 있지만, 이는 강력히 권장되지 않습니다. 수동 편집은 구문 오류를 쉽게 유발하여 시스템 접근이 차단되거나 시스템 불안정을 초래할 수 있습니다.

사용자 계정을 관리할 때는 항상 `useradd`, `usermod`, `userdel`과 같은 전용 명령줄 유틸리티를 사용하는 것이 더 안전하고 안정적입니다. 이러한 도구는 파일을 올바르게 수정하고 관련 구성을 모두 처리하도록 설계되었습니다.

## Exercise

지식을 공고히 하기 위해 다음 실습을 시도해 보세요. 이는 실제 시나리오에서 사용자 ID 및 계정 관리 개념을 적용하고 Linux 사용자 관리에 대한 자신감을 구축하는 데 도움이 될 것입니다.

1.  **[useradd, usermod 및 userdel 을 사용하여 Linux 사용자 계정 관리](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성 및 보안부터 수정 및 삭제에 이르기까지 사용자 관리의 전체 수명 주기를 연습합니다.
2.  **[groupadd, usermod 및 groupdel 을 사용하여 Linux 그룹 관리](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 새 그룹 생성 및 사용자 멤버십 수정 등 그룹 관리를 위한 핵심 명령줄 유틸리티에 대한 실습 경험을 얻습니다.
3.  **[Linux 에서 사용자 계정 및 Sudo 권한 구성](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Linux 시스템 보안 강화를 위해 사용자 계정 및 sudo 권한을 관리하는 필수 기술을 배웁니다.

## Quiz Question

사용자 계정이 잠겨서 로그인에 사용할 수 없는 경우, `/etc/passwd` 파일의 암호 필드에 어떻게 표시됩니까? 필요한 문자만 사용하여 답하십시오.

## Quiz Answer

-
