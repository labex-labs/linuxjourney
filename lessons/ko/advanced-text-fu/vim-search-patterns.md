---
lesson_id: "vim-search-patterns"
course_id: "advanced-text-fu"
lang: "ko"
order_index: 4
title: "Vim 검색 패턴"
description: "Vim에서 앞이나 뒤로 검색하고 패턴 일치를 반복하거나 조정하고 지우는 방법을 배웁니다."
meta_title: "Vim 검색 패턴 - Advanced Text-Fu"
meta_description: "패턴을 사용해 Vim에서 앞뒤로 검색하는 방법을 배웁니다. Vim 검색 기술을 익혀 텍스트를 빠르게 찾고 n과 N으로 결과를 탐색하세요."
meta_keywords: "Vim 검색, vim lookup, Vim 명령어, Linux 텍스트 편집기, Vim 튜토리얼, Vim 가이드, 검색 패턴"
---

Vim은 현재 커서 위치에서 패턴을 사용해 검색합니다. 일반 모드에서 앞이나 뒤 검색을 시작한 뒤 패턴을 다시 입력하지 않고 일치 항목을 반복해서 찾을 수 있습니다.

## 앞으로 검색하기

일반 모드에서 `/`를 입력하고 패턴을 쓴 뒤 Enter를 누릅니다. Vim은 커서 뒤의 다음 일치 항목으로 이동합니다.

```vim
/pretty
```

검색에는 Vim 정규 표현식 구문을 사용하므로 `.`, `*`, `[`, `\` 같은 문자에 특별한 의미가 있을 수 있습니다. 패턴의 나머지를 거의 모두 문자 그대로 처리하려면 시작에 `\V`를 사용하거나 특수 문자를 의도적으로 이스케이프하세요.

:::single-choice{#vim-search-forward-key}
일반 모드에서 `pretty`를 앞으로 검색하기 시작하는 명령은 무엇인가요?

::option[`?pretty`를 입력하고 Enter를 누릅니다.]{#vim-backward-pretty explanation="물음표는 현재 커서 위치에서 뒤쪽 검색을 시작합니다."}
::option[`/pretty`를 입력하고 Enter를 누릅니다.]{#vim-forward-pretty .correct explanation="슬래시는 앞으로 검색을 시작하고 Enter는 패턴을 제출합니다."}
::option[`:pretty`를 입력하고 Enter를 누릅니다.]{#vim-command-pretty explanation="콜론은 Ex 명령을 위한 명령줄 모드로 들어가며 이 방식으로 `pretty`를 검색으로 시작하지 않습니다."}
:::

## 뒤로 검색하기

`?`를 입력하고 패턴을 쓴 뒤 Enter를 누르면 커서 앞의 이전 일치 항목으로 이동합니다.

```vim
?pretty
```

이 동작이 본질적으로 “파일의 마지막 일치 항목”을 뜻하지는 않습니다. 결과는 현재 커서 위치에 따라 달라집니다. Vim의 기본 `wrapscan` 설정에서는 검색이 시작이나 끝에서 순환할 수 있고 `:set nowrapscan`은 순환을 비활성화합니다.

:::single-choice{#vim-search-backward-key}
커서에서 앞쪽의 이전 텍스트를 향해 찾는 일반 모드 검색 접두사는 무엇인가요?

::option[`/`]{#vim-slash-forward explanation="슬래시는 이전 텍스트가 아니라 커서에서 앞으로 검색합니다."}
::option[`?`]{#vim-question-backward .correct explanation="물음표는 현재 커서 위치에서 뒤쪽 패턴 검색을 시작합니다."}
::option[`:`]{#vim-colon-command explanation="콜론은 Ex 명령줄을 시작하며 뒤 검색 접두사가 아닙니다."}
:::

## 검색 반복하기

어느 방향으로 검색했든 이후에는 다음 키를 사용합니다.

- `n`: 원래 검색 방향으로 반복
- `N`: 반대 방향으로 반복

따라서 `/pretty` 뒤에는 `n`이 앞으로, `N`이 뒤로 이동합니다. `?pretty` 뒤에는 `n`이 뒤로, `N`이 앞으로 이동합니다.

:::single-choice{#vim-repeat-backward-search}
`?error`를 실행한 뒤 같은 뒤쪽 방향으로 검색을 반복하는 키는 무엇인가요?

::option[`n`]{#vim-same-question-search .correct explanation="소문자 `n`은 가장 최근 검색을 원래 방향으로 반복하며 여기서는 뒤쪽입니다."}
::option[`N`]{#vim-opposite-question-search explanation="대문자 `N`은 원래 검색 방향을 뒤집으므로 `?` 검색 뒤에는 앞으로 이동합니다."}
::option[`/`]{#vim-new-forward-search explanation="슬래시는 새 앞으로 검색을 시작하고 패턴 입력을 기다리며 이전 검색을 반복하지 않습니다."}
:::

## 커서 아래 단어 검색하기

일반 모드에서 커서를 단어 위에 두고 다음 키를 사용합니다.

- `*`: 해당 전체 단어를 앞으로 검색
- `#`: 해당 전체 단어를 뒤로 검색

이 명령은 최신 검색 패턴을 설정하므로 `n`과 `N`으로 계속 탐색할 수 있습니다.

:::single-choice{#vim-current-word-forward}
커서 아래의 전체 단어를 앞으로 검색하는 일반 모드 키는 무엇인가요?

::option[`#`]{#vim-hash-current-word explanation="해시 키는 커서 아래 단어를 뒤로 검색합니다."}
::option[`*`]{#vim-star-current-word .correct explanation="별표 명령은 커서 아래 단어로 전체 단어 패턴을 만들고 앞으로 검색합니다."}
::option[`n`]{#vim-repeat-current-pattern explanation="`n`은 기존 검색을 반복하며 현재 단어로 패턴을 먼저 만들지는 않습니다."}
:::

## 대소문자와 강조 표시 제어하기

Vim 옵션으로 대소문자 동작을 바꿀 수 있습니다.

- `:set ignorecase`: 검색에서 대소문자 차이를 무시
- `:set smartcase`: `ignorecase`도 설정된 상태에서 대문자가 있으면 대소문자를 다시 구분
- 패턴의 `\c`: 해당 검색에서 대소문자를 무시하도록 강제
- 패턴의 `\C`: 해당 검색에서 대소문자를 구분하도록 강제

예를 들어 `/\cerror`는 현재 대소문자 옵션과 관계없이 `error`, `Error`, `ERROR`와 일치합니다.

검색 강조 표시가 활성화되어 있을 때 `:nohlsearch`는 검색 패턴을 삭제하지 않고 현재 시각적 강조만 지웁니다. 다음 검색이나 반복에서 일치 항목이 다시 강조될 수 있습니다.

:::single-choice{#vim-force-case-insensitive}
현재 대소문자 옵션과 관계없이 `error`를 한 번의 Vim 검색에서 대소문자를 무시하도록 강제하는 패턴은 무엇인가요?

::option[`/\Cerror`]{#vim-pattern-match-case explanation="대문자 `\C`는 반대로 대소문자 구분 일치를 강제합니다."}
::option[`/:error`]{#vim-pattern-colon-error explanation="이 패턴 안의 콜론은 문자 그대로이며 대소문자 처리를 선택하지 않습니다."}
::option[`/\cerror`]{#vim-pattern-ignore-case .correct explanation="`\c` 원자는 해당 검색을 대소문자 비구분으로 만들어 여러 대문자 변형과 일치할 수 있게 합니다."}
:::

통제된 파일에서 Vim 탐색과 검색을 연습하려면 다음 실습을 진행해 보세요.

1. **[Vim과 Nano로 Linux 텍스트 파일 편집하기](https://labex.io/ko/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Vim과 Nano로 텍스트 파일을 만들고 편집하고 저장하고 탐색합니다.

## 요약

이제 Vim 버퍼를 검색하고 일치 항목 사이를 예측 가능하게 이동할 수 있습니다.

1. `/`로 앞으로, `?`로 뒤로 검색을 시작할 수 있습니다.
2. `n`으로 같은 방향, `N`으로 반대 방향으로 반복할 수 있습니다.
3. `*` 또는 `#`으로 커서 아래 전체 단어를 검색할 수 있습니다.
4. 한 패턴이나 옵션을 통해 대소문자 동작을 제어할 수 있습니다.
5. 현재 검색 패턴을 잃지 않고 강조 표시를 지울 수 있습니다.
