---
index: 7
lang: "ko"
title: "dd"
meta_title: "dd - 장치"
meta_description: "Linux dd 명령을 사용하여 데이터 복사 및 디스크 이미징에 대해 알아보세요. if, of, bs 와 같은 옵션을 이해하세요. Linux 데이터 관리 여정을 시작하세요!"
meta_keywords: "dd command, Linux dd, copy data, disk imaging, Linux tutorial, beginner, guide, data backup"
---

## Lesson Content

`dd` 도구는 데이터를 변환하고 복사하는 데 매우 유용합니다. 파일 또는 데이터 스트림에서 입력을 읽어 파일 또는 데이터 스트림에 씁니다.

다음 명령을 고려하십시오:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1024
```

이 명령은 `backup.img`의 내용을 `/dev/sdb`로 복사합니다. 더 이상 복사할 데이터가 없을 때까지 1024 바이트 블록으로 데이터를 복사합니다.

- `if=file` - 입력 파일; 표준 입력 대신 파일에서 읽습니다.
- `of=file` - 출력 파일; 표준 출력 대신 파일에 씁니다.
- `bs=bytes` - 블록 크기; 한 번에 이 바이트 수만큼 데이터를 읽고 씁니다. 킬로바이트는 `k`, 메가바이트는 `m` 등으로 크기를 나타내어 다른 크기 단위를 사용할 수 있습니다. 따라서 1024 바이트는 1k 입니다.
- `count=number` - 복사할 블록 수.

`count` 옵션을 사용하는 일부 `dd` 명령을 볼 수 있습니다. 일반적으로 `dd`를 사용하여 1 메가바이트 파일을 복사하려면 복사가 완료되었을 때 해당 파일이 1 메가바이트로 표시되기를 원할 것입니다. 다음 명령을 실행한다고 가정해 봅시다:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1M count=2
```

`backup.img` 파일은 10M 이지만, 이 명령에서는 1M 를 2 번 복사하라고 지시하고 있으므로 2M 만 복사되어 복사된 데이터가 불완전하게 됩니다. `count`는 여러 상황에서 유용할 수 있지만, 단순히 데이터를 복사하는 경우에는 `count`는 물론 `bs`도 생략할 수 있습니다. 데이터 전송을 정말로 최적화하려면 이러한 옵션을 사용하기 시작해야 합니다.

`dd`는 매우 강력합니다. 전체 디스크 드라이브를 포함한 모든 것의 백업을 만들고, 디스크 이미지를 복원하는 등 다양한 용도로 사용할 수 있습니다. 조심하세요. 무엇을 하는지 확실하지 않다면 강력한 도구가 대가를 치르게 할 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 에서 데이터 조작 및 디스크 관리에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[tar 를 사용하여 Linux 에서 백업 생성 및 복원](https://labex.io/ko/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - `dd`도 사용할 수 있는 데이터 무결성 및 복구와 관련된 중요한 기술인 파일 시스템 백업 생성 및 복원을 연습합니다.
2. **[Linux 파티션 및 파일 시스템 관리](https://labex.io/ko/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - `dd`와 같은 도구를 사용하여 디스크 이미징 작업을 할 때 기본 개념인 디스크 파티션 및 파일 시스템 생성, 포맷, 마운트를 포함한 관리를 배웁니다.

이러한 랩은 실제 시나리오에서 데이터 처리 및 디스크 작업 개념을 적용하고 시스템 관리 작업에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

블록 크기에 대한 `dd` 옵션은 무엇입니까?

## Quiz Answer

bs
