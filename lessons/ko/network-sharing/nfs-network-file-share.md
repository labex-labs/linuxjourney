---
index: 4
lang: "ko"
title: "NFS"
meta_title: "NFS - 네트워크 공유"
meta_description: "Linux 에서 NFS 클라이언트 설정 및 자동 마운트에 대해 알아보세요. 네트워크 파일 공유에 연결하고 원활한 액세스를 위해 자동 마운트를 사용하는 방법을 이해하세요."
meta_keywords: "NFS 클라이언트, 자동 마운트, 네트워크 파일 시스템, Linux 네트워킹, mount 명령어, Linux 튜토리얼, 초보자"
---

## Lesson Content

Linux 에서 가장 표준적인 네트워크 파일 공유는 NFS(Network File System) 입니다. NFS 를 사용하면 서버가 네트워크를 통해 하나 이상의 클라이언트와 디렉터리 및 파일을 공유할 수 있습니다.

NFS 서버를 생성하는 방법은 복잡할 수 있으므로 자세히 다루지는 않겠지만, NFS 클라이언트를 설정하는 방법에 대해 설명하겠습니다.

### NFS 클라이언트 설정

```bash
sudo service nfsclient start
sudo mount server:/directory /mount_directory
```

### 자동 마운트

NFS 서버를 자주 사용하고 영구적으로 마운트된 상태로 유지하고 싶다고 가정해 봅시다. 일반적으로 `/etc/fstab` 파일을 편집할 것이라고 생각할 수 있지만, 서버에 항상 연결되지 않을 수도 있으며, 이는 부팅 시 문제를 일으킬 수 있습니다. 대신, 필요할 때 NFS 서버에 연결할 수 있도록 자동 마운트를 설정해야 합니다. 이는 **automount** 도구 또는 최신 버전의 Linux 에서는 **amd**를 사용하여 수행됩니다. 지정된 디렉터리의 파일에 액세스하면 automount 가 원격 서버를 찾아 자동으로 마운트합니다.

## Exercise

이 주제에 대한 특정 실습은 없지만, 관련 Linux 기술 및 개념을 연습하기 위해 포괄적인 [Linux 학습 경로](https://labex.io/ko/learn/linux)를 탐색하는 것을 권장합니다.

## Quiz Question

마운트 지점을 자동으로 관리하는 데 사용되는 도구는 무엇입니까?

## Quiz Answer

automount
