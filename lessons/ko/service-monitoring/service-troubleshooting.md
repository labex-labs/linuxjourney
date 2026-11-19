---
lesson_id: "service-troubleshooting"
course_id: "service-monitoring"
lang: "ko"
order_index: 7
title: "서비스 문제 해결"
description: "서비스 중단, 의존 서비스 오류, 느린 요청을 조사할 때 다음으로 무엇을 확인할지 알아봅니다."
meta_title: "서비스 문제 해결 - 서비스 모니터링"
meta_description: "서비스 중단, 의존 서비스 오류, 느린 요청을 조사할 때 다음으로 무엇을 확인할지 알아봅니다."
meta_keywords: "서비스 문제 해결, 서비스 모니터링, DevOps, Linux Journey"
---

홈페이지 요청 실패처럼 구체적인 증상 하나에서 출발하세요. 비슷한 시각에 사용자의 접속 위치에서 얻은 관찰 결과를 비교합니다.

## 서버가 중단되었을 때

첫 번째 사례에서 브라우저는 연결 거부를 표시하고 서비스 컨테이너에는 `Exited (1)`이 표시됩니다. 이 두 관찰을 바탕으로 프로그램이 중단된 이유를 조사할 수 있습니다. 보존된 로그를 확인하세요. 다른 이벤트와 비교하기 전에 종료 시각을 확인하세요.

:::single-choice{#service-troubleshooting-stopped-case} 프로세스가 중단된 이유를 확인하는 데 가장 도움이 되는 것은 무엇인가요?

::option[같은 홈페이지에 다시 요청을 보내 최신 상태를 확인합니다.]{#service-troubleshooting-stopped-case-a explanation="다시 요청하면 증상이 여전한지 확인할 수 있습니다. 보존된 로그에는 프로그램이 종료된 이유가 나올 수 있습니다."}
::option[컨테이너에 남은 로그의 마지막 몇 줄을 읽습니다.]{#service-troubleshooting-stopped-case-b .correct explanation="시작 또는 종료 메시지를 보면 프로그램이 어디에서 멈췄는지 알 수 있습니다."}
::option[같은 이미지를 사용하는 다른 실행 중인 컨테이너의 로그를 봅니다.]{#service-troubleshooting-stopped-case-c explanation="그 컨테이너의 실행 이력은 별개이며 해당 오류를 겪지 않았을 수도 있습니다."}
:::

## 의존 서비스에 문제가 생겼을 때

두 번째 사례에서는 웹 프로세스는 실행 중이지만 페이지가 서버 오류를 반환합니다. 로그에 따르면 요청 `r17`을 처리하던 중 카탈로그에 접속하다 시간 초과가 발생했습니다. 의존 서비스에서 같은 요청의 기록을 살펴볼 차례입니다. 처음 접속한 서비스가 정상이어도 이후에 거치는 서비스에 문제가 있을 수 있습니다.

:::single-choice{#service-troubleshooting-dependency-case} r17을 조사하려면 다음으로 어떤 증거를 찾아야 하나요?

::option[해당 요청과 시각에 해당하는 카탈로그 기록입니다.]{#service-troubleshooting-dependency-case-a .correct explanation="의존 서비스에 요청을 보냈을 때 무슨 일이 있었는지 보여 줍니다."}
::option[보관된 Docker 이미지의 크기입니다.]{#service-troubleshooting-dependency-case-b explanation="이미지 크기로는 실제 요청에서 일어난 일을 알 수 없습니다."}
::option[어제 성공한 별개의 홈페이지 검사 결과입니다.]{#service-troubleshooting-dependency-case-c explanation="그 검사는 다른 시각의 결과이므로 이번 요청을 설명할 수 없습니다."}
:::

## 요청이 느려졌을 때

세 번째 예시에서는 대부분 정상적으로 응답하지만 사용자가 지연을 보고합니다. 워커 대기열이 길어진 구간에 지연 시간도 늘었습니다. 원인을 판단하기 전에 작업량과 워커의 활동을 확인하세요. 변경을 적용했다면 이후에 사용자 관점의 검사를 반복하고 같은 신호를 확인하세요.

:::single-choice{#service-troubleshooting-slow-case} 변경이 효과가 있었는지 확인하려면 무엇을 비교해야 하나요?

::option[변경 전후의 소스 저장소 스크린샷을 비교합니다.]{#service-troubleshooting-slow-case-a explanation="스크린샷으로는 요청에 걸린 시간이나 대기열을 측정할 수 없습니다."}
::option[캐시 크기와 배포한 브랜치 수를 비교합니다.]{#service-troubleshooting-slow-case-b explanation="두 값으로는 사용자가 기다린 시간을 설명할 수 없습니다."}
::option[변경 전후 비슷한 조건에서 사용자 요청 시간과 워커 대기열을 비교합니다.]{#service-troubleshooting-slow-case-c .correct explanation="처음 나타난 증상과 처리 한도에 걸렸다고 의심되는 지점을 함께 확인할 수 있습니다."}
:::

## 검사 결과가 서로 다를 때

로컬 검사는 성공하는데 사용자는 계속 오류를 겪는다고 가정해 보세요. 각 검사에 사용한 경로를 기록하세요. 로컬 검사로는 프로세스가 호스트에서 응답하는지 확인할 수 있습니다. 클라이언트의 요청은 해당 호스트까지 이어지는 경로에 문제가 있는지 보여 줄 수 있습니다.

:::single-choice{#service-troubleshooting-final-application} 영향을 받은 사용자의 문제를 계속 조사할 때 어느 결과를 참고해야 하나요?

::option[해당 사용자가 접속하는 경로와 위치에서 실행한 검사 결과입니다.]{#service-troubleshooting-final-application-a .correct explanation="사용자가 보고한 증상이 발생한 서비스 경로를 관찰할 수 있습니다."}
::option[서비스 호스트에서만 확인한 결과입니다.]{#service-troubleshooting-final-application-b explanation="이 결과로 문제가 발생하는 범위를 좁힐 수 있지만 외부 경로는 별도로 확인해야 합니다."}
::option[이미지 레지스트리의 현재 용량입니다.]{#service-troubleshooting-final-application-c explanation="레지스트리에서 이미지를 정상적으로 제공하더라도 사용자 접속 경로에 별도의 문제가 있을 수 있습니다."}
:::

## 요약

이제 확보한 증거에 따라 다음에 무엇을 확인할지 선택할 수 있습니다.

1. 프로세스 상태와 로그를 바탕으로 중단 원인을 조사합니다.
2. 실패한 요청을 의존 서비스까지 추적합니다.
3. 처음 사용자에게 나타난 증상이 개선되었는지 확인합니다.
