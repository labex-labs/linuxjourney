---
index: 2
lang: "ko"
title: "lsof 및 fuser"
meta_title: "lsof 및 fuser - 프로세스 사용량"
meta_description: "특정 파일을 사용하는 프로세스를 식별하기 위해 Linux 에서 lsof 및 fuser 명령을 탐색합니다. '장치 또는 리소스 사용 중' 오류 해결 방법, fuser 와 lsof 비교, fuser -k 와 같은 옵션을 사용하여 열린 파일을 효과적으로 관리하는 방법을 배웁니다."
meta_keywords: "lsof, fuser, fuser 명령어, 리눅스 fuser, fuser 대 lsof, lsof 대 fuser, fuser -k 리눅스, 열린 파일, 프로세스 관리, 장치 사용 중, Linux 명령어"
---

## Lesson Content

USB 드라이브를 마운트 해제하려고 할 때 "장치 또는 리소스가 사용 중입니다 (Device or Resource Busy)" 오류가 발생한 적이 있습니까? 이 일반적인 문제는 프로세스가 여전히 해당 장치의 파일이나 디렉터리를 사용하고 있을 때 발생합니다. 이를 해결하려면 어떤 프로세스가 해당 리소스를 점유하고 있는지 확인해야 합니다. 이 작업을 위한 두 가지 강력한 유틸리티는 `lsof`와 `fuser`입니다.

### lsof 를 사용하여 열린 파일 나열하기

리눅스에서는 디스크, 파이프, 네트워크 소켓, 장치를 포함하여 거의 모든 것이 파일로 취급됩니다. `lsof`( "list open files"의 약자) 명령어는 열려 있는 모든 파일과 해당 파일을 사용하는 프로세스의 자세한 목록을 보여줍니다.

현재 디렉터리 (`.`) 를 어떤 프로세스가 사용하고 있는지 확인하려면 다음을 실행할 수 있습니다.

```bash
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
```

출력에는 각 열린 파일과 관련된 명령어 (`COMMAND`), 프로세스 ID(`PID`), 사용자 (`USER`) 가 표시됩니다. 이 정보를 통해 장치 마운트 해제를 방해하는 프로세스를 식별할 수 있습니다.

### fuser 명령어

또 다른 훌륭한 도구는 `fuser`( "file user"의 약자) 명령어입니다. 이 유틸리티는 특정 파일, 소켓 또는 파일 시스템을 사용하는 프로세스를 식별합니다. `linux fuser` 명령어는 특정 리소스에 액세스하는 프로세스의 PID 를 빠르게 확인하는 방법입니다.

`-v`(자세히) 옵션을 사용하면 더 자세한 출력을 얻을 수 있습니다.

```bash
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
```

여기서 우리는 현재 디렉터리를 사용하고 있는 프로세스를 명확하게 볼 수 있습니다. `ACCESS` 열은 파일이 어떻게 사용되고 있는지 (예: 현재 디렉터리의 경우 `c`) 를 보여줍니다.

### fuser 로 프로세스 종료하기

`fuser` 명령어의 주요 기능은 리소스를 사용하는 프로세스를 종료할 수 있다는 것입니다. `fuser -k` 옵션은 지정된 파일이나 파일 시스템에 액세스하는 모든 프로세스에 `SIGKILL` 신호를 보냅니다. 이는 사용 중인 장치를 마운트 해제할 때 특히 유용합니다.

예를 들어, `/mnt/usb` 마운트 지점을 사용하는 모든 프로세스를 종료하려면 다음을 실행합니다.

```bash
sudo fuser -k /mnt/usb
```

리눅스에서 `fuser -k`를 사용하는 것은 리소스를 확보하는 빠르고 효과적인 방법입니다.

### fuser 대 lsof

그렇다면 `fuser` 대 `lsof` 중 언제 무엇을 사용해야 할까요?

- **`lsof`**는 자세한 조사를 위해 훌륭합니다. 열려 있는 모든 파일에 대한 광범위한 정보를 제공하므로 복잡한 문제 해결에 이상적입니다.
- **`fuser`**는 더 직접적입니다. 특정 파일이나 마운트 지점에서 프로세스를 신속하게 식별하고 필요한 경우 종료하는 데 적합합니다. `fuser command`는 "장치 또는 리소스가 사용 중" 오류를 해결하는 데 더 빠른 선택인 경우가 많습니다.

두 도구 모두 모든 리눅스 사용자에게 필수적입니다. 파일을 효율적으로 관리하고 프로세스를 관리하려면 이 도구들에 익숙해지십시오.

## Exercise

연습이 완벽을 만듭니다! 리소스 충돌 문제 해결 및 프로세스 관리에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[리눅스 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864)** - 포그라운드 및 백그라운드 프로세스와 상호 작용하고, `ps`로 검사하고, `top`으로 리소스를 모니터링하고, `kill`로 종료하는 연습을 합니다. 이 랩은 USB 드라이브의 파일과 같이 리소스를 점유하고 있을 수 있는 프로세스를 식별하고 관리하는 데 도움이 될 것입니다.

이 랩은 실제 시나리오에서 이러한 개념을 적용하고 시스템 프로세스를 식별하고 관리하는 데 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

열려 있는 파일과 해당 프로세스 정보를 나열하는 데 사용되는 명령어는 무엇입니까? (영어로, 소문자만 사용하여 답변하십시오.)

## Quiz Answer

lsof
