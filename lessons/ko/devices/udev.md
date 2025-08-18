---
index: 5
lang: "ko"
title: "udev"
meta_title: "udev - 장치"
meta_description: "udev 가 Linux 장치 파일을 동적으로 관리하는 방법과 udevadm 사용법을 배웁니다. 초보자를 위한 장치 노드 생성에 대해 이해합니다."
meta_keywords: "udev, udevadm, Linux 장치 관리, 장치 파일, Linux 튜토리얼, 초보자 Linux, udev 규칙, Linux 가이드"
---

## Lesson Content

예전에는, 그리고 정말 원한다면 오늘날에도 다음과 같은 명령을 사용하여 장치 노드를 생성했습니다:

```bash
mknod /dev/sdb1 b 8 3
```

이 명령은 `/dev/sdb1` 장치 노드를 생성하고, 주 번호 8 과 부 번호 3 을 가진 블록 장치 (b) 로 만듭니다.

장치를 제거하려면 `/dev` 디렉터리에서 장치 파일을 단순히 **rm**하면 됩니다.

다행히도 udev 덕분에 더 이상 이 작업을 할 필요가 없습니다. udev 시스템은 장치 연결 여부에 따라 장치 파일을 동적으로 생성하고 제거합니다. 시스템에서 실행 중인 `udevd` 데몬이 있으며, 이 데몬은 시스템에 연결된 장치에 대한 커널의 메시지를 수신합니다. `Udevd`는 해당 정보를 파싱하고 `/etc/udev/rules.d`에 지정된 규칙과 데이터를 일치시킵니다. 이러한 규칙에 따라 장치 노드와 심볼릭 링크를 생성할 가능성이 높습니다. 자신만의 udev 규칙을 작성할 수 있지만, 이 수업의 범위를 벗어납니다. 다행히도 시스템에는 이미 많은 udev 규칙이 포함되어 있으므로 자신만의 규칙을 작성할 필요가 없을 수도 있습니다.

**udevadm** 명령을 사용하여 udev 데이터베이스와 sysfs 를 볼 수도 있습니다. 이 도구는 매우 유용하지만 때로는 매우 복잡할 수 있습니다. 장치 정보를 보는 간단한 명령은 다음과 같습니다:

```bash
udevadm info --query=all --name=/dev/sda
```

## Exercise

제공된 `udevadm` 명령을 실행하고 출력을 확인하십시오.

## Quiz Question

무엇이 장치를 동적으로 추가하고 제거합니까?

## Quiz Answer

udev
