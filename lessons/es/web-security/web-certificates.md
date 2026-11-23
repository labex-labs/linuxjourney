---
lesson_id: "web-certificates"
course_id: "web-security"
lang: "es"
order_index: 3
title: "Certificados"
description: "Aprende a comprobar el nombre, las fechas de validez y el emisor de un certificado TLS."
meta_title: "Certificados - Seguridad web"
meta_description: "Aprende a comprobar el nombre, las fechas de validez y el emisor de un certificado TLS."
meta_keywords: "certificados, seguridad web, ciberseguridad, Linux Journey"
---

Un navegador necesita confirmar que se ha conectado al sitio web indicado en la URL. Un **certificado** TLS incluye una identidad y una clave pública. El navegador comprueba varias propiedades antes de confiar en esa identidad.

## Revisar los nombres

Abre la página del [certificado público de prácticas](https://github.com/labex-labs/linuxjourney/blob/master/examples/web-security/site-cert.pem) en GitHub y guarda el archivo como `site-cert.pem`. Es un ejemplo autofirmado para aprender. Usa OpenSSL para mostrar el emisor, las fechas de validez y los nombres alternativos del sujeto. La opción `-noout` omite el certificado codificado.

```bash
$ openssl x509 -in site-cert.pem -noout -issuer -dates -ext subjectAltName
```

La sección de **nombres alternativos del sujeto** enumera los nombres DNS cubiertos por el ejemplo. Busca `DNS:site.example`. Un navegador compara el nombre de la URL con los nombres del certificado.

:::single-choice{#web-certificates-wrong-name} El único nombre de la lista es site.example. ¿Qué URL coincide con ese nombre?

::option[https://site.example/.]{#web-certificates-wrong-name-b .correct explanation="El nombre DNS del certificado coincide con el nombre del equipo en la URL."}
::option[https://other.example/.]{#web-certificates-wrong-name-a explanation="El certificado de ejemplo indica un nombre distinto."}
::option[https://preview.site.example/.]{#web-certificates-wrong-name-c explanation="Un subdominio es un nombre distinto, salvo que el certificado también lo cubra."}
:::

![Salida registrada de OpenSSL con el emisor, las fechas y el nombre DNS site.example del certificado de prácticas](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-certificates/dns-name-and-validity.png)

## Comprobar las fechas

`notBefore` y `notAfter` delimitan el periodo en que puede usarse el certificado. Compara esas fechas con la hora de la prueba. Un problema de reloj también puede afectar a la comprobación. Las fechas por sí solas no bastan para verificar el certificado.

:::single-choice{#web-certificates-validity-period} La hora actual es posterior a notAfter. ¿Qué debes investigar?

::option[Si el nombre DNS correcto aparece en el certificado.]{#web-certificates-validity-period-b explanation="El nombre importa para verificar la identidad. Aunque coincida, un certificado caducado queda fuera de su periodo de validez."}
::option[Si cambió la contraseña de algún usuario.]{#web-certificates-validity-period-c explanation="El inicio de sesión en la aplicación es independiente de la validez del certificado."}
::option[Si el certificado ha caducado y debe renovarse.]{#web-certificates-validity-period-a .correct explanation="El servidor está presentando un certificado fuera del periodo de validez indicado."}
:::

## Comprobar la confianza

El campo **emisor** indica quién firmó el certificado. Los navegadores suelen comprobar las firmas de una cadena de certificados que lleva a una autoridad de confianza. Puedes consultar el campo del emisor que muestra OpenSSL. Verificar la cadena es una operación aparte. Un certificado de prácticas puede estar pensado solo para el laboratorio.

:::single-choice{#web-certificates-trust-check} El nombre y las fechas coinciden, pero el navegador no confía en quien firmó el certificado. ¿Qué falta?

::option[Otra copia de la fecha del certificado.]{#web-certificates-trust-check-a explanation="Que las fechas coincidan no demuestra quién avala la identidad."}
::option[Una cadena válida que lleve a una autoridad de confianza para esta conexión.]{#web-certificates-trust-check-c .correct explanation="El navegador necesita poder confiar en la cadena, además de comprobar el nombre y las fechas."}
::option[Un nombre de usuario distinto en el sitio web.]{#web-certificates-trust-check-b explanation="La comprobación de confianza se realiza antes de la autenticación habitual de la aplicación."}
:::

## Resumen

Ya puedes interpretar tres comprobaciones de un certificado.

1. Comprueba que el nombre del equipo en la URL coincida con un nombre cubierto.
2. Compara la hora actual con las fechas del certificado.
3. Verifica por separado si la cadena conduce a una autoridad de confianza.
