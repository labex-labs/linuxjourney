---
lesson_id: "git-commits"
course_id: "git"
lang: "ko"
order_index: 4
title: "커밋"
description: "스테이징된 상태를 저장하고 Git 이력에서 해당 커밋을 찾는 방법을 알아봅니다."
meta_title: "커밋 - Git"
meta_description: "스테이징된 상태를 저장하고 Git 이력에서 해당 커밋을 찾는 방법을 알아봅니다."
meta_keywords: "커밋, git, devops, Linux Journey"
---

**커밋**에는 스테이징 영역에서 고른 파일의 상태가 기록됩니다. 변경 내용을 설명하는 메시지와 작성자, 이전 커밋과의 관계도 함께 기록됩니다. Git이 부여한 식별자를 사용하면 이력에서 그 커밋을 정확히 찾을 수 있습니다.

## 실습 저장소의 작성자 정보 설정하기

Git은 커밋에 이름과 이메일 주소를 기록합니다. 이 저장소에서만 쓸 실습용 값을 설정하세요. 이 값은 이력에 표시되는 정보이며 원격 서비스의 접근 권한과는 관계가 없습니다.

```bash
$ git config --local user.name "Journey Learner"
$ git config --local user.email "learner@example.com"
```

`index.html`을 스테이징해 둔 실습 저장소를 사용합니다. 어떤 파일이 커밋에 들어가는지 확인하려면 `git status`를 실행하세요.

:::single-choice{#git-commits-identity-scope} 여기서 --local을 지정하면 어떻게 되나요?

::option[공유 호스팅 서비스에 로그인합니다.]{#git-commits-identity-scope-b explanation="이름과 이메일은 커밋에 기록되는 정보입니다. 원격 서비스 인증은 별도로 진행합니다."}
::option[이 저장소에서 쓸 작성자 정보를 설정합니다.]{#git-commits-identity-scope-a .correct explanation="로컬 설정은 현재 저장소에 적용됩니다."}
::option[기존 커밋의 작성자를 모두 바꿉니다.]{#git-commits-identity-scope-c explanation="이 설정은 앞으로 생성할 커밋에 쓰입니다."}
:::

## 스테이징한 상태 저장하기

원하는 버전을 스테이징한 뒤 `git commit`을 실행합니다. `-m` 옵션을 사용하면 명령줄에서 커밋 메시지를 지정할 수 있습니다.

```bash
$ git commit -m "Set the homepage heading"
```

커밋은 스테이징한 파일 버전을 저장합니다. 스테이징한 뒤 작업 트리의 파일을 다시 편집하면, 편집한 내용을 다시 스테이징하기 전까지는 커밋에 들어가지 않습니다.

:::single-choice{#git-commits-staged-snapshot} Welcome을 스테이징한 뒤 제목을 Hi로 바꾸고 다시 스테이징하지 않았습니다. 커밋에는 어떤 제목이 들어가나요?

::option[스테이징했을 때의 제목인 Welcome이 들어갑니다.]{#git-commits-staged-snapshot-c .correct explanation="커밋은 스테이징 영역에 담긴 내용을 읽어 저장합니다."}
::option[디스크에서 가장 최신인 Hi가 들어갑니다.]{#git-commits-staged-snapshot-a explanation="작업 트리의 최신 내용과 스테이징한 내용은 다를 수 있습니다."}
::option[Git이 모든 편집을 자동 저장하므로 둘 다 들어갑니다.]{#git-commits-staged-snapshot-b explanation="스테이징 영역에는 파일마다 선택한 버전 하나가 담깁니다."}
:::

## 짧은 형식으로 이력 읽기

`git log --oneline`을 사용하면 이력을 짧은 형식으로 볼 수 있습니다. 각 줄에는 축약한 커밋 식별자와 메시지가 차례로 표시됩니다. 실제 식별자는 예시와 다릅니다.

```text
$ git log --oneline
a12c345 Set the homepage heading
```

서로 다른 커밋에 같은 메시지를 붙일 수 있으므로, 특정 커밋을 가리킬 때는 식별자를 사용합니다. 보통 현재 이력에서 가장 최근 커밋이 맨 위에 나옵니다.

:::single-choice{#git-commits-identify-snapshot} 두 커밋의 메시지가 모두 Set the homepage heading입니다. 두 커밋의 저장 상태를 어떻게 구분하나요?

::option[둘의 공통 커밋 메시지로 구분합니다.]{#git-commits-identify-snapshot-a explanation="여러 커밋에 같은 메시지를 쓸 수 있습니다."}
::option[두 변경에 모두 포함된 파일 이름으로 구분합니다.]{#git-commits-identify-snapshot-c explanation="하나의 파일이 여러 커밋에 포함될 수 있습니다."}
::option[커밋 식별자로 구분합니다.]{#git-commits-identify-snapshot-b .correct explanation="식별자를 사용하면 이력의 특정 항목을 가리킬 수 있습니다."}
:::

브라우저 터미널에서 스테이징과 커밋을 연습하려면 [첫 Git 실습](https://labex.io/tutorials/git-your-first-git-lab-92739)을 해 보세요.

## 요약

이제 스테이징한 작업을 저장하고 이력에서 찾을 수 있습니다.

1. 실습 저장소에 커밋 작성자 정보를 설정합니다.
2. 변경이 드러나는 메시지와 함께 스테이징한 상태를 저장합니다.
3. 짧은 형식의 이력에서 커밋을 식별합니다.
