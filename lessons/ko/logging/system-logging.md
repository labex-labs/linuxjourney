---
index: 1
lang: "ko"
title: "시스템 로깅"
meta_title: "시스템 로깅 - 로깅"
meta_description: "Linux 시스템 로깅, syslog, 그리고 /var/log에서 로그 파일을 보는 방법을 배웁니다. rsyslogd 를 이해하고 이 초보자 가이드를 통해 시스템 이벤트를 모니터링하세요."
meta_keywords: "Linux 로깅, syslog, rsyslogd, var log, 시스템 로그, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

시스템의 서비스, 커널, 데몬 등은 끊임없이 무언가를 수행합니다. 이 데이터는 실제로 로그 형태로 시스템에 저장되도록 전송됩니다. 이를 통해 우리는 시스템에서 발생하는 이벤트를 사람이 읽을 수 있는 형태로 기록할 수 있습니다. 이 데이터는 일반적으로 `/var` 디렉토리에 보관됩니다. `/var` 디렉토리는 로그와 같은 가변 데이터를 보관하는 곳입니다!

이러한 메시지들은 어떻게 시스템에 수신될까요? 이 정보를 시스템 로거로 보내는 syslog 라는 서비스가 있습니다.

syslog 는 실제로 많은 구성 요소를 포함합니다. 중요한 구성 요소 중 하나는 `syslogd` (최신 Linux 배포판은 `rsyslogd` 사용) 라는 데몬으로, 이벤트 메시지가 발생하기를 기다렸다가 알고 싶은 메시지를 필터링합니다. 해당 메시지로 무엇을 해야 하는지에 따라 파일로 보내거나, 콘솔로 보내거나, 아무것도 하지 않습니다.

이 시스템 로거가 로그를 관리하는 중앙 집중식 장소라고 생각할 수 있지만, 안타깝게도 그렇지 않습니다. 많은 애플리케이션이 자체 로깅 규칙을 작성하고 다른 로그 파일을 생성하는 것을 볼 수 있습니다. 그러나 일반적으로 로그 형식에는 타임스탬프와 이벤트 세부 정보가 포함되어야 합니다.

다음은 syslog 의 한 줄 예시입니다:

```plaintext
pete@icebox:~$ less /var/log/syslog
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

여기서 1 월 27 일 07:41:32 에 cron 서비스가 `cron.weekly` 작업을 실행했음을 알 수 있습니다. `/var/log/syslog` 파일에서 syslog 가 수집하는 모든 이벤트 메시지를 볼 수 있습니다.

## Exercise

`/var/log/syslog` 파일을 보고 시스템에서 또 어떤 일이 일어나고 있는지 확인하십시오.

## Quiz Question

최신 Linux 시스템에서 로그를 관리하는 데몬은 무엇입니까?

## Quiz Answer

rsyslogd
