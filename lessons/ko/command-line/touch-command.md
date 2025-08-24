---
index: 5
lang: "ko"
title: "touch"
meta_title: "touch - 명령줄"
meta_description: "Linux touch 명령어를 사용하여 새 파일을 만들고 타임스탬프를 업데이트하는 방법을 배우세요. 이 초보자 친화적인 가이드는 파일 관리를 이해하는 데 도움이 됩니다."
meta_keywords: "touch command, create files, Linux tutorial, file timestamps, Linux for beginners, Linux guide, basic commands"
---

## Lesson Content

파일을 만드는 방법을 배워봅시다. 아주 간단한 방법은 `touch` 명령어를 사용하는 것입니다. `touch`를 사용하면 비어 있는 새 파일을 만들 수 있습니다.

```bash
touch mysuperduperfile
```

그리고 짠, 새 파일이 생겼습니다!

`touch`는 기존 파일 및 디렉터리의 타임스탬프를 변경하는 데도 사용됩니다. 한번 시도해 보세요: 파일에 `ls -l`을 실행하여 타임스탬프를 확인한 다음, 해당 파일을 `touch`하면 타임스탬프가 업데이트됩니다.

리디렉션 및 텍스트 편집기와 같은 다른 방법을 포함하여 파일을 만드는 다른 많은 방법이 있지만, 이는 텍스트 조작 과정에서 다룰 것입니다.

## Exercise

1. 새 파일을 만듭니다.
2. 타임스탬프를 확인합니다.
3. 파일을 touch 하고 타임스탬프를 다시 확인합니다.

파일 관리 실습을 위해 다음 대화형 랩을 살펴보세요:

- [Linux Directory Navigation](https://labex.io/ko/labs/linux-directory-navigation-387844)
- [Setting Up a New Project Structure](https://labex.io/ko/labs/linux-setting-up-a-new-project-structure-387859)

## Quiz Question

`myfile`이라는 파일을 어떻게 만드나요?

## Quiz Answer

touch myfile
