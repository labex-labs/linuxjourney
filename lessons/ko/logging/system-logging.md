---
index: 1
lang: "ko"
title: "시스템 로깅"
meta_title: "시스템 로깅 - 로깅"
meta_description: "Linux 시스템 로깅, syslog, 그리고 /var/log에서 로그 파일을 보는 방법을 알아보세요. rsyslogd 를 이해하고 이 초보자 가이드로 시스템 이벤트를 모니터링하세요."
meta_keywords: "Linux 로깅, syslog, rsyslogd, var log, 시스템 로그, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

시스템의 서비스, 커널, 데몬 등은 끊임없이 무언가를 수행합니다. 이 데이터는 실제로 로그 형태로 시스템에 저장됩니다. 이를 통해 시스템에서 발생하는 이벤트를 사람이 읽을 수 있는 형태로 기록할 수 있습니다. 이 데이터는 일반적으로 `/var` 디렉토리에 보관됩니다. `/var` 디렉토리는 로그와 같은 가변 데이터를 보관하는 곳입니다!

이러한 메시지는 어떻게 시스템에서 수신될까요? syslog 라는 서비스가 이 정보를 시스템 로거로 보냅니다.

syslog 는 실제로 많은 구성 요소를 포함합니다. 중요한 구성 요소 중 하나는 `syslogd` (최신 Linux 배포판은 `rsyslogd` 사용) 라는 데몬으로, 이벤트 메시지가 발생하기를 기다렸다가 필요한 메시지를 필터링합니다. 해당 메시지로 무엇을 해야 하는지에 따라 파일로 보내거나, 콘솔로 보내거나, 아무것도 하지 않습니다.

이 시스템 로거가 로그를 관리하는 중앙 집중식 장소라고 생각할 수 있지만, 안타깝게도 그렇지 않습니다. 많은 애플리케이션이 자체 로깅 규칙을 작성하고 다른 로그 파일을 생성하는 것을 볼 수 있습니다. 그러나 일반적으로 로그 형식에는 타임스탬프와 이벤트 세부 정보가 포함되어야 합니다.

다음은 syslog 의 한 줄 예시입니다:

```plaintext
pete@icebox:~$ less /var/log/syslog
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

여기서 1 월 27 일 07:41:32 에 cron 서비스가 `cron.weekly` 작업을 실행했음을 알 수 있습니다. syslog 가 수집하는 모든 이벤트 메시지는 `/var/log/syslog` 파일에서 볼 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! Linux 로그 및 파일 보기에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 로그 및 구성 파일 보기](https://labex.io/ko/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 시스템 로그 및 구성 파일을 포함하여 텍스트 파일을 효율적으로 보고 탐색하기 위한 필수 Linux 명령줄 기술을 배웁니다. `cat`, `more`, `less`와 같은 명령을 사용하여 다양한 파일 유형에서 중요한 정보를 추출하는 연습을 합니다.
2. **[Linux tail 명령어: 파일 끝 표시](https://labex.io/ko/labs/linux-linux-tail-command-file-end-display-214303)** - 텍스트 파일의 끝을 보고 모니터링하기 위한 Linux `tail` 명령어를 배웁니다. 이는 실시간 로그 분석에 특히 유용합니다.
3. **[Linux 에서 grep 으로 텍스트 검색](https://labex.io/ko/labs/comptia-search-text-with-grep-in-linux-590841)** - 이 랩에서는 `grep` 명령을 사용하여 Linux 시스템의 파일에서 텍스트를 검색하는 방법을 배웁니다. 이는 대용량 로그 파일 내에서 특정 항목을 찾는 데 매우 중요합니다.

이러한 랩은 실제 시나리오에서 로그 파일 관리 및 분석 개념을 적용하고 Linux 시스템 모니터링에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

최신 Linux 시스템에서 로그를 관리하는 데몬은 무엇입니까?

## Quiz Answer

rsyslogd
