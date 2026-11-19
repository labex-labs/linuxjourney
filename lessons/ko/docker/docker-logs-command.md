---
lesson_id: "docker-logs-command"
course_id: "docker"
lang: "ko"
order_index: 6
title: "docker logs"
description: "컨테이너에서 수집한 출력을 읽고 다음에 무엇을 조사할지 판단합니다."
meta_title: "docker logs - Docker"
meta_description: "실행 중인 컨테이너와 종료된 컨테이너의 로그를 읽고 최근 출력에 집중하며 애플리케이션 오류와 컨테이너 상태를 구분합니다."
meta_keywords: "docker logs, 컨테이너 로그, Docker 문제 해결, 시작 오류, 최근 로그"
---

`preview`라는 컨테이너가 종료됐습니다. 컨테이너 목록에서는 상태와 종료 코드를 볼 수 있습니다. 프로그램이 무엇을 보고했는지 알려면 Docker가 이 컨테이너에서 수집한 출력을 확인하세요.

## 컨테이너 고르기

`docker logs`에 컨테이너 이름을 전달합니다. 컨테이너가 중지됐더라도 여전히 존재하고 출력이 보존됐다면 읽을 수 있습니다. 이 예에서 짧은 작업은 멈추기 전에 `/site/title.txt`에 있는 파일을 읽으려고 했습니다.

```text
$ docker logs preview
cat: can't open '/site/title.txt': No such file or directory
```

여기서 파일을 읽으려 한 프로그램은 `cat`입니다. 메시지에는 프로그램이 컨테이너 안에서 찾지 못한 경로가 표시됩니다.

:::single-choice{#docker-logs-command-read-exited} preview와 report는 같은 이미지를 사용했습니다. preview의 출력을 읽는 명령어는 무엇인가요?

::option[`docker logs report`]{#docker-logs-command-exited-report explanation="이름은 어느 컨테이너를 볼지 지정합니다. report는 다른 실행을 가리킵니다."}
::option[`docker logs busybox:1.36`]{#docker-logs-command-exited-image explanation="이것은 이미지 참조입니다. 로그는 이미지로 만든 개별 컨테이너에 속합니다."}
::option[`docker logs preview`]{#docker-logs-command-exited-preview .correct explanation="출력을 읽고 싶은 컨테이너의 이름을 지정한 명령어입니다."}
:::

## 메시지를 상황과 함께 읽기

로그에는 프로그램이 남긴 메시지가 들어 있습니다. 시작 메시지는 프로그램이 요청을 받기 시작했다는 사실을 알려 줄 수 있습니다. 오류는 완료하지 못한 동작을 보여 주기도 합니다. 이 예에서는 `preview` 안의 경로를 찾을 수 없었습니다. 해당 위치에 파일이 있어야 했는지 확인하는 것이 좋습니다. 메시지는 조사할 위치를 알려 줍니다.

:::single-choice{#docker-logs-command-error-boundary} 파일을 찾지 못했다는 메시지로 무엇을 알 수 있나요?

::option[호스트의 모든 디렉터리에 해당 파일이 없다.]{#docker-logs-command-error-host-path explanation="프로그램이 확인한 것은 컨테이너 안의 경로입니다. 메시지는 호스트 전체의 파일을 설명하지 않습니다."}
::option[프로그램이 preview 안에서 지정된 파일을 찾지 못했다.]{#docker-logs-command-error-container-path .correct explanation="preview 안에서 실행된 프로그램의 파일 검색 결과입니다."}
::option[호스트의 브라우저가 공개되지 않은 포트를 사용했다.]{#docker-logs-command-error-network explanation="메시지는 파일 검색에 관한 내용이며 브라우저가 사용한 포트를 알려 주지 않습니다."}
:::

## 최근 출력 확인하기

출력이 많은 컨테이너에서는 `--tail` 뒤에 줄 수를 지정하세요. Docker는 수집한 출력의 끝부터 지정된 줄 수만큼만 반환합니다. 적은 수로 시작하고 첫 오류가 더 위에 있으면 범위를 넓힙니다.

```bash
$ docker logs --tail 5 web
```

![preview의 파일 누락 오류와 web의 마지막 로그 다섯 줄을 보여 주는 LabEx 터미널](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-logs-command/preview-and-tail.png)

두 명령어는 서로 다른 컨테이너의 출력을 읽습니다. LabEx에서 `preview`는 파일 누락을, `web`은 Nginx 시작을 보고합니다.

:::single-choice{#docker-logs-command-tail-choice} web에서 볼 수 있는 가장 최근 두 줄만 확인하려면 어떤 명령어가 적절한가요?

::option[`docker logs --tail 2 web`]{#docker-logs-command-tail-two .correct explanation="tail 2는 이 컨테이너의 출력 끝에서 최대 두 줄을 요청합니다."}
::option[`docker logs --tail 5 web`]{#docker-logs-command-tail-five explanation="최대 다섯 줄을 요청하므로 두 줄보다 많이 나올 수 있습니다."}
::option[`docker logs web`]{#docker-logs-command-tail-unlimited explanation="줄 수를 제한하지 않으면 Docker가 보존된 모든 줄을 반환할 수 있습니다."}
:::

## 출력이 없을 때 확인하기

Docker는 수집한 출력만 보여 줄 수 있습니다. 어떤 명령어는 아무것도 출력하지 않고, 어떤 프로그램은 Docker가 수집하지 않는 파일에 메시지를 쓰기도 합니다. `docker logs`가 성공했는데 빈 출력이 나왔다면 `docker ps -a`로 컨테이너 상태를 확인하세요. 로그가 비어 있다는 것만으로는 상태를 알 수 없습니다.

:::single-choice{#docker-logs-command-empty-result} cleanup 작업에는 로그가 없습니다. 여전히 실행 중인지 이미 종료됐는지 어떻게 알 수 있나요?

::option[Docker에 cleanup의 로그를 더 많이 요청한다.]{#docker-logs-command-empty-more-lines explanation="줄 수 제한을 바꿔도 출력이 없는 프로그램이 멈췄는지는 알 수 없습니다."}
::option[cleanup을 시작하는 데 사용한 이미지를 찾는다.]{#docker-logs-command-empty-image explanation="이미지는 시작할 때의 파일과 설정을 알려 줍니다. 상태는 컨테이너 목록에 표시됩니다."}
::option[전체 컨테이너 목록에서 cleanup의 상태를 확인한다.]{#docker-logs-command-empty-container-state .correct explanation="전체 목록에는 실행 중인 컨테이너와 이미 종료됐지만 남아 있는 컨테이너가 모두 포함됩니다."}
:::

## 요약

이제 컨테이너의 출력을 바탕으로 다음에 확인할 항목을 결정할 수 있습니다.

1. 이름을 지정해 종료된 컨테이너의 출력도 읽습니다.
2. 프로그램의 메시지로 보고된 문제를 찾습니다.
3. `--tail`로 출력 줄 수를 제한합니다.
4. 로그만으로 답이 나오지 않으면 다른 방법으로 확인합니다.
