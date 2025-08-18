---
index: 2
lang: "ko"
title: "rsync"
meta_title: "rsync - 네트워크 공유"
meta_description: "효율적인 Linux 파일 동기화 및 백업을 위해 rsync 를 배우세요. rsync 명령어와 옵션을 사용하여 원격 및 로컬 데이터 전송을 이해하세요. Linux 기술을 향상시키세요!"
meta_keywords: "rsync, Linux 파일 전송, 데이터 백업, 파일 동기화, Linux 튜토리얼, rsync 명령어, 초보자, 가이드"
---

## Lesson Content

다른 호스트에서 데이터를 복사하는 데 사용되는 또 다른 도구는 rsync(원격 동기화의 약자) 입니다. rsync 는 scp 와 매우 유사하지만 큰 차이점이 있습니다. rsync 는 복사하려는 데이터가 이미 있는지 미리 확인하고 차이점만 복사하는 특수 알고리즘을 사용합니다. 예를 들어, 파일을 복사하는 도중에 네트워크 연결이 끊겨 복사가 중단되었다고 가정해 봅시다. rsync 는 처음부터 모든 것을 다시 복사하는 대신 복사되지 않은 부분만 복사합니다.

또한 체크섬을 사용하여 복사하는 파일의 무결성을 확인합니다. 이러한 작은 최적화를 통해 파일 전송 유연성이 향상되며, rsync 는 원격 및 로컬 디렉터리 동기화, 데이터 백업, 대용량 데이터 전송 등에 이상적입니다.

자주 사용되는 rsync 옵션:

- v - 상세 출력
- r - 디렉터리 재귀
- h - 사람이 읽을 수 있는 출력
- z - 더 쉬운 전송을 위해 압축, 느린 연결에 적합

### Copy/sync files on the same host

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### Copy/sync files to local host from a remote host

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### Copy/sync files to a remote host from a local host

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

rsync 를 사용하여 디렉터리를 다른 디렉터리로 동기화하십시오. 중요한 디렉터리를 덮어쓰지 않도록 주의하십시오!

## Quiz Question

데이터 백업에 유용한 명령어는 무엇입니까?

## Quiz Answer

rsync
