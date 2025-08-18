---
index: 10
lang: "ko"
title: "/proc 파일 시스템"
meta_title: "/proc 파일 시스템 - 프로세스"
meta_description: "Linux 의 /proc 파일 시스템, 프로세스 정보 저장 방식 및 구조에 대해 알아보세요. 이 필수 Linux 가이드를 통해 프로세스 세부 정보를 탐색하세요."
meta_keywords: "/proc 파일 시스템, Linux 프로세스, 프로세스 정보, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

Linux 에서는 모든 것이 파일이며, 프로세스도 마찬가지입니다. 프로세스 정보는 `/proc` 파일 시스템으로 알려진 특수 파일 시스템에 저장됩니다.

```bash
ls /proc
```

여기서 여러 값을 볼 수 있습니다. 모든 PID 에 대한 하위 디렉터리가 있습니다. `ps` 출력에서 PID 를 확인했다면 `/proc` 디렉터리에서 찾을 수 있을 것입니다.

이제 프로세스 중 하나에 들어가 해당 파일을 살펴보세요:

```bash
bash
cat /proc/12345/status
```

프로세스 상태 정보와 더 자세한 정보를 볼 수 있습니다. `/proc` 디렉터리는 커널이 시스템을 보는 방식이므로, `ps`에서 볼 수 있는 것보다 훨씬 더 많은 정보가 있습니다.

## Exercise

No exercises for this lesson.

## Quiz Question

프로세스 정보를 저장하는 파일 시스템은 무엇입니까?

## Quiz Answer

/proc
