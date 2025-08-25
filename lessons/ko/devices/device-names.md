---
index: 3
lang: "ko"
title: "장치 이름"
meta_title: "장치 이름 - 장치"
meta_description: "SCSI(sd), 의사, PATA(hd) 장치와 같은 Linux 장치 이름을 배웁니다. 이 초보자 친화적인 가이드에서 /dev/sda, /dev/null 등을 이해하세요."
meta_keywords: "Linux 장치 이름, /dev, SCSI 장치, 의사 장치, PATA 장치, Linux 튜토리얼, 초보자 Linux, 장치 파일"
---

## Lesson Content

다음은 가장 일반적으로 접하게 될 장치 이름입니다:

### SCSI 장치

시스템에 어떤 종류의 대용량 저장 장치가 있다면, 그것은 SCSI("스커지"로 발음) 프로토콜을 사용하고 있을 가능성이 높습니다. SCSI 는 Small Computer System Interface 의 약자입니다. 이는 디스크, 프린터, 스캐너 및 기타 주변 장치와 시스템 간의 통신을 허용하는 데 사용되는 프로토콜입니다. 현대 시스템에서는 실제로 사용되지 않는 SCSI 장치에 대해 들어보셨을 수도 있습니다. 그러나 Linux 시스템은 SCSI 디스크를 `/dev`의 하드 디스크 드라이브와 연결합니다. 이들은 `sd` (SCSI 디스크) 접두사로 표시됩니다:

일반적인 SCSI 장치 파일:

- `/dev/sda` - 첫 번째 하드 디스크
- `/dev/sdb` - 두 번째 하드 디스크
- `/dev/sda3` - 첫 번째 하드 디스크의 세 번째 파티션

### 의사 장치

앞서 논의했듯이, 의사 장치는 실제로 시스템에 물리적으로 연결되어 있지 않습니다. 가장 일반적인 의사 장치는 문자 장치입니다:

- `/dev/zero` - 모든 입력을 수락하고 버리며, NULL(0 값) 바이트의 연속 스트림을 생성합니다.
- `/dev/null` - 모든 입력을 수락하고 버리며, 출력을 생성하지 않습니다.
- `/dev/random` - 난수를 생성합니다.

### PATA 장치

오래된 시스템에서는 하드 드라이브가 `hd` 접두사로 참조되는 것을 볼 수 있습니다:

- `/dev/hda` - 첫 번째 하드 디스크
- `/dev/hdd2` - 네 번째 하드 디스크의 두 번째 파티션

## Exercise

연습은 완벽을 만듭니다! 다음은 Linux 장치 이름 및 저장소 관리에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 파티션 및 파일 시스템 관리](https://labex.io/ko/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 파티션 생성, 포맷 및 마운트를 연습하여 장치 이름과 직접적으로 작업합니다.
2. **[Linux 에서 하드웨어 장치 탐색](https://labex.io/ko/labs/comptia-explore-hardware-devices-in-linux-590861)** - Linux 환경 내에서 다양한 하드웨어 장치와 관련 이름을 식별하고 검사하는 방법을 배웁니다.

이러한 랩은 실제 시나리오에 개념을 적용하고 Linux 에서 저장소를 관리하고 하드웨어를 이해하는 데 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

두 번째 SCSI 디스크의 첫 번째 파티션에 대한 장치 이름은 일반적으로 무엇입니까?

## Quiz Answer

sdb1
