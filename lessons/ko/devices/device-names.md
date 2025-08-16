---
title: "장치 이름"
description: "SCSI (sd), pseudo, PATA (hd) 장치와 같은 Linux 장치 이름을 배웁니다. 이 초보자 친화적인 가이드에서 /dev/sda, /dev/null 등을 이해합니다."
keywords: "Linux 장치 이름, /dev, SCSI 장치, pseudo 장치, PATA 장치, Linux 튜토리얼, 초보자 Linux, 장치 파일"
---

## Lesson Content

다음은 가장 일반적으로 접하게 될 장치 이름입니다:

### SCSI Devices

머신에 대용량 저장 장치가 있다면, 아마도 SCSI("스커지"로 발음) 프로토콜을 사용하고 있을 것입니다. SCSI 는 Small Computer System Interface 의 약자입니다. 이는 디스크, 프린터, 스캐너 및 기타 주변 장치와 시스템 간의 통신을 허용하는 데 사용되는 프로토콜입니다. 현대 시스템에서는 실제로 사용되지 않는 SCSI devices 에 대해 들어보셨을 수 있습니다. 그러나 Linux 시스템은 `/dev`에서 SCSI disks 를 하드 디스크 드라이브와 연결합니다. 이들은 `sd` (SCSI disk) 접두사로 표시됩니다:

일반적인 SCSI device files:

- `/dev/sda` - 첫 번째 하드 디스크
- `/dev/sdb` - 두 번째 하드 디스크
- `/dev/sda3` - 첫 번째 하드 디스크의 세 번째 파티션

### Pseudo Devices

앞서 논의했듯이, pseudo devices 는 실제로 시스템에 물리적으로 연결되어 있지 않습니다. 가장 일반적인 pseudo devices 는 character devices 입니다:

- `/dev/zero` - 모든 입력을 수락하고 버리며, NULL (0 값) 바이트의 연속 스트림을 생성합니다
- `/dev/null` - 모든 입력을 수락하고 버리며, 출력을 생성하지 않습니다
- `/dev/random` - 난수를 생성합니다

### PATA Devices

때때로 오래된 시스템에서는 `hd` 접두사로 참조되는 하드 드라이브를 볼 수 있습니다:

- `/dev/hda` - 첫 번째 하드 디스크
- `/dev/hdd2` - 네 번째 하드 디스크의 두 번째 파티션

## Exercise

pseudo devices 에 기록하여 어떤 일이 발생하는지 확인하십시오. 디스크를 해당 장치에 기록하지 않도록 주의하십시오!

## Quiz Question

두 번째 SCSI 디스크의 첫 번째 파티션에 대한 장치 이름은 일반적으로 무엇입니까?

## Quiz Answer

sdb1
