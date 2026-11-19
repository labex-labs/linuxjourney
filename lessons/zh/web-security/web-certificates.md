---
lesson_id: "web-certificates"
course_id: "web-security"
lang: "zh"
order_index: 3
title: "证书"
description: "学习核对 TLS 证书上的名称、有效期和签发者。"
meta_title: "证书 - Web 安全"
meta_description: "用 OpenSSL 查看练习证书，理解名称匹配、有效期和信任链各自要检查什么。"
meta_keywords: "TLS 证书, OpenSSL, 证书有效期, 信任链, Web 安全, Linux Journey"
---

浏览器需要确认自己访问的确实是 URL 指定的网站。TLS **证书**包含身份信息和公钥。浏览器会核对多项属性，之后才判断是否信任该身份。

## 查看证书中的名称

将[练习用公开证书](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/examples/web-security/site-cert.pem)保存为 `site-cert.pem`。这是一张自签名的教学证书。用 OpenSSL 输出签发者、有效期和使用者可选名称。`-noout` 选项会省略编码后的证书正文。

```bash
$ openssl x509 -in site-cert.pem -noout -issuer -dates -ext subjectAltName
```

**使用者可选名称**部分列出了这个示例覆盖的 DNS 名称。找出 `DNS:site.example`。浏览器会把 URL 中的名称与证书中列出的名称进行核对。

:::single-choice{#web-certificates-wrong-name} 列表里只有 site.example。哪个 URL 与这个名称匹配？

::option[https://site.example/]{#web-certificates-wrong-name-b .correct explanation="证书中的 DNS 名称与 URL 的主机部分一致。"}
::option[https://other.example/]{#web-certificates-wrong-name-a explanation="示例证书列出的是另一个名称。"}
::option[https://preview.site.example/]{#web-certificates-wrong-name-c explanation="子域名是另一个名称，只有证书覆盖它时才匹配。"}
:::

![OpenSSL 记录的输出显示练习证书的签发者、有效期和 DNS 名称 site.example](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-certificates/dns-name-and-validity.png)

## 核对有效期

`notBefore` 和 `notAfter` 说明证书可使用的时间范围。把它们与进行检查时的时间对照。设备时钟不准也会影响结果。单凭有效期无法完成证书验证。

:::single-choice{#web-certificates-validity-period} 当前时间已超过 notAfter。应该调查什么？

::option[证书上是否写了正确的 DNS 名称。]{#web-certificates-validity-period-b explanation="名称关系到身份，但即使名称吻合，证书仍可能已经过期。"}
::option[某个用户是否修改了密码。]{#web-certificates-validity-period-c explanation="应用的登录密码与证书有效期无关。"}
::option[证书是否已经过期，需要更新。]{#web-certificates-validity-period-a .correct explanation="端点当前出示的证书已经超出它标注的有效期。"}
:::

## 检查信任关系

**签发者**表示谁签署了证书。浏览器通常会逐级检查签名，直到链条上一个受信任的权威机构。OpenSSL 打印出的签发者名称只是一个可以查看的字段。验证证书链需要另行操作。练习证书可能只供实验使用。

:::single-choice{#web-certificates-trust-check} 名称和有效期都符合要求，但浏览器不信任签发者。缺少什么？

::option[再提供一份证书有效期信息。]{#web-certificates-trust-check-a explanation="有效期吻合无法建立对签发者的信任。"}
::option[这条连接上通往受信任权威机构的有效证书链。]{#web-certificates-trust-check-c .correct explanation="浏览器除了核对名称和有效期，还需要信任这条证书链。"}
::option[网站上的另一个用户名。]{#web-certificates-trust-check-b explanation="通常在应用身份验证之前，浏览器就会判断证书是否可信。"}
:::

## 总结

现在，你可以分别检查证书的三项信息。

1. 将 URL 中的主机名与证书覆盖的名称匹配。
2. 对照当前时间和证书的有效期。
3. 单独检查证书链是否可信。
