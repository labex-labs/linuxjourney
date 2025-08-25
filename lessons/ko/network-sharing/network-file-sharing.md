---
index: 1
lang: "ko"
title: "파일 공유 개요"
meta_title: "파일 공유 개요 - 네트워크 공유"
meta_description: "Linux 파일 공유 및 scp(secure copy) 명령에 대해 알아보세요. 네트워크의 호스트 간에 파일을 전송하세요. 이 초보자 친화적인 가이드로 시작하세요!"
meta_keywords: "Linux 파일 공유, scp 명령, 보안 복사, 네트워크 파일 전송, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

네트워크에서 컴퓨터가 유일한 경우는 거의 없으며, 특히 상업 환경에서 작업하는 경우에는 더욱 그렇습니다. 한 컴퓨터에서 다른 컴퓨터로 데이터를 전송해야 할 때, 때로는 USB 드라이브를 연결하여 수동으로 복사하는 것이 더 쉬울 수 있습니다. 하지만 대부분의 경우, 동일한 네트워크에 있는 컴퓨터로 작업하는 경우 데이터를 전송하는 방법은 네트워크 파일 공유를 통하는 것입니다.

이 과정에서는 네트워크의 다른 컴퓨터 간에 데이터를 복사하는 몇 가지 다른 방법을 다룰 것입니다. 간단한 파일 복사에 대해 논의한 다음, 별도의 드라이브처럼 작동하는 전체 디렉토리를 컴퓨터에 마운트하는 것에 대해 이야기할 것입니다.

간단한 파일 공유 도구 중 하나는 **scp** 명령입니다. scp 명령은 secure copy 의 약자입니다. cp 명령과 정확히 동일하게 작동하지만, 동일한 네트워크에 있는 한 호스트에서 다른 호스트로 복사할 수 있도록 합니다. ssh 를 통해 작동하므로 모든 작업은 ssh 와 동일한 인증 및 보안을 사용합니다.

### 로컬 호스트에서 원격 호스트로 파일을 복사하려면

```bash
scp myfile.txt username@remotehost.com:/remote/directory
```

### 원격 호스트에서 로컬 호스트로 파일을 복사하려면

```bash
scp username@remotehost.com:/remote/directory/myfile.txt /local/directory
```

### 로컬 호스트에서 원격 호스트로 디렉토리를 복사하려면

```bash
scp -r mydir username@remotehost.com:/remote/directory
```

## Exercise

연습은 완벽을 만듭니다! 다음은 보안 네트워크 파일 전송에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 SSH 를 사용한 보안 원격 액세스](https://labex.io/ko/labs/linux-secure-remote-access-in-linux-with-ssh-592816)** - 키 기반 인증, `scp`를 사용한 파일 보안 전송, 포트 포워딩을 위한 SSH 터널 생성 연습.

이 랩은 실제 시나리오에서 보안 원격 액세스 및 파일 전송 개념을 적용하고 `scp`에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

한 호스트에서 다른 호스트로 파일을 안전하게 복사하는 데 사용할 수 있는 명령은 무엇입

## Quiz Answer

scp
