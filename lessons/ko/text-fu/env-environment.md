---
index: 5
lang: "ko"
title: "env (환경)"
meta_title: "env (환경) - Text-Fu"
meta_description: "'env' 명령으로 Linux 환경 변수에 대해 알아보세요. PATH, HOME, USER 변수를 이해하세요. Linux 환경 관리에 대한 초보자 가이드를 얻으세요."
meta_keywords: "env command, Linux 환경 변수, PATH 변수, Linux 튜토리얼, 초보자 Linux, 셸 변수, Linux 가이드"
---

## Lesson Content

다음 명령을 실행하세요:

```bash
echo $HOME
```

홈 디렉토리의 경로가 표시될 것입니다. 제 경우에는 /home/pete와 같습니다.

이 명령은 어떻습니까?

```bash
echo $USER
```

사용자 이름이 표시될 것입니다!

이 정보는 어디에서 오는 걸까요? 환경 변수에서 오는 것입니다. 다음을 입력하여 확인할 수 있습니다:

```bash
env
```

이것은 현재 설정된 환경 변수에 대한 많은 정보를 출력합니다. 이 변수들은 셸과 다른 프로세스들이 사용할 수 있는 유용한 정보를 포함합니다.

다음은 간단한 예시입니다:

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

특히 중요한 변수 중 하나는 PATH 변수입니다. 다음과 같이 변수 이름 앞에 `$`를 붙여 이 변수들에 접근할 수 있습니다:

```bash
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
```

이것은 시스템이 명령을 실행할 때 검색하는 콜론으로 구분된 경로 목록을 반환합니다. 인터넷에서 패키지를 수동으로 다운로드하여 비표준 디렉토리에 설치하고 해당 명령을 실행하고 싶다고 가정해 봅시다. `$ coolcommand`를 입력했는데, 프롬프트에 "command not found"라고 표시됩니다. 이상하죠? 폴더에서 바이너리를 보고 있고 그것이 존재한다는 것을 알고 있습니다. 무슨 일이 일어나고 있는 것이냐면, `$PATH` 변수가 이 바이너리에 대해 해당 디렉토리를 확인하지 않아서 오류를 발생시키는 것입니다.

해당 디렉토리에서 실행하고 싶은 바이너리가 많다고 가정해 봅시다. PATH 변수를 수정하여 해당 디렉토리를 PATH 환경 변수에 포함시킬 수 있습니다.

## Exercise

다음은 무엇을 출력할까요? 그 이유는 무엇일까요?

```bash
echo $HOME
```

## Quiz Question

환경 변수를 어떻게 확인할 수 있나요?

## Quiz Answer

env
