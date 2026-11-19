---
lesson_id: "ci-build-artifacts"
course_id: "continuous-integration"
lang: "ko"
order_index: 6
title: "빌드 아티팩트"
description: "CI가 만든 파일을 해당 실행과 소스 리비전에 연결하는 방법을 알아봅니다."
meta_title: "빌드 아티팩트 - 지속적 통합"
meta_description: "CI가 만든 파일을 해당 실행과 소스 리비전에 연결하는 방법을 알아봅니다."
meta_keywords: "빌드 아티팩트, 소스 리비전, 지속적 통합, DevOps, Linux Journey"
---

**빌드 아티팩트**는 나중에 쓰려고 실행 결과에서 따로 보관하는 파일이나 파일 묶음입니다. 테스트 보고서나 사이트 압축 파일이 그 예입니다. 아티팩트를 만든 실행과 리비전을 함께 기록하면, 검토하는 사람이 어떤 소스에서 나왔는지 알 수 있습니다.

## 출력 디렉터리를 압축 파일로 만들기

빌드된 페이지가 `dist`에 있는 실습 폴더를 사용합니다. 이 예시는 디렉터리 내용을 한 파일로 묶은 압축 아카이브를 만듭니다. 현재 폴더에 같은 이름의 아카이브가 있으면 덮어씁니다.

```bash
$ tar -czf site.tar.gz -C dist .
$ tar -tzf site.tar.gz
```

첫 번째 명령의 `-c`는 아카이브를 만들고, `-z`는 압축하고, `-f`는 출력 파일 이름을 지정합니다. `-C dist .`는 tar가 `dist`에서 시작하도록 합니다. 두 번째 명령은 `-t`로 아카이브의 파일 목록을 표시합니다. 파일을 공유하기 전에 `./index.html`이 들어 있는지 확인하세요.

:::single-choice{#ci-build-artifacts-inspect-archive} 페이지 파일이 들어 있는지 어떻게 확인하나요?

::option[tar -tzf site.tar.gz로 아카이브의 목록을 표시합니다.]{#ci-build-artifacts-inspect-archive-b .correct explanation="목록에서 index.html이 안에 있는지 알 수 있습니다."}
::option[아카이브를 다시 만듭니다.]{#ci-build-artifacts-inspect-archive-a explanation="다시 만들기만 하면 검토할 항목이 표시되지 않습니다."}
::option[파일 이름만 읽습니다.]{#ci-build-artifacts-inspect-archive-c explanation="아카이브 이름으로는 내용물을 알 수 없습니다."}
:::

![site.tar.gz에 index.html이 포함되어 있음을 보여 주는 tar 목록](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-build-artifacts/archive-contents.png)

## 아티팩트와 실행 연결하기

워크플로는 완성한 압축 파일을 업로드할 수 있습니다. 실행 화면에는 빌드한 리비전이 표시됩니다. 이름이 똑같이 `site.tar.gz`라도 서로 다른 리비전에서 만들면 내용이 다를 수 있습니다. 내려받을 파일을 고를 때 실행과 리비전을 함께 확인하세요.

:::single-choice{#ci-build-artifacts-choose-run} 41번과 42번 실행에 모두 site.tar.gz가 있습니다. 검토한 리비전의 패키지는 어떻게 찾나요?

::option[site.tar.gz라는 이름으로 먼저 보이는 파일을 고릅니다.]{#ci-build-artifacts-choose-run-b explanation="이름으로는 어떤 소스로 만들었는지 알 수 없습니다."}
::option[리비전과 관계없이 가장 최근에 성공한 실행을 고릅니다.]{#ci-build-artifacts-choose-run-c explanation="더 최근 실행도 다른 소스 파일로 성공했을 수 있습니다. 사용하려는 리비전과 맞춰 보세요."}
::option[기록된 리비전이 검토한 리비전과 같은 실행을 고릅니다.]{#ci-build-artifacts-choose-run-a .correct explanation="여러 실행에서 같은 파일 이름을 쓸 수 있습니다."}
:::

## 아카이브와 컨테이너 이미지 구분하기

사이트 아카이브에는 압축을 풀어 쓸 수 있는 파일이 들어 있습니다. 컨테이너 이미지에는 Docker가 컨테이너를 시작할 때 쓰는 파일 시스템과 설정이 들어 있습니다. 워크플로는 이미지를 레지스트리에 게시할 수 있습니다. 해당 이미지에서 컨테이너를 실행할 계획이라면 이미지 참조와 소스 리비전을 함께 기록합니다.

:::single-choice{#ci-build-artifacts-deployable-type} 다음 과정에서 레지스트리의 이미지로 컨테이너를 시작해야 합니다. 어느 결과를 참조해야 하나요?

::option[실행에서 다운로드한 테스트 보고서입니다.]{#ci-build-artifacts-deployable-type-a explanation="보고서는 결과를 설명하지만 컨테이너 파일 시스템을 제공하지 않습니다."}
::option[게시한 컨테이너 이미지의 참조입니다.]{#ci-build-artifacts-deployable-type-c .correct explanation="Docker는 이 참조를 사용해 준비된 이미지를 가져옵니다."}
::option[사이트 아카이브의 파일 이름입니다.]{#ci-build-artifacts-deployable-type-b explanation="아카이브에 페이지 파일이 들어 있지만 레지스트리의 이미지를 식별할 수는 없습니다."}
:::

## 요약

이제 빌드 아티팩트를 식별하고 어디에서 만들어졌는지 추적할 수 있습니다.

1. 빌드한 파일을 묶고 내용을 확인합니다.
2. 어느 실행과 소스 리비전에서 만들었는지 확인합니다.
3. 다음 단계에 필요한 것이 파일 아티팩트인지 컨테이너 이미지인지 판단합니다.
