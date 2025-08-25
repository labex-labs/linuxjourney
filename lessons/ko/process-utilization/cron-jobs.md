---
index: 8
lang: "ko"
title: "Cron 작업"
meta_title: "Cron 작업 - 프로세스 활용"
meta_description: "cron 작업을 사용하여 Linux 작업을 예약하는 방법을 배우세요. crontab 구문을 이해하고 일상적인 작업을 위한 스크립트를 자동화하세요. 이 초보자 친화적인 가이드로 시작하세요!"
meta_keywords: "cron 작업, crontab, 작업 예약, Linux 자동화, Linux 명령, 초보자 Linux, Linux 튜토리얼, crontab -e"
---

## Lesson Content

자원 활용에 대해 이야기하고 있지만, 이 시점에서 cron 을 사용하여 작업을 예약하는 데 사용되는 Linux 의 깔끔한 도구를 언급하는 것이 좋다고 생각합니다. 예약한 시간에 프로그램을 실행해 주는 서비스가 있습니다. 매일 실행해야 하는 스크립트가 있다면 정말 유용합니다.

예를 들어, `/home/pete/scripts/change_wallpaper`에 스크립트가 있다고 가정해 봅시다. 저는 매일 아침 이 스크립트를 사용하여 배경화면으로 사용하는 사진을 변경하지만, 매일 아침 이 스크립트를 수동으로 실행해야 합니다. 대신, cron 을 통해 스크립트를 실행하는 cron 작업을 만들 수 있습니다. 이 cron 작업이 실행되고 스크립트가 실행되기를 원하는 시간을 지정할 수 있습니다.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

필드는 왼쪽에서 오른쪽으로 다음과 같습니다.

- 분 - (0-59)
- 시 - (0-23)
- 월의 일 - (1-31)
- 월 - (1-12)
- 요일 - (0-7). 0 과 7 은 일요일을 나타냅니다.

필드의 별표는 모든 값과 일치함을 의미합니다. 따라서 위 예시에서는 매월 매일 오전 8 시 30 분에 실행되기를 원합니다.

cron 작업을 생성하려면 crontab 파일을 편집하기만 하면 됩니다:

```bash
crontab -e
```

## Exercise

연습하면 완벽해집니다! 다음은 Linux 에서 작업 예약을 이해하는 데 도움이 되는 실습입니다:

1. **[Linux 에서 at 및 cron 으로 작업 예약하기](https://labex.io/ko/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - `at`, `atq`, `atrm`, `crontab`을 사용하여 작업을 생성, 관리 및 제거하는 연습을 통해 시스템 관리 작업을 자동화하는 실무 경험을 얻으세요.

이 실습은 실제 시나리오에 개념을 적용하고 작업 예약에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

cron 작업을 편집하는 명령은 무엇입요?

## Quiz Answer

crontab -e
