---
index: 6
lang: "ko"
title: "로그 파일 관리"
meta_title: "로그 파일 관리 - 로깅"
meta_description: "logrotate 를 사용하여 Linux 로그 파일을 효율적으로 관리하는 방법을 배우세요. 디스크 공간을 절약하기 위한 로그 로테이션, 압축 및 구성을 알아보세요. 지금 학습을 시작하세요!"
meta_keywords: "logrotate, Linux 로그, 로그 관리, 로그 로테이션, Linux 튜토리얼, 초보자, 가이드, 디스크 공간"
---

## Lesson Content

로그 파일은 많은 데이터를 생성하고 이 데이터를 하드 디스크에 저장합니다. 그러나 여기에는 여러 가지 문제가 있습니다. 대부분의 경우, 우리는 단지 최신 로그를 볼 수 있기를 원합니다. 또한 디스크 공간을 효율적으로 관리하고 싶습니다. 그렇다면 이 모든 것을 어떻게 할까요? 답은 `logrotate`입니다.

`logrotate` 유틸리티는 로그 관리를 수행합니다. 이 유틸리티에는 얼마나 많은 로그를 보관할지, 어떤 로그를 보관할지, 공간 절약을 위해 로그를 압축하는 방법 등을 지정할 수 있는 구성 파일이 있습니다. `logrotate` 도구는 일반적으로 하루에 한 번 cron 을 통해 실행되며, 구성 파일은 `/etc/logrotate.d`에서 찾을 수 있습니다.

로그를 관리하는 데 사용할 수 있는 다른 로그 로테이션 도구도 있지만, `logrotate`가 가장 일반적입니다.

## Exercise

연습은 완벽을 만듭니다! 다음은 로그 파일 관리 및 관련 시스템 관리 작업에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 로그 및 구성 파일 보기](https://labex.io/ko/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - `logrotate`와 같은 도구로 관리되는 시스템 로그 및 구성 파일을 포함하여 텍스트 파일을 효율적으로 보고 탐색하기 위한 필수 Linux 명령줄 기술을 연습합니다.
2. **[신속한 위협 탐지](https://labex.io/ko/labs/linux-rapid-threat-detection-387930)** - 사이버 보안 분석을 위한 필수 Linux 명령줄 기술을 배웁니다. `tail` 및 `head` 명령을 사용하여 최근 로그 항목을 신속하게 추출하고 분석하여, 중요한 기술 환경에서 신속한 위협 탐지를 시뮬레이션합니다.
3. **[Linux 에서 tar 로 백업 생성 및 복원](https://labex.io/ko/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - 디렉터리를 백업하여 시스템 관리 작업에 대한 실습 경험을 얻습니다. 이는 종종 오래된 로그를 보관하기 위한 로그 로테이션 전략의 일부입니다.

이 랩들은 실제 시나리오에 개념을 적용하고 Linux 에서 로그 파일을 관리하고 상호 작용하는 데 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

로그를 관리하는 데 사용되는 유틸리티는 무엇입니까?

## Quiz Answer

logrotate
