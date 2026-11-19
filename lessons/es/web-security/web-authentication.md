---
lesson_id: "web-authentication"
course_id: "web-security"
lang: "es"
order_index: 4
title: "Autenticación"
description: "Aprende cómo un servicio web verifica la identidad y por qué dos factores pueden aportar pruebas distintas."
meta_title: "Autenticación - Seguridad web"
meta_description: "Aprende cómo un servicio web verifica la identidad y por qué dos factores pueden aportar pruebas distintas."
meta_keywords: "autenticación, seguridad web, ciberseguridad, Linux Journey"
---

La **autenticación** es el paso en el que se comprueba la identidad que dice tener un usuario. Un formulario de inicio de sesión puede pedir un nombre de cuenta y una contraseña. El nombre indica la identidad solicitada. La contraseña aporta una prueba que el servicio puede comprobar.

## Identificar la cuenta solicitada

Imagina que un usuario introduce el nombre de cuenta `alex`. Cualquiera que conozca ese nombre puede escribirlo. El servicio verifica la prueba que recibe según los datos y la política de esa cuenta.

:::single-choice{#web-authentication-username-claim} ¿Qué dato indica a qué cuenta intenta acceder el usuario?

::option[El resultado de la comprobación de la contraseña.]{#web-authentication-username-claim-a explanation="Ese resultado sirve para aceptar o rechazar la identidad declarada."}
::option[El nombre de la cuenta.]{#web-authentication-username-claim-b .correct explanation="Le indica al servicio qué identidad debe verificar."}
::option[El formato de respuesta de la página de inicio.]{#web-authentication-username-claim-c explanation="El tipo de contenido no guarda relación con la identidad de quien inicia sesión."}
:::

## Comparar factores de autenticación

Un **factor** es una categoría de prueba. Una contraseña es algo que el usuario sabe. Una llave de seguridad registrada aporta una prueba de algo que el usuario posee. Usar una contraseña y una llave registrada proporciona dos tipos de prueba.

:::single-choice{#web-authentication-independent-factors} ¿Qué ejemplo combina algo que el usuario sabe con algo que posee?

::option[Una contraseña y una llave de seguridad registrada.]{#web-authentication-independent-factors-a .correct explanation="Una comprueba que el usuario conoce la contraseña y la otra que tiene acceso a la llave."}
::option[Una contraseña y otra contraseña memorizada.]{#web-authentication-independent-factors-b explanation="Ambas son cosas que el usuario sabe."}
::option[Un nombre de usuario y el título de una página.]{#web-authentication-independent-factors-c explanation="Estas etiquetas apenas aportan pruebas sobre la identidad."}
:::

## Entender qué demuestra una autenticación correcta

Tras verificar la prueba, el servicio puede permitir que el usuario inicie una sesión. La comprobación de identidad establece qué cuenta considera el servicio que ha iniciado sesión. Para decidir qué puede hacer esa cuenta, el servicio aplica sus reglas de acceso a las peticiones de recursos concretos.

:::single-choice{#web-authentication-auth-limit} Una cuenta ha iniciado sesión correctamente y solicita una página de administración. ¿Qué debe pasar ahora?

::option[Toda cuenta que haya iniciado sesión debe recibir la página automáticamente.]{#web-authentication-auth-limit-a explanation="La cuenta sigue necesitando el permiso que exige esa página."}
::option[El título original de la página debe determinar el acceso.]{#web-authentication-auth-limit-b explanation="Los títulos no indican los permisos de un usuario."}
::option[La aplicación debe comprobar si esa cuenta tiene acceso al recurso.]{#web-authentication-auth-limit-c .correct explanation="Verificar la identidad y decidir el acceso a un recurso son comprobaciones distintas."}
:::

## Resumen

Ya puedes explicar qué establece una decisión de autenticación.

1. Distingue la identidad declarada de la prueba que la respalda.
2. Reconoce dos tipos distintos de factores de autenticación.
3. Consulta la política de autorización del servicio para decidir el acceso a cada recurso.
