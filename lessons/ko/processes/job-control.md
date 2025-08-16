---
lang: "ko"
title: "작업 제어"
description: "Linux 작업 제어를 학습하여 백그라운드 프로세스를 관리하세요. 효율적인 셸 사용을 위해 'jobs', 'bg', 'fg', 'kill' 명령을 이해하세요. Linux 여정을 시작하세요!"
keywords: "Linux 작업 제어, 백그라운드 프로세스, jobs 명령, bg 명령, fg 명령, kill 명령, Linux 튜토리얼, 초보자 Linux"
---

## Lesson Content

단일 터미널 창에서 작업 중인데 명령이 너무 오래 걸린다고 가정해 봅시다. 명령이 완료될 때까지 셸과 상호 작용할 수 없습니다. 하지만 우리는 계속해서 컴퓨터에서 작업하고 싶으므로 셸을 열어 두어야 합니다. 다행히도 작업을 통해 프로세스가 실행되는 방식을 제어할 수 있습니다.

### Sending a job to the background

명령에 앰퍼샌드 (`&`) 를 추가하면 백그라운드에서 실행되므로 셸을 계속 사용할 수 있습니다. 예를 들어 보겠습니다:

```bash
sleep 1000 &
sleep 1001 &
sleep 1002 &
```

### View all background jobs

이제 방금 백그라운드로 보낸 작업을 볼 수 있습니다.

```bash
$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &
```

이렇게 하면 첫 번째 열에 작업 ID, 상태 및 실행된 명령이 표시됩니다. 작업 ID 옆의 **+**는 가장 최근에 시작된 백그라운드 작업을 의미합니다. **-**가 있는 작업은 두 번째로 최근에 실행된 명령입니다.

### Sending a job to the background on an existing job

이미 작업을 실행했고 백그라운드로 보내고 싶다면, 종료하고 다시 시작할 필요가 없습니다. 먼저 Ctrl-Z 로 작업을 일시 중단한 다음, **bg** 명령을 실행하여 백그라운드로 보냅니다.

```bash
pete@icebox ~ $ sleep 1003
^Z
[4]+    Stopped     sleep 1003

pete@icebox ~ $ bg
[4]+    sleep 1003 &

pete@icebox ~ $ jobs

[1]    Running     sleep 1000 &
[2]    Running     sleep 1001 &
[3]-   Running     sleep 1002 &
[4]+   Running     sleep 1003 &
```

### Moving a job from the background to the foreground

백그라운드에서 작업을 이동하려면 원하는 작업 ID 를 지정하기만 하면 됩니다. 옵션 없이 `fg`를 실행하면 가장 최근의 백그라운드 작업 (옆에 + 기호가 있는 작업) 이 다시 가져와집니다.

```bash
fg %1
```

### Kill background jobs

백그라운드에서 작업을 이동하는 것과 유사하게, 작업 ID 를 사용하여 프로세스를 종료하는 데 동일한 형식을 사용할 수 있습니다.

```bash
kill %1
```

## Exercise

백그라운드와 포그라운드 사이에서 일부 작업을 이동해 보세요.

## Quiz Question

백그라운드 작업을 나열하는 데 사용되는 명령은 무엇입니까?

## Quiz Answer

jobs
