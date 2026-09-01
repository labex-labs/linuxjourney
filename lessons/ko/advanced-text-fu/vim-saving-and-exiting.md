---
lesson_id: "vim-saving-and-exiting"
course_id: "advanced-text-fu"
lang: "ko"
order_index: 8
title: "Vim 저장과 종료"
description: "Vim 버퍼 변경을 쓰고 종료하거나 다른 이름으로 저장하거나 의도적으로 버리는 방법을 배웁니다."
meta_title: "Vim 저장과 종료 - Advanced Text-Fu"
meta_description: ":w 같은 명령으로 Vim 편집기에서 저장하는 방법을 배웁니다. :wq나 ZZ로 저장하고 종료하는 방법과 vi의 쓰기 및 종료 명령을 익혀 파일을 효율적으로 관리하세요."
meta_keywords: "vim 저장 방법, linux wq, vi 쓰기 및 종료, vim 저장하고 종료, vim 편집기 저장 방법, vim 파일 저장, vim 종료, vim 명령어"
---

쓰기와 종료는 서로 다른 Vim 작업입니다. Ex 명령을 입력하기 전에 `Esc`를 눌러 일반 모드로 돌아가고 `:`를 입력한 뒤 명령을 쓰고 Enter를 누릅니다. 쓰기가 성공했다고 가정하기 전에 Vim의 상태나 오류 메시지를 읽으세요.

## 현재 버퍼 쓰기

현재 창을 닫지 않고 연결된 파일에 버퍼를 쓰려면 `:w`를 사용합니다.

```vim
:w
```

버퍼에 파일 이름이 없거나 디렉터리에 쓸 수 없거나 파일 시스템이 가득 찼거나 다른 조건이 작업을 막으면 쓰기가 실패할 수 있습니다. Vim이 보고하는 메시지를 확인하세요.

`:w copy.txt`는 현재 버퍼의 기존 이름을 유지하면서 내용을 다른 경로에 씁니다. 버퍼가 새 경로를 사용하도록 하려면 `:saveas copy.txt`를 사용합니다.

:::single-choice{#vim-save-without-quit} 종료하지 않고 현재 버퍼를 연결된 파일에 쓰는 Vim 명령은 무엇인가요?

::option[`:q`]{#vim-save-q explanation="`:q`는 종료를 요청하며 수정된 버퍼를 쓰지 않습니다."}
::option[`:w`]{#vim-save-w .correct explanation="`:write` 명령은 현재 버퍼를 저장하고 편집 창을 열린 채로 둡니다."}
::option[`:q!`]{#vim-save-q-force explanation="`:q!`는 저장하지 않은 변경을 버리고 종료하며 변경을 저장하지 않습니다."}
:::

## 변경되지 않은 버퍼 종료하기

저장하지 않은 버퍼 변경을 버리지 않아도 될 때 현재 창을 닫으려면 `:q`를 사용합니다.

```vim
:q
```

현재 버퍼가 수정되었고 변경을 잃게 된다면 Vim은 일반적으로 종료를 거부하고 경고를 보고합니다. 이 보호 장치는 저장하거나 다시 생각할 기회를 줍니다.

:::single-choice{#vim-quit-clean-buffer} 저장하지 않은 변경을 잃지 않을 때 현재 Vim 창을 종료하는 명령은 무엇인가요?

::option[`:w`]{#vim-quit-w explanation="버퍼를 쓰지만 현재 창을 열린 채로 둡니다."}
::option[`:q`]{#vim-quit-q .correct explanation="일반 종료 명령은 Vim의 수정 버퍼 보호가 허용할 때 창을 닫습니다."}
::option[`u`]{#vim-quit-u explanation="일반 모드 `u`는 변경을 실행 취소하며 편집기 창을 닫지 않습니다."}
:::

## 저장하지 않은 변경 버리기

현재 창을 닫고 원래 종료를 막을 변경을 버리려는 의도가 있을 때만 `:q!`를 사용합니다.

```vim
:q!
```

느낌표는 저장하지 않은 변경 경고를 무시합니다. 해당 버퍼 변경은 기록되지 않으므로 Enter를 누르기 전에 정말 버려도 되는지 확인하세요.

:::single-choice{#vim-quit-discard-changes} 현재 버퍼에 의도적으로 저장하지 않으려는 변경이 있습니다. 현재 창을 종료하고 변경을 버리는 명령은 무엇인가요?

::option[`:q`]{#vim-discard-plain-q explanation="일반 `:q`는 종료로 수정된 버퍼 변경을 잃게 되면 보통 거부합니다."}
::option[`:wq`]{#vim-discard-wq explanation="`:wq`는 종료 전에 변경을 쓰므로 버리기와 반대입니다."}
::option[`:q!`]{#vim-discard-q-force .correct explanation="느낌표는 수정 경고를 무시하고 저장하지 않은 변경을 쓰지 않은 채 닫습니다."}
:::

## 쓰기와 종료 함께 수행하기

버퍼를 쓰고 성공한 뒤 현재 창을 닫으려면 `:wq`를 사용합니다.

```vim
:wq
```

쓰기가 실패하면 Vim은 요청한 종료를 완료하지 않습니다. 데이터가 디스크에 기록됐다고 가정하지 말고 오류를 해결하세요.

:::single-choice{#vim-write-and-quit} 현재 버퍼를 쓰고 성공하면 현재 창을 종료하는 명령은 무엇인가요?

::option[`:wq`]{#vim-save-wq .correct explanation="쓰기와 종료를 결합하며 종료는 쓰기 성공 여부에 따라 달라집니다."}
::option[`:q!`]{#vim-save-force-quit explanation="변경을 쓰지 않고 버리면서 종료합니다."}
::option[`:w copy.txt`]{#vim-save-copy explanation="다른 경로에 쓰지만 편집 창은 열린 채로 둡니다."}
:::

## :x와 ZZ 사용하기

`:x`는 버퍼가 수정되었을 때만 쓴 뒤 종료합니다. 일반 모드에서 대문자 `ZZ`도 같은 수정 시 쓰기 후 종료 동작을 수행합니다.

```vim
:x
```

```text
ZZ
```

버퍼가 변경되지 않았어도 쓰기를 요청하는 `:wq`와는 미묘하게 다릅니다. 대문자 `ZQ`는 일반 모드에서 `:q!`와 비슷하게 쓰지 않고 종료합니다.

:::single-choice{#vim-write-if-modified-quit} 버퍼가 수정되었을 때만 쓰고 종료하는 일반 모드 명령은 무엇인가요?

::option[`ZZ`]{#vim-save-zz .correct explanation="대문자 `ZZ`는 `:x`와 같은 수정 시 쓰기 후 종료 동작을 수행합니다."}
::option[`zz`]{#vim-center-screen explanation="소문자 `zz`는 현재 줄을 창 중앙에 맞추며 저장하거나 종료하지 않습니다."}
::option[`ZQ`]{#vim-quit-zq explanation="대문자 `ZQ`는 쓰지 않고 종료하므로 저장하지 않은 변경을 저장하지 않고 버립니다."}
:::

여러 창이나 버퍼가 관련된 경우 명령이 현재 창만 닫을 수 있습니다. `:qa`, `:wqa`, `:qa!` 같은 명령은 여러 창에 적용되지만 모든 창 강제 명령을 사용하기 전에 수정된 버퍼를 각각 검토하세요.

일회용 파일에서 쓰기와 종료를 연습하려면 다음 실습을 진행해 보세요.

1. **[Vim과 Nano로 Linux 텍스트 파일 편집하기](https://labex.io/ko/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Vim과 Nano로 파일을 만들고 편집하고 저장하고 탐색하며 기본적인 Vim 저장 및 종료 작업을 익힙니다.

## 요약

이제 저장하지 않은 데이터에 대한 의도에 맞는 Vim 종료 명령을 선택할 수 있습니다.

1. `:w`로 종료하지 않고 쓸 수 있습니다.
2. 변경을 잃지 않을 때 `:q`로 안전하게 종료할 수 있습니다.
3. `:q!`로 변경을 의도적으로 버릴 수 있습니다.
4. `:wq`로 쓰고 종료할 수 있습니다.
5. `:x` 또는 `ZZ`로 수정 시 쓰기 동작을 사용할 수 있습니다.
