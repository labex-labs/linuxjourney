---
index: 3
lang: "es"
title: "cd (Cambiar Directorio)"
meta_title: "cd (Cambiar Directorio) - Línea de Comandos"
meta_description: "Aprende a usar el comando 'cd' en Linux para navegar por directorios. Comprende las rutas absolutas, relativas y los atajos útiles. ¡Comienza tu viaje en Linux!"
meta_keywords: "comando cd, cambiar directorio, rutas Linux, ruta absoluta, ruta relativa, tutorial Linux, Linux para principiantes, navegación Linux"
---

## Lesson Content

Ahora que sabes dónde estás, veamos si podemos movernos un poco por el sistema de archivos. Recuerda, tendremos que navegar usando rutas. Hay dos formas diferentes de especificar una ruta: con rutas absolutas y relativas.

- Ruta absoluta: Esta es la ruta desde el directorio raíz. La raíz es el jefe. El directorio raíz se muestra comúnmente como una barra (`/`). Cada vez que tu ruta comienza con `/`, significa que estás comenzando desde el directorio raíz. Por ejemplo, `/home/pete/Desktop`.

- Ruta relativa: Esta es la ruta desde donde te encuentras actualmente en el sistema de archivos. Si estuviera en la ubicación `/home/pete/Documents` y quisiera llegar a un directorio dentro de `Documents` llamado `taxes`, no tengo que especificar la ruta completa desde la raíz como `/home/pete/Documents/taxes`; puedo simplemente ir a `taxes/` en su lugar.

Ahora que sabes cómo funcionan las rutas, solo necesitamos algo que nos ayude a cambiar al directorio que queremos. Afortunadamente, tenemos `cd` o "cambiar directorio" para hacer eso.

```bash
cd /home/pete/Pictures
```

Así que ahora he cambiado la ubicación de mi directorio a `/home/pete/Pictures`.

Ahora, desde este directorio, tengo una carpeta dentro llamada `Hawaii`. Puedo navegar a esa carpeta con:

```bash
cd Hawaii
```

¿Notas cómo solo usé el nombre de la carpeta? Es porque ya estaba en `/home/pete/Pictures`.

Puede ser bastante agotador navegar con rutas absolutas y relativas todo el tiempo. Afortunadamente, hay algunos atajos para ayudarte.

- `.` (directorio actual): Este es el directorio en el que te encuentras actualmente.
- `..` (directorio anterior): Te lleva al directorio superior al actual.
- `~` (directorio de inicio): Este directorio por defecto es tu "directorio de inicio", como `/home/pete`.
- `-` (directorio previo): Esto te llevará al directorio anterior en el que estuviste.

```bash
cd .
cd ..
cd ~
cd -
```

¡Pruébalos!

## Exercise

1. Ejecuta el comando `cd` sin ninguna opción. ¿A dónde te lleva?

Para practicar con el comando `cd`, prueba este laboratorio interactivo:

- [Linux cd Command: Directory Changing](https://labex.io/es/labs/linux-linux-cd-command-directory-changing-209733)

## Quiz Question

Si estás en `/home/pete/Pictures` y quieres ir a `/home/pete`, ¿cuál es un buen atajo para usar?

## Quiz Answer

cd ..
