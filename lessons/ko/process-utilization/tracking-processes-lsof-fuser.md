---
index: 2
lang: "ko"
title: "lsof 및 fuser"
meta_title: "lsof 및 fuser - 프로세스 활용"
meta_description: "Linux 에서 lsof 및 fuser 명령을 사용하여 파일을 사용하는 프로세스를 식별하는 방법을 배웁니다. '장치 또는 리소스 사용 중' 오류를 이해하고 열린 파일을 효과적으로 관리합니다."
meta_keywords: "lsof, fuser, Linux 명령, 열린 파일, 프로세스 관리, Linux 튜토리얼, 초보자 가이드, 장치 사용 중"
---

## Lesson Content

USB 드라이브를 연결하고 일부 파일 작업을 시작했다고 가정해 봅시다. 작업이 끝난 후 USB 장치를 마운트 해제하려고 했지만 "Device or Resource Busy"라는 오류가 발생했습니다. USB 드라이브의 어떤 파일이 아직 사용 중인지 어떻게 알아낼 수 있을까요? 이를 위해 사용할 수 있는 두 가지 도구가 있습니다:

### lsof

파일은 단순히 텍스트 파일, 이미지 등이 아니라는 점을 기억하십시오. 파일은 디스크, 파이프, 네트워크 소켓, 장치 등 시스템의 모든 것입니다. 프로세스에서 사용 중인 것을 확인하려면 `lsof` 명령 ( "list open files"의 약자) 을 사용할 수 있습니다. 이 명령은 모든 열린 파일과 관련 프로세스 목록을 보여줍니다.

```bash
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
indicator 1809 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
lsof      5915 pete  cwd    DIR    8,6     4096  131 .
```

이제 어떤 프로세스가 현재 장치/파일을 열고 있는지 확인할 수 있습니다. USB 예시에서는 이러한 프로세스를 종료하여 이 성가신 드라이브를 마운트 해제할 수도 있습니다.

### fuser

프로세스를 추적하는 또 다른 방법은 `fuser` 명령 ("file user"의 약자) 을 사용하는 것입니다. 이 명령은 파일 또는 파일 사용자를 사용하는 프로세스에 대한 정보를 보여줍니다.

```bash
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  1809 ..c.. indicator-power
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
```

현재 `/home/pete` 디렉토리를 사용하고 있는 프로세스를 확인할 수 있습니다. `lsof`와 `fuser` 도구는 매우 유사합니다. 이 도구들에 익숙해지고 다음 번에 파일이나 프로세스를 추적해야 할 때 사용해 보십시오.

## Exercise

연습하면 완벽해집니다! 다음은 프로세스 관리 및 리소스 충돌 해결에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864)** - 포그라운드 및 백그라운드 프로세스와 상호 작용하고, `ps`로 검사하고, `top`으로 리소스를 모니터링하고, `kill`로 종료하는 연습을 합니다. 이 실습은 USB 드라이브의 파일과 같이 리소스를 점유하고 있을 수 있는 프로세스를 식별하고 관리하는 데 도움이 될 것입니다.

이 실습은 실제 시나리오에 개념을 적용하고 시스템 프로세스를 식별하고 관리하는 데 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

열린 파일과 해당 프로세스 정보를 나열하는 데 사용되는 명령은 무엇입니까?

## Quiz Answer

lsof
