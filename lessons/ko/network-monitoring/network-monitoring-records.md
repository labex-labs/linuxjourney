---
lesson_id: "network-monitoring-records"
course_id: "network-monitoring"
lang: "ko"
order_index: 1
title: "네트워크 기록"
description: "확인하려는 내용에 맞는 네트워크 기록을 고르는 방법을 알아봅니다."
meta_title: "네트워크 기록 - 네트워크 모니터링"
meta_description: "확인하려는 내용에 맞는 네트워크 기록을 고르는 방법을 알아봅니다."
meta_keywords: "네트워크 기록, 네트워크 모니터링, 사이버 보안, Linux Journey"
---

네트워크 관찰 결과에는 특정 위치에서 도구가 볼 수 있었던 정보가 담깁니다. 먼저 무엇을 알아야 하는지 정하세요. 같은 활동도 출처에 따라 확인할 수 있는 부분이 다릅니다.

## 기록 유형 선택하기

**흐름 기록**은 네트워크의 양쪽 엔드포인트 사이의 통신을 요약합니다. **DNS 로그**는 리졸버에서 관찰한 이름 조회를 기록합니다. **패킷 캡처**는 캡처 지점에서 관찰한 개별 패킷의 사본을 저장합니다. 엔드포인트는 통신의 한쪽을 뜻하며 보통 주소와 포트로 식별합니다.

:::single-choice{#network-monitoring-records-choose-dns} 리졸버가 site.example에 어떤 응답을 반환했는지 알고 싶습니다. 어떤 자료가 가장 적합한가요?

::option[실행 중인 웹 워커 수입니다.]{#network-monitoring-records-choose-dns-b explanation="워커 수는 이름 조회와 관계없습니다."}
::option[해당 리졸버의 DNS 로그입니다.]{#network-monitoring-records-choose-dns-a .correct explanation="리졸버는 자신이 처리한 질의와 응답을 기록할 수 있습니다."}
::option[트래픽 양만 표시하는 흐름 요약입니다.]{#network-monitoring-records-choose-dns-c explanation="흐름 요약에는 DNS 질의와 응답이 생략될 수 있습니다."}
:::

## 관찰 지점 확인하기

노트북의 캡처에는 선택한 인터페이스에서 볼 수 있는 패킷이 담깁니다. 서버 로그에는 서버에 도착한 요청이나 서버가 기록한 이벤트가 담깁니다. 예를 들어 사용자 요청이 서버에 도달하기 전에 실패할 수 있습니다. 확인하려는 내용에 맞는 위치에서 작성한 자료를 사용하세요.

:::single-choice{#network-monitoring-records-capture-scope} 다른 컴퓨터에서 얻은 캡처에 해당 요청이 없습니다. 결론을 내리기 전에 무엇을 확인해야 하나요?

::option[캡처에 사용한 인터페이스에서 관련 경로와 시간대의 트래픽을 볼 수 있었는지 확인합니다.]{#network-monitoring-records-capture-scope-b .correct explanation="패킷이 없는 것은 관찰 지점의 가시 범위 때문일 수 있습니다."}
::option[캡처에 관련 없는 패킷이 있는지 확인합니다.]{#network-monitoring-records-capture-scope-a explanation="다른 트래픽이 보인다면 수집이 이루어졌다는 뜻입니다. 관련 경로와 시간대를 관찰할 수 있었는지는 따로 확인해야 합니다."}
::option[같은 시간에 다른 호스트도 캡처 중이었는지 확인합니다.]{#network-monitoring-records-capture-scope-c explanation="다른 호스트가 동시에 캡처했다고 해서 이 인터페이스가 무엇을 볼 수 있었는지 알 수는 없습니다."}
:::

## 작은 표본 사용하기

패킷 캡처에는 사람들이 공유하려고 하지 않은 내용이 담길 수 있습니다. 패킷 읽기를 연습할 때는 안전한 실습 트래픽만 담긴 준비된 캡처를 사용하세요. 일부를 공유할 때는 다른 사람이 그 범위를 이해할 수 있도록 확인한 시간대와 필터를 함께 기록하세요.

:::single-choice{#network-monitoring-records-choosing-evidence} DNS 응답을 식별하는 방법을 배우려면 어떤 표본이 가장 적합한가요?

::option[관련 없는 직원 트래픽을 오랫동안 캡처한 파일입니다.]{#network-monitoring-records-choosing-evidence-a explanation="불필요한 데이터가 많고 개인정보가 노출될 수 있습니다."}
::option[조회에 관한 필드가 없는 요약입니다.]{#network-monitoring-records-choosing-evidence-b explanation="학습자가 읽어야 할 증거가 빠져 있습니다."}
::option[실습용 질의와 응답을 담은 작은 캡처입니다.]{#network-monitoring-records-choosing-evidence-c .correct explanation="질문에 답하는 데 필요한 통신 내용을 담고 있습니다."}
:::

## 요약

이제 네트워크 기록을 고르고 그 기록으로 무엇을 관찰할 수 있는지 설명할 수 있습니다.

1. 흐름 요약, DNS 로그, 패킷 캡처를 구분합니다.
2. 네트워크 경로에 맞는 관찰 지점을 찾습니다.
3. 검토 목적에 맞는 작은 표본을 사용합니다.
