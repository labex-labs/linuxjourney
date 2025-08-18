---
lang: "ko"
title: "소유권 권한"
meta_title: "소유권 권한 - 권한"
meta_description: "chown 및 chgrp 명령을 사용하여 Linux 에서 파일 소유권을 변경하는 방법을 배웁니다. 이 초보자 친화적인 Linux 튜토리얼을 통해 사용자 및 그룹 권한을 이해합니다."
meta_keywords: "chown, chgrp, Linux 파일 소유권, Linux 권한, Linux 명령, 초보자 Linux, Linux 튜토리얼, Linux 가이드"
---

## Lesson Content

파일의 권한을 수정하는 것 외에도, 파일의 그룹 및 사용자 소유권을 수정할 수 있습니다.

### Modify user ownership

```bash
sudo chown patty myfile
```

이 명령은 `myfile`의 소유자를 `patty`로 설정합니다.

### Modify group ownership

```bash
sudo chgrp whales myfile
```

이 명령은 `myfile`의 그룹을 `whales`로 설정합니다.

### Modify both user and group ownership at the same time

사용자 뒤에 콜론과 그룹 이름을 추가하면 사용자 및 그룹을 동시에 설정할 수 있습니다.

```bash
sudo chown patty:whales myfile
```

## Exercise

일부 테스트 파일의 그룹과 사용자를 수정하십시오. 그 후에 `ls -l` 명령으로 권한을 확인하십시오.

## Quiz Question

사용자 소유권을 변경하는 데 사용하는 명령은 무엇입니까?

## Quiz Answer

chown
