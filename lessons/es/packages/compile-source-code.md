---
index: 7
lang: "es"
title: "Compilar Código Fuente"
meta_title: "Compilar Código Fuente - Paquetes"
meta_description: "Aprende a compilar código fuente en Linux usando make, configure y checkinstall. Comprende el proceso de construcción para usuarios principiantes e intermedios."
meta_keywords: "compilar código fuente, make install, checkinstall, compilar Linux, build-essential, tutorial Linux, guía para principiantes"
---

## Lesson Content

A menudo, te encontrarás con un paquete oscuro que solo viene en forma de código fuente puro. Necesitarás usar algunos comandos para compilar e instalar ese paquete de código fuente en tu sistema.

Primero lo primero, necesitarás tener software para instalar las herramientas que te permitirán compilar código fuente.

```bash
sudo apt install build-essential
```

Una vez hecho esto, extrae el contenido del archivo del paquete, muy probablemente un archivo `.tar.gz`.

```bash
tar -xzvf package.tar.gz
```

Antes de hacer cualquier cosa, echa un vistazo al archivo `README` o `INSTALL` dentro del paquete. A veces habrá instrucciones de instalación específicas.

Dependiendo del método de compilación que haya utilizado el desarrollador, tendrás que usar diferentes comandos, como `cmake` o algo más.

Sin embargo, lo más común es que veas la compilación básica con `make`, así que hablaremos de eso:

Dentro del contenido del paquete habrá un script `configure`. Este script verifica las dependencias en tu sistema, y si te falta algo, verás un error y tendrás que solucionar esas dependencias.

```bash
./configure
```

El `./` te permite ejecutar un script en el directorio actual.

```bash
make
```

Dentro del contenido del paquete, hay un archivo llamado `Makefile` que contiene reglas para construir el software. Cuando ejecutas el comando `make`, este busca en este archivo para construir el software.

```bash
sudo make install
```

Este comando realmente instala el paquete; copiará los archivos correctos a las ubicaciones correctas en tu computadora.

Si quieres desinstalar el paquete, usa:

```bash
sudo make uninstall
```

Ten cuidado al usar `make install`; es posible que no te des cuenta de cuánto está sucediendo realmente en segundo plano. Si decides eliminar este paquete, es posible que no elimines todo porque no te diste cuenta de lo que se agregó a tu sistema. En su lugar, olvida todo lo que te acabo de explicar sobre `make install` y usa el comando **checkinstall**. Este comando creará un archivo `.deb` para ti que puedes instalar y desinstalar fácilmente.

```bash
sudo checkinstall
```

Este comando esencialmente hará un "make install" y construirá un paquete `.deb` y lo instalará. Esto facilita la eliminación del paquete más adelante.

## Exercise

¡La práctica hace al maestro! Aquí tienes un laboratorio práctico para reforzar tu comprensión de la construcción de software desde el código fuente:

1. **[Construir Software desde el Código Fuente en Linux](https://labex.io/es/labs/comptia-build-software-from-source-code-in-linux-590853)** - Practica el proceso fundamental de construir e instalar software desde su código fuente, incluyendo el uso de `configure`, `make` y `make install`.

Este laboratorio te ayudará a aplicar los conceptos en un escenario real y a generar confianza al compilar software.

## Quiz Question

¿Qué deberías usar en lugar de `make install` SIEMPRE?

## Quiz Answer

checkinstall
