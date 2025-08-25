---
index: 9
lang: "ko"
title: "tail"
meta_title: "tail - 텍스트 다루기"
meta_description: "`tail` 명령을 사용하여 Linux 에서 파일 끝을 보고 로그를 모니터링하는 방법을 배웁니다. 실시간 업데이트를 위한 `tail -f`를 알아보세요. Linux 여정을 시작하세요!"
meta_keywords: "tail command, Linux tail, tail -f, 로그 보기, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

`head` 명령과 유사하게, `tail` 명령은 기본적으로 파일의 마지막 10 줄을 보여줍니다.

```bash
tail /var/log/syslog
```

`head`와 마찬가지로, 보고 싶은 줄 수를 변경할 수 있습니다.

```bash
tail -n 10 /var/log/syslog
```

사용할 수 있는 또 다른 훌륭한 옵션은 `-f` (follow) 플래그입니다. 이 플래그는 파일이 커짐에 따라 파일을 계속 추적합니다. 한번 시도해보고 어떤 일이 일어나는지 확인해보세요.

```bash
tail -f /var/log/syslog
```

시스템과 상호 작용하는 동안 `syslog` 파일은 계속 변경되며, `tail -f`를 사용하면 해당 파일에 추가되는 모든 것을 볼 수 있습니다.

## Exercise

연습은 완벽을 만듭니다! 다음은 `tail` 명령과 그 적용에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux tail 명령: 파일 끝 표시](https://labex.io/ko/labs/linux-linux-tail-command-file-end-display-214303)** - 실시간 업데이트를 위한 `-f` 옵션을 포함하여 텍스트 파일의 끝을 보고 모니터링하는 Linux `tail` 명령을 배웁니다.
2. **[Linux 에서 로그 및 구성 파일 보기](https://labex.io/ko/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 시스템 모니터링에 중요한 `tail` ( `cat` 및 `more`와 함께) 을 사용하여 로그 및 구성 파일을 효율적으로 보고 탐색하는 연습을 합니다.
3. **[신속한 위협 탐지](https://labex.io/ko/labs/linux-rapid-threat-detection-387930)** - `tail` 지식을 적용하여 최근 로그 항목을 신속하게 추출하고 분석하여 사이버 보안 컨텍스트에서 신속한 위협 탐지를 시뮬레이션합니다.

이러한 랩은 실제 시나리오에서 파일 내용을 보고 모니터링하는 개념을 적용하고 `tail` 명령에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

`tail`에서 파일을 추적하는 데 사용되는 플래그는 무엇입니까?

## Quiz Answer

-f
