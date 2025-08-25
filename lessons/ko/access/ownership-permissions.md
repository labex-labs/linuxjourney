---
index: 3
lang: "ko"
title: "소유권 권한"
meta_title: "소유권 권한 - 권한"
meta_description: "chown 및 chgrp 명령을 사용하여 Linux 에서 파일 소유권을 변경하는 방법을 배웁니다. 이 초보자 친화적인 Linux 튜토리얼을 통해 사용자 및 그룹 권한을 이해하세요."
meta_keywords: "chown, chgrp, Linux 파일 소유권, Linux 권한, Linux 명령, 초보자 Linux, Linux 튜토리얼, Linux 가이드"
---

## Lesson Content

파일의 권한을 수정하는 것 외에도 파일의 그룹 및 사용자 소유권을 수정할 수 있습니다.

### 사용자 소유권 수정

```bash
sudo chown patty myfile
```

이 명령은 `myfile`의 소유자를 `patty`로 설정합니다.

### 그룹 소유권 수정

```bash
sudo chgrp whales myfile
```

이 명령은 `myfile`의 그룹을 `whales`로 설정합니다.

### 사용자 및 그룹 소유권을 동시에 수정

사용자 뒤에 콜론과 그룹 이름을 추가하면 사용자 및 그룹을 동시에 설정할 수 있습니다.

```bash
sudo chown patty:whales myfile
```

## Exercise

연습은 완벽을 만듭니다! 다음은 파일 소유권 및 권한에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 사용자 그룹 및 파일 권한](https://labex.io/ko/labs/linux-linux-user-group-and-file-permissions-18002)** - 파일 권한 이해 및 파일 소유권 조작을 포함하여 필수 Linux 사용자 및 그룹 관리 개념을 배웁니다. 이 랩은 다중 사용자 Linux 환경을 보호하는 실질적인 경험을 제공합니다.
2. **[새 사용자 및 그룹 추가](https://labex.io/ko/labs/linux-add-new-user-and-group-17987)** - 이 챌린지에서는 새 사용자 계정을 생성하고, 사용자 지정 그룹을 설정하고, 그룹 멤버십을 관리하여 서버 환경에 새 팀원을 추가하는 것을 시뮬레이션합니다. 이는 Linux 사용자 및 그룹 관리 기술을 테스트할 것입니다.

이 랩은 실제 시나리오에 개념을 적용하고 Linux 에서 파일 소유권 및 권한을 관리하는 데 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

사용자 소유권을 변경하는 데 사용하는 명령은 무엇입니까?

## Quiz Answer

chown
