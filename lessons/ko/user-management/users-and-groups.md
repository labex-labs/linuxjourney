---
index: 1
lang: "ko"
title: "사용자 및 그룹"
meta_title: "사용자 및 그룹 - 사용자 관리"
meta_description: "Linux 사용자 및 그룹에 대해 알아보고, UID, GID, 그리고 root 사용자를 이해합니다. sudo 명령을 사용하여 권한을 높이는 방법을 알아봅니다. Linux 여정을 시작하세요!"
meta_keywords: "Linux 사용자, Linux 그룹, sudo 명령, root 사용자, Linux 권한, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

모든 전통적인 운영 체제에는 사용자 (user) 와 그룹 (group) 이 있습니다. 이들은 오직 접근 및 권한을 위해 존재합니다. 프로세스를 실행할 때, 해당 프로세스는 Jane 이든 Bob 이든 그 프로세스의 소유자로 실행됩니다. 파일 접근 및 소유권 또한 권한에 따라 달라집니다. Jane 이 Bob 의 문서를 보거나 그 반대의 경우를 원하지 않을 것입니다.

각 사용자는 사용자별 파일이 저장되는 자신만의 홈 디렉터리를 가집니다. 이는 일반적으로 `/home/username`에 위치하지만, 배포판에 따라 다를 수 있습니다.

시스템은 사용자 ID(UID) 를 사용하여 사용자를 관리합니다. 사용자 이름은 사용자를 식별하는 친숙한 방법이지만, 시스템은 UID 로 사용자를 식별합니다. 시스템은 또한 그룹을 사용하여 권한을 관리합니다. 그룹은 해당 그룹에 의해 설정된 권한을 가진 사용자들의 집합이며, 시스템은 그룹 ID(GID) 로 이들을 식별합니다.

Linux 에서는 시스템을 사용하는 일반적인 사람 외에도 사용자가 있습니다. 때로는 이러한 사용자가 시스템 기능을 유지하기 위해 지속적으로 프로세스를 실행하는 시스템 데몬입니다. 가장 중요한 사용자 중 하나는 `root` 또는 `superuser`입니다. `root`는 시스템에서 가장 강력한 사용자입니다. `root`는 모든 파일에 접근할 수 있고 모든 프로세스를 시작하고 종료할 수 있습니다. 이러한 이유로, 항상 `root`로 작업하는 것은 위험할 수 있습니다. 시스템에 중요한 파일을 실수로 제거할 수도 있습니다. 다행히도, `root` 접근이 필요하고 사용자가 `root` 접근 권한을 가지고 있다면, `sudo` 명령을 사용하여 `root`로 명령을 실행할 수 있습니다. `sudo` 명령 (superuser do) 은 `root` 접근 권한으로 명령을 실행하는 데 사용됩니다. 사용자가 `root` 접근 권한을 어떻게 얻는지에 대해서는 나중에 더 자세히 다룰 것입니다.

`/etc/shadow`와 같이 보호된 파일을 보려고 시도해 보세요:

```bash
cat /etc/shadow
```

권한 거부 오류가 발생하는 것을 확인하세요. 다음 명령으로 권한을 확인해 보세요:

```bash
$ ls -la /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

아직 권한에 대해 다루지는 않았지만, 여기서 일어나는 일은 `root`가 파일의 소유자이며, 내용을 읽으려면 `root` 접근 권한이 있거나 `shadow` 그룹의 일부여야 한다는 것입니다. 이제 `sudo`로 명령을 실행해 보세요:

```bash
sudo cat /etc/shadow
```

이제 파일의 내용을 볼 수 있을 것입니다!

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 사용자, 그룹 및 `sudo`에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[useradd, usermod, userdel 로 Linux 사용자 계정 관리](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성 및 보안 설정부터 수정 및 삭제에 이르기까지 사용자 관리의 전체 수명 주기를 연습합니다.
2. **[groupadd, usermod, groupdel 로 Linux 그룹 관리](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 새 그룹 생성, 사용자 멤버십 수정, 그룹 제거를 포함하여 그룹 관리를 위한 핵심 명령줄 유틸리티를 직접 경험합니다.
3. **[Linux 에서 사용자 계정 및 Sudo 권한 구성](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 관리 권한 부여를 포함하여 Linux 시스템의 보안을 강화하기 위한 사용자 계정 및 `sudo` 권한 관리의 필수 기술을 배웁니다.

이러한 랩은 사용자 및 그룹 관리 개념과 `sudo` 사용을 실제 시나리오에 적용하고 Linux 시스템 관리 능력을 향상시키는 데 도움이 될 것입니다.

## Quiz Question

`root`로 실행하기 위해 어떤 명령을 사용합니까?

## Quiz Answer

sudo
