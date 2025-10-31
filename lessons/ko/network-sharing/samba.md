---
index: 5
lang: "ko"
title: "삼바"
meta_title: "삼바 - 네트워크 공유"
meta_description: "리눅스에서 삼바 네트워크 공유를 설정하는 방법을 알아보세요. 이 가이드는 삼바 프로토콜, 설치, 구성 및 smb 리눅스 클라이언트를 사용하여 공유에 연결하는 방법을 다룹니다."
meta_keywords: "삼바, smb 리눅스, 리눅스 smb, 삼바 네트워크, 삼바 프로토콜, smb 삼바, 파일 공유, smb.conf, cifs, smbclient, 리눅스 튜토리얼"
---

## Lesson Content

수십 년 동안 Windows 와 Linux 머신 간에 파일을 공유하는 것은 혼합 OS 환경에서 주요한 과제였습니다. 이를 해결하기 위해 서버 메시지 블록 (SMB) 프로토콜이 등장했습니다. 원래 Windows 용으로 개발된 **samba protocol**은 나중에 공통 인터넷 파일 시스템 (CIFS) 이라는 방언으로 세분화되었습니다. 오늘날 최신 시스템은 SMB 의 새로운 버전을 사용하지만, 이 용어들은 종종 함께 사용됩니다.

Samba 는 Linux 및 기타 Unix 계열 시스템에서 **SMB/CIFS** 프로토콜을 구현하는 강력한 소프트웨어 모음입니다. 이는 **smb linux** 통합의 핵심이며, Linux 서버가 Windows, macOS 및 기타 Linux 클라이언트용 파일 및 인쇄 서버 역할을 하도록 하여 원활한 **samba network**를 생성할 수 있게 합니다. **smb samba**의 관계는 간단합니다. Samba 는 SMB 언어를 사용하는 소프트웨어입니다.

### Linux 에 Samba 설치하기

시작하려면 Samba 패키지를 설치해야 합니다. 명령어는 사용하는 Linux 배포판의 패키지 관리자에 따라 다릅니다. Ubuntu 와 같은 Debian 기반 시스템의 경우 다음을 사용합니다.

```bash
sudo apt update
sudo apt install samba
```

### Samba 공유 구성하기

Samba 의 기본 구성 파일은 `/etc/samba/smb.conf`에 있습니다. 이 파일은 어떤 디렉터리가 공유되는지, 누가 액세스할 수 있는지, 그리고 해당 권한을 결정합니다. 기본 파일에는 훌륭한 참조 자료가 되는 주석 처리된 예제가 많이 포함되어 있습니다.

기본 공유를 구성하는 단계를 살펴보겠습니다.

먼저 텍스트 편집기에서 구성 파일을 엽니다.

```bash
sudo nano /etc/samba/smb.conf
```

파일 하단에 공유를 위한 새 섹션을 추가합니다. 대괄호 안의 이름은 네트워크에서 보이는 공유 이름이 됩니다.

```ini
[myshare]
    comment = My First Samba Share
    path = /my/directory/to/share
    read only = no
    browsable = yes
```

다음으로 구성에서 지정한 디렉터리를 생성합니다.

```bash
mkdir -p /my/directory/to/share
```

마지막으로 Samba 액세스를 위한 특정 암호를 설정해야 합니다. Samba 는 시스템 사용자 암호와 별개인 자체 암호 데이터베이스를 유지 관리합니다.

```bash
sudo smbpasswd -a [username]
```

`[username]`을 시스템에 있는 기존 Linux 사용자로 바꾸십시오. Samba 액세스를 위해 해당 사용자에 대한 새 암호를 만들라는 메시지가 표시됩니다.

### Samba 서비스 관리하기

`smb.conf` 파일을 수정한 후에는 변경 사항을 적용하기 위해 Samba 서비스를 다시 시작해야 합니다.

```bash
sudo service smbd restart
```

### Samba 공유 액세스하기

공유가 구성되면 네트워크의 클라이언트가 액세스할 수 있습니다.

**Windows 에서:**
실행 창 (Win + R) 또는 파일 탐색기를 열고 네트워크 경로를 입력합니다: `\HOST\sharename` (여기서 `HOST`는 Linux 머신의 IP 주소 또는 호스트 이름입니다).

**Linux 에서:**
Samba 패키지에는 **smbclient**라는 명령줄 도구가 포함되어 있어 모든 **linux smb** 또는 Windows 공유와 상호 작용할 수 있습니다.

```bash
smbclient //HOST/myshare -U username
```

연결 후 파일을 관리하기 위해 `ls`, `get`, `put`과 같은 명령을 사용할 수 있는 `smb: \>` 프롬프트가 나타납니다.

### Samba 공유 마운트하기

더 영구적인 액세스를 위해 네트워크 공유를 파일 시스템에 직접 마운트하여 로컬 디렉터리처럼 보이게 할 수 있습니다.

```bash
sudo mount -t cifs //SERVER/sharename /mnt/mountpoint -o user=username,pass=password
```

이 명령어는 `cifs` 파일 시스템 유형을 사용하여 원격 공유를 로컬 마운트 지점에 연결합니다.

## Exercise

자신의 Linux 머신에 간단한 Samba 공유를 설정해 보세요. 디렉터리를 만들고, `smb.conf`에서 구성한 다음, 구성을 테스트하기 위해 동일한 머신에서 `smbclient`를 사용하여 액세스해 보세요. 더 많은 실습을 위해 관련 Linux 기술 및 개념을 연습할 수 있는 종합 [Linux 학습 경로](https://labex.io/ko/learn/linux)를 살펴보세요.

## Quiz Question

파일 공유를 위해 개발된 SMB 의 초기 방언인 프로토콜의 이름은 무엇입니까? 대소문자를 구분하여 영어로 답하십시오.

## Quiz Answer

CIFS
