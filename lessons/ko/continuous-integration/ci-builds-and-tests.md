---
lesson_id: "ci-builds-and-tests"
course_id: "continuous-integration"
lang: "ko"
order_index: 4
title: "빌드와 테스트"
description: "간단한 페이지를 로컬에서 검사하며 준비, 빌드, 테스트를 구분하는 방법을 알아봅니다."
meta_title: "빌드와 테스트 - 지속적 통합"
meta_description: "간단한 페이지를 로컬에서 검사하며 준비, 빌드, 테스트를 구분하는 방법을 알아봅니다."
meta_keywords: "빌드, 테스트, 종료 코드, 지속적 통합, DevOps, Linux Journey"
---

각 과정의 역할이 분명하면 검사에 실패했을 때 결과를 해석하기 쉽습니다. **준비** 과정에서는 입력 파일과 도구를 갖춥니다. **빌드**는 결과물을 만듭니다. **테스트**는 소스나 결과물이 예상한 조건을 만족하는지 확인합니다.

## 입력 파일 준비하기

비어 있는 실습 폴더에 예시 페이지를 작성합니다. 리디렉션은 기존 `index.html`을 덮어쓰므로 새 실습 디렉터리를 사용하세요.

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
```

CI 작업이라면 체크아웃 단계에서 페이지 파일을 받아 옵니다. 프로젝트에 따라 빌드나 테스트를 실행하는 데 필요한 라이브러리나 도구도 설치하는데, 이를 의존성이라고 합니다.

:::single-choice{#ci-builds-and-tests-prepare-input} 복사 명령을 실행하기 전부터 페이지 파일이 없습니다. 어느 과정을 먼저 확인해야 하나요?

::option[이후 작업의 아티팩트 다운로드입니다.]{#ci-builds-and-tests-prepare-input-a explanation="이 결과를 빌드하기 전에 입력 파일이 먼저 있어야 합니다."}
::option[준비 과정입니다.]{#ci-builds-and-tests-prepare-input-b .correct explanation="이 작업에서 입력 파일을 사용할 수 있게 준비했어야 합니다."}
::option[운영 환경의 응답 시간입니다.]{#ci-builds-and-tests-prepare-input-c explanation="이 상황은 러너의 파일과 관련 있습니다."}
:::

## 빌드 결과 만들기

완성된 사이트 파일을 둘 디렉터리에 페이지를 복사합니다.

```bash
$ mkdir -p dist
$ cp index.html dist/index.html
```

`-p` 옵션을 사용하면 디렉터리가 이미 있어도 `mkdir`이 성공합니다. 복사하면 출력 디렉터리에 별도 파일이 생깁니다. 이후 테스트는 이 결과물을 확인할 수 있습니다.

:::single-choice{#ci-builds-and-tests-build-product} 복사가 성공한 뒤 패키지에 담을 수 있는 파일은 무엇인가요?

::option[dist/index.html입니다.]{#ci-builds-and-tests-build-product-a .correct explanation="빌드에서 출력 디렉터리에 사본을 저장했습니다."}
::option[공개 사이트에 배포된 페이지입니다.]{#ci-builds-and-tests-build-product-b explanation="로컬 파일을 복사하는 일만으로 서비스가 실행되지는 않습니다."}
::option[워크플로의 상태 기록입니다.]{#ci-builds-and-tests-build-product-c explanation="이 빌드는 페이지를 만들고, 러너는 검사 상태를 따로 기록합니다."}
:::

## 페이지 테스트하기

빌드 직후 이 검사를 실행합니다. `-F`는 문자열 그대로 검색하고, `-q`는 일치한 줄을 화면에 표시하지 않습니다. 셸은 직전 명령의 종료 코드를 `$?`에 저장합니다. 0은 텍스트를 찾았다는 뜻이고, 1은 일치하는 줄이 없다는 뜻입니다.

```bash
$ grep -Fq '<h1>Welcome</h1>' dist/index.html
$ echo "$?"
```

`0`이 나와야 합니다. 테스트는 빌드된 파일에 해당하는 문자열이 정확히 들어 있는지 검사했습니다. 색상, 브라우저에 표시되는 방식, 응답 시간은 확인하지 않았습니다.

:::single-choice{#ci-builds-and-tests-test-scope} 이 테스트를 통과했습니다. 무엇을 알 수 있나요?

::option[인터넷에서 페이지에 접근할 수 있습니다.]{#ci-builds-and-tests-test-scope-a explanation="이 검사는 로컬 출력 파일을 읽었습니다."}
::option[모든 지원 브라우저에서 페이지가 표시됩니다.]{#ci-builds-and-tests-test-scope-b explanation="이 테스트에서는 브라우저를 사용하지 않았습니다."}
::option[빌드된 파일에 예상한 제목 문자열이 들어 있습니다.]{#ci-builds-and-tests-test-scope-c .correct explanation="grep 명령이 확인한 조건이 바로 이것입니다."}
:::

![LabEx에서 로컬 제목 검사가 성공해 셸 종료 코드 0이 나온 예시](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-builds-and-tests/heading-check.png)

## 요약

이제 간단한 CI 검사의 각 과정에서 무엇을 확인할 수 있는지 구분할 수 있습니다.

1. 빌드에 필요한 입력을 미리 준비합니다.
2. 빌드가 만든 파일을 찾습니다.
3. 종료 코드를 읽고 테스트가 정확히 무엇을 확인했는지 파악합니다.
