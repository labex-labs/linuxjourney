---
lesson_id: "web-certificates"
course_id: "web-security"
lang: "pt"
order_index: 3
title: "Certificados"
description: "Aprenda a verificar o nome, as datas de validade e o emissor de um certificado TLS."
meta_title: "Certificados - Segurança web"
meta_description: "Aprenda a verificar o nome, as datas de validade e o emissor de um certificado TLS."
meta_keywords: "certificados TLS, validade, segurança web, cibersegurança, Linux Journey"
---

Um navegador precisa de evidências de que chegou ao site indicado na URL. Um **certificado** TLS inclui uma identidade e uma chave pública. O navegador verifica várias propriedades antes de confiar nessa identidade.

## Examinando os nomes

Salve o [certificado público de prática](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/examples/web-security/site-cert.pem) como `site-cert.pem`. Ele é um exemplo didático autoassinado. Use o OpenSSL para exibir o emissor, as datas de validade e os nomes alternativos do titular. A opção `-noout` omite o certificado codificado.

```bash
$ openssl x509 -in site-cert.pem -noout -issuer -dates -ext subjectAltName
```

A seção de **nomes alternativos do titular** lista os nomes DNS que o exemplo cobre. Procure `DNS:site.example`. O navegador compara o nome da URL com os nomes do certificado.

:::single-choice{#web-certificates-wrong-name} O único nome listado é site.example. Qual URL corresponde a esse nome?

::option[https://site.example/.]{#web-certificates-wrong-name-b .correct explanation="O nome DNS do certificado corresponde ao host da URL."}
::option[https://other.example/.]{#web-certificates-wrong-name-a explanation="O certificado de exemplo lista outro nome."}
::option[https://preview.site.example/.]{#web-certificates-wrong-name-c explanation="Um subdomínio é um nome distinto, a menos que o certificado também o cubra."}
:::

![Saída do OpenSSL mostrando o emissor, as datas e o nome DNS site.example no certificado de prática](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-certificates/dns-name-and-validity.png)

## Verificando as datas

Os campos `notBefore` e `notAfter` indicam o intervalo em que o certificado pode ser usado. Compare as datas com o horário do teste. Um relógio incorreto também pode afetar a verificação. As datas, por si só, são insuficientes para validar um certificado.

:::single-choice{#web-certificates-validity-period} O horário atual é posterior a notAfter. O que você deve investigar?

::option[Se o nome DNS correto aparece no certificado.]{#web-certificates-validity-period-b explanation="A verificação do nome importa para a identidade. A correspondência do nome não prolonga a validade do certificado."}
::option[Se a senha de um usuário mudou.]{#web-certificates-validity-period-c explanation="O login na aplicação é independente da validade do certificado."}
::option[Se o certificado expirou e precisa ser renovado.]{#web-certificates-validity-period-a .correct explanation="O endpoint está apresentando um certificado fora do prazo de validade informado."}
:::

## Verificando a confiança

O **emissor** identifica quem assinou o certificado. Normalmente, o navegador verifica as assinaturas de uma cadeia que leva a uma autoridade confiável. O nome do emissor exibido pelo OpenSSL é um campo que você pode inspecionar. Verificar a cadeia exige outra operação. Um certificado de prática pode se destinar apenas ao laboratório.

:::single-choice{#web-certificates-trust-check} O nome e as datas estão corretos, mas o navegador não confia em quem assinou o certificado. O que ainda falta?

::option[Uma segunda cópia da data do certificado.]{#web-certificates-trust-check-a explanation="A correspondência das datas não comprova quem atesta a identidade."}
::option[Uma cadeia válida até uma autoridade confiável para essa conexão.]{#web-certificates-trust-check-c .correct explanation="O navegador precisa confiar na cadeia, além de confirmar o nome e as datas."}
::option[Outro nome de usuário no site.]{#web-certificates-trust-check-b explanation="A decisão de confiança ocorre antes da autenticação normal na aplicação."}
:::

## Resumo

Agora você consegue interpretar três partes da verificação de um certificado.

1. Compare o host da URL com os nomes cobertos.
2. Compare o horário atual com as datas do certificado.
3. Verifique a confiança na cadeia à parte.
