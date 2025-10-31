---
index: 4
lang: "ko"
title: "커널 로깅"
meta_title: "커널 로깅 - 로깅"
meta_description: "리눅스 커널 로그 (/var/log/kern.log 및 dmesg 포함) 를 살펴보세요. 부팅 메시지, 하드웨어 드라이버 정보 확인 및 시스템 문제 해결을 위해 kern 로그를 확인하는 방법을 알아보세요. 커널 로그 리눅스 파일 가이드."
meta_keywords: "커널 로그, kern.log, /var/log/kern.log, 커널 로그 리눅스, kern 로그, dmesg, 리눅스 로깅, 부팅 메시지, 커널 이벤트"
---

## Lesson Content

Linux 커널은 운영 체제의 핵심이며, 자체 작동, 하드웨어 상태 및 잠재적인 문제에 대한 메시지를 생성합니다. 이 정보에 액세스하는 것은 시스템 관리 및 문제 해결에 매우 중요합니다. 바로 이 지점에서 커널 로그가 필요합니다.

### 커널 링 버퍼와 dmesg

부팅 시 시스템은 커널 링 버퍼에서 방대한 양의 정보를 기록합니다. 이 버퍼에는 하드웨어 드라이버 로드, 커널 상태 업데이트 및 시작 프로세스 중에 발생하는 기타 이벤트에 대한 메시지가 포함되어 있습니다.

이 로그는 `dmesg` 명령을 사용하여 볼 수 있습니다. 내용은 종종 `/var/log/dmesg`에도 기록되지만, 이 파일은 일반적으로 재부팅할 때마다 지워지고 다시 작성된다는 점에 유의해야 합니다. 매일 필요하지는 않더라도, 하드웨어 문제나 부팅 중 문제가 발생하는 경우 `dmesg` 출력이 가장 먼저 확인해야 할 곳입니다.

### 기본 커널 로그 파일

커널 활동에 대한 보다 영구적인 기록을 위해 `/var/log/kern.log`를 확인할 수 있습니다. 이 파일은 `kernel log linux` 시스템이 사용하는 기본 대상입니다. 실행 중인 시스템에서 커널 정보와 이벤트를 캡처합니다.

`kern.log` 파일에는 `dmesg`의 출력도 포함되어 있어 커널 관련 메시지에 대한 포괄적인 소스가 됩니다. 링 버퍼에 더 이상 존재하지 않는 과거 이벤트의 `kernel log`를 조사해야 하는 경우, `kern log`가 올바른 위치입니다.

### 커널 로그가 중요한 이유

`kernel log`를 읽는 방법을 이해하는 것은 기본적인 기술입니다. 이 로그는 시스템이 하드웨어와 상호 작용하는 방식에 대한 깊은 통찰력을 제공합니다. `kern.log` 또는 `dmesg` 출력을 검사하여 드라이버 문제를 진단하고, 예기치 않은 하드웨어 동작을 조사하며, 커널의 전반적인 상태를 모니터링할 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! Linux 사용자 및 그룹 관리에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[useradd, usermod 및 userdel 을 사용하여 Linux 사용자 계정 관리](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성 및 보안부터 계정 수정 및 삭제에 이르기까지 사용자 관리의 전체 수명 주기를 연습합니다.
2. **[groupadd, usermod 및 groupdel 을 사용하여 Linux 그룹 관리](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 새 그룹 생성, 사용자 멤버십 수정 및 그룹 제거를 포함하여 그룹 관리를 위한 핵심 명령줄 유틸리티에 대한 실습 경험을 얻습니다.
3. **[Linux 에서 사용자 계정 및 Sudo 권한 구성](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 암호 정책 시행 및 관리자 권한 부여를 포함하여 Linux 시스템의 보안을 강화하기 위한 사용자 계정 및 sudo 권한 관리의 필수 기술을 배웁니다.

이러한 랩은 실제 시나리오에서 개념을 적용하고 Linux 에서 사용자 및 그룹 관리에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

커널 부팅 메시지를 보는 데 사용할 수 있는 명령은 무엇입니까? 소문자 영어 명령만 사용하여 답변하십시오.

## Quiz Answer

dmesg
