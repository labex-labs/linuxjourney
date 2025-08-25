---
index: 4
lang: "ko"
title: "CPU 모니터링"
meta_title: "CPU 모니터링 - 프로세스 활용"
meta_description: "uptime 명령으로 CPU 모니터링을 배우세요. 로드 평균, CPU 사용량, 그리고 Linux 초보자를 위한 시스템 성능 해석 방법을 이해하세요."
meta_keywords: "uptime command, Linux CPU monitoring, load average, system performance, Linux tutorial, beginner guide"
---

## Lesson Content

유용한 명령어인 **uptime**에 대해 알아보겠습니다.

```
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
```

이 강좌의 첫 번째 레슨에서 uptime 에 대해 이야기했지만, 로드 평균 필드에 대해서는 다루지 않았습니다. 로드 평균은 시스템의 CPU 부하를 확인하는 좋은 방법입니다. 이 숫자들은 1 분, 5 분, 15 분 간격의 평균 CPU 부하를 나타냅니다. CPU 부하란 무엇을 의미할까요? CPU 부하는 CPU 에 의해 실행되기를 기다리는 프로세스의 평균 개수입니다.

단일 코어 CPU 가 있다고 가정해 봅시다. 이 코어를 교통 체증의 단일 차선이라고 생각하십시오. 고속도로의 러시아워라면 이 차선은 매우 혼잡할 것이고, 교통량은 100% 또는 부하 1 이 될 것입니다. 이제 교통 체증이 너무 심해져 고속도로가 막히고 일반 도로가 평소보다 두 배 많은 차량으로 혼잡해졌다면, 부하가 200% 또는 부하 2 라고 말할 수 있습니다. 이제 조금 풀려서 고속도로 차선에 차량이 절반만 있다면, 차선의 부하가 0.5 라고 말할 수 있습니다. 교통 체증이 없고 집에 더 빨리 갈 수 있다면, 부하는 이상적으로는 새벽 2 시 교통량처럼 매우 낮아야 합니다. 이 경우 차량은 프로세스이며, 이 프로세스들은 고속도로에서 벗어나 집으로 가기를 기다리고 있을 뿐입니다.

로드 평균이 1 이라고 해서 컴퓨터가 느려진다는 의미는 아닙니다. 요즘 대부분의 최신 기계는 여러 코어를 가지고 있습니다. 쿼드 코어 프로세서 (4 코어) 를 가지고 있고 로드 평균이 1 이라면, 실제로는 CPU 의 25% 에만 영향을 미치는 것입니다. 각 코어를 교통 체증의 차선이라고 생각하십시오. **cat /proc/cpuinfo** 명령으로 시스템에 있는 코어의 수를 확인할 수 있습니다.

로드 평균을 관찰할 때는 코어 수를 고려해야 합니다. 시스템이 항상 평균 이상의 부하를 사용하고 있다면, 뭔가 잘못된 일이 진행되고 있을 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 시스템 성능 및 CPU 부하 모니터링에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Manage and Monitor Linux Processes](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864)** - `ps` 및 `top`과 같은 도구를 사용하여 프로세스와 상호 작용하고 검사하며 리소스를 모니터링하는 연습을 통해 CPU 부하 이해와 직접적으로 관련됩니다.
2. **[Linux top Command: Real-time System Monitoring](https://labex.io/ko/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - `top` 명령을 사용하여 실시간 시스템 모니터링을 배우고, 프로세스 정렬 및 필터링을 포함하여 CPU 및 프로세스 활동에 대한 심층적인 내용을 제공합니다.
3. **[Linux free Command: Monitoring System Memory](https://labex.io/ko/labs/linux-linux-free-command-monitoring-system-memory-388496)** - 시스템 메모리 사용량을 모니터링하고 분석하는 방법을 배우고, 이는 종종 전체 시스템 성능에서 CPU 부하와 함께 중요한 요소입니다.

이러한 랩은 실제 시나리오에서 시스템 모니터링 및 리소스 관리 개념을 적용하고 시스템 성능 분석에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

로드 평균을 확인하는 데 사용할 수 있는 명령어는 무엇입니까?

## Quiz Answer

uptime
