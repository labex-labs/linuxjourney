---
lesson_id: "service-logs"
course_id: "service-monitoring"
lang: "ko"
order_index: 2
title: "서비스 로그"
description: "요청 ID와 시각을 바탕으로 여러 서비스의 로그에서 같은 요청을 추적하는 방법을 알아봅니다."
meta_title: "서비스 로그 - 서비스 모니터링"
meta_description: "요청 ID와 시각을 바탕으로 여러 서비스의 로그에서 같은 요청을 추적하는 방법을 알아봅니다."
meta_keywords: "서비스 로그, 서비스 모니터링, DevOps, Linux Journey"
---

사용자에게 오류가 표시되면 서비스 로그를 통해 해당 요청의 어느 단계에서 문제가 발생했는지 파악할 수 있습니다. 먼저 시각을 확인하고 **요청 ID**를 찾으세요. 요청 ID는 같은 요청의 기록에 공통으로 붙는 식별자입니다.

## 요청 한 건 살펴보기

아래 예시에는 서비스 두 개가 나옵니다. **의존 서비스**는 프로그램이 작업을 완료하는 데 필요한 다른 서비스입니다. 여기서는 웹 서비스가 카탈로그 서비스에 상품 목록을 요청합니다.

```text
09:14:02 service=web     request=r17 path=/items status=502
09:14:02 service=catalog request=r17 action=read result=timeout
09:14:03 service=catalog request=r18 action=read result=ok
```

웹 서비스의 행에는 `r17`의 응답 실패가 기록되어 있습니다. 카탈로그 로그에서 같은 ID가 붙은 행에는 시간 초과가 나옵니다. 비슷한 시각에 성공한 카탈로그 요청의 ID는 `r18`입니다.

:::single-choice{#service-logs-matching-request} r17의 웹 요청 실패와 연결되는 카탈로그 결과는 무엇인가요?

::option[r18의 성공 결과입니다.]{#service-logs-matching-request-a explanation="이 행은 다른 요청의 기록입니다."}
::option[두 카탈로그 결과 모두 해당합니다.]{#service-logs-matching-request-c explanation="타임스탬프가 비슷해도 서로 다른 요청일 수 있습니다."}
::option[r17의 시간 초과입니다.]{#service-logs-matching-request-b .correct explanation="같은 ID를 통해 이 요청의 기록 두 건을 연결할 수 있습니다."}
:::

## 예시 로그 필터링하기

위 세 줄을 실습 디렉터리에 `requests.log`로 저장하세요. `grep -F`를 사용하면 입력한 문자열 그대로 찾을 수 있습니다. 이 예시에서는 필드 경계까지 맞추도록 식별자 뒤의 공백도 포함하세요.

```bash
$ grep -F 'request=r17 ' requests.log
```

웹 서비스와 카탈로그 서비스에서 각각 `r17`에 해당하는 행이 나옵니다. 실제 로그의 형식은 바뀔 수 있고 요청 ID가 생략되기도 합니다. 검색하는 필드가 모든 서비스에서 같은 의미인지 확인하세요.

:::single-choice{#service-logs-choose-filter} timeout이라는 단어 대신 요청 필드 전체로 검색하면 어떤 점이 좋은가요?

::option[모든 트래픽에서 같은 오류가 발생했음을 확인할 수 있습니다.]{#service-logs-choose-filter-b explanation="요청 한 건에 해당하는 기록을 거르는 작업입니다."}
::option[한 기록에만 timeout이 들어 있어도 웹과 카탈로그에서 해당 요청의 기록을 모두 찾을 수 있습니다.]{#service-logs-choose-filter-a .correct explanation="같은 ID로 두 서비스에서 이 요청을 추적할 수 있습니다."}
::option[로그를 바꿔 나중에 검색할 때 올바른 결과가 나오게 합니다.]{#service-logs-choose-filter-c explanation="Grep은 파일을 읽고 일치하는 줄을 출력합니다."}
:::

![요청 r17의 웹 오류와 카탈로그 시간 초과를 연결해 보여 주는 grep 출력](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-logs/request-id.png)

## 관찰한 범위 보고하기

시간 초과는 이 요청이 어느 지점에서 실패했는지 알려 줍니다. 카탈로그 내부에서 어떤 구성 요소가 느려졌는지는 알 수 없습니다. 다음으로 카탈로그 자체의 지표나 최근 기록을 확인하세요. 팀원에게 로그 일부를 전달할 때는 요청 ID를 남기고 그 사람에게 필요하지 않은 비밀 정보나 개인정보는 제거하세요.

:::single-choice{#service-logs-evidence-limit} 첫 보고에 어떤 내용을 담아야 하나요?

::option[r17을 처리하던 중 카탈로그에서 시간 초과가 발생하여 추가 확인이 필요합니다.]{#service-logs-evidence-limit-c .correct explanation="관련 기록에서 확인한 내용을 정리했고 근본 원인은 추측하지 않았습니다."}
::option[모든 카탈로그 요청에서 시간 초과가 발생했습니다.]{#service-logs-evidence-limit-a explanation="예시에는 별도로 성공한 카탈로그 요청도 있습니다."}
::option[특정 데이터베이스 디스크에 장애가 발생했습니다.]{#service-logs-evidence-limit-b explanation="로그에는 디스크를 확인한 내용이 없습니다."}
:::

Linux 호스트에서 서비스 기록을 검색하는 연습은 [사고 대응을 위한 로그 분석](https://labex.io/labs/linux-monitoring-and-incident-response-log-analysis-594586) 실습에서 할 수 있습니다.

## 요약

이제 여러 서비스의 로그에서 한 요청의 처리 흐름을 추적할 수 있습니다.

1. 관련 기록에서 같은 요청 ID를 찾습니다.
2. 입력한 문자열 그대로 검색해 범위를 좁힙니다.
3. 기록으로 확인한 사실을 보고하고 다음에 살펴볼 사항을 정합니다.
