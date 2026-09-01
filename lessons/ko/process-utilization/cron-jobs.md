---
lesson_id: "cron-jobs"
course_id: "process-utilization"
lang: "ko"
order_index: 8
title: "Cron 작업"
description: "cron으로 반복 작업을 만들고 검사하며 테스트하고 안전하게 운영하는 방법을 알아봅니다."
meta_title: "Cron 작업 - 프로세스 사용량"
meta_description: "cron 작업으로 리눅스에서 태스크를 예약하고 스크립트를 자동화하는 방법을 알아봅니다. crontab 구문과 crontab -e 같은 필수 명령을 설명합니다."
meta_keywords: "cron 작업, crontab, 작업 예약, 리눅스 자동화, crontab -e, cron, 리눅스 명령어"
---

cron은 대화형 셸 없이 반복 일정에 따라 명령을 실행합니다. 자동화는 올바른 동작뿐 아니라 실수도 반복하므로 예약하기 전에 명령을 테스트하고, 명시적인 경로를 사용하고, 권한을 제한하며, 로깅과 실패 알림을 계획하십시오.

## Crontab 항목 읽기

사용자 crontab 항목은 다섯 시간 필드와 그 뒤의 명령으로 구성됩니다.

```cron
30 8 * * * /home/pete/scripts/change_wallpaper
```

왼쪽부터 분, 시, 일, 월 및 요일 필드입니다. 이 예시는 cron 데몬에 적용되는 시간대를 기준으로 08:30에 실행됩니다. 별표는 해당 필드에서 허용되는 모든 값을 뜻합니다.

일과 요일 필드가 모두 제한된 경우 여러 cron 구현은 어느 한 필드가 일치하면 실행합니다. 두 필드를 함께 사용하는 일정을 만들기 전에 로컬 의미를 확인하십시오.

:::single-choice{#cron-daily-eight-thirty} `30 8 * * * command`는 언제 실행됩니까?

::option[8시간 동안 30분마다 실행됩니다.]{#cron-every-thirty explanation="필드는 지속 시간 표현식이 아니라 일정 안의 위치입니다."}
::option[매일 08:30에 실행됩니다.]{#cron-eight-thirty .correct explanation="분 30과 시 8은 고정되고 세 날짜 필드는 모든 값을 허용합니다."}
::option[매월 8일 30:08에 실행됩니다.]{#cron-invalid-time explanation="시는 0부터 23까지이며 이 예시는 일을 제한하지 않습니다."}
:::

## 사용자 Crontab 관리하기

현재 사용자의 crontab을 편집합니다.

```bash
$ crontab -e
```

변경 전후로 설치된 항목을 나열합니다.

```bash
$ crontab -l
```

`crontab -r`은 사용자의 전체 crontab을 제거하며 편집기를 열지 않을 수도 있습니다. 한 줄을 제거하려고 사용하지 말고 crontab을 편집한 뒤 남은 항목을 검증하십시오.

:::single-choice{#cron-list-current-user} 현재 사용자의 설치된 cron 항목을 나열하는 명령은 무엇입니까?

::option[`crontab -l`]{#cron-list .correct explanation="목록 옵션은 설치된 항목을 검사할 수 있도록 출력합니다."}
::option[`crontab -r`]{#cron-remove-all explanation="표시하지 않고 crontab을 제거하는 옵션입니다."}
::option[`crontab -e`]{#cron-edit explanation="단순히 나열하지 않고 crontab 편집기를 엽니다."}
:::

## Cron 환경 고려하기

cron은 일반적으로 제한된 환경과 비대화형 셸을 제공합니다. 명령과 파일에는 절대 경로를 사용하고 필요한 변수를 명시적으로 설정하며 별칭, 현재 터미널 디렉터리 또는 셸 시작 파일에 의존하지 마십시오.

표준 출력과 오류를 제어된 로그로 리디렉션하거나 시스템에 맞는 알림 메커니즘을 사용하십시오. 자격 증명을 제한적인 권한으로 보호하고 crontab 명령에 비밀 정보를 직접 넣지 마십시오.

:::single-choice{#cron-absolute-paths} cron 명령에서 명시적인 경로와 환경 설정을 사용해야 하는 이유는 무엇입니까?

::option[Cron이 항상 사용자의 현재 터미널 안에서 실행되기 때문입니다.]{#cron-current-terminal explanation="예약 작업은 대화형 세션과 독립적으로 실행됩니다."}
::option[절대 경로를 사용하면 모든 명령이 root로 실행되기 때문입니다.]{#cron-path-root explanation="경로는 파일을 선택하지만 권한을 부여하지 않습니다."}
::option[Cron 환경이 대화형 셸과 다를 수 있기 때문입니다.]{#cron-limited-environment .correct explanation="의존성을 명시하면 PATH, 디렉터리 또는 시작 파일 가정 때문에 생기는 실패를 막습니다."}
:::

## 테스트 및 중복 실행 방지

비슷하게 제한된 환경에서 같은 사용자로 스크립트를 수동 실행하십시오. 유용한 종료 상태를 반환하고 타임스탬프가 있는 결과를 기록하게 합니다. 설치 후 무해한 테스트 일정이나 제어된 실행을 기다리고 실제 부작용과 로그를 검증하십시오.

한 번의 실행이 일정 간격보다 오래 걸릴 수 있다면 동시 실행을 고려해 설계하거나 사용 가능한 경우 `flock` 같은 잠금 메커니즘을 사용합니다.

```cron
*/5 * * * * /usr/bin/flock -n /run/user/1000/report.lock /home/pete/bin/report
```

작업 사용자가 안전하게 만들 수 있는 잠금 경로를 선택하고 건너뛴 실행을 허용할지 결정하십시오. Cron은 인스턴스 하나만 실행됨을 자동으로 보장하지 않습니다.

:::single-choice{#cron-overlapping-runs} 작업 실행 시간이 일정 간격보다 길 때 발생할 수 있는 위험은 무엇입니까?

::option[여러 인스턴스가 겹쳐 실행되어 리소스를 두고 경쟁할 수 있습니다.]{#cron-overlap .correct explanation="이전 프로세스가 계속 실행 중이어도 cron은 새 실행을 시작할 수 있습니다."}
::option[다섯 일정 필드에 여섯 번째 잠금 필드가 자동으로 추가됩니다.]{#cron-auto-lock explanation="crontab 구문은 자동 상호 배제를 추가하지 않습니다."}
::option[스크립트가 영구적으로 커널 스레드로 변환됩니다.]{#cron-kernel-thread explanation="명령 예약은 이런 방식으로 프로세스 모델을 바꾸지 않습니다."}
:::

## 올바른 스케줄러 선택하기

cron은 단순한 반복 명령에 적합합니다. systemd 호스트에서 systemd 타이머는 의존성 통합, 누락 실행 보충, 무작위 지연 및 저널 로깅을 제공할 수 있습니다. 여러 시스템에서 작업을 정확히 한 번 실행해야 한다면 애플리케이션 또는 클러스터 스케줄러가 더 안전할 수 있습니다.

:::single-choice{#cron-cluster-exactly-once} 일반적인 호스트별 cron이 클러스터에서 정확히 한 번 실행해야 하는 작업에 적합하지 않을 수 있는 이유는 무엇입니까?

::option[모든 cron 항목이 한 글자로 제한되기 때문입니다.]{#cron-one-character explanation="crontab 명령에는 일반적인 명령줄을 넣을 수 있습니다."}
::option[각 호스트가 자체 복사본을 독립적으로 시작할 수 있기 때문입니다.]{#cron-each-host .correct explanation="호스트 전체에서 한 번의 실행을 적용하려면 분산 조정 메커니즘이 필요합니다."}
::option[Cron이 디스크에 저장된 스크립트를 실행할 수 없기 때문입니다.]{#cron-no-scripts explanation="스크립트 실행은 일반적인 cron 사용 사례입니다."}
:::

## 요약

이제 명시적인 일정 및 실행 가정을 갖춰 반복 cron 작업을 운영할 수 있습니다.

1. 정의된 순서대로 다섯 시간 필드를 읽습니다.
2. 관련 없는 작업을 삭제하지 않고 사용자 crontab을 검사하고 편집합니다.
3. 경로, 환경, 로깅 및 자격 증명 처리를 정의합니다.
4. 작업 사용자로 테스트하고 원하지 않는 중복 실행을 막습니다.
5. 호스트 및 조정 요구 사항에 맞는 스케줄러를 선택합니다.
