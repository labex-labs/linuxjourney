---
lesson_id: "compose-volumes"
course_id: "docker-compose"
lang: "ko"
order_index: 4
title: "볼륨"
description: "컨테이너를 바꿔도 이름이 지정된 볼륨에 저장한 파일이 남는 이유를 알아봅니다."
meta_title: "볼륨 - Docker Compose"
meta_description: "컨테이너를 바꿔도 이름이 지정된 볼륨에 저장한 파일이 남는 이유를 알아봅니다."
meta_keywords: "이름이 지정된 볼륨, 데이터 유지, Docker Compose, DevOps, Linux Journey"
---

컨테이너는 자체 쓰기 가능 계층에 파일을 쓸 수 있습니다. 컨테이너를 삭제하면 Docker가 그 계층도 삭제합니다. **이름이 지정된 볼륨**은 Docker가 컨테이너와 별도로 관리하는 저장 공간입니다. 컨테이너를 바꿔도 새 컨테이너에 같은 볼륨을 연결할 수 있습니다.

## 실습용 볼륨 정의하기

이 예시는 실습 폴더에 `compose.volume.yaml`이라는 별도 파일로 저장합니다. `notes`라는 저장 공간을 도구 컨테이너의 `/data`에 마운트합니다. 파일 하단의 `volumes` 섹션에서 이름이 지정된 볼륨을 선언합니다.

```yaml
services:
  toolbox:
    image: busybox:1.36
    volumes:
      - notes:/data
volumes:
  notes:
```

서비스 정의는 컨테이너 안에서 어디에 볼륨을 마운트할지 정합니다. 최상위 선언은 Compose가 이 볼륨을 프로젝트와 함께 관리하도록 합니다.

:::single-choice{#compose-volumes-attached-path} 도구 컨테이너 내부에서 어느 경로에 볼륨을 마운트하나요?

::option[/notes입니다.]{#compose-volumes-attached-path-b explanation="notes는 볼륨 이름입니다. 컨테이너에 마운트하는 경로는 콜론 오른쪽에 있습니다."}
::option[/data입니다.]{#compose-volumes-attached-path-a .correct explanation="notes:/data에서 오른쪽이 컨테이너 내부의 경로입니다."}
::option[컨테이너 안의 모든 경로입니다.]{#compose-volumes-attached-path-c explanation="볼륨은 설정한 디렉터리에만 마운트됩니다."}
:::

## 서로 다른 컨테이너로 쓰고 읽기

`-f` 옵션으로 다른 설정 파일을 선택하고 `-p`로 별도의 프로젝트 이름을 지정합니다. `run --rm` 명령은 한 번 실행할 컨테이너를 만들고, 실행이 끝나면 이를 삭제합니다. 다른 작업과 분리한 실습 폴더에서 명령을 실행하세요. 첫 번째 명령은 `/data/note.txt`의 테스트 파일을 덮어씁니다.

```bash
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox sh -c 'echo ready > /data/note.txt'
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox cat /data/note.txt
```

두 번째 컨테이너는 `ready`를 출력해야 합니다. 첫 번째 컨테이너와 같은 볼륨을 마운트하기 때문입니다.

:::single-choice{#compose-volumes-persistence} 첫 번째 컨테이너가 삭제된 뒤에도 두 번째 컨테이너가 파일을 읽을 수 있는 이유는 무엇인가요?

::option[두 컨테이너 모두 이름이 지정된 같은 볼륨을 마운트했습니다.]{#compose-volumes-persistence-b .correct explanation="/data에 마운트된 별도 저장 공간에 파일을 썼습니다."}
::option[두 컨테이너가 첫 번째 컨테이너의 쓰기 가능 계층을 보관했습니다.]{#compose-volumes-persistence-a explanation="첫 번째 컨테이너의 계층은 컨테이너와 함께 삭제되었습니다."}
::option[BusyBox가 파일을 이미지에 자동으로 추가했습니다.]{#compose-volumes-persistence-c explanation="컨테이너를 실행해도 원본 이미지는 바뀌지 않습니다."}
:::

![서로 다른 두 도구 컨테이너가 이름이 지정된 같은 볼륨의 파일을 쓰고 읽는 모습](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-volumes/persisted-note.png)

## 어떤 데이터가 남는지 확인하기

마운트된 디렉터리 바깥에 있는 `/tmp/note.txt` 같은 파일은 그 위치에 별도 저장 공간을 마운트하지 않았다면 해당 컨테이너에만 남습니다. 파일이 보존된다고 판단하기 전에 경로를 확인하세요. 볼륨 자체를 삭제하면 데이터가 사라질 수 있습니다. 백업은 따로 보관하는 복사본이며, 볼륨을 잃었을 때 데이터를 복원하는 데 사용합니다.

:::single-choice{#compose-volumes-inside-mount} 다음에 실행할 도구 컨테이너가 이 볼륨을 통해 읽을 수 있는 파일은 무엇인가요?

::option[첫 번째 도구 컨테이너의 쓰기 가능 계층에 있는 /tmp/note.txt입니다.]{#compose-volumes-inside-mount-a explanation="이 경로는 설정한 마운트 위치 밖에 있습니다."}
::option[다른 이름의 볼륨에 저장된 파일입니다.]{#compose-volumes-inside-mount-b explanation="그 파일을 읽으려면 새 컨테이너가 그 볼륨도 마운트해야 합니다."}
::option[첫 번째 도구 컨테이너가 쓴 /data/note.txt입니다.]{#compose-volumes-inside-mount-c .correct explanation="/data에 같은 볼륨을 마운트하므로 두 컨테이너에서 같은 파일에 접근할 수 있습니다."}
:::

## 요약

이제 파일을 쓴 컨테이너를 삭제해도 파일이 남을 수 있는 이유를 설명할 수 있습니다.

1. 볼륨 이름과 마운트 경로를 확인합니다.
2. 다른 컨테이너에서 파일을 읽어 데이터가 남아 있는지 확인합니다.
3. 볼륨을 삭제하는 일과 컨테이너를 교체하는 일을 구분합니다.
