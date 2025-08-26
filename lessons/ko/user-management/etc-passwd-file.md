---
index: 3
lang: "ko"
title: "/etc/passwd"
meta_title: "/etc/passwd - 사용자 관리"
meta_description: "Linux 의 /etc/passwd 파일에 대해 배우고, 사용자 정보 필드와 UID 작동 방식을 이해합니다. 이 필수 구성 파일을 탐색합니다."
meta_keywords: "/etc/passwd, Linux 사용자, 사용자 ID, UID, Linux 튜토리얼, 초보자, 가이드, Linux 명령"
---

## Lesson Content

사용자 이름은 실제로 사용자를 식별하는 것이 아님을 기억하십시오. 시스템은 사용자 ID(UID) 를 사용하여 사용자를 식별합니다. 어떤 사용자가 어떤 ID 에 매핑되는지 알아보려면 `/etc/passwd` 파일을 살펴보십시오.

```bash
cat /etc/passwd
```

이 파일은 사용자 목록과 그들에 대한 자세한 정보를 보여줍니다. 예를 들어, 이 파일의 첫 번째 줄은 다음과 같을 것입니다:

```plaintext
root:x:0:0:root:/root:/bin/bash
```

각 줄은 한 사용자에 대한 사용자 정보를 표시합니다. 가장 일반적으로 root 사용자가 첫 번째 줄에 표시됩니다. 콜론으로 구분된 많은 필드가 사용자에게 대한 추가 정보를 알려줍니다. 모두 살펴보겠습니다:

1. **사용자 이름**
2. **사용자 비밀번호** - 비밀번호는 실제로 이 파일에 저장되지 않습니다. 일반적으로 `/etc/shadow` 파일에 저장됩니다. 다음 단원에서 `/etc/shadow`에 대해 더 자세히 논의하겠지만, 지금은 암호화된 사용자 비밀번호를 포함하고 있다는 것을 알아두십시오. 이 필드에서 다양한 기호를 볼 수 있습니다: "x"가 보이면 비밀번호가 `/etc/shadow` 파일에 저장되어 있다는 의미입니다. "*"는 사용자가 로그인 액세스 권한이 없다는 의미입니다. 필드가 비어 있으면 사용자가 비밀번호를 가지고 있지 않다는 의미입니다.
3. **사용자 ID** - 보시다시피, root 는 UID 0 을 가집니다.
4. **그룹 ID**
5. **GECOS 필드** - 실제 이름이나 전화번호와 같이 사용자 또는 계정에 대한 주석을 남기는 데 일반적으로 사용됩니다. 쉼표로 구분됩니다.
6. **사용자의 홈 디렉토리**
7. **사용자의 셸** - 많은 사용자가 셸로 bash 를 기본값으로 사용하는 것을 볼 수 있을 것입니다.

일반적으로 사용자의 설정 페이지에서는 사람 사용자만 볼 수 있을 것으로 예상할 것입니다. 그러나 `/etc/passwd`에는 다른 사용자가 포함되어 있음을 알 수 있습니다. 사용자는 실제로 다른 권한으로 프로세스를 실행하기 위해 시스템에 존재한다는 것을 기억하십시오. 때로는 미리 결정된 권한으로 프로세스를 실행하고 싶을 때가 있습니다. 예를 들어, `daemon` 사용자는 데몬 프로세스에 사용됩니다.

또한, `vipw` 도구를 사용하여 사용자를 추가하고 정보를 수정하려면 `/etc/passwd` 파일을 직접 편집할 수 있다는 점에 유의해야 합니다. 그러나 `useradd` 및 `userdel`과 같이 나중에 논의할 도구에 맡기는 것이 가장 좋습니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 사용자 계정 및 관리에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[useradd, usermod, userdel 로 Linux 사용자 계정 관리](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성 및 보안 설정부터 수정 및 삭제에 이르기까지 사용자 관리의 전체 수명 주기를 연습합니다.
2. **[groupadd, usermod, groupdel 로 Linux 그룹 관리](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 새 그룹 생성 및 사용자 멤버십 수정 등 그룹 관리를 위한 핵심 명령줄 유틸리티를 직접 경험해 봅니다.
3. **[Linux 에서 사용자 계정 및 Sudo 권한 구성](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Linux 시스템의 보안을 강화하기 위한 사용자 계정 및 sudo 권한 관리의 필수 기술을 배웁니다.

이러한 랩은 실제 시나리오에서 사용자 ID 및 계정 관리 개념을 적용하고 Linux 사용자 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

사용자가 로그인 액세스 권한이 없는 경우, `/etc/passwd`에서 어떻게 표시됩니까?

## Quiz Answer

*
