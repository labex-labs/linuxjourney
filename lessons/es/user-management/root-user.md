---
index: 2
lang: "es"
title: "Raíz"
meta_title: "Raíz - Gestión de Usuarios"
meta_description: "Explora el rol del usuario root en Linux. Esta lección cubre las diferencias entre su y sudo para obtener privilegios de superusuario y explica cómo el archivo /etc/sudoers gestiona el acceso."
meta_keywords: "usuario root en linux, usuario root linux, su, sudo, sudoers, visudo, superusuario, gestión de usuarios, permisos linux"
---

## Lesson Content

En Linux, ciertas tareas administrativas requieren privilegios elevados. Estos privilegios pertenecen a una cuenta especial conocida como el **usuario root en Linux**. Aunque puedes iniciar sesión directamente como root, a menudo es más seguro y manejable obtener acceso de superusuario temporalmente.

### El Comando `su`

Además del comando `sudo`, puedes usar `su` (sustituir usuario) para obtener privilegios de superusuario. Cuando se ejecuta sin un nombre de usuario, `su` intenta abrir una nueva sesión de shell para el **usuario root de linux**, pidiéndote la contraseña de root.

```bash
su
```

También puedes usar este comando para cambiar a cualquier otro usuario en el sistema, siempre que conozcas su contraseña.

### Riesgos de una Shell Root Persistente

Usar `su` para abrir una shell root tiene desventajas significativas. Operar continuamente como usuario root aumenta el riesgo de cometer un error crítico que altere el sistema. Además, las acciones realizadas en una shell root no se registran bajo tu cuenta de usuario personal, lo que dificulta auditar los cambios del sistema. Por estas razones, la mejor práctica es usar `sudo` para comandos individuales que requieran acceso de superusuario.

### El Archivo `sudoers`

Entonces, ¿cómo determina el sistema quién tiene permitido usar `sudo`? El acceso está controlado por un archivo de configuración ubicado en `/etc/sudoers`. Este archivo enumera los usuarios y grupos a los que se les concede permiso para ejecutar comandos como superusuario.

Para editar este archivo de forma segura, siempre debes usar el comando `visudo`. Esta utilidad abre el archivo `sudoers` en un editor de texto y realiza una verificación de sintaxis antes de guardar, lo que ayuda a prevenir errores de configuración que podrían bloquearte el acceso administrativo.

## Exercise

Pon tu conocimiento en práctica. El siguiente laboratorio práctico te ayudará a reforzar tu comprensión del acceso y los privilegios de superusuario:

1. **[Configurar Cuentas de Usuario y Privilegios Sudo en Linux](https://labex.io/es/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Practica la aplicación de políticas de contraseñas, el bloqueo y desbloqueo de cuentas de usuario, la protección de la cuenta root y la concesión de permisos administrativos, lo que se relaciona directamente con la gestión del acceso de superusuario.

Este laboratorio te ayudará a aplicar los conceptos en escenarios reales y a ganar confianza en la gestión de privilegios de usuario y acceso de superusuario.

## Quiz Question

¿Qué archivo enumera los usuarios y grupos con privilegios de `sudo`? Por favor, proporciona la ruta completa. (Nota: Tu respuesta debe estar en inglés y distingue entre mayúsculas y minúsculas).

## Quiz Answer

/etc/sudoers
