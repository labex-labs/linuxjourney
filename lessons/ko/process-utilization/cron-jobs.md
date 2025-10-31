---
index: 8
lang: "ko"
title: "크론 작업"
meta_title: "크론 작업 - 프로세스 활용"
meta_description: "크론 작업을 사용하여 Linux 에서 작업을 예약하고 스크립트를 자동화하는 방법을 알아보세요. 이 가이드는 crontab 구문, crontab -e 와 같은 필수 명령어, 초보자를 위한 실용적인 예제를 다룹니다."
meta_keywords: "크론 작업, crontab, 작업 예약, Linux 자동화, Linux 명령어, 초보자 Linux, Linux 튜토리얼, crontab -e, cron"
---

## Lesson Content

프로세스 활용도가 중요하지만, `Linux 자동화`를 위한 강력한 도구인 `cron` 데몬을 소개하기에 아주 좋은 시기입니다. 이 백그라운드 서비스는 특정 시간이나 간격으로 작업을 자동으로 실행하도록 `작업을 예약`할 수 있게 해줍니다. 이러한 예약된 작업을 일반적으로 `cron 작업`이라고 합니다. 이는 매일 밤 백업 스크립트를 실행하거나 일주일에 한 번 임시 파일을 정리하는 등 일상적인 작업을 자동화하는 데 엄청나게 유용합니다.

### Cron 작업이란 무엇인가

매일 아침 바탕 화면 배경을 새로 설정하기 위해 `/home/pete/scripts/change_wallpaper`에 있는 스크립트를 실행한다고 상상해 보십시오. 매일 수동으로 실행하는 대신, `cron 작업`을 만들어 대신 실행하도록 할 수 있습니다. 일정을 정의함으로써 `cron` 서비스에 스크립트를 정확히 언제 실행해야 하는지 알려줄 수 있으므로 진정한 "설정하고 잊어버리는" 솔루션이 됩니다.

### Crontab 구문 이해하기

`cron 작업`을 생성하려면 일정과 실행할 명령을 지정해야 합니다. 일정은 명령 앞에 오는 다섯 개의 필드로 정의됩니다.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

왼쪽에서 오른쪽으로 다섯 가지 시간 및 날짜 필드는 다음과 같습니다.

- **분:** 0-59
- **시:** 0-23 (24 시간 형식)
- **월의 일:** 1-31
- **월:** 1-12
- **주의 일:** 0-7 (여기서 0 과 7 은 모두 일요일을 나타냄)

an asterisk (`*`) in a field acts as a wildcard, meaning "every". In the example above, the schedule `30 08 * * *` tells `cron` to run the command at 8:30 AM, every day of the month, every month, and every day of the week.

### Crontab 을 사용한 Cron 작업 관리

`crontab` 명령을 사용하여 개인 `cron 작업`을 관리할 수 있으며, 이를 통해 사용자별 crontab 파일을 편집할 수 있습니다. 이 파일에는 예약한 모든 `cron 작업`이 포함됩니다.

`cron 작업`을 추가하거나 편집하려면 `-e` (편집) 플래그를 사용합니다. 그러면 기본 텍스트 편집기에서 crontab 파일이 열립니다.

```bash
crontab -e
```

작업 정의를 추가하고 파일을 저장하면 `cron`이 새 일정을 자동으로 읽습니다. `crontab -l`로 활성 `cron 작업`을 나열하거나 `crontab -r`로 모든 작업을 제거할 수도 있습니다. `cron 작업`을 사용하는 것은 `Linux 자동화`에 관심이 있는 모든 사람에게 기본적인 기술입니다.

## Exercise

연습이 완벽하게 만듭니다! 이 실습 랩은 Linux 에서 `작업을 예약`하는 방법에 대한 이해를 강화하는 데 도움이 될 것입니다.

1.  **[Linux 에서 at 및 cron 으로 작업 예약](https://labex.io/ko/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - `at`, `atq`, `atrm`, 및 `crontab`을 사용하여 작업을 생성, 관리 및 제거하는 연습을 통해 시스템 관리 작업을 자동화하는 실습 경험을 얻으십시오.

이 랩은 실제 시나리오에서 이 강의의 개념을 적용하고 `Linux 자동화`에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

개인 cron 작업을 편집하는 명령어는 무엇입니까? (정확한 소문자 명령어와 해당 옵션을 사용하여 답변하십시오.)

## Quiz Answer

crontab -e
