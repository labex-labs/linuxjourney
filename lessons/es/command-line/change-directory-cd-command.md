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

- Ruta absoluta: Esta es la ruta desde el directorio raíz. La raíz es el jefe principal. El directorio raíz se muestra comúnmente como una barra (`/`). Cada vez que tu ruta comienza con `/`, significa que estás comenzando desde el directorio raíz. Por ejemplo, `/home/pete/Desktop`.

- Ruta relativa: Esta es la ruta desde donde te encuentras actualmente en el sistema de archivos. Si estuviera en la ubicación `/home/pete/Documents` y quisiera ir a un directorio dentro de `Documents` llamado `taxes`, no tengo que especificar la ruta completa desde la raíz como `/home/pete/Documents/taxes`; puedo simplemente ir a `taxes/` en su lugar.

Ahora que sabes cómo funcionan las rutas, solo necesitamos algo que nos ayude a cambiar al directorio que queremos. Afortunadamente, tenemos `cd` o “cambiar directorio” para hacer eso.

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
- `~` (directorio de inicio): Este directorio por defecto es tu “directorio de inicio”, como `/home/pete`.
- `-` (directorio anterior): Esto te llevará al directorio anterior en el que estuviste.

```bash
cd .
cd ..
cd ~
cd -
```

¡Pruébalos!

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la navegación de directorios en Linux:

1. **[Comando cd de Linux: Cambio de Directorio](https://labex.io/es/labs/linux-linux-cd-command-directory-changing-209733)** - Aprende el comando `cd` de Linux para navegar eficientemente por tu sistema de archivos, incluyendo varias técnicas para cambiar directorios, comprender rutas y explorar la estructura de archivos.
2. **[Navegación de Directorios en Linux](https://labex.io/es/labs/linux-directory-navigation-387844)** - Pon a prueba tus habilidades básicas de línea de comandos de Linux navegando a través de directorios usando comandos esenciales.
3. **[Configuración de una Nueva Estructura de Proyecto](https://labex.io/es/labs/linux-setting-up-a-new-project-structure-387859)** - Practica tus habilidades de gestión de directorios en Linux creando una estructura de proyecto específica y navegando a través de ella usando comandos esenciales como `mkdir` y `cd`.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a construir confianza al navegar por el sistema de archivos de Linux.

## Quiz Question

Si estás en `/home/pete/Pictures` y quieres ir a `/home/pete`, ¿qué atajo es bueno usar?

## Quiz Answer

cd ..
