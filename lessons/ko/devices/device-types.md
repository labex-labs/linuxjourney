---
index: 2
lang: "ko"
title: "장치 유형"
meta_title: "장치 유형 - 장치"
meta_description: "Linux 장치 유형 (문자, 블록, 파이프, 소켓) 과 `ls -l /dev`를 사용하여 식별하는 방법을 배웁니다. 주/부 장치 번호를 이해합니다. 초보자를 위한 Linux 튜토리얼."
meta_keywords: "Linux 장치 유형, ls -l /dev, 문자 장치, 블록 장치, 주 부 장치 번호, Linux 튜토리얼, Linux 가이드, 초보자"
---

## Lesson Content

장치가 어떻게 관리되는지 이야기하기 전에, 실제로 몇 가지 장치를 살펴보겠습니다.

```bash
$ ls -l /dev
brw-rw----   1 root disk      8,   0 Dec 20 20:13 sda
crw-rw-rw-   1 root root      1,   3 Dec 20 20:13 null
srw-rw-rw-   1 root root           0 Dec 20 20:13 log
prw-r--r--   1 root root           0 Dec 20 20:13 fdata
```

열은 왼쪽에서 오른쪽으로 다음과 같습니다:

- Permissions
- Owner
- Group
- Major Device Number
- Minor Device Number
- Timestamp
- Device Name

`ls` 명령에서 각 줄의 첫 번째 비트로 파일 유형을 확인할 수 있다는 것을 기억하십시오. 장치 파일은 다음과 같이 표시됩니다:

- c - character
- b - block
- p - pipe
- s - socket

### 문자 장치

이 장치들은 한 번에 한 문자씩 데이터를 전송합니다. 많은 의사 장치 (`/dev/null`) 를 문자 장치로 볼 수 있습니다. 이 장치들은 실제로 물리적으로 기계에 연결되어 있지 않지만, 운영 체제에 더 큰 기능을 제공합니다.

### 블록 장치

이 장치들은 고정된 크기의 큰 블록으로 데이터를 전송합니다. 하드 드라이브, 파일 시스템 등과 같이 데이터 블록을 활용하는 장치들을 블록 장치로 가장 흔하게 볼 수 있습니다.

### 파이프 장치

명명된 파이프는 두 개 이상의 프로세스가 서로 통신할 수 있도록 합니다. 이는 문자 장치와 유사하지만, 출력이 장치로 전송되는 대신 다른 프로세스로 전송됩니다.

### 소켓 장치

소켓 장치는 파이프 장치와 유사하게 프로세스 간의 통신을 용이하게 하지만, 한 번에 여러 프로세스와 통신할 수 있습니다.

### 장치 특성화

장치는 **주 장치 번호 (major device number)**와 **부 장치 번호 (minor device number)**의 두 가지 숫자를 사용하여 특성화됩니다. 위의 `ls` 예제에서 이 숫자들을 볼 수 있으며, 쉼표로 구분되어 있습니다. 예를 들어, 장치 번호가 **8, 0**인 장치가 있다고 가정해 봅시다:

주 장치 번호는 사용되는 장치 드라이버를 나타내며, 이 경우 8 은 종종 sd 블록 장치의 주 번호입니다. 부 번호는 커널에 이 드라이버 클래스에서 어떤 고유한 장치인지 알려줍니다. 이 경우 0 은 첫 번째 장치 (a) 를 나타내는 데 사용됩니다.

## Exercise

연습하면 완벽해집니다! 다음은 Linux 장치 파일 및 해당 관리에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 파티션 및 파일 시스템 관리](https://labex.io/ko/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Linux 의 기본 블록 장치인 디스크 파티션 및 파일 시스템을 생성하고 관리하는 연습을 합니다.
2. **[Linux 에서 하드웨어 장치 탐색](https://labex.io/ko/labs/comptia-explore-hardware-devices-in-linux-590861)** - 다양한 하드웨어 장치를 식별하고 검사하여 `/dev` 디렉터리에서 어떻게 표현되는지 이해하는 방법을 배웁니다.
3. **[Linux 에서 스왑 파일 생성 및 활성화](https://labex.io/ko/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - 가상 메모리 장치로 작동하는 스왑 파일을 생성하고 활성화하는 실습 경험을 얻습니다.

이 실습들은 실제 시나리오에서 장치 상호 작용 및 관리 개념을 적용하고 Linux 시스템 관리 능력을 향상시키는 데 도움이 될 것입니다.

## Quiz Question

`ls -l` 명령에서 문자 장치를 나타내는 기호는 무엇입니까?

## Quiz Answer

c
