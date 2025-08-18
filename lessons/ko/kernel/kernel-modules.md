---
index: 6
lang: "ko"
title: "커널 모듈"
meta_title: "커널 모듈 - Kernel"
meta_description: "Linux 커널 모듈에 대해 배우고, 로드, 언로드 및 관리하는 방법을 익힙니다. 커널 기능을 확장하기 위한 `modprobe` 및 `lsmod` 명령어를 이해합니다. Linux 여정을 시작하세요!"
meta_keywords: "Linux 커널 모듈, modprobe, lsmod, 커널 관리, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

제가 멋진 차를 가지고 있다고 가정해 봅시다. 저는 그 차에 많은 시간과 돈을 투자합니다. 스포일러, 히치, 자전거 랙 및 기타 여러 가지를 추가합니다. 이러한 구성 요소는 실제로 자동차의 핵심 기능을 변경하지 않으며, 매우 쉽게 제거하고 추가할 수 있습니다. 커널도 커널 모듈에 동일한 개념을 사용합니다.

커널 자체는 모놀리식 소프트웨어입니다. 새로운 유형의 키보드에 대한 지원을 추가하고 싶을 때, 이 코드를 커널 코드에 직접 작성하지 않습니다. 마치 자전거 랙을 자동차에 용접하지 않는 것과 같습니다 (물론 어떤 사람들은 그렇게 할 수도 있습니다). 커널 모듈은 필요에 따라 커널에 로드하고 언로드할 수 있는 코드 조각입니다. 이를 통해 핵심 커널 코드에 실제로 추가하지 않고도 커널의 기능을 확장할 수 있습니다. 또한 모듈을 추가하고 시스템을 재부팅할 필요가 없습니다 (대부분의 경우).

### 현재 로드된 모듈 목록 보기

```bash
lsmod
```

### 모듈 로드

```bash
sudo modprobe bluetooth
```

`modprobe`는 `/lib/modules/(kernel version)/kernel/drivers`에서 모듈을 로드합니다. 커널 모듈은 종속성을 가질 수도 있습니다. `modprobe`는 아직 로드되지 않은 경우 모듈 종속성을 로드합니다.

### 모듈 제거

```bash
sudo modprobe -r bluetooth
```

### 부팅 시 로드

`modprobe`로 임시로 로드하는 대신 (재부팅 시 언로드됨) 시스템 부팅 중에 모듈을 로드할 수도 있습니다. `/etc/modprobe.d` 디렉토리를 수정하고 다음과 같이 구성 파일을 추가하면 됩니다:

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

options peanut_butter type=almond
```

다소 기이한 예시이지만, `peanut_butter`라는 모듈이 있고 `type=almond`에 대한 커널 매개변수를 추가하고 싶다면, 이 구성 파일을 사용하여 시작 시 로드할 수 있습니다. 또한 커널 모듈에는 자체 커널 매개변수가 있으므로, 자세한 내용을 알아보려면 해당 모듈에 대해 특별히 읽어봐야 합니다.

### 부팅 시 로드하지 않음

다음과 같이 구성 파일을 추가하여 모듈이 부팅 시 로드되지 않도록 할 수도 있습니다:

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

blacklist peanut_butter
```

## Exercise

`modprobe`를 사용하여 Bluetooth 모듈을 언로드하고 어떤 일이 발생하는지 확인하십시오. 어떻게 해결하시겠습니까?

## Quiz Question

모듈을 언로드하는 데 사용되는 명령어는 무엇입니까?

## Quiz Answer

modprobe -r
