---
index: 4
lang: "ko"
title: "커널 로깅"
meta_title: "커널 로깅 - 로깅"
meta_description: "dmesg 및 kern.log 를 사용하여 Linux 커널 로깅에 대해 알아보세요. 부팅 메시지 및 하드웨어 문제를 이해하세요. 시스템 통찰력을 위해 커널 로그를 탐색하세요."
meta_keywords: "dmesg, kern.log, Linux 로깅, 커널 메시지, 부팅 로그, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

### /var/log/dmesg

부팅 시 시스템은 커널 링 버퍼에 대한 정보를 기록합니다. 이는 하드웨어 드라이버, 커널 정보, 부팅 중 상태 등에 대한 정보를 보여줍니다. 이 로그 파일은 `/var/log/dmesg`에서 찾을 수 있으며, 부팅할 때마다 재설정됩니다. 지금은 이 파일의 유용성을 느끼지 못할 수도 있지만, 부팅 중 문제나 하드웨어 문제가 발생할 경우 `dmesg`가 가장 먼저 확인해야 할 곳입니다. `dmesg` 명령어를 사용하여 이 로그를 볼 수도 있습니다.

### /var/log/kern.log

커널 정보를 볼 수 있는 또 다른 로그는 `/var/log/kern.log` 파일입니다. 이 파일은 시스템의 커널 정보와 이벤트를 기록하며, `dmesg` 출력도 기록합니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 사용자 및 그룹 관리에 대한 이해를 강화하기 위한 실습입니다.

1. **[useradd, usermod, userdel 을 사용하여 Linux 사용자 계정 관리](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성 및 보안 설정부터 수정 및 삭제까지 사용자 관리의 전체 수명 주기를 연습합니다.
2. **[groupadd, usermod, groupdel 을 사용하여 Linux 그룹 관리](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 새 그룹 생성, 사용자 멤버십 수정, 그룹 제거를 포함하여 그룹 관리를 위한 핵심 명령줄 유틸리티를 직접 경험합니다.
3. **[Linux 에서 사용자 계정 및 Sudo 권한 구성](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 암호 정책 적용 및 관리 권한 부여를 포함하여 Linux 시스템의 보안을 강화하기 위한 사용자 계정 및 sudo 권한 관리의 필수 기술을 배웁니다.

이 실습들은 실제 시나리오에 개념을 적용하고 Linux 에서 사용자 및 그룹 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

커널 부팅 메시지를 확인하는 데 사용할 수 있는 명령어는 무엇입니까?

## Quiz Answer

dmesg
