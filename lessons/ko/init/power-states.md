---
title: "전원 상태"
description: "Linux 시스템 전원 상태: shutdown, reboot, halt 명령을 배웁니다. Linux 시스템을 안전하게 전원 끄거나 재시작하는 방법을 이해합니다. 필수 명령으로 시작하세요!"
keywords: "Linux shutdown, reboot command, halt system, power off Linux, Linux commands, beginner Linux, Linux tutorial, system states"
---

## Lesson Content

명령줄을 통해 시스템 상태를 제어하는 방법을 아직 다루지 않았다는 것이 믿기지 않을 정도입니다. `init`에 대해 이야기할 때, 우리는 시스템을 시작하는 모드뿐만 아니라 시스템을 중지하는 모드에 대해서도 논의합니다.

시스템을 종료하려면:

```bash
sudo shutdown -h now
```

이 명령은 시스템을 정지 (전원 끄기) 시킵니다. 이 작업이 수행되기를 원하는 시간을 지정해야 합니다. 시스템을 해당 시간 후에 종료하도록 분 단위로 시간을 추가할 수 있습니다.

```bash
sudo shutdown -h +2
```

이것은 2 분 후에 시스템을 종료합니다. `shutdown` 명령으로 재시작할 수도 있습니다:

```bash
sudo shutdown -r now
```

또는 단순히 `reboot` 명령을 사용합니다:

```bash
sudo reboot
```

## Exercise

머신을 종료할 때 `init`에 무슨 일이 일어난다고 생각하십니까?

## Quiz Question

4 분 후에 시스템 전원을 끄는 명령은 무엇입니까?

## Quiz Answer

sudo shutdown -h +4
