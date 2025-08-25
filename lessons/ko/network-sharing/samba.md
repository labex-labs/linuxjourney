---
index: 5
lang: "ko"
title: "Samba"
meta_title: "Samba - 네트워크 공유"
meta_description: "Windows 및 macOS 용 Linux 에서 Samba 파일 공유를 설정하는 방법을 배웁니다. 이 초보자 가이드는 설치, 구성 및 공유 액세스를 다룹니다. 시작하세요!"
meta_keywords: "Samba, Linux 파일 공유, smb.conf, CIFS, smbclient, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

컴퓨팅 초창기에는 Windows 머신이 Linux 머신과 파일을 공유해야 할 필요성이 생겼고, 이에 따라 SMB(Server Message Block) 프로토콜이 탄생했습니다. SMB 는 Windows 운영 체제 간에 파일을 공유하는 데 사용되었으며 (macOS 도 SMB 를 사용하여 파일 공유 가능), 나중에 CIFS(Common Internet File System) 프로토콜 형태로 정리되고 최적화되었습니다.

Samba 는 Linux 에서 CIFS 와 함께 작동하는 Linux 유틸리티를 지칭합니다. 파일 공유 외에도 프린터와 같은 리소스도 공유할 수 있습니다.

### Samba 로 네트워크 공유 생성

Windows 머신이 액세스할 수 있는 네트워크 공유를 생성하는 기본 단계를 살펴보겠습니다.

### Samba 설치

```bash
sudo apt update
sudo apt install samba
```

### smb.conf 설정

Samba 의 구성 파일은 `/etc/samba/smb.conf`에 있습니다. 이 파일은 공유할 디렉토리, 액세스 권한 및 기타 옵션을 시스템에 알려야 합니다. 기본 `smb.conf`에는 이미 많은 주석 처리된 코드가 포함되어 있으며, 이를 예시로 사용하여 자신만의 구성을 작성할 수 있습니다.

```bash
sudo vi /etc/samba/smb.conf
```

### Samba 암호 설정

```bash
sudo smbpasswd -a [username]
```

### 공유 디렉토리 생성

```bash
mkdir /my/directory/to/share
```

### Samba 서비스 재시작

```bash
sudo service smbd restart
```

### Windows 를 통해 Samba 공유 액세스

Windows 에서 실행 프롬프트에 네트워크 연결을 입력하기만 하면 됩니다: `\\HOST\sharename`.

### Linux 를 통해 Samba/Windows 공유 액세스

```bash
smbclient //HOST/directory -U user
```

Samba 패키지에는 모든 Windows 또는 Samba 서버에 액세스하는 데 사용할 수 있는 **smbclient**라는 명령줄 도구가 포함되어 있습니다. 공유에 연결되면 파일을 탐색하고 전송할 수 있습니다.

### Samba 공유를 시스템에 연결

파일을 하나씩 전송하는 대신 네트워크 공유를 시스템에 마운트할 수 있습니다.

```bash
sudo mount -t cifs servername:directory mountpoint -o user=username,pass=password
```

## Exercise

이 주제에 대한 특정 랩은 없지만, 관련 Linux 기술 및 개념을 연습하기 위해 포괄적인 [Linux 학습 경로](https://labex.io/ko/learn/linux)를 탐색하는 것을 권장합니다.

## Quiz Question

Windows 와 Linux 간의 파일 전송에 사용되는 최신 프로토콜은 무엇입니까?

## Quiz Answer

CIFS
