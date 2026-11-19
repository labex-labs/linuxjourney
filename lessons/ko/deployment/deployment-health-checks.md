---
lesson_id: "deployment-health-checks"
course_id: "deployment"
lang: "ko"
order_index: 4
title: "상태 검사"
description: "배포 후 프로세스, 서비스, 클라이언트 요청을 차례로 확인하는 방법을 알아봅니다."
meta_title: "상태 검사 - 배포"
meta_description: "배포 후 프로세스, 서비스, 클라이언트 요청을 차례로 확인하는 방법을 알아봅니다."
meta_keywords: "상태 검사, 배포, DevOps, Linux Journey"
---

프로그램이 시작되었더라도 아직 요청을 처리할 준비가 끝나지 않았을 수 있습니다. 단계를 나눠 검사하면 각 검사가 성공했을 때 무엇을 확인한 것인지 알 수 있습니다.

## 프로세스 확인하기

컨테이너 목록에서는 주 프로그램이 실행 중인지 확인할 수 있습니다. 새 배포에서 가장 먼저 확인할 사항입니다. 초기화를 마쳤는지, 브라우저에서 접속할 수 있는지는 별도로 확인해야 합니다.

:::single-choice{#deployment-health-checks-process-scope} 새 컨테이너에 Up이 표시됩니다. 무엇을 알 수 있나요?

::option[방문자에게 새 페이지가 정상적으로 표시됩니다.]{#deployment-health-checks-process-scope-a explanation="컨테이너 상태는 방문자의 요청 결과를 보여 주지 않습니다."}
::option[확인 시점에 컨테이너의 주 프로그램이 실행 중입니다.]{#deployment-health-checks-process-scope-b .correct explanation="Up은 프로세스 상태를 나타냅니다."}
::option[모든 의존 서비스가 검사를 통과했습니다.]{#deployment-health-checks-process-scope-c explanation="의존 서비스의 검사 결과는 표시되지 않습니다."}
:::

## 서비스 엔드포인트 확인하기

**엔드포인트**는 서비스가 요청을 처리하는 주소와 경로입니다. 확인하려는 동작에 맞는 경로를 선택하세요. 로컬에서 실습할 때는 빈 폴더를 사용하세요. 리디렉션으로 버전 파일을 작성합니다. 이 터미널에서 Python 서버를 루프백 주소로 실행해 두고, 실습이 끝나면 Ctrl+C로 종료하세요.

```bash
$ mkdir site
$ printf '%s\n' 2 > site/version.txt
$ python3 -m http.server 8091 --bind 127.0.0.1 --directory site
```

두 번째 터미널에서 버전 파일을 요청하세요. curl의 `-f` 옵션은 HTTP 오류 응답을 실패로 처리합니다. `-sS`는 진행 표시를 숨기면서 오류 메시지는 표시합니다.

```bash
$ curl -fsS http://127.0.0.1:8091/version.txt
```

실습에서 예상하는 값은 `2`입니다. 버전 파일을 요청하는 데 성공해도 사이트의 전체 동작을 검증한 것은 아닙니다.

:::single-choice{#deployment-health-checks-endpoint-mismatch} 요청이 성공했고 1이 출력되었습니다. 무엇을 조사해야 하나요?

::option[해당 주소에서 응답 중인 서비스의 버전입니다.]{#deployment-health-checks-endpoint-mismatch-a .correct explanation="네트워크 접속은 성공했지만 실제로 확인한 버전이 배포하려던 버전과 다릅니다."}
::option[curl이 전혀 접속하지 못하는 이유입니다.]{#deployment-health-checks-endpoint-mismatch-b explanation="값이 돌아왔으므로 연결과 응답은 성공했습니다."}
::option[서비스 이름에 숫자가 들어 있는지입니다.]{#deployment-health-checks-endpoint-mismatch-c explanation="서비스 이름만으로 응답에 나온 버전을 판단할 수 없습니다."}
:::

![LabEx 실습 서버의 루프백 엔드포인트에서 버전 2를 반환한 화면](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-health-checks/version-response.png)

## 클라이언트가 접속하는 위치에서 확인하기

서비스 호스트에서 요청이 성공하면 사용자가 보통 접속하는 위치에서도 안전한 검사를 반복하세요. 로드 밸런서, 프록시, 네트워크 규칙으로 인해 요청이 다른 경로를 거칠 수 있습니다. 확인한 주소와 받은 응답을 기록하세요. 결과가 릴리스와 일치하지 않으면 배포 상태를 계속 조사하세요.

:::single-choice{#deployment-health-checks-user-path} 로컬 요청은 2를 반환하고 공개 테스트 주소는 1을 반환합니다. 다음에 가장 먼저 무엇을 확인하면 좋을까요?

::option[로컬 요청의 출력 줄 수를 셉니다.]{#deployment-health-checks-user-path-a explanation="줄 수로는 공개 주소에서 어떤 서비스가 응답하는지 알 수 없습니다."}
::option[같은 로컬 검사만 반복합니다.]{#deployment-health-checks-user-path-b explanation="로컬 경로에서 버전 2를 반환한다는 점은 이미 확인했습니다."}
::option[공개 경로가 어느 버전의 서비스로 연결되는지 확인합니다.]{#deployment-health-checks-user-path-c .correct explanation="두 경로에서 서로 다른 응답이 돌아왔습니다."}
:::

## 요약

이제 배포 후 각 검사에서 무엇을 확인했는지 설명할 수 있습니다.

1. 주 프로그램이 실행 중인지 확인합니다.
2. 엔드포인트에 요청을 보내 예상한 버전이 표시되는지 확인합니다.
3. 사용자가 접속하는 경로를 별도로 확인합니다.
