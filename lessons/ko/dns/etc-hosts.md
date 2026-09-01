---
lesson_id: "etc-hosts"
course_id: "dns"
lang: "ko"
order_index: 4
title: "/etc/hosts"
description: "로컬 hosts 파일 매핑이 리눅스 이름 확인에 참여하는 방식과 안전하게 테스트하는 방법을 알아봅니다."
meta_title: "/etc/hosts - DNS"
meta_description: "리눅스 /etc/hosts 파일의 목적을 알아봅니다. 호스트 이름과 IP 주소 매핑, 로컬 이름 확인에서의 역할 및 안전한 설정 방법을 설명합니다."
meta_keywords: "/etc/hosts, 리눅스 hosts, 호스트 이름 매핑, DNS 확인, 리눅스 네트워킹"
---

`/etc/hosts`는 로컬 시스템 이름 서비스 스택에 정적 주소-이름 항목을 제공합니다. 루프백 이름, 부트스트랩 의존성 및 범위가 좁은 테스트에 유용하지만 다른 호스트에 레코드를 게시하거나 DNS를 갱신하지는 않습니다.

## 파일 읽기

한 줄은 IPv4 또는 IPv6 주소로 시작하고 하나 이상의 이름이 뒤따릅니다.

```text
127.0.0.1       localhost
192.0.2.25      app-test.example.net app-test
2001:db8::25    app-test-v6.example.net app-test-v6
```

주석은 `#`으로 시작합니다. 일부 도구는 관례상 첫 이름을 정규 이름, 뒤의 이름을 별칭으로 취급하지만 애플리케이션 동작과 확인자 API는 다릅니다. 같은 이름에 중복되거나 충돌하는 항목을 피하십시오.

:::single-choice{#hosts-file-entry-order} 일반적인 `/etc/hosts` 매핑 줄의 처음에는 무엇이 나옵니까?

::option[IP 주소입니다.]{#hosts-file-address-first .correct explanation="같은 줄에서 주소 뒤에 하나 이상의 이름이 옵니다."}
::option[DNS 레코드 TTL입니다.]{#hosts-file-ttl-first explanation="hosts 파일 항목은 DNS TTL 필드를 사용하지 않습니다."}
::option[전송 포트 번호입니다.]{#hosts-file-port-first explanation="이 파일은 응용 포트가 아니라 이름과 주소를 매핑합니다."}
:::

## 확인자 순서

일반적으로 `/etc/nsswitch.conf`에 있는 NSS(Name Service Switch) 설정이 시스템 확인자 함수에서 `files`, DNS, 멀티캐스트 시스템 및 다른 소스를 결합하는 방식을 결정합니다. 흔한 줄은 다음과 같습니다.

```text
hosts: files dns
```

정책을 조사하지 않고 files가 항상 먼저라고 가정하지 마십시오. 애플리케이션이 자체 DNS 라이브러리, 캐시, 프록시 또는 암호화된 확인자를 사용해 시스템 경로를 따르지 않을 수도 있습니다.

:::single-choice{#hosts-file-nss-order} 시스템 확인자가 DNS보다 먼저 `/etc/hosts`를 조회하는지는 무엇이 결정합니까?

::option[`/etc`의 파일 이름 알파벳 순서입니다.]{#hosts-file-alphabetical explanation="파일시스템 목록 순서는 이름 서비스 정책을 정의하지 않습니다."}
::option[Name Service Switch 정책의 소스 순서입니다.]{#hosts-file-nss-policy .correct explanation="hosts 데이터베이스 줄이 일반 libc 확인자 소스 순서를 제어합니다."}
::option[목적지의 TCP 윈도 크기입니다.]{#hosts-file-tcp-window explanation="전송 흐름 제어는 로컬 이름 조회와 관계없습니다."}
:::

## 시스템 확인자를 통해 테스트하기

`getent`로 설정된 시스템 이름 서비스 경로를 사용합니다.

```bash
$ getent ahosts app-test.example.net
```

`dig`는 DNS를 직접 조회하며 일반적으로 `/etc/hosts` 매핑을 보고하지 않습니다. 이 차이는 유용합니다. `getent`는 성공하지만 `dig`는 실패하면 로컬 소스나 확인자 정책 차이를 나타낼 수 있습니다.

:::single-choice{#hosts-file-getent-versus-dig} 일반 시스템 이름 확인에서 hosts 파일 항목이 보이는지 확인하기에 더 적합한 도구는 무엇입니까?

::option[`dig`입니다. 항상 /etc/hosts를 먼저 읽기 때문입니다.]{#hosts-file-dig-first explanation="dig는 DNS 쿼리를 보내고 hosts 파일 조회 경로를 우회합니다."}
::option[`getent ahosts`입니다. 설정된 이름 서비스 소스를 사용하기 때문입니다.]{#hosts-file-getent .correct explanation="많은 네이티브 애플리케이션이 사용하는 확인자 경로를 반영합니다."}
::option[`ip route flush`입니다. 모든 이름을 다시 만들기 때문입니다.]{#hosts-file-flush-route explanation="경로 플러시는 파괴적이며 hosts 파일 조회와 관계없습니다."}
:::

## 안전하게 편집하기

필요한 localhost 및 호스트 신원 항목을 보존하고 의도한 주소를 검증하며 권한 있는 편집 도구로 복구 가능한 변경을 수행합니다. 가벼운 테스트를 위해 실제 공용 도메인을 덮어쓰지 마십시오. 자격 증명이나 애플리케이션 트래픽이 예기치 않게 다른 곳으로 갈 수 있습니다. 전용 테스트 이름을 사용하고 실험 후 항목을 제거합니다.

편집 후에는 애플리케이션이 캐시를 유지하거나 다른 확인자를 사용할 수 있으므로 정확한 애플리케이션을 테스트합니다. 영구적인 재정의는 목적보다 오래 조용히 남지 않도록 문서화하십시오.

:::single-choice{#hosts-file-test-name} 공용 서비스 이름을 덮어쓰지 않고 전용 테스트 이름을 사용해야 하는 이유는 무엇입니까?

::option[공용 이름에는 점을 넣을 수 없기 때문입니다.]{#hosts-file-public-no-dots explanation="도메인 이름은 일반적으로 점으로 구분된 여러 레이블을 포함합니다."}
::option[전용 이름이 권위 DNS 영역을 자동으로 만들기 때문입니다.]{#hosts-file-auto-zone explanation="hosts 파일 항목은 로컬에 남으며 영역을 게시하지 않습니다."}
::option[실제 트래픽이나 자격 증명이 다른 곳으로 향할 위험을 줄이기 위해서입니다.]{#hosts-file-reduce-redirection .correct explanation="로컬 재정의는 해당 공용 이름을 사용하는 모든 시스템 확인자 클라이언트에 영향을 줄 수 있습니다."}
:::

## 확인자 서버 설정

`/etc/resolv.conf`는 전통적으로 DNS 확인자 설정을 나열하지만 흔히 NetworkManager, systemd-resolved, DHCP 또는 다른 관리자가 생성합니다. 심볼릭 링크와 파일 주석을 조사한 뒤 덮어써질 생성 출력 대신 소유하는 설정 소스를 변경하십시오.

:::single-choice{#hosts-file-resolv-owner} `/etc/resolv.conf`를 편집하기 전에 무엇을 해야 합니까?

::option[`/etc/hosts`와 모든 네트워크 경로를 삭제합니다.]{#hosts-file-delete-state explanation="관련 없는 파괴적 변경이며 연결을 제거할 수 있습니다."}
::option[모든 배포판이 영구 설정을 그 파일에 직접 저장한다고 가정합니다.]{#hosts-file-assume-direct explanation="많은 시스템이 파일을 동적으로 생성하거나 관리되는 스텁에 연결합니다."}
::option[다른 서비스가 파일을 생성하고 소유하는지 확인합니다.]{#hosts-file-identify-resolver-owner .correct explanation="영구 DNS 서버 변경은 활성 관리자의 설정에서 해야 합니다."}
:::

## 요약

이제 `/etc/hosts`를 통제된 로컬 확인자 입력으로 사용할 수 있습니다.

1. 의도한 이름과 별칭을 주소 뒤에 씁니다.
2. Name Service Switch 순서를 가정하지 말고 조사합니다.
3. `getent`로 시스템 확인을, `dig`로 DNS를 별도 테스트합니다.
4. 전용 임시 이름을 사용하고 실제 애플리케이션을 검증합니다.
5. 설정 소유자를 통해 확인자 서버를 변경합니다.
