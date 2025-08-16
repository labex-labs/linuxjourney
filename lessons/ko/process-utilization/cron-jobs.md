---
title: "Cron 작업"
description: "cron job 을 사용하여 Linux 작업을 예약하는 방법을 배우세요. crontab 구문을 이해하고 일상적인 작업을 위한 스크립트를 자동화하세요. 이 초보자 친화적인 가이드로 시작하세요!"
keywords: "cron jobs, crontab, 작업 예약, Linux 자동화, Linux commands, 초보자 Linux, Linux tutorial, crontab -e"
---

## Lesson Content

리소스 활용에 대해 이야기했지만, cron 을 사용하여 작업을 예약하는 데 사용되는 Linux 의 깔끔한 도구를 언급하기에 좋은 시점이라고 생각합니다. 지정한 시간에 프로그램을 실행해 주는 서비스가 있습니다. 매일 실행해야 하는 스크립트가 있다면 정말 유용합니다.

예를 들어, `/home/pete/scripts/change_wallpaper`에 스크립트가 있다고 가정해 봅시다. 이 스크립트를 매일 아침 배경화면으로 사용하는 사진을 변경하는 데 사용하지만, 매일 아침 이 스크립트를 수동으로 실행해야 합니다. 대신, cron 을 통해 스크립트를 실행하는 cron job 을 만들 수 있습니다. 이 cron job 이 실행되고 스크립트를 실행할 시간을 지정할 수 있습니다.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

필드는 왼쪽에서 오른쪽으로 다음과 같습니다:

- Minute - (0-59)
- Hour - (0-23)
- Day of the month - (1-31)
- Month - (1-12)
- Day of the week - (0-7). 0 과 7 은 일요일을 나타냅니다.

필드의 별표는 모든 값과 일치함을 의미합니다. 따라서 위 예시에서는 매월 매일 오전 8 시 30 분에 실행되기를 원합니다.

cron job 을 생성하려면 crontab 파일을 편집하기만 하면 됩니다:

```bash
crontab -e
```

## Exercise

예약된 시간에 실행하고 싶은 cron job 을 생성하세요.

## Quiz Question

cron job 을 편집하는 명령어는 무엇입니까?

## Quiz Answer

crontab -e
