---
lesson_id: "vim-text-editor"
course_id: "advanced-text-fu"
lang: "ko"
order_index: 3
title: "Vim (Vi Improved)"
description: "Vim이 무엇인지, vi와 어떤 관계인지, 파일과 도움말 및 안내형 연습을 여는 방법을 배웁니다."
meta_title: "Vim (Vi Improved) - Advanced Text-Fu"
meta_description: "Vi Improved라는 이름의 강력하고 가벼운 텍스트 편집기 Vim을 알아봅니다. 대부분의 Linux 시스템에서 사용할 수 있는 vim vi improved의 핵심을 소개합니다."
meta_keywords: "Vim, vi improved, vim vi improved, Linux 텍스트 편집기, Vim 튜토리얼, Vi 편집기, vim improved, Linux 명령어"
---

Vim은 이름이 **Vi Improved**를 뜻하는 구성 가능한 텍스트 편집기입니다. 원래 `vi` 편집기와 관련된 모달 편집 모델을 유지하면서 다단계 실행 취소, 구문 지원, 스크립팅, 방대한 도움말 시스템 같은 기능을 추가합니다.

## Vim과 vi의 관계 이해하기

`vi`는 역사적인 편집기와 일반적인 명령 인터페이스를 모두 가리킵니다. 어떤 Linux 시스템에서는 `vi`가 호환성 중심 모드의 Vim을 시작하고 다른 시스템에서는 별도의 vi 구현을 시작할 수 있습니다. 모든 `vi` 명령이 모든 Vim 기능을 제공한다고 가정하지 마세요.

현재 쉘에서 무엇으로 해석되는지 확인합니다.

```bash
$ command -v vim
/usr/bin/vim
$ command -v vi
/usr/bin/vi
```

해석된 경로만으로 `vi`와 `vim`이 같은 구현인지 알 수는 없습니다. `type -a vi vim`과 편집기의 버전 출력으로 더 자세히 확인할 수 있습니다.

:::single-choice{#vim-name-origin} Vim이라는 이름은 무엇을 뜻하나요?

::option[Visual Input Manager]{#vim-visual-input explanation="이 확장은 편집기 이름의 기원이 아닙니다."}
::option[Virtual Interface Mode]{#vim-virtual-interface explanation="Vim이 모드를 사용하기는 하지만 이 문구가 이름을 나타내지는 않습니다."}
::option[Vi Improved]{#vim-vi-improved .correct explanation="Vim은 향상된 vi 호환 편집기로 시작했으며 그 사실이 이름에 반영되어 있습니다."}
:::

:::single-choice{#vim-check-command} Bash가 현재 `vim`이라는 이름을 해석할 수 있는지 확인하는 명령어는 무엇인가요?

::option[`vim --create`]{#vim-create-option explanation="쉘 해석 확인 명령이 아니며 Vim을 설치하거나 찾는 방법도 아닙니다."}
::option[`command -v vim`]{#vim-command-resolution .correct explanation="쉘 내장 명령은 사용할 수 있을 때 해당 이름에 사용될 명령을 보고합니다."}
::option[`file ~/.vimrc`]{#vim-file-vimrc explanation="가능한 구성 파일 하나를 검사할 뿐 Vim 실행 파일을 사용할 수 있는지는 확정하지 못합니다."}
:::

## Vim과 파일 열기

이름 없는 버퍼로 Vim을 시작합니다.

```bash
$ vim
```

파일을 편집하려면 경로를 전달합니다.

```bash
$ vim filename.txt
```

`filename.txt`가 존재하고 읽을 수 있으면 Vim은 내용을 버퍼에 불러옵니다. 경로가 없으면 그 이름과 연결된 새 버퍼를 열며 버퍼를 성공적으로 쓰기 전에는 파일을 만들지 않습니다.

Vim은 파일 시스템 권한을 우회하지 않습니다. 파일을 열 수 있다고 해서 계정이 그 경로에 변경 사항을 저장할 수 있다는 뜻은 아닙니다.

:::single-choice{#vim-open-missing-path} `vim draft.txt`에서 아직 존재하지 않는 경로를 지정하면 일반적으로 어떻게 되나요?

::option[Vim이 새 버퍼를 열고 쓸 때만 파일을 만듭니다.]{#vim-new-buffer .correct explanation="버퍼가 경로를 기억하지만 디스크 파일 생성은 성공적인 저장까지 미뤄집니다."}
::option[Vim이 인터페이스를 열기 전에 디스크에 빈 파일을 만듭니다.]{#vim-immediate-create explanation="새 버퍼가 경로와 연결되지만 파일은 성공적으로 쓰기 전까지 만들어지지 않습니다."}
::option[모든 경로가 이미 존재해야 하므로 Vim이 시작을 거부합니다.]{#vim-refuse-missing explanation="Vim은 없는 경로에 새 버퍼를 열어 새 파일 내용을 작성할 수 있습니다."}
:::

## 내장 학습 자료 사용하기

Vim 설치에 `vimtutor`가 포함되어 있다면 쉘에서 실행하여 대화형 연습 레슨을 시작합니다.

```bash
$ vimtutor
```

Vim 안에서는 `Esc`로 일반 모드에 들어가 `:help`를 입력하고 Enter를 눌러 도움말 시스템을 엽니다. 명령 뒤에 특정 주제를 붙일 수 있습니다.

```vim
:help user-manual
:help :write
```

도움말 태그는 정확하므로 문장 부호가 중요할 수 있습니다. 도움말 링크에서 `Ctrl+]`를 누르면 링크를 따라가고 `Ctrl+T`를 누르면 돌아옵니다.

:::single-choice{#vim-guided-tutorial} 설치되어 있을 때 Vim의 안내형 튜토리얼을 시작하는 쉘 명령어는 무엇인가요?

::option[`vim --quiz`]{#vim-quiz-option explanation="Vim은 이 옵션을 표준 안내형 튜토리얼 인터페이스로 사용하지 않습니다."}
::option[`vimtutor`]{#vim-tutor-command .correct explanation="`vimtutor`는 안전한 실습을 위해 설계된 대화형 튜토리얼 사본을 엽니다."}
::option[`help vim`]{#vim-shell-help explanation="Bash `help`는 쉘 내장 명령을 문서화하며 Vim의 대화형 튜토리얼을 시작하지 않습니다."}
:::

## 일회용 파일로 연습하기

자신이 소유한 디렉터리의 파일로 시작합니다.

```bash
$ printf 'alpha\nbeta\n' > vim-practice.txt
$ vim vim-practice.txt
```

이어지는 레슨에서는 검색, 탐색, 삽입, 편집, 저장을 소개합니다. 안전하게 나가는 방법을 익힐 때까지 `Esc`가 일반 모드로 돌아가고 `:q!` 뒤에 Enter를 누르면 현재 창의 저장하지 않은 변경을 버린다는 점을 기억하세요. 변경을 버리려는 의도가 있을 때만 이 명령을 사용합니다.

:::single-choice{#vim-abandon-practice-changes} 일회용 연습 파일에서 현재 창을 종료하고 저장하지 않은 변경을 버리는 Vim 명령은 무엇인가요?

::option[`:w`]{#vim-write-only explanation="`:w`는 버퍼를 쓰지만 현재 창을 종료하지 않습니다."}
::option[`:wq`]{#vim-write-quit explanation="`:wq`는 종료하기 전에 변경을 저장하므로 변경을 버리지 않습니다."}
::option[`:q!`]{#vim-quit-force .correct explanation="`!`는 수정된 버퍼 경고를 무시하고 변경을 쓰지 않은 채 종료하도록 Vim에 지시합니다."}
:::

Vim으로 파일 열기, 편집, 저장을 연습하려면 다음 실습을 진행해 보세요.

1. **[Vim과 Nano로 Linux 텍스트 파일 편집하기](https://labex.io/ko/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - 실제 Linux 환경에서 Vim과 Nano로 파일 생성, 텍스트 편집, 저장, 탐색을 연습합니다.

## 요약

이제 Vim을 식별하고 버퍼를 열며 안전한 학습 자료를 찾을 수 있습니다.

1. 하나의 구현이라고 가정하지 않고 Vim과 vi의 관계를 설명할 수 있습니다.
2. `vim` 명령을 사용할 수 있는지 확인할 수 있습니다.
3. 기존 파일이나 이름이 지정된 새 버퍼를 열 수 있습니다.
4. `vimtutor`를 시작하거나 Vim 내장 도움말을 열 수 있습니다.
5. 의도한 경우에만 저장하지 않은 연습 변경을 버릴 수 있습니다.
