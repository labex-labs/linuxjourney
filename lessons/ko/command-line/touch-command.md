---
lesson_id: "touch-command"
course_id: "command-line"
lang: "ko"
order_index: 5
title: "touch"
description: "touch 명령어로 빈 파일을 만들고 파일 타임스탬프를 관리하는 방법을 배웁니다."
meta_title: "touch - 명령어 사용법"
meta_description: "빈 파일 생성, 타임스탬프 업데이트, 날짜 설정, 참조 파일 사용, 덮어쓰기 방지 등 Linux touch 명령어 예제와 함께 배우기."
meta_keywords: "linux touch 명령어, touch 명령어, 파일 생성 linux, 타임스탬프 업데이트 linux, touch -d, touch -r, touch -c"
---

`touch` 명령어는 파일 타임스탬프를 변경하며, 하나 이상의 빈 파일을 만드는 데에도 흔히 사용됩니다.

기본 구문은 다음과 같습니다:

```bash
touch [OPTIONS] FILE...
```

## 빈 파일 만들기

빈 파일을 생성하는 가장 간단한 방법은 `touch` 뒤에 파일 이름을 적는 것입니다. 파일이 존재하지 않으면 `touch`가 새로 만듭니다.

```bash
$ touch mysuperduperfile
```

이 명령어를 실행하면 현재 디렉터리에 `mysuperduperfile`이라는 새 빈 파일이 생성됩니다. 여러 파일을 한 번에 생성하려면 파일 이름을 나열하면 됩니다.

```bash
$ touch file1.txt file2.txt file3.log
```

자리 표시자 파일을 만들 때 유용하지만 `touch`는 파일에 텍스트를 추가하지 않습니다. 내용이 필요한 파일에는 텍스트 편집기나 쓰기용 명령어를 사용하세요.

:::single-choice{#create-several-empty-files} 아직 존재하지 않는 `one`, `two`, `three`라는 빈 파일 세 개를 만드는 명령어는 무엇인가요?

::option[`touch "one two three"`]{#touch-one-spaced explanation="따옴표 때문에 공백이 포함된 파일 이름 하나로 처리되므로 세 파일이 아닌 한 파일을 대상으로 합니다."}
::option[`mkdir one two three`]{#mkdir-three explanation="`mkdir`는 빈 일반 파일이 아니라 디렉터리를 만듭니다. 여기서는 `touch`를 사용해야 합니다."}
::option[`touch one two three`]{#touch-three .correct explanation="`touch`는 여러 파일 피연산자를 받을 수 있으며, 없는 파일마다 내용을 추가하지 않고 새 파일을 만듭니다."}
:::

## 파일 타임스탬프 업데이트하기

파일에는 여러 타임스탬프가 있습니다. 기존 파일에 `touch`를 실행하면 기본적으로 접근 시간과 수정 시간이 현재 시간으로 바뀌며 파일 내용은 그대로 유지됩니다.

`ls -l`로 파일의 타임스탬프를 확인하고, `touch`를 실행한 후 다시 확인해보면 알 수 있습니다.

```bash
$ ls -l mysuperduperfile
$ touch mysuperduperfile
$ ls -l mysuperduperfile
```

`ls -l` 출력은 보통 접근 시간이 아니라 수정 시간을 보여 줍니다.

:::single-choice{#touch-existing-file} 이미 존재하는 `report.txt`에 `touch report.txt`를 실행하면 어떻게 되나요?

::option[내용은 그대로 두고 타임스탬프를 업데이트합니다.]{#timestamps-only .correct explanation="기본적으로 `touch`는 기존 파일의 접근 시간과 수정 시간을 갱신하며 파일 데이터를 덮어쓰지 않습니다."}
::option[내용을 삭제해 파일을 비웁니다.]{#contents-deleted explanation="빈 파일 생성은 파일이 없을 때의 동작입니다. 기존 파일은 타임스탬프가 바뀌어도 내용을 유지합니다."}
::option[파일 이름이 이미 사용 중이므로 실패합니다.]{#existing-error explanation="`touch`는 없는 파일뿐 아니라 기존 파일에도 사용하도록 설계되었습니다. 이름이 이미 존재한다는 사실 자체는 오류가 아닙니다."}
:::

## 변경할 타임스탬프 선택하기

`-a`는 접근 시간만, `-m`은 수정 시간만 변경합니다.

```bash
$ touch -a notes.txt
$ touch -m notes.txt
```

:::single-choice{#change-modification-time-only} `notes.txt`의 수정 시간만 업데이트하는 명령어는 무엇인가요?

::option[`touch -a notes.txt`]{#access-only explanation="`-a`는 접근 시간만 바꾸므로 요청한 수정 시간을 선택하지 않습니다."}
::option[`touch -m notes.txt`]{#modification-only .correct explanation="`-m`은 수정 시간만 변경하도록 제한하며 접근 시간은 그대로 둡니다."}
::option[`touch -c notes.txt`]{#no-create explanation="`-c`는 없는 파일의 생성 여부를 제어할 뿐, 하나의 타임스탬프만 선택하지는 않습니다."}
:::

## 시간 설정 또는 복사하기

`-d` 옵션은 현재 시간 대신 날짜 문자열을 받습니다.

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

`-r` 옵션으로 참조 파일의 타임스탬프를 복사할 수 있습니다.

```bash
$ touch -r file1.txt file2.txt
```

여기서 `file1.txt`는 타임스탬프를 제공하고 `file2.txt`가 변경됩니다. `-t` 옵션을 사용하면 압축된 숫자 형식으로 시간을 지정할 수도 있습니다.

:::single-choice{#copy-reference-timestamps} `source.txt`의 타임스탬프를 `target.txt`에 복사하는 명령어는 무엇인가요?

::option[`touch -r source.txt target.txt`]{#reference-source .correct explanation="`-r` 다음 피연산자가 참조 파일이고 마지막 피연산자가 타임스탬프를 업데이트할 파일입니다."}
::option[`touch -r target.txt source.txt`]{#reference-target explanation="두 파일의 역할을 뒤집었습니다. `target.txt`를 참조로 삼아 `source.txt`를 변경하게 됩니다."}
::option[`touch -d source.txt target.txt`]{#date-source explanation="`-d`는 참조 파일 이름이 아니라 날짜 문자열을 받습니다. 다른 파일의 시간을 복사할 때는 `-r`을 사용합니다."}
:::

## 파일 생성 방지하기

`-c` 옵션은 파일이 이미 존재할 때만 업데이트하며, 없으면 새로 만들지 않습니다.

```bash
$ touch -c existing-file.txt
```

파일이 없으면 이 명령어는 파일을 만들지 않습니다. 새 파일을 추가하지 않고 타임스탬프만 갱신해야 하는 스크립트에서 유용합니다.

:::single-choice{#update-without-creating} `status.log`가 있으면 업데이트하되 없으면 만들지 않는 명령어는 무엇인가요?

::option[`touch -a status.log`]{#touch-access explanation="`-a`는 접근 시간을 선택하지만 없는 파일은 여전히 생성될 수 있으므로 생성 방지 조건을 충족하지 않습니다."}
::option[`touch -m status.log`]{#touch-modification explanation="`-m`은 수정 시간을 선택하지만 없는 파일의 생성을 막지 않습니다. 그 조건에는 `-c`를 사용합니다."}
::option[`touch -c status.log`]{#touch-no-create .correct explanation="`-c`는 없는 파일의 생성을 막으며, 기존 파일의 타임스탬프는 계속 업데이트할 수 있습니다."}
:::

## 요약

이제 `touch`로 빈 파일을 만들고 파일 타임스탬프를 제어할 수 있습니다.

1. 하나 이상의 빈 파일을 만들 수 있습니다.
2. 파일 내용을 바꾸지 않고 타임스탬프를 갱신할 수 있습니다.
3. 접근 시간 또는 수정 시간을 선택할 수 있습니다.
4. 특정 시간을 설정하거나 참조 파일의 시간을 복사할 수 있습니다.
5. 없는 파일이 생성되지 않게 할 수 있습니다.
