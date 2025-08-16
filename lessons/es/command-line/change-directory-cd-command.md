---
lang: "es"
title: "cd (Cambiar Directorio)"
description: "Aprende a usar el comando 'cd' en Linux para navegar por directorios. Comprende las rutas absolutas, relativas y atajos útiles. ¡Comienza tu viaje en Linux!"
keywords: "comando cd, cambiar directorio, rutas Linux, ruta absoluta, ruta relativa, tutorial Linux, Linux para principiantes, navegación Linux"
---

## Lesson Content

Ahora que sabes dónde estás, veamos si podemos movernos un poco por el sistema de archivos. Recuerda, necesitaremos navegar usando rutas. Hay dos formas diferentes de especificar una ruta: con rutas absolutas y relativas.

- Ruta absoluta: Esta es la ruta desde el directorio raíz. La raíz es el jefe principal. El directorio raíz se muestra comúnmente como una barra (`/`). Cada vez que tu ruta comienza con `/`, significa que estás comenzando desde el directorio raíz. Por ejemplo, `/home/pete/Desktop`.

- Ruta relativa: Esta es la ruta desde donde te encuentras actualmente en el sistema de archivos. Si estuviera en la ubicación `/home/pete/Documents` y quisiera ir a un directorio dentro de `Documents` llamado `taxes`, no tengo que especificar la ruta completa desde la raíz como `/home/pete/Documents/taxes`; puedo simplemente ir a `taxes/` en su lugar.

Ahora que sabes cómo funcionan las rutas, solo necesitamos algo que nos ayude a cambiar al directorio que queremos. Afortunadamente, tenemos `cd` o “change directory” para hacer eso.

```bash
cd /home/pete/Pictures
```

Así que ahora he cambiado mi ubicación de directorio a `/home/pete/Pictures`.

Ahora, desde este directorio, tengo una carpeta dentro llamada `Hawaii`. Puedo navegar a esa carpeta con:

```bash
cd Hawaii
```

¿Notas cómo solo usé el nombre de la carpeta? Es porque ya estaba en `/home/pete/Pictures`.

Puede ser bastante agotador navegar con rutas absolutas y relativas todo el tiempo. Afortunadamente, hay algunos atajos para ayudarte.

- `.` (current directory): Este es el directorio en el que te encuentras actualmente.
- `..` (previous directory): Te lleva al directorio superior al actual.
- `~` (home directory): Este directorio por defecto es tu “home directory”, como `/home/pete`.
- `-` (previous directory): Esto te llevará al directorio anterior en el que estabas.

```bash
cd .
cd ..
cd ~
cd -
```

¡Pruébalos!

## Exercise

1. Run the `cd` command without any flags. Where does it take you?

## Quiz Question

Si estás en `/home/pete/Pictures` y quieres ir a `/home/pete`, ¿cuál es un buen atajo para usar?

## Quiz Answer

cd ..
