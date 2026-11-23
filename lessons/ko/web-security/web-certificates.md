---
lesson_id: "web-certificates"
course_id: "web-security"
lang: "ko"
order_index: 3
title: "인증서"
description: "TLS 인증서에 표시된 이름, 유효 기간, 발급자를 확인하는 방법을 알아봅니다."
meta_title: "인증서 - 웹 보안"
meta_description: "TLS 인증서에 표시된 이름, 유효 기간, 발급자를 확인하는 방법을 알아봅니다."
meta_keywords: "인증서, 웹 보안, 사이버 보안, Linux Journey"
---

브라우저는 URL에 적힌 웹사이트에 실제로 도달했는지 확인해야 합니다. TLS **인증서**에는 신원 정보와 공개 키가 들어 있습니다. 브라우저는 그 신원을 신뢰하기 전에 여러 속성을 확인합니다.

## 인증서에 포함된 이름 확인하기

GitHub에서 [공개 실습용 인증서](https://github.com/labex-labs/linuxjourney/blob/master/examples/web-security/site-cert.pem) 페이지를 열고 파일을 `site-cert.pem`으로 저장하세요. 이 파일은 자체 서명한 교육용 샘플입니다. OpenSSL을 사용해 발급자, 유효 기간, 주체 대체 이름을 출력합니다. `-noout` 옵션은 인코딩된 인증서의 출력을 생략합니다.

```bash
$ openssl x509 -in site-cert.pem -noout -issuer -dates -ext subjectAltName
```

**주체 대체 이름** 항목에는 예시 인증서가 적용되는 DNS 이름이 나옵니다. `DNS:site.example`을 찾아보세요. 브라우저는 URL의 호스트 이름을 인증서의 이름과 비교합니다.

:::single-choice{#web-certificates-wrong-name} 인증서에 나열된 이름이 site.example 하나뿐입니다. 어느 URL이 이 이름과 일치하나요?

::option[`https://site.example/`]{#web-certificates-wrong-name-b .correct explanation="인증서의 DNS 이름과 URL의 호스트가 일치합니다."}
::option[`https://other.example/`]{#web-certificates-wrong-name-a explanation="예시 인증서에는 다른 이름이 표시되어 있습니다."}
::option[`https://preview.site.example/`]{#web-certificates-wrong-name-c explanation="인증서가 해당 하위 도메인을 포함하지 않으면 별개의 이름으로 처리합니다."}
:::

![실습 인증서의 발급자, 유효 기간, DNS 이름 site.example을 보여 주는 OpenSSL 출력](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-certificates/dns-name-and-validity.png)

## 유효 기간 확인하기

`notBefore`와 `notAfter`는 인증서를 사용할 수 있는 기간을 나타냅니다. 두 시각을 검사 시점과 비교하세요. 시스템 시계에 문제가 있으면 검사에도 영향을 줄 수 있습니다. 인증서를 검증하려면 유효 기간 외에도 확인할 사항이 있습니다.

:::single-choice{#web-certificates-validity-period} 현재 시각이 notAfter를 지났습니다. 무엇을 확인해야 하나요?

::option[인증서에 올바른 DNS 이름이 들어 있는지 확인합니다.]{#web-certificates-validity-period-b explanation="이름 확인은 신원을 검증하는 데 필요하지만 이름이 일치해도 만료된 인증서의 유효 기간은 달라지지 않습니다."}
::option[어느 사용자의 비밀번호가 바뀌었는지 확인합니다.]{#web-certificates-validity-period-c explanation="애플리케이션 로그인과 인증서의 유효 기간은 별개입니다."}
::option[인증서가 만료되어 갱신해야 하는지 확인합니다.]{#web-certificates-validity-period-a .correct explanation="엔드포인트가 표시된 유효 기간을 벗어난 인증서를 제시하고 있습니다."}
:::

## 신뢰 관계 확인하기

**발급자**는 인증서에 서명한 주체를 나타냅니다. 보통 브라우저는 신뢰하는 인증 기관에 이르는 체인을 따라 서명을 검증합니다. OpenSSL 출력에서 발급자 이름을 읽을 수 있습니다. 체인 검증은 별도 작업입니다. 실습용 인증서는 실습 환경에서만 사용하도록 만든 것일 수 있습니다.

:::single-choice{#web-certificates-trust-check} 이름은 일치하고 유효 기간에도 문제가 없지만 브라우저가 서명자를 신뢰하지 않습니다. 무엇이 더 필요한가요?

::option[유효 기간을 적은 사본 한 개가 더 필요합니다.]{#web-certificates-trust-check-a explanation="날짜가 일치해도 누가 신원을 보증하는지는 확인할 수 없습니다."}
::option[이 연결에 대해 신뢰할 수 있는 인증 기관으로 이어지는 유효한 체인이 필요합니다.]{#web-certificates-trust-check-c .correct explanation="브라우저는 이름의 일치와 유효 기간뿐 아니라 체인의 신뢰성도 확인해야 합니다."}
::option[웹사이트에서 다른 사용자 이름이 필요합니다.]{#web-certificates-trust-check-b explanation="인증서의 신뢰 여부는 일반적인 애플리케이션 인증 전에 판단합니다."}
:::

## 요약

이제 인증서를 확인하는 데 필요한 세 가지 항목을 읽을 수 있습니다.

1. URL의 호스트와 인증서가 적용되는 이름을 비교합니다.
2. 현재 시각을 인증서의 유효 기간과 비교합니다.
3. 인증서 체인의 신뢰 여부를 별도로 확인합니다.
