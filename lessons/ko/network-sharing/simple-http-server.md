---
lesson_id: "simple-http-server"
course_id: "network-sharing"
lang: "ko"
order_index: 3
title: "간단한 HTTP 서버"
description: "Python HTTP 서버로 통제된 디렉터리를 임시로 공개하는 방법을 알아봅니다."
meta_title: "간단한 HTTP 서버 - 네트워크 공유"
meta_description: "Python의 http.server 모듈로 리눅스에서 간단한 HTTP 서버를 빠르게 구성하고 네트워크에서 파일을 공유하는 방법을 알아봅니다."
meta_keywords: "리눅스 간단한 HTTP 서버, 리눅스 웹 서버, python http.server, 파일 공유, 네트워크 서버"
---

Python의 `http.server` 모듈은 단기 테스트나 신뢰할 수 있는 전송을 위해 정적 파일을 제공할 수 있습니다. 프로덕션 웹 서버가 아니며 인증, 권한 부여, TLS, 속도 제한 또는 적대적 트래픽에 대한 강화된 처리를 제공하지 않습니다.

## 공유 디렉터리 준비하기

공개하려는 파일만 담은 전용 디렉터리를 만듭니다. 시작 전에 숨김 파일, 심볼릭 링크, 권한 및 민감한 메타데이터를 검토하십시오. 홈 디렉터리, 저장소 루트, 자격 증명 디렉터리 또는 시스템 경로는 제공하지 마십시오.

공유 루트를 명시하려면 `--directory`를 사용합니다.

```bash
$ python3 -m http.server 8000 --directory /srv/temporary-share
```

인덱스 파일이 없으면 모듈은 일반적으로 디렉터리 목록을 생성합니다. 리스너에 도달할 수 있는 사람은 누구나 제공되는 내용을 열거하고 내려받을 수 있습니다.

:::single-choice{#http-server-directory-option}
`--directory /srv/temporary-share`를 사용하는 이유는 무엇입니까?

::option[모든 HTTP 응답을 자동으로 암호화합니다.]{#http-server-directory-tls explanation="디렉터리 옵션은 TLS를 추가하지 않습니다."}
::option[다운로드 사용자마다 계정을 만듭니다.]{#http-server-directory-accounts explanation="기본 모듈은 사용자 인증을 제공하지 않습니다."}
::option[의도한 문서 루트를 명시합니다.]{#http-server-explicit-root .correct explanation="검토한 루트를 명시하면 실수로 현재 작업 디렉터리의 파일을 노출할 가능성이 줄어듭니다."}
:::

## 수신 주소 제어하기

같은 호스트만 연결해야 한다면 루프백에 바인딩합니다.

```bash
$ python3 -m http.server 8000 --bind 127.0.0.1 --directory /srv/temporary-share
```

신뢰할 수 있는 네트워크에서 공유하려면 적절한 인터페이스 주소에 의도적으로 바인딩하고 방화벽 정책을 확인합니다. 제한적인 바인딩 없이 실행하면 일반적으로 사용 가능한 모든 인터페이스에서 수신하므로 의도한 네트워크 밖에 디렉터리가 노출될 수 있습니다.

:::single-choice{#http-server-loopback-bind}
`127.0.0.1`에 바인딩한 서버에는 일반적으로 누가 접근할 수 있습니까?

::option[같은 호스트의 클라이언트입니다.]{#http-server-local-clients .correct explanation="루프백 바인딩은 로컬 테스트나 의도적으로 설정한 터널 뒤에서 사용하기에 적합합니다."}
::option[공용 인터넷의 모든 호스트입니다.]{#http-server-public explanation="루프백은 같은 네트워크 네임스페이스에만 속하며 공용 인터페이스가 아닙니다."}
::option[Bluetooth로 연결된 장치만 접근할 수 있습니다.]{#http-server-bluetooth explanation="이 주소는 Bluetooth 전송과 관계없습니다."}
:::

## 접근 테스트하기

서버를 실행하는 호스트에서 알려진 파일을 요청하고 응답을 검사합니다.

```bash
$ curl -f http://127.0.0.1:8000/example.txt
```

승인된 원격 테스트에는 루프백 대신 선택한 인터페이스 주소를 사용합니다. 의도한 파일에 접근할 수 있는지와 문서 루트 밖의 파일에는 접근할 수 없는지를 모두 확인합니다. 브라우저에서 성공했다는 사실만으로 적절한 공개 범위나 기밀성이 입증되지는 않습니다.

:::single-choice{#http-server-default-port-command}
`python3 -m http.server 8000`에서 명시적으로 선택한 포트는 무엇입니까?

::option[22]{#http-server-port-22 explanation="포트 22는 보통 SSH와 연결되며 여기서는 선택하지 않았습니다."}
::option[8000]{#http-server-port-8000 .correct explanation="위치 포트 피연산자가 모듈이 수신할 위치를 지정합니다."}
::option[443]{#http-server-port-443 explanation="이 명령은 포트 443에 HTTPS를 설정하지 않습니다."}
:::

## 중지 및 정리하기

감독하는 터미널에서 임시 서비스를 실행하고 전송이 끝나면 `Ctrl-C`로 중지합니다. 리스너가 사라졌는지 확인합니다.

```bash
$ ss -ltn 'sport = :8000'
```

데이터 처리 정책에 따라 임시 사본을 제거하고 임시 방화벽 규칙을 되돌립니다. 영구적이거나 인증이 필요하거나 인터넷에 공개되는 배포에는 접근 제어와 TLS가 설정된 유지 관리형 서버를 사용하십시오.

:::single-choice{#http-server-completion-check}
임시 전송이 완료된 뒤 무엇을 해야 합니까?

::option[서버를 중지하고 포트가 더 이상 수신 중이 아닌지 확인합니다.]{#http-server-stop-verify .correct explanation="검증을 통해 임시 네트워크 서비스가 실제로 종료됐음을 확인합니다."}
::option[나중에 누군가 필요할 수 있으므로 리스너를 계속 실행합니다.]{#http-server-leave-running explanation="승인된 목적이 끝나면 불필요한 노출을 제거해야 합니다."}
::option[문서 루트에 개인 파일을 더 복사합니다.]{#http-server-add-private explanation="의도적으로 공유하는 내용만 제공 디렉터리에 있어야 합니다."}
:::

## 요약

이제 공개 범위를 제한한 임시 Python HTTP 서버를 실행할 수 있습니다.

1. 검토한 전용 디렉터리만 제공합니다.
2. 가능한 가장 좁고 적절한 주소에 바인딩합니다.
3. 의도한 접근과 의도하지 않은 경계를 테스트합니다.
4. 이후 리스너를 중지하고 임시 접근을 정리합니다.
