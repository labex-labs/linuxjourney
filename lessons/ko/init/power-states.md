---
index: 7
lang: "ko"
title: "전원 상태"
meta_title: "전원 상태 - Init"
meta_description: "Linux 시스템 전원 상태: 종료, 재부팅 및 정지 명령을 배웁니다. Linux 시스템을 안전하게 전원 끄거나 다시 시작하는 방법을 이해합니다. 필수 명령으로 시작하세요!"
meta_keywords: "Linux 종료, 재부팅 명령, 시스템 정지, Linux 전원 끄기, Linux 명령, 초보자 Linux, Linux 튜토리얼, 시스템 상태"
---

## Lesson Content

명령줄을 통해 시스템 상태를 제어하는 방법에 대해 아직 논의하지 않았다는 것이 믿기지 않습니다. `init`에 대해 이야기할 때, 우리는 시스템을 시작하는 모드뿐만 아니라 시스템을 중지하는 모드에 대해서도 논의합니다.

시스템을 종료하려면:

```bash
sudo shutdown -h now
```

이 명령은 시스템을 정지 (전원 끄기) 합니다. 이 작업이 수행될 시간을 지정해야 합니다. 시스템을 해당 시간만큼 후에 종료하도록 분 단위로 시간을 추가할 수 있습니다.

```bash
sudo shutdown -h +2
```

이것은 2 분 후에 시스템을 종료합니다. `shutdown` 명령으로 다시 시작할 수도 있습니다:

```bash
sudo shutdown -r now
```

또는 단순히 `reboot` 명령을 사용합니다:

```bash
sudo reboot
```

## Exercise

이 주제에 대한 특정 랩은 없지만, 관련 Linux 기술 및 개념을 연습하기 위해 포괄적인 [Linux 학습 경로](https://labex.io/ko/learn/linux)를 탐색하는 것을 권장합니다.

## Quiz Question

4 분 후에 시스템 전원을 끄는 명령은 무엇입니까?

## Quiz Answer

sudo shutdown -h +4
