---
lang: "ko"
title: "장치 유형"
meta_title: "장치 유형 - 장치"
meta_description: "Linux 장치 유형 (character, block, pipe, socket) 과 `ls -l /dev`를 사용하여 이를 식별하는 방법을 배웁니다. major/minor 장치 번호를 이해합니다. 초보자를 위한 Linux 튜토리얼입니다."
meta_keywords: "Linux 장치 유형, ls -l /dev, character device, block device, major minor device number, Linux 튜토리얼, Linux 가이드, 초보자"
---

## Lesson Content

장치 관리 방법에 대해 이야기하기 전에, 몇 가지 장치를 살펴보겠습니다.

```bash
$ ls -l /dev
brw-rw----   1 root disk      8,   0 Dec 20 20:13 sda
crw-rw-rw-   1 root root      1,   3 Dec 20 20:13 null
srw-rw-rw-   1 root root           0 Dec 20 20:13 log
prw-r--r--   1 root root           0 Dec 20 20:13 fdata
```

왼쪽에서 오른쪽으로 열은 다음과 같습니다:

- Permissions
- Owner
- Group
- Major Device Number
- Minor Device Number
- Timestamp
- Device Name

`ls` 명령에서 각 줄의 첫 번째 비트로 파일 유형을 확인할 수 있습니다. 장치 파일은 다음과 같이 표시됩니다:

- c - character
- b - block
- p - pipe
- s - socket

### Character Device

이 장치들은 데이터를 한 번에 한 문자씩 전송합니다. `/dev/null`과 같은 많은 의사 (pseudo) 장치들을 character device 로 볼 수 있습니다. 이 장치들은 실제로 물리적으로 기계에 연결되어 있지 않지만, 운영 체제에 더 큰 기능을 제공합니다.

### Block Device

이 장치들은 데이터를 고정된 크기의 큰 블록으로 전송합니다. 하드 드라이브, 파일 시스템 등과 같이 데이터 블록을 활용하는 장치들을 block device 로 가장 흔하게 볼 수 있습니다.

### Pipe Device

명명된 파이프 (Named pipes) 는 두 개 이상의 프로세스가 서로 통신할 수 있도록 합니다. 이는 character device 와 유사하지만, 출력이 장치로 전송되는 대신 다른 프로세스로 전송됩니다.

### Socket Device

Socket device 는 pipe device 와 유사하게 프로세스 간의 통신을 용이하게 하지만, 동시에 여러 프로세스와 통신할 수 있습니다.

### Device Characterization

장치는 **major device number**와 **minor device number**라는 두 가지 숫자를 사용하여 특성화됩니다. 이 숫자들은 위 `ls` 예제에서 쉼표로 구분되어 있는 것을 볼 수 있습니다. 예를 들어, 장치에 **8, 0**이라는 장치 번호가 있다고 가정해 봅시다:

major device number 는 사용되는 장치 드라이버를 나타내며, 이 경우 8 은 종종 sd block device 의 major number 입니다. minor number 는 커널에 이 드라이버 클래스에서 어떤 고유한 장치인지 알려줍니다. 이 경우 0 은 첫 번째 장치 (a) 를 나타내는 데 사용됩니다.

## Exercise

`/dev` 디렉토리를 살펴보고 어떤 유형의 장치를 볼 수 있는지 확인하십시오.

## Quiz Question

`ls -l` 명령에서 character device 를 나타내는 기호는 무엇입니까?

## Quiz Answer

c
