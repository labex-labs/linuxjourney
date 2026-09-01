---
lesson_id: "managing-log-files"
course_id: "logging"
lang: "ko"
order_index: 6
title: "로그 파일 관리"
description: "logrotate로 안전한 텍스트 로그 로테이션을 설정하고 테스트하며 검증하는 방법을 알아봅니다."
meta_title: "로그 파일 관리 - 로깅"
meta_description: "초보자를 위한 logrotate 가이드로 리눅스 로그 관리를 익혀 보세요. 로그 로테이션으로 디스크 공간을 절약하고 설정을 구성해 시스템 로그를 정리하는 방법을 알아봅니다."
meta_keywords: "logrotate, 리눅스 로그, 로그 관리, 로그 로테이션, 리눅스 튜토리얼, 디스크 공간"
---

크기가 제한되지 않은 텍스트 로그는 파일시스템을 가득 채울 수 있고, 지나치게 공격적인 삭제는 운영이나 규정 준수에 필요한 증거를 없앨 수 있습니다. `logrotate`는 파일 기반 로그에 설정된 크기, 시간, 압축, 소유권 및 보존 정책을 적용합니다.

## 로테이션 이해하기

일반적인 로테이션은 활성 파일의 이름을 바꾸고, 대체 파일을 만들고, 필요하면 애플리케이션에 파일을 다시 열도록 요청하고, 오래된 세대를 압축하며, 보존 범위를 벗어난 파일을 제거합니다. 이 단계들은 설정에 따라 달라집니다. 보존된 사본도 삭제되거나 손상될 수 있고 같은 호스트의 장애로 유실될 수 있으므로 로테이션은 백업이 아닙니다.

:::single-choice{#logrotate-not-backup} 로그 로테이션이 백업이나 아카이빙을 대신할 수 없는 이유는 무엇입니까?

::option[로테이션된 파일도 로컬 보존 정책과 호스트 장애의 영향을 받기 때문입니다.]{#logrotate-local-retention .correct explanation="로테이션은 작업 로그의 세대를 제어하지만 독립적이고 영구적인 사본을 만들지는 않습니다."}
::option[로테이션은 이미지 파일만 처리할 수 있기 때문입니다.]{#logrotate-images explanation="이 유틸리티는 주로 로그 파일을 위해 설계됐습니다."}
::option[모든 로테이션이 모든 세대를 영원히 보존하기 때문입니다.]{#logrotate-forever explanation="보존 규칙은 일반적으로 오래된 세대를 제거합니다."}
:::

## 설정 찾기

주 파일은 일반적으로 `/etc/logrotate.conf`이고, 패키지 또는 애플리케이션 조각 파일은 `/etc/logrotate.d/` 아래에 있습니다. 단순화한 정책은 다음과 같습니다.

```text
/var/log/example/app.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 example adm
}
```

이 설정은 매일 평가하고, 로테이션된 세대 일곱 개를 보존하고, 한 세대 뒤에 압축하고, 로그가 없거나 비어 있어도 허용하며, 명시된 모드와 소유권으로 새 파일을 만들도록 요청합니다. 실제 로테이션은 기록된 상태와 스케줄러가 logrotate를 호출하는 방식에도 좌우됩니다.

:::single-choice{#logrotate-rotate-seven} `rotate 7`은 무엇을 지정합니까?

::option[정책에 따라 로테이션된 세대를 최대 일곱 개 보존합니다.]{#logrotate-seven-generations .correct explanation="설정한 보존 범위를 넘으면 더 오래된 세대가 제거됩니다."}
::option[애플리케이션을 하루에 일곱 번 실행합니다.]{#logrotate-run-seven explanation="이 지시문은 애플리케이션 실행이 아니라 보존할 세대를 제어합니다."}
::option[로테이션된 모든 파일의 권한을 모드 0007로 설정합니다.]{#logrotate-mode-seven explanation="파일 모드는 create 같은 지시문으로 제어합니다."}
:::

## 기록 프로세스와 조율하기

로그 파일의 이름을 바꾼 뒤에도 데몬은 열려 있는 파일 디스크립터를 통해 계속 쓸 수 있습니다. `postrotate` 스크립트는 문서화된 다시 불러오기 또는 다시 열기 신호를 보내는 데 자주 사용됩니다. 애플리케이션의 정확한 동작을 검증하고 스크립트 범위를 좁게 유지하십시오.

`copytruncate`는 애플리케이션이 로그를 다시 열 수 없을 때 파일을 복사하고 원본을 그 자리에서 잘라냅니다. 복사와 잘라내기 사이에 쓰기가 유실되거나 중복될 수 있으므로 보편적으로 안전한 기본값이 아니라 절충안입니다.

:::single-choice{#logrotate-open-descriptor} 로테이션 후 애플리케이션에 다시 열기 신호가 필요할 수 있는 이유는 무엇입니까?

::option[열린 디스크립터가 이름이 변경된 파일을 계속 가리킬 수 있기 때문입니다.]{#logrotate-descriptor-renamed .correct explanation="파일을 다시 열면 이후 쓰기가 새로 생성된 활성 경로를 사용합니다."}
::option[압축이 모든 애플리케이션 프로세스를 자동으로 중지하기 때문입니다.]{#logrotate-compression-stops explanation="압축은 기록 프로세스의 수명 주기를 자체적으로 관리하지 않습니다."}
::option[커널이 두 번째 로그 파일 생성을 금지하기 때문입니다.]{#logrotate-kernel-forbids explanation="여러 로그 파일이 존재할 수 있으며 문제는 기록 프로세스가 어느 inode를 열고 있는지입니다."}
:::

## 활성화 전 테스트

디버그 모드로 파일을 로테이션하지 않고 결정을 조사합니다.

```bash
$ sudo logrotate -d /etc/logrotate.conf
```

디버그 출력만으로 실제 실행 중 권한, 스크립트, 여유 공간 또는 애플리케이션의 파일 다시 열기가 성공한다고 입증되지는 않습니다. 통제된 환경에서 새 규칙을 테스트한 뒤 실행 후 활성 파일, 로테이션된 세대, 소유권, 압축, 애플리케이션 출력 및 logrotate 상태를 검사합니다. `-f`는 로테이션을 강제해 상태를 변경하므로 시험 실행과 혼동하지 마십시오.

:::single-choice{#logrotate-debug-mode} `logrotate -d`는 무엇을 제공합니까?

::option[만료된 모든 로그를 영구적으로 삭제합니다.]{#logrotate-debug-delete explanation="디버그 모드는 로테이션을 수행하지 않고 예정된 결정을 보고합니다."}
::option[정책과 관계없이 프로덕션 로테이션을 강제합니다.]{#logrotate-debug-force explanation="강제 옵션은 상태를 변경하는 -f입니다."}
::option[로그 파일이나 상태를 수정하지 않는 진단 평가입니다.]{#logrotate-debug-dry .correct explanation="구문과 결정을 먼저 검토하는 적절한 방법이며, 그 뒤에 통제된 실제 검증이 필요합니다."}
:::

## 다른 저장소 고려하기

Logrotate는 정책에 이름이 지정된 파일을 관리합니다. systemd 저널에는 자체 크기 및 보존 설정이 있고, 데이터베이스와 원격 로깅 서비스에는 별도의 수명 주기 제어가 있습니다. 파일시스템 용량과 로깅 상태를 모니터링해 멈춘 기록 프로세스나 실패한 로테이션을 공간이 소진되기 전에 감지하십시오.

:::single-choice{#logrotate-journal-retention} logrotate 규칙이 systemd 저널 보존을 자동으로 적용합니까?

::option[아니요. 저널 저장소에는 자체 설정과 제한이 있습니다.]{#logrotate-journal-separate .correct explanation="Logrotate는 파일 정책에서 선택한 경로만 관리합니다."}
::option[예. 모든 로그가 하나의 보존 엔진을 공유하기 때문입니다.]{#logrotate-all-logs explanation="파일 로테이션과 저널 보존은 서로 다른 메커니즘입니다."}
::option[예. 단, 텍스트 로그가 없을 때만 적용됩니다.]{#logrotate-journal-fallback explanation="텍스트 로그가 존재하더라도 두 보존 시스템이 합쳐지지는 않습니다."}
:::

## 요약

이제 파일 로그 로테이션을 아카이빙으로 오해하지 않고 정책을 설계하고 검증할 수 있습니다.

1. 공간, 운영 및 보존 요구 사항의 균형을 맞춥니다.
2. 세대 수, 압축, 소유권 및 빈 파일 처리 방식을 정의합니다.
3. 파일 디스크립터를 계속 열어 두는 애플리케이션과 안전하게 조율합니다.
4. 통제된 실제 로테이션 전에 설정을 디버그합니다.
5. 저널 및 외부 저장소의 보존을 별도로 관리합니다.
