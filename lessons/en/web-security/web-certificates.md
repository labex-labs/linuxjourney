---
lesson_id: "web-certificates"
course_id: "web-security"
lang: "en"
order_index: 3
title: "Certificates"
description: "Learn to check the name, validity dates, and issuer shown by a TLS certificate."
meta_title: "Certificates - Web Security"
meta_description: "Learn to check the name, validity dates, and issuer shown by a TLS certificate."
meta_keywords: "certificates, web security, cybersecurity, Linux Journey"
---

A browser needs evidence that it reached the website named in the URL. A TLS **certificate** includes an identity and a public key. The browser checks several properties before trusting that identity.

## Looking at the Names

Open the [public practice certificate](https://github.com/labex-labs/linuxjourney/blob/master/examples/web-security/site-cert.pem) on GitHub and save the file as `site-cert.pem`. It is a self-signed teaching sample. Use OpenSSL to print the issuer, validity dates, and subject alternative names. The `-noout` option suppresses the encoded certificate.

```bash
$ openssl x509 -in site-cert.pem -noout -issuer -dates -ext subjectAltName
```

The **subject alternative name** section lists the DNS names covered by the sample. Look for `DNS:site.example`. A browser checks the name from its URL against the names in the certificate.

:::single-choice{#web-certificates-wrong-name} The only listed name is site.example. Which URL matches this name?

::option[https://site.example/.]{#web-certificates-wrong-name-b .correct explanation="The DNS name in the certificate matches the URL host."}
::option[https://other.example/.]{#web-certificates-wrong-name-a explanation="The sample certificate lists a different name."}
::option[https://preview.site.example/.]{#web-certificates-wrong-name-c explanation="A subdomain is a separate name unless the certificate covers it."}
:::

![Recorded OpenSSL output showing the practice certificate issuer, dates, and site.example DNS name](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-certificates/dns-name-and-validity.png)

## Checking the Dates

`notBefore` and `notAfter` describe the time range in which the certificate can be used. Compare those dates with the time of your test. A clock problem can also affect the check. Dates alone are insufficient to verify a certificate.

:::single-choice{#web-certificates-validity-period} The current time is after notAfter. What should you investigate?

::option[Whether the correct DNS name appears in the certificate.]{#web-certificates-validity-period-b explanation="The name check matters for identity. A name match leaves an expired certificate outside its validity period."}
::option[Whether a password changed for one user.]{#web-certificates-validity-period-c explanation="Application login is separate from certificate validity."}
::option[Whether the certificate has expired and needs renewal.]{#web-certificates-validity-period-a .correct explanation="The endpoint is presenting a certificate outside its stated validity period."}
:::

## Checking Trust

The **issuer** names who signed the certificate. Browsers normally check signatures along a chain that leads to a trusted authority. The issuer label printed by OpenSSL is a field you can inspect. Verifying the chain is a separate operation. A practice certificate may be intended only for a lab.

:::single-choice{#web-certificates-trust-check} The name and dates match, but the browser does not trust the signer. What is still missing?

::option[A second copy of the certificate date.]{#web-certificates-trust-check-a explanation="Matching dates do not establish who vouches for the identity."}
::option[A valid chain to a trusted authority for this connection.]{#web-certificates-trust-check-c .correct explanation="A browser needs trust in the chain as well as a matching name and valid dates."}
::option[A different username on the website.]{#web-certificates-trust-check-b explanation="The trust decision happens before normal application authentication."}
:::

## Summary

You can now read three useful parts of a certificate check.

1. Match the URL host to a covered name.
2. Compare the current time with the certificate's dates.
3. Treat chain trust as a separate check.
