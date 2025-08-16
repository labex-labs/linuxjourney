---
title: "파일 공유 개요"
description: "Linux 파일 공유 및 scp(secure copy) 명령에 대해 알아보세요. 네트워크의 호스트 간에 파일을 전송하세요. 이 초보자 친화적인 가이드로 시작하세요!"
keywords: "Linux 파일 공유, scp 명령, 보안 복사, 네트워크 파일 전송, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

네트워크에 있는 컴퓨터가 사용자 혼자만 있는 경우는 드뭅니다. 특히 상업 환경에서 작업하는 경우 더욱 그렇습니다. 한 컴퓨터에서 다른 컴퓨터로 데이터를 전송해야 할 때, 때로는 USB 드라이브를 연결하여 수동으로 복사하는 것이 더 쉬울 수 있습니다. 하지만 대부분의 경우, 동일한 네트워크에 있는 컴퓨터들과 작업할 때는 네트워크 파일 공유를 통해 데이터를 전송합니다.

이 과정에서는 네트워크의 다른 컴퓨터 간에 데이터를 복사하는 몇 가지 다른 방법을 다룰 것입니다. 간단한 파일 복사를 논의한 다음, 별도의 드라이브처럼 작동하는 전체 디렉토리를 컴퓨터에 마운트하는 것에 대해 이야기할 것입니다.

간단한 파일 공유 도구 중 하나는 **scp** 명령입니다. scp 명령은 secure copy 의 약자입니다. cp 명령과 정확히 동일하게 작동하지만, 동일한 네트워크의 한 호스트에서 다른 호스트로 복사할 수 있도록 해줍니다. ssh 를 통해 작동하므로, 모든 작업은 ssh 와 동일한 인증 및 보안을 사용합니다.

### 로컬 호스트에서 원격 호스트로 파일 복사하기

```bash
scp myfile.txt username@remotehost.com:/remote/directory
```

### 원격 호스트에서 로컬 호스트로 파일 복사하기

```bash
scp username@remotehost.com:/remote/directory/myfile.txt /local/directory
```

### 로컬 호스트에서 원격 호스트로 디렉토리 복사하기

```bash
scp -r mydir username@remotehost.com:/remote/directory
```

## Exercise

scp 를 사용하여 한 컴퓨터에서 다른 컴퓨터로 파일을 복사해 보십시오.

## Quiz Question

한 호스트에서 다른 호스트로 파일을 안전하게 복사하는 데 사용할 수 있는 명령은 무엇입니까?

## Quiz Answer

scp
